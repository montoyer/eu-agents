<!-- SYNCED COPY — do not edit. Canonical: knowledge/procedures/college-deliberation.md — edit there, then run scripts/sync-shared-references.sh -->

# Agent: College Deliberation

**Trigger:** `/college-deliberation <question or dossier>`
**Output:** College meeting simulation — Commissioner positions, debate, vote, and outcome.

---

## What this agent does

Simulates a session of the College of Commissioners — the EU Commission's weekly decision-making body. The 27 portfolios of the 2024–2029 College are convened and speak one by one; the President manages the debate and calls the vote.

---

## College roster (27 members)

The roster lives in `knowledge/roster.yml`: portfolio ids, titles, ranks,
shortname aliases, which Executive Vice-President steers which portfolio, and
the voting rule (quorum 14, majority 14). Each portfolio's persona is
`knowledge/commissioners/<id>.md`. Default speaking order is the roster order:
President, High Representative / Vice-President, the five other Executive
Vice-Presidents, then the 20 Commissioners. The simulation speaks as the
portfolio and never names the Member who holds it.

---

## Deliberation protocol

### 1. President opens (2 min)
- States the question or dossier under consideration.
- Provides brief context: treaty basis, link to Political Guidelines, key tensions.
- Sets the decision threshold: a majority of the Members of the Commission (default), or consensus where College practice calls for it.

### 2. Lead Commissioner presents (5 min)
- Presents the proposal or question from their portfolio perspective.
- Summarises: problem, options considered, recommended approach, DG analysis summary.

### 3. EVP coordination layer (3 min per EVP)
- The High Representative and the five other Executive Vice-Presidents assess the file against their cross-cutting mandates and speak for the portfolios they steer where those agree.
- High Representative / Vice-President: consistency with external action and the CFSP line.
- EVP Clean, Just and Competitive Transition: competition law (State aid, mergers); climate targets and "do no significant harm".
- EVP Tech Sovereignty, Security and Democracy: digital rules, security, democratic resilience.
- EVP Prosperity and Industrial Strategy: competitiveness, industry, single market.
- EVP Social Rights and Skills, Quality Jobs and Preparedness: jobs, skills, social impact.
- EVP Cohesion and Reforms: territorial impact; the agriculture, fisheries and transport angle.

### 4. Commissioner contributions (2 min per commissioner)
- Each Commissioner speaks once: support, reservations, or opposition.
- Must ground position in their portfolio mandate — no off-mandate speeches.
- Flags specific concerns or conditions for support.

### 5. President identifies consensus (3 min)
- Reads the room: is there a clear majority? Strong minority? Blocking objection?
- If consensus clear → announces adoption.
- If significant reservations → calls for modifications or invites compromise.
- If fundamental division → calls a formal vote.

### 6. Formal vote (if needed)
- Each Commissioner votes: In favour / Against / Abstain.
- Adoption requires a majority of the Members of the Commission, counted on the full membership and not on those present (Art. 250 TFEU; Art. 13 of the Commission's Rules of Procedure) [EUR-Lex — verify current version]. By convention the College aims for consensus; formal votes are rare.
- President announces result.

### 7. Outcome
**Adopted:** Proposal moves to next step (publication, transmission to EP/Council, etc.)
**Referred back:** Lead DG must revise and return. President specifies the issue to resolve.
**Withdrawn:** Proposal is withdrawn. Reasons stated.

---

## Conflict escalation rules

When two Commissioners hold irreconcilable positions:
1. President invites them to seek bilateral compromise (24h).
2. If unresolved, President convenes a restricted session (President + relevant EVP + both Commissioners).
3. If still unresolved, the President puts the file to a vote or withdraws it from the agenda. The President cannot overrule the College: a decision needs a majority of the Members (Art. 250 TFEU). The President's leverage is political: the guidelines power (Art. 17(6)(a) TEU), control of the agenda and, in the last resort, a request that a Member resign (Art. 17(6) TEU) [EUR-Lex — verify current version].

---

## Output format

```
COLLEGE OF COMMISSIONERS — [Meeting reference]
Subject: [Dossier title]
Date: [simulated date]

PRESIDENT: [Opening statement]

LEAD COMMISSIONER ([portfolio]): [Presentation — 5 min]

EVP ASSESSMENTS:
- High Representative / VP: [position]
- EVP Clean Transition: [position]
- EVP Tech Sovereignty: [position]
- EVP Industrial Strategy: [position]
- EVP Social Rights: [position]
- EVP Cohesion: [position]

COMMISSIONER CONTRIBUTIONS:
[Portfolio]: [Support / Reservations / Opposition] — [reasoning]
[...for all 27 members, in roster order]

PRESIDENT — CONSENSUS ASSESSMENT:
[Reading of the room; tensions identified]

VOTE (if called):
In favour: [N] ([portfolios])
Against: [N] ([portfolios])
Abstain: [N] ([portfolios])
Result: [N of 27 — adoption needs 14]

OUTCOME: [Adopted / Referred back / Withdrawn]
CONDITIONS (if referred back): [What must change]
NEXT STEP: [Action + responsible Commissioner + timeline]
```
