# Example: AI Act — Commission to Adoption Simulation

This worked example walks through how the EU AI Act (Regulation 2024/1689)
would have been processed through the Agents for EU system, from Commission
proposal to final adoption.

## Setup

```
/plugin marketplace add montoyer/eu-agents
/plugin install eu-simulation@eu-agents
/plugin install eu-legislative@eu-agents
```

---

## Historical context

The AI Act was proposed by the Commission in April 2021 (COM(2021) 206 final).
It took 3 years to adopt — final text published in OJ on 12 July 2024.
It is the world's first comprehensive AI regulatory framework.

---

## Step 1 — Commission proposal

```
/eu-legislative:legislative-proposal

Brief: A regulation establishing harmonised rules on artificial intelligence,
based on a risk-based approach: prohibited AI, high-risk AI, limited risk AI,
and minimal risk AI. Legal basis: TFEU Art. 114 (internal market). Lead
Commissioner: EVP Digital.
```

Key tensions to surface:
- DG COMP: AI Act vs. competition law — market access implications for Big Tech
- DG JUST: Biometric identification — fundamental rights (Charter Arts. 7, 8)
- DG HOME: Law enforcement exemptions — security vs. rights

---

## Step 2 — Inter-service consultation

```
/eu-simulation:inter-service-consultation

Dossier: AI Act draft — COM(2021) 206. Lead DG: DG CONNECT. Consult: DG JUST,
DG HOME, DG GROW, DG RTD, DG COMP, Legal Service, SecGen.
```

Expected positions:
- DG JUST: Reservations on biometric AI exemptions for law enforcement
- DG HOME: Support for law enforcement exemptions; wants broader security carve-outs
- DG GROW: Concerns about compliance burden on SMEs; requests SME test review
- DG RTD: Concerns about research exemption scope
- Legal Service: Confirm Art. 114 legal basis; flag GPAI coverage gap

---

## Step 3 — College deliberation

```
/eu-simulation:college-deliberation

Dossier: AI Act proposal — COM(2021) 206. Decision sought: adopt for
transmission to EP and Council. Lead Commissioner: EVP Digital.
```

Expected College dynamics:
- EVP Digital: Strong support — flagship digital proposal
- EVP Economy: Reservations on compliance costs; requests SME relief
- Commissioner for Justice: Support conditional on strong biometric restrictions
- Commissioner for Home Affairs: Demands law enforcement exemptions preserved
- Commissioner for Competition: Flags market concentration risk

---

## Step 4 — EP position

```
/eu-simulation:european-parliament

Dossier: AI Act — COM(2021) 206. Responsible committee: IMCO + LIBE (joint).
Model the EP rapporteur position and key amendments.
```

The EP moved significantly further than the Commission on:
- Banning real-time biometric surveillance (EP initially wanted near-total ban)
- Adding GPAI / foundation models as a new category
- Expanding the prohibited AI list (emotion recognition, social scoring)

---

## Step 5 — Council position

```
/eu-simulation:council-eu

Dossier: AI Act — COM(2021) 206. Configuration: COMPET. Model the Council
general approach — where it diverges from the Commission proposal and EP amendments.
```

---

## Step 6 — Trilogue

```
/eu-simulation:trilogue

Dossier: AI Act. Commission: COM(2021) 206. EP position: IMCO/LIBE mandate
(biometric ban, GPAI, expanded prohibited list). Council GA: flexibility for
law enforcement, narrower GPAI scope, longer transition periods.
```

Key trilogue fault lines:
- **GPAI / foundation models**: EP strict; Council flexible; Commission tiered
  approach based on systemic risk
- **Biometric surveillance**: EP red line (strict prohibition); Council red line
  (law enforcement needs exemptions); bridge: narrow exemptions + judicial authorisation
- **Prohibited AI**: EP broader list; Council narrower; Commission defended its categories

Historical outcome: political agreement December 2023. Final text adopted April 2024.

---

## Or run the whole cycle at once

```
/eu-simulation:legislative-cycle

Brief: AI Act — a regulation establishing harmonised rules on AI based on a
risk-based approach (prohibited / high-risk / limited risk / minimal risk).
Legal basis: TFEU Art. 114. Lead Commissioner: EVP Digital. Run all phases.
```

---

## Key learnings from this simulation

1. **GPAI was a gap in the original proposal** — the Commission had not
   anticipated the ChatGPT moment; the trilogue had to legislate in real time

2. **Biometric surveillance was the hardest fault line** — the rights/security
   tension is irreducible; the final compromise (narrow exemptions + strict
   conditions + judicial authorisation) was the only viable path

3. **SME impact was underweighted** in the original IA — a recurring weakness
   on tech regulation

4. **Art. 114 legal basis held** — the CJEU would likely confirm it given the
   clear single-market rationale for uniform AI rules
