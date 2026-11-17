# TODO

Improvements and future change requests.

---

## Bluebook trainee skills to build

- [ ] `/briefing-note` — Draft a 1-page briefing note in standard Commission format (issue / context / options / recommendation)
- [ ] `/meeting-minutes` — Produce structured minutes with action points, owners, and deadlines in EU style
- [ ] `/mission-order` — Draft and submit a mission order in SYSPER; per diem rules, travel booking, reimbursement
- [ ] `/policy-brief` — Produce a 4-page policy brief: problem, evidence, options, recommendation
- [ ] `/ares-guide` — Step-by-step guide to creating, routing, and archiving documents in ARES
- [ ] `/eu-jargon-buster` — Decode EU acronyms and jargon on demand (ISC, SWD, OLP, QMV, RPS, HoU, etc.)
- [ ] `/end-of-traineeship-report` — Draft the mandatory end-of-traineeship report in the expected format
- [ ] `/executive-summary` — Condense a lengthy policy document into a 1-page executive summary
- [ ] `/sensitive-redaction` — Identify and redact personal data or sensitive commercial information before publication

---

## Marketplace

- [ ] After next stable release: add `sha` commit hash to each plugin source entry in `.claude-plugin/marketplace.json` to pin users to a specific version. Run `git rev-parse HEAD` after pushing, copy hash into each plugin's `sha` field.

---

## Roadmap — repo quality review (2026-06-10)

### Broken / inconsistent (fix first)

- [x] `eu-privacy` and `eu-careers` declare `"post_output": "hooks/post-output-disclaimer.sh"` in their `plugin.json` but have no `hooks/` directory — the path resolves to nothing. Add the symlink dirs (as in the other 7 plugins) or drop the manifest entry. *(Done: symlink dirs created, 2026-06-10.)*
- [x] Root `marketplace.json` is stale: it lists 7 plugins by display name and is missing `eu-privacy` and `eu-careers`; `.claude-plugin/marketplace.json` has all 9. Pick one source of truth (likely `.claude-plugin/`) and delete or auto-generate the other. *(Done 2026-06-10: legacy root file deleted — it also claimed MIT instead of EUPL and pointed at the wrong repo URL; `.claude-plugin/marketplace.json` is the single registry. README and CONTRIBUTING updated.)*
- [x] Hook registration is non-functional — verified against the plugins reference (code.claude.com/docs/en/plugins-reference), 2026-06-10: invented event names, wrong schema (flat `{event: path}` map instead of `hooks/hooks.json`), and scripts written as stdin→stdout text transformers, a capability Claude Code hooks don't have. *(Done 2026-06-10: `hooks` key dropped from all 9 manifests; no-op disclaimer hook deleted (templates + validate.sh check 2 already enforce the disclaimer); legal-basis and subsidiarity hooks rewritten as `plugins/eu-legislative/hooks/hooks.json` — `PostToolUse`/`Skill` matcher, JSON payload in, `additionalContext` out, scripts vendored in-plugin via `${CLAUDE_PLUGIN_ROOT}`; `lib/` removed; validate.sh check 4 now verifies hooks.json commands; CONTRIBUTING/README/CLAUDE.md/faq updated.)*
- [x] Cross-tree symlinks break on marketplace install: `plugins/*/hooks/*.sh → ../../../lib/hooks/` and `plugins/eu-careers/references/staff-regulations-annex-i-2026.md → ../../eu-institutional-management/...` point outside the plugin directory, but the marketplace `git-subdir` source only fetches the plugin's own subtree. *(Done 2026-06-10: zero symlinks remain — hooks vendored into eu-legislative; the eu-careers reference is now a machine-managed copy via `scripts/sync-shared-references.sh` with a drift check in validate.sh check 6, so the single-source-of-truth maintenance concern is handled by tooling, not by hand.)*
- [ ] Cited-but-missing reference citations — **132 remaining**, down from 189 at review time — full annotated list and phased plan in [docs/reference-backlog.md](docs/reference-backlog.md):
  - [x] Phase 1 — alias consolidation *(Done 2026-06-10: 160 → 138 unique files; naming convention documented in CONTRIBUTING § 3a; `isg.md` identified as the Interinstitutional Style Guide, kept distinct)*
  - [x] Phase 2 — all 11 Tier-1 primers written *(Done 2026-06-10: BR Toolbox Dec 2025 + subsidiarity-protocol + JPG + eu-charter (+sync) verified against official PDFs; comitology-reg-182-2011 verified verbatim via the Publications Office Cellar API; BR Guidelines verified against SWD(2021) 305; tfeu-teu-consolidated canonical + 2 synced copies; cjeu-legal-basis Curia-tagged)*
  - [ ] Phase 3 — thematic packs: **BR/IA pack done** *(2026-06-10: 10 files written from the verified Dec 2025 Toolbox PDFs; only `cjeu-subsidiarity-caselaw.md` left from that pack)*. Remaining: eu-legislative comitology/drafting/procedure/economist packs; eu-competition antitrust/state-aid/merger/litigation packs; eu-grants infringement/grants/procurement packs; eu-data-communication comms pack
  - [ ] Phase 4 — strip ~18 internal-system/portal citations (ARES, ABAC, SANI2, FNT, CHAP, …) and cross-domain strays; then flip pre-commit to `validate.sh --strict`
- [x] Broken link in `docs/getting-started.md:98`: `../examples/` should be `examples/` (examples live at `docs/examples/`). *(Done 2026-06-10.)*

### Dead code / housekeeping

- [x] `lib/hooks/post_tool_use_citation_matcher.sh` and `post_tool_use_eurlex_resolver.sh` are referenced only in README and registered in no plugin manifest — wire them up or remove them. *(Done 2026-06-10: removed, with README tree updated; recoverable from git history if a working hook mechanism lands.)*
- [x] `lib/legacy-skills/` is empty but still documented in CLAUDE.md as "pending conversion" — delete the dir and the directory-conventions row. *(Done 2026-06-10: dir removed; rows dropped from CLAUDE.md, README, CONTRIBUTING.)*
- [x] `plugins/eu-institutional-management/references/.convert_sr.py` is an untracked hidden file — move to `scripts/` (it's repo tooling, like `extract-skills.py`) and commit, or delete if the staff-regulations conversion is final. *(Done 2026-06-10: now tracked as `scripts/convert-staff-regulations.py`, reads/writes the references dir, fails gracefully when the gitignored source HTML is absent.)*
- [x] `site/prompts.json` is tracked but regenerated by CI and already drifts from the generator output — either stop tracking it or add a CI check that fails on drift. *(Done 2026-06-10: untracked and gitignored — drift was only the `generated` timestamp; CI rebuilds it for Pages, run `extract-skills.py` before `serve.py` locally.)*
- [x] Extend `scripts/validate.sh`: check that every `hooks` path declared in `plugin.json` exists, and that no in-plugin symlink escapes the plugin root (catches the two classes of bug above). *(Done: checks 4 and 5 added, 2026-06-10. Missing hook paths and dangling symlinks are hard errors; escaping symlinks are soft warnings, promoted by `--strict`.)*

### Verified healthy (no action)

- CLAUDE.md skill listing is 100% in sync with the 98 on-disk skills; all 9 `plugin.json` skill registries match disk.
- Every SKILL.md has `name`/`description` frontmatter and a DRAFT disclaimer.
- 27 portfolio files match `knowledge/roster.yml` (validate.sh check 8 since 2026-11-17); the shortname grid and the `/commissioner` table were regenerated from the roster.
- `knowledge/member-states.yml` totals (check 9) and DG/institution headers (check 10) since 2026-11-17.
- `validate.sh` + `.githooks/pre-commit` + Pages CI pipeline all run clean (hard checks).


---

## Site: commissioners page (`site/commissioners.html`)

Moved here from the page footer, 2026-11-17.

- [ ] Fetch each Commissioner's latest X post instead of quoting hand-copied ones
- [ ] Fill in X handles and agent shortnames for all 27 members (23 rows have neither)
- [ ] Quote a real post on the Ribera card, or drop the card

---

## EU simulation architecture (agreed 2026-11-17)

The prompt library is the funnel to montoyer.com; the full simulation runs in
Claude Code from the knowledge base. Commissioners speak one by one in a single
conversation; parallel subagents are not needed.

- [x] Phase 1 — `knowledge/` synced into `plugins/eu-simulation/knowledge/` (drift check in validate.sh check 6, cited paths in check 7); College command named `college-deliberation` everywhere in this repo; majority rule stated as Art. 250 TFEU instead of 11/21; workflow entries dropped from the library
- [ ] Outside this repo: fix `/college-deliberate` on the montoyer.com landing page and `/simulation-eu:` on the published simulation pages; reword "21 Commissioner personas running in parallel"
- [ ] Phase 2 — knowledge (two follow-ups open below)
  - [x] The real 2024–2029 College as 27 portfolio files (by portfolio, never by name), each with a YAML header (`id`, `rank`, `title`, `lead_dgs`, `treaty_basis`, `as_of`, `verified: false`); the 21 generic files removed, their shortnames kept as aliases (2026-11-17)
  - [x] `knowledge/roster.yml`: ids, titles, ranks, aliases, EVP steering, quorum and majority (14 of 27); synced into the plugin; validate.sh check 8 keeps roster and files in step
  - [x] College skills, `/commissioner` table, shortname grid, DG profiles, docs and site page moved to the 27 portfolios; Art. 17(6)(c) TEU "President imposes a decision" error corrected
  - [x] Extractor appends the roster to the five simulation prompts that cite it, and drops the plugin-only "Knowledge files" note
  - [x] Checked against official sources (2026-11-17): titles and ranks against the College page; EVP guidance and lead DGs against the 26 mission letters of 17 September 2024 (three steering errors fixed: Health under the Clean Transition EVP, Defence and Space under Tech Sovereignty only, Mediterranean also under Social Rights for demography; digital euro moved to Economy; DIGIT to Tech Sovereignty; DGT and SCIC to Budget); College voting rule against Decision (EU) 2024/3080. Each persona header now has `checked:`; `verified` stays false because priorities and dossiers are model knowledge
  - [ ] Verify each persona's priorities and key dossiers against live sources (Commission Work Programme 2026, Legislative Observatory), then set `verified: true` per file
  - [x] `knowledge/member-states.yml`: 2026 populations from Council Decision (EU, Euratom) 2025/2427 (Annex III), EP seats, euro membership, presidencies to 2030; validate.sh check 9 checks the totals; QMV skills read it and the extractor appends the table to the four Council prompts. qmv-calculator rewritten: abstentions count as not in favour, reinforced QMV and Art. 238(3) corrected
  - [ ] Replace the population block with the 2027 Annex III when the Council adopts it (expected late 2026, applies from 1 January 2027)
  - [x] YAML headers on all DG and institution files; validate.sh check 10 keeps each DG's `supports` in step with the portfolios' `lead_dgs`
  - [x] Missing actors: Secretariat-General, Legal Service, Regulatory Scrutiny Board (`knowledge/dgs/`), Member States and national parliaments (`knowledge/institutions/`); DG profiles for ECFIN, CLIMA, DEFIS, ENEST, MENA, INTPA, FISMA, MARE, EAC, ECHO; yellow-card arithmetic in subsidiarity-stress corrected to votes (18 of 54)
  - [x] `knowledge/agents/` and `knowledge/workflows/` merged into `knowledge/procedures/`; EDPS moved to `knowledge/institutions/`
  - [ ] Worked examples in `docs/examples/` still use the 2019–2024 portfolio names (left as historical records)
- [ ] Phase 3 — engine: consolidate simulation skills 16 → 13 (`college` absorbs college-decision; `council` absorbs coreper and council-presidency; new `dg` actor); every session writes `simulation.json` in the montoyer.com format; JSON schema and a self-contained validator in this repo; "Simulate this" links on the commissioners page
- [ ] Phase 4 — MCP server exposing the knowledge base, so claude.ai users can run a full simulation without a terminal
