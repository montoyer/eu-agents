# Agents for EU — Operating Manual

This file tells Claude Code how to operate the EU Commission agent system.

## What this repository is

A structured multi-agent framework that models the European Commission. Each Commissioner portfolio, Directorate-General, and inter-institutional body is represented as a specialized agent with a defined mandate, decision-making style, and scope of competence. Agents interact through real EU procedures: inter-service consultation, college deliberation, trilogue, comitology.

Skills live in `plugins/` as SKILL.md files and are invoked as slash commands. EU institutional knowledge (Commissioner personas, DG profiles, workflows) lives in `knowledge/` as reference material loaded by skills.

---

## How to invoke agents

### Commissioner personas (eu-simulation plugin)

```
/commissioner president          — President of the European Commission
/commissioner competition        — Commissioner for Competition
/commissioner trade              — Commissioner for Trade
/commissioner digital            — Executive Vice-President for Digital
/commissioner green-deal         — Executive Vice-President for the Green Deal
```

See `knowledge/commissioners/` for all 21 portfolios.

### Simulation support skills (eu-simulation plugin)

```
/coreper                         — COREPER I/II ambassador negotiation and mandate formation
/qmv-calculator                  — Qualified majority voting arithmetic and blocking minority check
/advocate-general                — CJEU Advocate General opinion (preliminary ruling, annulment)
/council-presidency               — Rotating Presidency compromise text and agenda management
```

### Workflow skills (eu-legislative plugin)

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
// Legislative & Policy (eu-legislative)
/policy-officer              — Commission policy officer (briefing notes, WP negotiations, ISC)
/legislative-drafter         — Legislative drafter (regulations, directives, OLP drafts)
/lawyer-secgen               — SecGen legal quality reviewer (subsidiarity, JPG compliance)
/comitology-officer          — Comitology procedure assessment
/impact-assessment-analyst   — Impact assessment specialist persona
/economist                   — Economic analysis and market failure assessment
/isc-contributor             — Inter-service consultation contributor (DG position paper)
/pq-responder                — Parliamentary Question answer drafting
/subsidiarity-checker        — Subsidiarity and proportionality assessment
/trilogue-position-tracker   — Track EP/Council positions across trilogue rounds
/delegated-acts-drafter      — Draft delegated acts under Art. 290 TFEU with empowerment analysis
/fundamental-rights-assessor — Charter of Fundamental Rights compatibility check
/regulatory-impact-quantifier — Quantify regulatory costs and benefits for impact assessments
/policy-cycle                — Full policy cycle management from agenda-setting to evaluation

// Competition & Legal Service (eu-competition)
/lawyer-competition-antitrust — Antitrust analysis (Arts. 101–102 TFEU)
/lawyer-state-aid            — State aid analysis (Arts. 107–109 TFEU)
/lawyer-legal-service        — Legal Service opinion and litigation
/state-aid-review            — State aid four-limb test and compatibility assessment
/market-definer              — Relevant market definition (product and geographic)
/gber-screener               — GBER block exemption eligibility screening
/merger-screener             — EUMR merger screening: thresholds, referral, Phase I/II assessment
/dawn-raid-advisor           — Art. 20–21 Regulation 1/2003 dawn raid rights and obligations
/eu-liability-advisor        — Non-contractual liability (Art. 340 TFEU), Francovich, damages claims

// Institutional Management (eu-institutional-management)
/head-of-unit                — Unit management and staff operations
/deputy-head-of-unit         — Deputy HoU: unit coordination, staff cover, workflow management
/assistant-hod               — Assistant to Head of Unit: agenda, ARES, correspondence, action points
/hr-contract-manager-ta      — TA contract management under CEOS: selection, renewal, reclassification
/financial-officer           — Financial regulation compliance, payment authorisation, ex-ante control
/pmo-pension-specialist      — PMO pension rights, JSIS, allowances under Staff Regulations
/cdr-drafter                 — Career Development Report drafting and appraisal procedure
/amp-drafter                 — Annual Management Plan drafting and objective-setting
/aar-drafter                 — Annual Activity Report drafting and performance reporting
/selection-board             — Selection board procedures, reserve list management, EPSO liaison
/access-to-documents         — Regulation 1049/2001 access-to-documents requests and exceptions
/underperformance-advisor    — Underperformance procedures under Staff Regulations
/budget-planner              — DG budget planning, commitment/payment appropriations, BIA

// Trade Defence (eu-trade)
/trade-defence-investigator  — Anti-dumping, anti-subsidy, safeguards
/dumping-margin-calculator   — Anti-dumping margin calculation methodology
/sanctions-screener          — EU sanctions compliance screening and derogation assessment

// Grants, Procurement & Enforcement (eu-grants-enforcement)
/grant-manager               — Horizon Europe grant management
/infringement                — Infringement procedure assessment (Arts. 258–260 TFEU)
/infringement-officer        — Infringement case management and member-state dialogue
/procurement-expert          — Public procurement
/lfn-drafter                 — Letter of Formal Notice drafting (Art. 258 TFEU, first step)
/transposition-tracker       — Directive transposition monitoring across member states
/reasoned-opinion-drafter    — Infringement reasoned opinion drafting (Art. 258 TFEU)
/grant-audit-advisor         — Grant audit response, error rates, financial corrections
/grant-amendment-officer     — Grant agreement amendment procedures
/tender-evaluator            — Tender evaluation methodology and scoring grids
/olaf-referral-advisor       — OLAF referral assessment and case opening criteria
/direct-award-advisor        — Direct award justification and single tender procedure
/eppo-jurisdiction-advisor   — EPPO jurisdiction and admissibility assessment
/cohesion-fund-manager       — ESIF/cohesion fund management, managing authority obligations

// Data & Communication (eu-data-communication)
/data-analyst                — Eurostat data extraction and scoreboard design
/communication-officer       — Press releases, speeches, lines to take
/lines-to-take-drafter       — Lines to take for press briefings and spokesperson responses
/digit-project-manager       — DIGIT IT project management, ISA², interoperability
/data-steward                — Data governance, metadata, data quality, open data publication
/cybersecurity-officer       — NIS2 compliance, CERT-EU liaison, incident response
/transparency-officer        — Transparency register, lobby meetings, conflict of interest

// Data Protection & Privacy (eu-privacy)
/dpo                         — Data Protection Officer (EUDPR threshold, DPIA sign-off, Art. 40 referral)
/it-project-manager          — IT architecture, data flows, processors, AI module documentation (DPIA)
/it-security                 — CIA threat model, TIA for non-EU cloud/AI, residual risk (DPIA)
/legal-officer               — Legal basis Art. 5(1) EUDPR, necessity, proportionality, retention (DPIA)
/it-security-plan            — IT Security Plan drafting, ISO 27001/NIS2 compliance
/data-breach-officer         — Art. 34–35 EUDPR data breach notification and register
/ropa-drafter                — Art. 31 EUDPR Record of Processing Activities
/ai-act-officer              — AI Act risk classification, FRIA, technical documentation
/tia-expert                  — Transfer Impact Assessment for third-country data transfers
/retention-schedule          — Art. 25 EUDPR retention schedule and deletion procedures
/privacy-notice-drafter      — Arts. 15–16 EUDPR compliant privacy notices
/data-subject-rights         — Data subject rights responses, deadlines, exemptions
/edps-complaint-handler      — EDPS supervisory inquiry response and remedial action
/ai-governance-officer       — AI system register, model cards, governance board ToR

// EU Careers & EPSO (eu-careers)
/epso-grade                  — Estimate entry grade, step, and net salary for a competition type
/epso-presentation           — Coach and critique a 10-minute Assessment Centre oral presentation
/epso-offer                  — Analyse a job offer letter: grade/step, remuneration, contract obligations
```

### DPIA workflow skill (eu-privacy plugin)

Produces a complete Art. 39 EUDPR DPIA by voicing five specialist roles in sequence:

```
/dpia "<processing activity>"  — Full DPIA: DPO threshold → IT-PM → Legal → IT Security → EDPS determination
```

### Multi-agent simulation skills (eu-simulation plugin)

These voice multiple institutional actors in sequence:

```
/college-deliberation          — Full College vote (all 21 Commissioners in sequence)
/inter-service-consultation    — Route a proposal through all affected DGs + Legal Service
/trilogue                      — EP / Council / Commission three-institution negotiation
/european-parliament           — EP committee, rapporteur, political groups, plenary vote
/council-eu                    — Council working party, QMV arithmetic, general approach
/legislative-cycle             — Full OLP from Commission proposal to OJ publication
```

### Compound analysis commands (eu-simulation plugin)

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
| `eu-legislative` | Legislative & Policy | `policy-officer`, `legislative-drafter`, `lawyer-secgen`, `impact-assessment`, `legislative-proposal`, `treaty-check`, `better-regulation`, `consultation`, `comitology-officer`, `economist`, `isc-contributor`, `pq-responder`, `subsidiarity-checker`, `trilogue-position-tracker`, `delegated-acts-drafter`, `fundamental-rights-assessor`, `regulatory-impact-quantifier`, `policy-cycle` |
| `eu-competition` | Competition & Legal Service | `lawyer-competition-antitrust`, `lawyer-state-aid`, `lawyer-legal-service`, `state-aid-review`, `market-definer`, `gber-screener`, `merger-screener`, `dawn-raid-advisor`, `eu-liability-advisor` |
| `eu-institutional-management` | Institutional Management | `head-of-unit`, `deputy-head-of-unit`, `assistant-hod`, `hr-contract-manager-ta`, `financial-officer`, `pmo-pension-specialist`, `cdr-drafter`, `amp-drafter`, `aar-drafter`, `selection-board`, `access-to-documents`, `underperformance-advisor`, `budget-planner` |
| `eu-trade` | Trade Defence | `trade-defence-investigator`, `dumping-margin-calculator`, `sanctions-screener` |
| `eu-grants-enforcement` | Grants, Procurement & Enforcement | `grant-manager`, `infringement-officer`, `infringement`, `procurement-expert`, `lfn-drafter`, `transposition-tracker`, `reasoned-opinion-drafter`, `grant-audit-advisor`, `grant-amendment-officer`, `tender-evaluator`, `olaf-referral-advisor`, `direct-award-advisor`, `eppo-jurisdiction-advisor`, `cohesion-fund-manager` |
| `eu-data-communication` | Data & Communication | `data-analyst`, `communication-officer`, `lines-to-take-drafter`, `digit-project-manager`, `data-steward`, `cybersecurity-officer`, `transparency-officer` |
| `eu-simulation` | EU Institutional Simulation | `commissioner`, `college-deliberation`, `inter-service-consultation`, `trilogue`, `legislative-cycle`, `european-parliament`, `council-eu`, `coreper`, `qmv-calculator`, `advocate-general`, `council-presidency`, `mandate-conflict`, `red-team-college`, `subsidiarity-stress`, `timeline` |
| `eu-privacy` | Data Protection & Privacy | `dpia`, `dpo`, `it-project-manager`, `it-security`, `legal-officer`, `it-security-plan`, `data-breach-officer`, `ropa-drafter`, `ai-act-officer`, `tia-expert`, `retention-schedule`, `privacy-notice-drafter`, `data-subject-rights`, `edps-complaint-handler`, `ai-governance-officer` |
| `eu-careers` | EU Careers & EPSO Preparation | `epso-grade`, `epso-presentation`, `epso-offer` |

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
4. Update the commissioner shortnames grid in `plugins/eu-simulation/CLAUDE.md`.

**To add a new skill:**
1. Create `plugins/<domain>/skills/<skill-name>/SKILL.md` using the SKILL.md frontmatter convention.
2. Register it in `plugins/<domain>/.claude-plugin/plugin.json` under `"skills"`.
3. Add a row to the Playbook table in `plugins/<domain>/CLAUDE.md`.

**To add a new domain plugin:**
Follow the full procedure in [CONTRIBUTING.md](CONTRIBUTING.md) — scaffold, manifest, practice profile, cold-start interview, hook symlink, marketplace registration.
