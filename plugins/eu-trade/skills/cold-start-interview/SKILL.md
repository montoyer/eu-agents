---
name: cold-start-interview
description: >
  Personalise the trade-eu plugin to the current investigation type, product,
  country of origin, case reference, investigation phase, and working language.
  Writes the session context into trade-eu/CLAUDE.md. Run this first before
  using any other skill in this package.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-trade-defence
  triggers: >
    cold start, setup, configure, personalise, my investigation, my case,
    set context, start interview, TDI setup, investigation setup
  role: setup
  scope: session-personalisation
  output-format: session-context-block
  institution: European Commission / DG TRADE
  related-skills: trade-defence-investigator
---

# Cold-Start Interview — Trade Defence

Welcome to the **Trade Defence** plugin.

This interview personalises the practice profile for your investigation. Answers
are stored in `trade-eu/CLAUDE.md`.

---

## Interview Questions

### 1. Investigation Type
> "What type of investigation are you working on?
> - Anti-dumping (AD)
> - Anti-subsidy / Countervailing measures (CVD)
> - Safeguards
> - Expiry review (sunset review)
> - Interim review
> - New exporter review
> - Anti-circumvention
> - Foreign Subsidies Regulation (FSR)
> - International Procurement Instrument (IPI)"

### 2. Product and CN Codes
> "What is the product under investigation?
> (include CN codes if known — e.g., 'solar panels, CN codes 8541 40 90 and 8541 40 10')"

### 3. Country of Origin
> "Which country or countries are subject to the investigation?
> (e.g., China, India, Egypt — or specify if NME determination applies)"

### 4. Case Reference
> "What is the case reference?
> (e.g., 'AD/001/2024 — Hot-rolled flat products from China',
> or 'new investigation, no reference yet')"

### 5. Investigation Phase
> "What phase is the investigation in?
> (e.g., complaint assessment / initiation / questionnaire / verification /
> interim disclosure / PCPD / provisional measures / definitive measures / review)"

### 6. Working Language
> "What language do you need outputs in?
> (default: English — NOI drafts are typically in EN for OJ publication)"

---

## What to Do With the Answers

Produce a filled `[SESSION CONTEXT]` block:

```
## [SESSION CONTEXT]

DG / Unit:              DG TRADE — TDI unit
Investigation type:     [answer to Q1]
Product / CN codes:     [answer to Q2]
Country of origin:      [answer to Q3]
Case reference:         [answer to Q4]
Investigation phase:    [answer to Q5]
Working language(s):    [answer to Q6]
```

Then confirm:

> "Session context set. Available skill:
>
> - `/trade-defence-investigator` — complaint assessment, NOI drafting,
>   questionnaire design, dumping margin calculation, injury analysis,
>   lesser duty rule, Union Interest test, PCPD, undertakings
>
> Phase-aware: all outputs will note the statutory deadline for
> [investigation type] investigations and flag proximity to that deadline.
>
> All outputs marked DRAFT and tagged `[review — SBI present]`
> where confidential party data is involved."
