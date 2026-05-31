# Trade Defence — Calculation Method and Thresholds

Curated static reference for the `trade-eu` skills (`dumping-margin-calculator`,
`trade-defence-investigator`). These thresholds and methodology constants are set
by the Basic Regulations and WTO agreements — read them from this file; **do not
generate them from training data**.

Cite as: `(anti-dumping-method.md — verify against the current Basic Regulation)`.

Legal sources (verify current consolidated version on EUR-Lex):
- Basic Anti-Dumping Regulation — Reg. (EU) 2016/1036 `[EUR-Lex — verify current version]`
- Basic Anti-Subsidy Regulation — Reg. (EU) 2016/1037 `[EUR-Lex — verify current version]`
- Safeguards — Reg. (EU) 2015/478
- WTO Anti-Dumping Agreement (ADA), SCM Agreement, Safeguards Agreement

---

## De minimis and negligibility thresholds

| Threshold | Value | Legal basis |
|---|---|---|
| Dumping margin de minimis | **< 2%** of export price → margin treated as nil; investigation terminated for that exporter | Art. 9(3) BAR; ADA Art. 5.8 |
| Subsidy de minimis (general) | **< 1%** ad valorem | Art. 14(3) BAS |
| Subsidy de minimis (developing countries) | **< 2%** (and **< 3%** / **< 4%** special cases per SCM Annex VII) | SCM Art. 11.9, 27.10 |
| Negligible import volume — single country | **< 1%** of EU consumption (unless countries < 1% collectively exceed 3%) | Art. 5(7) BAR; ADA Art. 5.8 |
| Negligible imports — developing-country cumulation | collectively **< 3%** of imports | ADA Art. 5.8 |

---

## Constructed normal value (Art. 2(3), (6) BAR)

```
Constructed normal value = Cost of production + SGA + Profit
  SGA (selling, general & administrative): actual, or a reasonable amount
  Profit: actual on ordinary-course domestic sales, or a reasonable amount
```

There is **no fixed statutory 2% minimum** for SGA/profit in Reg. 2016/1036; use
actual amounts where representative, otherwise a reasonable amount under Art. 2(6).
(If a SKILL body states a "min. 2%" floor, treat that as a drafting shortcut and
defer to Art. 2(6) — flag for correction.)

---

## Dumping margin

```
Dumping margin (per PCN) = (Normal Value − Export Price) / Export Price × 100%
Overall exporter margin  = weighted average of PCN margins (weighted by export quantity)
```

Fair comparison adjustments under Art. 2(10): level of trade, transport,
insurance, handling, credit, commissions, currency conversion.

---

## Lesser duty rule (Art. 7(2) / Art. 9(4) BAR)

```
Definitive duty = min(dumping margin, injury margin)
Injury (underselling) margin = (target price − weighted-avg import price) / CIF price × 100%
```

The EU applies the lesser duty rule as a legal obligation (subject to the raw
materials / Art. 7(2a) distortion exception, which can disapply it).

---

## Measure duration

| Item | Value |
|---|---|
| Definitive measures — standard duration | 5 years (Art. 11(2) BAR) |
| Provisional measures — maximum | 6 months (extendable to 9) (Art. 7(7)) |
| Expiry / interim review trigger | on request or own-initiative before expiry |

---

## Maintenance note

Update this file when the Basic AD/AS Regulations are amended (last major reform:
the 2017/2321 "new methodology" and 2018/825 "modernisation" packages). Refresh the
thresholds above and re-verify the Article numbers. Cite as
`(anti-dumping-method.md — verify against the current Basic Regulation)`.
