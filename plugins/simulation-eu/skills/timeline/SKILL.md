---
name: timeline
description: >
  Given a proposed regulation or directive, produce a realistic OLP timeline
  from Commission pre-proposal through OJ publication. The timeline identifies:
  phase durations (with realistic variance ranges), blocking dependencies
  (which step must complete before the next can begin), QMV thresholds
  (the member-state arithmetic needed for a Council general approach),
  and trilogue risk points (where EP and Council positions are structurally
  incompatible and agreement is not assured). Output: a structured timeline
  with milestones, dependency graph, and risk flags.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-simulation
  triggers: >
    timeline, legislative timeline, OLP timeline, how long will this take,
    when will this be adopted, legislative schedule, regulation timeline,
    directive timeline, procedural timeline, adoption timeline, blocking
    dependencies, QMV threshold, trilogue risk, legislative calendar
  role: workflow-analysis
  scope: legislative-timeline
  output-format: timeline-with-risk-flags
  institution: European Commission / European Parliament / Council of the EU
  related-skills: legislative-cycle, council-eu, european-parliament, trilogue,
    mandate-conflict, subsidiarity-stress
---

# Legislative Timeline Modeller

Produces a realistic Ordinary Legislative Procedure timeline for a proposed
regulation or directive. The output goes beyond a phase list: it identifies
blocking dependencies (steps that cannot begin until a prior step is complete),
QMV arithmetic (which member-state coalitions can block a Council general
approach), and trilogue risk points (where EP and Council positions are
structurally incompatible and a political agreement is not guaranteed).

The timeline is not optimistic. Most OLP dossiers take 3–5 years from
Commission initiative to OJ publication. Contentious dossiers (energy,
migration, digital markets, financial regulation) routinely take 5–7 years
or fail entirely. The model uses realistic variance ranges, not best-case
scenarios, and flags where the dossier has characteristics associated with
delay or failure.

---

## Core Workflow

1. **Parse the proposal** — identify: instrument (regulation/directive/decision),
   legal basis, decision rule (QMV or unanimity), policy domain, political
   sensitivity, and whether the proposal pre-empts existing national legislation
2. **Determine the procedural path** — OLP (Art. 294 TFEU) is default for
   shared competence; identify any SLP or consent procedure requirements;
   flag if unanimity applies in Council (changes timeline significantly)
3. **Model Commission pre-proposal phase** (Phase 1)
   - Impact assessment: 12–18 months typically; 6 months minimum if fast-tracked
   - Public consultation: 12 weeks mandatory; longer for sensitive dossiers
   - Inter-service consultation: 8–12 weeks; flag if high-conflict portfolios
     are involved (use `/mandate-conflict` analysis if available)
   - College deliberation: 2–4 weeks; flag if SIGNIFICANT/SEVERE objections
     are likely
   - Blocking dependency: College vote cannot occur before ISC is closed
4. **Model EP first reading phase** (Phase 2)
   - Committee referral and rapporteur appointment: 2–3 months
   - Rapporteur draft report: 3–6 months
   - Committee vote: variable; 6–18 months from referral typical
   - Plenary vote: 2–4 months after committee
   - Total Phase 2 range: 12–24 months
   - Blocking dependency: EP cannot vote until Commission proposal is formally
     transmitted (COM document published)
   - Risk flag: assess whether the dossier is likely to see high-volume
     amendments (indicator of contested EP phase)
5. **Model Council first reading phase** (Phase 3)
   - Working party examination: 3–12 months depending on technical complexity
   - COREPER: 1–3 months
   - Council vote (QMV arithmetic — see below): 1–2 months
   - Total Phase 3 range: 6–24 months
   - QMV check: 55% of member states (15/27) representing 65% of EU population;
     blocking minority = 4 member states representing 35% of population
   - Blocking dependency: Council general approach typically precedes trilogue
     mandate; without it, the Presidency cannot negotiate
6. **Model trilogue** (Phase 4 — replaces second reading in ~90% of dossiers)
   - Political agreement typical range: 6–18 months; 24+ months for contested
     dossiers
   - Number of rounds: 3–8 typical; 10+ for difficult dossiers
   - Risk flag: identify trilogue risk points (see below)
   - Blocking dependency: trilogue cannot begin without both an EP mandate
     and a Council general approach
7. **Model formal adoption and publication** (Phase 5–6)
   - EP confirmation + formal Council adoption: 3–6 months after political
     agreement
   - Legal-linguistic revision: 3–6 months
   - OJ publication: 1 month
   - Entry into force: 20th day after OJ publication (or date in the act)
   - Application date: typically 12–24 months after entry into force for
     regulations with implementation requirements; 18–24 months transposition
     deadline for directives
8. **Assemble the timeline** — produce the full timeline with phase dates,
   variance ranges, and milestone dependencies
9. **QMV arithmetic** — for the Council general approach, identify the
   member-state coalitions most likely to form a blocking minority; assess
   whether the policy domain, instrument choice, or specific provisions
   create predictable blocking configurations
10. **Trilogue risk assessment** — identify the provisions where EP and Council
    starting positions are structurally incompatible; assess the probability
    of political agreement within a reasonable timeframe

---

## QMV Arithmetic Reference

Standard QMV (Art. 16 TEU): 55% of member states (15/27) + 65% of EU population
Blocking minority: 4 member states representing 35% of EU population

Key blocking configurations to assess:
- **Large-state blocking minority**: DE + FR + IT or DE + FR + ES — covers
  35%+ of population easily; requires only 3 large states
- **Eastern bloc**: PL + HU + CZ + SK + RO — combined population ~95M;
  not sufficient alone but significant in coalition
- **Nordic/Baltic**: SE + DK + FI + EE + LV + LT — aligned on regulatory
  quality and digital but below population threshold alone
- **Mediterranean**: IT + ES + PT + GR + MT + CY — large combined population;
  relevant for agriculture, fisheries, migration dossiers

For unanimity dossiers: any single member state can block; flag the MS most
likely to exercise veto given the dossier content.

---

## Trilogue Risk Points

Flag a provision as a HIGH trilogue risk point if:
- EP's mandate reflects a committee position adopted by a slim majority
  (indicator of unstable mandate)
- Council's general approach contains a qualified-majority reservation note
  from 3+ member states on a specific provision
- The provision touches an EP red line (e.g., fundamental rights, democratic
  oversight, environmental standards) that the Council position does not address
- The Commission's original text has been substantially amended in opposite
  directions by EP and Council (four-column document shows EP + and Council -)

---

## Reference Guide

| Resource | Path | Load when |
|---|---|---|
| Legislative cycle workflow | `knowledge/workflows/legislative-cycle.md` | Full session — phase definitions |
| Council agent | `knowledge/institutions/council-eu.md` | QMV arithmetic (Step 9) |
| EP agent | `knowledge/institutions/european-parliament.md` | Trilogue risk (Step 10) |

---

## Constraints

### MUST DO
- **Use realistic variance ranges, not point estimates** — a timeline that
  says "Phase 2: 18 months" is less useful than "Phase 2: 12–24 months
  (18 months median for this dossier type)"
- **Name the blocking dependencies explicitly** — a timeline without
  dependency notation is just a list of phases; the blocking dependencies
  are what determine the critical path
- **Apply QMV arithmetic** — for the Council phase, identify specific
  likely blocking coalitions; do not just say "QMV required"
- **Flag dossier-specific delay factors** — certain policy domains, instrument
  choices, and political moments are associated with systematic delay; flag
  these explicitly

### MUST NOT DO
- **Do not present a best-case timeline as the base case** — fast-track
  scenarios (Commission initiative to adoption in 18 months) are exceptional
  and should be labelled as such
- **Do not omit the application/transposition deadline** — the adoption date
  is not when the regulation applies; for most regulations with implementation
  requirements, and all directives, there is a further gap

---

## Output Template

LEGISLATIVE TIMELINE
Proposal: [Title / one-line description]
Instrument: [Regulation / Directive / Decision]
Legal basis: [TFEU Art. X] — Decision rule: [QMV / Unanimity]
Procedure: [OLP Art. 294 / SLP — specify]
Lead Commissioner: [Portfolio]
Lead DG: [DG name]
Baseline start: [Estimated Commission initiative date or known date]

Overall timeline estimate: [YEAR–YEAR] — [N–N years total]
Timeline risk: [LOW / MODERATE / HIGH / CRITICAL]

---

### Phase Timeline

| Phase | Description | Duration (range) | Starts | Ends (est.) | Blocking dependency |
|---|---|---|---|---|---|
| 1a | Impact assessment | 12–18 months | [Date] | [Date range] | — |
| 1b | Public consultation | 3 months | After 1a draft | [Date range] | 1a in progress |
| 1c | Treaty check (Legal Service) | 2–3 months | [Date] | [Date range] | 1a near completion |
| 1d | Inter-service consultation | 2–3 months | [Date] | [Date range] | 1a complete |
| 1e | College deliberation | 1 month | After ISC closed | [Date range] | 1d complete |
| COM | Commission proposal published | — | After 1e | [Date] | 1e adopted |
| 2 | EP first reading | 12–24 months | After COM | [Date range] | COM published |
| 3 | Council first reading / GA | 6–24 months | Parallel with EP | [Date range] | COM published |
| T | Trilogue | 6–18 months | After EP + Council mandates | [Date range] | Phase 2 + 3 complete |
| 5 | Formal adoption | 3–6 months | After political agreement | [Date range] | Trilogue complete |
| 6 | OJ publication | 1 month | After formal adoption | [Date range] | Phase 5 complete |
| EIF | Entry into force | 20 days after OJ | [Date range] | [Date range] | OJ published |
| APP | Application / transposition deadline | [12–24 months / 18–24 months] | After EIF | [Date range] | EIF |

**Critical path:** [List the sequence of blocking dependencies that determines
the minimum total duration]

---

### QMV Analysis — Council General Approach

Decision rule: [QMV — 15/27 member states + 65% population]

Likely supportive coalition: [Characterise — which MS groupings are aligned
with the Commission's approach and why]

Blocking minority risk: [LOW / MODERATE / HIGH]

Most probable blocking configuration:
[Name 3–4 member states, their shared concern, and the provision that
triggers it]
Population of this coalition: [~X% of EU population]
Threshold for blocking minority: 35% of EU population
[ABOVE / BELOW threshold — assess likelihood of coalition holding]

[If unanimity: name the member state most likely to exercise veto and on
what grounds]

---

### Trilogue Risk Points

| Provision | EP position (expected) | Council position (expected) | Incompatibility | Risk |
|---|---|---|---|---|
| [Art. X / Topic] | [EP lean] | [Council lean] | [Nature of gap] | [LOW/MED/HIGH] |
| [Repeat] | | | | |

Overall trilogue risk: [LOW / MODERATE / HIGH]
Estimated rounds to agreement: [N–N rounds]
Risk of trilogue breakdown: [LOW / POSSIBLE / SIGNIFICANT]

[If significant trilogue risk: identify the provision where breakdown is most
likely and what a fallback position would require]

---

### Delay Factors

[ ] Unanimity required — adds 12–24 months to Council phase on contested dossiers
[ ] High EP amendment volume expected — extends committee phase by 6–12 months
[ ] Existing national legislation to be pre-empted — elevates Council resistance
[ ] Politically sensitive timing (election cycle, Council Presidency change) —
    may delay Council GA
[ ] Subsidiarity risk — yellow card procedure adds 8 weeks minimum; review may
    add further delay
[ ] Mandate conflict (BLOCKING severity) — requires Presidential arbitration
    before College adoption
[ ] External trigger (crisis, court ruling, international agreement) — may
    accelerate or derail

Active delay factors for this dossier: [List applicable]

---

### Summary Verdict

Realistic adoption window: [YEAR–YEAR]
Application/transposition deadline: [YEAR]
Most likely cause of delay: [One sentence]
Most likely cause of failure: [One sentence — or "Not identified" if risk is low]

[model knowledge — verify] for all TFEU citations, QMV thresholds, and
institutional procedure references.

> **DRAFT** — Simulation output. Not an official Commission position.
