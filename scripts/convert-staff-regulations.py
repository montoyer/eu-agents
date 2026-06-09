#!/usr/bin/env python3
"""Convert the EUR-Lex consolidated Staff Regulations HTML into per-Title /
per-Annex markdown reference files.

Source: Consolidated TEXT_ 31962R0031 - EN - 01.01.2026.html  (CELEX 01962R0031)
This is a documentation-tool consolidation with no legal effect; the authentic
text is the OJ version. Generated files carry that disclaimer in their header.

Markers handled (by unicode codepoint, to avoid copy-paste ambiguity):
  ► (BLACK RIGHT-POINTING POINTER)  e.g. M128  -> inline "changed text" start
  ◄ (BLACK LEFT-POINTING POINTER)               -> inline "changed text" end
  ▼ (BLACK DOWN-POINTING TRIANGLE)  e.g. M112  -> block "amended by" band
  ▲ (BLACK UP-POINTING TRIANGLE)                -> block band close
"""
import re, html, os

HERE = os.path.dirname(os.path.abspath(__file__))
REFS = os.path.abspath(os.path.join(
    HERE, "..", "plugins", "eu-institutional-management", "references"))
SRC = os.path.join(REFS, "Consolidated TEXT_ 31962R0031 — EN — 01.01.2026.html")

if not os.path.exists(SRC):
    raise SystemExit(
        f"source HTML not found: {SRC}\n"
        "Download the EUR-Lex consolidated text (CELEX 01962R0031) into that "
        "directory first — the .html source is gitignored by design.")

data = open(SRC, encoding="utf-8", errors="replace").read()

# amendment-marker glyphs, referenced by codepoint
ARROWS = "►◄▼▲"   # pointers + triangles
MARKER_RE = re.compile("[" + ARROWS + r"]\s*[A-Z]?\d*")

def clean_inline(s: str) -> str:
    """Strip tags + amendment markers + footnote stars, unescape entities,
    normalise unicode spaces, collapse whitespace. Wording is preserved."""
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = MARKER_RE.sub("", s)
    s = re.sub(r"—{3,}", "", s)          # em-dash run = deleted provision
    s = re.sub(r"\(\s*\*+\s*\)", "", s)       # ( * ) footnote refs
    # collapse every whitespace + nbsp/thin-space run to one plain space
    s = re.sub(r"[\s     ]+", " ", s)
    s = re.sub(r"\s+([.,;:)])", r"\1", s)   # no space before punctuation
    return s.strip()

def grid_to_md(grid: str) -> str:
    """EUR-Lex lettered/numbered lists are 2-column grids (marker | body)."""
    cells = re.findall(
        r'class="[^"]*grid-list-column-1"[^>]*>(.*?)</div>\s*'
        r'<div[^>]*class="[^"]*grid-list-column-2"[^>]*>(.*?)</div>',
        grid, re.S)
    lines = []
    for marker, body in cells:
        mk, bd = clean_inline(marker), clean_inline(body)
        line = f"{mk} {bd}".strip()
        if line:
            lines.append(line)
    return "\n".join(lines)

def table_to_md(tbl: str) -> str:
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, re.S)
    md, started = [], False
    for row in rows:
        cells = [clean_inline(c) for c in
                 re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)]
        if not any(cells):
            continue
        md.append("| " + " | ".join(cells) + " |")
        if not started:
            md.append("|" + "|".join([" --- "] * len(cells)) + "|")
            started = True
    return ("\n".join(md) + "\n") if md else ""

def find_blocks(html_str: str):
    """Yield (kind, raw) top-level structural elements in document order,
    correctly handling nested <div> (norm divs contain inline-element divs).
    kind in {art, d1, d2, table, grid, norm, p}."""
    i, n = 0, len(html_str)
    tag_open = re.compile(r"<(p|div|table)\b[^>]*>", re.I)
    while i < n:
        m = tag_open.search(html_str, i)
        if not m:
            break
        tag = m.group(1).lower()
        attrs = html_str[m.start():m.end()]
        cls = ""
        cm = re.search(r'class="([^"]*)"', attrs)
        if cm:
            cls = cm.group(1)
        # find the matching close tag, accounting for nesting of same tag
        depth, j = 1, m.end()
        open_re = re.compile(rf"<{tag}\b", re.I)
        close_re = re.compile(rf"</{tag}>", re.I)
        while depth and j < n:
            no = open_re.search(html_str, j)
            nc = close_re.search(html_str, j)
            if nc is None:
                j = n
                break
            if no and no.start() < nc.start():
                depth += 1
                j = no.end()
            else:
                depth -= 1
                j = nc.end()
        inner = html_str[m.end():j - len(f"</{tag}>")]
        # classify
        if tag == "p" and "title-article-norm" in cls:
            yield ("art", inner)
        elif tag == "p" and ("title-division-1" in cls or "title-annex-1" in cls):
            yield ("d1", inner)
        elif tag == "p" and ("title-division-2" in cls or "title-annex-2" in cls):
            yield ("d2", inner)
        elif tag == "table":
            yield ("table", html_str[m.start():j])
        elif tag == "div" and "grid-container" in cls:
            yield ("grid", inner)
        elif tag == "div" and cls.split() == ["norm"]:
            # top-level norm div = one (sub)paragraph; render whole thing
            yield ("norm", html_str[m.start():j])
        elif tag == "p":
            yield ("p", inner)
        # else: skip wrapper divs we don't care about, but descend into them
        if tag == "div" and not (cls.split() == ["norm"] or "grid-container" in cls):
            # recurse into generic wrapper divs to reach inner structure
            yield from find_blocks(inner)
            i = j
            continue
        i = j

def norm_to_md(raw: str) -> str:
    """A <div class='norm'> = a numbered/lettered paragraph: optional
    <span class='no-parag'> marker + body text (possibly in nested divs)."""
    marker = ""
    mm = re.search(r'class="no-parag"[^>]*>(.*?)</span>', raw, re.S)
    if mm:
        marker = clean_inline(mm.group(1))
        raw = raw[:mm.start()] + raw[mm.end():]
    body = clean_inline(raw)
    return f"{marker} {body}".strip()

def block_to_md(block: str) -> str:
    block = re.sub(r"<br\s*/?>", "\n", block, flags=re.I)
    out = []
    for kind, raw in find_blocks(block):
        if kind == "art":
            out.append(f"\n### {clean_inline(raw)}\n")
        elif kind == "d1":
            t = clean_inline(raw)
            if t:
                out.append(f"\n## {t}\n")
        elif kind == "d2":
            t = clean_inline(raw)
            if t:
                out.append(f"\n**{t}**\n")
        elif kind == "table":
            out.append(table_to_md(raw))
        elif kind == "grid":
            g = grid_to_md(raw)
            if g:
                out.append(g)
        elif kind == "norm":
            t = norm_to_md(raw)
            if t:
                out.append(t)
        elif kind == "p":
            t = clean_inline(raw)
            if t:
                out.append(t)
    # annotate articles that have no body (repealed/deleted provisions)
    for i, chunk in enumerate(out):
        if chunk.startswith("\n### Article"):
            nxt = out[i + 1] if i + 1 < len(out) else ""
            if nxt.startswith("\n### ") or nxt.startswith("\n## ") or not nxt:
                out[i] = chunk.rstrip("\n") + "\n\n*(repealed / no longer in force)*\n"
    text = "\n\n".join(x for x in out if x.strip())
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"

# ---- file generation -------------------------------------------------------

DISCLAIMER = (
    "> **Source:** EUR-Lex consolidated text, CELEX `01962R0031`, "
    "consolidation date **01.01.2026**.\n"
    "> A consolidated text is a documentation tool with **no legal effect** — "
    "the authentic version is the one published in the *Official Journal*. "
    "Amendment markers (the change/deletion arrows) have been removed for readability.\n"
    "> **Cite as** `[Staff Regulations Art. XX — EUR-Lex 01962R0031, 01.01.2026]` "
    "(or `[CEOS Art. XX — …]` for Conditions of Employment).\n"
)

# (start_offset, slug, H1 title). end = next start. Offsets from the structural scan.
SECTIONS = [
    (246804,  "title-i-general-provisions",                "Staff Regulations — Title I: General Provisions (Arts. 1–10c)"),
    (296336,  "title-ii-rights-and-obligations",            "Staff Regulations — Title II: Rights and Obligations of Officials (Arts. 11–26a)"),
    (347454,  "title-iii-career",                           "Staff Regulations — Title III: Career of Officials (Arts. 27–53)"),
    (462219,  "title-iv-working-conditions",                "Staff Regulations — Title IV: Working Conditions of Officials (Arts. 55–61)"),
    (492174,  "title-v-emoluments-and-social-security",     "Staff Regulations — Title V: Emoluments and Social Security (Arts. 62–84)"),
    (613033,  "title-vi-disciplinary-measures",             "Staff Regulations — Title VI: Disciplinary Measures (Art. 86; procedure in Annex IX)"),
    (615087,  "title-vii-appeals",                          "Staff Regulations — Title VII: Appeals (Arts. 90–91a)"),
    (628948,  "title-viiia-eeas",                           "Staff Regulations — Title VIIIa: Special Provisions for the EEAS (Arts. 95–99)"),
    (636568,  "title-viiib-third-country",                  "Staff Regulations — Title VIIIb: Officials Serving in a Third Country (Art. 101a; detail in Annex X)"),
    (637658,  "title-ix-transitional-and-final",            "Staff Regulations — Title IX: Transitional and Final Provisions (Arts. 99–110)"),
    # Annex I (pay scales) lives at 649461 and is intentionally skipped — see note below.
    (666193,  "annex-ii-staff-committee-bodies",            "Staff Regulations — Annex II: Composition of Bodies under Article 9"),
    (691834,  "annex-iii-competitions",                     "Staff Regulations — Annex III: Competitions"),
    (713433,  "annex-iv-allowance-arts-41-50",              "Staff Regulations — Annex IV: Allowance under Articles 41 and 50"),
    (738099,  "annex-iva-part-time-work",                   "Staff Regulations — Annex IVa: Part-time Work"),
    (744306,  "annex-v-leave",                              "Staff Regulations — Annex V: Leave"),
    (758713,  "annex-vi-overtime",                          "Staff Regulations — Annex VI: Compensatory Leave and Overtime"),
    (763344,  "annex-vii-remuneration-expenses",            "Staff Regulations — Annex VII: Remuneration and Reimbursement of Expenses"),
    (889793,  "annex-viii-pension-scheme",                  "Staff Regulations — Annex VIII: Pension Scheme"),
    (1014737, "annex-ix-disciplinary",                      "Staff Regulations — Annex IX: Disciplinary Proceedings"),
    (1053675, "annex-x-third-country-staff",                "Staff Regulations — Annex X: Officials Serving in Third Countries"),
    (1092798, "annex-xi-remuneration-update-method",        "Staff Regulations — Annex XI: Method for Updating Remuneration and Pensions"),
    (1134389, "annex-xii-pension-contribution-method",      "Staff Regulations — Annex XII: Pension Contribution Rate Method"),
    (1307403, "annex-xiii-transitional-measures",           "Staff Regulations — Annex XIII: Transitional Measures (incl. XIII.1)"),
    (1725597, "ceos-conditions-of-employment",              "Conditions of Employment of Other Servants (CEOS) — TA, CA, special advisers"),
]
# Note: Annex I (pay scales) already exists as staff-regulations-annex-i-2026.md
#       and is the maintained source for figures; we do not regenerate it here.
END = 2067359   # start of the final CEOS annex block / tail; clip there

# Every top-level structural boundary, in order — used purely to clip each
# slice at the *next* real section even when we skip emitting one (Annex I).
ALL_BOUNDS = sorted(set(
    [s[0] for s in SECTIONS] + [649461, END]   # 649461 = Annex I (skipped)
))

def next_bound(start: int) -> int:
    for b in ALL_BOUNDS:
        if b > start:
            return b
    return END

def main():
    index = []
    for start, slug, h1 in SECTIONS:
        end = next_bound(start)
        body = block_to_md(data[start:end])
        fname = f"staff-regulations-{slug}.md"
        md = f"# {h1}\n\n{DISCLAIMER}\n---\n\n{body}"
        with open(os.path.join(REFS, fname), "w", encoding="utf-8") as fh:
            fh.write(md)
        index.append((fname, h1, len(body)))
        print(f"wrote {fname:52s} {len(body):>7d} chars")
    return index

if __name__ == "__main__":
    main()
