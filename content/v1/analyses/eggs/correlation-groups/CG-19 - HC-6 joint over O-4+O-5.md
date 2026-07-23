---
type: correlation-group
id: CG-19
to: "[[HC-6 - Effect of egg-egg-cholesterol intake on the atherogenic blood-lipid profile]]"
members:
  - "[[E-15 - O-4 x HC-6 — no HDL-C difference in 3-month egg RCT]]"
  - "[[E-16 - O-5 x HC-6 — null TC-LDL-TG in 3-month egg RCT]]"
---

Joint likelihood for correlated observations O-4, O-5 (shared basis: D-3). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-19 (HC-6) — ONE joint estimate over O-4 + O-5, both from the DIABEGG 3-month RCT (S-26, shared
# basis D-3), rule 1. Pattern judged whole: high-egg (~12/wk, 2 eggs/day) vs low-egg in prediabetes/T2D
# adults on a weight-maintenance (NON-carb-restricted) background gave a flat HDL (pre-specified primary
# endpoint, +0.02 mmol/L, P=0.38) AND null TC/LDL/TG. Members in HC-6.hypotheses order
# [H-20, H-34, H-40, H-53]. Anchored on H-40 (rule 7): "nothing worsened" is the net-neutral reading's
# exact signature. A-2 (approved) reads this registered-RCT null as real counter-evidence against the harm
# members but caps it (both arms counselled toward MUFA/PUFA, macronutrient-matched → biased toward null),
# so the harm/neutral gap is moderate, not extreme.
lik_diabegg_H40 = 1.0    # anchor: the flat panel is exactly "net-neutral". Its HDL-up half is not seen, but
                         # H-40's HDL rise is scoped to a carb-restricted background, absent here, so the
                         # flat HDL barely counts against it while the null LDL fits cleanly
lik_diabegg_H34 = 0.7    # 0.7×: H-34 predicts a small absolute LDL rise (~+2-3 mg/dL at this modest dose),
                         # not seen — but the effect is small and the background-diet match (A-2) biases to
                         # null, and H-34's "rise spares HDL" is met by the flat HDL, so only mildly below
lik_diabegg_H20 = 0.6    # 0.6×: H-20's comparator-relative worsening is barely engaged (comparator is
                         # low-egg, not a high-carb breakfast), yet this IS its dysglycemic population and no
                         # worsening appeared; leans adverse against a clean null, so just below H-34
lik_diabegg_H53 = 0.55   # 0.55×: unlisted effect, unconstrained — a particle-quality-only effect leaves
                         # this bulk panel flat, so the null is consistent with it; middling, neither
                         # predicting nor forbidding (rule 3)
t_diabegg = 0.66         # cap = min trust over {O-4,O-5} = S-26 = 0.70; docked slightly for O-5's per-arm
                         # secondary-lipid values being non-recoverable from the accessible text (only the
                         # qualitative "no difference" is reported). A-2's background-match caveat is
                         # reasoning about strength (priced in the ratios), not a data-reliability defect
evidence("HC-6", ["O-4", "O-5"], [lik_diabegg_H20, lik_diabegg_H34, lik_diabegg_H40, lik_diabegg_H53], t=t_diabegg)
```
