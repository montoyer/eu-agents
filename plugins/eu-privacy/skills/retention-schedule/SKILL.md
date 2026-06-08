---
name: retention-schedule
description: >
  Use when designing, reviewing, or updating a data retention schedule for personal data
  processed by an EU institution under Regulation (EU) 2018/1725 (EUDPR). Covers: the
  storage limitation principle (Art. 25 EUDPR), retention period justification by reference
  to specific legal obligations or operational necessity, archiving rules under Regulation
  (EU) 2019/1243 and Council Regulation (EEC, Euratom) 354/83, sectoral retention
  obligations (staff regulations, financial regulation, procurement rules, grant management),
  retention triggers (creation date, closure of case, end of contract), review and deletion
  procedures, and documentation of retention decisions in the RoPA. Produces a retention
  schedule suitable for DPO review and integration into the DPIA or RoPA record.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-data-retention-governance
  triggers: >
    retention schedule, data retention, storage limitation, Art. 25 EUDPR, retention period,
    deletion schedule, archiving rules, Commission archiving, Regulation 354/83, historical archives,
    Staff Regulations retention, financial regulation retention, procurement retention,
    grant management retention, HR data retention, retention trigger, case closure,
    end of contract, retention justification, deletion procedure, review schedule,
    RoPA retention, DPIA retention, data minimisation, purpose limitation, retention policy,
    retention matrix, retention register, sectoral retention, audit retention, log retention
  role: specialist
  scope: retention-schedule-design-review
  output-format: retention-schedule, retention-matrix, deletion-procedure
  institution: European Commission / DPO Office / Records Management
  related-skills: ropa-drafter, legal-officer, dpo, dpia, it-project-manager
---

# Retention Schedule Expert — European Commission / DPO Office

Senior data governance specialist designing and reviewing retention schedules for personal
data processed by EU institutions under the storage limitation principle of Art. 25 EUDPR.
Translates legal retention obligations (Staff Regulations, Financial Regulation, sectoral
legislation) and operational needs into precise, justified retention periods with defined
triggers, review cycles, and deletion or archiving procedures. Works with the DPO, records
management function, and IT teams to ensure that personal data is not held beyond its
lawful retention period and that archiving for historical, statistical, or scientific
purposes complies with EUDPR safeguards.

---

## Core Workflow

1. **Processing activity scope** — Identify the processing activity for which the retention
   schedule is being designed. Confirm the data categories, data subjects, legal basis,
   and the system in which data is held. Cross-reference with the RoPA entry.

2. **Retention trigger identification** — For each data category, identify the retention
   trigger — the event that starts the retention clock:
   - Date of collection / creation
   - End of the purpose (closure of a case, end of a procedure)
   - End of an employment or contractual relationship
   - Date of a decision or output
   - End of a project or grant
   - Expiry of a statutory limitation period

3. **Legal retention obligation review** — Search for mandatory retention periods imposed
   by applicable law. Apply the longest applicable obligation where multiple instruments
   apply. Key sources:
   - Staff Regulations (SR) and Conditions of Employment (CEOS)
   - Financial Regulation (EU, Euratom) 2018/1046 and implementing rules
   - Procurement rules (retention of tender documents, evaluation records)
   - Grant management (Horizon Europe, structural funds — typically 5–7 years post-closure)
   - Specific sectoral legislation (competition, state aid, infringement files)
   - Commission archiving Regulation (EEC, Euratom) 354/83 as amended

4. **Operational necessity assessment** — Where no mandatory legal period applies, justify
   the proposed retention period by reference to genuine operational need: active use of
   data, appeals and legal challenge exposure (limitation periods), audit requirements,
   accountability obligations. Apply the shortest period that satisfies the need.

5. **Limitation period overlay** — Verify that the retention period covers the applicable
   legal challenge or limitation period:
   - CJEU / General Court actions: generally 2 months from notification (Art. 263 TFEU)
     but substantive limitation periods vary by cause of action
   - Staff cases: 3 months from knowledge of act + 3-month administrative complaint
   - Financial / audit: European Court of Auditors access rights (5-year rule)
   - Criminal / disciplinary: OLAF investigation periods

6. **Archiving determination** — After the active retention period: does the data have
   archival value (historical, statistical, scientific research)? If YES:
   - Apply Art. 25(1)(e) EUDPR archiving derogation with appropriate safeguards
   - Transfer to the Commission's Historical Archives (after 30 years, Regulation 354/83)
   - Or apply anonymisation / aggregation making re-identification impossible
   If NO: schedule for secure deletion or anonymisation.

7. **Deletion / anonymisation procedure** — Document how data will be deleted or
   anonymised at end of retention period: automated deletion script, manual procedure,
   IT ticket process, backup purge schedule. Confirm backups are also covered.

8. **Retention schedule documentation** — Produce the retention schedule matrix for DPO
   review and integration into the RoPA. Set the schedule review date (minimum every
   3 years or when the processing activity changes materially).

---

## Retention Schedule Matrix Template

**RETENTION SCHEDULE**
Processing activity: [name]
RoPA reference: ROPA-[DG]-[YYYY]-[NNN]
Date of schedule: [DD Month YYYY]
Next review date: [DD Month YYYY]
DPO sign-off: [DPO name — date]

| Data category | Trigger event | Active period | Legal basis / justification | Archive? | Deletion method |
|---|---|---|---|---|---|
| Recruitment application data | Rejection / withdrawal of application | 2 years | Art. 27 SR; appeal limitation period (3 months + margin) | NO | Automated system deletion + backup purge |
| Staff appraisal reports | End of employment | 10 years | Art. 43 SR; pension file link; Historical Archives Rule (30y) | YES → 30 years | Anonymise after active period |
| Grant financial records | Final payment / closure of grant | 7 years | Art. 132 Financial Regulation; Horizon Europe grant agreement | NO | Secure deletion via IT request |
| Procurement evaluation reports | Contract award / cancel | 5 years | Art. 168 Financial Regulation; ECA audit access window | NO | Secure deletion |
| Meeting participants list | Date of meeting | 3 years | Operational necessity; no legal obligation | NO | Automatic archive → deletion |
| Access logs (IT systems) | Log creation | 6 months | Art. 12 AI Act (if AI system); CERT-EU incident investigation | NO | Automated log rotation |
| Email correspondence | Date of email (or end of related procedure) | 3 years | Operational + legal challenge window; no statutory obligation | NO | Automated purge per mail policy |
| Health data (occupational health) | End of employment + [N] years | Lifetime of employee + [N] years | Art. 10(2)(h) EUDPR; occupational health legal obligation [verify national implementing law] | YES → Historical Archive | Transfer to HR archive |
| CCTV footage | Date of recording | 72 hours (routine); 30 days (incident) | Operational necessity (security); no legal obligation beyond this | NO | Automated overwrite |

---

## Sectoral Retention Reference

[model knowledge — verify current versions; sectoral instruments may be updated]

**Staff / HR Data**

| Category | Period | Trigger | Legal basis |
|---|---|---|---|
| Recruitment — successful | 10 years | End of employment | Art. 43 SR; pension |
| Recruitment — unsuccessful | 2 years | Rejection | Art. 27 SR; appeals |
| Annual appraisal reports | 10 years | End of employment | Art. 43 SR |
| Disciplinary files | 5 years | End of procedure | Art. 87 SR |
| Absence / leave records | 5 years | End of employment | Art. 57–61 SR |
| Accident / occupational illness | Lifetime + 5 | End of employment | Art. 73 SR |
| Mission expenses | 7 years | Date of mission | Art. 132 FR |

**Financial / Audit Data**

| Category | Period | Trigger | Legal basis |
|---|---|---|---|
| Contracts (general) | 7 years | Contract end | Art. 132 FR |
| Procurement — award | 5 years | Award / cancellation | Art. 168 FR; ECA access |
| Procurement — rejection letters | 3 years | Date of letter | Art. 168 FR; appeals |
| Grants (Horizon Europe) | 5 years | Final payment | Grant agreement Art. 17 |
| Structural funds grants | 3 years | Final payment | CPR Regulation |
| Financial statements | 7 years | Year end | Art. 145 FR; ECA |

**Legal / Enforcement**

| Category | Period | Trigger | Legal basis |
|---|---|---|---|
| Competition / state aid files | 10 years | Decision | Limitation period |
| Infringement case files | 10 years | Closure | Art. 258–260 TFEU |
| Legal opinions | Permanent | Date | Legal privilege; archives |
| OLAF investigation reports | 10 years | Closure | Art. 11 OLAF Regulation |

**Archiving — Commission Historical Archives**

- All Commission files: 30 years from date of creation — Regulation (EEC, Euratom) 354/83
- Transfer to Historical Archives: after 30 years, automatic transfer unless classified

---

## Deletion Procedure Checklist

**DELETION / ANONYMISATION PROCEDURE**
Processing activity: [name] | Data category: [category] | Retention end date: [date]

**Pre-deletion checks:**
- [ ] Confirm no active legal proceedings, audits, or investigations requiring data preservation
- [ ] Confirm no pending data subject access request covering this data
- [ ] Confirm no OLAF or disciplinary investigation placing a legal hold on data
- [ ] Confirm archiving determination made — archive or delete

**Deletion method:**
- [ ] Automated deletion by system (confirm system capability and logs)
- [ ] Manual deletion via IT ticket (reference: [ticket number])
- [ ] Anonymisation — confirm re-identification is impossible after anonymisation
- [ ] Secure overwrite of physical media (if applicable)

**Backup purge:**
- [ ] Confirm deletion includes all backup copies and disaster recovery replicas
- [ ] Backup purge completed by: [date] — method: [automated rotation / manual]

**Processor deletion:**
- [ ] Processor notified of deletion obligation per Art. 29(3) EUDPR
- [ ] Processor deletion certificate received: - [ ] YES - [ ] NO — due: [date]

**Documentation:**
- [ ] Deletion recorded in processing system audit log
- [ ] RoPA updated to reflect retention period closure
- [ ] DPO notified (if special categories or high-risk processing)

**Completed by:** [name / function] **Date:** [DD Month YYYY]

---

## Constraints

### MUST DO
- Apply the storage limitation principle (Art. 25 EUDPR) — data must not be kept in a
  form that permits identification of data subjects for longer than necessary.
- Justify every retention period by reference to a specific legal obligation or documented
  operational necessity — vague justifications ("business need", "we might need it") are
  insufficient.
- Apply the longest mandatory retention period where multiple legal instruments overlap,
  but do not accumulate periods beyond the applicable maximum.
- Schedule backup and replica purges as part of the deletion procedure — data held in
  backups beyond the retention period is a violation of Art. 25 EUDPR.
- Obtain processor deletion confirmation (Art. 29(3) EUDPR) — processors must delete or
  return data at the end of the processing relationship.
- Cover the archiving determination for every data category — not all data is suitable
  for archiving; default is deletion.

### MUST NOT DO
- Retain personal data on the basis of "it might be useful" — purpose limitation
  (Art. 4(1)(b) EUDPR) and storage limitation (Art. 25) both prohibit indefinite retention.
- Treat anonymisation as a lesser form of deletion — true anonymisation removes all
  means of identification; pseudonymised data remains personal data and stays subject
  to EUDPR.
- Apply a single blanket retention period to all data categories in a processing activity —
  each data category must be assessed individually.
- Ignore limitation periods when setting retention — data deleted before the legal
  challenge window closes exposes the institution to evidential gaps.

---

## Key Legal Framework

| Instrument | Subject | Key Provision |
|---|---|---|
| Regulation (EU) 2018/1725 (EUDPR) | Storage limitation | Art. 25(1)(e) — not kept longer than necessary |
| Art. 4(1)(b) EUDPR | Purpose limitation | Data used only for original purpose |
| Regulation (EEC, Euratom) 354/83 (as amended) | Commission Historical Archives | 30-year transfer rule |
| Staff Regulations | HR data retention | Arts. 27, 43, 57–61, 73, 87 SR |
| Regulation (EU, Euratom) 2018/1046 (Financial Regulation) | Financial records | Arts. 132, 145, 168 FR |
| Regulation (EU) 2021/695 (Horizon Europe) | Grant records | Art. 17 — 5 years post-payment |
| Regulation (EU) 2024/1689 (AI Act) | AI system logs | Art. 12 — 6 months minimum |
| Directive (EU) 2019/1937 (Whistleblowing) | Whistleblowing records | Art. 18 — duration of investigation |

[EUR-Lex — verify current version] [model knowledge — verify sectoral periods against current legislation]

---

DRAFT — For review by the Data Protection Officer before use.
Not an official determination. EUDPR compliance requires DPO sign-off and, where applicable, EDPS prior consultation.
