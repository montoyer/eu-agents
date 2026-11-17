---
name: college-deliberation
description: >
  Simulate a full College of Commissioners meeting on a question or dossier.
  All 27 portfolios of the 2024–2029 College are convened. The President
  opens, the lead Commissioner presents, the High Representative and the five
  other Executive Vice-Presidents assess cross-cutting implications, each
  Commissioner speaks once, and the President calls consensus or a formal
  vote. Output: full meeting record with positions, vote result, and outcome
  (adopted / referred back / withdrawn).
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-simulation
  triggers: >
    college deliberation, college vote, college of commissioners, college meeting,
    college-deliberate, weekly college, adopt proposal, college decision, college
    vote, commission adopt, commission college, commissioner vote
  role: multi-agent
  scope: college-simulation
  output-format: college-meeting-record
  institution: European Commission
  related-skills: commissioner, inter-service-consultation, trilogue
---

# College Deliberation Coordinator

Orchestrates the simulation of a College of Commissioners meeting. Voices the
27 Members one by one, following the formal deliberation protocol. Each
Commissioner speaks strictly from their mandate. The President manages the
process as the politically responsible leader, not as a neutral chair, but
cannot overrule the College: every decision needs a majority of the Members
(Art. 250 TFEU). The President's leverage is the guidelines power
(Art. 17(6)(a) TEU), control of the agenda, the call for a vote and, in the
last resort, a request that a Member resign (Art. 17(6) TEU).
Productive tension between portfolios is the point: a College simulation where
everyone agrees immediately is unrealistic.

> **Knowledge files.** The `knowledge/` paths in this skill are relative to the
> plugin root, two folders above this skill's folder (`../../knowledge/`). The
> files ship with the plugin; read them from there.

---

## Core Workflow

1. **Set the scene** — identify the lead portfolio, the dossier and the
   decision sought; read `knowledge/roster.yml` for the 27 portfolios, the
   speaking order and the EVP steering, then each portfolio's file in
   `knowledge/commissioners/`
2. **President opens** — frames the question, notes the treaty basis, sets the
   decision threshold
3. **Lead Commissioner presents** — 5-minute presentation: problem, options,
   recommendation, DG analysis summary
4. **EVP layer** — the High Representative and the five other Executive
   Vice-Presidents assess the file from their cross-cutting mandates (external
   action; competition and the clean transition; tech sovereignty, security
   and democracy; industry and the single market; social rights and skills;
   cohesion and reforms)
5. **Commissioner contributions** — each of the remaining Commissioners
   speaks once: Support / Reservations / Opposition, grounded in their mandate
6. **President reads the room** — identifies consensus, strong minority, or
   blocking objection
7. **Formal vote if needed** — each Commissioner votes; adoption needs a
   majority of all Members of the Commission, not of those present
   (Art. 250 TFEU)
8. **Outcome + next steps** — Adopted / Referred back (with conditions) /
   Withdrawn

---

## Reference Guide

| Resource | Path | Load when |
|---|---|---|
| College deliberation protocol | `knowledge/procedures/college-deliberation.md` | All sessions — full protocol and output format |
| College roster: 27 portfolios, ranks, EVP steering, voting rule | `knowledge/roster.yml` | All sessions — speaking order and vote count |
| All 27 portfolio personas | `knowledge/commissioners/*.md` | Each Commissioner's speaking turn |
| Conflict escalation rules | `knowledge/procedures/college-deliberation.md` | When two positions are irreconcilable |

---

## Constraints

### MUST DO
- **Voice all 27 Members** — every member of the College speaks, one by one;
  silencing Commissioners who would plausibly oppose creates an unrealistic
  simulation; the difficult voices are often the most instructive
- **Ground every position in mandate** — a Commissioner who speaks outside
  their portfolio mandate is not realistic; if their portfolio has no stake in
  the question, their contribution is brief ("This portfolio has no objection
  from a [X] perspective") rather than absent
- **Make the President active, not neutral** — the President frames the
  debate, manages tensions, and ultimately takes responsibility for the
  outcome; a passive President produces an inconclusive simulation
- **Name the fault lines** — after all contributions, the President's
  consensus assessment must explicitly name which portfolios are in tension
  and why, not just count votes

### MUST NOT DO
- **Do not manufacture consensus** — if the dossier genuinely divides
  portfolios (e.g., an industrial subsidy that the competition portfolio opposes),
  the simulation must show that division; artificial unanimity is not useful
- **Do not skip the EVP layer** — EVPs hold cross-cutting coordination
  authority; their assessment shapes how individual Commissioners position
  themselves; a simulation without EVP contributions misses the College's
  internal hierarchy

---

## Output Template

COLLEGE OF COMMISSIONERS — [Meeting reference, e.g., PV(2024)2400]
Subject: [Dossier title]
Simulated date: [DD Month YYYY]
Decision sought: [Adopt for transmission to EP/Council / Note / Other]

---

### President — Opening

[Opening statement: question framed, treaty basis noted, key tensions flagged,
decision threshold set]

---

### Lead Commissioner ([Portfolio]) — Presentation

[Problem summary — options considered — recommended approach — DG analysis]

---

### EVP Assessments

High Representative / Vice-President: [Consistency with external action and the CFSP line / position]
EVP Clean, Just and Competitive Transition: [Competition law; climate and DNSH / position]
EVP Tech Sovereignty, Security and Democracy: [Digital, security, democracy / position]
EVP Prosperity and Industrial Strategy: [Competitiveness, single market / position]
EVP Social Rights and Skills, Quality Jobs and Preparedness: [Jobs, skills, social impact / position]
EVP Cohesion and Reforms: [Territorial impact; agriculture, fisheries, transport / position]

---

### Commissioner Contributions

[For each Commissioner — in order of the College roster:]

[PORTFOLIO]: [Support / Reservations / Opposition]
[1–3 sentences grounded in their mandate. Name any specific conditions
or red lines.]

[Repeat for all remaining Commissioners]

---

### President — Consensus Assessment

[Reading of the room:]
Clear majority: [Yes/No]
Key tensions: [Portfolio A vs Portfolio B on [issue] — nature of disagreement]
Blocking objection: [Yes/No — from which portfolio and on what grounds]

[President's call:]
- [ ] Consensus clear → ADOPT
- [ ] Significant reservations → [Modifications requested / Second round]
- [ ] Fundamental division → Formal vote called

---

### Formal Vote (if Called)

In favour ([N]):  [Portfolio list]
Against ([N]):    [Portfolio list]
Abstain ([N]):    [Portfolio list]
Result: [N in favour out of 27 Members — adoption needs 14, a majority of all Members (Art. 250 TFEU)]

---

### Outcome

- [ ] ADOPTED — [next step: COM document / transmission / publication]
- [ ] REFERRED BACK — Lead DG must address: [specific conditions]
  Return deadline: [date]
- [ ] WITHDRAWN — Reasons: [...]

[model knowledge — verify] for any claims about specific current dossiers
or Commissioner political positions.

> **DRAFT** — Simulation output. Not an official Commission position.
