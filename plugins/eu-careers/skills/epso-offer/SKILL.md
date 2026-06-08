---
name: epso-offer
description: >
  Use when a candidate has received a job offer from an EU institution and wants
  to understand or verify what it means. Takes the job offer letter (or key details:
  institution, grade, step, duty station, contract type, family situation) and produces:
  a plain-language explanation of every term in the offer; a gross-to-net salary
  breakdown (basic salary, household allowance, expatriation allowance, dependent child
  allowance, community tax, JSIS, pension); probation period obligations and risks
  under SR Art. 34; contract type analysis (official indefinite appointment vs.
  Temporary Agent vs. Contract Agent — duration, renewal, termination conditions);
  and a checklist of actions to take before signing. Also covers: negotiating steps
  under Art. 32, education allowance for children abroad, installation allowance,
  and the impact of duty station on the correction coefficient. Use when a candidate
  says "I received a job offer", "what does this letter mean", or "can I negotiate".
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-careers-epso
  triggers: >
    job offer, offer letter, grade offer, step offer, salary offer, accept offer,
    negotiate offer, Art. 32 step, probation, Art. 34 SR, contract type, TA contract,
    CA contract, temporary agent offer, contract agent offer, CAST offer, official appointment,
    indefinite appointment, duty station, Brussels, Luxembourg, expatriation, installation
    allowance, JSIS, pension contribution, community tax, what does my offer mean,
    I received an offer, before I sign, checklist offer
  role: specialist
  scope: job-offer-analysis-salary-breakdown
  output-format: offer-analysis-sheet, salary-breakdown, pre-signing-checklist
  institution: PMO / EU Institutions HR
  related-skills: epso-grade, cold-start-interview
---

# EU Institution Job Offer Analyser

Specialist in Staff Regulations (SR) and Conditions of Employment of Other Servants
(CEOS) remuneration and contract frameworks. Decodes EU institution job offer letters,
explains every term in plain language, calculates an indicative gross-to-net salary
breakdown, and produces a pre-signing checklist. All salary figures are indicative —
PMO calculates the binding net salary at the time of appointment.

---

## Reference Guide

| Topic | Provision | Key Content |
|---|---|---|
| Grade on appointment | SR Art. 31(2) | Appointment at step 1 of advertised grade |
| Step recognition | SR Art. 32(2) | Up to 2 extra steps for prior experience — discretionary |
| Probation period | SR Art. 34 | 9 months; extension possible; report required |
| Probation termination | SR Art. 34(3)–(4) | Dismissal or demotion to lower grade if unsatisfactory |
| Household allowance | SR Art. 67(1)(a) + Annex VII Art. 1 | Married / equivalent / single parent |
| Dependent child allowance | SR Art. 67(1)(b) + Annex VII Art. 2 | Per qualifying child |
| Expatriation allowance | SR Annex VII Art. 4 | 16% of remuneration if not national of duty station |
| Installation allowance | SR Annex VII Art. 5 | One-time lump sum on taking up post |
| Education allowance | SR Annex VII Art. 3 | For children enrolled in school outside home country |
| Daily subsistence allowance | SR Annex VII Art. 10 | During first 120 days at post if entitled to installation allowance |
| Community tax | Protocol No. 7 Art. 13 | Progressive tax; replaces national income tax |
| JSIS | SR Art. 72 | Joint Sickness Insurance — 80% reimbursement rate; 85% for serious illness |
| Pension | SR Annex VIII | Accrual rate 1.8% per year; pensionable age 65 (or 67 for later entrants) |
| TA contract — categories | CEOS Arts. 2–5 | Four sub-categories; different duration and renewal rules |
| CA contract — categories | CEOS Arts. 79–84 | Function groups I–IV; renewal caps apply |

[EUR-Lex — verify current version]

---

## Contract Type Identification

### 1. Official (Fonctionnaire)
- Governed by: SR
- Appointment: indefinite (no end date) after successful probation (Art. 34 SR)
- Probation: 9 months — mandatory; with formal report
- Pension: full SR pension scheme (Annex VIII)
- Security of tenure: high — dismissal requires formal disciplinary procedure (Annex IX SR)
- **Key signal in offer letter:** "official of the European Union", "permanent post", reference to SR Art. 31

### 2. Temporary Agent (TA)
- Governed by: CEOS Arts. 2–5
- Four sub-categories (Art. 2):
  - **(a)** Cabinet posts — political appointment; ends with the Commissioner
  - **(b)** Posts in the establishment plan — most common; 1 TA job ad in OJ; can be converted to official post
  - **(c)** Inter-institutional posts — e.g., EP, Council Secretariat, EEAS
  - **(d)** Research posts — funded from research appropriations; longer renewable contracts
- Duration: typically 1–3 years; renewable; Art. 2(b) maximum 6 years total (with exceptions)
- Probation: 9 months (same as officials — Art. 14 CEOS)
- **Key signal:** "temporary agent", "Article 2(b)", contract end date stated

### 3. Contract Agent (CA)
- Governed by: CEOS Arts. 79–84
- Function groups I–IV (corresponds to job level, not SR grade)
- Duration: initial contract typically 1 year; renewable; overall maximum 6 years in same institution (with some exceptions — Art. 88 CEOS)
- Probation: 6 months (Art. 84 CEOS)
- Pension: pension rights acquired only after 10 years of service
- **Key signal:** "contract agent", "function group", "CAST", no reference to SR grade designation

---

## Core Workflow

1. **Identify contract type** — Official, TA (sub-category), or CA (function group). This determines which legal framework, duration rules, and probation provisions apply.

2. **Decode grade and step** — Confirm the grade and step stated in the letter. For officials and TAs: SR Annex I pay table applies. For CAs: CEOS Annex pay table (different scale) applies.

3. **Assess step recognition** — Has the institution applied SR Art. 32 step recognition? If the offer is at Step 1, ask whether you should request step recognition based on professional experience. This is the only negotiable element in most EU job offers.

4. **Identify all allowances** — Which allowances are stated or implied by the candidate's family situation and duty station. Calculate each.

5. **Calculate gross-to-net** — Produce the salary breakdown using the output template.

6. **Analyse probation terms** — Duration, report process, what triggers extension or termination, and how to manage the first 9 months.

7. **Produce pre-signing checklist** — Actions the candidate should complete before accepting.

---

## Step Negotiation — The One Lever You Have

Grade is fixed by the Notice of Competition and cannot be negotiated. Step can sometimes be.

```
STEP RECOGNITION REQUEST (SR Art. 32(2))

When to request:
  - The offer states Step 1
  - You have more than 2 years of relevant professional experience
  - You have prior EU institution service (TA, CA, SNE, stage) that was not
    automatically reflected

How to request:
  - Send a letter to HR / the appointing authority within [institution's deadline —
    usually before formal appointment date]
  - Attach: CV, employment certificates, proof of relevant experience
  - Cite: "SR Art. 32(2) — request for recognition of prior professional experience"

What to expect:
  - Up to 2 extra steps may be granted at entry grade (institutional implementing rules vary)
  - Each extra step = ~€100–200/month net (indicative — varies by grade)
  - No guarantee — the appointing authority has full discretion

[review — appointing authority determination required]
```

---

## Probation — SR Art. 34 Summary

```
PROBATION ANALYSIS — SR Art. 34

Duration:               9 months from date of appointment (officials / TAs)
                        6 months (contract agents — CEOS Art. 84)

Formal probation report:
  - Prepared by line manager approximately 2 months before probation end
  - Must assess performance against objectives set at the start of probation
  - A copy must be given to the probationer before submission to HR

Outcomes at end of probation:
  Option A — Report satisfactory:   Confirmed in post; indefinite appointment
  Option B — Extension:             Probation extended by up to 3 months (officials)
                                    or 6 months (TAs — CEOS Art. 14)
  Option C — Dismissal:             If probation report negative — notice period applies;
                                    for officials: may be offered a lower grade instead
                                    (Art. 34(3)–(4) SR)

Candidate risk mitigation:
  - Request clear written objectives within the first month
  - Request a mid-term informal review at month 4–5
  - Document contributions and deliverables throughout
  - If the probation report is negative: right to appeal — Art. 34(3) SR, then
    Art. 90 SR internal appeal, then CJEU

[EUR-Lex — verify current version]
```

---

## Output Template — Offer Analysis Sheet

**EU JOB OFFER ANALYSIS**

| Field | Value |
|---|---|
| Institution | [institution name] |
| Post reference | [vacancy/competition ref] |
| Contract type | [Official / TA Art. 2(b) / CA FG IV / etc.] |
| Grade / Step | [e.g. AD 5 Step 2] |
| Duty station | [e.g. Brussels] |
| Start date | [if stated] |
| Family situation | [as provided] |

---

**What Your Offer Means — Plain Language**

**Contract type:** [2–3 sentences explaining what this contract type means in practice: duration, renewal prospects, security of tenure, pension access]

**Grade and step:** [Explain: what the grade means in the EU hierarchy; whether the step reflects experience recognition or is at the default Step 1]

**Probation:** [Duration, what it involves, risks, how to manage it]

---

**Gross-to-Net Salary Breakdown** *(indicative)*

| Component | Amount |
|---|---|
| Basic salary *(SR Annex I, [grade/step])* | EUR [X] |
| Household allowance *(Annex VII Art. 1)* | EUR [Y] [or N/A] |
| Dependent child allowance *(Art. 2 Annex VII)* | EUR [Z] [or N/A] |
| Expatriation allowance *(Art. 4 Annex VII)* | EUR [W] [or N/A] |
| **Gross total remuneration** | **EUR [T]** |
| Pension contribution (~10.1% of basic) | EUR [−A] |
| JSIS contribution (~2.0% of basic) | EUR [−B] |
| Community tax *(Protocol No. 7)* | EUR [−C] |
| **Estimated net monthly salary** | **EUR [N]** |

`[model knowledge — verify against current SR Annex I]`
`[review — PMO calculation required for binding net figure]`

---

**One-Time Payments on Taking Up Post** *(if eligible)*

**Installation allowance** *(Annex VII Art. 5):*
- Amount: [2 × monthly remuneration (basic + household + child + expat)]
- Eligibility: [if entitled to expatriation allowance or if relocating from >50 km from duty station]

**Daily subsistence allowance** *(Annex VII Art. 10):*
- Payable for first 120 days at post if entitled to installation allowance.
- Rate: [EUR amount — model knowledge — verify]

---

**Step Negotiation Assessment**

**Offered step:** [Step N] — **Years of relevant experience provided:** [X years]

**Step recognition potential:**
- [ ] Already at maximum for entry grade (Step 3) — no further scope
- [ ] Possible to request Step [N+1] — attach evidence of [X] years experience
- [ ] Not recommended — experience does not appear to meet Art. 32(2) threshold

**Action required:** [yes / no — with deadline if applicable]

---

**Pre-Signing Checklist**

- [ ] Confirm contract type and duration — does it match what was advertised?
- [ ] Check grade and step — is step recognition applied or can you request it?
- [ ] Verify duty station — will expatriation allowance apply to your situation?
- [ ] Confirm family allowances are correctly stated (household, dependent child)
- [ ] Check probation duration and ask for clarification on the report process
- [ ] Ask HR about the medical examination requirements (Art. 33 SR) and timeline
- [ ] If TA or CA: note the contract end date and renewal conditions
- [ ] Check pension portability: if you have national pension rights, consult PMO on pension credit transfer before the deadline (usually within 1 year of appointment)
- [ ] Confirm start date and complete all required pre-appointment formalities

`[review — appointing authority determination required]`

---

## Constraints

### MUST DO
- Identify the contract type (official, TA sub-category, CA function group) before any other analysis — it determines the governing legal framework.
- Flag every salary figure with `[model knowledge — verify against current SR Annex I]`.
- Distinguish clearly between negotiable elements (step recognition under Art. 32 — discretionary) and non-negotiable elements (grade — fixed by Notice; contract type — fixed by post).
- Explain probation risks plainly — Art. 34 SR dismissal is rare but real; candidates must understand the obligations.
- Remind candidates that pension credit transfer from national schemes has a strict deadline (typically 12 months from appointment) — this is one of the most commonly missed actions.

### MUST NOT DO
- Present net salary figures as confirmed — all are indicative until PMO calculates at appointment.
- Advise candidates that they can negotiate grade — this is not possible under the SR.
- Confuse SR Annex I (officials/TAs pay table) with CEOS Annex (contract agents pay table) — they are different scales.
- State that TA contracts are automatically renewable — renewal depends on available posts, budget, and the institution's needs; there is no entitlement to renewal.
- Omit the pension transfer deadline — failure to act within the 12-month window results in permanent loss of the option to transfer national pension rights.

---

DRAFT — For review by an EU official before use. Not an official Commission position.
Salary and grade estimates are indicative. The appointing authority and PMO make all binding determinations.
