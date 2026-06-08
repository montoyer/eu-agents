# Trade Defence — Practice Profile

This file is the practice profile for the `trade-eu` plugin.
Run `/cold-start-interview` to personalise the `[SESSION CONTEXT]` section.

---

## [SESSION CONTEXT]

```
DG / Unit:              [run cold-start-interview to set — default: DG TRADE]
Investigation type:     [AD / CVD / Safeguard / FSR / IPI / Review]
Case reference:         [run cold-start-interview to set]
Product / CN codes:     [run cold-start-interview to set]
Country of origin:      [run cold-start-interview to set]
Investigation phase:    [Complaint / Initiation / Questionnaire / Verification / Disclosure / Measures]
Working language(s):    [run cold-start-interview to set — default: EN]
```

---

## Playbook — Which Skill for Which Request

| User request | Skill to invoke |
|---|---|
| Assess a complaint for standing and sufficiency | `trade-defence-investigator` |
| Draft a Notice of Initiation | `trade-defence-investigator` |
| Design an exporting producer or importer questionnaire | `trade-defence-investigator` |
| Calculate a dumping margin | `trade-defence-investigator` |
| Assess injury indicators and establish causation | `trade-defence-investigator` |
| Apply the lesser duty rule | `trade-defence-investigator` |
| Draft a pre-closure pre-disclosure document (PCPD) | `trade-defence-investigator` |
| Assess a price undertaking offer | `trade-defence-investigator` |
| Draft or review a Union Interest test | `trade-defence-investigator` |
| Assess anti-circumvention evidence | `trade-defence-investigator` |
| Calculate a dumping margin — normal value, export price, Art. 2(10) adjustments | `dumping-margin-calculator` |
| Apply the lesser duty rule and compare dumping vs. injury margin | `dumping-margin-calculator` |
| Screen a counterparty or transaction against EU restrictive measures | `sanctions-screener` |
| Assess asset freeze obligations and derogation options | `sanctions-screener` |

---

## House Style

- **Case references**: all outputs cite the OJ reference and investigation case number
- **CN codes**: product scope is defined by CN codes; always specify the 8-digit code
  and note any product exclusions explicitly
- **Margins**: dumping and injury margins are expressed as a percentage of the CIF
  import price at EU border; never express as a percentage of domestic price
- **Lesser duty rule**: the output must explicitly show both the dumping/subsidy
  margin and the injury margin (underselling margin) and take the lower of the two
- **NME / surrogate country**: if a non-market economy determination applies, flag
  the surrogate country used and the methodology for selecting it
- **Deadlines**: always note the statutory deadline for the current phase
  (9 months to provisional for AD; 13 months to definitive for CVD);
  flag proximity to deadline in every output
- **Classification**: case-related outputs default to LIMITE;
  public NOI and disclosures are NORMALE for OJ publication

---

## Output Trust Standards

| Tag | When to use |
|---|---|
| `[EUR-Lex — verify current version]` | Basic AD Regulation 2016/1036, Basic AS Regulation 2016/1037 citations |
| `[WTO — verify ADA/SCM compliance]` | Any procedural step or calculation with WTO implications |
| `[TARIC — verify current CN codes]` | Product scope CN code references |
| `[model knowledge — verify]` | Any market data, import statistics, or production figures from training data |
| `[review — political judgement required]` | Union Interest test conclusions; undertaking acceptance/rejection |
| `[review — legal uncertainty]` | Novel NME methodology; contested causation analysis |
| `[review — SBI present]` | Output contains confidential data submitted by a party |

**Every output must end with:**
```
---
DRAFT — For review by the responsible investigator and Legal Service before use.
Not an official Commission TDI finding or position.
```

---

## Escalation Matrix

| Situation | Action |
|---|---|
| Provisional measures deadline approaching (< 4 weeks) | Flag urgently; Director-level escalation |
| NME methodology is contested | Flag `[review — legal uncertainty]`; Legal Service + WTO unit review |
| Undertaking offer received | Flag `[review — political judgement required]`; Director sign-off required |
| A sampled party refuses verification (OSV) | Flag; trigger adverse facts available (Art. 18) assessment |
| WTO consistency of a proposed measure is uncertain | Mandatory Legal Service review before imposition |
| Union Interest test conclusion is negative | Flag `[review — political judgement required]`; Director and cabinet involvement |

---

## Constraints Active in This Package

- **Statutory deadlines are binding** — WTO Agreements (ADA Art. 5.10, SCMA Art.
  11.11) and the Basic Regulations impose hard deadlines; measures not imposed within
  the statutory period lapse automatically
- **Lesser duty rule is mandatory in EU law** — Art. 7(2) and 9(4) Basic AD
  Regulation; the duty is the lower of the dumping margin and the injury margin;
  any output suggesting otherwise is legally incorrect
- **Unverified data cannot support calculations** — margins based on unverified data
  are procedurally defective; always note verification status of data used
- **Price undertakings are individual, not governmental** — Art. 8 Basic AD
  Regulation; government-level undertakings are not legally valid
