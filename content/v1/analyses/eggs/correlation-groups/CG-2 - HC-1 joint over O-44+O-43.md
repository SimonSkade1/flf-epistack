---
type: correlation-group
id: CG-2
to: "[[HC-1 - Overall net effect of moderate habitual egg intake on cardiovascular disease and mortality]]"
members:
  - "[[E-36 - O-44 × HC-1 — Harvard egg-CVD null after adjustment]]"
  - "[[E-64 - O-43 × HC-1 — higher egg eaters carry more CVD risk factors (confounding structure)]]"
---

Joint likelihood for correlated observations O-44, O-43 (shared basis: D-7). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-2 (HC-1) — ONE joint estimate over E-36 (O-44) + E-64 (O-43): both rest on the same Harvard NHS/NHSII/HPFS
# pooled cohort (basis D-7), one witness (rule 1). The pattern: in US cohorts higher egg eaters carry a worse
# risk-factor profile (more red/processed meat, smoking, BMI, T2D — O-43), the crude egg-CVD HR is modestly
# positive (1.10), and it REVERSES to null (0.93, per-egg 0.98) on full lifestyle/diet adjustment (O-44), with
# an E-value of ~1.43 needed to move the CI back to positive. Members in HC-1.hypotheses order. Anchored on
# H-21 = 1 (rule 7): a confounded crude positive collapsing to a robust null is the textbook null signature.
lik_harv_H21 = 1.0   # anchor: H-21 (no causal effect) predicts exactly this — O-43 supplies the confounding
                     # structure, adjustment removes it (A-16 approved), and the E-value 1.43 makes the null
                     # fairly robust to residual confounding (A-17 approved). Sharpest fit.
lik_harv_H6  = 0.55  # 0.55x: H-6 is Asian-scoped and makes no US claim, so a US null/slightly-inverse (0.93) is
                     # compatible — but it does not specifically predict the crude-positive-then-reversal
                     # structure, and a universal protective effect would lean the crude below 1, not to 1.10.
lik_harv_H27 = 0.3   # 0.3x: H-27 (US monotonic harm) predicts a positive egg-CVD association that SURVIVES
                     # adjustment; here it is a robust null. Survival requires over-adjusting away a real effect
                     # (A-16 notes BMI/T2D could be partial mediators), but the E-value 1.43 robustness (A-17)
                     # makes a fully-masked true harm unlikely. Below null.
lik_harv_H44 = 0.45  # 0.45x: H-44 (Chinese U) makes no sharp US prediction; a U averaged over the linear
                     # >=1/day-vs-<1/month contrast can read null, so compatible but unpredicted. Middling-low.
lik_harv_H49 = 0.55  # 0.55x: a region-dependent-sign world (US null, Asia inverse) fits a US null fine; middling
                     # per rule 3, does not specifically predict the confounding-reversal detail.
t_harv = 0.82        # cap = trust_score(S-19) = 0.82, min over {O-44, O-43} (one source). Left at the cap: FFQ
                     # measurement error and residual confounding are already in 0.82, and A-16/A-17 are
                     # reasoning about direction/robustness (they set the H-21:H-27 ratio), not raw-data flaws.
evidence("HC-1", ["O-44", "O-43"],
         [lik_harv_H6, lik_harv_H21, lik_harv_H27, lik_harv_H44, lik_harv_H49], t=t_harv)
```
