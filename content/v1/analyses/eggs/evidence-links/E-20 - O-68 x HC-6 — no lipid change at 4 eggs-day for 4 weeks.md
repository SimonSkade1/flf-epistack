---
id: E-20
type: evidence-link
from: "[[O-68 - No lipid-panel component changed in any arm, including 4 eggs-day for 4 weeks]]"
to: "[[HC-6 - Effect of egg-egg-cholesterol intake on the atherogenic blood-lipid profile]]"
---
![[O-68 - No lipid-panel component changed in any arm, including 4 eggs-day for 4 weeks]]

## Why this is evidence
At 4 eggs/day H-34's linear model predicts roughly +10 mg/dL LDL; a flat panel favours the net-neutral H-40 over H-34.

## Likelihood

```python
# E-20 (HC-6) — lone edge, one observation O-68 "no lipid-panel component changed in any arm, incl. 4 eggs/day
# x4wk" (Wilcox; healthy young normoglycemic adults, eggs ADDED not displacing carbs). Members in
# HC-6.hypotheses order [H-20 comparator-relative-worse-vs-carb, H-34 linear-absolute-LDL-rise,
# H-40 net-neutral/HDL-up, H-53 residual]. This edge's body: at 4 eggs/day H-34 predicts ~+10 mg/dL LDL; a
# flat panel favours net-neutral H-40 over H-34. Anchored H-40 = 1.0 (rule 7).
lik_flat_H40 = 1.0   # anchor / best fit: a flat panel is what "net-neutral" predicts; only imperfect because
                     # H-40 also claims HDL UP and HDL did not move either (the low-carb background it needs is
                     # absent here) — so the neutral half fits, the favourable half is unobserved.
lik_flat_H34 = 0.3   # 0.3x: the linear dose-response predicts a clear ~+10 mg/dL LDL rise at 4 eggs/day, so a
                     # flat panel is against H-34; not lower because median-age-28 hypo-responders and n=18 can
                     # null out a real population mean effect (the general dose-response O-28 sits in the prior).
lik_flat_H20 = 0.85  # 0.85x: H-20's worsening is specific to dysglycemic adults displacing high-carb breakfast
                     # — trigger conditions absent in this normoglycemic add-on design, so a flat result is
                     # fully consistent with (though not positively predicted by) H-20.
lik_flat_H53 = 0.65  # 0.65x residual, middling (rule 3): an effect confined to LDL particle quality/oxidation
                     # or an ApoE4 subgroup would leave this bulk panel flat — consistent, unconstrained.
t_flat = 0.72        # cap = trust_score of O-68's source S-60 = 0.72; kept at cap — a directly-measured
                     # (secondary) lipid panel in a registered RCT; the young hypo-responder sample is a
                     # generalizability caveat (priced in the likelihoods), not a data-reliability defect.
evidence("HC-6", ["O-68"], [lik_flat_H20, lik_flat_H34, lik_flat_H40, lik_flat_H53], t=t_flat)
```
