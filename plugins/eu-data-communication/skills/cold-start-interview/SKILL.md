---
name: cold-start-interview
description: >
  Personalise the eu-data-communication plugin to the user's DG, primary
  audiences, Commissioner portfolio (for speeches), data sources available,
  and working language. Writes the session context into
  eu-data-communication/CLAUDE.md. Run this first before using any other skill.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-data-communication
  triggers: >
    cold start, setup, configure, personalise, my audience, my DG, set context,
    start interview, data setup, communication setup
  role: setup
  scope: session-personalisation
  output-format: session-context-block
  institution: European Commission
  related-skills: data-analyst, communication-officer
---

# Cold-Start Interview — Data & Communication

Welcome to the **Data & Communication** plugin.

This interview personalises the practice profile for your data or communication
work. Answers are stored in `eu-data-communication/CLAUDE.md`.

---

## Interview Questions

### 1. DG and Unit
> "Which DG and unit are you in?
> (e.g., DG COMM Unit B.2 — Digital Media, DG EMPL Unit A.1 — Statistics,
> DG ENV — Communication team)"

### 2. Work Area
> "What are you mainly working on?
> - Data analysis and statistical products (Eurostat, scoreboard, indicators)
> - Communication (press releases, speeches, social media, lines to take)
> - Both"

### 3. Primary Audiences
> "Who are your main audiences?
> (select all that apply)
> - Internal (Commission services, Commissioner's cabinet)
> - Press / journalists
> - General public
> - Member state officials
> - European Parliament
> - Businesses / stakeholders
> - Other (specify)"

### 4. Commissioner Portfolio (for communication work)
> "If you are preparing communication for a Commissioner, which portfolio?
> (e.g., EVP Digital, Commissioner for Environment, Commissioner for Economy)
> If not applicable, say 'not applicable'."

### 5. Data Sources
> "Which data sources do you primarily work with?
> (e.g., Eurostat — national accounts and labour market,
> Comext — trade statistics,
> AMECO — macroeconomic,
> JRC datasets,
> other / specify)"

### 6. Working Language
> "What language do you need outputs in?
> (default: English — press releases are typically issued in EN/FR/DE)"

---

## What to Do With the Answers

Produce a filled `[SESSION CONTEXT]` block:

```
## [SESSION CONTEXT]

DG / Unit:              [answer to Q1]
Work area:              [answer to Q2]
Primary audiences:      [answer to Q3]
Commissioner portfolio: [answer to Q4]
Data sources available: [answer to Q5]
Working language(s):    [answer to Q6]
```

Then confirm:

> "Session context set. Available skills:
>
> - `/data-analyst` — Eurostat extraction, indicators, scoreboards, data notes
> - `/communication-officer` — press releases, lines to take, speeches, social media
>
> Data outputs will be tagged with source and extraction date.
> Communication outputs will be flagged `[review — cleared lines required]`
> until the clearance chain is complete."

---
DRAFT — Personalisation helper. Not an official Commission communication.
