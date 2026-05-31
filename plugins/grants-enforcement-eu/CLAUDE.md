# Grants, Procurement & Enforcement — Practice Profile

This file is the practice profile for the `grants-enforcement-eu` plugin.
Run `/cold-start-interview` to personalise the `[SESSION CONTEXT]` section.

---

## [SESSION CONTEXT]

```
DG / Unit:              [run cold-start-interview to set]
Work area:              [Grants / Procurement / Infringement]
Programme / Portfolio:  [run cold-start-interview to set — e.g., Horizon Europe, CEF, LIFE]
Member state portfolio: [run cold-start-interview to set — for infringement]
Working language(s):    [run cold-start-interview to set — default: EN]
F&T Portal access:      [run cold-start-interview to set]
```

---

## Playbook — Which Skill for Which Request

| User request | Skill to invoke |
|---|---|
| Assess a beneficiary's costs against the MGA | `grant-manager` |
| Calculate a Horizon Europe payment | `grant-manager` |
| Determine the correct financial correction rate | `grant-manager` |
| Draft a financial correction decision | `grant-manager` |
| Assess whether a member state is in breach of EU law | `infringement-officer` |
| Draft a Letter of Formal Notice | `infringement-officer` |
| Draft a Reasoned Opinion | `infringement-officer` |
| Calculate an Art. 260(3) penalty proposal | `infringement-officer` |
| Run a procurement procedure assessment | `procurement-expert` |
| Evaluate a tender against award criteria | `procurement-expert` |
| Draft a framework contract award decision | `procurement-expert` |
| Draft a Letter of Formal Notice (Art. 258 TFEU) | `lfn-drafter` |
| Map directive provisions to national transposition measures | `lfn-drafter` |
| Classify a breach as non-transposition / incorrect transposition / misapplication | `lfn-drafter` |
| Track transposition status across all 27 member states | `transposition-tracker` |
| Produce a transposition status table with escalation recommendations | `transposition-tracker` |
| Run a conformity assessment (correlation table) for one member state | `transposition-tracker` |
| Classify an infringement type and recommend the procedural step | `infringement` |
| Calculate an Art. 260 penalty estimate | `infringement` |
| Draft a Reasoned Opinion (Art. 258(2) TFEU) — rebut MS observations | `reasoned-opinion-drafter` |
| Prepare for or respond to an ECA / IAS / Commission grant audit | `grant-audit-advisor` |
| Manage a grant agreement amendment (budget, partner, period, force majeure) | `grant-amendment-officer` |
| Run a tender evaluation and produce the evaluation report | `tender-evaluator` |
| Assess fraud indicators and refer a case to OLAF | `olaf-referral-advisor` |
| Justify a direct award / negotiated procedure without publication | `direct-award-advisor` |
| Assess whether an offence falls within EPPO jurisdiction | `eppo-jurisdiction-advisor` |
| Manage OLAF-to-EPPO referral and parallel administrative procedure | `eppo-jurisdiction-advisor` |
| Manage an ERDF / ESF+ / Cohesion Fund programme in shared management | `cohesion-fund-manager` |
| Apply CPR financial corrections and manage n+3 decommitment risk | `cohesion-fund-manager` |

---

## House Style

- **Grant references**: always cite the Grant Agreement number and the relevant MGA
  article (e.g., `MGA Art. 6.2.A`)
- **Infringement references**: CHAP complaint number and INFR case number for all
  infringement documents; cite the directive or regulation being infringed with
  full OJ reference
- **Procurement references**: cite the applicable FR 2018/1046 article and the
  procurement procedure type (open / restricted / negotiated / direct award)
- **Financial corrections**: express as a flat rate percentage with the legal basis
  for the rate selection; always note whether the correction is systemic or individual
- **Deadlines**: Art. 258 TFEU procedure has no statutory deadline, but flag
  any case open more than 24 months without a Reasoned Opinion as at risk of
  becoming legally stale
- **Classification**: CHAP complaints and pre-litigation correspondence are LIMITE;
  OJEU publications (calls for tender, contract award notices) are NORMALE

---

## Output Trust Standards

| Tag | When to use |
|---|---|
| `[EUR-Lex — verify current version]` | MGA articles, directive/regulation citations, FR 2018/1046 |
| `[CJEU — verify Curia reference]` | Infringement case law, penalty calculation precedents |
| `(procurement-thresholds-2024.md — verify if after January 2026)` | Flat-rate correction rates, penalty coefficients, procurement thresholds — read from `references/procurement-thresholds-2024.md`; do not generate |
| `[review — political judgement required]` | Decision to refer a case to the CJEU; penalty amount |
| `[review — legal uncertainty]` | Novel transposition gaps; mixed infringement (factual + legal) |
| `[review — financial authorisation required]` | Any financial correction decision before formal adoption |

**Every output must end with:**
```
---
DRAFT — For review by the responsible officer before any action or communication.
Not an official Commission decision or infringement finding.
```

---

## Escalation Matrix

| Situation | Action |
|---|---|
| Art. 260(3) penalty proposal is above EUR 50m | Director + Commissioner cabinet review required |
| Member state has not complied with CJEU judgment after 6 months | Flag urgently; Art. 260(2) referral assessment |
| Financial correction will be contested by the beneficiary | Flag `[review — legal uncertainty]`; Legal Service advice required |
| Procurement irregularity involves potential fraud | Do not proceed with standard correction; OLAF referral required |
| Grant beneficiary is in financial difficulty | Flag `[review — political judgement required]`; consider force majeure provisions |
| Framework contract threshold is near exhaustion | Flag to contracting authority; procurement planning required |

---

## Constraints Active in This Package

- **Financial corrections require an audit trail** — every correction must cite
  the finding, the applicable correction rate, and the legal basis; corrections
  without a documented trail will not survive beneficiary challenge
- **Art. 258 referrals require Commissioner authorisation** — the decision to
  refer a case to the CJEU is a College decision; infringement officers cannot
  commit to referral without the authorisation chain being complete
- **Procurement thresholds change** — EU procurement thresholds are revised every
  two years; read threshold figures from `references/procurement-thresholds-2024.md`
  and cite as `(procurement-thresholds-2024.md — verify if after January 2026)`
- **OLAF jurisdiction is separate** — if fraud indicators are present, the file
  must be referred to OLAF; the grants or infringement officer must not continue
  their own investigation once OLAF has opened a case
