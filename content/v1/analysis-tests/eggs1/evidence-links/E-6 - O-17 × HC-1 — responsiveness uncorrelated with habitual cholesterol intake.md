---
type: evidence-link
id: E-6
from: "[[O-17 - Cholesterol responsiveness correlates with HDL2-total-cholesterol rise but not with habitual intake or body weight]]"
to: "[[HC-1 - Magnitude and mechanism of egg's effect on atherogenic blood lipids]]"
arguments:
  - "[[A-5 - Stable-but-unpredictable responder classes make the population-average LDL response misleading for subgroups]]"
---
![[O-17 - Cholesterol responsiveness correlates with HDL2-total-cholesterol rise but not with habitual intake or body weight]]

## Why this is evidence

H-8's saturating dose-response predicts that people with high habitual cholesterol intake sit on the flat part of the curve and are therefore less responsive - i.e. a negative correlation between habitual intake and responsiveness. None was found, which disfavours H-8. H-1 and H-5 make no such prediction.

## Likelihood

```python
# E-6 (HC-1) - lone edge, one observation O-17 "responsiveness correlates with the HDL2/total-cholesterol
# rise but NOT with habitual cholesterol intake or body weight". Members in HC-1.hypotheses order:
# [H-1 large ApoB rise, H-5 poor bioavailability, H-8 real-but-saturating, H-11 residual].
# This edge cuts AGAINST H-8 (see "Why this is evidence"): a saturating curve implies high-habitual-intake
# subjects sit on the flat part and respond less, i.e. a negative intake-responsiveness correlation.
# Anchored on H-1 = 1 (rule 7).
lik_nocorr_H1 = 1.0    # anchor: a non-saturating account makes no prediction tying responsiveness to
                       # habitual intake, so a null correlation is unremarkable
lik_nocorr_H5 = 1.0    # same: absorption-limited effects predict nothing about habitual-intake gradients
lik_nocorr_H8 = 0.45   # 0.45x: H-8's corollary predicts the negative correlation that was not found.
                       # Not lower because habitual-intake measurement is self-reported and noisy, the
                       # sample is small, and the observed habitual range may be narrow - all of which
                       # attenuate a real correlation toward zero. So this disfavours H-8 but weakly
lik_nocorr_H11 = 0.85  # residual, unconstrained (rule 3): most unlisted characterizations impose no
                       # intake-responsiveness link, so a null is largely expected
t_nocorr = 0.50        # cap = trust_score of O-17's source S-5 = 0.68. Docked substantially: this is an
                       # absence-of-correlation in a small responder-typing study, the weakest kind of
                       # inference, and habitual intake is a self-reported exposure. A-5 (approved) notes
                       # responder classes are stable but unpredictable, which is consistent with the
                       # measured covariates simply being poor proxies rather than the curve being flat
evidence("HC-1", ["O-17"], [lik_nocorr_H1, lik_nocorr_H5, lik_nocorr_H8, lik_nocorr_H11], t=t_nocorr)
```
