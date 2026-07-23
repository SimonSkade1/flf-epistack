---
id: E-38
type: evidence-link
from: "[[O-72 - KoGES (Korea) - egg intake not associated with CVD incidence in the whole cohort]]"
to: "[[HC-1 - Overall net effect of moderate habitual egg intake on cardiovascular disease and mortality]]"
arguments:
  - "[[A-24 - Adverse egg-CVD HR confined to the diabetic stratum supports effect-modification by diabetes, but the small subgroup makes it imprecise]]"
---
![[O-72 - KoGES (Korea) - egg intake not associated with CVD incidence in the whole cohort]]

## Likelihood

```python
# E-38 (HC-1) — lone edge, one observation O-72 "KoGES whole-cohort egg-CVD null": in a small Korean cohort
# (9,248 adults, 570 CVD cases) the whole-cohort egg-CVD HR is a non-significant 1.14 (0.87-1.49, P-trend 0.7).
# A-24 (approved): this whole-cohort null masks an adverse HR confined to the diabetic stratum (2.81), diluted
# by the diabetic minority. Members in HC-1.hypotheses order [H-6, H-21, H-27, H-44, H-49]. Anchored on
# H-21 = 1 (rule 7): a whole-cohort null is the null's direct prediction.
lik_koges_H21 = 1.0   # anchor: a non-significant whole-cohort HR is exactly H-21; the diabetic-subgroup 2.81 is
                      # small-n noise under a true null and the ~1.14 point is well within its wide CI.
lik_koges_H6  = 0.5   # 0.5x: Korea is Asian, so H-6 (Asian protection) would lean the whole-cohort HR BELOW 1;
                      # the observed point is 1.14 (slightly positive), mild tension — but the cohort is small and
                      # imprecise (CI down to 0.87 still admits protection), so only a moderate dock.
lik_koges_H27 = 0.55  # 0.55x: the point estimate 1.14 is in the harm direction and the diabetic-subgroup harm
                      # (A-24 approved) is consistent with a susceptibility-concentrated cholesterol mechanism;
                      # non-significant in an underpowered cohort (570 events) is compatible with H-27. Slightly
                      # above H-6 because the sign matches, though H-27 is US-scoped.
lik_koges_H44 = 0.4   # 0.4x: KoGES intake (~0.1-4.2 servings/wk) spans the U's low-to-optimum range where H-44
                      # predicts an INVERSE (descending) trend; the observed 1.14 highest-vs-lowest runs mildly the
                      # other way, so mild tension, softened by imprecision.
lik_koges_H49 = 0.6   # 0.6x: a whole-cohort null that masks a subgroup-specific (diabetic) sign is precisely the
                      # subgroup-dependent world the residual covers (A-24 approved supports effect-modification),
                      # so H-49 fits a little above middling here.
t_koges = 0.55        # cap = trust_score(S-14) = 0.55, the source of O-72. Left at the cap: the 0.55 already
                      # reflects the small imprecise cohort; the whole-cohort null itself (570 cases) is the more
                      # reliable half of this source, and A-24 concerns the subgroup's imprecision, not O-72's, so
                      # no dock below the cap.
evidence("HC-1", ["O-72"],
         [lik_koges_H6, lik_koges_H21, lik_koges_H27, lik_koges_H44, lik_koges_H49], t=t_koges)
```
