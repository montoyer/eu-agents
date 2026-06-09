# Example: Using the Staff Regulations reference from skills and agents

This worked example shows how skills in the `eu-institutional-management` and
`eu-careers` plugins use the **`staff-regulations` connector** — the full
authentic text of the Staff Regulations and the Conditions of Employment of
Other Servants (CEOS), stored as reference markdown and read at runtime.

Unlike the API-backed connectors (`eurostat`, `eur-lex`), `staff-regulations` is
a **`manual`** connector: there is no live endpoint. The text was retrieved once
from EUR-Lex (consolidated CELEX `01962R0031`, 01.01.2026), converted to
markdown, and split one file per Title and per Annex under
`plugins/eu-institutional-management/references/`. Skills quote the article text
directly from those files instead of reconstructing it from training data.

## Setup

```
/plugin marketplace add montoyer/eu-agents
/plugin install eu-institutional-management@eu-agents
```

No MCP server or API key is required — the files ship with the plugin.

---

## How a skill uses the reference

A skill does **not** load the whole corpus. It consults the index, opens the one
file covering the Title or Annex it needs, and quotes from it. The map lives in:

```
plugins/eu-institutional-management/references/staff-regulations-INDEX.md
```

Each skill's `SKILL.md` lists the specific files it should read in its **Reference
Guide** table. For example, `pmo-pension-specialist` points to:

| Topic | File |
|---|---|
| Accrual rate, 70% cap, invalidity/survivors | `../../references/staff-regulations-title-v-emoluments-and-social-security.md` |
| Pensionable service, actuarial reduction | `../../references/staff-regulations-annex-viii-pension-scheme.md` |
| 2014-reform transitionals | `../../references/staff-regulations-annex-xiii-transitional-measures.md` |
| Pay scales | `../../references/staff-regulations-annex-i-2026.md` |

When the skill states a figure, it cites the source inline:

```
[Staff Regulations Art. XX — EUR-Lex 01962R0031, 01.01.2026]
```

and for salary figures:

```
(SR Annex I 2026 — verify if after January 2027)
```

A figure **not** covered by any file still carries `[model knowledge — verify]`.

---

## Step 1 — Pension estimate (reads Annex VIII + Title V + Annex XIII)

```
/eu-institutional-management:pmo-pension-specialist

Estimate the pension for an official at grade AD11, retiring on 01/07/2026 after
35 years of service.
```

What the skill does:

1. Reads the **AD11** basic salary from `staff-regulations-annex-i-2026.md`.
2. Reads the accrual rule from `…-title-v-…` — **Art. 77 SR**: *"The maximum
   retirement pension shall be 70 % of the final basic salary… 1,80 % of that
   final basic salary shall be payable… for each year of service."*
3. Establishes the **entry-into-service cohort** — 35 years to mid-2026 means
   entry ~1991, a **pre-1 May 2004** official. It then reads
   `…-annex-xiii-transitional-measures.md` (Art. 21), which sets the accrual at
   **1,9 % per year** for that cohort — *not* the 1,80 % default.
4. Computes: 35 × 1,9 % = 66.5 % (under the 70 % cap → no reduction); retiring at
   full pensionable age → no actuarial reduction.

> **Why this matters:** the skill's at-a-glance parameter table says 1,80 %.
> Reading Annex XIII produces the *correct* pre-2004 rate of 1,9 %. The reference
> file changes the answer — that is the whole point of the connector.

The skill flags `[review — confirm entry-into-service date]` because the exact
date determines both the cohort rate and the pensionable age.

---

## Step 2 — Total compensation package (reads Annex I + CEOS)

```
/eu-institutional-management:financial-officer  (or head-of-unit / hr-contract-manager-ta)

What is the total monthly compensation for an AD7 Step 2 Head of Sector,
married with 2 dependent children, in Brussels, with no expatriation allowance?
Show gross and net.
```

What the skill does:

1. Reads **AD7 Step 2** basic salary from `staff-regulations-annex-i-2026.md`:
   `EUR 6,526.17`.
2. Builds family allowances from the same file's Annex VII section:
   - Household (Art. 1): `EUR 210.62 + 2% of basic`
   - Dependent child (Art. 2): `EUR 432.38 × 2`
3. Applies the deduction rates from the file: pension `10.10%`, JSIS `2.00%`,
   and the progressive Community-tax bands.
4. Notes "Head of Sector" is a **functional role, not a grade** → no salary
   supplement under the SR.

Result: gross ≈ `EUR 7,732.07/month`; net ≈ `EUR 6,058.96/month`.

### Variant — Temporary Agent (TA)

```
Same profile, but the person is a Temporary Agent (TA), not an official.
```

The skill reads `staff-regulations-ceos-conditions-of-employment.md` and finds:
- **CEOS Arts. 19–21**: TA remuneration and family allowances apply the SR Annex
  VII rules *by analogy* → **gross is identical** to an official.
- **CEOS Art. 41**: pension funded per SR Art. 83 by analogy → same 10.10%.
- The **0.81 % unemployment contribution** (Annex I, "temporary and contract
  agents only") now applies.

Net delta: TA nets ≈ `EUR 41/month` less than an official — the unemployment
contribution. This is a figure the skill could only get right by reading CEOS,
not from the generic "officials" parameter table.

---

## How another agent can reuse this

Any agent persona — not just the named skills — can read these files. A College
or ISC simulation that needs an HR or budget figure can instruct the relevant
sub-agent to:

```
Read plugins/eu-institutional-management/references/staff-regulations-INDEX.md,
open the file for the Title/Annex you need, and quote the article verbatim with
the citation [Staff Regulations Art. XX — EUR-Lex 01962R0031, 01.01.2026].
```

This keeps every HR/financial figure in a simulation traceable to the authentic
consolidated text rather than to model memory.

---

## Refreshing the reference (annual / on amendment)

Pay scales change every January; the consolidated text changes on each amendment.

| What changed | What to do |
|---|---|
| **Annual pay adjustment** (each January) | Replace `staff-regulations-annex-i-2026.md` with the new Council regulation figures; rename to the new year. |
| **New consolidation** of the SR/CEOS | Download the new EUR-Lex HTML, then re-run `references/.convert_sr.py` (the byte-offset boundaries in the script may need updating for the new file). |

After refreshing, the citation date (`01.01.2026`) in the file headers should be
bumped so outputs cite the correct consolidation.

---

## Key learnings from this example

1. **The connector changes answers, not just provenance.** The pre-2004 pension
   accrual (1,9 %) and the TA unemployment contribution (0.81 %) are both cases
   where reading the file produces a *different* number than the skill's built-in
   table — and the file is right.

2. **Read one file, not the corpus.** The INDEX maps Title/Annex → file so a
   skill loads only what it needs, keeping context small.

3. **`manual` ≠ unreliable.** A reference-backed connector with no live API still
   replaces `[model knowledge — verify]` with a dated, citable source.

4. **Citations stay traceable.** Every figure carries
   `[Staff Regulations Art. XX — EUR-Lex 01962R0031, 01.01.2026]` so a reviewer
   can check it against EUR-Lex.
