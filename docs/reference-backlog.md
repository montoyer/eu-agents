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
| `eu-legislative/br-guidelines-2023.md`, `better-regulation-guidelines.md` | `better-regulation-guidelines-2021.md` |
| `eu-legislative/br-toolbox-2023.md` (×2), `br-toolbox-economics.md` | `better-regulation-toolbox-2025.md` |
| `eu-legislative/better-regulation-toolbox.md` (×5) | `better-regulation-toolbox-2025.md` |
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
| `eu-grants-enforcement/fr-grants-chapter.md` | `financial-regulation-2024-2509.md` |
| `eu-grants-enforcement/recovery-order-guide.md` | `financial-correction-methodology.md` |

## Phase 2 — Tier-1 shared primers (top-cited)

For documents needed by several plugins (`eu-charter.md`,
`tfeu-teu-consolidated.md`): write the canonical once in `eu-legislative`, then
register the consumer copies in `scripts/sync-shared-references.sh`.

- [x] `eu-legislative/references/better-regulation-toolbox-2025.md` — 8 citations after alias pass ✅ written 2026-06-10
- [x] `eu-legislative/references/subsidiarity-protocol.md` — Protocol No 2 article-by-article + early-warning mechanism — 5 citations ✅ written 2026-06-10
- [x] `eu-legislative/references/joint-practical-guide.md` — JPG 22 guidelines + DA/IA drafting standard — 5 citations ✅ written 2026-06-10
- [x] `eu-legislative/references/eu-charter.md` — Charter structure, Art. 51 scope, Art. 52(1) restriction test, rights-engagement screen — 4 citations ✅ written 2026-06-10
- [x] `eu-competition/references/eu-charter.md` — synced copy of the above via `sync-shared-references.sh` ✅ 2026-06-10
- [x] `eu-legislative/references/tfeu-teu-consolidated.md` — key-articles index: TEU foundations, legal-basis table, Arts. 288–294 (OLP stages), 258–260, judicial review ✅ written 2026-06-10
- [x] `eu-competition/references/tfeu-teu-consolidated.md` — synced copy ✅ 2026-06-10
- [x] `eu-grants-enforcement/references/tfeu-teu-consolidated.md` — synced copy ✅ 2026-06-10
- [x] `eu-legislative/references/better-regulation-guidelines-2021.md` — verified against the SWD(2021) 305 PDF; notes the Guidelines-vs-Toolbox edition split ✅ written 2026-06-10
- [x] `eu-legislative/references/comitology-reg-182-2011.md` — verified verbatim against the OJ text via the Publications Office Cellar API (EUR-Lex itself is WAF-blocked for non-browser clients; Cellar `publications.europa.eu/resource/celex/<CELEX>` works) ✅ written 2026-06-10
- [x] `eu-legislative/references/cjeu-legal-basis.md` — centre-of-gravity doctrine, Art. 114 limits, boundary disputes, drafting checklist; all holdings Curia-tagged ✅ written 2026-06-10

**Phase 2 complete** (2026-06-10): all 11 primers written; citations 189 → 132.

## Phase 3 — thematic packs per plugin (WRITE unless tagged)

### eu-legislative (remaining)

**Better Regulation / IA pack** ✅ written 2026-06-10 from the December 2025
Toolbox chapter PDFs (verified source text): `rsb-criteria.md` (Tool #3),
`swd-ia-templates.md` (Tool #11), `consultation-standards.md` (Tools #51–#55),
`stakeholder-categories.md` (Tool #52), `sme-test.md` (Tool #23),
`cba-methodology.md` (Tools #56–#65), `evaluation-methodology.md`
(Tools #45–#50), `fundamental-rights-ia.md` (Tool #29), `dnsh-guidance.md`
(Tool #36), `refit-platform.md` (Tool #2). `early-warning-mechanism.md` folded
into `subsidiarity-protocol.md` (citation updated). Still open from this pack:
- [ ] `cjeu-subsidiarity-caselaw.md` — case law, not a Toolbox topic; write
      from CJEU sources with Curia trust tags

**Comitology / delegated acts pack** — `iia-2016-comitology.md` ✅ written
2026-06-10 (verified against OJ L 123/2016). Remaining:
`delegated-implementing-acts.md` (×2),
`art290-291-tfeu.md`, `comitology-urgency.md`,
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

**Antitrust pack** — ✅ partially written 2026-06-10 from user-saved OJ HTML
(verified): `reg-1-2003.md`, `vber-2022.md`, `art102-guidance.md` (×2),
`fines-guidelines-2006.md`. Remaining: `art101-102-tfeu.md` (consider alias →
synced `tfeu-teu-consolidated.md`), `horizontal-guidelines-2023.md`,
`leniency-notice-2006.md`, `settlement-notice.md`, `cls-privilege.md`
(case law)

**State aid pack** — `sa-procedure-regulation.md` ✅ written 2026-06-10 (verified against OJ L 248/2015). Remaining: `art107-109-tfeu.md`,
`state-aid-manual.md`, `aber-2022.md`, `gber-rdni.md`, `eeag-2022.md`,
`rag-2022.md`, `rdni-framework-2022.md`, `ipcei-communication.md`, `tctf.md`,
`sgei-framework.md`, `sgei-altmark.md`

**Merger / market pack** — ✅ mostly written 2026-06-10 from user-saved OJ
HTML (verified): `merger-regulation.md`, `market-definition-notice.md` (×2,
2024 Notice), `dma-gatekeeper.md` (×2). Remaining:
`market-definition-caselaw.md`

**Litigation pack** — `art263-standing.md`, `art267-preliminary.md`,
`art218-procedure.md`, `cjeu-statute-rp.md`, `gc-rules-procedure.md`,
`cjeu-caselaw.md`, `general-principles.md`

**STRIP (eu-competition)** — `sani2-guide.md` (internal notification system)

### eu-grants-enforcement (remaining)

**Infringement pack** — `infringement-procedure-guide.md` (×2) + `infringement-priorities.md` ✅ written 2026-06-10 (verified against OJ C 18/2017). Remaining: `art258-procedure.md`, `art260-penalties.md`,
`art260-3-non-transposition.md`, `infringement-case-law.md`, `eu-pilot-guide.md`
(×2), `lfn-drafting-guide.md`, `ro-drafting-guide.md`, `penalty-calculation.md`,
`transposition-guide.md` (×2), `mne-guide.md`

**Grants pack** — `financial-regulation-2024-2509.md` ✅ written 2026-06-10 (verified against the 2024 recast OJ text; canonical renamed from financial-regulation-2018-1046 — the 2018 FR was recast by Reg 2024/2509). Remaining: `he-mga.md`,
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
