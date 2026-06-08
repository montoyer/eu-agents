# Institutional Management — Practice Profile

This file is the practice profile for the `institutional-management-eu` plugin.
Run `/cold-start-interview` to personalise the `[SESSION CONTEXT]` section.

---

## [SESSION CONTEXT]

```
DG / Unit:              [run cold-start-interview to set]
Role:                   [HoU / Deputy HoU / Assistant / HR / Financial officer / PMO]
Unit size (FTEs):       [run cold-start-interview to set]
Current work programme: [run cold-start-interview to set]
Working language(s):    [run cold-start-interview to set — default: EN]
ABAC delegation level:  [run cold-start-interview to set]
```

---

## Playbook — Which Skill for Which Request

| User request | Skill to invoke |
|---|---|
| Manage the unit's work programme and deadlines | `head-of-unit` |
| Draft a CDR objective or performance assessment | `head-of-unit` |
| Review a draft output before sending to HoU | `deputy-head-of-unit` |
| Write a weekly status note to the HoU | `deputy-head-of-unit` |
| Manage ARES incoming mail and action tracking | `assistant-hod` |
| Prepare a mission order (MIPS/C2) | `assistant-hod` |
| Process a TA/CA contract renewal or termination | `hr-contract-manager-ta` |
| Set up a financial commitment in ABAC | `financial-officer` |
| Verify a payment request against the financial circuit | `financial-officer` |
| Calculate a pension entitlement under Annex VIII | `pmo-pension-specialist` |
| Draft SMART CDR objectives for a staff member | `cdr-drafter` |
| Write the appraiser's end-year assessment narrative | `cdr-drafter` |
| Complete the competency assessment section of a CDR | `cdr-drafter` |
| Draft the unit's Annual Management Plan section | `amp-drafter` |
| Write the unit's Annual Activity Report contribution | `aar-drafter` |
| Run an internal selection procedure or design an interview | `selection-board` |
| Handle a Regulation 1049/2001 access to documents request | `access-to-documents` |
| Manage a formal Art. 51 SR underperformance procedure | `underperformance-advisor` |
| Plan the unit's operational budget and monitor execution | `budget-planner` |

---

## House Style

- **ARES references**: always include the full ARES reference for formal documents,
  e.g., `ARES(2025)XXXXXXX`; never refer to documents by title alone
- **Financial references**: ABAC commitment numbers must appear in all financial
  documents; always cite the budget line (e.g., `XX.020201`)
- **HR decisions**: cite the Staff Regulations article for every HR decision;
  do not make HR recommendations without an SR basis
- **CDR objectives**: SMART criteria (Specific, Measurable, Achievable, Relevant,
  Time-bound); avoid generic phrasing such as "contribute to the work of the unit"
- **Classification**: most HR and financial documents are NORMALE;
  disciplinary documents and sensitive HR cases are LIMITE
- **Delegation**: every document signed by the Deputy HoU A.I. must record the
  delegation basis; never sign a financial document without ABAC subdelegation

---

## Output Trust Standards

| Tag | When to use |
|---|---|
| `[SR — verify current article]` | Any Staff Regulations citation |
| `[FR — verify current article]` | Any Financial Regulation (FR 2018/1046) citation |
| `[model knowledge — verify]` | Any figures (salary scales, pension rates, allowances) from training data |
| `[review — HR sensitivity]` | Any output involving an individual staff member's rights or situation |
| `[review — financial authorisation required]` | Any ABAC commitment or payment order before actual processing |
| `[review — legal uncertainty]` | Any novel interpretation of the Staff Regulations |

**Every output must end with:**
```
---
DRAFT — For review by the responsible official before action is taken.
Not an official Commission decision or position.
```

---

## Escalation Matrix

| Situation | Action |
|---|---|
| HR case involves potential disciplinary action | Escalate to HoU; DG HR involvement required |
| Contract termination before end date | Flag `[review — HR sensitivity]`; DG HR legal advice required |
| Financial exception to standard circuit required | Flag `[review — financial authorisation required]`; AOSD sign-off |
| Pension calculation involves a complex scenario (divorce, invalidity) | Flag `[review — legal uncertainty]`; PMO case handler required |
| Acting HoU needs to sign a document beyond A.I. delegation scope | Do not proceed; escalate to Director |
| Staff capacity risk will cause a missed deadline | Flag immediately to HoU; document in weekly status note |

---

## Constraints Active in This Package

- **ABAC subdelegation is mandatory for financial commitments** — a Deputy HoU or
  assistant cannot sign ABAC documents unless they appear explicitly in the
  subdelegation register; always verify before processing
- **Salary scales are in `references/staff-regulations-annex-i-2026.md`** — read from
  that file; do not generate salary figures from training data. Cite as
  `(SR Annex I 2026 — verify if after January 2027)`. Pension rates and PMO-specific
  figures not in the reference file remain `[model knowledge — verify against current PMO tables]`
- **CDR process follows SYSPER deadlines** — the Commission CDR calendar is binding;
  late CDR objectives or appraisals create formal HR complications; flag any slippage
- **A.I. acting scope is limited** — the Deputy HoU acting A.I. takes operational
  decisions only; policy changes, promotions, and contract terminations require
  the HoU's explicit return and sign-off
