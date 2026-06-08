---
name: cold-start-interview
description: >
  Personalise the institutional-management-eu plugin to the user's DG, unit,
  management role, unit size, ABAC delegation level, and current work programme
  priorities. Writes the session context into institutional-management-eu/CLAUDE.md.
  Run this first before using any other skill in this package.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-institutional-management
  triggers: >
    cold start, setup, configure, personalise, my unit, my role, set context,
    start interview, management setup, unit setup
  role: setup
  scope: session-personalisation
  output-format: session-context-block
  institution: European Commission
  related-skills: head-of-unit, deputy-head-of-unit, assistant-hod,
    hr-contract-manager-ta, financial-officer, pmo-pension-specialist
---

# Cold-Start Interview — Institutional Management

Welcome to the **Institutional Management** plugin.

This interview personalises the practice profile for your unit and management
role. Answers are stored in `institutional-management-eu/CLAUDE.md`.

---

## Interview Questions

### 1. DG and Unit
> "Which DG and unit are you in?
> (e.g., DG GROW Unit A.4, DG ENV Unit B.1 — or specify your DG's finance/HR team)"

### 2. Your Role
> "What is your role in the unit?
> - Head of Unit
> - Deputy Head of Unit
> - Assistant to the HoU
> - HR and Contract Manager
> - Financial Officer
> - PMO / Pension enquiry
> - Other (specify)"

### 3. Unit Size
> "Roughly how many people are in your unit?
> (e.g., 8 FTEs, 12 FTEs — or 'small unit, under 10')"

### 4. Current Work Programme Priorities
> "What are the top 1–3 deliverables your unit is working towards right now?
> (e.g., 'legislative proposal by Q3', 'implementing regulation by November',
> 'preparing 3 infringement opinions', 'closing the AAR')"

### 5. Financial Delegation
> "Do you have ABAC subdelegation?
> (e.g., 'yes — AOSD for budget line XX.020201',
> 'no — all financial commitments go to the HoU',
> 'not relevant for my role')"

### 6. Working Language
> "What language do you need outputs in?
> (default: English)"

---

## What to Do With the Answers

Produce a filled `[SESSION CONTEXT]` block:

```
## [SESSION CONTEXT]

DG / Unit:              [answer to Q1]
Role:                   [answer to Q2]
Unit size (FTEs):       [answer to Q3]
Current work programme: [answer to Q4]
ABAC delegation level:  [answer to Q5]
Working language(s):    [answer to Q6]
```

Then confirm:

> "Session context set. Available skills:
>
> - `/head-of-unit` — work programme, CDR, staff decisions, AMP
> - `/deputy-head-of-unit` — quality review, deadline tracking, A.I. acting
> - `/assistant-hod` — ARES, MIPS/C2 missions, SYSPER, action trackers
> - `/hr-contract-manager-ta` — TA/CA contracts, CAST, renewals
> - `/financial-officer` — ABAC circuit, commitments, payment orders
> - `/pmo-pension-specialist` — Annex VIII calculations, PMO entitlements
>
> All outputs will be marked DRAFT.
> HR-sensitive outputs will be flagged `[review — HR sensitivity]`."
