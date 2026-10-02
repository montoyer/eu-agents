---
name: cold-start-interview
description: >
  Personalise the eu-careers plugin to the candidate's competition, profile,
  languages, stage and key dates. Collects the notice of competition reference,
  degree and its official length, dated experience, language 1 and language 2,
  family situation and duty station. Writes the session context into
  eu-careers/CLAUDE.md and points the candidate to the skill that fits their
  stage. Run this first before using any other skill in this package.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "2.0.0"
  domain: eu-careers-epso
  triggers: >
    cold start, setup, configure, personalise, my competition, my profile,
    set context, start interview, EPSO setup, careers setup, candidate profile
  role: setup
  scope: session-personalisation
  output-format: session-context-block
  institution: EPSO / EU Institutions
  related-skills: epso-application, epso-tests, epso-written-test, epso-presentation, epso-grade, epso-offer
---

# Cold-Start Interview — EU Careers & EPSO Preparation

Welcome to the **EU Careers & EPSO Preparation** plugin.

This short interview personalises the practice profile for your situation.
Answers are stored in `eu-careers/CLAUDE.md` and carried across all skills
in this package. Ask the questions one group at a time and accept "skip".

---

## Interview Questions

### 1. Target competition
> "Which competition or selection are you targeting? Give the reference if you
> have it (for example EPSO/AD/427/26), or the type: AD5 graduates, AD7
> specialist in a field, AST3, AST/SC, CAST FG IV, an agency vacancy.
> If you have the notice of competition, paste it or its link. Every answer I
> give on tests, deadlines and eligibility depends on that text."

### 2. Where you are
> "Where are you in the process?
> - Deciding whether to apply
> - Filling in the application
> - Applied, preparing the tests
> - Tests done, waiting for results
> - On a reserve list, looking for a post or invited to an interview
> - Job offer received"

### 3. Key dates
> "Which dates do you already know? Application deadline, document upload
> deadline, test date, interview date, reply deadline for an offer."

### 4. Education and experience
> "Tell me about your background:
> - Highest degree, field, the date it was awarded and the official length of
>   the programme in years
> - Jobs since then, with approximate start and end dates and whether full-time
> - Any EU institution experience (traineeship, contract agent, temporary
>   agent, seconded national expert)"

### 5. Languages
> "Which official EU languages do you have, and at what level? Which would you
> take as language 1 and language 2, if you have decided?"

### 6. Family situation (for salary estimates)
> "For salary estimates: are you single, married or in a registered
> partnership, and do you have dependent children? You can skip this."

### 7. Duty station and nationality (for allowance estimates)
> "Which duty station are you aiming at or have been offered? Which
> nationalities do you hold, and where have you lived and worked over the last
> six years? This decides the expatriation allowance."

### 8. Output language
> "In which language do you want my answers? (default: English)"

---

## What to Do With the Answers

Produce a filled `[SESSION CONTEXT]` block:

```
## [SESSION CONTEXT]

Target competition:       [Q1]
Notice of competition:    [Q1 — OJ reference, or "pasted in session", or "not supplied"]
Candidate profile:        [Q4]
Languages:                [Q5]
Current stage:            [Q2]
Key dates:                [Q3]
Family situation:         [Q6]
Duty station preference:  [Q7]
Output language:          [Q8]
```

Then tell the candidate which skill fits their stage and list the rest:

> "Session context set. For where you are now, start with `/[skill]`.
>
> - `/epso-application` — read the notice, check eligibility, fill in the form, list documents and deadlines
> - `/epso-tests` — priorities, study plan, timed practice and test-day rules for the computer-based tests
> - `/epso-written-test` — prepare and mark the essay or written test
> - `/epso-presentation` — interviews and presentations before a selection panel
> - `/epso-grade` — entry grade, step and net monthly salary with the working
> - `/epso-offer` — decode a job offer, check the step, plan the first months
>
> My assessments are indicative. EPSO's Selection Board, the appointing
> authority and PMO make the binding decisions."

If a known date is less than two weeks away, say so first and name the one
action that cannot wait.

---
DRAFT — Personalisation helper. Indicative only; not official EPSO or appointing-authority advice.
