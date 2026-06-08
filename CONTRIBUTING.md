# Contributing to agents-for-EU

This guide covers how to add skills, extend packages, create a new plugin,
or contribute to the knowledge base. Read the directory layout first — it
determines where everything goes.

---

## Directory layout (quick reference)

```
agents-for-EU/
├── plugins/                        ← installable skill packages (one per domain)
│   └── [domain]/
│       ├── CLAUDE.md               ← domain practice profile + playbook
│       ├── .claude-plugin/
│       │   └── plugin.json         ← skill registry + hooks + connectors
│       ├── skills/
│       │   └── [skill-name]/
│       │       └── SKILL.md        ← the skill itself
│       ├── references/             ← reference docs loaded by skills
│       └── hooks/                  ← symlinks to lib/hooks/
├── knowledge/                      ← EU institutional knowledge base (read-only reference)
│   ├── commissioners/              ← Commissioner agent personas
│   ├── dgs/                        ← Directorate-General profiles
│   ├── institutions/               ← EP, Council, ECJ, ECB, EEAS
│   ├── workflows/                  ← OLP, policy cycle sequences
│   └── agents/                     ← College, ISC, trilogue protocols
├── lib/
│   ├── hooks/                      ← shared hook shell scripts
│   └── legacy-skills/              ← pre-SKILL.md flat skills (pending conversion)
├── docs/                           ← user guides and examples
│   └── examples/
└── marketplace.json                ← plugin registry
```

---

## 1. Adding a skill to an existing package

### Step 1 — Create the skill directory

```bash
mkdir -p plugins/[domain]/skills/[skill-name]
```

### Step 2 — Write the SKILL.md

Every skill follows this exact format. Copy and fill in:

```markdown
---
name: [skill-name]
description: >
  [One paragraph. Who uses it, for what task, producing what output.
  Be specific — this is how Claude decides whether to invoke this skill.]
license: MIT
metadata:
  author: [your name or EC-Skills-Library]
  version: "1.0.0"
  domain: [eu-legislative / eu-competition / eu-simulation / etc.]
  triggers: >
    [Comma-separated phrases that should invoke this skill — think about
    how a user would describe the task they need done]
  role: [specialist / workflow / persona / multi-agent / setup]
  scope: [kebab-case description of the task scope]
  output-format: [document type produced]
  institution: [European Commission / DG XX / European Parliament / etc.]
  related-skills: [other skill ids this one works alongside]
---

# [Skill Title] — [Institution]

[One paragraph: who this persona is and what expertise they bring.
What body of law, regulation, or procedure do they master?]

---

## Core Workflow

1. **[Step name]** — [What happens in this step]
2. **[Step name]** — [...]

---

## Reference Guide

| Topic | Reference | Load When |
|---|---|---|
| [Topic] | `references/[file].md` or `knowledge/[path].md` | [Condition] |

---

## Constraints

### MUST DO
- [Specific obligation — include the reason]

### MUST NOT DO
- [Specific prohibition — include why it matters]

---

## Output Templates

### 1. [Template name]

\`\`\`
[Complete template. Every field. Use [placeholder] for user-supplied values.
End with the DRAFT disclaimer.]

---
DRAFT — For review by an EU official before use. Not an official Commission position.
\`\`\`

---

## Knowledge Reference

[Flat list of treaties, regulations, guidelines, case law, and methodologies
this skill draws on. No annotations needed — just the list.]
```

### Step 3 — Register in plugin.json

Add an entry to `plugins/[domain]/.claude-plugin/plugin.json` under `"skills"`:

```json
{ "id": "[skill-name]", "path": "skills/[skill-name]/SKILL.md", "description": "[One sentence]" }
```

### Step 4 — Add to the CLAUDE.md playbook

Add a row to the Playbook table in `plugins/[domain]/CLAUDE.md`:

```markdown
| [User request that should trigger this skill] | `[skill-name]` |
```

---

## 2. Adding a new domain package (new plugin)

If the skill area does not fit any existing package, create a new one.

### Step 1 — Scaffold the directory

```bash
mkdir -p plugins/[new-domain]/{.claude-plugin,skills/cold-start-interview,references,hooks}
```

### Step 2 — Create the plugin manifest

`plugins/[new-domain]/.claude-plugin/plugin.json`:

```json
{
  "id": "[new-domain]",
  "name": "[Human-readable name]",
  "version": "1.0.0",
  "description": "[What this package covers and who it is for]",
  "claude_md": "CLAUDE.md",
  "skills": [
    { "id": "cold-start-interview", "path": "skills/cold-start-interview/SKILL.md", "description": "Personalise this plugin to your context" }
  ],
  "hooks": {
    "post_output": "hooks/post-output-disclaimer.sh"
  },
  "connectors": []
}
```

### Step 3 — Create the practice profile

`plugins/[new-domain]/CLAUDE.md` — copy and adapt from any existing domain CLAUDE.md.
Required sections: `[SESSION CONTEXT]`, `Playbook`, `House Style`,
`Output Trust Standards`, `Escalation Matrix`, `Constraints Active in This Package`.

### Step 4 — Create the cold-start-interview skill

Copy `plugins/eu-legislative/skills/cold-start-interview/SKILL.md` as a starting
point and adapt the questions to the new domain's context.

### Step 5 — Wire up the hook symlink

```bash
ln -s ../../../lib/hooks/post-output-disclaimer.sh plugins/[new-domain]/hooks/post-output-disclaimer.sh
```

### Step 6 — Register in marketplace.json

Add an entry to `marketplace.json` under `"plugins"`:

```json
{
  "id": "[new-domain]",
  "name": "[Human-readable name]",
  "description": "[What this package covers and who it is for]",
  "path": "plugins/[new-domain]",
  "skills": ["cold-start-interview"]
}
```

---

## 3. Adding to the knowledge base

`knowledge/` contains EU institutional reference material — Commissioner personas,
DG profiles, institution definitions, workflow sequences. These are not skills;
they are loaded as context by skills (particularly by `eu-simulation`).

| What to add | Where |
|---|---|
| New Commissioner persona | `knowledge/commissioners/[portfolio].md` — follow `_template.md` |
| New DG profile | `knowledge/dgs/dg-[name].md` |
| New institution agent | `knowledge/institutions/[name].md` |
| New workflow sequence | `knowledge/workflows/[name].md` |
| New multi-agent protocol | `knowledge/agents/[name].md` |

Knowledge files are **reference material only** — they do not produce invokable
skills on their own. To make a knowledge file invokable, create a corresponding
skill in `plugins/eu-simulation/` that loads it.

---

## 4. Quality standards

### Legal accuracy
- Every legal obligation cited must reference a specific Treaty article,
  regulation article, or binding guideline — not just a document title
- Case law must include the full case name and C-/T- reference
- Uncertain or contested points must be flagged `[review — legal uncertainty]`

### Constraints must be specific
- **Good:** "Must not approve state aid without checking all four Art. 107(1) TFEU limbs — omitting any limb means the measure may not constitute aid at all"
- **Bad:** "Must not make errors"

### Output templates must be complete
- Every structural element an EU official expects must be present
- Use `[placeholder text]` for user-supplied fields
- Every template ends with the DRAFT disclaimer
- Every template that cites statutory text includes `[EUR-Lex — verify current version]`

### Trust tags must be applied
- `[EUR-Lex — verify current version]` — any citation of treaty text, regulation, or directive
- `[CJEU — verify Curia reference]` — any citation of case law
- `[model knowledge — verify]` — any figure or fact from training data, not retrieved live
- `[Eurostat YYYY-MM — verify]` — any statistical data
- `[review — political judgement required]` — any call that requires an official decision
- `[review — legal uncertainty]` — any genuinely unsettled legal point

---

## 5. Self-check before submitting

Run through this list before opening a pull request:

```
□ SKILL.md frontmatter has all required fields (name, description, license,
  metadata.author, metadata.version, metadata.domain, metadata.triggers,
  metadata.role, metadata.scope, metadata.output-format, metadata.institution,
  metadata.related-skills)
□ Skill is registered in plugin.json
□ Skill appears in the domain CLAUDE.md playbook
□ If new package: hook symlink created and resolves
□ If new package: registered in marketplace.json with correct path (plugins/[domain])
□ All output templates end with the DRAFT disclaimer
□ All legal citations use trust tags
□ MUST DO / MUST NOT DO constraints are specific and include a reason
□ `scripts/validate.sh` passes (no errors)
```

### Automated validation

`scripts/validate.sh` enforces the structural rules above. It runs two **hard
checks** (a failure blocks a commit) and one **soft check** (warnings only):

| Check | Type | What it asserts |
|---|---|---|
| Registered skill paths exist | hard | Every `skills[].path` in a `plugin.json` resolves to a real `SKILL.md` |
| DRAFT disclaimer present | hard | Every `SKILL.md` contains a `DRAFT` disclaimer |
| Cited reference files exist | soft | Every `references/<file>.md` cited in a SKILL exists (many legacy citations don't — these are surfaced, not fatal) |

Run it manually:

```bash
scripts/validate.sh            # full repo
scripts/validate.sh --strict   # promote the soft check to a hard failure
```

Enable it as a pre-commit hook once per clone:

```bash
git config core.hooksPath .githooks
```

With the hook active, the hard checks run automatically before every commit.

---

## Licence

All contributions are made under the MIT licence. By submitting a pull request
you agree that your contribution may be redistributed under the terms of that licence.
