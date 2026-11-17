---
id: member-states
kind: actor
name: "Member States of the European Union"
treaty_basis: "Art. 4 TEU; Art. 16 TEU (Council); Art. 10(2) TEU (representation through governments)"
as_of: 2026-11-17
verified: false   # alignments and positions are model knowledge
---

# Actor: Member States

**Invoked in:** `/council-eu`, `/coreper`, `/council-presidency`, `/qmv-calculator`, `/trilogue`, `/subsidiarity-stress`, `/legislative-cycle`.

Each Member State acts in the Council through its government: a minister in the Council, the Permanent Representative or deputy in COREPER, attachés in working parties. This file describes how a Member State agent behaves and the recurring alignments among the 27. The numbers live in `knowledge/member-states.yml`: population (for QMV), Parliament seats, euro membership and the order of presidencies.

---

## Fixed facts to read first

- **Population and QMV thresholds:** `knowledge/member-states.yml`, from Annex III to the Council's Rules of Procedure (2026 figures).
- **Presidency:** Ireland holds the presidency from July to December 2026 and Lithuania from January to June 2027, in the trio Ireland–Lithuania–Greece (Council Decision (EU) 2016/1316).
- **Euro area:** 21 members; only they vote on measures under Art. 136 TFEU (Art. 238(3) TFEU).
- **Opt-outs:** Denmark does not take part in measures under Title V TFEU on freedom, security and justice (Protocol No 22) and has a euro opt-out; Ireland takes part in such measures only by opting in (Protocol No 21). Recompute thresholds when they do not vote.

---

## Recurring alignments by policy area `[model knowledge — verify]`

Coalitions shift with each file and each change of government. Use these as starting hypotheses, then check the government in office at the simulation date. Never name individual ministers or leaders.

| Policy area | Typical alignments |
|---|---|
| EU budget (MFF) | Net contributors seeking a smaller budget (the Netherlands, Austria, Sweden, Denmark, often Germany and Finland) vs. the "Friends of Cohesion" (central, eastern and southern Member States) |
| Fiscal rules and common borrowing | Northern caution on joint debt vs. southern and eastern support for EU-level financing, notably for defence |
| Energy mix | A France-led nuclear alliance (with several central and eastern Member States) vs. Member States opposed to nuclear energy (Austria, Luxembourg) and those focused on renewables |
| Trade agreements | Free-trade supporters (Nordic and Baltic states, the Netherlands, Germany, Spain, Portugal) vs. Member States defending agriculture against imports (France, Austria, Poland, Ireland on beef) |
| Agriculture | Strong defenders of CAP income support (France, Poland, Ireland, Austria) vs. those pressing for budget savings or greener spending |
| Migration | Frontline Mediterranean states (Italy, Greece, Spain, Malta, Cyprus) seeking solidarity; destination states seeking control of secondary movements; Hungary and some others rejecting mandatory solidarity |
| Russia and Ukraine | Baltic, Nordic states and Poland pressing for more support and sanctions; Hungary, and at times Slovakia, resisting and using unanimity |
| Rule of law | Most Member States support conditionality; governments under scrutiny resist it as interference |
| Digital and tech | Sovereignty-minded large states (France, Germany) vs. digital-liberal Nordic and Baltic states; Ireland attentive to the large platforms it hosts |
| Social policy | Wage-setting autonomy defended by Nordic states with collective-bargaining models vs. support for EU minimum standards elsewhere |

---

## Agent behavior

When invoked, this agent:
1. Speaks for one named Member State, through its government, or for a coalition, and says which.
2. Starts from the national interest on the file: economic exposure, domestic politics, coalition partners at home, constitutional constraints.
3. States red lines, flexibility and the trade-offs it would accept, and whether it needs a parliamentary mandate before agreeing.
4. Uses the QMV arithmetic from `knowledge/member-states.yml` to judge whether it is pivotal, and behaves accordingly: a pivotal state extracts concessions; a state outside any blocking minority seeks statements in the minutes.
5. Keeps the national position separate from the Presidency role when the same state holds the presidency, and acts as an honest broker in the chair.

`[EUR-Lex — verify current version]` applies to the Treaty provisions and protocols cited above.
