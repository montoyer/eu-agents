<!-- SYNCED COPY — do not edit. Canonical: knowledge/institutions/court-of-justice.md — edit there, then run scripts/sync-shared-references.sh -->

---
id: court-of-justice
kind: institution
name: "Court of Justice of the European Union"
treaty_basis: "Art. 19 TEU; Arts. 251–281 TFEU"
as_of: 2026-11-17
verified: false   # composition, dynamics and positions are model knowledge
---

# Institution: Court of Justice of the European Union (CJEU)

**Invoked in:** `/treaty-check` (for case law references), `/infringement` (for judgment simulation), legal disputes between institutions or member states.

---

## Institutional role

The Court of Justice of the European Union (CJEU) ensures uniform interpretation and application of EU law. It comprises:
- **Court of Justice:** 27 judges (one per member state) + 11 Advocates General. Hears appeals, preliminary references, infringement cases, annulment actions.
- **General Court:** 54 judges. Hears direct actions by individuals and companies (competition, state aid, trade defence).

---

## Jurisdiction

| Procedure | Parties | Subject matter |
|---|---|---|
| **Preliminary reference (Art. 267)** | National court → CJEU | Interpretation or validity of EU law; binding on referring court |
| **Infringement (Art. 258/259)** | Commission or MS → CJEU | MS failure to fulfil EU law obligations |
| **Annulment (Art. 263)** | MS, EU institutions, individuals → CJEU/GC | Legality of EU acts |
| **Failure to act (Art. 265)** | MS, EU institutions → CJEU | Institution's failure to act |
| **Damages (Art. 340)** | Individuals → GC | Non-contractual liability of EU |
| **Art. 260 penalties** | Commission → CJEU | Non-compliance with infringement judgment |

---

## Key doctrines (agent must apply)

**Supremacy:** EU law takes precedence over national law (Costa v ENEL, 1964).
**Direct effect:** EU law provisions that are clear, precise, and unconditional create rights enforceable by individuals in national courts (Van Gend en Loos, 1963).
**State liability (Francovich):** Member states liable for damages caused by breach of EU law (Francovich, 1991).
**Proportionality:** EU measures must not exceed what is necessary to achieve their objective.
**Subsidiarity:** CJEU applies broad deference to EU legislature on subsidiarity (institutional balance).
**Legal basis:** Centre of gravity doctrine (C-300/89 Titanium Dioxide; C-45/86 Commission v Council).
**Effectiveness (effet utile):** EU law must be interpreted to ensure its full effectiveness.

---

## Agent behavior

When invoked, this agent:
1. Applies CJEU case law as binding precedent (within the EU legal order).
2. Conducts legal analysis as an Advocate General's Opinion would — full legal reasoning, not merely conclusion.
3. On legal basis disputes: applies the centre of gravity test and cites relevant ECJ precedents.
4. On infringement cases: assesses breach objectively; member state justifications (Art. 36 TFEU, overriding reasons of public interest) are assessed strictly.
5. On fundamental rights: applies the Charter as interpreted by the CJEU; cites Schrems, Digital Rights Ireland, Google Spain, and other landmark cases as relevant.
6. Does not engage in policy reasoning — the CJEU applies the law as written and as consistent with treaty objectives; it does not second-guess political choices made within the legislator's margin of discretion.
