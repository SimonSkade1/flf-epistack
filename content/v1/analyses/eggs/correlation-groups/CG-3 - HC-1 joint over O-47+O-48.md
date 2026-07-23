---
type: correlation-group
id: CG-3
to: "[[HC-1 - Overall net effect of moderate habitual egg intake on cardiovascular disease and mortality]]"
members:
  - "[[E-49 - O-47 × HC-1 — 33-cohort meta null point estimate with high heterogeneity]]"
  - "[[E-50 - O-48 × HC-1 — meta region gradient Asian inverse vs Western null]]"
---

Joint likelihood for correlated observations O-47, O-48 (shared basis: D-26). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-3 (HC-1) — ONE joint estimate over E-49 (O-47) + E-50 (O-48): both rest on the same 33-cohort meta corpus
# (basis D-26), one witness (rule 1). The JOINT pattern is the load-bearing thing: the world literature pools
# to the NULL (RR 0.98/egg-day) BUT with high, region-STRUCTURED heterogeneity (I2=62.3%; Asia inverse 0.92
# significant, US 1.01 null, Europe 1.05 null; region the main heterogeneity source, P-interaction 0.07).
# Members in HC-1.hypotheses order. Anchored on H-49 = 1 (rule 7, and rule 3 permits the residual as best fit
# where argued): "pooled null WITH region-structured heterogeneity" is literally the residual's signature —
# a genuinely region-dependent sign averages to null globally while refusing to pool cleanly.
lik_meta_H49 = 1.0   # anchor: H-49 (no single population verdict; sign region-dependent) predicts BOTH halves —
                     # the null pooled point AND the structured I2 — jointly. The edge notes call the high I2
                     # "diagnostic for the residual" and the region gradient "the signature prediction of H-49".
lik_meta_H6  = 0.7   # 0.7x: H-6 (Asian protection) predicts the Asia inverse arm well and is consistent with a
                     # West/global null, but it does not itself explain WHY the heterogeneity is region-structured
                     # around a null the way H-49 does; strong but slightly less complete than the anchor.
lik_meta_H21 = 0.6   # 0.6x: H-21 loves the pooled null (O-47) but its statement claims neutrality HOLDS across
                     # regions, which the significant Asian inverse and I2=62.3% dent; survives only via
                     # null-plus-differential-bias (A-18 corrected: heterogeneity is consistent with, not proof
                     # of, modification), so it must explain away the structure it did not predict.
lik_meta_H27 = 0.2   # 0.2x: H-27 needs the US positive; the US estimate is 1.01 (null) and the pool is null —
                     # direct tension. Europe 1.05 is only null-positive. Worst fit.
lik_meta_H44 = 0.45  # 0.45x: a per-egg LINEAR meta-slope cannot see curvature, so a true U would read ~null here
                     # (compatible with O-47) — but H-44 does not predict the region-structured heterogeneity, so
                     # it is only weakly separated and sits below the anchor.
t_meta = 0.82        # cap = trust_score(S-19) = 0.82, min over {O-47, O-48}. Left at the cap: the FFQ/pooling
                     # limits are in 0.82; the heterogeneity itself is an observed feature (it drives the ratios),
                     # not a data-reliability defect, and no specific un-inspectable raw-data step is named.
evidence("HC-1", ["O-47", "O-48"],
         [lik_meta_H6, lik_meta_H21, lik_meta_H27, lik_meta_H44, lik_meta_H49], t=t_meta)
```
