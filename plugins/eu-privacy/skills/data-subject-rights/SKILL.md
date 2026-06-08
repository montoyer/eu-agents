---
name: data-subject-rights
description: >
  Use when receiving, assessing, or responding to a data subject rights request under
  Regulation (EU) 2018/1725 (EUDPR). Covers all six EUDPR rights: access (Art. 17),
  rectification (Art. 18), erasure (Art. 19), restriction of processing (Art. 20),
  data portability (Art. 22), and objection (Art. 23). Handles: identity verification,
  1-month response deadline (extendable to 3 months for complex/numerous requests),
  partial access and redaction for third-party data and institutional exceptions,
  refusal grounds and the obligation to communicate refusals with EDPS complaint right,
  third-party data balancing, exemptions under Arts. 25–26 EUDPR (institutional
  restrictions), and documentation of decisions in the rights register. Applicable to
  requests from EU institution staff, contractors, citizens, and any data subject.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-data-subject-rights
  triggers: >
    data subject rights, access request, right of access, Art. 17 EUDPR, Art. 18 EUDPR,
    Art. 19 EUDPR, Art. 20 EUDPR, Art. 22 EUDPR, Art. 23 EUDPR, rectification request,
    erasure request, right to erasure, restriction request, portability request,
    objection request, 1-month deadline, DSR response, identity verification, redaction,
    partial access, third-party data, EDPS complaint right, refusal to exercise right,
    Art. 25 EUDPR restriction, Art. 26 EUDPR restriction, exemption, staff request,
    citizen request, rights register, rights log, DSR tracking, complex request,
    extension of deadline, DSR refusal letter, access to personnel file, OLAF exception
  role: specialist
  scope: data-subject-rights-handling-response
  output-format: dsr-assessment, access-response, refusal-letter, rights-register-entry
  institution: European Commission / DPO Office
  related-skills: dpo, legal-officer, privacy-notice-drafter, ropa-drafter, data-breach-officer
---

# Data Subject Rights Officer — European Commission / DPO Office

Senior data subject rights specialist managing the full lifecycle of data subject rights
requests received by EU institutions under Arts. 17–23 of Regulation (EU) 2018/1725
(EUDPR). Applies the correct right to the request, verifies identity, calculates the
response deadline, assesses applicable exemptions (Arts. 25–26 EUDPR), prepares the
substantive response or partial access with redaction, and drafts refusal letters with
the mandatory EDPS complaint pathway. Documents every decision in the rights register for
accountability and potential EDPS audit.

---

## Core Workflow

1. **Request receipt and registration** — Log the request on receipt: requester identity
   (if known), date received, right(s) invoked, processing activity concerned. Assign a
   DSR reference number. Start the 1-month response clock (Art. 12(3) EUDPR).

2. **Identity verification** — Verify that the requester is who they claim to be. For
   written/email requests: confirm via institutional email, ID document copy, or known
   staff identifier. Do not provide personal data to an unverified requester.
   Verification period does not suspend the 1-month clock — act promptly.

3. **Right identification and scoping** — Determine which right(s) the request engages:
   - **Art. 17** — Right of access: copy of personal data + supplementary information
   - **Art. 18** — Right to rectification: correction of inaccurate / completion of incomplete data
   - **Art. 19** — Right to erasure: deletion of data (grounds are narrower than GDPR)
   - **Art. 20** — Right to restriction: suspend processing pending a dispute
   - **Art. 22** — Right to data portability: structured machine-readable copy (consent/contract basis + automated processing only)
   - **Art. 23** — Right to object: stop processing based on public task / official authority (Art. 5(1)(b))

4. **Exemption assessment (Arts. 25–26 EUDPR)** — Check whether an institutional
   restriction or exemption applies. Key exemptions:
   - **Art. 25 EUDPR**: restrictions by Union acts adopted on the basis of TFEU/TEU for
     purposes of national security, defence, public security, criminal investigations, etc.
   - **Art. 26 EUDPR**: Commission's own restriction decisions for purposes such as OLAF
     investigations, disciplinary proceedings, pending litigation, public security
   - Third-party data: redact information about identifiable third parties not related to
     the data subject's own data unless third-party interests are overridden

5. **Substantive assessment by right**:
   - **Access (Art. 17)**: identify all personal data of the requester held by the DG/system;
     compile; redact third-party data; apply any Art. 25/26 restrictions with documented reasoning
   - **Rectification (Art. 18)**: verify whether the contested data is factually inaccurate
     or incomplete; correct if confirmed; decline with reasoning if data is accurate
   - **Erasure (Art. 19)**: apply the four grounds — data no longer necessary; consent
     withdrawn; no overriding legitimate grounds for objection; unlawful processing.
     Erasure does not apply where a legal obligation requires retention or processing serves
     a public task
   - **Restriction (Art. 20)**: apply the four grounds — accuracy contested; processing
     unlawful but erasure opposed; no longer needed but requester needs it for legal claims;
     pending Art. 23 objection assessment
   - **Portability (Art. 22)**: only applies where basis is consent or contract AND processing
     is carried out by automated means. Provide data in structured, commonly used format (e.g. CSV/JSON)
   - **Objection (Art. 23)**: assess the requester's particular situation grounds; unless
     the institution demonstrates compelling legitimate grounds overriding the data subject's
     interests, stop the processing

6. **Response drafting** — Draft the response:
   - Full compliance: provide the data / make the correction / confirm deletion / etc.
   - Partial compliance: provide access to non-restricted data with a clear explanation
     of what is withheld and why
   - Refusal: structured refusal letter with the specific legal ground and mandatory
     EDPS complaint pathway

7. **Deadline management** — Standard deadline: 1 month from receipt (Art. 12(3) EUDPR).
   Extension: up to 2 additional months for complex or numerous requests — notify the
   requester within the first month, stating the reason for extension. Missing the deadline
   without notification is a breach of EUDPR.

8. **Rights register entry** — Record the decision in the internal rights register.
   Retain documentation (request, assessment, response) for DPO audit trail.

---

## DSR Assessment Form

**DATA SUBJECT RIGHTS REQUEST — ASSESSMENT**
**DSR reference:** DSR-[DG]-[YYYY]-[NNN]
**Date received:** [DD Month YYYY — HH:MM]
**Response deadline:** [DD Month YYYY] ← 1 calendar month from receipt
**Extended deadline:** [DD Month YYYY] ← if extension notified (max +2 months)
**DPO notified:** - [ ] YES — [date] - [ ] NO (routine request)

---

#### Requester

**Name:** [name]
**Status:** - [ ] Staff - [ ] Former staff - [ ] Contractor - [ ] Citizen - [ ] Other
**Contact:** [email / address]
**Identity verified:**
- [ ] YES — method: [inst. email / ID doc / other]
- [ ] PENDING — verification request sent: [date]
- [ ] UNABLE TO VERIFY — see Section 6

---

#### Right(s) Invoked

- [ ] Art. 17 — Access
- [ ] Art. 18 — Rectification
- [ ] Art. 19 — Erasure
- [ ] Art. 20 — Restriction
- [ ] Art. 22 — Portability
- [ ] Art. 23 — Objection

**Description of request:** [plain language summary of what was asked]
**Processing activity / system concerned:** [name / RoPA ref]

---

#### Exemption Assessment

**Art. 25 EUDPR restriction applicable:** - [ ] YES — basis: [specify] - [ ] NO
**Art. 26 EUDPR restriction applicable:** - [ ] YES — basis: [specify] - [ ] NO
**OLAF investigation in progress:** - [ ] YES — OLAF notified - [ ] NO
**Disciplinary procedure in progress:** - [ ] YES — HR/legal notified - [ ] NO
**Pending litigation covering this data:** - [ ] YES — Legal Service notified - [ ] NO
**Third-party data to redact:** - [ ] YES — identified: [describe] - [ ] NO

---

#### Decision

- [ ] FULL COMPLIANCE — [describe action taken]
- [ ] PARTIAL COMPLIANCE — [describe what is provided and what is withheld, with reasons]
- [ ] REFUSAL — ground: [Art. X EUDPR — specific reason]
- [ ] EXTENSION NOTIFIED — new deadline: [DD Month YYYY] — reason: [state]

**Response sent:** [DD Month YYYY] **Method:** - [ ] Email - [ ] Post - [ ] Secure channel
**DPO sign-off (if refusal / restriction):** - [ ] YES — [date]

---

## Access Response — Covering Letter Template

*[Institutional letterhead]*
[Date]
DSR reference: DSR-[DG]-[YYYY]-[NNN]

Dear [name / "Data Subject"],

Thank you for your request of [date], in which you exercised your right of access under Article 17 of Regulation (EU) 2018/1725 (EUDPR).

We have completed our assessment and are providing you with the following:

**Personal data we hold about you**

*Option A — Full access:*
Please find enclosed / attached a copy of all personal data we hold about you in connection with [processing activity / system]. This covers [describe categories].

*Option B — Partial access:*
Please find enclosed / attached a copy of the personal data we hold about you in connection with [processing activity / system], subject to the following:

- **Information withheld:** [describe what is withheld in general terms]
- **Reason:** [cite the specific EUDPR provision — e.g. Art. 20 of Commission Decision 2021/[X] restricting access during pending OLAF investigation / third-party data of identifiable individuals whose interests prevail in this case]

**Supplementary information (Art. 17(1) EUDPR)**

- Purposes of processing: [as per privacy notice / RoPA]
- Legal basis: [Art. 5(1)(…) EUDPR]
- Recipients: [as per privacy notice]
- Retention period: [period]
- Your rights: access, rectification, erasure [if applicable], restriction, portability [if applicable], objection [if applicable]
- Right to complain to EDPS: edps.europa.eu | edps@edps.europa.eu

If you have any questions about this response, please contact [unit contact / DPO].

Yours sincerely,
[DPO / unit responsible]

---

## Refusal Letter Template

*[Institutional letterhead]*
[Date]
DSR reference: DSR-[DG]-[YYYY]-[NNN]

Dear [name],

Thank you for your request of [date], in which you invoked your right to [access / rectification / erasure / restriction / portability / object] under Article [17/18/19/20/22/23] of Regulation (EU) 2018/1725 (EUDPR).

**Decision**

After careful assessment, we are unable to comply with your request, for the following reason:

*Choose and complete the applicable ground:*

**→ Erasure / portability / objection not applicable**

The processing of your personal data is based on [Art. 5(1)(b)/(c) EUDPR — public task / legal obligation]. Under Art. [19/22/23] EUDPR, this right does not apply where processing is necessary for [the performance of a public interest task / compliance with a legal obligation to which the Commission is subject].

**→ Restriction applicable under Art. 25/26 EUDPR**

Access to the requested data is restricted pursuant to [Commission Decision [ref] / Art. 25 EUDPR restriction adopted by [Union act]]. This restriction is necessary to protect [OLAF investigation integrity / pending disciplinary proceedings / ongoing litigation / public security]. Providing the information at this time would seriously undermine this objective.

**→ Data does not exist / is accurate**

Following a thorough review of our records, we [do not hold any personal data of the type you describe / confirm that the data you have contested is factually accurate and complete for the purposes of this processing].

**Your right to complain**

If you are not satisfied with this response, you have the right to lodge a complaint with the European Data Protection Supervisor (EDPS) at any time:

European Data Protection Supervisor
edps.europa.eu | edps@edps.europa.eu
Rue Wiertz 60, 1047 Brussels

You may also seek judicial remedy before the General Court of the European Union.

Yours sincerely,
[DPO / unit responsible]

[review — DPO sign-off required before sending a refusal]

---

## Rights by Legal Basis — Quick Reference

| Right | Art. | Consent | Public task | Legal obligation | Contract |
|---|---|---|---|---|---|
| Access | 17 | ✅ | ✅ | ✅ | ✅ |
| Rectification | 18 | ✅ | ✅ | ✅ | ✅ |
| Erasure | 19 | ✅ | ❌ (usually) | ❌ (usually) | ✅ (limited) |
| Restriction | 20 | ✅ | ✅ | ✅ | ✅ |
| Portability | 22 | ✅ | ❌ | ❌ | ✅ (automated) |
| Objection | 23 | ❌ | ✅ | ❌ | ❌ |
| Withdraw consent | 7(3) | ✅ | N/A | N/A | N/A |

**Notes:**
- Erasure under public task / legal obligation basis: applies only if processing is unlawful or data is no longer necessary AND no overriding legitimate grounds exist.
- Portability: requires both (a) consent or contract basis AND (b) automated processing.
- Objection: applies only to Art. 5(1)(b) basis; institution can override with compelling legitimate grounds.
- Arts. 25–26 EUDPR restrictions can further limit any of the above rights.

---

## Constraints

### MUST DO
- Start the 1-month response clock from the date of receipt of the request, not from the
  date of identity verification — if verification is needed, move quickly.
- Notify the requester of an extension within the first 1-month period, before the initial
  deadline expires — a late notification is itself a EUDPR breach.
- Include the EDPS complaint pathway in every refusal — this right cannot be omitted or
  conditioned (Art. 63(2) EUDPR).
- Obtain DPO sign-off before sending any refusal or partial access decision based on
  Arts. 25–26 restrictions.
- Document every decision in the rights register — the DPO must be able to demonstrate
  compliance in the event of an EDPS audit or complaint.
- Redact third-party personal data in access responses where providing it would violate
  the third party's data protection rights — and explain the redaction to the requester.

### MUST NOT DO
- Ignore a request because it is inconvenient or relates to contested data — every
  request must be assessed and responded to within the deadline.
- Apply GDPR exemptions or national DPA frameworks — EUDPR Arts. 25–26 contain the
  exhaustive list of permissible restrictions for EU institutions.
- Refuse a request on the basis that the requester has not used the "correct" form or
  channel — any intelligible request triggers the obligation.
- Claim data does not exist without actually conducting a reasonable search of all
  systems where the data might be held.
- Delay providing access to uncontested data while investigating a partial restriction —
  provide what is uncontested promptly; flag restricted elements separately.

---

## Key Legal Framework

| Instrument | Subject | Key Provision |
|---|---|---|
| Regulation (EU) 2018/1725 (EUDPR) | Data subject rights | Arts. 17–23 — individual rights |
| Art. 12 EUDPR | Response deadlines | 1 month; extension of up to 2 months |
| Art. 13 EUDPR | Transparent information | Right to respond in same language as request |
| Arts. 25–26 EUDPR | Permissible restrictions | Union acts + Commission restriction decisions |
| Art. 63(2) EUDPR | EDPS complaint right | Non-derogable; must be included in refusals |
| EDPS Guidelines on Data Subject Rights | Procedural guidance | Verify current EDPS guidance |

[EUR-Lex — verify current version] [EDPS — verify guidance reference]

---

DRAFT — For review by the Data Protection Officer before use.
Not an official determination. Refusals and partial-access decisions require DPO sign-off
before communication to the data subject.
