---
type: evidence-link
id: E-10
from: "[[O-8 - Egg-mortality association about twice as strong in diabetic PHS subgroup, HR 2.01]]"
to: "[[HC-3 - Whether egg's effect varies by subgroup or individual responder type]]"
---
![[O-8 - Egg-mortality association about twice as strong in diabetic PHS subgroup, HR 2.01]]

## Why this is evidence
Directly opposes H-6: the diabetic subgroup looks worse off, not protected. H-13 predicts no subgroup-by-intake interaction at all, so an HR of 2.01 vs the overall 1.23 counts against it too (though P-interaction=0.09 and the exploratory status keep the weight modest). H-7 is largely silent on a diabetes-defined split.
## Likelihood

```python
# E-10 (HC-3) - lone edge, one observation O-8 (PHS: egg-mortality HR 2.01 in the diabetic subgroup vs
# ~1.23 overall, P-interaction=0.09, exploratory). Members in HC-3.hypotheses order:
# [H-6 diabetic subgroup not harmed, H-7 hypo/hyper-responder trait, H-13 residual: homogeneous].
# This edge cuts AGAINST H-6, i.e. the opposite way from E-9 - the tension is real (an RCT lipid null vs
# an observational mortality signal in nominally the same subgroup) and is priced here as such, not
# smoothed. Note the two are not strictly contradictory: lipids are a surrogate and mortality a hard
# endpoint, and the PHS signal may be confounding rather than effect. Anchored on H-13 = 1 (rule 7).
lik_phs_H13 = 1.0    # anchor: under homogeneity there is no true subgroup-by-intake interaction, so an
                     # apparent doubling must come from noise/confounding. With P-interaction=0.09 in an
                     # exploratory subgroup split, a spurious interaction of this size is unremarkable -
                     # multiple-testing across subgroups makes one such signal roughly the expectation.
lik_phs_H6 = 0.45    # 0.45x: H-6 says the diabetic subgroup is NOT worse off, so a doubled mortality HR
                     # is a genuine surprise under it - the clearest disconfirming datum for H-6 in the
                     # graph. Not lower than ~0.45 because H-6 is a claim about the causal effect of eggs
                     # while this is an unadjusted-for-confounding observational association: diabetic
                     # physicians eating more eggs plausibly differ in overall diet quality, glycaemic
                     # control and severity, and reverse causation is live. So H-6 can accommodate the
                     # observation as confounding, just less comfortably than H-13 can.
lik_phs_H7 = 0.95    # 0.95x: H-7 is largely silent on a diabetes-defined split - a responder trait neither
                     # predicts nor forbids a diabetic subgroup interaction. Set just below the anchor
                     # rather than at it only because H-7 asserts SOME real heterogeneity exists, which
                     # marginally raises tolerance for a real interaction elsewhere. No discrimination is
                     # being manufactured here.
t_phs = 0.40         # cap = trust_score of O-8's source S-14 = 0.68. Docked hard: the observation is an
                     # explicitly exploratory subgroup analysis with P-interaction=0.09 (i.e. not
                     # conventionally significant), a small diabetic stratum inside PHS, self-reported
                     # egg intake, and an all-male US-physician cohort. The step from raw data to
                     # "the association is twice as strong in diabetics" is exactly where selective
                     # subgroup reporting bites.
evidence("HC-3", ["O-8"], [lik_phs_H6, lik_phs_H7, lik_phs_H13], t=t_phs)
```
