---
type: correlation-group
id: CG-18
to: "[[HC-5 - Operative exposure behind the egg-cardiovascular association]]"
members:
  - "[[E-120 - O-103 x HC-5 — egg choline feeds the TMAO pathway dose-dependently]]"
  - "[[E-121 - O-105 x HC-5 — egg-TMAO rise is transient, not a sustained exposure]]"
---

Joint likelihood for correlated observations O-103, O-105 (shared basis: S-47). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-18 (HC-5) — ONE joint estimate over E-120 + E-121: both rest on S-47 (Miller 2014 dose-response), so priced
# together (rule 1). Members [H-3, H-26, H-54]. Joint pattern: egg ingestion raised plasma/urine TMAO
# dose-dependently (~11-15% of egg choline converted, O-103), but the rise was an acute postprandial flux
# (peak 6-8 h), not a fasting steady-state change (O-105). It demonstrates the non-cholesterol choline->TMAO
# pathway is real in humans (pro-H-54) while showing it is transient, not a sustained exposure (pro-H-26/H-3).
# The two halves largely offset, leaving a weak net tilt to H-54's mechanistic demonstration. Anchored on H-54 = 1.0.
lik_eggtmao_H54 = 1.0  # anchor: a clean dose-dependent human egg-choline->TMAO conversion is most directly
                       # expected if a non-cholesterol egg component is the operative agent.
lik_eggtmao_H26 = 0.8  # 0.8x, near the anchor: the conversion pathway existing is mildly unexpected under
                       # cholesterol-operative, but O-105's transience (single-meal flux, no steady-state change)
                       # largely offsets it, and A-40 (approved) notes the postprandial spike leaves hsCRP/oxLDL
                       # unmoved, so it does not establish a durable harmful exposure.
lik_eggtmao_H3 = 0.8   # 0.8x: identical reasoning — the choline route does not separate fat- from
                       # cholesterol-operative, and the transience is equally reassuring for H-3.
t_eggtmao = 0.73       # cap = trust over {O-103, O-105} = S-47 0.73. Held at cap: n=6 is small, but the
                       # within-subject dose-response (urinary TMAO 236->944 umol/24h, P<0.01) is internally
                       # consistent and the postprandial-timing fact (O-105) is a robust design feature.
evidence("HC-5", ["O-103", "O-105"], [lik_eggtmao_H3, lik_eggtmao_H26, lik_eggtmao_H54], t=t_eggtmao)
```
