---
type: correlation-group
id: CG-14
to: "[[HC-5 - Operative exposure behind the egg-cardiovascular association]]"
members:
  - "[[E-108 - O-41 x HC-5 — egg effect is a function of the comparator, not a fixed exposure]]"
  - "[[E-112 - O-58 x HC-5 — dietary cholesterol per se carries a monotonic dose-response]]"
  - "[[E-113 - O-60 x HC-5 — egg association vanishes on cholesterol adjustment]]"
---

Joint likelihood for correlated observations O-41, O-58, O-60 (shared basis: D-1). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-14 (HC-5) — ONE joint estimate over E-108 + E-112 + E-113: all three trace to the pooled US-cohort basis
# D-1 (Zhong's 6-cohort data behind O-58/O-60, and the substitution analysis O-41 drawing the same cohorts),
# so priced together as one witness (rule 1). Members [H-3, H-26, H-54]. Joint pattern: dietary cholesterol
# carries a monotonic +300 mg/day dose-response with CVD/mortality (O-58), the egg association goes
# non-significant specifically on cholesterol adjustment (O-60), and the egg-removal effect is entirely
# comparator-dependent, ranking eggs near processed meat (O-41). Anchored on H-26 = 1.0.
lik_chol_H26 = 1.0    # anchor: O-58 (cholesterol-per-se dose-response) and O-60 (egg signal removed by
                      # cholesterol adjustment specifically) are the exact signature of dietary cholesterol as
                      # the operative mediator (A-21, approved). O-41's comparator-dependence (A-13, approved:
                      # no unconditional egg effect is identified) is a substitution-algebra fact compatible with H-26.
lik_chol_H3 = 0.5     # 0.5x: under H-3, dietary cholesterol co-occurs with saturated fat, so O-58's dose-response
                      # and O-60's attenuation can reflect the correlated fat rather than cholesterol per se —
                      # accommodated, but adjustment on cholesterol *specifically* nulling the egg signal fits a
                      # cholesterol lever more cleanly than a fat one.
lik_chol_H54 = 0.45   # 0.45x: O-41 fits the artefact/substitution branch well, but O-60's cholesterol-specific
                      # attenuation is awkward for pure dietary-pattern confounding or a non-cholesterol component
                      # (A-21) — only partly rescued by dietary cholesterol itself proxying the unhealthy pattern.
t_chol = 0.57         # cap = min trust over {O-41 (S-89 0.62), O-58, O-60 (S-21 0.57)} = 0.57. Held at cap: the
                      # observed dose-response and attenuation are reliably reported; residual confounding is a
                      # truth question already reflected in S-21's score, and A-13 is a design caveat not a
                      # raw-data->observation weakness.
evidence("HC-5", ["O-41", "O-58", "O-60"], [lik_chol_H3, lik_chol_H26, lik_chol_H54], t=t_chol)
```
