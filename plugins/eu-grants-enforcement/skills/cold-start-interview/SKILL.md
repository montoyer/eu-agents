---
name: cold-start-interview
description: >
  Personalise the grants-enforcement-eu plugin to the user's work area (grants,
  procurement, or infringement), programme or member state portfolio, and relevant
  system access. Writes the session context into grants-enforcement-eu/CLAUDE.md.
  Run this first before using any other skill in this package.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-grants-enforcement
  triggers: >
    cold start, setup, configure, personalise, my programme, my portfolio,
    set context, start interview, grants setup, infringement setup
  role: setup
  scope: session-personalisation
  output-format: session-context-block
  institution: European Commission
  related-skills: grant-manager, infringement-officer, procurement-expert
---

# Cold-Start Interview — Grants, Procurement & Enforcement

Welcome to the **Grants, Procurement & Enforcement** plugin.

This interview personalises the practice profile for your work area. Answers
are stored in `grants-enforcement-eu/CLAUDE.md`.

---

## Interview Questions

### 1. DG and Unit
> "Which DG and unit are you in?
> (e.g., DG RTD Unit A.3 — Horizon implementation, DG JUST Unit C.2 — infringement,
> DG GROW Unit D.4 — procurement)"

### 2. Work Area
> "Which of these best describes your current work?
> - Grant management (Horizon Europe / LIFE / CEF / other programme)
> - Infringement procedures (Art. 258–260 TFEU)
> - Public procurement (FR 2018/1046 procedures)
> - Multiple (specify)"

### 3. Programme or Portfolio
For grants:
> "Which programme and call are you working on?
> (e.g., 'Horizon Europe Pillar II, EIC Accelerator, grant ref. 101234567')"

For infringement:
> "Which member state(s) and directive(s) are in your portfolio?
> (e.g., 'Romania — Water Framework Directive transposition',
> 'Italy — Habitats Directive, INFR(2022)0123')"

For procurement:
> "What type of procurement procedure?
> (e.g., open tender for IT services, framework contract for consultancy,
> negotiated procedure without prior publication)"

### 4. Stage
> "What stage are you at?
> - Grants: [eligibility check / cost verification / payment / correction / closure]
> - Infringement: [complaint / EU Pilot / LFN / RO / CJEU referral / Art. 260 follow-up]
> - Procurement: [needs assessment / tender drafting / evaluation / award / contract management]"

### 5. Working Language
> "What language do you need outputs in?
> (default: English — Reasoned Opinions addressed to member states may be in their
> official EU language)"

---

## What to Do With the Answers

Produce a filled `[SESSION CONTEXT]` block:

```
## [SESSION CONTEXT]

DG / Unit:              [answer to Q1]
Work area:              [answer to Q2]
Programme / Portfolio:  [answer to Q3]
Stage:                  [answer to Q4]
Working language(s):    [answer to Q5]
```

Then confirm:

> "Session context set. Available skills:
>
> - `/grant-manager` — MGA cost verification, payment calculation, corrections
> - `/infringement-officer` — LFN, RO, CJEU referral, Art. 260 penalties
> - `/procurement-expert` — tender procedures, evaluation, award decisions
>
> All outputs marked DRAFT. Financial correction decisions flagged
> `[review — financial authorisation required]` before formal adoption."
