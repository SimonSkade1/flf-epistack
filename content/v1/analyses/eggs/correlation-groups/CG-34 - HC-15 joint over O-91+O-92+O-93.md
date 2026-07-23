---
type: correlation-group
id: CG-34
to: "[[HC-15 - Whether nutritional-cohort associations can support causal egg-health claims]]"
members:
  - "[[E-100 - O-91 x HC-15 — FFQ energy under-reported ~35 percent, instrument-driven]]"
  - "[[E-101 - O-92 x HC-15 — protein density escapes under-reporting bias]]"
  - "[[E-102 - O-93 x HC-15 — under-reporting is BMI-correlated (differential)]]"
---

Joint likelihood for correlated observations O-91, O-92, O-93 (shared basis: S-99). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-34 (HC-15) — ONE joint estimate over members E-100 + E-101 + E-102: O-91/O-92/O-93 all rest on the OPEN
# validation study S-99 (rule 1). Whole pattern judged together: (a) FFQ under-reports energy ~35%, ~2x the 24HR
# (instrument-driven); (b) absolute protein under-reported ~30% but protein DENSITY (a ratio) barely biased; (c)
# under-reporting rises with BMI (differential, person-specific). Members in HC-15.hypotheses order [H-31 reform;
# H-41 defence; H-59 residual]. Anchored on H-31 = 1 (best fit); others as ratios (rule 7). Condition strictly on H.
lik_open_H31 = 1.0   # anchor: the reform pole predicts exactly (a)+(c) — a large, FFQ-specific, BMI-CORRELATED error
                     # (O-93, the load-bearing differential finding; A-29 approved: a single attenuation/calibration
                     # factor cannot fully remove it). (b) density-escape is a mild concession but leaves the
                     # differential core that defeats causal weight, so it barely dents the fit
lik_open_H41 = 0.45  # 0.45x: (b) is the empirical basis defence wants for energy-adjustment/ratio measures, but (c)'s
                     # BMI-correlated differential error directly breaks the non-differential premise the manageability
                     # claim rests on (A-29 approved). The strong policy-grade pole predicts this whole pattern worst
lik_open_H59 = 0.9   # 0.9x: the intermediate standing (real error, partly removable by ratios yet with an irreducible
                     # differential core, reliable only for large effects) fits the mixed pattern almost as well as
                     # H-31; unconstrained middle sits just below the reform anchor
t_open = 0.85        # cap = min trust_score over {O-91,O-92,O-93}, all via S-99 = 0.85; OPEN measures against
                     # gold-standard biomarkers (doubly-labeled water, urinary nitrogen), no raw->observation weakness
                     # to dock for beyond the source trust set at step 2
evidence("HC-15", ["O-91", "O-92", "O-93"], [lik_open_H31, lik_open_H41, lik_open_H59], t=t_open)
```
