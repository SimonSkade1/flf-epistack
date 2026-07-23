---
id: E-58
type: evidence-link
from: "[[O-55 - JPHC (Japan) - no association between egg intake and incident T2D in either men or women]]"
to: "[[HC-3 - Effect of habitual egg intake on incident type-2 diabetes]]"
arguments:
  - "[[A-19 - Self-reported T2D over a short 5-year follow-up biases toward the null, so the JPHC egg null under-discriminates]]"
---
![[O-55 - JPHC (Japan) - no association between egg intake and incident T2D in either men or women]]

## Why this is evidence
A null Asian cohort anchors the null-to-inverse Asia pole predicted by H-8 and H-9, and is evidence against H-51's uniform non-null effect.

## Likelihood

```python
# E-58 (HC-3) — lone edge, one observation O-55 "JPHC (Japan) egg-T2D null in both sexes". Members in
# HC-3.hypotheses order [H-8 region-dependent-causal (Asia null-to-inverse), H-9 uniform-null-via-confounding,
# H-51 residual uniform non-null effect]. A clean Asian null is predicted about equally by H-8 and H-9 (both
# put Asia at null/inverse) and tells against H-51's uniform non-null effect (this edge's body). Anchored H-9 = 1.0.
p_jphc_H9 = 1.0    # anchor: uniform-null-everywhere predicts an exactly-null Asian cohort directly.
p_jphc_H8 = 0.95   # ~0.95x: H-8 predicts Asia "null-to-inverse", so a flat null sits at the null end of its
                   # range — very slightly less expected than H-9's exact null, essentially co-equal.
p_jphc_H51 = 0.55  # 0.55x: a uniform non-null effect is disfavoured by a null, but A-19 (approved) shows the
                   # self-reported outcome over ~5 y plus single-FFQ exposure bias toward the null, so a modest
                   # true effect (~US 14-18%/egg) could be masked — the null under-discriminates, kept real.
t_jphc = 0.6       # cap = trust_score of O-55's source S-9 = 0.65; docked to 0.6 for the abstract-level
                   # extraction (full text not accessed, per O-55) — a provenance weakness in the datum itself,
                   # distinct from A-19's attenuation already priced into the likelihoods.
evidence("HC-3", ["O-55"], [p_jphc_H8, p_jphc_H9, p_jphc_H51], t=t_jphc)
```
