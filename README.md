# Agents for EU — Simulate EU Policy, Law, and Institutions with Claude Code

> 30,000 staff. 21 Commissioners. Real procedures. Now on your laptop.

<div align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjByaDMyMXFqcmo4aXZxNWVwdHJzbXZlZnN4bWEzNmp3b3g2Z3doeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/UqASWHeU91ADUSk5co/giphy.gif" width="520" alt="EU Commission in session"/>
</div>

<div align="center">

![GitHub Stars](https://img.shields.io/github/stars/montoyer/eu-agents?style=flat-square&color=gold&label=stars)
&nbsp;
![Last Commit](https://img.shields.io/github/last-commit/montoyer/eu-agents?style=flat-square&color=brightgreen&label=last+commit)
&nbsp;
![License](https://img.shields.io/badge/license-EUPL--1.2-blue?style=flat-square)

</div>

---

**A startup lawyer needs a defensible GDPR DPIA for an AI hiring tool.**  
`/eu-privacy:dpia "AI hiring tool"` produces the full Art. 39 EUDPR assessment — DPO threshold, architecture, legal basis, security, EDPS determination — with citations the DPO can actually sign.

**Your team must know if a draft regulation will die in inter-service consultation.**  
`/eu-simulation:inter-service-consultation "Algorithmic pricing regulation"` runs every affected DG and returns their objections with the exact treaty or regulatory basis.

**You are drafting and want to know which Commissioners will fight it.**  
`/eu-simulation:mandate-conflict "AI liability regulation"` maps every structural conflict across all 21 portfolios, with the legal basis on each side and severity.

**You need to know whether your proposal even passes subsidiarity.**  
`/eu-simulation:subsidiarity-stress "Harmonised SME insolvency rules"` tests the necessity argument against five different member-state configurations.

This is not generic prompting. It is the European Commission's institutional machinery — mandates, procedures, and adversarial checks — made executable.

---

## The non-obvious insight

The EU Commission is not primarily a regulator. It is a **structured argumentation engine**: 21 mandate-scoped agents forced to reconcile conflicting treaty obligations through explicit procedures (subsidiarity, impact assessment, inter-service consultation, College deliberation, trilogue).

That machinery is reusable. The same scaffold that produces defensible policy for 450 million people works for any high-stakes decision where multiple legitimate perspectives must survive adversarial scrutiny.

The most powerful commands in this system are the ones that are impossible for a single model:

| Command                        | What only multi-agent + real mandates can do |
|--------------------------------|---------------------------------------------|
| `/eu-simulation:mandate-conflict` | Maps every structurally guaranteed clash across 21 portfolios with treaty bases and severity |
| `/eu-simulation:red-team-college` | Runs the proposal through all 21; returns only SEVERE objections + adoptability verdict |
| `/eu-simulation:subsidiarity-stress` | Tests the necessity argument against 5 different member-state configurations |
| `/eu-simulation:timeline`       | Produces a realistic OLP timeline with QMV thresholds and trilogue risk points |

See [NOI.md](NOI.md) for the full argument.

---

## Quick start

```bash
# 1. Add the marketplace (once)
/plugin marketplace add montoyer/eu-agents

# 2. Install what you need
/plugin install eu-simulation@eu-agents
/plugin install eu-legislative@eu-agents
/plugin install eu-privacy@eu-agents

# Or install everything:
/plugin install --all@eu-agents
```

```markdown
# Run a Commissioner
/eu-simulation:commissioner competition

# Full College deliberation
/eu-simulation:college-deliberation "Should the EU ban algorithmic pricing in retail?"

# Draft a regulation
/eu-legislative:legislative-proposal "Regulation on synthetic biology, legal basis Art. 114 TFEU"

# Compound stress tests
/eu-simulation:mandate-conflict "Regulation on AI liability in critical infrastructure"
/eu-simulation:red-team-college "Carbon border adjustment for agriculture"
/eu-simulation:subsidiarity-stress "Harmonised insolvency rules for SMEs"
```

Every skill output ends with:
```
DRAFT — For review by an EU official before use. Not an official Commission position.
```

---

## What you get

| Plugin                        | Purpose |
|-------------------------------|---------|
| `eu-simulation`               | 21 Commissioners + College + ISC + trilogue + OLP + compound analysis commands |
| `eu-legislative`              | Impact assessment, legislative drafting, treaty check, consultation, REFIT, policy cycle |
| `eu-privacy`                  | Full Art. 39 EUDPR DPIA workflow (DPO → IT-PM → Legal → Security → EDPS) |
| `eu-competition`              | Antitrust (Arts. 101-102), state aid (107-109), mergers, dawn raids, Legal Service |
| `eu-trade`                    | Trade defence: anti-dumping, anti-subsidy, safeguards |
| `eu-grants-enforcement`       | Grant management, infringement procedures (Arts. 258-260), public procurement |
| `eu-institutional-management` | HR, unit management, financial circuits, CDR/AAR/AMP, access to documents |
| `eu-data-communication`       | Eurostat, scoreboards, press releases, lines to take, transparency |
| `eu-careers`                  | EPSO grade/step estimation, presentation coaching, offer analysis |

See [CLAUDE.md](CLAUDE.md) for the complete command reference.

---

## How commands work

- Single-skill: `/eu-legislative:impact-assessment "brief here"`
- Commissioner persona: `/eu-simulation:commissioner digital`
- Multi-agent sessions: `/eu-simulation:inter-service-consultation "proposal"`
- Compound (unique value): `/eu-simulation:mandate-conflict`, `red-team-college`, `subsidiarity-stress`, `timeline`

Most plugins also include a `/eu-xxx:cold-start-interview` to tailor behaviour to your DG or dossier.

---

## Design principles

- **One agent per mandate.** The Competition Commissioner never speaks for Agriculture.
- **Real procedures.** Workflows follow actual EU rules (Better Regulation, Joint Practical Guide, subsidiarity protocol, etc.).
- **Adversarial by design.** Commissioners disagree. The system surfaces conflict rather than smoothing it over.
- **Grounded output.** Every claim that needs verification carries an attribution tag.

---

## Who this is for

- EU policy officers and legislative drafters
- Lawyers doing EU compliance, state aid, or antitrust work
- Consultants and lobbyists who need the institutional position fast
- Researchers modelling policy processes
- Journalists who want the legal basis and cross-portfolio tensions
- Students learning the ordinary legislative procedure interactively
- Anyone who needs structured, multi-perspective reasoning under constraint

---

## Documentation

- [QUICKSTART.md](QUICKSTART.md) — 5-minute onboarding
- [CLAUDE.md](CLAUDE.md) — Complete command reference and agent rules
- [docs/getting-started.md](docs/getting-started.md)
- [docs/examples/](docs/examples/) — Full worked simulations
- [NOI.md](NOI.md) — Why the EU's reasoning machinery is worth programming
- [ARCHITECTURE.md](ARCHITECTURE.md) — How the layers fit together

---

## Status

Production scaffolding for serious use. Core Commissioners, DGs, legislative and privacy workflows are stable. Compound simulation commands and additional domains are under active development.

---

## License

**European Union Public Licence v. 1.2 (EUPL-1.2)**

See [LICENSE](LICENSE) and [joinup.ec.europa.eu/collection/eupl](https://joinup.ec.europa.eu/collection/eupl).

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New skills, Commissioners, DGs, and connectors are welcome.

---

<div align="center">
  <sub>If this helps you do better EU work, star the repo. It helps other people find it.</sub>
</div>
