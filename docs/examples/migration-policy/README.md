# Example: New Pact on Migration and Asylum

This example simulates the Commission's New Pact on Migration and Asylum — the most politically contested legislative package in recent EU history, 4 years in the making (2020-2024).

---

## The package

| Instrument | Legal nature | Key provision |
|---|---|---|
| Asylum and Migration Management Regulation | Regulation | Solidarity mechanism (mandatory solidarity — financial/relocation) |
| Asylum Procedures Regulation | Regulation | Accelerated border procedure; safe third country |
| Screening Regulation | Regulation | Screening at external border within 7 days |
| Eurodac Regulation | Regulation | Expanded biometric database |
| Reception Conditions Directive | Directive | Minimum standards for asylum seekers |
| Crisis and Force Majeure Regulation | Regulation | Emergency solidarity mechanism |

---

## The core political tension

```
/eu-simulation:college-deliberation "New Pact: mandatory solidarity vs. voluntary solidarity — which model should the Commission propose?"
```

**The fundamental divide:**
- **Southern member states (Italy, Greece, Spain, Malta):** "Primary arrival" countries; demand mandatory relocation of asylum seekers to other member states.
- **Central/Eastern member states (Hungary, Poland, Czech Republic, Slovakia — Visegrád group):** Refuse mandatory relocation on sovereignty grounds; willing to offer financial contributions instead.
- **Commission's challenge:** Find a solidarity mechanism that is mandatory enough to satisfy the south but flexible enough not to lose the east and north.

**The Commission solution:** Flexible mandatory solidarity — member states choose between relocation, financial contributions, or operational support. The total solidarity "pool" is mandatory; the form is flexible.

---

## Simulate the Council blocking minority dynamics

```
/eu-simulation:council-eu "New Pact — mandatory solidarity: QMV analysis. Which member states form a blocking minority?"
```

**Analysis:** Hungary, Poland (pre-2023), Czech Republic, Slovakia = 4 member states, but their combined population is insufficient for a blocking minority alone. The Commission's QMV bet was correct — the Visegrád group could not block. But political dynamics (non-paper coalitions, package deals) meant the negotiations were still highly complex.

---

## The fundamental rights constraint

```
/eu-legislative:treaty-check "Accelerated border procedure — is 7-day screening compatible with fundamental rights?"
```

**Key rights engaged:**
- Art. 18 Charter: Right to asylum
- Art. 19 Charter: Non-refoulement
- Art. 47 Charter: Right to effective judicial remedy
- ECHR Art. 3: Prohibition of inhuman treatment

**The legal tightrope:** A 7-day border procedure that effectively bars entry without adequate legal review may violate Art. 47 Charter (effective remedy must be available before a removal decision becomes enforceable). This is the central legal vulnerability of the Pact's border procedure provisions.

---

## Key learning

The New Pact illustrates the hardest category of EU legislation: where member-state sovereignty concerns are high, fundamental rights constraints are real, and the political coalition needed for adoption requires trading off both. The Commission's 4-year negotiation succeeded — but only by accepting significant dilution of the original mandatory solidarity ambition.
