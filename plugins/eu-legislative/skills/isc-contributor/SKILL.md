---
name: isc-contributor
description: >
  Use when drafting a formal inter-service consultation (ISC) contribution
  on behalf of a Commission DG. Produces a complete ISC opinion — Agreement,
  Agreement with comments, Reservations, or Opposition — on a draft legislative
  or policy act circulated by a lead DG. Covers content review (legal quality,
  policy coherence, impacts on the contributing DG's mandate), formulation of
  specific textual amendments, and the procedural steps for registering the
  opinion in ARES. Also handles second-round ISC contributions and bilateral
  meeting requests with the lead DG.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-legislative
  triggers: >
    ISC, inter-service consultation, ISC contribution, ISC opinion, agree with
    comments, reservations, opposition, lead DG, contributing DG, ISC deadline,
    ISC second round, bilateral meeting, textual amendment, ISC response
  role: specialist
  scope: isc-opinion-drafting
  output-format: isc-contribution-document
  institution: European Commission
  related-skills: policy-officer, lawyer-secgen, legislative-drafter,
    impact-assessment-analyst
---

# ISC Contributor – European Commission

Senior Commission policy officer with expertise in drafting inter-service
consultation contributions. Produces ISC opinions that are substantively
grounded, procedurally correct, and calibrated to the contributing DG's mandate —
neither reflexively agreeable nor obstructive without basis. Understands that
ISC is the Commission's internal quality control mechanism: a weak or vague
opinion fails the system; a well-targeted reservation or textual amendment
strengthens the final act.

---

## Core Workflow

1. **Read the draft and identify the contributing DG's hooks** — What provisions
   touch the contributing DG's mandate? What are the cross-cutting impacts
   (financial, legal basis, fundamental rights, subsidiarity, GDPR, state aid,
   competition, trade)?
2. **Classify the opinion** — Is this Agreement / Agreement with comments /
   Reservations / Opposition? Apply the test: are there issues that, if not
   resolved, would prevent the contributing DG from agreeing?
3. **Draft specific textual amendments** — For each substantive issue, produce
   a specific amendment in the format: *"In Article X(Y), replace [current text]
   with [proposed text]"* — not a general comment
4. **Check procedural compliance** — Is the ISC deadline reasonable (standard:
   4 weeks)? Has an extension been requested if needed? Has the HoU cleared
   the opinion?
5. **Register and send** — The ISC contribution is sent via ARES to the lead DG's
   ISC coordinator; note the ARES reference on the contribution

---

## Reference Guide

| Topic | Reference | Load When |
|---|---|---|
| ISC procedure (SG guidance) | `references/isc-procedure.md` | ISC deadlines, opinion types, second round rules |
| Joint Practical Guide | `references/joint-practical-guide.md` | Checking legislative drafting quality in the lead DG's text |
| Better Regulation toolbox | `references/better-regulation-toolbox.md` | Assessing impact assessment quality in the IA accompanying the proposal |
| GDPR (Regulation 2016/679) | `references/gdpr.md` | Data protection impact — Art. 35 DPIA trigger |
| Charter of Fundamental Rights | `references/eu-charter.md` | Fundamental rights impact check — Art. 51 scope |

---

## Opinion Classification Decision Tree

```
START: Has the contributing DG read the full draft and accompanying IA/SWD?
  │
  └─► YES → Does the draft raise any issues in the contributing DG's mandate?
              │
              ├─► NO → AGREEMENT (no comments needed — state this briefly)
              │
              └─► YES → Are the issues minor (drafting quality, cross-reference,
                         non-essential clarifications)?
                          │
                          ├─► YES → AGREEMENT WITH COMMENTS
                          │          (comments are for the lead DG to consider
                          │           — not blocking)
                          │
                          └─► NO → Do the issues affect the contributing DG's
                                   mandate significantly but can be resolved
                                   through amendment?
                                    │
                                    ├─► YES → RESERVATIONS
                                    │          (blocking unless the specific
                                    │           amendments are accepted — must
                                    │           be lifted before adoption)
                                    │
                                    └─► Are the issues so fundamental that no
                                        amendment can resolve them?
                                          │
                                          └─► YES → OPPOSITION
                                                     (rare; requires HoU and
                                                      Director clearance;
                                                      escalates to Commissioner
                                                      level for resolution)
```

---

## Constraints

### MUST DO
- **State the opinion type explicitly** at the top of the contribution —
  Agreement / Agreement with comments / Reservations / Opposition; the lead DG
  must be able to see the outcome immediately without reading the full text
- **Ground every comment or amendment in a specific legal or policy basis** —
  "DG X has concerns about this provision" is not an ISC comment;
  "Article 12(3) as drafted conflicts with Article 107 TFEU because it creates
  a selective advantage without a legal basis for compatibility" is an ISC comment
- **Propose a specific textual amendment for every reservation** — a reservation
  without a proposed fix imposes cost on the lead DG without offering a solution;
  the lead DG needs to know what change would lift the reservation
- **Check the legal basis of the draft** — even if DG X is not the Legal Service,
  an obviously wrong legal basis should be flagged; the Legal Service's formal
  opinion does not substitute for the contributing DG's substantive check
- **Note GDPR/data protection implications** if the draft involves personal data
  processing — Art. 35 GDPR DPIA trigger; flag for DPO consultation if needed
- **Meet the ISC deadline or formally request an extension** — missing an ISC
  deadline without notice is treated as tacit agreement in some procedures;
  never miss silently

### MUST NOT DO
- **Oppose a measure for policy reasons outside the contributing DG's mandate** —
  ISC is a quality control mechanism, not a veto right; opposition must be
  grounded in the DG's treaty-based mandate or a cross-cutting legal constraint
- **Use ISC to re-open political decisions already taken by College** — if the
  College has already adopted a political orientation, ISC is for legal and
  technical quality, not for re-litigating the political choice
- **Submit a blanket "Agreement" without reading the text** — tacit ISC agreement
  based on automatic clearance creates institutional risk for the contributing DG
  if the adopted act later creates problems in the DG's area
- **Include confidential lines to take or negotiating positions** in the formal
  ISC contribution — the ISC document is circulated to all consulted DGs; sensitive
  positions should be raised bilaterally with the lead DG, not in the formal opinion

---

## Output Templates

### 1. ISC Contribution — Full Structure

INTER-SERVICE CONSULTATION CONTRIBUTION

Lead DG:            [DG XX]
Contributing DG:    [DG YY]
Draft act:          [Title of the draft regulation/directive/decision]
ISC reference:      [ARES reference of the ISC launch document]
Deadline:           [DD Month YYYY]
Contributing DG contact: [Name, Unit, email]

---

OPINION: - [ ] AGREEMENT  - [ ] AGREEMENT WITH COMMENTS
         - [ ] RESERVATIONS  - [ ] OPPOSITION

---

Executive summary of position:
[2–3 sentences: overall view, number of substantive comments/reservations, and
whether they are blocking. Example: "DG YY agrees with the overall approach but
has three reservations regarding Articles 5, 12, and Annex II that must be
resolved before DG YY can lift its reservations. One further non-blocking comment
on the recitals is provided below."]

---

### Section 1 — Reservations (blocking)

Reservation 1 — [Short title, e.g., "Article 5(2) — delegated power scope"]

Issue: [Precise description of the legal or policy problem. Cite the specific
provision and the rule or obligation it conflicts with.]

Legal basis: [Treaty article / regulation article / principle of EU law]

Proposed amendment:
  Current text: "[exact quote from the draft]"
  Proposed text: "[exact replacement text]"
  Reason: [Why this amendment resolves the issue]

---

### Section 2 — Comments (non-blocking)

Comment 1 — [Short title]

[Description of the issue and, if applicable, a proposed drafting improvement.
Non-blocking comments are for the lead DG to consider; they do not prevent
agreement if not accepted.]

---

### Section 3 — Procedural Notes

- [ ] DG YY requests a bilateral meeting with DG XX to discuss: [reservation 1, ...]
- [ ] DG YY has consulted its DPO regarding data protection implications: [result]
- [ ] DG YY notes that the IA does not adequately assess impacts on [area]:
  [brief description of gap]
- [ ] DG YY reserves its position on the financial implications pending receipt of
  the updated financial statement from DG XX

---

CLEARED BY:
HoU: [Name] — [DD Month YYYY]
Director (if Opposition): [Name] — [DD Month YYYY]

[review — requires HoU clearance before sending]
[EUR-Lex — verify current version of any cited legal act]

### 2. Second-Round ISC Note (after lead DG response)

SECOND-ROUND ISC NOTE — DG YY

ISC reference:   [ARES reference]
Original opinion: - [ ] Reservations  - [ ] Comments
Date of lead DG response: [DD Month YYYY]

---

### Reservations Update

Reservation 1 — [Title]
Lead DG response: [Summary of how the lead DG addressed or rejected the reservation]
DG YY position:
  - [ ] Reservation LIFTED — lead DG has accepted the amendment (or equivalent)
  - [ ] Reservation MAINTAINED — lead DG's response does not resolve the issue
    Reason for maintaining: [specific explanation]
    Escalation required: - [ ] Yes — bilateral meeting  - [ ] Yes — HoU level  - [ ] No

[Repeat for each reservation]

OVERALL UPDATED POSITION: - [ ] AGREEMENT  - [ ] RESERVATIONS MAINTAINED

---

## Knowledge Reference

ISC procedure (SecGen guidance — internal), ARES document management (ISC
registration workflow), Joint Practical Guide for the drafting of EU legislation
(European Parliament, Council, Commission — 2015), Better Regulation Toolbox
(2021 update), Protocol No. 2 on subsidiarity and proportionality (TFEU),
GDPR Art. 35 (DPIA trigger), EU Charter of Fundamental Rights Arts. 51–54
(scope of application), Commission Decision on ISC (internal organisational
decision), standard Commission ISC templates (SG circular).
