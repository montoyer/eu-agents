# Agent: DPIA Multi-Agent Session

**Trigger:** `/dpia "<processing activity description>"`
**Output:** Complete DPIA report under Art. 39(7) Regulation (EU) 2018/1725 (EUDPR), including Art. 40 EDPS prior-consultation determination.

---

## What this agent does

The DPIA agent orchestrates five specialist roles in sequence to produce a structurally
complete DPIA. Each role contributes a defined section of the DPIA report. The DPO leads
the process and issues the sign-off opinion. The EDPS agent makes the final Art. 40
prior-consultation determination. The output meets all seven mandatory content requirements
of Art. 39(7) EUDPR.

This agent applies to EU institutions, bodies, offices, and agencies subject to
Regulation (EU) 2018/1725 (EUDPR). It does not apply to GDPR-governed entities.

---

## Agent Roster

| Role | Agent skill | Section |
|---|---|---|
| Data Protection Officer (DPO) | `plugins/eu-privacy/skills/dpo/SKILL.md` | §0 Threshold screening; §4 Sign-off |
| IT Project Manager | `plugins/eu-privacy/skills/it-project-manager/SKILL.md` | §1 Technical description |
| Legal Officer | `plugins/eu-privacy/skills/legal-officer/SKILL.md` | §2 Legal analysis |
| IT Security Officer | `plugins/eu-privacy/skills/it-security/SKILL.md` | §3 Security & risk |
| EDPS | `knowledge/agents/edps.md` | §5 Prior consultation |

---

## Sequencing Protocol

### Step 0 — DPO: Threshold Screening
- DPO applies Art. 39(1)–(2) EUDPR threshold test
- If DPIA not required: stop and document
- If DPIA mandatory or recommended: proceed to Step 1

### Step 1 — IT Project Manager: Technical Description
- System architecture and processing operations description (Art. 39(7)(a))
- Data categories, data flows, third-party processors, retention
- AI module documentation and AI Act risk-tier classification if applicable
- Transfer mapping for non-EU/EEA components

### Step 2 — Legal Officer: Necessity and Proportionality
- Legal basis under Art. 5(1) EUDPR (Art. 5(1)(a) task basis or Art. 5(1)(b) contract)
- Necessity analysis: could the purpose be achieved without this processing?
- Proportionality analysis: data minimisation, scope, retention (Art. 39(7)(b))
- Special categories (Art. 10 EUDPR) — heightened necessity where applicable
- Automated decision-making (Art. 24 EUDPR) — if AI outputs affect data subjects
- Data subject rights (Arts. 17–24 EUDPR) implementability check

### Step 3 — IT Security: Threat Model and Risk Assessment
- CIA triad assessment per data flow and storage element
- STRIDE analysis for complex systems
- Inherent risk rating (likelihood × severity) per threat
- Existing technical and organisational measures review
- Residual risk rating after mitigations (Art. 39(7)(c)–(d))

### Step 4 — IT Security: Transfer Impact Assessment (if applicable)
- TIA for every personal data flow to a non-EU/EEA provider (Art. 25 EUDPR)
- Surveillance law assessment for recipient country
- Transfer mechanism verification (adequacy / SCCs / other)
- Transfer risk: LOW / MEDIUM / HIGH

### Step 5 — DPO: Risk Consolidation and Sign-Off
- Art. 39(7) completeness check (all seven elements)
- Overall residual risk determination
- DPO opinion: FAVOURABLE / WITH CONDITIONS / UNFAVOURABLE
- Art. 40 trigger assessment: prior consultation required?

### Step 6 — EDPS: Prior Consultation Determination
- Art. 40(1) EUDPR: required if residual risk HIGH after all mitigations
- Scope of prior consultation dossier if required
- Informal consultation recommendation (Art. 40(3)) if uncertain

---

## Output Format

```
DPIA-[YYYY]-[NNN] — [Processing Activity Name]
Date: [DD Month YYYY]
Controller: [EU institution / DG]
Status: DRAFT — Pending DPO sign-off

§0 — DPO Threshold Screening ........... [MANDATORY / RECOMMENDED / NOT REQUIRED]
§1 — Technical Description ............. [by IT Project Manager]
§2 — Legal Analysis .................... [by Legal Officer]
§3 — Security & Risk Assessment ........ [by IT Security Officer]
§4 — DPO Sign-Off Opinion .............. [FAVOURABLE / WITH CONDITIONS / UNFAVOURABLE]
§5 — EDPS Prior Consultation ........... [REQUIRED / NOT REQUIRED]
```

---

## Interaction Rules

- The DPO may redirect any section back to its authoring role for clarification before sign-off.
- If the IT Security Officer identifies a HIGH residual risk, the DPO must address it in §4 before the EDPS determination.
- If the Legal Officer cannot identify a valid Art. 5(1) legal basis, the DPIA concludes with an UNFAVOURABLE opinion — the DPO does not sign off.
- If an AI module is flagged as PROHIBITED under AI Act Art. 5: the DPIA concludes immediately with an UNFAVOURABLE opinion — the DPO directs discontinuation of the module.
- The EDPS agent in §5 does not determine lawfulness — that is the DPO's role. The EDPS determination is solely about whether Art. 40 prior consultation is required.

---

## Key Legal References

| Provision | Subject |
|---|---|
| Art. 39 EUDPR | DPIA — mandatory threshold and content |
| Art. 40 EUDPR | EDPS prior consultation |
| Arts. 4–5 EUDPR | Principles and legal bases |
| Art. 25 EUDPR | International transfers |
| Art. 33 EUDPR | Security of processing |
| Regulation (EU) 2024/1689 (AI Act) | AI system classification |

[EUR-Lex — verify current version]
