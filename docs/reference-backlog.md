# Reference backlog — cited-but-missing files

Generated from `scripts/validate.sh` warnings on 2026-06-10: **160 unique missing
files, 189 citations** across 4 plugins (eu-legislative 73, eu-competition 38,
eu-grants-enforcement 36, eu-data-communication 13). The other five plugins are
clean.

Each file below is tagged with one proposed action:

- **WRITE** — author the reference (short "key provisions / how to use" summary
  with EUR-Lex trust tags, like the existing `gber-de-minimis-2024.md`). Grouped
  into thematic packs so one work session clears a whole group.
- **ALIAS → x** — same document cited under a different name; do not write a new
  file, update the citation in the SKILL.md to the canonical name.
- **STRIP** — internal Commission system / portal walkthrough that cannot be
  authored from public sources. Remove the `references/` citation from the
  SKILL.md and replace with an inline pointer (e.g. "consult the ARES user guide
  on MyIntraComm").

Naming convention and cross-plugin sharing rules: see CONTRIBUTING.md § 3a.
Recurring documents (treaty articles, Charter) have one canonical file; other
plugins receive machine-managed copies via `scripts/sync-shared-references.sh`,
drift-checked by `validate.sh` check 6. Never symlink, never copy by hand.

Re-run `bash scripts/validate.sh | grep cited-but-missing` at any time to see
which SKILL.md cites which file. When a plugin reaches zero warnings, the goal
is `scripts/validate.sh --strict` in the pre-commit hook.

---

## Phase 1 — alias consolidation ✅ applied 2026-06-10

All citations below were renamed in the SKILL.md files (unique missing files:
160 → 138; the `gber-de-minimis-2024.md` rows resolved outright because the
file exists).

| Cited name | Canonical (to write in Phase 2/3) |
|---|---|
| `eu-legislative/br-guidelines-2023.md`, `better-regulation-guidelines.md` | `better-regulation-guidelines-2023.md` |
| `eu-legislative/br-toolbox-2023.md` (×2), `br-toolbox-economics.md` | `better-regulation-toolbox-2023.md` |
| `eu-legislative/better-regulation-toolbox.md` (×5) | `better-regulation-toolbox-2023.md` |
| `eu-legislative/protocol-2-subsidiarity.md` | `subsidiarity-protocol.md` |
| `eu-legislative/jpo-drafting-guide.md` | `joint-practical-guide.md` |
| `eu-legislative/sme-test-guide.md`, `sme-test-methodology.md` | `sme-test.md` |
| `eu-legislative/comitology-regulation.md`, `comitology-delegated-acts.md` | `comitology-reg-182-2011.md` |
| `eu-legislative/cba-guidelines.md` | `cba-methodology.md` |
| `eu-legislative/isc-guide.md` | `isc-procedure.md` |
| `eu-legislative/isg.md` | `interinstitutional-style-guide.md` (distinct document — Interinstitutional Style Guide, not ISC) |
| `eu-legislative/legal-base-treaty.md` | `tfeu-teu-consolidated.md` |
| `eu-legislative/fitness-check-methodology.md` | `evaluation-methodology.md` |
| `eu-legislative/rsb-quality-checklist.md`, `rsb-review-standards.md` | `rsb-criteria.md` |
| `eu-competition/aber.md` | `aber-2022.md` |
| `eu-competition/gber-2014.md`, `de-minimis-regulation.md` | existing `gber-de-minimis-2024.md` ✅ already on disk |
| `eu-grants-enforcement/eu-pilot.md` | `eu-pilot-guide.md` |
| `eu-grants-enforcement/transposition-monitoring.md` | `transposition-guide.md` |
| `eu-grants-enforcement/tfeu-infringement.md` | `art258-procedure.md` |
| `eu-grants-enforcement/fr-grants-chapter.md` | `financial-regulation-2018-1046.md` |
| `eu-grants-enforcement/recovery-order-guide.md` | `financial-correction-methodology.md` |

## Phase 2 — Tier-1 shared primers (top-cited)

For documents needed by several plugins (`eu-charter.md`,
`tfeu-teu-consolidated.md`): write the canonical once in `eu-legislative`, then
register the consumer copies in `scripts/sync-shared-references.sh`.

- [ ] `eu-legislative/references/better-regulation-toolbox-2023.md` — 8 citations after alias pass
- [ ] `eu-legislative/references/subsidiarity-protocol.md` — Protocol No 2 (9 articles, short enough for full text) + early-warning summary — 5 citations
- [ ] `eu-legislative/references/joint-practical-guide.md` — JPG key drafting rules — 5 citations
- [ ] `eu-legislative/references/eu-charter.md` — Charter structure + most-litigated articles — 4 citations
- [ ] `eu-competition/references/eu-charter.md` — same content, competition-litigation angle
- [ ] `eu-legislative/references/tfeu-teu-consolidated.md` — key legal-basis articles index — 3 citations after alias pass
- [ ] `eu-competition/references/tfeu-teu-consolidated.md`
- [ ] `eu-grants-enforcement/references/tfeu-teu-consolidated.md` — ×2 citations
- [ ] `eu-legislative/references/better-regulation-guidelines-2023.md` — 2 citations after alias pass
- [ ] `eu-legislative/references/comitology-reg-182-2011.md` — 4 citations after alias pass
- [ ] `eu-legislative/references/cjeu-legal-basis.md` — centre-of-gravity case law — 2 citations

## Phase 3 — thematic packs per plugin (WRITE unless tagged)

### eu-legislative (remaining)

**Better Regulation / IA pack** — `rsb-criteria.md`, `swd-ia-templates.md`,
`consultation-standards.md` (×2), `stakeholder-categories.md`, `sme-test.md`,
`cba-methodology.md`, `evaluation-methodology.md`, `fundamental-rights-ia.md`,
`dnsh-guidance.md`, `refit-platform.md`, `cjeu-subsidiarity-caselaw.md`,
`early-warning-mechanism.md` (or fold into `subsidiarity-protocol.md`)

**Comitology / delegated acts pack** — `delegated-implementing-acts.md` (×2),
`art290-291-tfeu.md`, `iia-2016-comitology.md`, `comitology-urgency.md`,
`comitology-preamble-templates.md`, `da-empowerment-analysis.md`,
`da-scrutiny-management.md`, `committee-meeting-guide.md`

**Drafting pack** (candidates to fold into `joint-practical-guide.md`) —
`definitions-drafting.md`, `transitional-repeal-clauses.md`,
`penalty-clause-formulas.md`, `legal-service-drafting.md`,
`interinstitutional-style-guide.md`

**Procedure pack** — `isc-procedure.md` (×2), `pq-procedure.md` (×2),
`ep-rules-procedure.md` (×2), `council-rules-procedure.md`,
`council-wp-procedure.md`, `expert-group-rules.md`, `four-column-document.md`,
`commission-trilogue-role.md`, `transposition-monitoring.md`, `tris-procedure.md`

**Economist pack** — single `economist-methods.md` replacing citations to:
`eurostat-methodology.md`, `european-semester-methodology.md`, `ameco-guide.md`,
`jrc-modelling-tools.md`, `cge-trade-modelling.md`, `eif-formulas.md`

**STRIP (eu-legislative)** — `ares-user-guide.md` (internal system),
`have-your-say.md` (portal), `comitology-register-guide.md` (portal),
`gdpr.md` (cite EUR-Lex 2016/679 inline), `financial-regulation-2018.md`
(out of domain — cite inline), `merger-assessment-guidelines.md` +
`market-definition-notice.md` (eu-competition domain — cite inline),
`amp-aar-guide.md` (eu-institutional-management domain),
`line-to-take.md` + `communication-drafting-guide.md` (eu-data-communication
domain — cite inline)

### eu-competition (remaining)

**Antitrust pack** — `art101-102-tfeu.md`, `reg-1-2003.md`,
`horizontal-guidelines-2023.md`, `vber-2022.md`, `art102-guidance.md` (×2),
`fines-guidelines-2006.md`, `leniency-notice-2006.md`, `settlement-notice.md`,
`cls-privilege.md`

**State aid pack** — `art107-109-tfeu.md`, `sa-procedure-regulation.md`,
`state-aid-manual.md`, `aber-2022.md`, `gber-rdni.md`, `eeag-2022.md`,
`rag-2022.md`, `rdni-framework-2022.md`, `ipcei-communication.md`, `tctf.md`,
`sgei-framework.md`, `sgei-altmark.md`

**Merger / market pack** — `merger-regulation.md`, `market-definition-notice.md`
(×2), `market-definition-caselaw.md`, `dma-gatekeeper.md` (×2)

**Litigation pack** — `art263-standing.md`, `art267-preliminary.md`,
`art218-procedure.md`, `cjeu-statute-rp.md`, `gc-rules-procedure.md`,
`cjeu-caselaw.md`, `general-principles.md`

**STRIP (eu-competition)** — `sani2-guide.md` (internal notification system)

### eu-grants-enforcement (remaining)

**Infringement pack** — `art258-procedure.md`, `art260-penalties.md`,
`art260-3-non-transposition.md`, `infringement-procedure-guide.md` (×2),
`infringement-priorities.md`, `infringement-case-law.md`, `eu-pilot-guide.md`
(×2), `lfn-drafting-guide.md`, `ro-drafting-guide.md`, `penalty-calculation.md`,
`transposition-guide.md` (×2), `mne-guide.md`

**Grants pack** — `financial-regulation-2018-1046.md`, `he-mga.md`,
`he-eligible-costs.md`, `cef-grant-guide.md`, `life-grant-guide.md`,
`rap-delegated-regulation.md`, `audit-preparation-checklist.md`,
`financial-correction-methodology.md`, `alt-analysis.md`

**Procurement pack** — `exclusion-selection-criteria.md`,
`contract-modification-rules.md`, `conflict-of-interest-procurement.md`,
`framework-contracts-guide.md`

**STRIP (eu-grants-enforcement)** — `abac-grants-guide.md`, `fnt-portal-guide.md`,
`chap-guide.md`, `etendering-guide.md`, `eur-lex-nim.md` (all internal systems
or database portals)

### eu-data-communication

**Comms practice pack** — `comm-style-guide.md`, `spokesperson-guidelines.md`,
`speech-drafting-guide.md`, `crisis-communication.md`,
`disinformation-response.md`, `social-media-guidelines.md`,
`europa-content-standards.md`, `eu-campaign-toolkit.md`,
`commissioner-statements.md`, `ep-rules-procedure.md`

**STRIP (eu-data-communication)** — `ltt-registry.md` (internal registry),
`rapid-press-service.md` (portal), `av-production-guide.md` (internal service)

## Phase 4 — enforce

- [ ] When a plugin reaches zero warnings, note it here.
- [ ] When all plugins are clean, switch `.githooks/pre-commit` to
      `scripts/validate.sh --strict` so new dead citations fail the commit.
