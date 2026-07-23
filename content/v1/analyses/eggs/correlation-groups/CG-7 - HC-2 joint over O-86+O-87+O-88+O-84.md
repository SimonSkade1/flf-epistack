---
type: correlation-group
id: CG-7
to: "[[HC-2 - Regional-population modification of the egg-cardiovascular association]]"
members:
  - "[[E-123 - O-86 × HC-2 — PURE multi-region null consistent across regions]]"
  - "[[E-124 - O-87 × HC-2 — PURE MI signal not replicated in ONTARGET]]"
  - "[[E-125 - O-88 × HC-2 — PURE heterogeneity is NS subgroup not region]]"
  - "[[E-129 - O-84 × HC-2 — regional exposure-range variation, none above 1 egg per day]]"
---

Joint likelihood for correlated observations O-86, O-87, O-88, O-84 (shared basis: S-91). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-7 (HC-2) — ONE joint estimate over E-123 (O-86) + E-124 (O-87) + E-125 (O-88) + E-129 (O-84): all four
# rest on PURE / S-91 (rule 1). Members in HC-2.hypotheses order [H-7 Asian inverse is healthy-user/residual
# confounding (no genuine modification), H-22 genuine region effect-modification, H-50 residual: other origin
# (exposure-range/measurement/chance)]. The whole PURE pattern judged jointly: a 50-country cohort with
# center-random-intercept region adjustment finds NO significant egg-CVD association, "consistent across
# geographic regions" (O-86); the only clinical signal (MI HR 0.84) is flagged a multiple-testing artefact
# and NOT replicated in ONTARGET/TRANSCEND (O-87); the sole heterogeneity signal (prevalent-CVD subgroup) is
# NS (P-interaction 0.24) and not reproduced (O-88); and the exposure contrast spans only ~none to ~1.2
# egg/day (O-84). Anchored on H-7 = 1 (best fit); others priced as ratios (rule 7).
lik_pure_H7  = 1.0   # anchor: "no genuine modification, the salient Asian inverse is not robust" predicts
                     # exactly a well-adjusted multi-region null that is consistent across regions, with the
                     # apparent protective signals evaporating on replication — PURE's whole pattern
lik_pure_H22 = 0.5   # 0.5×: genuine region-modification predicts a detectable Asian inverse within PURE's
                     # Asian samples (China 5.6/wk, South Asia 1.4/wk) plus region heterogeneity; PURE reports
                     # consistency across regions instead — evidence against, softened because O-84's narrow
                     # low exposure range (<=~1.2 egg/day) limits PURE's power to resolve modification
lik_pure_H50 = 0.8   # 0.8×: residual, unconstrained. Its exposure-range sub-explanation is directly fed by
                     # O-84 (uniformly low intake -> PURE sampled the flat low limb of one dose-response) and
                     # its chance sub-explanation accommodates the evaporating NS signals, so nearly as
                     # expected as H-7; a hair lower only as a diffuse grab-bag rather than a sharp prediction
t_pure = 0.78        # cap = min trust_score over {O-86,O-87,O-88,O-84}, all via S-91 = 0.78. No specific
                     # dock: the multi-country FFQ measurement heterogeneity is already reflected in S-91's
                     # cap, and the HRs and intake distribution are precisely stated; kept at cap (rule 4)
evidence("HC-2", ["O-86", "O-87", "O-88", "O-84"], [lik_pure_H7, lik_pure_H22, lik_pure_H50], t=t_pure)
```
