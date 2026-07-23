---
type: correlation-group
id: CG-8
to: "[[HC-3 - Effect of habitual egg intake on incident type-2 diabetes]]"
members:
  - "[[E-55 - O-17 x HC-3 — region gradient US+-Europe-null-Asia-inverse]]"
  - "[[E-56 - O-31 x HC-3 — US 1.18 (I2 0%) vs non-US 0.97 split]]"
  - "[[E-57 - O-29 x HC-3 — Swedish men null, register outcomes]]"
  - "[[E-60 - O-18 x HC-3 — association concentrates at low diet quality]]"
  - "[[E-61 - O-43 x HC-3 — eggs co-occur with unhealthy Western pattern]]"
  - "[[E-62 - O-19 x HC-3 — substitution helps only vs prudent foods]]"
  - "[[E-63 - O-15 x HC-3 — US signal null in men, positive in women]]"
---

Joint likelihood for correlated observations O-17, O-31, O-29, O-18, O-43, O-19, O-15 (shared basis: D-7, D-9, D-25). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-8 (HC-3) — ONE joint estimate over E-55/E-56/E-57/E-60/E-61/E-62/E-63: all seven observations rest on the
# overlapping Harvard / Swedish / pooled-meta cohort corpus (D-7, D-9, D-25), so they are judged as ONE pattern
# (rule 1), not seven independent witnesses. The whole pattern: a US-positive / Europe-null / Asia-inverse
# gradient (O-17, O-31; p-interaction 0.01, US I2=0%), a functionally-null register-based European cohort
# (O-29), the association concentrating at LOW diet quality (O-18), eggs co-occurring with the unhealthy
# Western basket (O-43), benefit only when eggs are swapped for PRUDENT foods and none vs other animal proteins
# (O-19), and a fragile, sex-varying US signal null in men (O-15). Members in HC-3.hypotheses order
# [H-8 region-dependent-causal, H-9 uniform-null-via-confounding, H-51 residual/uniform-effect].
# Anchored on H-9 = 1 (best fit); others priced as ratios (rule 7).
lik_grad_H9  = 1.0   # anchor: the confounding account predicts the WHOLE pattern — the gradient arises because
                     # confounding strength varies by region (eggs mark the diabetogenic Western pattern in the
                     # US, prudent diets in Asia); O-18 (stronger where diet quality is low) is where residual
                     # confounding is strongest; O-43 is the confounder-correlation H-9 requires; O-19's
                     # marker-substitution signature (benefit only vs prudent foods, neutral vs the animal-food
                     # class eggs belong to) and O-15's sex-fragility both fit a confounded, non-causal signal.
                     # A-5/A-10/A-16 (approved) and A-6 (corrected) all read these features as confounding.
lik_grad_H8  = 0.45  # ~0.45x the anchor: a genuinely region-dependent CAUSAL effect predicts the bare gradient
                     # (O-17/O-31/O-29) about as well as H-9 does — E-55/E-56/E-57 note the gradient does not
                     # separate the two — but it gives no strong reason for the WITHIN-population diet-quality
                     # modification (O-18), the marker-substitution pattern (O-19: a real egg effect should lower
                     # risk when eggs are replaced by ANY neutral food, yet swaps vs other animal proteins are
                     # null), or the sex-fragility (O-15, null in HPFS men). Those four features tilt the joint
                     # pattern toward confounding, so H-8 sits below the anchor.
lik_grad_H51 = 0.25  # ~0.25x: a UNIFORM modest effect (positive or inverse) across all regions predicts
                     # homogeneous estimates — directly contradicted by the region heterogeneity (p-interaction
                     # 0.01; US 1.18 I2=0% vs non-US 0.97), the register-based Swedish null (O-29) and the
                     # null-in-men (O-15). Below both listed members, but kept well above zero: "some other
                     # structure" is unconstrained (rule 3) and a uniform inverse could weakly accommodate the
                     # Asia end, so the heterogeneity does not forbid it outright.
t_gradient = 0.75    # cap = min trust over {S-4 0.78, S-8 0.75, S-19 0.82} = 0.75 (S-8). Held at the cap: the
                     # region gradient is a straightforward description of published, independently reproduced
                     # meta-analytic estimates (S-4 and S-8 report it separately); the overlapping-cohort
                     # correlation is handled by this being ONE joint call, not by t, and the FFQ/observational
                     # limitations are already priced into the step-2 trust scores.
evidence("HC-3", ["O-17", "O-31", "O-29", "O-18", "O-43", "O-19", "O-15"], [lik_grad_H8, lik_grad_H9, lik_grad_H51], t=t_gradient)
```
