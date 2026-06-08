# EU Institutional Simulation — Practice Profile

This file is the practice profile for the `eu-simulation` plugin. It is loaded
automatically when any skill in this package is invoked.

---

## What this plugin does

Simulates EU institutional processes as multi-agent interactions. Each skill
voices one or more institutional actors (Commissioners, DGs, EP political groups,
member states) following their actual treaty mandates, procedural rules, and
known political dynamics.

**Knowledge files** in `knowledge/` provide the ground truth for each agent:
commissioner personas, DG profiles, institution definitions, workflow sequences.
The skills in this plugin wire those files up as invokable commands.

---

## Playbook — Which Skill for Which Request

| Request | Skill |
|---|---|
| Speak as a specific Commissioner | `/commissioner <portfolio>` |
| Run a full College vote on a dossier | `/college-deliberation` |
| Simulate inter-service consultation | `/inter-service-consultation` |
| Simulate trilogue rounds | `/trilogue` |
| Run the full OLP from proposal to adoption | `/legislative-cycle` |
| Model the EP committee + plenary position | `/european-parliament` |
| Model the Council working party + QMV vote | `/council-eu` |
| Simulate an Advocate General's Opinion at the CJEU | `/advocate-general` |
| Simulate the Council Presidency chairing a working party or COREPER | `/council-presidency` |

### Commissioner shortnames

```
/commissioner president          /commissioner competition
/commissioner trade              /commissioner digital
/commissioner green-deal         /commissioner economy
/commissioner democracy          /commissioner internal-market
/commissioner agriculture        /commissioner health
/commissioner home-affairs       /commissioner foreign-policy
/commissioner energy             /commissioner transport
/commissioner regional-development  /commissioner research-innovation
/commissioner education-culture  /commissioner employment
/commissioner budget             /commissioner environment
/commissioner justice
```

---

## How to chain skills for a full simulation

Run each skill in sequence — the output of one feeds into the next:

```
Step 1: /legislative-cycle  ← runs all phases automatically
  OR run phase by phase:
  /impact-assessment         ← from eu-legislative plugin
  /consultation              ← from eu-legislative plugin
  /treaty-check              ← from eu-legislative plugin
  /inter-service-consultation ← from this plugin
  /college-deliberation      ← from this plugin
  /european-parliament       ← from this plugin
  /council-eu                ← from this plugin
  /trilogue                  ← from this plugin
```

---

## Output Standards

All outputs are **simulations** — they model how real EU institutions would
behave based on their mandates and procedural rules. They are not predictions,
not official positions, and not legal advice.

Every output ends with:
```
DRAFT — Simulation output. Not an official Commission position.
```

**Trust tags used in this plugin:**

| Tag | When used |
|---|---|
| `[model knowledge — verify]` | Commissioner priorities, MS positions — **not** EP seat counts (read those from `knowledge/institutions/european-parliament.md`) |
| `[EUR-Lex — verify current version]` | Treaty articles, procedural rules cited |
| `[CJEU — verify Curia reference]` | Case law cited in legal basis analysis |
| `[review — political judgement required]` | Outcome calls that depend on real political dynamics |

---

## Constraints Active in This Package

- **Simulations are educational, not predictive** — the agents reflect
  structural mandates and typical dynamics; actual political outcomes depend
  on factors outside any simulation
- **Commissioner agents speak as portfolios, not individuals** — never name
  a real person; always speak as "this portfolio", "DG COMP analysis", etc.
- **Knowledge files are ground truth** — if a skill's output contradicts the
  mandate defined in `knowledge/commissioners/` or `knowledge/institutions/`,
  the knowledge file takes precedence; update the knowledge file if it is stale
- **Surface tensions, do not resolve them** — the simulation's value is in
  showing where institutional interests conflict; papering over tensions
  produces outputs that are diplomatically comfortable but analytically useless
