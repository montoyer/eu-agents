---
name: cold-start-interview
description: >
  Personalise the eu-careers plugin to the candidate's competition target, profile,
  and current preparation stage. Collects degree level, domain, years of experience,
  family situation, and AC readiness. Writes the session context into
  eu-careers/CLAUDE.md. Run this first before using any other skill in this package.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-careers-epso
  triggers: >
    cold start, setup, configure, personalise, my competition, my profile,
    set context, start interview, EPSO setup, careers setup, candidate profile
  role: setup
  scope: session-personalisation
  output-format: session-context-block
  institution: EPSO / EU Institutions
  related-skills: epso-grade, epso-presentation, epso-offer
---

# Cold-Start Interview — EU Careers & EPSO Preparation

Welcome to the **EU Careers & EPSO Preparation** plugin.

This short interview personalises the practice profile for your situation.
Answers are stored in `eu-careers/CLAUDE.md` and carried across all skills
in this package.

---

## Interview Questions

### 1. Target competition
> "Which competition are you targeting?
> (e.g., 'AD5 generalist administrator', 'AD7 economist', 'AST3 assistant',
> 'CAST Permanent FG IV', 'linguist EN-FR', 'specialist — cybersecurity AD7')"

### 2. Candidate profile
> "Tell me a bit about your background:
> - Highest degree and field of study
> - Years of relevant professional experience
> - Any previous EU institution experience (stage, CA, SNE, TA)?
> (e.g., 'Master's in law, 4 years as a national civil servant, no prior EU experience')"

### 3. Current stage
> "Where are you in the EPSO process?
> - Not yet applied / preparing the application
> - Talent screener submitted, waiting for CBT invitation
> - CBT passed, preparing for Assessment Centre
> - Assessment Centre completed, on reserve list
> - Job offer received
> (Answer: one of the above or describe your situation)"

### 4. Family situation (for salary estimates)
> "For salary estimates, what is your family situation?
> - Single, no dependants
> - Married or equivalent (or single parent)
> - Married / single parent with dependent child(ren)
> - Prefer not to say
> (This affects household allowance and dependent child allowance calculations)"

### 5. Duty station
> "Which duty station are you targeting or have been offered?
> (e.g., Brussels, Luxembourg, other EU city or delegation)
> — This affects the expatriation allowance and correction coefficient."

### 6. Working language
> "In which language do you want outputs?
> (default: English)"

---

## What to Do With the Answers

Produce a filled `[SESSION CONTEXT]` block:

```
## [SESSION CONTEXT]

Target competition:       [answer to Q1]
Candidate profile:        [answer to Q2]
Current stage:            [answer to Q3]
Family situation:         [answer to Q4]
Duty station preference:  [answer to Q5]
Working language(s):      [answer to Q6]
```

Then confirm:

> "Session context set. Here is what I can help you with based on your stage:
>
> - `/epso-grade` — Estimate your entry grade, step, and indicative net monthly salary
> - `/epso-presentation` — Prepare and get feedback on your 10-minute oral presentation
> - `/epso-offer` — Decode a job offer: grade, step, salary breakdown, probation terms
>
> All outputs are indicative. Salary figures require PMO verification.
> Eligibility and grade determinations are made solely by the appointing authority."

---
DRAFT — Personalisation helper. Indicative only; not official EPSO or appointing-authority advice.
