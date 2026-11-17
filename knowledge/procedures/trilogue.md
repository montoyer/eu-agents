# Agent: Trilogue

**Trigger:** `/trilogue <dossier>`
**Output:** Trilogue simulation — rounds of negotiation leading to political agreement or breakdown.

---

## What this agent does

Simulates the informal inter-institutional trilogue between the European Commission, the European Parliament, and the Council of the EU. Trilogue is how the vast majority of EU legislation is agreed in practice, before formal second reading positions are adopted.

---

## Participants

| Institution | Agent | Role |
|---|---|---|
| European Commission | Lead Commissioner + DG | Defends its proposal; proposes compromises; acts as honest broker |
| European Parliament | EP Rapporteur + political group coordinators | Presents EP mandate; negotiates amendments |
| Council of the EU | Council Presidency + COREPER | Presents Council general approach; negotiates within member-state mandate |

---

## Pre-trilogue setup

### Commission mandate
- The Commission's starting position is its adopted proposal.
- The Commission can modify its proposal at any point during the OLP (Art. 293(2) TFEU — requires unanimity in Council to override Commission position).
- The Commission's goal: achieve an outcome as close to its original proposal as possible while facilitating agreement.

### EP mandate
- Established by the responsible committee's report (adopted by simple majority in committee, then confirmed or amended in plenary).
- The rapporteur leads negotiations; shadow rapporteurs from each political group must be briefed.
- The mandate specifies: which amendments are "must-have" (red lines), "important" (negotiating chips), and "nice-to-have".

### Council mandate
- Established as a "general approach" adopted by Council (by QMV for OLP files).
- The Presidency negotiates on behalf of all member states within this mandate.
- Informal updates to member states through COREPER/working party throughout negotiations.

---

## Trilogue round structure

Each round has three steps:

**1. Opening positions (Round 1 only)**
- Commission: presents key elements of its proposal and where it sees room for compromise.
- Parliament: presents its mandate — priority amendments, red lines.
- Council: presents its general approach — where it diverges from both Commission and EP.

**2. Negotiation on open issues**
- Issues are clustered into packages.
- Typical negotiation pattern:
  - EP proposes amendment → Council counterproposal → Commission bridge text.
  - Four-column document: Commission text | EP position | Council position | Compromise text under negotiation.
- Presidency shuttles between EP and Council delegations (and Commission).

**3. Progress assessment**
- After each round: which issues are closed (provisionally agreed), which remain open.
- Political agreement declared when all issues are closed.

---

## Four-column document format

```
Article [N] — [Title]

| Commission Proposal | EP Position | Council GA | Compromise text |
|---|---|---|---|
| [original text] | [EP amendment] | [Council text] | [draft compromise] |
| Status: baseline | Status: [accepted/rejected/modified] | Status: [accepted/rejected/modified] | Status: [open/agreed] |
```

---

## Typical trilogue dynamics

**Issues where EP typically pushes for:** More ambitious targets; stronger fundamental rights protections; greater EP scrutiny powers (delegated vs. implementing acts); transparency provisions.

**Issues where Council typically pushes for:** More flexibility for member states; longer transition periods; unanimity in Council for sensitive issues; fewer delegated acts.

**Commission role:** Defends the coherence of the original proposal; mediates between EP and Council; proposes compromises when both sides are far apart; can accept EP or Council positions that improve the proposal but signals clearly when amendments undermine its purpose.

---

## Failure conditions

Trilogue fails when:
- EP plenary rejects the mandate or withdraws the rapporteur's negotiating authority.
- Council cannot maintain QMV for the compromise (blocking minority emerges).
- Fundamental red lines on both sides are incompatible.

In failure → **Conciliation Committee** (formal Art. 294(11) procedure) — 6-week deadline; if no agreement → act fails.

---

## Output format

```
TRILOGUE — [DOSSIER TITLE]
Round [N] — [date]

PARTICIPANTS:
Commission: [Commissioner + DG]
EP: Rapporteur [name/portfolio], Shadow rapporteurs: [list]
Council: [Presidency country] Presidency

ROUND SUMMARY:

Issues agreed in this round:
- Article [N]: [what was agreed]
- [...]

Issues still open:
- Article [N]: EP position vs Council position — gap: [describe]
- [...]

Commission bridge text proposed:
- Article [N]: [compromise text]

Progress: [X/Y issues closed]

POLITICAL TEMPERATURE:
[Overall assessment: agreement likely by round N+1 / significant gaps remain / risk of breakdown on [issue]]

NEXT ROUND:
Date: [proposed]
Agenda: [open issues to address]
```

---

## Political agreement declaration

```
POLITICAL AGREEMENT — [DOSSIER TITLE]
Date: [date]

The European Parliament, the Council of the EU, and the European Commission
have reached a political agreement on [dossier].

Key elements of the agreed text:
1. [Element 1]
2. [Element 2]
3. [Element 3]

Points of particular note:
- [Any significant departure from Commission proposal — and Commission's view]

Next steps:
- Legal-linguistic revision: [timeline]
- EP committee confirmation vote: [expected date]
- EP plenary vote: [expected date]
- Council formal adoption: [expected date]
```
