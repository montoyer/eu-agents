# Agents for EU — Operating Manual

This file tells Claude Code how to operate the EU Commission agent system.

## What this repository is

A structured multi-agent framework that models the European Commission. Each Commissioner portfolio, Directorate-General, and inter-institutional body is represented as a specialized agent with a defined mandate, decision-making style, and scope of competence. Agents interact through real EU procedures: inter-service consultation, college deliberation, trilogue, comitology.

Skills live in `plugins/` as SKILL.md files and are invoked as slash commands. EU institutional knowledge (Commissioner personas, DG profiles, workflows) lives in `knowledge/` as reference material loaded by skills.

---

## How to invoke agents

### Commissioner personas (simulation-eu plugin)

```
/commissioner president          — President of the European Commission
/commissioner competition        — Commissioner for Competition
/commissioner trade              — Commissioner for Trade
/commissioner digital            — Executive Vice-President for Digital
/commissioner green-deal         — Executive Vice-President for the Green Deal
```

See `knowledge/commissioners/` for all 21 portfolios.

### Workflow skills (legislative-eu plugin)

Single-agent procedural tools that follow a fixed structure and produce a defined output:

```
/impact-assessment <policy brief>      — Full SWD regulatory impact assessment (8 steps)
/legislative-proposal <brief>          — Draft a structurally compliant regulation or directive
/treaty-check <proposal>               — Check legal basis, subsidiarity, proportionality, Charter
/consultation <topic>                  — Simulate a 12-week public consultation
/better-regulation <act>               — REFIT fitness check (5 criteria)
```

### Role skills (domain plugins)

Open-ended specialist personas. Adapt to whatever the user asks within their mandate:

```
/policy-officer        — Commission policy officer (briefing notes, WP negotiations, ISC)
/legislative-drafter   — Legislative drafter (regulations, directives, OLP drafts)
/lawyer-secgen         — SecGen legal quality reviewer (subsidiarity, JPG compliance)
/comitology-officer    — Comitology procedure assessment
/impact-assessment-analyst — Impact assessment specialist persona
/economist             — Economic analysis and market failure assessment
/lawyer-competition-antitrust — Antitrust analysis (Arts. 101–102 TFEU)
/lawyer-state-aid      — State aid analysis (Arts. 107–109 TFEU)
/lawyer-legal-service  — Legal Service opinion and litigation
/state-aid-review      — State aid four-limb test and compatibility assessment
/infringement          — Infringement procedure assessment (Arts. 258–260 TFEU)
/grant-manager         — Horizon Europe grant management
/procurement-expert    — Public procurement
/head-of-unit          — Unit management and staff operations
/trade-defence-investigator — Anti-dumping, anti-subsidy, safeguards
/data-analyst          — Eurostat data extraction and scoreboard design
/communication-officer — Press releases, speeches, lines to take
/dpo                   — Data Protection Officer (EUDPR threshold, DPIA sign-off, Art. 40 referral)
/it-project-manager    — IT architecture, data flows, processors, AI module documentation (DPIA)
/it-security           — CIA threat model, TIA for non-EU cloud/AI, residual risk (DPIA)
/legal-officer         — Legal basis Art. 5(1) EUDPR, necessity, proportionality, retention (DPIA)
```

### DPIA workflow skill (privacy-eu plugin)

Produces a complete Art. 39 EUDPR DPIA by voicing five specialist roles in sequence:

```
/dpia "<processing activity>"  — Full DPIA: DPO threshold → IT-PM → Legal → IT Security → EDPS determination
```

### Multi-agent simulation skills (simulation-eu plugin)

These voice multiple institutional actors in sequence:

```
/college-deliberation          — Full College vote (all 21 Commissioners in sequence)
/inter-service-consultation    — Route a proposal through all affected DGs + Legal Service
/trilogue                      — EP / Council / Commission three-institution negotiation
/european-parliament           — EP committee, rapporteur, political groups, plenary vote
/council-eu                    — Council working party, QMV arithmetic, general approach
/legislative-cycle             — Full OLP from Commission proposal to OJ publication
```

### Compound analysis commands (simulation-eu plugin)

These require all 21 Commissioner agents and are structurally impossible with a single-agent system:

```
/mandate-conflict <proposal>    — Conflict map across all 21 portfolios: guaranteed clashes,
                                  treaty basis for each side, severity (BLOCKING / SIGNIFICANT /
                                  MANAGEABLE), resolution path
/red-team-college <proposal>    — Token-efficient College stress test: runs all 21 Commissioners,
                                  returns only SEVERE objections + College adoptability verdict
/subsidiarity-stress <proposal> — Tests subsidiarity against 5 member-state configurations to find
                                  where the necessity argument fails; assesses yellow card risk
/timeline <proposal>            — OLP timeline with blocking dependencies, QMV arithmetic, and
                                  trilogue risk points for a proposed regulation or directive
```

---

## Agent behavior rules

**Stay in mandate.** Each agent must confine its output to its treaty-based competence. Out-of-scope questions are deferred to the correct portfolio rather than answered outside its remit.

**Cite the legal basis.** All legislative proposals and opinions must identify their TFEU or TEU legal basis (article number). This is non-negotiable.

**Apply the Better Regulation toolbox.** Policy initiatives include: problem definition, baseline, policy options, proportionality check, stakeholder mapping, expected impacts.

**Surface tensions.** When two Commissioner positions conflict (e.g., Competition vs. Industrial Policy), the system surfaces the tension explicitly rather than papering over it. The President arbitrates.

**Speak as the institution, not as an individual.** Commissioner agents represent the institutional position of their portfolio. They do not act as named individuals.

**Subsidiarity first.** Before proposing EU action, any agent must check whether the objective could be achieved at member-state level. If yes, it should recommend non-legislative action or framework legislation.

**Knowledge files are ground truth.** If a skill's output contradicts a mandate defined in `knowledge/commissioners/` or `knowledge/institutions/`, the knowledge file takes precedence.

---

## Directory conventions

| Directory | Purpose |
|---|---|
| `plugins/` | Installable skill packages — one sub-directory per domain |
| `plugins/<domain>/skills/<name>/SKILL.md` | A skill — frontmatter + persona + workflow + templates |
| `plugins/<domain>/.claude-plugin/plugin.json` | Plugin manifest — skill registry, hooks, connectors |
| `plugins/<domain>/CLAUDE.md` | Domain practice profile — playbook, house style, constraints |
| `plugins/<domain>/hooks/` | Hook symlinks pointing to `lib/hooks/` |
| `plugins/<domain>/references/` | Reference documents loaded by skills in that domain |
| `knowledge/commissioners/` | Commissioner agent personas — mandate, priorities, decision style |
| `knowledge/dgs/` | DG operational agents — technical analysis, legal framing |
| `knowledge/institutions/` | Counter-party agents (Parliament, Council, ECJ, ECB, EEAS) |
| `knowledge/workflows/` | Sequenced multi-step process definitions |
| `knowledge/agents/` | Multi-agent session protocols (College, ISC, trilogue) |
| `lib/hooks/` | Shared hook shell scripts |
| `lib/legacy-skills/` | Pre-SKILL.md flat skills (pending conversion) |
| `docs/` | User guides and reference material |
| `docs/examples/` | Worked end-to-end simulations |

### Installed plugins

| Plugin ID | Domain | Key skills |
|---|---|---|
| `legislative-eu` | Legislative & Policy | `policy-officer`, `legislative-drafter`, `lawyer-secgen`, `impact-assessment`, `legislative-proposal`, `treaty-check`, `better-regulation`, `consultation`, `comitology-officer`, `economist`, `isc-contributor`, `pq-responder`, `subsidiarity-checker`, `trilogue-position-tracker` |
| `competition-eu` | Competition & Legal Service | `lawyer-competition-antitrust`, `lawyer-state-aid`, `lawyer-legal-service`, `state-aid-review`, `market-definer`, `gber-screener` |
| `institutional-management-eu` | Institutional Management | `head-of-unit`, `deputy-head-of-unit`, `assistant-hod`, `hr-contract-manager-ta`, `financial-officer`, `pmo-pension-specialist`, `cdr-drafter` |
| `trade-eu` | Trade Defence | `trade-defence-investigator` |
| `grants-enforcement-eu` | Grants, Procurement & Enforcement | `grant-manager`, `infringement-officer`, `infringement`, `procurement-expert`, `lfn-drafter`, `transposition-tracker` |
| `data-communication-eu` | Data & Communication | `data-analyst`, `communication-officer`, `lines-to-take-drafter`, `digit-project-manager`, `data-steward`, `cybersecurity-officer`, `transparency-officer` |
| `simulation-eu` | EU Institutional Simulation | `commissioner`, `college-deliberation`, `inter-service-consultation`, `trilogue`, `legislative-cycle`, `european-parliament`, `council-eu`, `mandate-conflict`, `red-team-college`, `subsidiarity-stress`, `timeline` |
| `privacy-eu` | Data Protection & Privacy | `dpia`, `dpo`, `it-project-manager`, `it-security`, `legal-officer` |
| `careers-eu` | EU Careers & EPSO Preparation | `epso-grade`, `epso-presentation`, `epso-offer` |

---

## Output trust standards

Every skill applies inline attribution tags. Never act on tagged content without verification:

| Tag | Meaning |
|---|---|
| `[EUR-Lex — verify current version]` | Any citation of treaty text, regulation, directive, or decision |
| `[CJEU — verify Curia reference]` | Any citation of case law |
| `[model knowledge — verify]` | Any fact or figure from training data, not retrieved live |
| `[Eurostat YYYY-MM — verify]` | Statistical data — append extraction date |
| `[review — political judgement required]` | Requires an official to make the call |
| `[review — legal uncertainty]` | Law is genuinely unsettled — Legal Service consultation recommended |

Every skill output ends with:
```
DRAFT — For review by an EU official before use. Not an official Commission position.
```

---

## Tone and output format

- Institutional register: formal, precise, policy-oriented.
- Avoid hedging that is not substantively grounded. If a position is clear under the treaties, state it.
- Use EU terminology correctly: "regulation" vs "directive", "ordinary legislative procedure" vs "special", "recital" vs "article".
- Output legislative text in standard EU format: recitals, then operative articles, then annexes.
- Impact assessments follow the SWD (Staff Working Document) structure.
- Opinions include a short executive summary, analysis, and conclusion.

---

## Extending the system

**To add a new Commissioner or DG:**
1. Create a file in `knowledge/commissioners/` or `knowledge/dgs/` following the existing template.
2. Define: mandate, legal basis, key dossiers, decision style, tensions with other portfolios.
3. Add the agent to the `knowledge/agents/college-deliberation.md` roster.
4. Update the commissioner shortnames grid in `plugins/simulation-eu/CLAUDE.md`.

**To add a new skill:**
1. Create `plugins/<domain>/skills/<skill-name>/SKILL.md` using the SKILL.md frontmatter convention.
2. Register it in `plugins/<domain>/.claude-plugin/plugin.json` under `"skills"`.
3. Add a row to the Playbook table in `plugins/<domain>/CLAUDE.md`.

**To add a new domain plugin:**
Follow the full procedure in [CONTRIBUTING.md](CONTRIBUTING.md) — scaffold, manifest, practice profile, cold-start interview, hook symlink, marketplace registration.
