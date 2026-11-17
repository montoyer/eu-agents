---
name: qmv-calculator
description: >
  Calculate Qualified Majority Voting (QMV) outcomes for the Council of the EU.
  Given a dossier and a set of member-state positions (supporting, opposing, or
  abstaining), determines whether a qualified majority is available, whether a
  blocking minority has formed, which swing states are decisive, and what
  coalition-building strategy the Presidency should pursue. Also handles the
  reinforced qualified majority (Council acting without a Commission or High
  Representative proposal), votes where only some Member States take part,
  unanimity checks, and simple majority (procedural votes). Uses the official
  population figures in Annex III to the Council's Rules of Procedure.
  Use as a standalone arithmetic tool or chain it from council-eu, coreper, or
  council-presidency when precise vote arithmetic is needed.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.1.0"
  domain: eu-simulation
  triggers: >
    QMV, qualified majority voting, blocking minority, vote arithmetic, Council vote,
    member state positions, population threshold, 55% threshold, 65% population,
    reinforced qualified majority, enhanced QMV, unanimity check, simple majority
    Council, swing states, coalition building, Council adoption, vote count, QMV
    calculator, Art. 16 TEU, Art. 238 TFEU, Council decision-making, vote simulation
  role: specialist
  scope: qmv-arithmetic
  output-format: qmv-assessment
  institution: Council of the European Union
  related-skills: council-eu, coreper, council-presidency, timeline, subsidiarity-stress
---

# QMV Calculator — Council of the EU

Precision vote arithmetic for Council of the EU decisions under Qualified Majority
Voting. QMV is not a simple head count: a proposal can have a majority of member
states and still fail on population, or have the population without enough
states. In a QMV vote an abstention has the same effect as a vote against: only
votes in favour count towards the two thresholds.

Germany and France together hold 33.65 % of the Union's population in 2026, so
with any two further states holding more than 1.35 % between them they block.
Three large states can never block alone, whatever their population: a blocking
minority needs at least four members (Art. 16(4) TEU).

This skill runs the arithmetic for all 27 Member States from the official
figures, finds the minimum winning coalition and the minimum blocking minority,
and names the swing states.

---

## Voting Rules Reference

```
QUALIFIED MAJORITY (Art. 16(4) TEU; Art. 238(3)(a) TFEU when not all take part):
  State threshold:      ≥ 55 % of members      = ≥ 15 of 27 in favour
  Population threshold: ≥ 65 % of population   = ≥ 293 905 933 in favour (2026)
  BOTH thresholds must be met by the members voting IN FAVOUR.

  ABSTENTIONS: an abstaining member is not in favour. Its state does not count
    towards the 15, and its population stays in the total but not in the
    favour column, so it weighs against adoption on both thresholds exactly as
    a NO vote does.

BLOCKING MINORITY (Art. 16(4) TEU, second subparagraph):
  Members not in favour (NO + ABSTAIN) block on population when they hold more
  than 35 % (> 158 257 041 in 2026) AND number at least four. With three or
  fewer, the qualified majority is deemed attained even if the favour column
  is below 65 %.
  Thirteen members not in favour always block, on the state count alone.

REINFORCED QUALIFIED MAJORITY (Art. 238(2) TFEU):
  Applies when the Council does NOT act on a proposal from the Commission or the
  High Representative, for example an initiative of a quarter of the Member
  States in police and judicial cooperation (Art. 76(b) TFEU).
  State threshold:      ≥ 72 % of members      = ≥ 20 of 27
  Population threshold: ≥ 65 % of population

PARTIAL PARTICIPATION (Art. 238(3) TFEU):
  When the Treaties exclude some members from a vote (euro-area measures under
  Art. 136 TFEU; Denmark and Ireland under Protocols 21 and 22 in freedom,
  security and justice), recompute every threshold on the participating members
  and their population. A blocking minority then needs the minimum number of
  members representing more than 35 % of the participating population, plus one.

SIMPLE MAJORITY (Art. 238(1) TFEU):
  A majority of component members = ≥ 14 of 27 in favour. No population test.
  Used for: procedural decisions, the Council's Rules of Procedure.

UNANIMITY:
  No member votes against. Abstentions do not prevent adoption (Art. 238(4) TFEU).
  Used for: CFSP, taxation, own resources, Art. 352 TFEU, some JHA files.
  Also needed when the Council amends a Commission proposal against the
  Commission's will (Art. 293(1) TFEU), and at second reading for Parliament
  amendments on which the Commission gave a negative opinion (Art. 294(9) TFEU).
```

---

## Population data

Read `knowledge/member-states.yml` before calculating. It holds the population of
each Member State from Annex III to the Council's Rules of Procedure, the EU
total, the 65 % threshold and the 35 % blocking figure.

- **Figures in force:** Council Decision (EU, Euratom) 2025/2427, applicable from
  1 January to 31 December 2026: EU total 452 162 974; threshold 293 905 933
  [EUR-Lex — verify current version].
- **Yearly update:** the Council replaces Annex III with effect from each
  1 January, on Eurostat data held on 30 September of the year before (Art. 11(6)
  of its Rules of Procedure). For a vote dated in a later year, say that the
  figures may have changed and use them as the latest available.
- **Rounding:** compute shares from the absolute figures. The indicative
  percentages in Annex III are rounded and their sum is not exactly 100.

---

## Core Workflow

1. **Establish the voting rule** — confirm which rule applies and cite the
   legal basis:
   - QMV (Art. 16(4) TEU): the default for Council acts, including first and
     second reading under the ordinary legislative procedure
   - Reinforced QMV (Art. 238(2) TFEU): Council acting without a Commission or
     High Representative proposal
   - Partial participation (Art. 238(3) TFEU): list who is excluded and why
   - Unanimity: taxation, CFSP, own resources and the other listed cases
   - Simple majority: procedural decisions

2. **Map member-state positions** — classify each of the 27 MS as:
   - **YES**: in favour; the only position that counts towards the thresholds
   - **NO**: against
   - **ABSTAIN**: not in favour; in QMV it weighs exactly like NO
   - **UNKNOWN**: not yet determined; run scenarios

3. **Calculate state threshold** — count YES votes:
   - ≥ 15 YES: state threshold met
   - < 15 YES: not met; 13 or more members not in favour block on this alone

4. **Calculate population threshold** — sum the population of YES states:
   - ≥ 293 905 933 (2026): met
   - below: not met, unless step 5 shows fewer than four members not in favour

5. **Check blocking minority** — take every member not in favour (NO + ABSTAIN):
   - ≥ 4 such members AND their population > 158 257 041 (2026): blocking minority
   - fewer than 4: the qualified majority is deemed attained if the state
     threshold is met, whatever their population
   - Example: Germany + France + Italy hold 46.84 % but are only three; with
     every other member in favour, the act is adopted

6. **Identify swing states** — which UNKNOWN or ABSTAIN states are pivotal:
   - Which states, if moved to YES, would clear both thresholds?
   - Which states, if moved to NO or ABSTAIN, would form a blocking minority?
   - These are the Presidency's priority for bilateral contacts

7. **Coalition strategy** — based on the arithmetic, recommend:
   - Minimum winning coalition (fewest states needed to clear both thresholds)
   - Maximum pressure scenario (largest YES coalition achievable)
   - Blocking minority prevention strategy (which states must be separated)

---

## Abstention Mechanics (Often Misunderstood)

In a QMV vote, abstaining and voting against have the same arithmetic effect:
neither adds to the 15 states or to the 65 % of population. A delegation that
wants to signal unease without helping a blocking minority cannot do so by
abstaining; only a YES vote leaves the blocking side.

The difference matters under **unanimity**. There, a NO vote blocks and an
abstention does not (Art. 238(4) TFEU). A member that cannot support a unanimous
act but does not want to stop it abstains, and may add a statement to the
minutes. An adopted act binds every Member State, including those that voted
against or abstained.

Members also use statements in the minutes under QMV to record their reasons.
Those statements have no legal effect on the act.

---

## Common Blocking Minority Scenarios (2026 figures)

```
SCENARIO 1 — Large-state alignment:
  DE + FR = 33.65 % → need two more states holding > 1.35 % together
  DE + FR + BG + MT = 35.20 % → blocks
  DE + FR + IT = 46.84 % → only three members; cannot block without a fourth

SCENARIO 2 — Large states without Germany or France:
  IT + ES + PL + RO = 36.54 % → blocks

SCENARIO 3 — Central and eastern alignment:
  PL + RO + CZ + HU = 17.02 %; with SK = 18.23 %
  Far below 35 %; this group blocks only by reaching 13 members not in favour,
  or by joining a large Western state (DE + PL + RO + IT = 44.15 %)

SCENARIO 4 — Small-state majority without large-state support:
  The 23 states other than DE, FR, IT and ES hold 42.31 %. They clear the
  state threshold but fail the population threshold, and DE + FR + IT + ES
  (57.69 %) form a blocking minority of four.
```

---

## Constraints

### MUST DO
- **Apply both thresholds to the YES column** — a result that meets the state
  threshold but not the population threshold (or the reverse) fails, unless
  fewer than four members are not in favour; flag which threshold is decisive
- **Apply the four-member floor** — three members can never block on
  population, however large they are (Art. 16(4) TEU)
- **Count abstentions as not in favour** — they weigh against adoption on both
  thresholds and count towards a blocking minority
- **Use the dated official figures** — read `knowledge/member-states.yml` and
  state which Annex III applies; never estimate populations
- **Check the voting rule before calculating** — QMV, reinforced QMV, partial
  participation, unanimity and simple majority use different thresholds; the
  legal basis decides
- **Flag Ioannina requests** — under Council Decision 2009/857/EC, members that
  fall short of a blocking minority but hold at least 55 % of the population or
  of the number of members needed for one can ask the Council to keep
  negotiating [EUR-Lex — verify current version]; this is a political signal
  even though it does not stop a vote

### MUST NOT DO
- **Do not treat a QMV calculation as final** — member-state positions shift;
  label all calculations as based on stated or modelled positions at a given point
  in time; flag which positions are confirmed vs. estimated
- **Do not confuse Council of the EU QMV with European Council** — the European
  Council (heads of state or government) decides by consensus unless the
  Treaties provide otherwise (Art. 15(4) TEU); when it does vote by QMV, its
  President and the Commission President do not vote (Art. 235(1) TFEU)

---

## Reference Guide

| Topic | Reference | Load When |
|---|---|---|
| Population per Member State, EU total, 65 % threshold, euro-area membership | `knowledge/member-states.yml` | Every calculation |

---

## Output Template

QMV ASSESSMENT — [DOSSIER TITLE]
Legal basis: [TFEU Art. X]
Voting rule: [QMV / Reinforced QMV / Partial participation / Unanimity / Simple majority]
Population figures: Annex III, Council Decision [number] (applicable [year])
Date of assessment: [DD Month YYYY]

---

### Member State Position Map

| MS  | Position | Population (M) | Notes |
|-----|----------|---------------|-------|
| [MS code, 27 rows in Annex III order] | [YES/NO/ABSTAIN/UNKNOWN] | [M, one decimal] | [any specific note] |

---

### QMV Arithmetic

YES:            [N] states / 27   → [X.X %]   Threshold: ≥ 55 % (≥ 15)   → [MET / NOT MET]
YES population: [XXX.X]M / [total]M → [X.XX %] Threshold: ≥ 65 %          → [MET / NOT MET]

Not in favour (NO + ABSTAIN): [N] states, [XXX.X]M → [X.XX %]
Blocking minority (> 35 % and ≥ 4 members, or ≥ 13 members): [YES / NO]

─────────────────────────────────────────────────────────────
RESULT: [ADOPTED / ADOPTED (fewer than four members not in favour) /
         NOT ADOPTED — BLOCKING MINORITY / INSUFFICIENT STATES /
         INSUFFICIENT POPULATION]
─────────────────────────────────────────────────────────────

---

### Swing State Analysis

States whose position is UNKNOWN or ABSTAIN and whose shift to YES would be decisive:
  [MS] (+[X.X]M population): [why decisive — moves state count / population over threshold]
  [MS] (+[X.X]M population): [why decisive]

States whose move away from YES would form or complete a blocking minority:
  [MS] ([X.X]M): [current position — why pivotal for blocking minority]

---

### Coalition Strategy

Minimum winning coalition (fewest additional YES votes needed):
  Current YES + [MS list]: [N] states / [XXX.X]M — clears both thresholds

Maximum achievable YES coalition (optimistic scenario):
  [MS list] → [N] states / [XXX.X]M

Blocking minority prevention priority:
  The Presidency should focus on bringing [MS] to YES
  Reason: [population arithmetic — moving this state takes the members not in
           favour below 35 % OR below four members]

Recommended Presidency action:
  [ ] QMV available — recommend A-point or call vote
  [ ] QMV marginal — pre-cook bilaterally with [MS list] before calling vote
  [ ] Blocking minority present — do not call vote; continue compromise text discussions
  [ ] Unanimity required and not available — flag to ministers

[model knowledge — verify dossier-specific political positions]

> **DRAFT** — Simulation output. Not an official Council position.
