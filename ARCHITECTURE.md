# Architecture

## Overview

Agents for EU is a layered multi-agent framework. The layers map directly onto the European Commission's actual institutional structure: political leadership (Commissioners), technical administration (DGs), procedural instruments (skills), and inter-institutional relationships (institutions).

```
┌─────────────────────────────────────────────────────┐
│                    USER / RESEARCHER                │
└───────────────────────┬─────────────────────────────┘
                        │ invokes skill, workflow, or agent
┌───────────────────────▼─────────────────────────────┐
│                   SKILLS LAYER                      │
│  impact-assessment · legislative-proposal ·         │
│  treaty-check · consultation · state-aid-review …  │
└───────────────────────┬─────────────────────────────┘
                        │ delegates to
          ┌─────────────┴──────────────┐
          │                            │
┌─────────▼──────────┐    ┌────────────▼────────────┐
│  COMMISSIONER LAYER│    │      DG LAYER           │
│  27 portfolio agents│   │  17 directorate agents  │
│  Political mandate  │   │  Technical analysis     │
│  Treaty competence  │   │  Legal framing, data    │
└─────────┬──────────┘    └────────────┬────────────┘
          │                            │
          └─────────────┬──────────────┘
                        │ coordinates via
┌───────────────────────▼─────────────────────────────┐
│                  AGENTS LAYER                       │
│  college-deliberation · inter-service-consultation  │
│  trilogue · task-force                             │
└───────────────────────┬─────────────────────────────┘
                        │ negotiates with
┌───────────────────────▼─────────────────────────────┐
│               INSTITUTIONS LAYER                    │
│  European Parliament · Council · ECJ · ECB · EEAS   │
└─────────────────────────────────────────────────────┘
```

---

## Layer 1 — Skills

Skills are **stateless, procedural tools**. They take a brief as input, run a structured procedure, and return a formatted output. They are the atomic unit of the system — composable, reusable, and invocable standalone.

Each skill file defines:
- **Trigger**: the slash command name
- **Inputs**: what the user must provide
- **Procedure**: step-by-step process the agent follows
- **Output format**: what the deliverable looks like
- **Legal/procedural references**: which TFEU articles, Better Regulation tools, or EU templates apply

### Skill catalog

| Skill | Output | Key reference |
|---|---|---|
| `impact-assessment` | Staff Working Document (SWD) | Better Regulation Toolbox |
| `legislative-proposal` | Draft regulation or directive | OLP template, TFEU Art. 294 |
| `treaty-check` | Legal opinion | TFEU, subsidiarity protocol |
| `consultation` | Consultation summary | Better Regulation guidelines |
| `state-aid-review` | Compatibility decision | TFEU Art. 107-109 |
| `comitology` | Committee opinion | Regulation 182/2011 |
| `infringement` | Reasoned opinion draft | TFEU Art. 258 |
| `sdg-alignment` | SDG mapping | UN 2030 Agenda |
| `better-regulation` | Regulatory fitness check | REFIT platform |
| `review` | Evaluation report | SWD evaluation template |

---

## Layer 2 — Commissioners

Commissioner agents are **persona-bound political agents**. Each holds a portfolio derived from the treaties, has a defined set of dossiers, a decision-making style, and known tensions with other portfolios.

### Commissioner agent file structure

Each portfolio file starts with a YAML header that repeats its `id`, `rank` and
`title` from `knowledge/roster.yml`; `scripts/validate.sh` fails if they differ.
Template: `knowledge/commissioners/_template.md`.

```markdown
---
id: clean-transition
kind: commissioner
rank: evp                      # president | hrvp | evp | commissioner
title: "Executive Vice-President for a Clean, Just and Competitive Transition"
lead_dgs: [COMP]
treaty_basis: "Arts. 101–109 TFEU; Arts. 191–194 TFEU"
as_of: 2026-11-17
verified: false
---

# [Official portfolio title]

## Mandate
[Treaty basis, scope of competence, key instruments administered]

## Political priorities
[From the Political Guidelines and the mission letter]

## Decision style
[How the portfolio weighs trade-offs]

## Key dossiers
[Files live at the as_of date]

## Tensions with other portfolios
[vs. <portfolio id>: why the two mandates collide]

## Supporting DG
[Which Directorate-General provides technical support]

## Agent behavior
[Specific instructions for how this agent should respond]
```

### The College hierarchy

The real 2024–2029 College: 27 portfolios, modelled by portfolio and never by
the person who holds it. Generated from `knowledge/roster.yml`; steering is
model knowledge to verify against the mission letters of 17 September 2024.

```
President of the European Commission (president)
├── High Representative of the Union for Foreign Affairs and Security Policy / Vice-President (high-representative)
│     ├─ steers enlargement
│     ├─ steers mediterranean
│     ├─ steers international-partnerships
│     ├─ steers defence-space
│     └─ steers preparedness
├── Executive Vice-President for a Clean, Just and Competitive Transition (clean-transition)
│     ├─ steers climate
│     ├─ steers energy
│     └─ steers environment
├── Executive Vice-President for Tech Sovereignty, Security and Democracy (tech-sovereignty)
│     ├─ steers defence-space
│     ├─ steers internal-affairs
│     ├─ steers justice
│     └─ steers research-innovation
├── Executive Vice-President for Prosperity and Industrial Strategy (industrial-strategy)
│     ├─ steers economy
│     ├─ steers financial-services
│     ├─ steers research-innovation
│     └─ steers trade
├── Executive Vice-President for Social Rights and Skills, Quality Jobs and Preparedness (social-rights)
│     ├─ steers youth-culture
│     ├─ steers preparedness
│     └─ steers health
├── Executive Vice-President for Cohesion and Reforms (cohesion)
│     ├─ steers agriculture
│     ├─ steers fisheries
│     └─ steers transport
│
├── Commissioner for Trade and Economic Security; Interinstitutional Relations and Transparency (trade)
├── Commissioner for Economy and Productivity; Implementation and Simplification (economy)
├── Commissioner for Enlargement (enlargement)
├── Commissioner for Climate, Net Zero and Clean Growth (climate)
├── Commissioner for Energy and Housing (energy)
├── Commissioner for Defence and Space (defence-space)
├── Commissioner for the Mediterranean (mediterranean)
├── Commissioner for Internal Affairs and Migration (internal-affairs)
├── Commissioner for Democracy, Justice, the Rule of Law and Consumer Protection (justice)
├── Commissioner for Financial Services and the Savings and Investments Union (financial-services)
├── Commissioner for Startups, Research and Innovation (research-innovation)
├── Commissioner for Environment, Water Resilience and a Competitive Circular Economy (environment)
├── Commissioner for Agriculture and Food (agriculture)
├── Commissioner for Fisheries and Oceans (fisheries)
├── Commissioner for Health and Animal Welfare (health)
├── Commissioner for International Partnerships (international-partnerships)
├── Commissioner for Budget, Anti-Fraud and Public Administration (budget)
├── Commissioner for Sustainable Transport and Tourism (transport)
├── Commissioner for Intergenerational Fairness, Youth, Culture and Sport (youth-culture)
└── Commissioner for Equality; Preparedness and Crisis Management (preparedness)
```

---

## Layer 3 — Directorate-Generals (DGs)

DG agents are **technical-analytical agents**. They do not hold political positions; they produce the analysis, legal framing, data synthesis, and options papers that Commissioner agents rely on.

A DG agent's output is always attributed: "DG COMP analysis shows…", "DG ENV assessment finds…". This mirrors the real Commission, where political decisions are distinct from technical preparation.

### DG-to-Commissioner mapping

| DG | Portfolio (roster id) |
|---|---|
| DG COMP (Competition) | EVP for a Clean, Just and Competitive Transition (`clean-transition`) |
| DG CNECT | EVP for Tech Sovereignty, Security and Democracy (`tech-sovereignty`) |
| DG GROW | EVP for Prosperity and Industrial Strategy (`industrial-strategy`) |
| DG EMPL | EVP for Social Rights and Skills, Quality Jobs and Preparedness (`social-rights`) |
| DG REGIO | EVP for Cohesion and Reforms (`cohesion`) |
| DG TRADE | Trade and Economic Security (`trade`) |
| DG TAXUD | Climate, Net Zero and Clean Growth for taxation (`climate`); Trade for customs (`trade`) |
| DG ENER | Energy and Housing (`energy`) |
| DG HOME | Internal Affairs and Migration (`internal-affairs`) |
| DG JUST | Democracy, Justice, the Rule of Law and Consumer Protection (`justice`); Equality (`preparedness`) |
| DG RTD | Startups, Research and Innovation (`research-innovation`) |
| DG ENV | Environment, Water Resilience and a Competitive Circular Economy (`environment`) |
| DG AGRI | Agriculture and Food (`agriculture`) |
| DG SANTE | Health and Animal Welfare (`health`) |
| DG BUDG | Budget, Anti-Fraud and Public Administration (`budget`) |
| OLAF | Political responsibility of `budget`; independent in its investigations |
| DG MOVE | Sustainable Transport and Tourism (`transport`) |

The other lead services named in the portfolio files (ECFIN, CLIMA, DEFIS,
ENEST, MENA, INTPA, FISMA, MARE, EAC, ECHO, HERA, the EEAS) have no DG profile
yet.

---|---|
| DG COMP (Competition) | Commissioner for Competition |
| DG TRADE | Commissioner for Trade |
| DG AGRI | Commissioner for Agriculture |
| DG SANTE | Commissioner for Health |
| DG ENER | Commissioner for Energy |
| DG MOVE | Commissioner for Transport |
| DG REGIO | Commissioner for Regional Development |
| DG RTD | Commissioner for Research & Innovation |
| DG EMPL | Commissioner for Employment |
| DG BUDG | Commissioner for Budget |
| DG ENV | Commissioner for Environment |
| DG JUST | Commissioner for Justice |
| DG HOME | Commissioner for Home Affairs |
| DG GROW | Commissioner for Internal Market |
| DG TAXUD | Commissioner for Internal Market (taxation) |
| DG CONNECT | EVP for Digital |

---

## Layer 4 — Agents (multi-agent sessions)

Multi-agent sessions coordinate multiple Commissioner and DG agents in a defined procedure.

### College deliberation

The most important multi-agent session. Simulates the weekly College meeting where all Commissioners vote on proposals.

**Protocol:**
1. Rapporteur Commissioner presents the dossier (3 min).
2. Each Commissioner speaks once (1 min) — support, reservations, or opposition.
3. President identifies consensus or calls a formal vote.
4. Outcome: adopted, referred back, or withdrawn.

### Inter-service consultation (ISC)

When a lead DG prepares a proposal, it circulates to all affected DGs for written opinions. This agent session simulates that circulation:

1. Lead DG circulates draft.
2. Each affected DG returns a written opinion (agreement, reservations, opposition).
3. Lead DG produces a synthesis and revises the draft.
4. Second round if needed.

### Trilogue

Simulates the informal inter-institutional negotiation between Commission, Parliament (rapporteur + shadow rapporteurs), and Council (Presidency + member state delegations):

1. Commission defends its proposal.
2. Parliament presents its amendments.
3. Council presents its general approach.
4. Rounds of compromise text negotiation.
5. Political agreement or breakdown.

### Task force

Ad-hoc multi-DG working group convened by the President or an EVP for cross-cutting issues (e.g., AI governance cutting across CONNECT, COMP, JUST, HOME).

---

## Layer 5 — Institutions

Counter-party agents representing EU bodies outside the Commission. They receive Commission proposals and respond according to their institutional role and political dynamics.

| Institution | Role in the system |
|---|---|
| European Parliament | Amends legislation, holds democratic accountability |
| Council of the EU | Represents member states, adopts legislation jointly with EP |
| European Council | Sets strategic direction, no legislative function |
| Court of Justice (ECJ) | Rules on legality, interprets treaties |
| European Central Bank | Monetary policy, consulted on financial legislation |
| EEAS | External relations, implements foreign policy |

---

## Data flow for a legislative proposal

```
User brief
    │
    ▼
/legislative-proposal skill
    │
    ├── DG (lead) produces technical options paper
    │
    ├── /impact-assessment skill runs on preferred option
    │
    ├── /treaty-check skill validates legal basis
    │
    ├── /consultation skill simulates stakeholder round
    │
    ├── /inter-service-consultation circulates to all DGs
    │
    ├── Lead Commissioner endorses and signs
    │
    ├── /college-deliberation votes on adoption
    │
    └── OUTPUT: draft legislative text (regulation/directive)
              + explanatory memorandum
              + impact assessment SWD
              + consultation summary
```

---

## Extension guide

### Adding a commissioner
1. Copy `knowledge/commissioners/_template.md`.
2. Fill in mandate, legal basis, priorities, tensions.
3. Add to the roster in `knowledge/agents/college-deliberation.md`.
4. Link to the corresponding DG file in `knowledge/dgs/`.

### Adding a skill
1. Create `plugins/<domain>/skills/<skill-name>/SKILL.md` using the SKILL.md frontmatter convention.
2. Define: trigger, inputs, step-by-step procedure, output format.
3. Cite the EU procedure or legal instrument it models.
4. Register the skill name in `plugins/<domain>/.claude-plugin/plugin.json`.

### Adding a workflow
1. Create `knowledge/workflows/my-workflow.md`.
2. Define the sequence of skills and agents to invoke, with data passed between steps.
3. Note any decision gates (e.g., College must adopt before proceeding).

### Adding an institution
1. Create `knowledge/institutions/my-institution.md`.
2. Define: treaty role, decision procedure, political dynamics, how it receives Commission input.

---

## Design decisions

**Why model DGs separately from Commissioners?**
The real Commission separates political direction (Commissioner) from technical administration (DG). A Commissioner can override their DG's recommendation — that tension is interesting and productive. Conflating them loses it.

**Why follow real EU procedures?**
Procedural fidelity is what makes the outputs useful. A "legislative proposal" that skips the impact assessment and subsidiarity check is not an EU legislative proposal. The constraints are features, not friction.

**Why adversarial by design?**
The Commission's college system requires unanimity or qualified majority. That means dissent matters. A system that always converges to agreement misses the entire point of collegiate governance.

**Why no LLM orchestration framework (LangChain, CrewAI…)?**
The system is built as markdown prompts consumed by Claude Code. This keeps it lightweight, inspectable, and version-controllable. Orchestration happens through Claude's native multi-agent capabilities (subagents, MCP). If the project grows, a TypeScript orchestration layer can be added without changing the agent definitions.
