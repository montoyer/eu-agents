# Connectors — EU Data Sources

This file lists the MCP connectors available for the `agents-for-EU` plugins.
Connectors enable skills to retrieve live data from authoritative EU sources
rather than relying solely on model training data.

Each connector is optional. Skills work without connectors, but outputs will
carry `[model knowledge — verify]` tags on any figure or legal text not retrieved
live. With connectors active, the relevant tags are replaced with dated source
citations.

---

## Status

> **No connector is wired yet.** No MCP server is configured in this repository,
> so every connector below is currently **`planned`** — declaring a connector in a
> plugin's `plugin.json` does *not* mean live data is being retrieved. Skills that
> reference a connector (e.g., `connector: eur-lex` in a SKILL workflow) degrade
> gracefully: they emit `[model knowledge — verify]` / `[EUR-Lex — verify current
> version]` tags and, where a curated `references/*.md` file exists, read static
> figures from that file instead. Treat every connector as planned until this table
> says otherwise.

| Connector | Status | Auth | Backed by `references/*.md` fallback |
|---|---|---|---|
| `eur-lex` | planned | none | — |
| `eurostat` | planned | none | — |
| `ted-ojeu` | planned | API key | `eu-grants-enforcement/references/procurement-thresholds-2024.md` |
| `comitology-register` | planned | none | — |
| `rapid` | planned | none | — |
| `eu-open-data-portal` | planned | none | — |
| `oj-state-aid-register` | planned | none | `eu-competition/references/gber-de-minimis-2024.md` |
| `f-and-t-portal` | planned | EU Login | — |
| `chap` | planned | EU Login (intranet) | — |
| `epso-eu` | planned | none | `eu-careers/references/staff-regulations-annex-i-2026.md` |
| `staff-regulations` | manual | none | `eu-institutional-management/references/staff-regulations-*.md` |
| `sysper` | planned | EU Login (intranet) | — |
| `abac` | planned | EU Login (intranet) | — |
| `edps-register` | planned | none | — |
| `comext` | planned | none | `eu-trade/references/anti-dumping-method.md` |

**Status legend** — `live`: an MCP server is configured and the connector returns
data; `manual`: no API, retrieval is via a documented manual step; `planned`:
declared but not wired (current state of all connectors).

---

## Available Connectors

### `eur-lex`
**EUR-Lex — EU Law and Official Journal**

Retrieves the current consolidated text of EU regulations, directives, decisions,
and international agreements. Enables skills to quote the legally current version
of any cited legal act rather than the training-data version.

- Source: `https://eur-lex.europa.eu/`
- API: EUR-Lex SPARQL endpoint + REST search API
- Used by: `eu-legislative`, `eu-competition`, `eu-trade`, `eu-grants-enforcement`
- Primary use cases:
  - Retrieve current consolidated text of the Basic AD Regulation (2016/1036)
  - Retrieve current GBER (651/2014 as amended)
  - Retrieve current Financial Regulation (2018/1046 as amended)
  - Retrieve treaty articles (TFEU/TEU)
  - Search for recent OJ publications (Notices of Initiation, State aid decisions)

```json
{
  "connector": "eur-lex",
  "endpoint": "https://eur-lex.europa.eu/rest/sparql",
  "auth": "none",
  "rate_limit": "10 req/min (unauthenticated)"
}
```

---

### `eurostat`
**Eurostat — EU Statistical Office**

Retrieves current statistical data from Eurostat databases using the SDMX REST
API. Enables the `data-analyst` skill to pull live data with an accurate
extraction date, replacing `[model knowledge — verify]` tags with
`[Eurostat YYYY-MM — extracted]`.

- Source: `https://ec.europa.eu/eurostat/`
- API: Eurostat SDMX-JSON REST API
- Used by: `eu-data-communication`, `eu-legislative` (economist skill)
- Primary use cases:
  - Labour market statistics (LFS — `lfsa_urgan`, `lfsa_ergan`)
  - GDP and national accounts (`nama_10_gdp`)
  - Trade statistics (`ext_lt_intertrd`)
  - Inflation / HICP (`prc_hicp_manr`)
  - Social indicators — poverty, Gini (`ilc_li02`, `ilc_di01`)
  - Environmental indicators (`env_air_gge`)

```json
{
  "connector": "eurostat",
  "endpoint": "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/",
  "auth": "none",
  "format": "JSON (SDMX-JSON)"
}
```

---

### `ted-ojeu`
**TED — Tenders Electronic Daily / Official Journal (Supplement)**

Monitors the Official Journal Supplement for new procurement notices, contract
award notices, and trade defence Notices of Initiation. Enables the
`trade-defence-investigator` and `procurement-expert` skills to check for
current publications.

- Source: `https://ted.europa.eu/`
- API: TED API v3 (search and retrieve notices)
- Used by: `eu-trade`, `eu-grants-enforcement`
- Primary use cases:
  - Retrieve published Notices of Initiation (AD/CVD investigations)
  - Monitor contract award notices in a sector
  - Check current procurement thresholds (via OJ S)

```json
{
  "connector": "ted-ojeu",
  "endpoint": "https://ted.europa.eu/api/v3.0/notices/search",
  "auth": "API key (register at https://ted.europa.eu/api)",
  "rate_limit": "100 req/min (authenticated)"
}
```

---

### `comitology-register`
**Comitology Register — Council/Commission**

Retrieves published committee opinions, delegated act notifications, and EP
scrutiny status. Enables the `comitology-officer` skill to check the current
status of a delegated or implementing act.

- Source: `https://comitology.consilium.europa.eu/`
- API: Comitology Register public search (scrape / RSS)
- Used by: `eu-legislative`
- Primary use cases:
  - Check committee opinion outcome for a specific DA/IA
  - Retrieve EP objection status for a delegated act
  - Monitor appeal committee referrals

```json
{
  "connector": "comitology-register",
  "endpoint": "https://comitology.consilium.europa.eu/en/searchresults.html",
  "auth": "none (public search)",
  "notes": "No formal REST API; use RSS feed or scrape search results"
}
```

---

### `rapid`
**RAPID — European Commission Press Release Database**

Retrieves published press releases, Commissioner speeches, and infringement
decision announcements. Enables the `communication-officer` skill to check
existing Commission communication on a topic before drafting new materials.

- Source: `https://ec.europa.eu/commission/presscorner/`
- API: RAPID search API (full-text search)
- Used by: `eu-data-communication`
- Primary use cases:
  - Check existing Commission press releases on a topic
  - Retrieve the standard phrasing for a recurring announcement type
  - Check infringement decision announcements

```json
{
  "connector": "rapid",
  "endpoint": "https://ec.europa.eu/commission/presscorner/api/documents",
  "auth": "none",
  "notes": "Full-text search available; returns press release metadata and text"
}
```

---

### `eu-open-data-portal`
**EU Open Data Portal**

Accesses datasets published by the Commission and EU agencies on the
European Data Portal. Supplements Eurostat for datasets not available
through the SDMX API (e.g., JRC datasets, DG ENV monitoring data).

- Source: `https://data.europa.eu/`
- API: DCAT-AP REST API
- Used by: `eu-data-communication`
- Primary use cases:
  - JRC analytical datasets (energy, environment, industry)
  - DG ENV biodiversity and environmental quality monitoring data
  - Copernicus climate data published through the portal

```json
{
  "connector": "eu-open-data-portal",
  "endpoint": "https://data.europa.eu/api/hub/search/",
  "auth": "none"
}
```

---

### `oj-state-aid-register`
**Official Journal — State Aid Register**

Searches the State Aid Register for published Commission decisions on state
aid cases. Enables the `lawyer-state-aid` skill to check precedent decisions
for comparable aid schemes.

- Source: `https://competition-cases.ec.europa.eu/`
- API: Competition Cases Portal search
- Used by: `eu-competition`
- Primary use cases:
  - Retrieve Commission decisions on comparable state aid schemes
  - Check whether a specific SA case number has a published decision
  - Find recent block exemption compatibility decisions

```json
{
  "connector": "oj-state-aid-register",
  "endpoint": "https://competition-cases.ec.europa.eu/cases",
  "auth": "none (public portal)"
}
```

---

### `f-and-t-portal`
**Funding and Tenders Portal (F&T Portal)**

Connects to the Commission's Funding and Tenders Portal for Horizon Europe
grant management. Enables the `grant-manager` skill to retrieve grant agreement
details, submission deadlines, and beneficiary data.

- Source: `https://ec.europa.eu/info/funding-tenders/`
- API: F&T Portal REST API (authenticated)
- Used by: `eu-grants-enforcement`
- Primary use cases:
  - Retrieve grant agreement financial data
  - Check reporting deadlines
  - Access work programme provisions for eligibility assessment

```json
{
  "connector": "f-and-t-portal",
  "endpoint": "https://api.research-and-innovation.ec.europa.eu/",
  "auth": "EU Login (OAuth 2.0)",
  "notes": "Requires authenticated Commission staff or beneficiary credentials"
}
```

---

### `chap`
**CHAP — Complaints Handling and Anti-Pollution**

Accesses the Commission's complaints management system for infringement
pre-screening. Enables the `infringement-officer` skill to check the status
of a complaint before opening EU Pilot or drafting formal correspondence.

- Source: Internal Commission system — not publicly accessible
- Access: Commission intranet only
- Used by: `eu-grants-enforcement`
- Primary use cases:
  - Check complaint status (registered, in EU Pilot, closed)
  - Retrieve complainant information for correspondence
  - Link infringement case to the originating CHAP complaint

```json
{
  "connector": "chap",
  "endpoint": "internal — Commission intranet access only",
  "auth": "EU Login + Commission network access",
  "notes": "External deployment of this plugin cannot use this connector"
}
```

---

### `epso-eu`
**EPSO — European Personnel Selection Office**

Retrieves published competition notices, reserve list status, and the current
Staff Regulations pay tables. Enables the `eu-careers` skills to check live
competition timelines and grade requirements.

- Source: `https://eu-careers.europa.eu/`
- API: no public REST API — competition notices published as OJ C-series
- Used by: `eu-careers`
- Fallback when planned: read pay-scale figures from
  `eu-careers/references/staff-regulations-annex-i-2026.md`; do not generate them

```json
{
  "connector": "epso-eu",
  "endpoint": "https://eu-careers.europa.eu/en/job-opportunities",
  "auth": "none",
  "notes": "No REST API; competition notices via OJ C-series / EPSO account"
}
```

---

### `staff-regulations`
**Staff Regulations & CEOS — Consolidated Text (CELEX 01962R0031)**

The full authentic text of the Staff Regulations of Officials and the Conditions
of Employment of Other Servants, split one markdown file per Title and per Annex.
Unlike the API-backed connectors above, this is **`manual`**: there is no live
endpoint — the text is retrieved once from EUR-Lex, converted to markdown, and
read from `references/*.md`. Skills quote the article text directly and tag it
`[Staff Regulations Art. XX — EUR-Lex 01962R0031, 01.01.2026]` instead of
`[model knowledge — verify]`.

- Source: `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01962R0031`
- API: none — consolidated HTML downloaded and converted offline
- Used by: `eu-institutional-management`, `eu-careers`
- Index: `eu-institutional-management/references/staff-regulations-INDEX.md`
- Primary use cases:
  - Quote the current wording of an SR/CEOS article in an HR decision
  - Disciplinary procedure (Title VI + Annex IX) and underperformance (Title III §4)
  - Pension scheme (Annex VIII), pension contribution method (Annex XII)
  - Leave entitlements (Title IV + Annex V), allowances (Annex VII)
- Refresh: when a new consolidation is published, download the new EUR-Lex HTML
  and re-run `references/.convert_sr.py` (offsets may need updating).

```json
{
  "connector": "staff-regulations",
  "endpoint": "manual — references/staff-regulations-*.md (CELEX 01962R0031, consol. 01.01.2026)",
  "auth": "none",
  "notes": "No live API; full text converted from EUR-Lex HTML. Pay scales remain in staff-regulations-annex-i-2026.md (updated each January)."
}
```

---

### `sysper`
**Sysper — Commission HR Management System**

Internal Commission HR system. Enables `eu-institutional-management` skills to
retrieve staff records, leave balances, and appraisal (CDR) data.

- Source: Internal Commission system — not publicly accessible
- Access: Commission intranet only
- Used by: `eu-institutional-management`
- Fallback when planned: no live access outside the Commission network; all
  figures carry `[model knowledge — verify]`

```json
{
  "connector": "sysper",
  "endpoint": "internal — Commission intranet access only",
  "auth": "EU Login + Commission network access",
  "notes": "External deployment of this plugin cannot use this connector"
}
```

---

### `abac`
**ABAC — Commission Accounting / Budget Execution System**

Internal Commission financial system. Enables `eu-institutional-management`
skills (financial-officer) to check commitment/payment appropriations and
budget line balances.

- Source: Internal Commission system — not publicly accessible
- Access: Commission intranet only
- Used by: `eu-institutional-management`
- Fallback when planned: no live access outside the Commission network

```json
{
  "connector": "abac",
  "endpoint": "internal — Commission intranet access only",
  "auth": "EU Login + Commission network access",
  "notes": "External deployment of this plugin cannot use this connector"
}
```

---

### `edps-register`
**EDPS — Register of Records (Art. 31 EUDPR)**

Searches the public register of processing records and prior consultations.
Enables `eu-privacy` skills to check whether a comparable processing activity
has an existing record or a prior EDPS consultation.

- Source: `https://www.edps.europa.eu/`
- API: no formal REST API — public register search
- Used by: `eu-privacy`
- Fallback when planned: DPIA threshold and Art. 39 EUDPR criteria applied from
  model knowledge with `[EUR-Lex — verify current version]` tags

```json
{
  "connector": "edps-register",
  "endpoint": "https://www.edps.europa.eu/data-protection/our-work/publications",
  "auth": "none",
  "notes": "No REST API; public register search / scrape"
}
```

---

### `comext`
**Comext — Eurostat International Trade Database**

Detailed EU external trade statistics at product (CN/HS) level. Enables the
`trade-defence-investigator` skill to check import volumes, values, and trends
for a product under investigation.

- Source: `https://ec.europa.eu/eurostat/web/international-trade-in-goods/data/database`
- API: Eurostat SDMX REST API (Comext datasets, e.g., `DS-045409`)
- Used by: `eu-trade`
- Fallback when planned: anti-dumping duty calculation method and de minimis
  thresholds read from `eu-trade/references/anti-dumping-method.md`

```json
{
  "connector": "comext",
  "endpoint": "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/",
  "auth": "none",
  "format": "JSON (SDMX-JSON) — Comext product-level datasets"
}
```

---

## Connector Configuration

To activate connectors, add them to your Claude Code settings or the relevant
plugin's `.claude-plugin/plugin.json` `"connectors"` array, then configure the
MCP server:

```bash
# Example: add the EUR-Lex connector to your Claude Code MCP config
claude mcp add eur-lex --connector eur-lex --endpoint "https://eur-lex.europa.eu/rest/sparql"
```

See the [Claude Code MCP documentation](https://docs.anthropic.com/claude-code/mcp)
for full connector setup instructions.

---

## Which Plugin Uses Which Connectors

| Connector | legislative | competition | inst-mgmt | trade | grants-enf | data-comm | careers | privacy |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `eur-lex` | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ |
| `eurostat` | ✓ | — | — | — | — | ✓ | — | — |
| `ted-ojeu` | — | — | — | ✓ | ✓ | — | — | — |
| `comitology-register` | ✓ | — | — | — | — | — | — | — |
| `rapid` | — | — | — | — | — | ✓ | — | — |
| `eu-open-data-portal` | — | — | — | — | — | ✓ | — | — |
| `oj-state-aid-register` | — | ✓ | — | — | — | — | — | — |
| `f-and-t-portal` | — | — | — | — | ✓ | — | — | — |
| `chap` | — | — | — | — | ✓ | — | — | — |
| `epso-eu` | — | — | — | — | — | — | ✓ | — |
| `staff-regulations` | — | — | ✓ | — | — | — | ✓ | — |
| `sysper` | — | — | ✓ | — | — | — | — | — |
| `abac` | — | — | ✓ | — | — | — | — | — |
| `edps-register` | — | — | — | — | — | — | — | ✓ |
| `comext` | — | — | — | ✓ | — | — | — | — |

(`eu-simulation` declares no connectors — it is a pure model-knowledge simulation.)
