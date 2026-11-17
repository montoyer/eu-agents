<!-- SYNCED COPY — do not edit. Canonical: knowledge/workflows/legislative-cycle.md — edit there, then run scripts/sync-shared-references.sh -->

# Workflow: Legislative Cycle (Ordinary Legislative Procedure)

**Trigger:** `/legislative-cycle <brief>`
**Duration:** Simulates the full OLP from Commission initiative to adoption.
**Output:** Complete legislative file — proposal, EP position, Council position, compromise text.

---

## What this workflow does

Runs the full Ordinary Legislative Procedure (OLP) as defined in TFEU Art. 294. The Commission proposes; the European Parliament and Council co-decide; the workflow models all phases including trilogue.

---

## Phase 1 — Commission initiative

**Actors:** Lead Commissioner, lead DG, all DGs (ISC), Legal Service, College
**Duration:** ~12-18 months (pre-proposal phase)

Steps:
1. `/impact-assessment` — full SWD produced by lead DG
2. `/consultation` — 12-week OPC
3. `/treaty-check` — Legal Service opinion on legal basis
4. `/inter-service-consultation` — all DGs comment on draft
5. Lead Commissioner endorses and presents to College
6. `/college-deliberation` — College votes on adoption
7. Commission publishes proposal (COM document)

**Output:** COM([year]) [number] final — proposal transmitted to EP and Council.

---

## Phase 2 — First reading (European Parliament)

**Actors:** European Parliament (responsible committee + plenary), Commission
**Duration:** 12-18 months typically

Steps:
1. EP President refers proposal to responsible committee.
2. Responsible committee appoints rapporteur.
3. Rapporteur drafts report (amendments to Commission proposal).
4. Committee vote on report.
5. Plenary vote on EP first reading position.

**Invoke:** `/european-parliament` — model the EP position, key amendments, and political group dynamics.

**Decision rule:** Simple majority of votes cast (Art. 294(2) TFEU).
**Output:** EP first reading position (legislative resolution).

---

## Phase 3 — Council first reading

**Actors:** Council of the EU (relevant configuration + COREPER), Commission
**Duration:** 6-24 months (varies widely by dossier sensitivity)

Steps:
1. Working party examination (technical level).
2. COREPER examination (ambassadorial level).
3. Council adopts its position.

**Invoke:** `/council-eu` — model Council position, member-state dynamics, blocking minorities.

**Decision rule:** QMV (unless special procedure — unanimity for specific legal bases).

If Council adopts EP position unchanged → Act adopted (Art. 294(3)).
If not → Council first reading position transmitted to EP.

**Output:** Council first reading position.

---

## Phase 4 — Second reading (parallel EP and Council)

**Duration:** 3 months (EP) + 3 months (Council); extensions possible.

**EP second reading:**
- EP can adopt, amend (by absolute majority of members), or reject Council position.
- If EP amends → Council second reading.
- If EP rejects → Act not adopted (failure).

**Council second reading:**
- If Council approves EP second reading amendments (by QMV or unanimity depending on whether Commission agrees) → Act adopted.
- If Council does not approve → Conciliation Committee convened.

---

## Phase 5 — Trilogue (informal inter-institutional negotiation)

**Actors:** EP (rapporteur + shadow rapporteurs), Council (Presidency + member states), Commission
**Duration:** 1-6 months (can be faster or longer)

**Invoke:** `/trilogue`

Steps:
1. EP and Council each adopt their mandate (EP: committee vote; Council: COREPER/Council).
2. Trilogue rounds: typically 3-5 meetings.
3. Commission acts as honest broker, proposes compromises.
4. Political agreement reached → compromise text.
5. EP committee and plenary confirm (simple majority).
6. Council confirms (QMV or unanimity).

**If no agreement in trilogue → Conciliation Committee (formal Art. 294(11) procedure).**

**Output:** Agreed compromise text.

---

## Phase 6 — Formal adoption and publication

1. Agreed text goes through legal-linguistic revision (lawyer-linguists in all 24 EU languages).
2. EP plenary formally adopts (simple majority).
3. Council formally adopts (QMV).
4. Act signed by Presidents of EP and Council.
5. Published in Official Journal of the EU.
6. Entry into force: 20th day after OJ publication (or date specified in the act).

**Output:** Final legislative act published in OJ — Regulation/Directive reference number.

---

## Timeline summary

| Phase | Typical duration |
|---|---|
| Commission pre-proposal | 12-18 months |
| EP first reading | 12-18 months |
| Council first reading | 6-24 months |
| Trilogue | 3-12 months |
| Legal-linguistic revision + adoption | 3-6 months |
| **Total** | **~3-5 years** |

Fast-track is possible (3-6 months total in trilogue) when political consensus exists from the start.
