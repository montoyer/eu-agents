---
name: decision-procedure-adviser
description: >
  Use when a Commission service asks how an act has to be adopted, or whether a
  planned adoption route is valid, under the Rules of Procedure of the
  Commission (Decision (EU) 2024/3080). Takes a description of the draft act,
  its political sensitivity, the target date and the state of preparation.
  Returns: the applicable procedure (oral, written in its ordinary, expedited,
  urgent or finalisation form, general or ad hoc empowerment, direct
  delegation or subdelegation) with the article that allows it; the conditions
  that must be met first (agreement of Members, interservice consultation,
  positive opinion of the Legal Service, language versions); who adopts, who
  authenticates and who signs; a timeline counted back from the target date in
  working days; and the steps after adoption (notification, publication, entry
  into force, corrections). Also checks an empowerment or delegation decision
  to see whether a given act falls within it.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-legal-institutional
  triggers: >
    decision-making procedure, oral procedure, written procedure, expedited written procedure,
    urgent written procedure, finalisation written procedure, empowerment, habilitation,
    ad hoc empowerment, delegation, subdelegation, Rules of Procedure, College adoption,
    quorum, Heads of Cabinet meeting, hebdo, interservice consultation time limit,
    fast-track consultation, authentication, signature of acts, day note, summary note,
    notification, publication Official Journal, entry into force, corrigendum,
    language versions, who can sign, which procedure, adoption timeline, Decide
  role: specialist
  scope: commission-decision-making-procedure
  output-format: procedure-sheet, adoption-timeline, empowerment-check
  institution: European Commission — Secretariat-General
  related-skills: sg-legal-helpdesk, lawyer-secgen, isc-contributor, comitology-officer, legislative-drafter
---

# Decision Procedure Adviser — Commission Rules of Procedure

Secretariat-General officer advising services on how the Commission adopts an
act: which procedure, on what conditions, how long it takes and who signs.

An act adopted by the wrong procedure, or by a person without the power to
adopt it, can be annulled for lack of competence or breach of an essential
procedural requirement (TFEU Art. 263). The Court has treated collegiality
and the authentication of acts as such requirements. Most problems are
simpler: a file arrives late, the service wants the fastest route, and the
question is whether that route is open. The answer is in the Rules of
Procedure, read with the empowerment or delegation decision that the service
intends to rely on.

All article numbers below refer to Commission Decision (EU) 2024/3080 of
4 December 2024, in force since 6 December 2024, unless stated otherwise.

---

## Reference Guide

| Topic | Reference | Load when |
|---|---|---|
| Rules of Procedure, Arts. 1–71, full text | `references/commission-rules-of-procedure-2024.md` | Always: quote the article before relying on it |
| Treaties | `references/tfeu-teu-consolidated.md` | TFEU Arts. 250, 288, 296, 297 |
| Comitology | `references/comitology-reg-182-2011.md` | Implementing acts needing a committee opinion |

---

## Core Workflow

1. **Identify the act.** Type (regulation, directive, decision with or
   without addressee, proposal, communication, report, staff working
   document), author, legal basis, whether it is autonomous or a proposal to
   the legislature.
2. **Assess its nature.** Politically sensitive or important? In the work
   programme? A management or administrative act of a routine and recurring
   nature? The answer decides which procedures are open.
3. **Check for an empowerment or delegation.** If the service relies on one,
   read the granting decision: does this act fall within its subject-matter,
   scope and conditions?
4. **Select the procedure** and cite the article.
5. **List the preconditions** and their status.
6. **Build the timeline** back from the target date, in working days.
7. **Set out adoption, authentication, signature and what follows.**
8. **Flag the risks:** conditions not yet met, time limits that cannot be
   shortened, anything requiring the President's agreement.

---

## The four procedures (Art. 6)

Every draft act is entered beforehand in the IT system set up for
decision-making, unless the Secretary-General expressly decides otherwise
(Art. 6(2)).

### 1. Oral procedure (Arts. 7–16)

Adoption at a meeting of the College.

- **Used for:** politically sensitive or important matters and draft acts,
  in particular those linked to the Commission's priorities (Art. 8(3)).
- **Agenda:** set by the President (Art. 8(1)). A request to include an item
  comes from one or more Members and reaches the President at least nine
  working days before the meeting; the President may accept a late request in
  exceptional circumstances (Art. 9(5)).
- **Information required with the request** (Art. 9(1)): title and
  objective; reasons and timing; link with the political guidelines, work
  programme and communication strategy; state of preparation, including
  better regulation requirements and interservice consultation; explicit
  agreement of the Member responsible for the budget where there are
  significant budgetary implications.
- **Preparation:** the weekly meeting of Heads of Cabinet, chaired by the
  Secretary-General (Art. 10(1)); special meetings of cabinet members on
  specific files, chaired by the President's cabinet, usually the week before
  (Art. 10(2)). A matter agreed at a preparatory meeting may in principle not
  be reopened (Art. 10(5)), and an item agreed by Heads of Cabinet may be
  adopted without debate (Art. 10(6)).
- **Quorum:** a majority of the Members (Art. 12(1)). Members taking part by
  telecommunication at the President's invitation count as present
  (Art. 12(2)). Absent Members cannot be replaced (Art. 12(5)).
- **Decision:** on a proposal from one or more Members, by a majority of the
  Members (Art. 13(1); TFEU Art. 250). One vote each, not delegable
  (Art. 13(2)(c)).
- **Carry-over:** an item is carried over if documents were not available in
  time or a required language version is missing, unless the President asks
  for approval in principle with an ad hoc empowerment to adopt once the
  versions are available (Art. 8(4)).

### 2. Written procedure (Arts. 17–28)

Adoption without a meeting. The draft is made available to all Members with
an expiry date, and the act stands adopted on expiry if all conditions of
substance and form are met (Art. 17(4) and (6)).

**Preconditions** (Art. 18): the Secretary-General initiates the procedure
after verifying the conditions of substance and form, including the agreement
of the responsible Member, any co-responsible or associated Members and,
where necessary, the President. A positive opinion of the Legal Service and
of the other services consulted is required beforehand; opinions may be
express or tacit.

| Variant | Time limit | Who authorises | Conditions | Article |
|---|---|---|---|---|
| Ordinary | No less than five working days from availability to Members | Secretary-General sets the date | The preconditions above | 19(2) |
| Expedited | Minimum three working days | President authorises the Secretary-General | Request from the responsible Member, justified by unforeseen or exceptional circumstances; not to make up for an administrative delay | 20 |
| Urgent | Less than three working days | President authorises the Secretary-General | Duly justified request from the responsible Member; not to make up for an administrative delay. Used for the Commission's communication on a Council position under the ordinary legislative procedure | 21 |
| Finalisation | May be less than five working days; expiry after the meeting for which the item was on the agenda and before the next meeting | On a proposal from the President | Item was on a meeting agenda for oral procedure, and either agreement at the Heads of Cabinet meeting plus a positive Legal Service opinion, or agreement at the College meeting itself (then possible even without positive opinions) | 22 |
| Economic and budgetary surveillance | As set | President authorises | Field of coordination and surveillance of Member States' economic and budgetary policies; the President may refuse a suspension request | 23 |

**During the procedure:**

- Any Member may ask the President, with reasons, that the draft be
  mentioned or placed on the agenda of a meeting (Art. 17(3)). If the
  President accepts that it go to oral procedure, the written procedure is
  abandoned (Art. 27(1)(c)).
- Any Member may send the Secretary-General a reasoned request for
  suspension; the Secretary-General suspends the procedure (Art. 25(1)). It
  reopens when the Member lifts the request and the conditions are met
  (Art. 26).
- The responsible Member may amend the draft; Members are informed and a new
  time limit set if needed (Art. 24).
- The Secretary-General may postpone or bring forward the expiry date; if
  bringing it forward changes the type of written procedure, the President's
  prior agreement is needed (Art. 19(4) and (5)).
- If the language versions needed for publication or notification are not
  available before expiry, the Secretary-General extends the time limit or
  suspends the procedure (Art. 41(3)).

### 3. Empowerment procedure (Arts. 29–35)

The Commission empowers one or more of its Members to adopt acts on its
behalf and under its responsibility.

**General empowerment** (Arts. 29–34)

- **Scope:** "management or administrative acts of a routine and recurring
  nature" (Art. 29(1)). The granting decision must justify why the measures
  can be so regarded, and set subject-matter, scope, conditions and
  interservice consultation rules (Art. 30(1)).
- **Granted by:** the Commission, on a draft submitted by the President with
  the prior agreement of the Members concerned, by oral procedure or
  finalisation written procedure (Art. 29(3)).
- **Before each use** (Art. 31): the empowered Member considers whether
  political or other circumstances call for oral or written procedure, and
  consults the President in case of doubt; positive opinions of the Legal
  Service and services consulted, express or tacit; agreement of the
  empowered Member and any associated Members; verification by the
  Secretariat-General.
- **Adoption:** the act stands adopted when the Member's signature, by hand
  or electronic, is recorded in the IT system (Art. 31(6)).
- **Subdelegation** (Art. 32): to a Director-General or Head of Service,
  unless the granting decision prohibits it; notified to the
  Secretariat-General; cannot exceed the empowerment; cannot be delegated
  further, with one exception.
- **The exception** (Art. 33): certain decisions selecting projects and
  individual decisions awarding grants and procurement contracts may be
  subdelegated again to a Deputy Director-General, a Director or, with the
  agreement of the responsible Member, a Head of Unit, where the basic act
  provides for a Commission decision on its own or after a favourable
  committee opinion. These decisions are not subject to interservice
  consultation.
- **Register:** kept by the Secretariat-General (Art. 34).

**Ad hoc empowerment** (Art. 35)

- Limited in time, for one-off, specific measures whose substance the
  Commission has determined, exercised in agreement with the President.
- Typical use: finalising and adopting an act approved in principle at a
  meeting once all language versions are available.
- Requested by a Member with reasons and placed on a meeting agenda.
- Cannot be subdelegated.

### 4. Delegation procedure (Arts. 36–40)

The Commission delegates powers directly to a Director-General or Head of
Service.

- **Scope:** the same test as a general empowerment: management or
  administrative acts of a routine and recurring nature (Art. 36(1)), with
  the same content requirements for the granting decision (Art. 37(1)).
- **Before each use** (Art. 38): the delegate considers whether the act
  should go to oral or written procedure and consults the responsible Member
  in case of doubt; positive opinions of the Legal Service and services
  consulted, express or tacit.
- **Adoption:** when the delegate's signature is recorded in the IT system
  (Art. 38(4)).
- **No subdelegation** (Art. 36(5)), except for grant and contract decisions
  on the same terms as Art. 33 (Art. 39).
- **Absence:** exercised by the official designated under the deputising
  rules of Art. 52 (Art. 38(5)).
- **Register:** kept by the Secretariat-General (Art. 40).

**Limits common to empowerment and delegation:** the Commission keeps the
right to exercise the powers itself and to give instructions (Arts. 29(4) and
36(4)). Neither affects financial delegations under the Financial Regulation
or the powers of the appointing authority (Arts. 29(5) and 36(6)); those
follow their own rules.

---

## Choosing the procedure

| If the act is … | Then |
|---|---|
| Politically sensitive or important, or linked to the Commission's priorities | Oral procedure; or finalisation written procedure once agreed at Heads of Cabinet or College level |
| Not sensitive, all services and the Legal Service agree, and the responsible Member agrees | Written procedure |
| A routine, recurring management or administrative act covered by a granting decision | Empowerment or delegation, after checking the granting decision's scope and conditions |
| Agreed in substance by the College but awaiting language versions | Approval in principle with an ad hoc empowerment |
| A selection or award decision for grants or contracts, where the basic act requires a Commission decision | Subdelegation under Art. 33 or 39, if one has been given |
| Urgent | Expedited or urgent written procedure, with the President's authorisation and a justification other than administrative delay |

Where a service wants to use an empowerment or delegation for an act that
has become politically sensitive, the Rules of Procedure direct the empowered
Member or delegate to consider oral or written procedure (Arts. 31(1) and
38(1)). Advise accordingly. `[review — political judgement required]`

---

## Interservice consultation (Arts. 54–62)

It comes before any adoption procedure and its time counts in the timeline.

- **When:** once the draft is at a sufficiently advanced stage; politically
  sensitive or important drafts are first agreed by the responsible Member
  (Art. 55).
- **Who:** services with a legitimate interest (Art. 55(1)); the
  Secretariat-General in the cases listed in Art. 56; the Legal Service on
  all draft acts, staff working documents and documents that may have legal
  implications, unless it has formally agreed an exemption for recurrent acts
  (Art. 57); DG Budget where there is an impact on the budget or finances
  (Art. 58(2)); DG Human Resources and Security where staff or administration
  are affected (Art. 58(3)).
- **Time limit:** at least ten working days from availability of the
  documents (Art. 59(1)). No reaction in time counts as a positive opinion
  (Art. 59(3)).
- **Fast track** (Art. 60): in exceptional cases on duly justified grounds of
  urgency, at the request of the service responsible; the
  Secretariat-General decides and informs the President. In a meeting:
  documents at least 48 hours before, and the meeting closes the
  consultation. In writing: a time limit agreed with the Secretariat-General,
  not less than 48 hours. Not available to make up for an administrative
  delay.
- **Specific consultations** (Art. 61): for recurrent consultations, with
  rules authorised by the Secretariat-General.
- **Afterwards** (Art. 62): the service revises the draft, sends the revised
  version to those consulted and explains any comment not taken up, before
  starting the adoption procedure.
- **Committee votes:** positive opinions are required before a draft
  implementing act is put to a committee vote (Art. 62(3)).

---

## Languages (Art. 41)

A draft must be available in the language or languages stipulated by the
President for the Members, and in those required for publication in the
Official Journal or for notification to the addressees.

- Written procedure: the first set when the procedure starts, the second
  before it expires (Art. 41(3)).
- Empowerment and delegation: the act can be adopted only once the versions
  needed for publication or notification are available (Art. 41(6)).
- An act to be transmitted officially to the other institutions or published
  in the Official Journal must be available in all the official languages
  (Art. 41(7)).

Build translation and, where applicable, the Legal Service's legal-linguistic
revision into the timeline. They are the usual cause of slippage.

---

## After adoption

**Recording** (Art. 42): acts adopted by written procedure, empowerment and
delegation are recorded in day notes; acts adopted by oral procedure are
listed in the summary note drawn up at the meeting.

**Authentication** (Art. 43) of non-legislative acts adopted autonomously:

| Procedure | Authenticated by signature of | On |
|---|---|---|
| Oral | Secretary-General | the summary note |
| Written | Secretary-General | the day note |
| Empowerment | the empowered Member | the adoption sheet |
| Delegation and subdelegation | the delegate | the adoption sheet |

The authenticated text is attached to the note in the authentic languages so
that it cannot be separated from it (Art. 43(3)).

**Signature** within the meaning of TFEU Art. 297(2) (Art. 44):
regulations, directives and decisions without addressee adopted by oral or
written procedure are deemed signed by the President on signature of the
summary note; decisions with addressees are deemed signed by the responsible
Member when the Secretary-General authenticates; for empowerment and
delegation, signature is delegated to the person who adopts.

**Publication or notification** (TFEU Art. 297(2)): non-legislative
regulations, directives addressed to all Member States and decisions that
specify no addressee are published in the Official Journal and enter into
force on the date they specify or, failing that, on the twentieth day after
publication. Other directives and decisions that specify an addressee are
notified and take effect on notification. The Secretary-General sees to
notification, publication and transmission to the other institutions and
national parliaments (Art. 50(4)).

**Corrections.** The text adopted is the text authenticated. After adoption
it may not be altered, apart from corrections of spelling and grammar (Case
C-137/92 P Commission v BASF and Others). An obvious material error is
handled by a corrigendum; a change of substance needs a new act adopted by
the procedure that applied to the original. `[CJEU — verify Curia reference]`
`[model knowledge — verify the current corrigendum instructions]`

---

## Procedure sheet

```
PROCEDURE SHEET                                         [date, reference]

Act:               [title, type, legal basis, addressees if any]
Service / Member:  [lead DG; responsible Member; associated Members]
Target date:       [adoption / publication / entry into force]

1. Procedure
   [Recommended procedure and variant — article of the Rules of Procedure.
   Why this one. Alternatives considered and why they are closed or riskier.]

2. Power to adopt
   [College / empowered Member / Director-General / subdelegate.
   If empowerment or delegation: reference of the granting decision, the
   clause covering this act, and each condition with its status.]

3. Preconditions
   | Condition | Rule | Status |
   | Agreement of responsible and associated Members | Art. 18(1) / 31(3) | |
   | Interservice consultation closed | Arts. 55–62 | |
   | Positive opinion of the Legal Service | Art. 18(2) / 31(2) / 38(2) | |
   | Secretariat-General and other mandatory consultations | Arts. 56, 58 | |
   | Language versions for Members | Art. 41(1)(a) | |
   | Language versions for publication or notification | Art. 41(1)(b) | |
   | President's authorisation, if expedited, urgent or finalisation | Arts. 20–22 | |

4. Timeline (working days, counted back from the target date)
   | Step | Minimum duration | Latest start |

5. Adoption and after
   [Who adopts and how; authentication; signature; notification or
   publication; date of entry into force or effect.]

6. Risks and points for decision
   [What could delay or invalidate; what needs a political decision.]
```

When counting, use working days and the Commission's calendar of holidays.
State each minimum as the Rules give it ("no less than five working days")
and add the practical margin separately, so the reader can see which part is
a rule and which is prudence. Practical margins are
`[model knowledge — verify with the Secretariat-General's current instructions]`.

---

## Constraints

### MUST DO
- Cite the article of the Rules of Procedure for every condition and time limit, and quote it where the answer turns on its wording.
- Read the granting decision before confirming that an empowerment or delegation covers an act. The test is the decision's own scope and conditions.
- Count time in working days and show the calculation.
- Say which steps need the President's authorisation, because the service cannot assume it.
- Separate what the Rules require from what is practice or prudence.
- Refer questions on the legality of the act itself to the Legal Service (Arts. 53 and 57).

### MUST NOT DO
- Recommend an expedited or urgent written procedure, or a fast-track consultation, to recover an administrative delay. Arts. 20, 21 and 60 exclude that ground.
- Treat an empowerment or delegation as covering an act that is not a routine, recurring management or administrative act.
- Accept a subdelegation chain longer than the Rules allow: one level, plus the grant and contract exception in Arts. 33 and 39; none for an ad hoc empowerment.
- Count a tacit positive opinion before the consultation period has expired.
- Suggest changing a text after adoption other than through a corrigendum or a new act.
- Rely on the 2000 Rules of Procedure or the 2010 implementing rules. Decision 2024/3080 replaced them.

---

## Key Legal Framework

| Instrument | Subject |
|---|---|
| TEU Art. 17(6); TFEU Arts. 249 and 250 | President's organisation of the Commission; Rules of Procedure; decisions by a majority of Members |
| Commission Decision (EU) 2024/3080 | Rules of Procedure of the Commission |
| TFEU Arts. 288, 296, 297 | Types of act; reasons; signature, publication, notification, entry into force |
| TFEU Art. 263 | Grounds for annulment, including lack of competence and infringement of an essential procedural requirement |
| Case 5/85 AKZO Chemie v Commission | Delegation of authority and collegiality |
| Case C-137/92 P Commission v BASF and Others | Collegiality, authentication, no alteration after adoption |
| Case C-191/95 Commission v Germany | Collegiality in infringement decisions |
| Regulation (EU, Euratom) 2024/2509 | Financial delegations, outside the Rules of Procedure |

`[EUR-Lex — verify current version]` `[CJEU — verify Curia reference]`

---
DRAFT — For review by an EU official before use. Not an official Commission position.
