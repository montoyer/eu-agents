---
name: cold-start-interview
description: >
  Personalise the competition-eu plugin to the user's unit, case type, case
  reference, sector, confidentiality level, and working language. Writes the
  session context into competition-eu/CLAUDE.md so all subsequent skills operate
  with the correct institutional and legal frame. Run this first in every new
  session before using any other skill in this package.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-competition
  triggers: >
    cold start, setup, configure, personalise, my case, my unit, set context,
    start interview, who am I, what is my role
  role: setup
  scope: session-personalisation
  output-format: session-context-block
  institution: European Commission / DG COMP
  related-skills: lawyer-competition-antitrust, lawyer-state-aid, lawyer-legal-service
---

# Cold-Start Interview — Competition & Legal Service

Welcome to the **Competition & Legal Service** plugin.

This interview takes 2 minutes. Your answers personalise the practice profile
for your case or opinion work. Answers are stored in `competition-eu/CLAUDE.md`
under `[SESSION CONTEXT]`.

---

## Interview Questions

### 1. DG and Unit
> "Which DG and unit are you in?
> (e.g., DG COMP Unit F.1, DG COMP State Aid team, Commission Legal Service Unit X)"

### 2. Work Area
> "What type of work are you doing?
> - Antitrust case (Art. 101 / Art. 102 TFEU)
> - State aid case (Art. 107–109 TFEU)
> - Legal Service opinion
> - Litigation (CJEU / General Court)
> - DMA enforcement
> - Other (specify)"

### 3. Case Reference and Sector
> "What is the case reference or dossier name, and in what sector?
> (e.g., 'AT.40099 Google Shopping — digital platforms',
> 'SA.56789 — renewable energy scheme for Germany',
> 'SJ-2025-0042 — legal opinion on draft delegated act')"

### 4. Procedural Stage
> "What stage is the case or opinion at?
> (e.g., pre-investigation / RFI sent / dawn raid conducted /
> Statement of Objections / oral hearing / final decision /
> pre-notification contacts / formal notification / ISC review)"

### 5. Confidentiality
> "What is the confidentiality level?
> - NORMALE — no special restrictions
> - LIMITE — pre-decisional, restricted distribution
> - Contains SBI — sensitive business information from parties"

### 6. Working Language
> "What language do you need outputs in?
> (default: English)"

---

## What to Do With the Answers

Produce a filled `[SESSION CONTEXT]` block:

```
## [SESSION CONTEXT]

DG / Unit:              [answer to Q1]
Case type:              [answer to Q2]
Case reference:         [answer to Q3]
Sector:                 [sector from Q3]
Procedural stage:       [answer to Q4]
Confidentiality level:  [answer to Q5]
Working language(s):    [answer to Q6]
```

Then confirm:

> "Session context set. Available skills:
>
> - `/lawyer-competition-antitrust` — Arts. 101–102 analysis, SO drafting, fines
> - `/lawyer-state-aid` — four-limb test, GBER screening, recovery
> - `/lawyer-legal-service` — CLS opinions, litigation, Written Observations
>
> All outputs will be marked DRAFT and tagged for human review.
> SBI-containing outputs will be flagged `[review — SBI present]`."
