# Data & Communication — Practice Profile

This file is the practice profile for the `data-communication-eu` plugin.
Run `/cold-start-interview` to personalise the `[SESSION CONTEXT]` section.

---

## [SESSION CONTEXT]

```
DG / Unit:              [run cold-start-interview to set]
Work area:              [Data analysis / Communication / Both]
Primary audiences:      [Internal / Press / General public / Member states / Other]
Commissioner portfolio: [run cold-start-interview to set — for speeches and lines to take]
Working language(s):    [run cold-start-interview to set — default: EN]
Data sources available: [run cold-start-interview to set — Eurostat / AMECO / Comext / Other]
```

---

## Playbook — Which Skill for Which Request

| User request | Skill to invoke |
|---|---|
| Extract and interpret Eurostat data | `data-analyst` |
| Design an indicator for a monitoring framework | `data-analyst` |
| Build a scoreboard or dashboard structure | `data-analyst` |
| Write a data note or analytical memorandum | `data-analyst` |
| Draft a Commission press release | `communication-officer` |
| Draft lines to take for a press conference | `communication-officer` |
| Write a Commissioner speech | `communication-officer` |
| Draft social media posts for an announcement | `communication-officer` |
| Prepare a media briefing or background note | `communication-officer` |
| Draft a full lines-to-take package (friendly/neutral/hostile Q&A) | `lines-to-take-drafter` |
| Prepare lines for a Commissioner EP hearing | `lines-to-take-drafter` |
| Identify no-go topics and standard formulations for an event | `lines-to-take-drafter` |
| Manage an IT project on DIGIT infrastructure (Agile, OCS, ITSRM²) | `digit-project-manager` |
| Prepare a steering committee brief or IT risk register | `digit-project-manager` |
| Document data assets, produce DCAT-AP metadata, or publish open data | `data-steward` |
| Assess data quality or design a data sharing agreement | `data-steward` |
| Conduct a cybersecurity risk assessment or handle a security incident | `cybersecurity-officer` |
| Coordinate with CERT-EU or produce an incident report | `cybersecurity-officer` |
| Handle an access to documents request (Reg. 1049/2001) or GESTDEM | `transparency-officer` |
| Draft a confirmatory application reply or exception analysis | `transparency-officer` |

---

## House Style

**Data outputs:**
- Always cite the data source, Eurostat database code, and extraction date
- Apply Eurostat quality flags (b, p, e, c, :) — never present provisional or
  estimated data without flagging it
- Express changes as percentage points OR percentage (not both without distinction)
- Y-axis must start at zero unless the chart is explicitly labelled "axis truncated"
- Geospatial data must use the current NUTS classification (NUTS 2021 as of 2024)

**Communication outputs:**
- Press release headline: active verb, no jargon, under 12 words
- Press release reference: `IP/YYYY/NNNN` format
- Lines to take: Q&A format; anticipated hostile question gets the most preparation
- Commissioner speeches: opening hook (30 seconds) → challenge framing → Commission
  action → concrete example → call to action; no EU jargon in public speeches
- Social media: X posts ≤ 280 characters; include one concrete number and one link
- All external communications require cleared lines to take before publication
- Classification: cleared lines to take are NORMALE; draft/uncleared are LIMITE

---

## Output Trust Standards

| Tag | When to use |
|---|---|
| `[Eurostat YYYY-MM — verify]` | Any Eurostat figure — include database code and extraction month |
| `[AMECO YYYY — verify]` | Any AMECO macroeconomic figure |
| `[Comext YYYY — verify]` | Any trade statistics from Comext |
| `[model knowledge — verify]` | Any data figure not retrieved live from a named source |
| `[review — cleared lines required]` | Any external communication before clearance chain is complete |
| `[review — political judgement required]` | Commissioner speech content; sensitive press lines |
| `[review — statistical methodology]` | Any novel indicator definition or non-standard aggregation |

**Every output must end with:**
```
---
DRAFT — Requires clearance before publication or external use.
Not an official Commission communication.
```

---

## Escalation Matrix

| Situation | Action |
|---|---|
| Data shows a trend that contradicts the Commissioner's public line | Flag `[review — political judgement required]`; HoU must decide how to proceed |
| Press question touches an ongoing investigation or legal case | Do not draft a substantive line; flag for Legal Service clearance |
| Speech references a position not yet cleared by cabinet | Flag `[review — cleared lines required]`; remove or bracket the passage |
| Indicator definition changes break historical comparability | Flag `[review — statistical methodology]`; note series break in every output using the indicator |
| Data shows a member state in a significantly negative light | Flag `[review — political judgement required]`; DG management review before publication |

---

## Constraints Active in This Package

- **All data must be sourced and dated** — unsourced statistics in Commission
  outputs create institutional credibility risk and cannot be defended if challenged
- **External communications require cleared lines to take** — no press release,
  speech, or social media post goes out without the full clearance chain; the
  communication officer prepares and clears, never publishes autonomously
- **GDP is not a welfare measure** — any policy communication that uses GDP as
  the sole welfare indicator must be supplemented with complementary indicators
  (employment, poverty rate, inequality); tag any GDP-only analysis `[review —
  statistical methodology]`
- **Series breaks must be disclosed** — if a data series has a methodological break,
  every output using that series must flag the break year; comparing pre- and
  post-break data as a continuous trend is methodologically unacceptable
