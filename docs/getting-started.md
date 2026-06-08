# Getting Started

## What you can do in 5 minutes

### 0. Install the plugins

Add the marketplace and install the plugins you need:

```
/plugin marketplace add montoyer/eu-agents
/plugin install simulation-eu@eu-agents
/plugin install legislative-eu@eu-agents
```

---

### 1. Ask a single Commissioner a question

```
/eu-simulation:commissioner competition
```

Then ask: *Is the proposed merger of two major European steel producers compatible with EU competition law?*

Claude will adopt the Competition Commissioner persona, apply the EU Merger Regulation test, and give you a legally grounded preliminary assessment.

---

### 2. Run a quick impact assessment

```
/eu-legislative:impact-assessment "A proposed EU regulation requiring all commercial buildings to install EV charging infrastructure by 2030"
```

This produces a structured Staff Working Document covering problem definition, policy options, and economic/social/environmental impacts.

---

### 3. Simulate a College vote

```
/eu-simulation:college-deliberation "Should the Commission propose a ban on PFAS ('forever chemicals') across all uses by 2030?"
```

All 21 Commissioners will speak. The Competition Commissioner will worry about industry impact. The Environment Commissioner will support the ban. The EVP Economy will demand a REFIT analysis. The President will find a compromise. You get the full deliberation.

---

### 4. Draft a legislative proposal

```
/eu-legislative:legislative-proposal "A regulation establishing a European Digital Infrastructure Fund, financed by a levy on large digital platforms"
```

Produces a structurally complete draft regulation with legal basis, recitals, operative articles, explanatory memorandum, and quality checks.

---

### 5. Run a full legislative cycle simulation

```
/eu-simulation:legislative-cycle "Mandatory supply chain due diligence for critical raw materials"
```

This runs the entire process: Commission proposal → impact assessment → inter-service consultation → College adoption → EP first reading → Council → trilogue → adoption.

---

## Understanding the outputs

**What these agents produce is structurally realistic, not legally authoritative.** The outputs follow EU drafting conventions and apply real treaty articles and procedures. They are suitable for:
- Research and scenario analysis
- Education and simulation
- Policy drafting scaffolds (to be refined by lawyers)
- Civic tech applications explaining EU decisions

They are not legal opinions and should not be relied upon as such.

---

## Common errors to avoid

**Don't ask a Commissioner to speak outside their mandate.** The Agriculture Commissioner will not give you an opinion on competition law. If you need cross-portfolio analysis, use `/eu-simulation:college-deliberation` or specify multiple Commissioner perspectives.

**Don't skip the legal basis.** Any legislative proposal needs a treaty legal basis. If you don't know which article applies, use `/eu-legislative:treaty-check` first.

**Don't confuse Council of the EU with the European Council.** The Council of the EU (ministers) co-legislates. The European Council (heads of state) sets strategic direction but does not legislate.

**Don't confuse regulation with directive.** A regulation is directly applicable (no national transposition). A directive requires transposition by a deadline. The choice matters for the legislative proposal structure.

---

## Reading further

- [ARCHITECTURE.md](../ARCHITECTURE.md) — system design and layer structure
- [CLAUDE.md](../CLAUDE.md) — full command reference
- [docs/glossary.md](glossary.md) — EU terminology
- [examples/](../examples/) — worked simulations
