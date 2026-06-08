# Example: Green Deal Package — Fit for 55

This example simulates the Commission's Fit for 55 package: 13 legislative proposals adopted in July 2021 to deliver a 55% net greenhouse gas emissions reduction by 2030.

---

## The package

| Proposal | Lead Commissioner | Status |
|---|---|---|
| ETS revision (more stringent cap) | EVP Green Deal | Adopted 2023 |
| CBAM (Carbon Border Adjustment) | EVP Green Deal + Trade | Adopted 2023 |
| CO2 standards for cars (2035 ban) | Transport | Adopted 2023 |
| RED III (45% renewables by 2030) | Energy | Adopted 2023 |
| EED (13% efficiency reduction) | Energy | Adopted 2023 |
| Land use (LULUCF revision) | EVP Green Deal + Agriculture | Adopted 2023 |
| Effort Sharing Regulation revision | EVP Green Deal | Adopted 2023 |
| ReFuelEU Aviation | Transport | Adopted 2023 |
| FuelEU Maritime | Transport | Adopted 2023 |
| Social Climate Fund | EVP Green Deal + Employment | Adopted 2023 |
| ETS 2 (buildings and road transport) | EVP Green Deal | Adopted 2023 |

---

## Simulate the College deliberation

```
/eu-simulation:college-deliberation "Fit for 55: adopt the 13-proposal package for simultaneous transmission to EP and Council"
```

**Expected tensions:**
- Agriculture Commissioner: LULUCF accounting puts pressure on land use — farmland implications must be addressed
- Regional Development Commissioner: Social Climate Fund must be adequately funded to ensure just transition
- EVP Economy: Package compliance costs are significant — needs serious SME test review
- Competition Commissioner: ETS 2 (buildings/road transport) — social impact on low-income households; carbon price volatility

---

## Simulate the 2035 ICE ban trilogue

```
/eu-simulation:trilogue "CO2 standards for cars and vans — 2035 zero-emission mandate"
```

**Historical fault lines:**
- Germany: Protected the e-fuels exemption (synthetic fuels for ICE vehicles after 2035)
- Italy: Automotive industry concerns (Ferrari exemption for small-volume manufacturers)
- EP: Hardliners wanted no e-fuels exemption; progressives accepted it as a compromise

**Key learning:** Germany's blocking power in Council (over 35% population threshold alone insufficient, but with Italy + Hungary → blocking minority credible) shaped the e-fuels compromise.

---

## The CBAM WTO question

```
/eu-legislative:treaty-check "Carbon Border Adjustment Mechanism — WTO compatibility"
```

```
/eu-trade:trade-defence-investigator "Is the CBAM compatible with WTO rules? What is the risk of WTO dispute settlement?"
```

**Key legal question:** Is the CBAM a legitimate environmental measure under GATT Art. XX(b) (necessary to protect human life or health) or Art. XX(g) (relating to conservation of exhaustible natural resources)? Or does it constitute a discriminatory trade barrier?

**Answer:** The CBAM's design (product-specific, based on embedded carbon content, with adjustment for equivalent carbon pricing in exporting country) is defensible under Art. XX GATT — but it will be contested and the WTO dispute is likely.
