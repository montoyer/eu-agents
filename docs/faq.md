# EC-Skills-Library — Frequently Asked Questions

A plain-language guide for European Commission staff on what the EC-Skills-Library contains, what each concept means, and how to use any part of it — whether in Claude Code, GPT@EC, or another AI assistant.

---

## Table of contents

1. [What is the EC-Skills-Library?](#1-what-is-the-ec-skills-library)
2. [What is a Prompt?](#2-what-is-a-prompt)
3. [What is a Skill?](#3-what-is-a-skill)
4. [What is an Agent?](#4-what-is-an-agent)
5. [What is a Workflow?](#5-what-is-a-workflow)
6. [What is a Plugin?](#6-what-is-a-plugin)
7. [How the five concepts relate to each other](#7-how-the-five-concepts-relate-to-each-other)
8. [How to use skills in Claude Code](#8-how-to-use-skills-in-claude-code)
9. [How to use skills in GPT@EC or any other chat tool](#9-how-to-use-skills-in-gptec-or-any-other-chat-tool)
10. [Common use cases and which concept to reach for](#10-common-use-cases-and-which-concept-to-reach-for)
11. [Output quality and trust standards](#11-output-quality-and-trust-standards)
12. [Troubleshooting](#12-troubleshooting)

---

## 1. What is the EC-Skills-Library?

The EC-Skills-Library is a structured collection of AI assistant configurations modelled on the European Commission. It lets you interact with AI as if you were working with a Commission policy officer, a Commissioner's cabinet, a Legal Service lawyer, or the full College of Commissioners.

It is not a database and not a search engine. It is a set of **instruction packages** that tell an AI assistant:

- what role to play (policy officer, competition lawyer, DPO, etc.)
- what procedures to follow (Better Regulation, TFEU Art. 294, EUDPR Art. 39, etc.)
- what output format to produce (SWD, legislative proposal, DPIA, ISC synthesis note, etc.)
- what institutional constraints apply (subsidiarity check, legal basis citation, SecGen compliance, etc.)

The library is maintained in this repository and covers eight domains: legislative & policy, competition & legal, institutional management, trade defence, grants & procurement, data & communication, institutional simulation, and data protection & privacy.

---

## 2. What is a Prompt?

### Definition

A **prompt** is a plain-text instruction you type directly into any AI chat tool. It requires no setup, no installation, and no special software. You write it; the AI reads it and responds.

The **EU Prompt Library** is a curated collection of ready-made prompts designed for Commission work. Each prompt is a self-contained paragraph (or a few paragraphs) that tells the AI what role to play, what context applies, and what output to produce.

### Key characteristics

| Feature | Prompt |
|---|---|
| Format | Plain text, written by hand or copied from a library |
| Tool requirement | Any AI chat (GPT@EC, Claude, Gemini, Copilot, etc.) |
| Setup | None — paste and send |
| Persistence | Gone when the conversation ends |
| Complexity | One instruction → one response |
| Customisation | You edit the text directly |

### Example

You open GPT@EC and type:

> You are a European Commission policy officer specialising in competition policy. I need a one-page briefing note for my Head of Unit on the antitrust risks of a proposed merger between two major European cloud infrastructure providers. Structure it as: background, key legal questions under the EU Merger Regulation, preliminary risk assessment, and recommended next steps.

That is a prompt. No slash command, no plugin, no installation. Any AI that can read text will process it.

### When to use a prompt

- You are using a tool that does not support plugins or slash commands (GPT@EC, standard Claude chat, Gemini).
- You need something quickly and do not need a full structured workflow.
- You want to experiment or adapt the task before committing to a formal skill output.
- You are sharing the instruction with a colleague who uses a different tool.

### Prompts from this library

The SKILL.md files in `plugins/` are the authoritative source. The **persona section** of any SKILL.md (the text after the frontmatter `---` block) can be copied and used as the opening paragraph of a prompt in any LLM. See [section 9](#9-how-to-use-skills-in-gptec-or-any-other-chat-tool) for how to do this.

---

## 3. What is a Skill?

### Definition

A **skill** is a fully packaged version of a prompt. It lives in a `SKILL.md` file, has structured metadata, and is invoked with a slash command inside Claude Code. Instead of typing a multi-paragraph instruction every time, you type `/eu-legislative:policy-officer` and the AI loads the full persona, workflow, and output format automatically.

Think of a skill as a **saved, versioned, shareable prompt** with extras: metadata for automatic triggering, a defined output template, links to related skills, and integration with hooks and connectors.

### Key characteristics

| Feature | Skill |
|---|---|
| Format | `SKILL.md` file with YAML frontmatter + persona |
| Tool requirement | Claude Code (for slash-command invocation) |
| Setup | Plugin must be installed in the project |
| Persistence | Available every session as long as the plugin is installed |
| Complexity | One command → structured multi-step output |
| Customisation | Edit the SKILL.md file |

### Structure of a SKILL.md

Every skill file has two parts:

**1. Frontmatter (YAML)** — machine-readable metadata:

```yaml
---
name: policy-officer
description: >
  Use when performing the core duties of a European Commission policy officer...
metadata:
  role: specialist
  scope: policy-analysis-drafting-representation
  output-format: policy-documents-communications
  related-skills: legislative-drafter, impact-assessment-analyst, lawyer-secgen
---
```

The `description` field is especially important: Claude Code uses it to **automatically select the right skill** when your message matches — you may not need to type the slash command at all.

**2. Persona body (Markdown)** — human-readable instructions:

```markdown
# Policy Officer – European Commission

Experienced European Commission administrator with deep expertise in EU policy development...

## Core Workflow
1. Analyse — Understand the dossier...
2. Draft — Produce the required document...
3. Coordinate internally — Circulate drafts...
```

### Example

In Claude Code, in this repository, type:

```
/eu-legislative:policy-officer

Draft a briefing note for the Commissioner on the risk of regulatory fragmentation
in the EU cloud market following three member states' unilateral certification schemes.
```

The skill loads the policy officer persona, applies the Commission briefing note format, and produces a document structured as: background → policy context → legal assessment → options → recommended line.

### Skills in this library (selected)

| Slash command | Domain | What it produces |
|---|---|---|
| `/eu-legislative:policy-officer` | Legislative | Briefing notes, ISC contributions, negotiating briefs |
| `/eu-legislative:legislative-drafter` | Legislative | Regulations, directives, decisions (Joint Practical Guide format) |
| `/eu-legislative:impact-assessment` | Legislative | Full SWD — problem definition, options, CBA, SME test |
| `/eu-legislative:treaty-check` | Legislative | Legal basis, subsidiarity, proportionality, Charter review |
| `/eu-competition:lawyer-state-aid` | Competition | Art. 107–109 TFEU four-limb test and compatibility |
| `/eu-competition:lawyer-competition-antitrust` | Competition | Art. 101–102 TFEU analysis |
| `/eu-privacy:dpo` | Privacy | EUDPR threshold check, DPIA scoping, Art. 40 referral |
| `/eu-grants-enforcement:procurement-expert` | Grants | Tender evaluation, framework contract management |
| `/eu-institutional-management:head-of-unit` | Institutional | Appraisal reports, unit work plans, HR decisions |
| `/eu-data-communication:communication-officer` | Communication | Press releases, speeches, lines to take |
| `/eu-data-communication:data-analyst` | Data | Eurostat extraction, scoreboard design |

---

## 4. What is an Agent?

### Definition

An **agent** is an AI configured to embody a specific institutional role with a defined mandate, decision-making style, and scope of competence. Where a skill gives the AI a *task*, an agent gives the AI an *identity*.

In this library, agents model real EU institutional actors: the Commissioner for Competition, the Secretary-General's legal reviewer, a Council Presidency negotiator, the EDPS. Each agent:

- speaks strictly within its treaty-based mandate
- applies the legal tests appropriate to its portfolio
- surfaces tensions with other portfolios rather than papering over them
- refuses to act outside its competence and redirects to the correct portfolio

Agents live in the `knowledge/` directory as reference files loaded by skills.

### Key characteristics

| Feature | Agent |
|---|---|
| Format | Knowledge file (`knowledge/commissioners/`, `knowledge/institutions/`) |
| Tool requirement | Any — agents are personas that can be invoked in any LLM |
| Setup | The skill or system prompt loads the agent's mandate file |
| Persistence | The agent stays in character throughout the session |
| Complexity | Adapts to any question within its mandate |
| Customisation | Edit the knowledge file for the portfolio |

### The difference between a skill and an agent

A **skill** tells the AI *what to do* (draft a briefing note, run an impact assessment, produce a DPIA).

An **agent** tells the AI *who to be* (Competition Commissioner, Legal Service lawyer, DPO).

Most skills load an agent persona automatically. When you type `/eu-competition:lawyer-state-aid`, the skill loads both the workflow (four-limb test → compatibility analysis) and the agent (Legal Service State Aid lawyer who applies Art. 107 TFEU rigorously and refuses to approve aid for "strategic reasons" not grounded in the rules).

### Example: Commissioner agents

The `knowledge/commissioners/competition.md` file defines the Competition Commissioner agent:

```markdown
# Commissioner for Competition

## Mandate
Treaty basis: TFEU Art. 101-109
Scope: Enforces EU competition rules: antitrust, merger control, and state aid.

## Decision style
Legally precise. All positions must be defensible before the General Court and ECJ.
Distinguishes sharply between competition enforcement and industrial policy.
Resists pressure to clear mergers for "strategic" reasons not grounded in competition analysis.

## Tensions with other portfolios
- vs. EVP Economy: Industrial policy state aid vs. level playing field.
- vs. EVP Digital: DMA (ex ante) vs. antitrust (ex post) — jurisdiction boundaries.
```

When you invoke `/eu-simulation:commissioner competition`, this mandate file is loaded and the AI responds as that portfolio — not as a named individual, but as the institutional position of DG COMP.

### Multi-agent sessions

Agents can be run in sequence to simulate inter-institutional processes. The `knowledge/agents/` directory defines these multi-agent protocols:

- `college-deliberation.md` — all 21 Commissioner agents convene, each speaks, President arbitrates and calls the vote
- `inter-service-consultation.md` — lead DG circulates, affected DGs respond (Agreement / Reservations / Opposition), Legal Service opines, SecGen checks Better Regulation compliance
- `trilogue.md` — EP rapporteur, Council Presidency, and Commission representative negotiate article by article
- `dpia.md` — five specialist agents (IT-PM, Legal Officer, IT Security, DPO, EDPS) contribute sections of a complete DPIA in sequence

---

## 5. What is a Workflow?

### Definition

A **workflow** is a structured, multi-step procedure that follows a fixed sequence to produce a defined output. Where a skill gives you a specialist persona and a general workflow, a dedicated workflow skill locks the sequence and ensures every required step is completed.

Workflows model real EU procedures: the Ordinary Legislative Procedure, the Better Regulation impact assessment cycle, the DPIA process under EUDPR Art. 39. They are the closest the library gets to automating a procedural obligation.

### Key characteristics

| Feature | Workflow |
|---|---|
| Format | SKILL.md with a numbered step sequence |
| Tool requirement | Claude Code (slash command) or any LLM (paste the steps) |
| Setup | Plugin must be installed |
| Complexity | Multi-step, each step builds on the previous |
| Output | Complete structured document or simulation record |

### Workflow vs. skill — the distinction

A **role skill** like `/eu-legislative:policy-officer` is open-ended. You ask it anything within the policy officer's mandate and it responds.

A **workflow skill** like `/eu-legislative:impact-assessment` is procedurally constrained. It runs through a fixed sequence (problem definition → subsidiarity check → baseline → policy options → CBA → comparison matrix → preferred option → monitoring framework) and will not skip a step, because skipping a step in a real impact assessment would result in an RSB negative opinion.

### Example: `/eu-legislative:impact-assessment`

```
/eu-legislative:impact-assessment "A proposed EU regulation requiring platforms with over 10,000 
business users to publish algorithmic ranking criteria by 2027"
```

The skill runs 8 fixed steps:

| Step | Output |
|---|---|
| 1 | Problem definition and market failure analysis |
| 2 | Subsidiarity test (Art. 5(3) TEU) — is EU action needed? |
| 3 | Baseline scenario — what happens if the Commission does nothing? |
| 4 | Policy options (Option 0: no action through Option 3: full regulation) |
| 5 | Impact analysis per option — economic, social, environmental |
| 6 | SME test and DNSH assessment |
| 7 | Comparison matrix and preferred option with proportionality statement |
| 8 | Monitoring and evaluation framework |

### Example: `/eu-simulation:legislative-cycle`

The most complex workflow in the library. Runs the full Ordinary Legislative Procedure (TFEU Art. 294) from Commission initiative to Official Journal publication:

```
/eu-simulation:legislative-cycle "Mandatory supply chain due diligence for critical raw materials"
```

Phases:
1. Commission pre-proposal phase (impact assessment → ISC → College vote → COM document)
2. EP first reading (committee, rapporteur, amendments, plenary vote)
3. Council first reading (working party, COREPER, QMV)
4. Trilogue (if positions diverge)
5. Second readings and conciliation (if needed)
6. Signature and OJ publication

### Example: `/eu-privacy:dpia`

Workflow for a complete Data Protection Impact Assessment under EUDPR Art. 39:

```
/eu-privacy:dpia "HR analytics system processing staff performance data and absence patterns 
to generate management recommendations"
```

Produces all seven Art. 39(7) EUDPR elements in sequence, each authored by the relevant specialist agent (IT-PM → Legal → IT Security → DPO → EDPS prior-consultation determination).

---

## 6. What is a Plugin?

### Definition

A **plugin** is a packaged collection of skills, agent knowledge files, hooks, and connectors — all scoped to one domain. Installing a plugin gives you all the skills in that domain as slash commands, pre-configured to work together and aware of each other.

Think of a plugin as the equivalent of installing a specialised software module. Before: you have no `/eu-competition:lawyer-state-aid` command. After: you have the full competition & legal service plugin with six interrelated skills.

### Key characteristics

| Feature | Plugin |
|---|---|
| Format | Directory with `plugin.json` manifest, `SKILL.md` files, `CLAUDE.md`, `hooks/`, `references/` |
| Tool requirement | Claude Code |
| Setup | Install by pointing Claude Code at the plugin directory |
| Coverage | All skills in the domain, pre-connected |
| House style | Domain-specific `CLAUDE.md` sets tone, constraints, output conventions |
| Hooks | Shell scripts that run automatically on defined events |

### Plugin structure

```
plugins/eu-competition/
├── .claude-plugin/
│   └── plugin.json          ← skill registry, connector declarations
├── CLAUDE.md                ← domain practice profile and house style
├── skills/
│   ├── lawyer-state-aid/
│   │   └── SKILL.md
│   ├── lawyer-competition-antitrust/
│   │   └── SKILL.md
│   ├── market-definer/
│   │   └── SKILL.md
│   └── gber-screener/
│       └── SKILL.md
└── references/
    └── [domain reference documents]
```

### The eight plugins in this library

| Plugin | Domain | Skills included |
|---|---|---|
| `eu-legislative` | Legislative & Policy | `policy-officer`, `legislative-drafter`, `lawyer-secgen`, `impact-assessment`, `legislative-proposal`, `treaty-check`, `better-regulation`, `consultation`, `comitology-officer`, `economist`, and 8 more |
| `eu-competition` | Competition & Legal | `lawyer-competition-antitrust`, `lawyer-state-aid`, `lawyer-legal-service`, `state-aid-review`, `market-definer`, `gber-screener` |
| `eu-institutional-management` | Institutional Management | `head-of-unit`, `deputy-head-of-unit`, `assistant-hod`, `hr-contract-manager-ta`, `financial-officer`, `pmo-pension-specialist`, `cdr-drafter` |
| `eu-trade` | Trade Defence | `trade-defence-investigator` |
| `eu-grants-enforcement` | Grants, Procurement & Enforcement | `grant-manager`, `infringement-officer`, `infringement`, `procurement-expert`, `lfn-drafter`, `transposition-tracker` |
| `eu-data-communication` | Data & Communication | `data-analyst`, `communication-officer`, `lines-to-take-drafter` |
| `eu-simulation` | EU Institutional Simulation | `commissioner`, `college-deliberation`, `inter-service-consultation`, `trilogue`, `legislative-cycle`, `european-parliament`, `council-eu` |
| `eu-privacy` | Data Protection & Privacy | `dpia`, `dpo`, `it-project-manager`, `it-security`, `legal-officer`, `ai-act-officer`, `ropa-drafter`, and 7 more |

### Hooks

Hooks are shell scripts that run automatically at Claude Code lifecycle events — no user action needed. Only `eu-legislative` ships hooks (`hooks/hooks.json`, fired on `PostToolUse` when a drafting skill is invoked):

- `legal-basis-check.sh` — injects the requirement that every legislative draft cite its treaty legal basis (an act without one is void — CJEU C-300/89)
- `subsidiarity-prompt.sh` — injects a reminder that the draft needs a subsidiarity and proportionality check, and prompts the user to run `/eu-legislative:subsidiarity-checker`

The `DRAFT` disclaimer on every output is enforced by the SKILL.md templates themselves, verified by `scripts/validate.sh`.

Hooks enforce procedural discipline at the infrastructure level, not just through the persona instructions.

---

## 7. How the five concepts relate to each other

```
PLUGIN
└── contains multiple SKILLS
    └── each SKILL loads one or more AGENTS (from knowledge/)
        └── some SKILLS implement a fixed WORKFLOW (multi-step sequence)
            └── all of the above can be distilled into a PROMPT for use in any LLM
```

### Decision tree: which concept do I need?

| Situation | Concept | Example |
|---|---|---|
| I need a quick answer in GPT@EC right now | **Prompt** | Paste the persona paragraph from the SKILL.md + your question |
| I need a specialist persona that adapts to my questions | **Skill** | `/eu-legislative:policy-officer` or `/eu-competition:lawyer-state-aid` |
| I need to simulate an institutional actor's position | **Agent** | `/eu-simulation:commissioner competition` |
| I need a complete procedural output (IA, DPIA, legislative proposal) | **Workflow skill** | `/eu-legislative:impact-assessment`, `/eu-privacy:dpia`, `/eu-simulation:legislative-cycle` |
| I work in one domain regularly and want all tools pre-configured | **Plugin** | Install `eu-legislative` or `eu-privacy` |

### Analogy

| Concept | Office analogy |
|---|---|
| Prompt | A sticky note with instructions you hand to a colleague |
| Skill | A standardised procedure document in the unit's shared drive |
| Agent | A named expert colleague with a defined portfolio and known positions |
| Workflow | A procedural checklist (e.g. the DPIA form, the IA template) |
| Plugin | The entire unit — all its staff, procedures, and tools, available as a package |

---

## 8. How to use skills in Claude Code

### Prerequisites

- Claude Code installed and running
- This repository open as the working directory (`/agents`)

### Invoking a skill by slash command

Type the skill name preceded by `/`:

```
/eu-legislative:policy-officer

I need a negotiating brief for next week's Council working party on the proposed
Cyber Resilience Act amendment. The debate is on Art. 12 (vulnerability disclosure
timeline). Our DG's position is that 72 hours is too short for complex embedded systems.
```

Claude reads the `policy-officer` SKILL.md, loads the persona, and produces the brief.

### Natural-language invocation (automatic skill selection)

You do not always need the slash command. Claude Code reads the `description` field in every SKILL.md and selects the best-matching skill automatically:

```
Help me check whether Art. 114 TFEU is a valid legal basis for a regulation on 
platform interoperability, and whether it meets the subsidiarity test.
```

Claude will automatically engage the `treaty-check` skill because the request matches its trigger keywords (`legal basis`, `subsidiarity test`).

### Running a workflow

Workflow skills take a brief as input and run the full procedure:

```
/eu-legislative:impact-assessment "Mandatory recycled content requirements for single-use plastic 
packaging in the food sector, phased from 20% by 2028 to 50% by 2033"
```

The output will be a complete SWD-structured impact assessment. For long workflows, Claude may produce the output in sections — you can ask it to continue to the next step.

### Running a multi-agent simulation

```
/eu-simulation:college-deliberation

Should the Commission propose mandatory human oversight requirements for all 
AI systems used in public benefit decisions (social benefits, taxation, permit grants)?
```

All 21 Commissioner agents deliberate in sequence. Expect: the EVP Digital to support (Digital Rights angle), the Commissioner for Employment to flag labour market implications, the Commissioner for Budget to worry about implementation costs, the Competition Commissioner to flag state aid risk in national AI procurement, the President to find a consensus position.

### Chaining skills

Skills can be chained manually for complex tasks:

```
Step 1: /eu-legislative:treaty-check — confirm legal basis for the proposal
Step 2: /eu-legislative:legislative-proposal — draft the regulation
Step 3: /eu-legislative:impact-assessment — produce the accompanying SWD
Step 4: /eu-simulation:inter-service-consultation — simulate the ISC round
Step 5: /eu-simulation:college-deliberation — simulate College adoption
```

Or run `/eu-simulation:legislative-cycle` which does all of this in one command.

---

## 9. How to use skills in GPT@EC or any other chat tool

Skills are designed for Claude Code, but the underlying expertise is transferable to any LLM. Here is how to use any skill in GPT@EC, standard Claude chat, Microsoft Copilot, Gemini, or any other tool.

### Method 1 — Copy the persona paragraph

Every SKILL.md contains a persona section after the frontmatter. Copy it and paste it as the first message (system prompt or opening message) in your chat session.

**Steps:**
1. Open the relevant SKILL.md (e.g. `plugins/eu-legislative/skills/policy-officer/SKILL.md`)
2. Scroll past the `---` frontmatter block to the `# Policy Officer` heading
3. Copy from that heading down through the Core Workflow
4. Paste it at the start of your GPT@EC conversation, then add your specific question

**Example — using `/eu-competition:lawyer-state-aid` in GPT@EC:**

Open `plugins/eu-competition/skills/lawyer-state-aid/SKILL.md`. Copy the persona section. Then in GPT@EC, start with:

> [paste persona here]
>
> Now analyse the following measure for compatibility with EU state aid rules under Art. 107 TFEU: the Belgian regional government offers a €50M non-repayable grant to a steel producer to build a new hydrogen-ready furnace, on condition that the plant remains operational for 15 years.

The LLM will adopt the Legal Service State Aid lawyer persona and apply the four-limb test.

### Method 2 — Copy just the workflow steps

For workflow skills, you do not need the full persona. Copy the numbered step sequence from the SKILL.md and paste it as instructions:

**Example — `/eu-privacy:dpia` in GPT@EC:**

> I need you to produce a complete DPIA following the EUDPR Art. 39 structure. Use exactly these steps:
>
> Step 1 — DPO threshold screening: confirm whether Art. 39(1)/(2) EUDPR requires a DPIA.
> Step 2 — IT Project Manager technical description: architecture, data flows, processors, retention, AI module if any.
> Step 3 — Legal Officer analysis: legal basis Art. 5(1) EUDPR, necessity, proportionality, special categories.
> Step 4 — IT Security Officer: CIA threat model, TIA for non-EU providers, security measures, residual risk.
> Step 5 — DPO assessment: risk sign-off, completeness check, Art. 40 determination.
>
> The processing activity is: [describe your system]

### Method 3 — Use the Commissioner knowledge files as system prompts

The `knowledge/commissioners/` files are already formatted as LLM-ready system prompts. Copy any commissioner file and paste it into the system prompt field of GPT@EC (if accessible) or as the first message.

**Example — Competition Commissioner in GPT@EC:**

1. Open `knowledge/commissioners/competition.md`
2. Copy the entire file
3. In GPT@EC, start a new chat and paste it as your first message, followed by:

> You are now operating as this Commissioner. Please assess the proposed acquisition of a European mid-size cloud provider by a US hyperscaler under the EU Merger Regulation.

### Method 4 — Reference the EU Prompt Library entries

If your organisation publishes prompt library entries based on this repository, those entries are already adapted for GPT@EC and require no further preparation. Simply select the relevant prompt template, fill in the [brackets], and send.

### Limitations when using skills outside Claude Code

| Feature | Claude Code | GPT@EC / other LLM |
|---|---|---|
| Slash command invocation | Yes | No — paste manually |
| Automatic skill selection | Yes | No — you specify the persona |
| Hooks (auto-disclaimer, pre-checks) | Yes | No — add manually |
| Plugin connectors (EUR-Lex, Eurostat) | When configured | No — describe the source you want |
| Skills aware of each other | Yes | Only if you copy both |
| Persistent persona across sessions | Yes | No — re-paste each session |
| Multi-agent College simulation | Automatic | Possible — paste the college protocol from `knowledge/agents/eu-simulation:college-deliberation.md` |

**Bottom line:** Claude Code gives you the full system with slash commands, hooks, and cross-skill awareness. GPT@EC gives you the same intellectual content — the personas, the procedures, the legal frameworks — but requires manual setup each session. The quality of the substantive output is comparable; the workflow efficiency is not.

---

## 10. Common use cases and which concept to reach for

### "I need to draft a briefing note for my HoU before tomorrow's COREPER meeting"

Reach for: **`/eu-legislative:policy-officer`** (skill)

```
/eu-legislative:policy-officer

Draft a 2-page briefing note for the Head of Unit ahead of the COREPER II meeting 
on Thursday. Topic: the Commission's position on the General Product Safety Regulation 
amendment proposed by the Hungarian Presidency. Focus on our redlines and the current 
state of member-state positions.
```

### "I want to understand what the Commissioner for Digital would say about a mandatory 
AI audit requirement"

Reach for: **`/eu-simulation:commissioner digital`** (agent)

```
/eu-simulation:commissioner digital

How does your portfolio assess the proposal to require mandatory third-party audits 
of all AI systems used in HR decisions across the EU public sector?
```

### "I need to check whether our proposed regulation is legally sound before we send 
it to the Legal Service"

Reach for: **`/eu-legislative:treaty-check`** (skill + workflow)

```
/eu-legislative:treaty-check

[paste your draft legislative proposal]
```

The skill checks legal basis, subsidiarity, proportionality, and Charter rights — the same four elements the Legal Service will scrutinise.

### "My DG is launching a major initiative and I need the full package: IA, legislative 
proposal, and a College simulation"

Reach for: **`/eu-simulation:legislative-cycle`** (workflow)

```
/eu-simulation:legislative-cycle "EU framework for mandatory transparency of public sector algorithmic 
decision-making systems"
```

### "We have a new IT system. I need to know whether it triggers a DPIA and if so 
produce the full assessment"

Reach for: **`/eu-privacy:dpia`** (workflow skill, multi-agent)

```
/eu-privacy:dpia "Automated leave management system that uses AI to flag anomalous absence 
patterns and generate management recommendations for HR decisions. Processes 
health-related absence data for 15,000 staff. Hosted on a US-based cloud provider."
```

### "I want to present a state aid case to my Head of Unit and need a structured 
legal analysis"

Reach for: **`/eu-competition:lawyer-state-aid`** (skill, eu-competition plugin)

```
/eu-competition:lawyer-state-aid

Analyse whether the following measure constitutes state aid within the meaning of 
Art. 107(1) TFEU, and if so, assess compatibility under the Climate, Energy and 
Environmental Aid Guidelines (CEEAG): [describe the measure]
```

### "I am in GPT@EC and cannot use Claude Code — I still need an impact assessment"

Reach for: **Method 2** from [section 9](#9-how-to-use-skills-in-gptec-or-any-other-chat-tool) — copy the workflow steps from `plugins/eu-legislative/skills/impact-assessment/SKILL.md` and paste them as instructions.

---

## 11. Output quality and trust standards

Every skill output carries **inline attribution tags** that tell you how certain the information is:

| Tag | What it means | What you should do |
|---|---|---|
| `[EUR-Lex — verify current version]` | Treaty text, regulation, directive, or decision cited | Check EUR-Lex for the current consolidated version |
| `[CJEU — verify Curia reference]` | Case law cited | Verify on Curia.europa.eu |
| `[model knowledge — verify]` | Fact or figure from AI training data | Cross-check with authoritative source |
| `[Eurostat YYYY-MM — verify]` | Statistical data | Check Eurostat for current figures |
| `[review — political judgement required]` | The AI has framed the options; an official must decide | Escalate to the responsible official |
| `[review — legal uncertainty]` | The law is genuinely unsettled | Request a Legal Service opinion |

Every output ends with:

```
DRAFT — For review by an EU official before use. Not an official Commission position.
```

This is not a formality. The outputs are structurally realistic and procedurally correct, but they are not authoritative. They are starting points for official work, not substitutes for it.

### What the library is good for

- Research and scenario analysis before launching a formal procedure
- First drafts that an official refines and takes ownership of
- Training and simulation — understanding how the College would react, how the Legal Service would argue, how a trilogue would unfold
- Rapid prototyping of legislative proposals and IAs before committing staff time
- Onboarding — new officials understanding Commission procedures through worked examples

### What the library is not

- A legal opinion (request one from the Legal Service)
- An official Commission position (only the College or the relevant Commissioner can adopt one)
- A substitute for EUR-Lex (always verify cited legislation)
- A substitute for Eurostat (always verify cited statistics)

---

## 12. Troubleshooting

### The slash command does not work

- Confirm you are running Claude Code (not Claude.ai chat or another tool).
- Confirm you are in the `/agents` working directory — the plugins must be installed.
- Try the natural-language approach: describe what you need and Claude Code will select the skill automatically.

### The output skipped a workflow step

- For workflow skills, explicitly ask Claude to continue: "Please proceed to step 3 — policy options."
- If the output seems incomplete, check whether your input brief was specific enough. Vague inputs produce compressed outputs.

### The Commissioner agent went off-mandate

- This should not happen — the agents are constrained by their knowledge files. If it does, remind the agent: "You are the Commissioner for Competition. Please respond only within the scope of your portfolio mandate."
- Check that the `knowledge/commissioners/competition.md` file exists and has not been edited to remove the mandate constraints.

### I am using GPT@EC and the persona drifts after a few messages

- GPT@EC (like all chat tools) does not enforce the persona automatically. After 5–10 exchanges, re-paste the key persona paragraph to reset.
- Alternatively, use Claude Code where the persona is locked in the SKILL.md for the entire session.

### The output contains a legal citation I cannot verify

- Use EUR-Lex (`eur-lex.europa.eu`) to search by article number or document reference.
- The `[EUR-Lex — verify current version]` tag is your signal that this citation needs checking. Do not rely on the cited text without verification.

### I want to add a new skill or Commissioner portfolio

See `CLAUDE.md` — the "Extending the system" section — for the step-by-step procedure:
- New Commissioner: add a file to `knowledge/commissioners/` using `_template.md`, add to the College roster in `knowledge/agents/eu-simulation:college-deliberation.md`.
- New skill: create `plugins/<domain>/skills/<name>/SKILL.md`, register in `plugin.json`, add a row to the domain `CLAUDE.md`.
- New domain plugin: follow `CONTRIBUTING.md` — scaffold, manifest, practice profile, cold-start interview, marketplace registration.

---

---

## 13. Complete skill reference

All 97 skills across 9 plugins. Add the marketplace with `/plugin marketplace add montoyer/eu-agents`, then install the plugin you need with `/plugin install <plugin-name>@eu-agents`.

### `eu-legislative` — Legislative & Policy

| Skill | Description |
|---|---|
| `/eu-legislative:policy-officer` | Briefing notes, negotiating briefs, ISC contributions, options papers |
| `/eu-legislative:legislative-drafter` | Draft EU regulations, directives, and decisions to Joint Practical Guide standards |
| `/eu-legislative:lawyer-secgen` | ISC legal quality review, subsidiarity and proportionality analysis |
| `/eu-legislative:comitology-officer` | Delegated and implementing acts, committee procedures, EP objections |
| `/eu-legislative:impact-assessment-analyst` | Better Regulation impact assessments — problem definition, CBA, SME test |
| `/eu-legislative:economist` | Economic analysis, market failure assessment, European Semester data |
| `/eu-legislative:isc-contributor` | Draft ISC contributions — Agreement, Reservations, or Opposition with textual amendments |
| `/eu-legislative:pq-responder` | Draft EP Parliamentary Question responses (Rules 138 and 139) with clearance tracking |
| `/eu-legislative:subsidiarity-checker` | Run Art. 5(3)–(4) TEU subsidiarity and proportionality test with Protocol No. 2 risk |
| `/eu-legislative:trilogue-position-tracker` | Maintain four-column document, track positions, draft pre-round mandate briefs |
| `/eu-legislative:impact-assessment` | Full SWD impact assessment — problem definition, options, CBA, SME test, DNSH, comparison matrix |
| `/eu-legislative:legislative-proposal` | Draft complete EU regulation or directive — legal basis, recitals, operative articles, EM |
| `/eu-legislative:treaty-check` | Legal basis, subsidiarity, proportionality, and Charter rights review — mirrors CLS check |
| `/eu-legislative:better-regulation` | REFIT regulatory fitness check — five criteria, overall score, simplification opportunities |
| `/eu-legislative:consultation` | Simulate or draft a 12-week public consultation — stakeholder positions, synthesis, Commission response |
| `/eu-legislative:delegated-acts-drafter` | Art. 290 TFEU delegated acts — enabling clause check, DA vs IA classification, scrutiny period, draft act |
| `/eu-legislative:fundamental-rights-assessor` | Charter of Fundamental Rights full assessment — Art. 51 scope, Art. 52(1) limitation test, all 54 articles |
| `/eu-legislative:regulatory-impact-quantifier` | CBA/CEA quantification — compliance costs, SME test, OIOO, benefit monetisation, RSB-ready tables |
| `/eu-legislative:policy-cycle` | Full EU policy lifecycle — agenda-setting through evaluation, all 7 phases, Better Regulation methodology |

### `eu-competition` — Competition & Legal Service

| Skill | Description |
|---|---|
| `/eu-competition:lawyer-competition-antitrust` | Arts. 101–102 TFEU analysis, SO drafting, fines calculation, dawn raids |
| `/eu-competition:lawyer-state-aid` | Art. 107–109 TFEU four-limb test, GBER screening, recovery calculation |
| `/eu-competition:lawyer-legal-service` | CLS legal opinions, litigation management, Written Observations, risk assessment |
| `/eu-competition:gber-screener` | Screen a measure against GBER categories — all conditions, incentive effect, cumulation |
| `/eu-competition:market-definer` | Apply SSNIP test, define relevant product and geographic market for Art. 101/102/merger |
| `/eu-competition:state-aid-review` | Art. 107(1) four-limb test, de minimis, GBER screening, compatibility assessment workflow |
| `/eu-competition:merger-screener` | EU Merger Regulation — SIEC test, jurisdictional thresholds, Phase I/II, remedies design |
| `/eu-competition:dawn-raid-advisor` | Competition inspection defence — LPP claims, employee rights, document log, post-inspection obligations |
| `/eu-competition:eu-liability-advisor` | Art. 340(2) TFEU non-contractual liability — Bergaderm three-limb test, damage assessment, MS Francovich liability |

### `eu-simulation` — EU Institutional Simulation

| Skill | Description |
|---|---|
| `/eu-simulation:commissioner` | Invoke any of 21 Commissioner personas — speaks from treaty mandate, priorities, tensions |
| `/eu-simulation:college-deliberation` | Full College of Commissioners meeting — all 21 speak, President calls vote, outcome recorded |
| `/eu-simulation:inter-service-consultation` | ISC round — lead DG circulates, all affected DGs respond, synthesis note produced |
| `/eu-simulation:trilogue` | Inter-institutional trilogue — EP/Council/Commission negotiate via four-column document |
| `/eu-simulation:legislative-cycle` | Full OLP from Commission initiative to OJ publication — chains all six phases |
| `/eu-simulation:european-parliament` | EP counter-party agent — committee, rapporteur, group dynamics, amendments, plenary vote |
| `/eu-simulation:council-eu` | Council counter-party agent — configuration, QMV arithmetic, general approach, Presidency mandate |
| `/eu-simulation:advocate-general` | AG Opinion simulation — legal question analysis, party arguments, proposed ruling, Art. 252 TFEU independence |
| `/eu-simulation:council-presidency` | Council Presidency chair — compromise texts, non-papers, QMV tracking, general approach, trilogue mandate |
| `/eu-simulation:mandate-conflict` | Conflict map across all 21 Commissioner portfolios — structurally guaranteed mandate clashes with treaty basis and severity rating |
| `/eu-simulation:red-team-college` | Token-efficient College stress test — runs all 21 Commissioners, returns only SEVERE objections and adoptability verdict |
| `/eu-simulation:subsidiarity-stress` | Tests subsidiarity justification against 5 member-state configurations — finds where necessity argument fails and assesses yellow card risk |
| `/eu-simulation:timeline` | OLP timeline with blocking dependencies, QMV arithmetic, and trilogue risk points |

### `eu-privacy` — Data Protection & Privacy

| Skill | Description |
|---|---|
| `/eu-privacy:dpia` | Full DPIA under Art. 39 EUDPR — multi-agent: DPO, IT-PM, IT Security, Legal Officer, EDPS prior-consultation determination |
| `/eu-privacy:dpo` | DPO persona — Art. 39 threshold screening, risk sign-off, register of processing activities, Art. 40 referral decision |
| `/eu-privacy:it-project-manager` | IT Project Manager — system architecture, data flows, third-party processors, ROPA record, retention schedule |
| `/eu-privacy:it-security` | IT Security Officer — CIA threat model, TIA for non-EU cloud/AI providers, security measures, residual risk rating |
| `/eu-privacy:legal-officer` | Legal Officer — legal basis Art. 5(1) EUDPR, necessity, proportionality, special categories, retention justification |
| `/eu-privacy:it-security-plan` | IT Security Plans Expert — ISP drafting, ISO 27001/CIS Controls mapping, risk register, incident response, NIS2 compliance |
| `/eu-privacy:data-breach-officer` | Data Breach Response — breach assessment, 72-hour EDPS notification (Art. 34 EUDPR), data subject communication, breach register |
| `/eu-privacy:ropa-drafter` | RoPA Drafter — Art. 31 EUDPR Record of Processing Activities, legal basis, retention schedule, processor register |
| `/eu-privacy:ai-act-officer` | AI Act Compliance — risk tier classification, prohibited practice check, FRIA (Art. 27), technical documentation, conformity assessment |
| `/eu-privacy:tia-expert` | Transfer Impact Assessment — full TIA for third-country transfers, adequacy decisions, SCCs, supplementary measures, Schrems II |
| `/eu-privacy:retention-schedule` | Retention Schedule — Art. 25 EUDPR storage limitation, retention matrix, sectoral obligations, archiving rules, deletion procedures |
| `/eu-privacy:privacy-notice-drafter` | Privacy Notice Drafter — Arts. 15–16 EUDPR compliant notices, plain language, layered notices, mandatory content checklist |
| `/eu-privacy:data-subject-rights` | Data Subject Rights — access, rectification, erasure, restriction, portability, objection — deadlines, exemptions, refusal letters |
| `/eu-privacy:edps-complaint-handler` | EDPS Complaint Handler — Art. 57/58 EUDPR supervisory inquiry response, contradictory procedure, remedial action plan |
| `/eu-privacy:ai-governance-officer` | AI Governance Officer — AI system register, model cards, governance board ToR, human oversight, AI procurement clauses |

### `eu-institutional-management` — Institutional Management

| Skill | Description |
|---|---|
| `/eu-institutional-management:head-of-unit` | Unit management, CDR, work programme, staff decisions, AMP |
| `/eu-institutional-management:deputy-head-of-unit` | Operational coordination, quality review, deadline tracking, A.I. acting |
| `/eu-institutional-management:assistant-hod` | ARES management, MIPS/C2 missions, SYSPER, PQ tracking, action trackers |
| `/eu-institutional-management:hr-contract-manager-ta` | TA/CA contract management, CEOS, CAST, recruitment, renewal decisions |
| `/eu-institutional-management:financial-officer` | ABAC financial circuit, FR 2018/1046, commitment and payment orders |
| `/eu-institutional-management:pmo-pension-specialist` | Annex VIII pension calculations, PMO entitlements, pension projections |
| `/eu-institutional-management:cdr-drafter` | Draft SMART CDR objectives, end-year appraisals, and competency assessments in SYSPER |
| `/eu-institutional-management:amp-drafter` | Annual Management Plan — unit objectives, KPIs, deliverables, resource mapping, risk section, COO cycle |
| `/eu-institutional-management:aar-drafter` | Annual Activity Report — objective assessment, resource use, internal control, HoU management assurance |
| `/eu-institutional-management:selection-board` | Selection procedure — vacancy notice, shortlisting, competency-based interview grid, selection board report |
| `/eu-institutional-management:access-to-documents` | Regulation 1049/2001 access requests — exception assessment, partial access, refusal letters, confirmatory procedure |
| `/eu-institutional-management:underperformance-advisor` | Art. 51 SR underperformance procedure — warning letter, improvement plan, monitoring, JEC submission |
| `/eu-institutional-management:budget-planner` | Budget planning and execution — CA/PA programming, virements, carry-overs, execution monitoring, AAR reporting |

### `eu-grants-enforcement` — Grants, Procurement & Enforcement

| Skill | Description |
|---|---|
| `/eu-grants-enforcement:grant-manager` | Horizon Europe MGA management, payment assessment, financial corrections |
| `/eu-grants-enforcement:infringement-officer` | Arts. 258–260 TFEU procedure — EU Pilot, LFN, RO, CJEU referral, Art. 260 penalties |
| `/eu-grants-enforcement:procurement-expert` | FR 2018/1046 procurement — framework contracts, tender evaluation, award decisions |
| `/eu-grants-enforcement:lfn-drafter` | Draft Art. 258 TFEU Letters of Formal Notice — non-transposition, incorrect transposition, misapplication |
| `/eu-grants-enforcement:transposition-tracker` | Track and assess directive transposition across 27 MS — status table, conformity, escalation |
| `/eu-grants-enforcement:infringement` | Art. 258–260 TFEU infringement assessment — type classification, procedural stage, penalty estimate |
| `/eu-grants-enforcement:reasoned-opinion-drafter` | Art. 258(2) TFEU Reasoned Opinion — rebuttal of member state observations, maintained allegations, RO drafting |
| `/eu-grants-enforcement:grant-audit-advisor` | Grant audit preparation and response — ECA/IAS on-the-spot checks, contradictory procedure, rebuttal notes |
| `/eu-grants-enforcement:grant-amendment-officer` | Grant agreement amendments — budget reallocation, partner withdrawal, period extension, force majeure |
| `/eu-grants-enforcement:tender-evaluator` | Tender evaluation — exclusion/selection/award criteria scoring, ALT assessment, evaluation report, debrief letters |
| `/eu-grants-enforcement:olaf-referral-advisor` | OLAF referral — fraud indicators, Art. 8 Reg. 883/2013 notification, payment suspension, parallel procedure rules |
| `/eu-grants-enforcement:direct-award-advisor` | Direct award justification — urgency, sole source, follow-on services, FR Art. 164 exception assessment |
| `/eu-grants-enforcement:eppo-jurisdiction-advisor` | EPPO jurisdiction — PIF offences, Reg. 2017/1939, OLAF-EPPO referral, parallel administrative procedure management |
| `/eu-grants-enforcement:cohesion-fund-manager` | Cohesion funds shared management — CPR 2021/1060, financial corrections, n+3 decommitment, closure, audit response |

### `eu-data-communication` — Data & Communication

| Skill | Description |
|---|---|
| `/eu-data-communication:data-analyst` | Eurostat data extraction, indicator design, scoreboards, data notes, visualisation |
| `/eu-data-communication:communication-officer` | Press releases, lines to take, Commissioner speeches, social media, briefings |
| `/eu-data-communication:lines-to-take-drafter` | Draft complete LTT packages — friendly/neutral/hostile Q&A, no-go zones, background facts, clearance tracking |
| `/eu-data-communication:digit-project-manager` | DIGIT IT project governance: Agile delivery, OCS gates, ITSRM² risk, EU Cloud, vendor management, steering-committee reporting |
| `/eu-data-communication:data-steward` | Data governance, metadata (DCAT-AP, ISA², SEMIC), open data publication, data quality, data spaces, Data Governance Act |
| `/eu-data-communication:cybersecurity-officer` | Cybersecurity risk (ITSRM²), NIS2 compliance, incident response, CERT-EU coordination, security accreditation, vulnerability management |
| `/eu-data-communication:transparency-officer` | Access to documents (Reg. 1049/2001), GESTDEM, confirmatory applications, exception analysis, Transparency Register, Ombudsman |

### `eu-trade` — Trade Defence

| Skill | Description |
|---|---|
| `/eu-trade:trade-defence-investigator` | AD/CVD/safeguard investigations — margins, injury, NOI, questionnaires, OSV |
| `/eu-trade:dumping-margin-calculator` | Dumping margin calculation — normal value, export price, Art. 2(10) adjustments, WA-WA, LDR |
| `/eu-trade:sanctions-screener` | EU restrictive measures screening — consolidated list, asset freeze, sectoral sanctions, derogation procedure |

### `eu-careers` — EU Careers & EPSO Preparation

| Skill | Description |
|---|---|
| `/eu-careers:epso-grade` | Estimate entry grade, step, and net monthly salary for a given competition type and candidate profile under SR Annex I |
| `/eu-careers:epso-presentation` | Coach and critique a 10-minute Assessment Centre oral presentation against EPSO Communication competency indicators |
| `/eu-careers:epso-offer` | Analyse a job offer letter: decode grade/step, calculate gross and net remuneration, map probation and contract obligations under the SR |

---

*Last updated: May 2026. EC-Skills-Library — MIT licence. Not an official European Commission publication.*
