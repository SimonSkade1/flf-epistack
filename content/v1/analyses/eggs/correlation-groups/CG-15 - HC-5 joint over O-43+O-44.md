---
type: correlation-group
id: CG-15
to: "[[HC-5 - Operative exposure behind the egg-cardiovascular association]]"
members:
  - "[[E-109 - O-43 x HC-5 — eggs co-occur with an unhealthy pattern (confounding structure)]]"
  - "[[E-110 - O-44 x HC-5 — egg association vanishes on lifestyle (not cholesterol) adjustment]]"
---

Joint likelihood for correlated observations O-43, O-44 (shared basis: D-7). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-15 (HC-5) — ONE joint estimate over E-109 + E-110: both rest on the Harvard-cohort basis D-7 (S-19), so
# priced together (rule 1). Members [H-3, H-26, H-54]. Joint pattern: higher egg intake tracks an unhealthier
# diet-lifestyle pattern (O-43), and the crude positive egg-CVD association (HR 1.10) reverses to null (0.93)
# specifically on lifestyle/co-consumed-food adjustment — NOT on cholesterol adjustment (O-44). This is the
# signature of dietary-pattern confounding. Anchored on H-54 = 1.0.
lik_confound_H54 = 1.0  # anchor: the crude->adjusted reversal on lifestyle covariates is exactly H-54's artefact
                        # branch (A-16, approved: association confounded by an unhealthy-eater pattern; A-17: an
                        # E-value ~1.43 confounder is needed to make it positive). The residual legitimately fits
                        # best here because the observation IS the confounding signature, not because it is unconstrained.
lik_confound_H3 = 0.6   # 0.6x: the lifestyle/diet adjustment set includes co-consumed saturated-fat foods, so the
                        # egg null after adjustment is partly consistent with H-3 (the accompanying fat, not egg
                        # per se, being the lever) — but H-3 does not specifically predict the reversal.
lik_confound_H26 = 0.5  # 0.5x: H-26 expects the egg signal to be carried by cholesterol and removed by cholesterol
                        # adjustment (cf O-60), whereas here it vanishes on lifestyle adjustment without needing
                        # cholesterol — the two attenuations implicate different operative accounts (E-110).
t_confound = 0.82       # cap = trust over {O-43, O-44} = S-19 0.82. Held at cap: well-conducted Harvard cohorts;
                        # residual confounding is a truth issue already in the score, no raw-data->observation weakness.
evidence("HC-5", ["O-43", "O-44"], [lik_confound_H3, lik_confound_H26, lik_confound_H54], t=t_confound)
```
