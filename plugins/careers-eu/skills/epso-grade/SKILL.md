---
name: epso-grade
description: >
  Use when a candidate wants to understand what grade and step they would enter
  at if successful in an EPSO competition, and what net monthly salary to expect.
  Takes the competition type (AD5, AD7, AD9, AST3, CAST FG IV, etc.), degree level,
  years of relevant professional experience, and family situation. Returns: entry
  grade and step under SR Art. 31–32, gross basic salary from SR Annex I, applicable
  allowances (household, expatriation, dependent child) under SR Annex VII, standard
  deductions (community tax Art. 13 Protocol No. 7, JSIS, pension, unemployment),
  and an indicative net monthly salary. Flags all figures as requiring PMO verification
  since the SR Annex I pay table is adjusted annually. Also covers grade comparison
  across function groups (AD, AST, CA), step advancement logic, and the impact of
  prior EU service on step recognition.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-careers-epso
  triggers: >
    grade, step, salary, remuneration, pay, net salary, gross salary, AD5, AD7, AST,
    CAST, function group, entry grade, step recognition, experience credit, SR Annex I,
    Annex VII, household allowance, expatriation allowance, dependent child allowance,
    community tax, JSIS, pension contribution, PMO, pay table, salary estimate,
    what would I earn, how much does an AD5 earn, how much does an EU official earn
  role: specialist
  scope: grade-step-salary-estimation
  output-format: grade-step-salary-sheet
  institution: EPSO / PMO / EU Institutions
  related-skills: epso-offer, cold-start-interview
---

# EPSO Grade & Salary Estimator

Specialist in EU Staff Regulations remuneration framework. Calculates indicative
entry grade, step, and net monthly salary for candidates successful in EPSO
competitions. Applies SR Arts. 31–32 (grade on appointment, step recognition),
SR Annex I (pay table), SR Annex VII (allowances), and Protocol No. 7 Art. 13
(community tax). All figures are indicative — PMO is the authoritative calculator
and the appointing authority makes all binding determinations.

---

## Reference Guide

| Topic | Provision | Key Content |
|---|---|---|
| Grade on appointment | SR Art. 31(2) | Appointment at step 1 of the advertised grade |
| Step recognition | SR Art. 32(2) | Up to 2 extra steps for prior professional experience at entry grade |
| Pay table | SR Annex I | Basic monthly salaries by grade and step — read from `references/staff-regulations-annex-i-2026.md` |
| Household allowance | SR Art. 67(1)(a) + Annex VII Art. 1 | Fixed amount + % of basic salary if married/equivalent or single parent |
| Dependent child allowance | SR Art. 67(1)(b) + Annex VII Art. 2 | Per qualifying dependent child |
| Expatriation allowance | SR Annex VII Art. 4 | 16% of (basic + household + dependent child) if not national of duty station |
| Installation allowance | SR Annex VII Art. 5 | One-time lump sum on taking up post — 2× monthly allowances |
| Community tax | Protocol No. 7 Art. 13 | Progressive rates on taxable income; replaces national income tax |
| JSIS contribution | SR Art. 72 | Joint Sickness Insurance Scheme — percentage of basic salary |
| Pension contribution | SR Annex VIII Art. 83(2) | Percentage of basic salary; set annually |
| Unemployment insurance | CEOS Art. 96 | Applies to temporary agents and contract agents only |

[EUR-Lex — verify current version]

---

## Competition Type → Entry Grade Map

| Competition type | Typical entry grade | Notes |
|---|---|---|
| AD5 open competition | AD 5 | General administrators; minimum 3 years experience (or none for some profiles) |
| AD7 specialist competition | AD 7 | Domain specialists; master's + relevant experience required |
| AD9 senior specialist | AD 9 | Senior / management profiles |
| AD12 head of unit | AD 12 | Exceptional; usually internal mobility |
| AST 1 | AST 1 | Assistants — entry level; upper secondary + experience |
| AST 3 | AST 3 | Assistants — experienced |
| AST/SC 1 | AST/SC 1 | Secretarial / clerical — entry level |
| CAST Permanent FG I | FG I | Contract agents — clerical; compulsory education level |
| CAST Permanent FG II | FG II | Contract agents — administrative; secondary + relevant experience |
| CAST Permanent FG III | FG III | Contract agents — executive; post-secondary or secondary + significant experience |
| CAST Permanent FG IV | FG IV | Contract agents — specialist/managerial; university degree + experience |

[model knowledge — verify against current EPSO notice of competition]

---

## Core Workflow

1. **Identify the competition grade** — From the Notice of Competition or candidate input. This is the grade at which the successful candidate will be appointed (Art. 31(2) SR). Candidates cannot negotiate a higher grade.

2. **Determine step on appointment** — Default is step 1. Apply SR Art. 32(2): the appointing authority may grant additional steps based on prior professional experience. Standard implementing rules allow up to 2 extra steps at entry grade (each step requires ~2 years of relevant experience). Note: this is discretionary, not automatic.

3. **Read basic salary from SR Annex I** — Look up the gross basic monthly salary for the grade and step in `references/staff-regulations-annex-i-2026.md`. Do not generate this figure from training data. If the current date is after 31 December 2026, flag that the 2027 adjustment regulation should be checked.

4. **Calculate allowances** — Apply SR Annex VII:
   - Household allowance (Art. 1): if married or equivalent, or single parent with dependant
   - Dependent child allowance (Art. 2): per qualifying child
   - Expatriation allowance (Art. 4): if candidate is not a national of the duty station country and did not reside there for the 5 years before appointment

5. **Gross total remuneration** — Sum of basic salary + all applicable allowances.

6. **Apply standard deductions** — Calculate net:
   - Community tax (Protocol No. 7 Art. 13): progressive; applied to taxable base after deducting pension, JSIS, and unemployment contributions
   - JSIS contribution (Art. 72 SR): applied to basic salary
   - Pension contribution (Annex VIII): applied to basic salary
   - Unemployment insurance (CEOS Art. 96): for TAs/CAs only

7. **Produce the grade/step/salary sheet** — Using the output template below.

---

## Step Recognition Logic (SR Art. 32)

```
STEP RECOGNITION — SR Art. 32(2)

Entry grade of competition:     [e.g. AD 5]
Default appointment:            Step 1

Professional experience assessed:
  Years of relevant experience:   [X years]
  Each additional step requires:  approximately 2 years of relevant experience
  Maximum additional steps:       2 (standard implementing rules at entry grade)

Step on appointment (indicative):
  0–1 year experience:     Step 1
  2–3 years experience:    Step 2 (1 extra step — discretionary)
  4+ years experience:     Step 3 (2 extra steps — discretionary, maximum)

Note: The appointing authority has discretion. Step recognition is not automatic.
Prior EU service as CA, TA, or SNE may be weighted differently.

[review — appointing authority determination required]
```

---

## Allowance Calculation Framework (SR Annex VII)

### Household Allowance (Art. 1 Annex VII)
Payable if: married or legally recognised equivalent; or single parent with a dependent child.

```
Household allowance =
  Fixed amount:    EUR 210.62 (from references/staff-regulations-annex-i-2026.md — verify if after January 2027)
  Variable part:   2% of basic monthly salary
  ─────────────────────────────────────────────────────
  Total:           Fixed + Variable

  If not eligible (single, no dependants): €0
```

### Dependent Child Allowance (Art. 2 Annex VII)
Payable per qualifying dependent child.

```
Dependent child allowance =
  Per child:    EUR 432.38 (from references/staff-regulations-annex-i-2026.md — verify if after January 2027)
  Number of qualifying children: [N]
  ─────────────────────────────────────────────────────
  Total:        Per child × N
```

### Expatriation Allowance (Art. 4 Annex VII)
Payable if the official is not a national of the duty station country AND did not have their habitual residence or main occupation in that country during the 5-year period ending 6 months before taking up post.

```
Expatriation allowance =
  Rate:    16% of (basic salary + household allowance + dependent child allowance)
  ─────────────────────────────────────────────────────
  If not eligible (national of duty station, or residence criteria not met): €0

  Note: Eligibility determination is made by HR at appointment — complex cases
  require individual assessment.
  [review — appointing authority determination required]
```

---

## Deduction Framework

### Community Tax (Protocol No. 7 Art. 13)
EU officials pay no national income tax. Instead they pay a progressive community tax.

```
Taxable base =
  Basic salary
  + Household allowance
  + Dependent child allowance
  + Expatriation allowance
  − Pension contribution
  − JSIS contribution
  − Unemployment insurance contribution (TAs/CAs only)
  − Personal and family allowance deduction (flat rate)

Community tax bands (from references/staff-regulations-annex-i-2026.md — verify if after January 2027):
  0 – 1,156.16:        8%
  1,156.17 – 1,884.15: 10%
  1,884.16 – 2,776.54: 12.5%
  2,776.55 – 3,668.93: 15%
  3,668.94 – 4,561.31: 17.5%
  4,561.32 – 5,453.69: 20%
  5,453.70 – 6,346.07: 22.5%
  6,346.08 – 7,238.45: 25%
  7,238.46 – 8,568.31: 27.5%
  8,568.32 – 9,898.14: 30%
  9,898.15 – 11,956.13: 32.5%
  11,956.14 – 14,014.09: 35%
  14,014.10 – 16,810.92: 37.5%
  above 16,810.92:      45%
```

### Standard Contribution Rates (approximate — verify)

| Deduction | Rate | Base |
|---|---|---|
| Pension contribution | 10.10% | Basic salary |
| JSIS (sickness insurance) | 2.00% | Basic salary |
| Unemployment insurance | 0.81% | Basic salary (TAs/CAs only) |

(from references/staff-regulations-annex-i-2026.md — verify if after January 2027)

---

## Output Template — Grade & Salary Sheet

**EPSO GRADE & SALARY ESTIMATE**

| Field | Value |
|---|---|
| Competition | [competition name / type] |
| Entry grade | [e.g. AD 5] |
| Step on appointment | [1 / 2 / 3 — with reasoning] |
| Duty station | [e.g. Brussels] |
| Family situation | [e.g. single / married with 1 child] |
| Reference date | [month/year of estimate] |

---

**Gross Remuneration**

| Component | Amount |
|---|---|
| Basic salary *(SR Annex I, grade AD5 step 1)* | EUR [X] |
| Household allowance *(SR Annex VII Art. 1)* | EUR [Y] [or N/A] |
| Dependent child allowance *(Art. 2 Annex VII)* | EUR [Z] [or N/A] |
| Expatriation allowance *(Art. 4 Annex VII)* | EUR [W] [or N/A] |
| **Gross total remuneration** | **EUR [T]** |

**Standard Deductions** *(indicative)*

| Deduction | Amount |
|---|---|
| Pension contribution (~10.1% of basic) | EUR [−A] |
| JSIS contribution (~2.0% of basic) | EUR [−B] |
| Community tax *(Protocol No. 7)* | EUR [−C] |
| **Estimated net monthly salary** | **EUR [N]** |

**Notes**

- Step recognition is discretionary (SR Art. 32(2)) — the appointing authority decides.
- Salary figures are based on SR Annex I as known at [date] and must be verified against the current pay table, which is adjusted annually.
- Net figure is an estimate. PMO calculates the authoritative net salary on appointment.
- Expatriation allowance eligibility depends on nationality and residence history — individual assessment required.

`[model knowledge — verify against current SR Annex I]`
`[review — appointing authority determination required]`
`[review — PMO calculation required]`

---

## Constraints

### MUST DO
- Read every salary figure from `references/staff-regulations-annex-i-2026.md`. Cite it as `(SR Annex I 2026 — verify if after January 2027)`. Do not generate figures from training data.
- Explain both the grade (set by the Notice) and the step (discretionary recognition under Art. 32).
- Distinguish between officials (SR applies) and contract agents (CEOS applies — different pay tables and function groups).
- State explicitly that the net salary estimate requires PMO verification for a binding figure.
- Apply the correct allowance eligibility rules — particularly for expatriation allowance, which has strict nationality and residence criteria.

### MUST NOT DO
- Present any salary figure as confirmed or guaranteed — all figures are indicative.
- Suggest that a candidate can negotiate a higher grade than the one advertised in the Notice of Competition.
- Apply national income tax rules — EU officials pay community tax (Protocol No. 7), not national income tax.
- Conflate function groups for contract agents (FG I–IV under CEOS) with grade designations for officials (AD/AST under SR).

---

DRAFT — For review by an EU official before use. Not an official Commission position.
Salary and grade estimates are indicative. The appointing authority and PMO make all binding determinations.
