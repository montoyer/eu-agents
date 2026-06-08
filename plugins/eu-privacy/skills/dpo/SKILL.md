---
name: dpo
description: >
  Use when acting as or consulting the Data Protection Officer (DPO) for an EU institution,
  body, office, or agency under Regulation (EU) 2018/1725 (EUDPR). Covers: Art. 39 DPIA
  threshold screening (mandatory vs. discretionary), DPIA process leadership and sign-off,
  maintenance of the Record of Processing Activities (ROPA) under Art. 31, DPO advisory
  opinions, Art. 40 prior-consultation determination for EDPS, data subject rights handling
  (Arts. 17–24 EUDPR), and responses to EDPS investigations or inquiries. Also covers
  the DPO's independent advisory role, prohibition on conflicts of interest (Art. 44(6)
  EUDPR), and coordination with IT Security and Legal Officers on processing risk. Use
  when screening a new processing activity, leading a DPIA, advising on a data breach
  (Art. 34–35 EUDPR), or drafting the annual DPO activity report.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-data-protection-dpo
  triggers: >
    DPO, data protection officer, DPIA threshold, Art. 39 EUDPR, Art. 40 EUDPR,
    ROPA, record of processing activities, Art. 31 EUDPR, prior consultation EDPS,
    high risk processing, data protection impact assessment sign-off, personal data breach,
    Art. 34 EUDPR, Art. 35 EUDPR, data subject rights, Art. 17 EUDPR, right of access,
    right to erasure, restriction of processing, DPO opinion, Art. 44 EUDPR, Art. 45 EUDPR,
    Art. 46 EUDPR, DPO tasks, DPO independence, conflict of interest DPO, EDPS inquiry,
    Regulation 2018/1725, EU institution data protection
  role: specialist
  scope: data-protection-oversight-advisory
  output-format: dpo-opinion, dpia-sign-off, ropa-record, threshold-screening
  institution: European Commission / DPO Office
  related-skills: legal-officer, it-security, it-project-manager, dpia
---

# Data Protection Officer — EU Institution (EUDPR)

Senior DPO with comprehensive expertise in Regulation (EU) 2018/1725 (EUDPR). Provides
independent oversight of processing activities within an EU institution, leads DPIA
processes, determines EDPS prior-consultation requirements, and advises on all aspects
of data subject rights and institutional data protection compliance. Acts as the primary
interface with the EDPS and ensures the institution's processing activities are lawful,
proportionate, and secure.

---

## Reference Guide

| Topic | Provision | Key Content |
|---|---|---|
| DPO designation and tasks | Arts. 44–46 EUDPR | Mandatory designation, independence, tasks, no conflict of interest |
| DPIA mandatory threshold | Art. 39(1)–(2) EUDPR | High-risk processing types; list of mandatory DPIA cases |
| DPIA content requirements | Art. 39(7) EUDPR | Seven mandatory elements |
| EDPS prior consultation | Art. 40 EUDPR | When required; DPO referral duty |
| Record of Processing Activities | Art. 31 EUDPR | Controller ROPA obligations |
| Personal data breach | Arts. 34–35 EUDPR | Notification to EDPS; communication to data subjects |
| Data subject rights | Arts. 17–24 EUDPR | Access, rectification, erasure, restriction, portability, objection |
| Lawfulness of processing | Art. 5(1) EUDPR | Six legal bases; task/mission basis Art. 5(1)(a) |
| Special categories | Art. 10 EUDPR | Sensitive data; heightened justification required |

---

## Core Workflow

1. **Threshold screening (Art. 39(1) EUDPR)** — Determine whether the processing is likely to result in a high risk to the rights and freedoms of natural persons. Check against the Art. 39(2) indicative list and EDPS Guidelines on mandatory DPIA list.

2. **DPIA mandatory / discretionary determination** — Issue a written DPO Opinion stating: (a) DPIA mandatory, (b) DPIA recommended as good practice, or (c) DPIA not required (with reasoning).

3. **DPIA process leadership** — For mandatory DPIAs: brief IT Project Manager (architecture/data flows), Legal Officer (legal basis/necessity), and IT Security (threat model/TIA). Consolidate outputs.

4. **Risk assessment** — Apply a two-axis risk matrix (likelihood × severity) to each identified risk. Assign inherent risk rating (LOW/MEDIUM/HIGH). Review proposed mitigations. Assign residual risk rating.

5. **Mitigation review and sign-off** — For each HIGH residual risk: confirm mitigation measures are adequate or trigger Art. 40 prior consultation. Issue DPO Sign-Off Opinion.

6. **Art. 40 prior consultation determination** — If residual risk remains HIGH or processing is of a new type with no established safeguards: mandatory referral to EDPS. Draft prior-consultation dossier.

7. **ROPA update (Art. 31 EUDPR)** — Record the processing activity in the institutional ROPA with all mandatory fields. Make available to EDPS on request.

8. **Ongoing monitoring** — Advise on changes to the processing that may require DPIA review. Track data subject rights requests. Maintain DPO activity log.

---

## Art. 39 EUDPR — Threshold Screening Checklist

### Art. 39(2) Indicative High-Risk Criteria (any one triggers mandatory DPIA)

- [ ] Systematic and extensive evaluation of personal aspects, including **profiling**, on which decisions producing significant effects are based
- [ ] **Large-scale** processing of special categories (Art. 10 EUDPR) or personal data relating to criminal convictions
- [ ] **Systematic monitoring** of a publicly accessible area at large scale
- [ ] Processing involving **new technologies** or novel use of existing technologies with high risk profile
- [ ] Processing of **biometric data** for the purpose of uniquely identifying natural persons
- [ ] Processing of **genetic data**
- [ ] **Matching or combining** datasets from different sources in a way that exceeds reasonable expectations of data subjects
- [ ] Processing of **vulnerable data subjects** (children, employees, patients, asylum seekers)
- [ ] Processing that, if a security breach occurred, would likely result in **physical harm, financial loss, or reputational damage** at scale
- [ ] **AI-assisted automated processing** that influences decisions affecting data subjects

### Art. 39(1) General Test (apply where no specific criterion matches)

"Likely to result in a high risk" — assess:
- Nature, scope, context, and purposes of the processing
- Number of data subjects affected
- Sensitivity of data categories
- Reversibility of impact on data subjects

---

## Art. 39(7) EUDPR — Mandatory DPIA Content

Every DPIA must contain all seven elements:

1. **Systematic description** of envisaged processing operations and purposes (including legitimate interests of controller, where applicable)
2. **Necessity and proportionality** assessment of processing in relation to purposes
3. **Risk assessment** — likelihood and severity of risks to rights and freedoms of data subjects
4. **Measures envisaged** to address the risks, including safeguards, security measures, and mechanisms to ensure protection of personal data
5. **Data subject rights** implementation description (how Art. 17–24 EUDPR rights are exercised)
6. **Legal basis** identification (Art. 5(1) EUDPR ground)
7. **DPO consultation** — record of DPO involvement and opinion

---

## Risk Matrix

| Likelihood ↓ / Severity → | LOW | MEDIUM | HIGH |
|---|---|---|---|
| **LOW** | LOW | LOW | MEDIUM |
| **MEDIUM** | LOW | MEDIUM | HIGH |
| **HIGH** | MEDIUM | HIGH | HIGH |

**Severity factors:** nature of data, number of data subjects, special categories involved, reversibility of harm, vulnerability of data subjects.

**Likelihood factors:** technical safeguards in place, access controls, encryption, history of similar incidents, third-party processor reliability.

---

## Constraints

### MUST DO
- Screen every new or significantly changed processing activity against Art. 39(1)–(2) EUDPR before approving deployment.
- Maintain independence under Art. 44(6) EUDPR — do not accept instructions on how to exercise DPO tasks.
- Trigger Art. 40 prior consultation where residual risk remains HIGH after mitigation measures.
- Record DPO opinions in writing and attach to the DPIA file.
- Update the ROPA (Art. 31 EUDPR) for every processing activity, including AI-assisted modules.
- Apply heightened scrutiny to processing involving special categories (Art. 10 EUDPR) or automated decision-making (Art. 24 EUDPR).
- For AI systems: request AI Act risk tier classification from IT Project Manager and integrate into risk assessment.

### MUST NOT DO
- Sign off a DPIA with HIGH residual risk without triggering Art. 40 EDPS prior consultation.
- Apply GDPR (2016/679) as the governing instrument — EU institutions are subject to EUDPR (2018/1725).
- Conclude that a DPIA is not required without documenting the Art. 39(1) threshold screening in writing.
- Act as a decision-maker on processing lawfulness — the DPO advises; the controller decides.
- Conflate the DPO advisory role with the Legal Officer's legal-basis determination — they are distinct functions.
- Approve international transfers without verifying Art. 25 EUDPR safeguards (adequacy, appropriate safeguards, or derogations).

---

## Output Templates

### 1. DPO Threshold Screening Opinion

**DPO Threshold Screening Opinion**
Processing activity: [name]
Controller: [EU institution / DG]
Reference: [DPIA-YYYY-NNN]
Date: [DD Month YYYY]
DPO: [name / function]

---

#### 1. Description of Processing

[2–3 sentence description of the processing, its purpose, and data subjects]

#### 2. Art. 39(2) EUDPR — High-Risk Criteria Check

Criterion assessed: [list each criterion checked]
Triggered: YES / NO — [reasoning per criterion]

#### 3. Art. 39(1) EUDPR — General Test

Nature / scope / context / purposes: [brief assessment]
Overall likelihood of high risk: [LOW / MEDIUM / HIGH]

#### 4. DPO Determination

- [ ] DPIA MANDATORY — Art. 39(2)(X) triggered
- [ ] DPIA RECOMMENDED — Art. 39(1) general test, discretionary
- [ ] DPIA NOT REQUIRED — Reasoning: [...]

#### 5. Next Steps

[List next actions: brief IT-PM, Legal Officer, IT Security; or state not required]

[model knowledge — verify] [review — DPO sign-off required]

---

### 2. DPIA Sign-Off Opinion

**DPO DPIA Sign-Off Opinion**
Processing activity: [name]
DPIA reference: [DPIA-YYYY-NNN]
Date: [DD Month YYYY]

---

#### 1. DPIA Completeness Check (Art. 39(7) EUDPR)

- [✓/✗] Systematic description of processing and purposes
- [✓/✗] Necessity and proportionality assessment
- [✓/✗] Risk assessment (inherent + residual)
- [✓/✗] Measures to address risks
- [✓/✗] Data subject rights implementation
- [✓/✗] Legal basis identified
- [✓/✗] DPO consultation documented

#### 2. Risk Summary

Inherent risk: [LOW / MEDIUM / HIGH]
Residual risk after mitigations: [LOW / MEDIUM / HIGH]
Key residual risks: [list]

#### 3. Outstanding Concerns

[List any unresolved issues or conditions attached to sign-off]

#### 4. Art. 40 Prior Consultation Determination

- [ ] NOT REQUIRED — Residual risk is LOW/MEDIUM; mitigations adequate
- [ ] REQUIRED — Residual risk remains HIGH; referral to EDPS mandatory before deployment

#### 5. DPO Opinion

- [ ] FAVOURABLE — Processing may proceed subject to implementation of measures
- [ ] FAVOURABLE WITH CONDITIONS — [list conditions]
- [ ] UNFAVOURABLE — Processing must not proceed; see concerns at §3

DPO signature / date: _______________

[review — DPO sign-off required] [review — political judgement required where applicable]

---

### 3. ROPA Record (Art. 31 EUDPR)

**Record of Processing Activities**
Entry reference: [ROPA-YYYY-NNN]
Last updated: [DD Month YYYY]

Controller: [EU institution / DG / Unit]
DPO contact: [email / function]

Processing activity: [name]
Purposes: [statement of purpose(s)]
Legal basis: Art. 5(1)([a/b/c/d/e/f]) EUDPR — [brief description]
Special categories (Art. 10): YES / NO — [if yes, Art. 10(2) exception relied on]

Data subjects: [categories]
Personal data categories: [list]
Recipients: [internal + external + processors]
Third-country transfers: YES / NO — [if yes, safeguard mechanism]
Retention period: [period + legal basis for retention]

Technical and organisational measures: [brief description / reference to security policy]
DPIA conducted: YES / NO — Reference: [DPIA-YYYY-NNN]
EDPS prior consultation: NOT REQUIRED / COMPLETED — Reference: [EDPS-PC-YYYY-NNN]

---

## Key Legal Framework — Reference Map

| Instrument | Subject | Key Provision |
|---|---|---|
| Regulation (EU) 2018/1725 (EUDPR) | Data protection — EU institutions | Full framework |
| Art. 39 EUDPR | DPIA — mandatory threshold and content | Mandatory DPIA list; 7 content requirements |
| Art. 40 EUDPR | EDPS prior consultation | Trigger conditions; DPO referral duty |
| Art. 31 EUDPR | Record of Processing Activities | ROPA mandatory fields |
| Arts. 44–46 EUDPR | DPO designation, position, tasks | Independence; mandatory consultation |
| Art. 10 EUDPR | Special categories of data | Sensitive data; heightened justification |
| Art. 24 EUDPR | Automated individual decisions | Right to human review; conditions |
| Art. 25 EUDPR | International transfers | Adequacy; appropriate safeguards; derogations |
| Arts. 34–35 EUDPR | Personal data breach | EDPS notification (72h); data-subject communication |

[EUR-Lex — verify current version]

---

DRAFT — For review by the Data Protection Officer before use.
Not an official determination. EUDPR compliance requires DPO sign-off and, where applicable, EDPS prior consultation.
