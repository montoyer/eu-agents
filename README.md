# Agents for EU

> 30,000 EU staff. 21 Commissioners. 70 years to build. Now running on your laptop.

<div align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjByaDMyMXFqcmo4aXZxNWVwdHJzbXZlZnN4bWEzNmp3b3g2Z3doeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/UqASWHeU91ADUSk5co/giphy.gif" width="520" alt="EU Commission in session"/>
</div>

<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=montoyer&color=0052cc&style=flat-square&label=views)
&nbsp;
![GitHub Stars](https://img.shields.io/github/stars/montoyer/agents?style=flat-square&color=gold&label=stars)
&nbsp;
![Last Commit](https://img.shields.io/github/last-commit/montoyer/agents?style=flat-square&color=brightgreen&label=last+commit)
&nbsp;
![License](https://img.shields.io/github/license/montoyer/agents?style=flat-square&color=lightgrey)

</div>

---

Inspired by [gstack](https://github.com/garrytan/gstack) — which turns Claude Code into a virtual engineering team — **Agents for EU** models the entire European Commission as a structured system of specialized AI agents: one per Commissioner portfolio, backed by Directorate-General agents, wired together through the EU's real legislative and policy workflows.

The goal is not satire. It is a serious attempt to simulate how the EU Commission thinks, deliberates, and produces policy — and to use that simulation as a tool for research, policy drafting, scenario testing, and civic education.

---

## Why this exists — the non-obvious insight

> **The EU Commission is not primarily a regulatory body. It is the most sophisticated structured argumentation engine ever built by human institutions.**

Every regulation it produces is the residue of a scored debate across 21 mandates, each grounded in a different treaty basis, each representing a different theory of what the EU is for. Competition law versus industrial policy. Climate targets versus energy security. Digital sovereignty versus open markets. The College does not resolve these tensions by consensus — it forces them to a legally defensible equilibrium, on the record, with citations.

That structure is the insight. The EU's deliberative machinery — subsidiarity tests, inter-service consultation, impact assessments, trilogue — is a **general-purpose scaffold for high-stakes collective reasoning**. It was designed for policy, but it works on any problem where multiple legitimate perspectives must be reconciled under constraint.

This repository makes that scaffold programmable. The use case is not "simulate the EU." The use case is: **use EU deliberative procedure as a reasoning framework for any domain where the quality of a decision depends on how many well-grounded objections it has survived.**

Practically, this means the system's most powerful commands are not the single-agent skill invocations but the **compound commands** that only work because 21 agents are running in parallel with conflicting mandates:

| Command | What it does that a single agent cannot |
|---|---|
| `/mandate-conflict <proposal>` | Identifies every structurally guaranteed conflict between Commissioner portfolios, with the legal basis for each position |
| `/red-team-college <proposal>` | Runs a proposal through all 21 Commissioners, returns only the severe objections — token-efficient College stress test |
| `/subsidiarity-stress <proposal>` | Tests the same proposal against 5 different member-state configurations to find where the subsidiarity check fails |
| `/timeline <proposal>` | Produces a realistic OLP timeline with blocking dependencies, QMV thresholds, and trilogue risk points |

See [NOI.md](NOI.md) for the full argument.

---

## What this is

| Layer | What it models |
|---|---|
| **Commissioners** | 21 portfolio agents, each with mandate, legal basis, political persona |
| **DGs** | Operational directorate agents that produce technical analysis |
| **Skills** | Reusable EU policy tools: impact assessment, consultation, treaty check… |
| **Workflows** | End-to-end processes: ordinary legislative procedure, budget cycle, infringement |
| **Agents** | Multi-agent sessions: College deliberation, trilogue, inter-service consultation |
| **Institutions** | Counter-party agents: Parliament, Council, ECJ, ECB, EEAS |

---

## Quick start

```bash
# Ask the President to open a policy initiative
/president

# Run a full College deliberation on a topic
/college-deliberation "Should the EU ban algorithmic pricing in retail?"

# Draft a legislative proposal via the standard workflow
/legislative-proposal "Regulation on synthetic biology"

# Stress-test a policy against all Commissioner portfolios
/impact-assessment "Carbon border adjustment expansion to agriculture"

# --- Compound commands (multi-agent only) ---

# Find every structurally guaranteed conflict across 21 portfolios
/mandate-conflict "Regulation on AI liability in critical infrastructure"

# Run all 21 Commissioners, surface only severe objections
/red-team-college "Carbon border adjustment expansion to agriculture"

# Test subsidiarity failure across 5 member-state configurations
/subsidiarity-stress "Harmonised insolvency rules for SMEs"

# Produce a realistic OLP timeline with blocking dependencies
/timeline "Platform regulation for financial services"
```

---

## Repository layout

```
agents-for-EU/
├── CLAUDE.md                       ← how to operate this system
├── ARCHITECTURE.md                 ← design rationale & extension guide
├── CONTRIBUTING.md                 ← how to extend the system
├── CONNECTORS.md                   ← MCP connector catalogue
├── QUICKSTART.md                   ← 5-minute onboarding guide
├── SKILL.md                        ← SKILL.md authoring standard
├── marketplace.json                ← plugin registry for /plugin install
│
├── plugins/                        ← installable skill packages
│   ├── legislative-eu/             ← Policy, legislative drafting, ISC, PQ
│   ├── competition-eu/             ← Antitrust, state aid, Legal Service
│   ├── institutional-management-eu/← Unit management, HR, finance, CDR
│   ├── trade-eu/                   ← Trade defence instruments
│   ├── grants-enforcement-eu/      ← Grants, infringement, procurement
│   ├── data-communication-eu/      ← Data analysis, press, speeches
│   ├── simulation-eu/              ← Commissioner personas, College, trilogue, OLP
│   └── privacy-eu/                 ← DPIA workflow, DPO, IT security, legal officer
│       Each contains:
│           CLAUDE.md               ← domain practice profile
│           .claude-plugin/         ← plugin.json manifest
│           skills/<name>/SKILL.md  ← individual skills
│           skills/cold-start-interview/ ← plugin onboarding skill
│           hooks/                  ← symlinks to lib/hooks/
│           references/             ← reference documents loaded by skills
│
├── knowledge/                      ← EU institutional knowledge base
│   ├── commissioners/              ← 21 Commissioner agent definitions + _template.md
│   ├── dgs/                        ← 17 Directorate-General operational agents
│   ├── institutions/               ← Counter-party agents (EP, Council, ECJ, ECB, EEAS, European Council)
│   ├── workflows/                  ← End-to-end policy processes (legislative-cycle, policy-cycle)
│   └── agents/                     ← Multi-agent session definitions (college, ISC, trilogue, DPIA, EDPS)
│
├── lib/                            ← Shared technical assets
│   ├── hooks/                      ← Event hook shell scripts
│   │   ├── post-output-disclaimer.sh
│   │   ├── post-subsidiarity-prompt.sh
│   │   ├── post_tool_use_citation_matcher.sh
│   │   ├── post_tool_use_eurlex_resolver.sh
│   │   └── pre-legal-basis-check.sh
│   └── legacy-skills/              ← Pre-SKILL.md flat skills (pending conversion)
│
└── docs/                           ← Guides and reference material
    ├── getting-started.md
    ├── glossary.md
    ├── using-skills-beginners-guide.md
    └── examples/                   ← Worked end-to-end simulations
        ├── ai-act-simulation/
        ├── green-deal-package/
        └── migration-policy/
```

---

## Design principles

**One agent per mandate.** Each Commissioner's agent is scoped strictly to its treaty-based competence. The Competition Commissioner cannot speak for Agriculture; the President arbitrates conflicts.

**Real procedures, not shortcuts.** Workflows follow actual EU procedures — subsidiarity checks, impact assessments, inter-service consultations — so outputs are structurally realistic.

**Adversarial by design.** Commissioners disagree. The Council pushes back. Parliament amends. The system is built for productive tension, not rubber-stamping.

**Composable.** Every skill, commissioner, and workflow can be invoked standalone or composed into larger multi-agent sessions.

---

## Use cases

- **Policy research** — Simulate how a new regulation would be received across all Commission portfolios before it is written. `/mandate-conflict` finds the structural fault lines in under a minute.
- **Legislative drafting** — Use `/legislative-proposal` to produce a structurally compliant draft from a one-line brief; use `/red-team-college` to find the objections that will survive committee.
- **Education** — Walk students through the full ordinary legislative procedure with live agent interactions; `/timeline` makes the blocking dependencies visible.
- **Scenario testing** — Test geopolitical shocks, climate events, or market crises against the College's deliberative capacity. `/subsidiarity-stress` reveals when a proposed EU intervention loses its legal justification.
- **General-purpose structured reasoning** — Use EU deliberative procedure as a scaffold for any high-stakes collective decision outside government: a corporate strategy review, a standards body proposal, a research consortium priority-setting. The scaffold works whenever multiple legitimate perspectives must survive adversarial scrutiny under constraint.
- **Civic tech** — Build tools that explain EU decisions in plain language by running them backward through the agents that produced them.

---

## Status

Early scaffolding. Commissioners and core skills are defined; multi-agent orchestration and tooling are in active development.

<div align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHVzbnVxZm95anh5c2gydjBtb3FwMDl5YmFzajloZzZnOHgzNXVlayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohze27VlwTv7VmoTe/giphy.gif" width="360" alt="The College is deliberating..."/>
  <br/>
  <sub><i>The College is deliberating. Stand by.</i></sub>
</div>

---

## Spread the word

If this project is useful to you — or just makes you smile — help it reach more people.

<div align="center">

[![GitHub Stars](https://img.shields.io/github/stars/montoyer/agents?style=for-the-badge&color=gold&label=⭐%20Star%20this%20repo)](https://github.com/montoyer/agents/stargazers)

</div>

Every star increases the project's visibility and helps researchers, policy wonks, and civic technologists find it. It takes one click and means a lot.

---

## License

MIT
