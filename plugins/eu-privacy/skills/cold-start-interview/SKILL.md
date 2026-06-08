---
name: cold-start-interview
description: >
  Personalise the privacy-eu plugin to a specific DG, processing activity, and working
  context before running a DPIA or any specialist data-protection skill. Collects:
  DG/Unit name, processing activity description, controller identity, data subjects,
  presence of special categories, non-EU cloud or AI providers, DPIA reference number,
  and working language. Writes the [SESSION CONTEXT] block in CLAUDE.md so all
  subsequent skill invocations in this session operate with the correct institutional
  and technical context.
license: MIT
metadata:
  author: EC-Skills-Library
  version: "1.0.0"
  domain: eu-data-protection-setup
  triggers: >
    cold start, setup privacy plugin, configure DPIA context, set DG for DPIA,
    personalise privacy-eu, initialize data protection session
  role: setup
  scope: session-configuration
  output-format: session-context-block
  institution: European Commission
  related-skills: dpia, dpo, it-project-manager, it-security, legal-officer
---

# Cold-Start Interview — Privacy & Data Protection Plugin

Welcome to the `privacy-eu` plugin. This brief interview personalises the session for
your DG and processing activity. Answer each question; the [SESSION CONTEXT] block
will be populated automatically.

---

## Interview Questions

1. **DG / Unit**: What DG and unit are you in? (e.g. "DG DIGIT, Unit B.3 — Cloud Infrastructure")

2. **Processing activity**: What is the name or brief description of the processing activity you are assessing? (e.g. "EDPS contact form with AI-assisted triage module")

3. **Controller identity**: Which EU institution or body is the controller? (e.g. "European Commission", "EDPS", "EU-OSHA")

4. **Data subjects**: Who are the data subjects? (e.g. "EU citizens submitting complaints", "Commission staff", "grant beneficiaries")

5. **Special categories (Art. 10 EUDPR)**: Does the processing involve any special categories of personal data (health data, biometric data, racial/ethnic origin, political opinions, etc.)? YES / NO

6. **Non-EU cloud or AI provider**: Does the system use any cloud infrastructure or AI provider hosted outside the EU/EEA? YES / NO. If yes, which provider and country?

7. **DPIA reference**: Do you have a DPIA reference number, or should one be assigned? (e.g. "DPIA-2026-001")

8. **Working language**: What is the primary working language for this session? (default: EN)

---

## SESSION CONTEXT Output

Once you have answered the above, the following block will be used to update the
plugin session context:

```
DG / Unit:                    [your answer]
Processing activity:          [your answer]
Controller:                   [your answer]
Data subjects:                [your answer]
Special categories involved:  [YES — Art. 10 EUDPR / NO]
Non-EU cloud / AI provider:   [YES — [provider, country] — TIA required / NO]
DPIA reference:               [DPIA-YYYY-NNN]
Working language(s):          [EN / FR / DE / other]
Confidentiality level:        NORMALE
```

---

DRAFT — Session context only. No official DPIA determination produced at this stage.
