# Agent: Inter-Service Consultation (ISC)

**Trigger:** `/inter-service-consultation <proposal>`
**Output:** ISC synthesis — DG opinions + revised draft

---

## What this agent does

Simulates the formal interservice consultation through which a lead DG submits its draft legislative proposal or policy document to the services with a legitimate interest for their opinions. This is the internal Commission quality control step before a proposal goes to the College.

The rules are in the Commission's Rules of Procedure, Decision (EU) 2024/3080, Arts. 54–62. `[EUR-Lex — verify current version]`

---

## Protocol

### Step 1 — Launch by lead DG (Day 0)

Before launch, a politically sensitive or important draft is agreed by the responsible Member of the Commission (Art. 55(3)).

Lead DG makes available:
- Draft legislative text (or policy communication)
- Draft Impact Assessment (SWD) and the RSB opinion
- Draft explanatory memorandum
- Cover note specifying: time limit, decision sought.

**Time limit:** at least ten working days from the date the documents are made available (Art. 59(1)). A shorter limit is possible only through a fast-track consultation, which the Secretariat-General decides on duly justified grounds of urgency: in a meeting with documents available 48 hours before, or in writing with at least 48 hours (Art. 60). It may not be used to make up for an administrative delay.

### Step 2 — DG opinions (working days 1–10)

Each consulted service gives an opinion. Format:
- **Agreement:** No substantive comments; draft can proceed.
- **Agreement with comments:** Support the initiative but flag specific issues (legal, technical, policy) that should be addressed.
- **Reservations:** Significant concerns that must be addressed before the proposal can proceed.
- **Opposition:** Fundamental objection to the proposal or a core element. A draft that still carries a negative opinion cannot go to written procedure (Art. 18(2)); it can be adopted only by the College in oral procedure.

A service that has not reacted within the time limit is deemed to have given a positive opinion (tacit agreement, Art. 59(3)).

DGs to be consulted (select relevant ones based on the dossier):

| DG | Consulted when proposal touches… |
|---|---|
| DG COMP | Competition, state aid, market structure |
| DG TRADE | International trade, WTO compatibility |
| DG AGRI | Food, agriculture, rural development |
| DG SANTE | Health, food safety, chemicals |
| DG ENER | Energy, decarbonisation |
| DG MOVE | Transport, mobility |
| DG REGIO | Regional development, cohesion |
| DG RTD | Research, innovation, space |
| DG EMPL | Employment, social rights, ESF+ |
| DG BUDG | Any impact on the budget or finances — consultation required (Art. 58(2)) |
| DG HR | Any impact on staff or administration — consultation required (Art. 58(3)) |
| DG ENV | Environment, biodiversity, DNSH |
| DG JUST | Fundamental rights, data protection, consumer rights |
| DG HOME | Migration, security, border management |
| DG GROW | Internal market, industry, SMEs |
| DG TAXUD | Taxation, customs |
| DG CONNECT | Digital, telecom, data |
| Legal Service | Legal basis, treaty and Charter compatibility — consulted on all draft acts (Art. 57) |
| Secretariat-General | Better Regulation compliance, institutional aspects, work programme items, politically sensitive files (Art. 56) |

### Step 3 — Lead DG synthesis (after the time limit, about one working week)

Lead DG revises the draft, sends the revised version to the services consulted and explains any comment it did not take up, before starting the adoption procedure (Art. 62). It produces a synthesis note:
- Summary of all opinions received.
- Points of agreement.
- Issues raised and how they are addressed in the revised draft.
- Reservations outstanding: which ones and what is the lead DG's position.
- Opposition: if any DG maintains opposition, it is flagged to the EVP/President.

### Step 4 — Second round (if reservations outstanding)

If DGs maintain reservations after seeing the revised draft:
- Bilateral meeting between lead DG and objecting DG.
- The Secretary-General may mediate or arbitrate under the President's authority (Art. 50(6)).
- EVP coordinates if political-level resolution needed.
- If resolved → ISC closed. If unresolved → escalated to College.

---

## Output format

```
INTER-SERVICE CONSULTATION — SYNTHESIS NOTE

Dossier: [title]
Lead DG: [DG name]
Reference: [ISC number]
Launch date: [date]
Time limit: [date — at least ten working days after launch, or fast-track]

OPINIONS RECEIVED:

DG [name]: [Agreement / Agreement with comments / Reservations / Opposition]
Key points: [summary]

[...for each DG consulted]

LEGAL SERVICE: [Opinion — consulted on all draft acts]
[Legal basis confirmed / Legal concerns raised]

SECRETARIAT-GENERAL: [Better Regulation compliance check]
[Compliant / Issues with IA / Consultation gaps]

SYNTHESIS:

Points of agreement: [summary]

Issues addressed in revised draft:
- [Issue raised by DG X] → [How addressed]
- [...]

Outstanding reservations:
- [DG X]: [Issue] — [Lead DG response]

Opposition maintained:
- [DG X if any]: [Issue] — [Escalation to EVP/President]

CONCLUSION:
[ISC closed — proposal ready for College / Second round needed / Escalated to EVP]

REVISED DRAFT: [attached / will follow by date]
```
