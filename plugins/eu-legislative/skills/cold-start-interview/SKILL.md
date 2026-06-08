---
name: cold-start-interview
description: >
  Personalise the legislative-eu plugin to the user's DG, active dossier(s),
  Council configuration, working language, and Commissioner portfolio. Writes
  the session context into legislative-eu/CLAUDE.md so all subsequent skills
  operate with the correct institutional frame. Run this first in every new
  session before using any other skill in this package.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-legislative
  triggers: >
    cold start, setup, configure, personalise, my dossier, my DG, my unit,
    set context, start interview, who am I, what is my role
  role: setup
  scope: session-personalisation
  output-format: session-context-block
  institution: European Commission
  related-skills: policy-officer, legislative-drafter, lawyer-secgen,
    comitology-officer, impact-assessment-analyst, economist
---

# Cold-Start Interview — Legislative & Policy

Welcome to the **Legislative & Policy** plugin for the European Commission.

This interview takes 2 minutes. Your answers personalise the practice profile
so every skill in this package produces outputs calibrated to your DG, dossier,
and working context. Answers are stored in `legislative-eu/CLAUDE.md` under
`[SESSION CONTEXT]` for this session.

---

## Interview Questions

Ask the user the following questions. Accept brief answers — expand from context.

### 1. DG and Unit
> "Which DG and unit are you working in?
> (e.g., DG GROW Unit B.2, DG ENV Unit C.1, SecGen Unit E)"

### 2. Active Dossier(s)
> "What is your main dossier or proposal right now?
> (e.g., 'Packaging and Packaging Waste Regulation — trilogue stage',
> 'Artificial Intelligence Liability Directive — Council first reading',
> 'Delegated act on CBAM methodology')"

### 3. Procedural Stage
> "What stage is your dossier at?
> (e.g., inception / impact assessment / ISC / EP first reading / Council WP /
> trilogue / comitology / implementation)"

### 4. Council Configuration
> "Which Council configuration are you primarily working with?
> (e.g., Competitiveness, Environment, Internal Market, Transport, ECOFIN,
> Agriculture, General Affairs)"

### 5. Commissioner Portfolio
> "Which Commissioner's portfolio does your dossier fall under?
> (e.g., EVP Digital, Commissioner for Environment, Commissioner for Trade)"

### 6. Working Language(s)
> "What language(s) do you need outputs in?
> (default: English — also available: French, German, or bilingual EN/FR)"

### 7. Sensitive Context (optional)
> "Is there anything I should know about the sensitivity of this dossier?
> (e.g., politically sensitive, LIMITE handling, NDA with member states,
> ongoing trilogues with Parliament — or just say 'standard')"

---

## What to Do With the Answers

Once the user has answered, produce a filled `[SESSION CONTEXT]` block and tell
the user to paste it into `legislative-eu/CLAUDE.md`, replacing the placeholder:

```
## [SESSION CONTEXT]

DG / Unit:              [answer to Q1]
Active dossier(s):      [answer to Q2]
Procedural stage:       [answer to Q3]
Council configuration:  [answer to Q4]
Commissioner portfolio: [answer to Q5]
Working language(s):    [answer to Q6]
Sensitivity:            [answer to Q7 — default: NORMALE]
```

Then confirm:

> "Session context set. You can now use any skill in this package:
>
> - `/policy-officer` — briefing notes, negotiating briefs, ISC contributions
> - `/legislative-drafter` — draft regulations, directives, decisions
> - `/lawyer-secgen` — ISC legal quality review, subsidiarity analysis
> - `/comitology-officer` — delegated/implementing acts, committee procedures
> - `/impact-assessment-analyst` — Better Regulation impact assessments
> - `/economist` — economic analysis, market failure, CBA
>
> All outputs will be calibrated to: [DG/Unit] — [dossier] — [stage]."
