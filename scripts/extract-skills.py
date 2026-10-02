#!/usr/bin/env python3
"""
extract-skills.py — Build site/prompts.json from SKILL.md files and knowledge/workflows/*.md

No external dependencies — stdlib only.

Usage:
    python scripts/extract-skills.py
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).parent.parent
PLUGINS_DIR = REPO_ROOT / "plugins"
WORKFLOWS_DIR = REPO_ROOT / "knowledge" / "workflows"
OUTPUT_FILE = REPO_ROOT / "site" / "prompts.json"

PLUGIN_CATEGORIES = {
    "eu-legislative": "Legislative & Policy",
    "eu-competition": "Competition & Legal Service",
    "eu-institutional-management": "Institutional Management",
    "eu-trade": "Trade Defence",
    "eu-grants-enforcement": "Grants, Procurement & Enforcement",
    "eu-data-communication": "Data & Communication",
    "eu-simulation": "EU Institutional Simulation",
    "eu-privacy": "Data Protection & Privacy",
    "eu-careers": "EU Careers & EPSO",
}

ACRONYMS = {
    "dpia", "dpo", "cdr", "pmo", "isc", "pq", "lfn", "gber", "eu", "ep", "olaf", "hod", "epso",
    "eppo", "tia", "edps", "sme", "aar", "amp", "hr", "ai", "it", "ta", "digit", "sg",
}
MIXED_CASE = {"ropa": "RoPA"}
SKIP_SKILLS = {"cold-start-interview"}

# Sections that are internal/Claude-Code-specific — dropped from the prompt body.
# Only the section itself is removed; the sections after it are kept.
BODY_DROP_SECTIONS = (
    "## Output Template",
    "## Knowledge Reference",
)
# A Reference Guide is dropped only when it is a table of local files to load
# (useless outside Claude Code); a table of legal provisions is kept.
REFERENCE_GUIDE_HEADING = "## Reference Guide"
LOCAL_FILE_POINTER = re.compile(r"`[^`\n]*(?:references|knowledge)/[^`\n]*`|\|\s*Load when\s*\|", re.IGNORECASE)

COMPLEX_FORMATS = {
    "swd-impact-assessment",
    "dpia-report-art-39-7-eudpr",
    "legislative-proposal",
    "college-meeting-record",
    "trilogue-compromise-text",
    "ep-committee-report",
    "multi-phase-workflow",
}


# ── YAML frontmatter parser (stdlib, handles our SKILL.md structure) ──────────

def _consume_folded(lines: list[str], start: int, indent: str) -> tuple[str, int]:
    chunks, j = [], start
    while j < len(lines) and lines[j].startswith(indent):
        chunks.append(lines[j].strip())
        j += 1
    return " ".join(chunks), j


def _consume_multiline(first: str, lines: list[str], start: int, indent: str) -> tuple[str, int]:
    parts, j = ([first] if first else []), start
    while j < len(lines) and lines[j].startswith(indent):
        parts.append(lines[j].strip())
        j += 1
    return " ".join(p for p in parts if p), j


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter delimited by ---."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text

    fm_lines = text[4:end].split("\n")
    body = text[end + 4:].strip()
    n = len(fm_lines)

    data: dict = {}
    meta: dict = {}
    i = 0
    in_meta = False

    while i < n:
        line = fm_lines[i]

        if not line.strip():
            i += 1
            continue

        if in_meta:
            if not line.startswith(" "):
                in_meta = False
                continue  # re-process this line as top-level without incrementing

            if line.startswith("  ") and not line.startswith("   ") and ":" in line:
                mk, _, mv = line.strip().partition(":")
                mk, mv = mk.strip(), mv.strip()
                if mv == ">":
                    val, i = _consume_folded(fm_lines, i + 1, "    ")
                    meta[mk] = val
                else:
                    val, i = _consume_multiline(mv, fm_lines, i + 1, "    ")
                    meta[mk] = val.strip("\"'")
            else:
                i += 1

        else:
            if not line.startswith(" ") and ":" in line:
                key, _, val = line.partition(":")
                key, val = key.strip(), val.strip()

                if key == "metadata":
                    in_meta = True
                    i += 1
                elif val == ">":
                    v, i = _consume_folded(fm_lines, i + 1, "  ")
                    data[key] = v
                else:
                    data[key] = val.strip("\"'")
                    i += 1
            else:
                i += 1

    data["metadata"] = meta
    return data, body


# ── Helpers ───────────────────────────────────────────────────────────────────

def to_title(name: str) -> str:
    def _word(w):
        lw = w.lower()
        if lw in MIXED_CASE: return MIXED_CASE[lw]
        if lw in ACRONYMS: return w.upper()
        return w.title()
    return " ".join(_word(w) for w in name.split("-"))


def infer_difficulty(role: str, output_format: str) -> str:
    if role == "multi-agent":
        return "advanced"
    if output_format in COMPLEX_FORMATS:
        return "advanced"
    return "standard"


# ── Prompt body extraction ────────────────────────────────────────────────────

def split_sections(body: str) -> list[str]:
    """Split a body into its preamble and `## ` sections, ignoring headings inside code fences."""
    sections, current, in_fence = [], [], False
    for line in body.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif line.startswith("## ") and not in_fence:
            sections.append("\n".join(current))
            current = []
        current.append(line)
    sections.append("\n".join(current))
    return sections


def is_dropped_section(section: str) -> bool:
    if section.startswith(BODY_DROP_SECTIONS):
        return True
    return section.startswith(REFERENCE_GUIDE_HEADING) and bool(LOCAL_FILE_POINTER.search(section))


def clean_prompt_body(body: str) -> str:
    """Return the persona+workflow portion of a SKILL.md body — usable in any LLM."""
    # Strip the closing DRAFT block (never one that is followed by further sections)
    body = re.sub(r"\n---\s*\nDRAFT(?:(?!\n## ).)*$", "", body, flags=re.DOTALL)
    # Each section carries the `---` separator that follows it, so dropping one
    # leaves the separators between the remaining sections intact.
    body = "\n".join(s for s in split_sections(body) if not is_dropped_section(s))
    return re.sub(r"(?:\n\s*---\s*)+$", "", body.rstrip()).strip()


# ── Extractors ────────────────────────────────────────────────────────────────

def extract_skill(skill_path: Path, plugin_name: str) -> Optional[dict]:
    text = skill_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if not fm or "name" not in fm:
        return None

    name = fm["name"]
    if name in SKIP_SKILLS:
        return None

    meta = fm.get("metadata", {})
    role = meta.get("role", "specialist")
    scope = meta.get("scope", "")
    output_format = meta.get("output-format", "")

    triggers_raw = meta.get("triggers", "")
    tags = [t.strip() for t in triggers_raw.split(",") if t.strip()][:6]

    related_raw = meta.get("related-skills", "")
    related = [r.strip() for r in related_raw.split(",") if r.strip()]

    trigger = f"/{plugin_name}:{name}"
    if any(k in scope for k in ("assessment", "proposal", "analysis", "orchestration", "dpia")):
        trigger += " <brief>"

    return {
        "id": name,
        "title": to_title(name),
        "description": fm.get("description", "").strip(),
        "plugin": plugin_name,
        "category": PLUGIN_CATEGORIES.get(plugin_name, "Other"),
        "trigger": trigger,
        "tags": tags,
        "role": role,
        "output_format": output_format,
        "scope": scope,
        "related": related,
        "type": "skill",
        "difficulty": infer_difficulty(role, output_format),
        "prompt_body": clean_prompt_body(body),
    }


def extract_workflow(wf_path: Path) -> Optional[dict]:
    text = wf_path.read_text(encoding="utf-8")

    title_m = re.search(r"^# (.+)$", text, re.MULTILINE)
    raw_title = title_m.group(1) if title_m else wf_path.stem.replace("-", " ").title()
    title = raw_title.replace("Workflow: ", "")

    trigger_m = re.search(r"\*\*Trigger:\*\*\s*`([^`]+)`", text)
    trigger = trigger_m.group(1) if trigger_m else f"/{wf_path.stem} <brief>"

    desc_m = re.search(r"## What this workflow does\s*\n+(.+?)(?=\n---|\n##)", text, re.DOTALL)
    description = desc_m.group(1).strip() if desc_m else ""

    phase_count = len(re.findall(r"^## Phase \d+", text, re.MULTILINE))

    return {
        "id": wf_path.stem,
        "title": title,
        "description": description,
        "plugin": "workflows",
        "category": "Guided Workflows",
        "trigger": trigger,
        "tags": [],
        "role": "multi-agent",
        "output_format": "multi-phase-workflow",
        "scope": "workflow",
        "related": [],
        "type": "workflow",
        "difficulty": "advanced" if phase_count >= 4 else "standard",
        "prompt_body": text.strip(),
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    prompts = []  # type: list
    errors = 0

    print("Extracting skills...")
    for plugin_dir in sorted(PLUGINS_DIR.iterdir()):
        if not plugin_dir.is_dir():
            continue
        skills_dir = plugin_dir / "skills"
        if not skills_dir.exists():
            continue
        for skill_dir in sorted(skills_dir.iterdir()):
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.exists():
                continue
            try:
                entry = extract_skill(skill_file, plugin_dir.name)
                if entry:
                    prompts.append(entry)
                    print(f"  + {plugin_dir.name}/{skill_dir.name}")
            except Exception as exc:
                print(f"  ! {plugin_dir.name}/{skill_dir.name}: {exc}", file=sys.stderr)
                errors += 1

    print("\nExtracting workflows...")
    for wf_file in sorted(WORKFLOWS_DIR.glob("*.md")):
        try:
            entry = extract_workflow(wf_file)
            if entry:
                prompts.append(entry)
                print(f"  + workflow/{wf_file.name}")
        except Exception as exc:
            print(f"  ! workflow/{wf_file.name}: {exc}", file=sys.stderr)
            errors += 1

    # Pin "EU Institutional Simulation" first; sort everything else by category then title
    PINNED_CAT = "EU Institutional Simulation"
    prompts.sort(key=lambda p: (0 if p["category"] == PINNED_CAT else 1, p["category"], p["title"]))

    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    now = datetime.now(timezone.utc)
    payload = {
        "generated": now.isoformat(),
        "count": len(prompts),
        "prompts": prompts,
        "footer": {
            "disclaimer": (
                "Independent project — not an official European Commission product "
                "and not affiliated with the European Commission or any EU institution in any way."
            ),
            "website": "https://www.montoyer.com",
            "website_description": "AI agents and prompts for the Brussels quarter",
            "updated": now.strftime("%d/%m/%Y"),
        },
    }
    OUTPUT_FILE.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n{'OK' if not errors else 'DONE (with errors)'}: {len(prompts)} prompts → {OUTPUT_FILE}")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
