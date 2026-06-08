# Using the EU Skills Plugins — Beginner's Guide

This guide is for European Commission staff (or people learning EU institutional
work) who want to use the skill plugins in this repository. No technical
background is needed. You do not need to understand how AI works.

---

## What this system is

Each **skill** in this repository is a specialist assistant trained to do one
specific job that a Commission official does: draft a legislative text, calculate
a dumping margin, write a CDR objective, respond to a Parliamentary Question.

The skills know EU law, Commission procedures, and the specific formats those
documents take. They produce structured first drafts — faster than starting
from a blank page — with built-in reminders about what needs human review
before anything is used officially.

**Important: every output is a draft.** The system never produces a final
document. It produces a structured starting point for a human official to
review, correct, and take responsibility for. This is by design.

---

## The six skill packages

| Package | Who it is for | What it covers |
|---|---|---|
| **legislative-eu** | Policy officers, legislative drafters, SecGen lawyers | Briefing notes, regulations, ISC contributions, PQ responses, trilogue, impact assessment, consultation, REFIT |
| **competition-eu** | DG COMP lawyers, Legal Service lawyers | Antitrust analysis, state aid (four-limb test, GBER, compatibility), legal opinions, market definition |
| **institutional-management-eu** | Heads of Unit, assistants, HR officers, financial officers | CDR appraisals, ARES workflow, ABAC, contracts, pensions |
| **trade-eu** | DG TRADE investigators | Anti-dumping/anti-subsidy investigations, dumping margins, injury analysis |
| **grants-enforcement-eu** | Grant managers, infringement officers, procurement officers | Horizon Europe grants, Letters of Formal Notice, transposition tracking, infringement assessment |
| **data-communication-eu** | Data analysts, communication officers | Eurostat data notes, press releases, speeches, lines to take |

Each package lives under `plugins/<package-name>/` in the repository. EU
institutional knowledge (Commissioner personas, DG profiles, institutions) is
under `knowledge/`. Shared hook scripts are under `lib/hooks/`.

---

## How a session works

Every session has the same three steps:

```
1. Install the right package
2. Run the cold-start interview (2 minutes)
3. Use the skill
```

That is all. The rest of this guide explains each step with a concrete example.

---

## Core concepts you need to know

### Two types of skill: roles and workflow tools

Skills come in two flavours:

**Role skills** are broad personas — they cover a job function. `/eu-legislative:policy-officer`
can draft a briefing note, a negotiating brief, or an ISC contribution. They are
good for open-ended work where you are not sure of the exact output format.

**Workflow skills** are narrow task tools — they produce one specific output
following a defined procedure. `/eu-legislative:impact-assessment` produces a SWD following the
Better Regulation methodology. `/eu-legislative:treaty-check` produces a legal opinion on legal
basis, subsidiarity, proportionality, and Charter rights. `/eu-grants-enforcement:infringement` produces
a structured Art. 258 TFEU case assessment. They are good when you know exactly
what document you need.

When in doubt: start with the role skill, then switch to the workflow skill once
you know what output you need.

### Skills are specialists, not generalists

Each skill knows one domain deeply. `/eu-competition:lawyer-legal-service` knows CJEU litigation
and treaty interpretation. `/eu-legislative:pq-responder` knows how to draft a Parliamentary
Question response. They do not know each other's domains.

If your task crosses domains — for example, a legal opinion that requires
statistical data — use two skills in sequence: first `/eu-data-communication:data-analyst` to get the
data note, then `/eu-competition:lawyer-legal-service` to draft the opinion using that data.

### The cold-start interview personalises the output

Before you use any skill, you run the cold-start interview for your plugin (e.g. `/eu-competition:cold-start-interview`). It asks you 6–7
questions: which DG you are in, what your current dossier is, what language
you need, how sensitive the work is. The answers go into the package's practice
profile and shape every output you get in that session.

Without the cold-start interview, the skill will still work, but the outputs
will use generic defaults instead of your specific context.

### Trust tags tell you what to verify

Every output contains inline tags. These are not decoration — they are
instructions. They tell you exactly which parts of the output you need to check
before using it.

| Tag | What it means | What you should do |
|---|---|---|
| `[EUR-Lex — verify current version]` | The cited regulation or directive text came from training data, not a live retrieval | Open EUR-Lex and confirm the article still reads as quoted |
| `[CJEU — verify Curia reference]` | A case name and number were cited from training data | Check the case exists and the citation is accurate on curia.europa.eu |
| `[model knowledge — verify]` | A figure, date, or fact was generated from training data | Cross-check against the primary source before using |
| `[review — legal uncertainty]` | The law on this point is unsettled or contested | Get a second opinion; consider Legal Service consultation |
| `[review — political judgement required]` | This is a policy call, not a legal deduction | A human official needs to make this decision |
| `[review — cleared lines required]` | This communication has not been through the clearance chain | Do not send externally until cleared |

### Every output ends with a DRAFT notice

```
---
DRAFT — For review by an EU official before use. Not an official Commission position.
```

This is not a formality. It is a reminder that the document has legal and
institutional consequences only when a human official takes responsibility for it.

---

## Step-by-step example: responding to a personal data request

### The scenario

You are a legal officer at **DG GROW** (Internal Market, Industry,
Entrepreneurship and SMEs). A staff member from another DG — DG EMPL — has
submitted a formal **Subject Access Request** under **Regulation (EU) 2018/1725**
(the data protection regulation for EU institutions, equivalent to the GDPR).

The request asks:
> "I request access to all personal data held about me by DG GROW, including
> data relating to a procurement evaluation in which I participated as an
> external evaluator in 2023."

You need to draft DG GROW's formal reply.

The reply must:
- Identify what data is held
- Apply the access rights under Regulation 2018/1725 (Art. 17)
- Note any exceptions that may apply (Art. 25 — limitations on access rights)
- Be sent within **one month** (Art. 12(3) of Regulation 2018/1725)
- Be cleared by DG GROW's Data Protection Officer (DPO) before sending

---

### Step 1: Install the right package

This task is legal work — drafting a formal reply based on a specific legal
framework (Regulation 2018/1725). The right package is **`competition-eu`**
because it contains the `lawyer-legal-service` skill, which handles legal
analysis and formal legal documents.

In Claude Code:

```
/plugin marketplace add montoyer/eu-agents
/plugin install competition-eu@eu-agents
```

---

### Step 2: Run the cold-start interview

```
/eu-competition:cold-start-interview
```

The interview will ask you several questions. Here is how to answer them for
this scenario:

> **"Which DG and unit are you in?"**
> DG GROW — Legal Affairs unit

> **"What type of work are you doing?"**
> Legal analysis and drafting — not a competition case; a data protection
> response under Regulation 2018/1725

> **"What is the case reference or dossier name?"**
> Subject Access Request from [DG EMPL staff member] — received [date]

> **"What stage is the case or opinion at?"**
> Initial assessment — need to draft the formal reply

> **"What is the confidentiality level?"**
> NORMALE for the reply itself; the underlying personal data is sensitive

> **"What language do you need?"**
> English

The interview writes these answers into the package's practice profile. Every
output in this session will be calibrated to: DG GROW, data protection reply,
Regulation 2018/1725.

---

### Step 3: Use the skill

You now invoke the `lawyer-legal-service` skill with your specific request:

```
/eu-competition:lawyer-legal-service

A staff member from DG EMPL has submitted a Subject Access Request under
Regulation (EU) 2018/1725. They are requesting access to all personal data
held by DG GROW relating to their participation as an external evaluator in
a 2023 procurement procedure.

I need:
1. A legal assessment of our obligations under Regulation 2018/1725
2. An identification of what categories of data are likely held
3. A draft formal reply to the data subject
4. A note on any applicable exceptions (Art. 25) and whether they apply here
```

---

### Step 4: Read the output

The skill produces a structured output. Here is what a realistic output looks like:

---

```
LEGAL ASSESSMENT — SUBJECT ACCESS REQUEST
Regulation (EU) 2018/1725 of the European Parliament and of the Council
[EUR-Lex — verify current version: OJ L 295, 21.11.2018, p. 39]

DG / Unit:    DG GROW — Legal Affairs
Request type: Subject Access Request — Art. 17 Regulation 2018/1725
Deadline:     One month from receipt (Art. 12(3)) — extendable to three months
              for complex or numerous requests (Art. 12(4))
DPO consultation: Required before sending — flag to DPO immediately

─────────────────────────────────────────────────────────
I. LEGAL OBLIGATIONS UNDER REGULATION 2018/1725
─────────────────────────────────────────────────────────

Article 17 of Regulation 2018/1725 [EUR-Lex — verify current version] gives the
data subject the right to obtain from the controller:

(a) confirmation of whether personal data concerning them is being processed;
(b) access to that personal data; and
(c) the information listed in Art. 17(2): the purpose of processing, the
    categories of data, the recipients or categories of recipient, the
    retention period, the existence of the rights to rectification, erasure,
    and restriction, and the right to lodge a complaint with the EDPS.

DG GROW is the controller for data processed in connection with procurement
procedures it conducts. The data subject has a right of access to their
personal data held in that capacity.

─────────────────────────────────────────────────────────
II. CATEGORIES OF DATA LIKELY HELD
─────────────────────────────────────────────────────────

For an external evaluator in a 2023 procurement procedure, DG GROW is likely
to hold the following categories of personal data:

1. Identity data: name, institutional affiliation, contact details
   (provided on registration as evaluator)

2. Conflict of interest declaration: signed declaration submitted before
   evaluation — this document contains personal data and is subject to
   the access right

3. Evaluation scores and individual comments: scores given by the evaluator
   on individual tender criteria — [review — legal uncertainty: see Section III]

4. Attendance and participation records: dates, meeting records

5. Correspondence: emails or formal communications with the evaluator

6. Contractual documents: if the evaluator was remunerated, any contract
   or reimbursement claim will contain financial personal data

─────────────────────────────────────────────────────────
III. APPLICABLE EXCEPTION — ART. 25(1)(c): PROTECTION OF OTHERS' DATA
─────────────────────────────────────────────────────────

[review — legal uncertainty: this is the central legal question in this request]

Article 25(1)(c) of Regulation 2018/1725 [EUR-Lex — verify current version]
permits restriction of the access right where it is necessary to protect
"the rights and freedoms of others."

EVALUATION SCORES AND COMMENTS: The evaluation report will typically contain
the scores and comments of all evaluators collectively. Disclosing the individual
scores of the requesting evaluator may also reveal, or allow inference about,
the scores of other evaluators, thereby disclosing their personal data.

Assessment: DG GROW may restrict access to the collective evaluation report
under Art. 25(1)(c) if disclosure would reveal the individual assessments of
other evaluators. However, DG GROW should provide access to the requesting
evaluator's own scores and comments (those attributable solely to them) where
these can be separated.

[review — legal uncertainty: the EDPS has issued guidance on this balance;
consult DPO and check EDPS Decision on access to evaluation documents
[model knowledge — verify against current EDPS guidance]]

OTHER CATEGORIES: No exception appears to apply to identity data, conflict of
interest declarations, attendance records, and correspondence. These should
be disclosed in full.

─────────────────────────────────────────────────────────
IV. DRAFT FORMAL REPLY
─────────────────────────────────────────────────────────

[DG GROW letterhead]
[Reference: ARES(20XX)XXXXXXX]
[Classification: NORMALE]

[City], [DD Month YYYY]

Subject: Reply to your Subject Access Request under Regulation (EU) 2018/1725

Dear [Name],

DG GROW acknowledges receipt of your Subject Access Request dated [date],
received on [date of receipt]. This reply is provided in accordance with
Article 17 of Regulation (EU) 2018/1725 [EUR-Lex — verify current version].

1. PERSONAL DATA HELD BY DG GROW

DG GROW has identified the following categories of personal data held in
connection with your participation as an external evaluator in procurement
procedure [reference / description], conducted in [year]:

  — Your name, institutional affiliation, and contact details, as provided
    at registration;
  — Your signed conflict of interest declaration dated [date];
  — Records of your attendance and participation in the evaluation sessions
    on [dates];
  — Your individual evaluation scores and written comments on the tenders
    evaluated, to the extent these are separately identifiable as your own;
  — Correspondence exchanged between you and DG GROW in connection with
    the procedure.

Copies of these documents are enclosed / available upon request [choose].

2. PARTIAL RESTRICTION UNDER ARTICLE 25(1)(c)

Access to [the full collective evaluation report / specific document] is
partially restricted under Article 25(1)(c) of Regulation (EU) 2018/1725,
as disclosure of [specify the specific parts] would reveal personal data
of other evaluators who participated in the same procedure.

DG GROW has provided you with the portions of the evaluation documentation
that contain exclusively your own assessments. The restricted portions
relate solely to the assessments of other individuals and do not affect
your right of access to your own data.

3. YOUR FURTHER RIGHTS

You have the right to:
  — Request rectification of inaccurate personal data (Art. 18);
  — Request erasure of data no longer necessary (Art. 19);
  — Lodge a complaint with the European Data Protection Supervisor (EDPS)
    at edps.europa.eu if you consider that the processing of your personal
    data does not comply with Regulation 2018/1725.

4. CONTACT

For any questions regarding this reply or the processing of your personal data
by DG GROW, please contact: [DG GROW DPO contact details].

Yours sincerely,

[Name]
[Title]
DG GROW — [Unit]
On behalf of the Data Controller

─────────────────────────────────────────────────────────
V. ACTIONS BEFORE SENDING
─────────────────────────────────────────────────────────

□ DPO consultation — mandatory before sending; DPO must confirm the Art. 25
  restriction is correctly applied [review — DPO clearance required]
□ Attach or make available the identified data (see Section I categories)
□ Redact other evaluators' data from any shared documents before enclosing
□ Record the reply in ARES with ARES reference
□ Note the one-month deadline: reply must be sent by [calculate date]

[EUR-Lex — verify current version of Regulation 2018/1725]
[model knowledge — verify: check current EDPS guidance on access to
evaluation documents and any relevant EDPS decisions on Art. 25(1)(c)]
[review — legal uncertainty: the partial restriction analysis should be
confirmed with DPO before relying on it]

---
DRAFT — For review by DG GROW's DPO and the responsible legal officer before
sending to the data subject. Not an official Commission position.
```

---

### Step 5: What to do with the output

The skill has produced:
- A legal analysis of your obligations (Section I)
- A list of the data categories you are likely holding (Section II)
- An analysis of whether an exception applies and why (Section III)
- A complete draft reply ready to populate with the real details (Section IV)
- A pre-send checklist (Section V)

**Your work now is:**

1. **Fill in the placeholders** in the draft reply — `[date]`, `[reference]`,
   `[DG GROW DPO contact]`, and so on

2. **Check the trust tags:**
   - `[EUR-Lex — verify current version]` appears on the Regulation citation.
     Open EUR-Lex and confirm Regulation 2018/1725 still contains the articles
     as described. Regulations can be amended.
   - `[model knowledge — verify]` appears on the EDPS guidance reference.
     Search the EDPS website for any decisions or guidance on Art. 25(1)(c)
     and evaluation documents.
   - `[review — legal uncertainty]` appears on the partial restriction analysis.
     This is the hardest legal question in the file. Do not rely on the draft
     analysis without the DPO's view.

3. **Send the draft to your DPO** — the DPO's clearance is flagged as
   mandatory in the output. Do not send the reply to the data subject without it.

4. **Register in ARES** — the draft reminds you to register the reply with an
   ARES reference.

---

---

## Second example: using a workflow skill directly

The previous example used a role skill (`/eu-competition:lawyer-legal-service`). This example
shows how a **workflow skill** works differently — it follows a fixed procedure
and always produces the same output structure, regardless of what you ask.

### The scenario

You are a policy officer at DG ENV preparing the Better Regulation package for
a new directive on industrial water reuse. The proposal is at the options-analysis
stage and you need to produce the impact assessment SWD.

### Using `/eu-legislative:impact-assessment` directly

Workflow skills do not need a long prompt — they run a defined procedure on
whatever brief you give them:

```
/eu-legislative:impact-assessment

Policy brief: The Commission is considering a directive requiring industrial
operators with water discharge above 10,000 m³/year to implement closed-loop
water recycling systems. The objective is to reduce industrial freshwater
abstraction by 30% by 2035 in water-stressed regions (currently affecting 11
member states). The legal basis is proposed as Art. 192 TFEU (environment).
```

The skill will run all eight workflow steps automatically:

1. Problem definition + subsidiarity
2. Baseline (business as usual)
3. Objectives (general/specific/operational)
4. Policy options (Option 0 → Option 3+)
5. Impact analysis — economic, social, environmental for each option
6. Comparison matrix
7. Preferred option with proportionality statement
8. Monitoring framework

You do not need to ask for each step separately. The output will be the full
SWD structure, with trust tags on every data figure and a pre-submission
quality checklist at the end.

### When to use `/eu-legislative:impact-assessment` vs `/eu-legislative:impact-assessment-analyst`

| | `/eu-legislative:impact-assessment` | `/eu-legislative:impact-assessment-analyst` |
|---|---|---|
| Type | Workflow — fixed procedure | Role — open-ended |
| Output | Always: full SWD structure | Depends on what you ask |
| Best for | When you need the complete document | When you need analysis of one step (e.g., just the SME test, just the comparison matrix) |

---

## Other tasks you can do with the same package

Once your cold-start interview has set the competition-eu context, you can
continue the same session with related tasks without re-interviewing:

```
/eu-competition:lawyer-legal-service

The data subject has now replied to our letter asking for clarification on
why the collective evaluation report was partially withheld. They are
threatening to file a complaint with the EDPS. Draft a holding response and
assess whether we should proactively share more of the evaluation report.
```

Or:

```
/eu-competition:lawyer-legal-service

Separately, DG GROW's DPO has asked whether the retention period for external
evaluator data is correctly set. Currently we retain the data for 5 years after
the procedure. Is this consistent with Regulation 2018/1725 and the applicable
procurement record-keeping rules?
```

The skill will handle follow-up questions within the same session, building
on the context already set.

---

## Common mistakes and how to avoid them

### "I skipped the cold-start interview"

You can. The skill will still produce an output. But it will not know your DG,
your specific document, or your sensitivity level. The output will be more
generic and will need more editing. Run the interview — it takes two minutes
and saves much more time in editing.

### "The output said something I know is wrong"

This is why trust tags exist. The skill drew on training data that may be
outdated. Any citation tagged `[EUR-Lex — verify]` or `[model knowledge — verify]`
must be checked against the live source. The skill gives you the structure and
the legal reasoning; you verify the specific provisions.

### "The skill answered a slightly different question"

Rephrase your request more specifically. Skills respond to what you ask.
If you want a formal reply letter and not a legal analysis, say "draft the
formal reply letter" not "help me with this data request." The more specific
your instruction, the more targeted the output.

### "The skill used GDPR terminology, not Regulation 2018/1725"

EU institutions are not governed by GDPR (Regulation 2016/679). They are governed
by **Regulation (EU) 2018/1725**, which is the institutions-specific equivalent.
If the output uses GDPR instead of Regulation 2018/1725, correct it explicitly:

```
Note: the applicable regulation is Regulation (EU) 2018/1725, not GDPR
(Regulation 2016/679). GDPR applies to member state authorities; Regulation
2018/1725 applies to EU institutions. Please revise the analysis accordingly.
```

### "I don't know which package to use"

Use this quick-decision question: *What kind of official would normally do this task?*

- A DG COMP or Legal Service lawyer → `competition-eu`
- A policy officer working on a legislative file → `legislative-eu`
- A Head of Unit or HR officer → `institutional-management-eu`
- A DG TRADE investigator → `trade-eu`
- A grant manager or infringement officer → `grants-enforcement-eu`
- A data analyst or press officer → `data-communication-eu`

If in doubt, `legislative-eu` with `policy-officer` is the closest to a generalist
Commission policy function.

---

## Complete skill reference

All 97 skills across 9 plugins. Install a plugin with `/plugin install <plugin-name>@eu-agents`.

### `legislative-eu` — Legislative & Policy

| Skill | Description |
|---|---|
| `/eu-legislative:policy-officer` | Briefing notes, negotiating briefs, ISC contributions, options papers |
| `/eu-legislative:legislative-drafter` | Draft EU regulations, directives, and decisions to Joint Practical Guide standards |
| `/eu-legislative:lawyer-secgen` | ISC legal quality review, subsidiarity and proportionality analysis |
| `/eu-legislative:comitology-officer` | Delegated and implementing acts, committee procedures, EP objections |
| `/eu-legislative:impact-assessment-analyst` | Better Regulation impact assessments — problem definition, CBA, SME test |
| `/eu-legislative:economist` | Economic analysis, market failure assessment, European Semester data |
| `/eu-legislative:isc-contributor` | Draft ISC contributions — Agreement, Reservations, or Opposition with textual amendments |
| `/eu-legislative:pq-responder` | Draft EP Parliamentary Question responses (Rules 138 and 139) with clearance tracking |
| `/eu-legislative:subsidiarity-checker` | Run Art. 5(3)–(4) TEU subsidiarity and proportionality test with Protocol No. 2 risk |
| `/eu-legislative:trilogue-position-tracker` | Maintain four-column document, track positions, draft pre-round mandate briefs |
| `/eu-legislative:impact-assessment` | Full SWD impact assessment — problem definition, options, CBA, SME test, DNSH, comparison matrix |
| `/eu-legislative:legislative-proposal` | Draft complete EU regulation or directive — legal basis, recitals, operative articles, EM |
| `/eu-legislative:treaty-check` | Legal basis, subsidiarity, proportionality, and Charter rights review — mirrors CLS check |
| `/eu-legislative:better-regulation` | REFIT regulatory fitness check — five criteria, overall score, simplification opportunities |
| `/eu-legislative:consultation` | Simulate or draft a 12-week public consultation — stakeholder positions, synthesis, Commission response |
| `/eu-legislative:delegated-acts-drafter` | Art. 290 TFEU delegated acts — enabling clause check, DA vs IA classification, scrutiny period, draft act |
| `/eu-legislative:fundamental-rights-assessor` | Charter of Fundamental Rights full assessment — Art. 51 scope, Art. 52(1) limitation test, all 54 articles |
| `/eu-legislative:regulatory-impact-quantifier` | CBA/CEA quantification — compliance costs, SME test, OIOO, benefit monetisation, RSB-ready tables |
| `/eu-legislative:policy-cycle` | Full EU policy lifecycle — agenda-setting through evaluation, all 7 phases, Better Regulation methodology |

### `competition-eu` — Competition & Legal Service

| Skill | Description |
|---|---|
| `/eu-competition:lawyer-competition-antitrust` | Arts. 101–102 TFEU analysis, SO drafting, fines calculation, dawn raids |
| `/eu-competition:lawyer-state-aid` | Art. 107–109 TFEU four-limb test, GBER screening, recovery calculation |
| `/eu-competition:lawyer-legal-service` | CLS legal opinions, litigation management, Written Observations, risk assessment |
| `/eu-competition:gber-screener` | Screen a measure against GBER categories — all conditions, incentive effect, cumulation |
| `/eu-competition:market-definer` | Apply SSNIP test, define relevant product and geographic market for Art. 101/102/merger |
| `/eu-competition:state-aid-review` | Art. 107(1) four-limb test, de minimis, GBER screening, compatibility assessment workflow |
| `/eu-competition:merger-screener` | EU Merger Regulation — SIEC test, jurisdictional thresholds, Phase I/II, remedies design |
| `/eu-competition:dawn-raid-advisor` | Competition inspection defence — LPP claims, employee rights, document log, post-inspection obligations |
| `/eu-competition:eu-liability-advisor` | Art. 340(2) TFEU non-contractual liability — Bergaderm three-limb test, damage assessment, MS Francovich liability |

### `simulation-eu` — EU Institutional Simulation

| Skill | Description |
|---|---|
| `/eu-simulation:commissioner` | Invoke any of 21 Commissioner personas — speaks from treaty mandate, priorities, tensions |
| `/eu-simulation:college-deliberation` | Full College of Commissioners meeting — all 21 speak, President calls vote, outcome recorded |
| `/eu-simulation:inter-service-consultation` | ISC round — lead DG circulates, all affected DGs respond, synthesis note produced |
| `/eu-simulation:trilogue` | Inter-institutional trilogue — EP/Council/Commission negotiate via four-column document |
| `/eu-simulation:legislative-cycle` | Full OLP from Commission initiative to OJ publication — chains all six phases |
| `/eu-simulation:european-parliament` | EP counter-party agent — committee, rapporteur, group dynamics, amendments, plenary vote |
| `/eu-simulation:council-eu` | Council counter-party agent — configuration, QMV arithmetic, general approach, Presidency mandate |
| `/eu-simulation:advocate-general` | AG Opinion simulation — legal question analysis, party arguments, proposed ruling, Art. 252 TFEU independence |
| `/eu-simulation:council-presidency` | Council Presidency chair — compromise texts, non-papers, QMV tracking, general approach, trilogue mandate |
| `/eu-simulation:mandate-conflict` | Conflict map across all 21 Commissioner portfolios — structurally guaranteed mandate clashes with treaty basis and severity rating |
| `/eu-simulation:red-team-college` | Token-efficient College stress test — runs all 21 Commissioners, returns only SEVERE objections and adoptability verdict |
| `/eu-simulation:subsidiarity-stress` | Tests subsidiarity justification against 5 member-state configurations — finds where necessity argument fails and assesses yellow card risk |
| `/eu-simulation:timeline` | OLP timeline with blocking dependencies, QMV arithmetic, and trilogue risk points |

### `privacy-eu` — Data Protection & Privacy

| Skill | Description |
|---|---|
| `/eu-privacy:dpia` | Full DPIA under Art. 39 EUDPR — multi-agent: DPO, IT-PM, IT Security, Legal Officer, EDPS prior-consultation determination |
| `/eu-privacy:dpo` | DPO persona — Art. 39 threshold screening, risk sign-off, register of processing activities, Art. 40 referral decision |
| `/eu-privacy:it-project-manager` | IT Project Manager — system architecture, data flows, third-party processors, ROPA record, retention schedule |
| `/eu-privacy:it-security` | IT Security Officer — CIA threat model, TIA for non-EU cloud/AI providers, security measures, residual risk rating |
| `/eu-privacy:legal-officer` | Legal Officer — legal basis Art. 5(1) EUDPR, necessity, proportionality, special categories, retention justification |
| `/eu-privacy:it-security-plan` | IT Security Plans Expert — ISP drafting, ISO 27001/CIS Controls mapping, risk register, incident response, NIS2 compliance |
| `/eu-privacy:data-breach-officer` | Data Breach Response — breach assessment, 72-hour EDPS notification (Art. 34 EUDPR), data subject communication, breach register |
| `/eu-privacy:ropa-drafter` | RoPA Drafter — Art. 31 EUDPR Record of Processing Activities, legal basis, retention schedule, processor register |
| `/eu-privacy:ai-act-officer` | AI Act Compliance — risk tier classification, prohibited practice check, FRIA (Art. 27), technical documentation, conformity assessment |
| `/eu-privacy:tia-expert` | Transfer Impact Assessment — full TIA for third-country transfers, adequacy decisions, SCCs, supplementary measures, Schrems II |
| `/eu-privacy:retention-schedule` | Retention Schedule — Art. 25 EUDPR storage limitation, retention matrix, sectoral obligations, archiving rules, deletion procedures |
| `/eu-privacy:privacy-notice-drafter` | Privacy Notice Drafter — Arts. 15–16 EUDPR compliant notices, plain language, layered notices, mandatory content checklist |
| `/eu-privacy:data-subject-rights` | Data Subject Rights — access, rectification, erasure, restriction, portability, objection — deadlines, exemptions, refusal letters |
| `/eu-privacy:edps-complaint-handler` | EDPS Complaint Handler — Art. 57/58 EUDPR supervisory inquiry response, contradictory procedure, remedial action plan |
| `/eu-privacy:ai-governance-officer` | AI Governance Officer — AI system register, model cards, governance board ToR, human oversight, AI procurement clauses |

### `institutional-management-eu` — Institutional Management

| Skill | Description |
|---|---|
| `/eu-institutional-management:head-of-unit` | Unit management, CDR, work programme, staff decisions, AMP |
| `/eu-institutional-management:deputy-head-of-unit` | Operational coordination, quality review, deadline tracking, A.I. acting |
| `/eu-institutional-management:assistant-hod` | ARES management, MIPS/C2 missions, SYSPER, PQ tracking, action trackers |
| `/eu-institutional-management:hr-contract-manager-ta` | TA/CA contract management, CEOS, CAST, recruitment, renewal decisions |
| `/eu-institutional-management:financial-officer` | ABAC financial circuit, FR 2018/1046, commitment and payment orders |
| `/eu-institutional-management:pmo-pension-specialist` | Annex VIII pension calculations, PMO entitlements, pension projections |
| `/eu-institutional-management:cdr-drafter` | Draft SMART CDR objectives, end-year appraisals, and competency assessments in SYSPER |
| `/eu-institutional-management:amp-drafter` | Annual Management Plan — unit objectives, KPIs, deliverables, resource mapping, risk section, COO cycle |
| `/eu-institutional-management:aar-drafter` | Annual Activity Report — objective assessment, resource use, internal control, HoU management assurance |
| `/eu-institutional-management:selection-board` | Selection procedure — vacancy notice, shortlisting, competency-based interview grid, selection board report |
| `/eu-institutional-management:access-to-documents` | Regulation 1049/2001 access requests — exception assessment, partial access, refusal letters, confirmatory procedure |
| `/eu-institutional-management:underperformance-advisor` | Art. 51 SR underperformance procedure — warning letter, improvement plan, monitoring, JEC submission |
| `/eu-institutional-management:budget-planner` | Budget planning and execution — CA/PA programming, virements, carry-overs, execution monitoring, AAR reporting |

### `grants-enforcement-eu` — Grants, Procurement & Enforcement

| Skill | Description |
|---|---|
| `/eu-grants-enforcement:grant-manager` | Horizon Europe MGA management, payment assessment, financial corrections |
| `/eu-grants-enforcement:infringement-officer` | Arts. 258–260 TFEU procedure — EU Pilot, LFN, RO, CJEU referral, Art. 260 penalties |
| `/eu-grants-enforcement:procurement-expert` | FR 2018/1046 procurement — framework contracts, tender evaluation, award decisions |
| `/eu-grants-enforcement:lfn-drafter` | Draft Art. 258 TFEU Letters of Formal Notice — non-transposition, incorrect transposition, misapplication |
| `/eu-grants-enforcement:transposition-tracker` | Track and assess directive transposition across 27 MS — status table, conformity, escalation |
| `/eu-grants-enforcement:infringement` | Art. 258–260 TFEU infringement assessment — type classification, procedural stage, penalty estimate |
| `/eu-grants-enforcement:reasoned-opinion-drafter` | Art. 258(2) TFEU Reasoned Opinion — rebuttal of member state observations, maintained allegations, RO drafting |
| `/eu-grants-enforcement:grant-audit-advisor` | Grant audit preparation and response — ECA/IAS on-the-spot checks, contradictory procedure, rebuttal notes |
| `/eu-grants-enforcement:grant-amendment-officer` | Grant agreement amendments — budget reallocation, partner withdrawal, period extension, force majeure |
| `/eu-grants-enforcement:tender-evaluator` | Tender evaluation — exclusion/selection/award criteria scoring, ALT assessment, evaluation report, debrief letters |
| `/eu-grants-enforcement:olaf-referral-advisor` | OLAF referral — fraud indicators, Art. 8 Reg. 883/2013 notification, payment suspension, parallel procedure rules |
| `/eu-grants-enforcement:direct-award-advisor` | Direct award justification — urgency, sole source, follow-on services, FR Art. 164 exception assessment |
| `/eu-grants-enforcement:eppo-jurisdiction-advisor` | EPPO jurisdiction — PIF offences, Reg. 2017/1939, OLAF-EPPO referral, parallel administrative procedure management |
| `/eu-grants-enforcement:cohesion-fund-manager` | Cohesion funds shared management — CPR 2021/1060, financial corrections, n+3 decommitment, closure, audit response |

### `data-communication-eu` — Data & Communication

| Skill | Description |
|---|---|
| `/eu-data-communication:data-analyst` | Eurostat data extraction, indicator design, scoreboards, data notes, visualisation |
| `/eu-data-communication:communication-officer` | Press releases, lines to take, Commissioner speeches, social media, briefings |
| `/eu-data-communication:lines-to-take-drafter` | Draft complete LTT packages — friendly/neutral/hostile Q&A, no-go zones, background facts, clearance tracking |
| `/eu-data-communication:digit-project-manager` | DIGIT IT project governance: Agile delivery, OCS gates, ITSRM² risk, EU Cloud, vendor management, steering-committee reporting |
| `/eu-data-communication:data-steward` | Data governance, metadata (DCAT-AP, ISA², SEMIC), open data publication, data quality, data spaces, Data Governance Act |
| `/eu-data-communication:cybersecurity-officer` | Cybersecurity risk (ITSRM²), NIS2 compliance, incident response, CERT-EU coordination, security accreditation, vulnerability management |
| `/eu-data-communication:transparency-officer` | Access to documents (Reg. 1049/2001), GESTDEM, confirmatory applications, exception analysis, Transparency Register, Ombudsman |

### `trade-eu` — Trade Defence

| Skill | Description |
|---|---|
| `/eu-trade:trade-defence-investigator` | AD/CVD/safeguard investigations — margins, injury, NOI, questionnaires, OSV |
| `/eu-trade:dumping-margin-calculator` | Dumping margin calculation — normal value, export price, Art. 2(10) adjustments, WA-WA, LDR |
| `/eu-trade:sanctions-screener` | EU restrictive measures screening — consolidated list, asset freeze, sectoral sanctions, derogation procedure |

### `careers-eu` — EU Careers & EPSO Preparation

| Skill | Description |
|---|---|
| `/eu-careers:epso-grade` | Estimate entry grade, step, and net monthly salary for a given competition type and candidate profile under SR Annex I |
| `/eu-careers:epso-presentation` | Coach and critique a 10-minute Assessment Centre oral presentation against EPSO Communication competency indicators |
| `/eu-careers:epso-offer` | Analyse a job offer letter: decode grade/step, calculate gross and net remuneration, map probation and contract obligations under the SR |

---

## Where to go next

- [QUICKSTART.md](../QUICKSTART.md) — technical installation steps
- [CONTRIBUTING.md](../CONTRIBUTING.md) — how to add a skill or extend a package
- [CONNECTORS.md](../CONNECTORS.md) — connect live EU data sources (Eurostat, EUR-Lex, TED)
- [docs/glossary.md](glossary.md) — EU terminology reference
