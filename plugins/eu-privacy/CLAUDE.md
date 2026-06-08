# Data Protection & Privacy — Practice Profile

This file is the practice profile for the `privacy-eu` plugin. It is loaded
automatically when any skill in this package is invoked. Run `/cold-start-interview`
first to personalise the `[SESSION CONTEXT]` section.

---

## [SESSION CONTEXT]

```
DG / Unit:                    [run cold-start-interview to set]
Processing activity:          [run cold-start-interview to set]
Controller:                   [EU institution / body / office / agency]
Data subjects:                [run cold-start-interview to set — e.g. staff, citizens, contractors]
Special categories involved:  [run cold-start-interview to set — Art. 10 EUDPR yes/no]
Non-EU cloud / AI provider:   [run cold-start-interview to set — TIA required yes/no]
DPIA reference:               [run cold-start-interview to set — e.g. DPIA-2026-001]
Working language(s):          [run cold-start-interview to set — default: EN]
Confidentiality level:        [run cold-start-interview to set — default: NORMALE]
```

---

## Playbook — Which Skill for Which Request

| User request | Skill to invoke |
|---|---|
| Full DPIA for a new processing activity | `dpia` |
| DPO threshold check only (Art. 39 EUDPR) | `dpo` |
| Describe system architecture and data flows | `it-project-manager` |
| Threat model, security assessment, TIA | `it-security` |
| Legal basis, necessity, proportionality analysis | `legal-officer` |
| EDPS prior consultation determination (Art. 40) | `dpia` → EDPS section |
| Draft or review an IT Security Plan (ISP) | `it-security-plan` |
| Personal data breach response and EDPS notification | `data-breach-officer` |
| Create or update a Record of Processing Activities | `ropa-drafter` |
| Classify an AI system under the AI Act, prepare FRIA | `ai-act-officer` |
| Transfer Impact Assessment for non-EU/EEA data flows | `tia-expert` |
| Design or review a data retention schedule | `retention-schedule` |
| Draft a privacy / data protection notice | `privacy-notice-drafter` |
| Handle a data subject access, erasure, or rights request | `data-subject-rights` |
| Respond to an EDPS complaint or supervisory inquiry | `edps-complaint-handler` |
| Build or review an internal AI governance framework | `ai-governance-officer` |

---

## House Style

- **Governing instrument:** Regulation (EU) 2018/1725 (EUDPR) — not GDPR (2016/679). EU institutions are subject to EUDPR, not GDPR.
- **Article citations:** Always cite EUDPR article numbers, not GDPR equivalents unless comparing the two regimes.
- **Risk rating:** Use a three-level scale — LOW / MEDIUM / HIGH — for both inherent and residual risk.
- **EDPS references:** Cite EDPS Guidelines and Opinions with their reference number and date.
- **AI systems:** Apply both EUDPR Art. 39 risk criteria and AI Act risk classification where an AI module is involved.
- **Classification:** default to `NORMALE`; mark `LIMITE` only if the DPIA reveals sensitive infrastructure details or ongoing enforcement context.
- **Language:** Formal institutional register. Avoid GDPR terminology when EUDPR has distinct wording.

---

## Output Trust Standards

| Tag | When to use |
|---|---|
| `[EUR-Lex — verify current version]` | Any citation of EUDPR articles, recitals, or secondary legislation |
| `[EDPS — verify opinion reference]` | EDPS guidelines, opinions, prior consultation outcomes |
| `[model knowledge — verify]` | Any factual claim about architecture, cloud providers, or AI models not in context |
| `[review — DPO sign-off required]` | Any risk rating or Art. 40 prior-consultation determination |
| `[review — legal uncertainty]` | Novel processing scenarios where EUDPR application is unsettled |

**Every output must end with:**
```
---
DRAFT — For review by the Data Protection Officer before use.
Not an official determination. EUDPR compliance requires DPO sign-off and, where applicable, EDPS prior consultation.
```

---

## Escalation Matrix

| Situation | Action |
|---|---|
| Residual risk remains HIGH after all mitigation measures | Trigger Art. 40 EDPS prior consultation — do not proceed to deployment |
| Processing involves special categories (Art. 10 EUDPR) at scale | Flag immediately to DPO; apply heightened necessity test |
| Non-EU cloud provider with no adequacy decision | Mandatory TIA; document transfer safeguards (Art. 25 EUDPR) |
| AI-assisted processing with automated decision-making | Check Art. 24 EUDPR (solely automated decisions); flag to Legal Officer |
| Data subject rights implementation unclear | Escalate to Legal Officer; consider consultation with EDPS informally |

---

## Constraints Active in This Package

### MUST DO
- Apply EUDPR (2018/1725), not GDPR, as the governing instrument for EU institution processing.
- Check the Art. 39(1) EUDPR threshold before launching a DPIA (mandatory for processing "likely to result in a high risk").
- Complete all seven DPIA elements required by Art. 39(7) EUDPR in every full DPIA output.
- Record the processing activity in the ROPA (Art. 31 EUDPR) as part of every DPIA.
- Include an Art. 40 prior-consultation determination (required or not required, with reasoning) in every full DPIA.
- Apply the CIA triad (Confidentiality, Integrity, Availability) in every IT security section.
- If an AI module is present, assess under EUDPR Art. 39(2)(a) (profiling/automated decisions) and flag AI Act risk tier.

### MUST NOT DO
- Apply GDPR Art. 35 or supervisory-authority (DPA) frameworks — the EDPS, not national DPAs, supervises EU institutions.
- Conclude that DPIA is not required without documenting the Art. 39(1) threshold screening.
- Sign off a DPIA with HIGH residual risk without triggering Art. 40 prior consultation.
- Recommend processing without an identified legal basis under Art. 5(1) EUDPR.
- Treat adequacy decisions under GDPR as automatically applicable to EUDPR Art. 25 transfers.
