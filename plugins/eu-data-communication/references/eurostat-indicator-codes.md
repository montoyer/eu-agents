# Eurostat — Indicator / Dataset Codes (2024)

Curated static reference for the `data-communication-eu` skills (`data-analyst`).
Eurostat dataset codes are stable identifiers but are occasionally renamed, split,
or discontinued. Read the code for a requested indicator from this file rather than
recalling it; **do not invent dataset codes** — an invented code produces a dead
SDMX query and an uncheckable figure.

Cite the data itself as `[Eurostat YYYY-MM — verify]` with the dataset code and
extraction month. Cite this file for the code mapping as
`(eurostat-indicator-codes.md — verify code on the Eurostat data browser)`.

SDMX REST base: `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/<code>`

---

## Macroeconomics

| Indicator | Dataset code |
|---|---|
| GDP and main components (national accounts) | `nama_10_gdp` |
| Government finance (deficit, debt) | `gov_10a_main` |
| Balance of payments — current account | `bop_c6_q` |
| Purchasing power parities | `prc_ppp_ind` |

## Labour market (LFS)

| Indicator | Dataset code |
|---|---|
| Unemployment rate by sex, age | `lfsa_urgan` |
| Employment rate by sex, age | `lfsa_ergan` |
| Employment by NUTS3 region | `lfst_r_lfe2emp` |
| Structure of earnings / gender pay gap | `earn_ses_pub` / `sdg_05_20` |

## Prices

| Indicator | Dataset code |
|---|---|
| HICP — monthly inflation (annual rate) | `prc_hicp_manr` |
| HICP — monthly index | `prc_hicp_midx` |

## Trade

| Indicator | Dataset code |
|---|---|
| EU trade in goods (product × partner × flow) — Comext | `DS-045409` (Comext) |
| EU trade with main partners (simplified) | `ext_lt_intertrd` |

## Social

| Indicator | Dataset code |
|---|---|
| At-risk-of-poverty rate | `ilc_li02` |
| People at risk of poverty or social exclusion (AROPE) | `ilc_peps01` |
| Gini coefficient of equivalised income | `ilc_di12` |

## Environment / energy

| Indicator | Dataset code |
|---|---|
| GHG emissions by sector (UNFCCC) | `env_air_gge` |
| Energy balances | `nrg_bal_c` |
| GHG emissions intensity of energy | `env_ac_aigg_q` |

## Innovation / R&D

| Indicator | Dataset code |
|---|---|
| R&D expenditure (GERD) by NUTS2 region | `rd_e_gerdreg` |
| Community Innovation Survey | `inn_cis12` |
| High-tech employment | `htec_emp_nat2` |

---

## Quality flags (always preserve in output)

`b` break in series · `p` provisional · `e` estimated · `c` confidential ·
`d` definition differs · `:` not available. Never present `p`/`e`/`:` data without
the flag (House Style, `data-communication-eu/CLAUDE.md`).

---

## Maintenance note

Verify any code on the Eurostat data browser before first use in a session — codes
such as `ilc_di01` (Gini) have been superseded (now `ilc_di12`). When Eurostat
renames or discontinues a dataset, update the row here and bump the filename year.
NUTS classification in use: **NUTS 2021** (as of 2024).
