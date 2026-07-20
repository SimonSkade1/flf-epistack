---
type: correlation-group
id: CG-5
to: "[[HC-2 - Net direction of egg's effect on hard cardiovascular and mortality endpoints]]"
members:
  - "[[E-19 - O-9 x HC-2 - EPIC modest inverse egg-IHD association]]"
  - "[[E-20 - O-10 x HC-2 - EPIC inverse association vanishes after 4-year lag exclusion]]"
---

Joint likelihood for correlated observations O-9, O-10 (shared basis: D-10). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-5 (HC-2) - ONE joint estimate over E-19 + E-20: O-9 and O-10 both rest on D-10 (EPIC, same analysis and
# its own sensitivity check), so they are ONE witness (rule 1). The pattern judged whole: a modest inverse
# egg-IHD association (HR 0.93 per 20 g/d, 7198 cases) that loses statistical significance when the first
# 4 years of follow-up are dropped. Members in HC-2.hypotheses order:
# [H-2 protective, H-3 harmful, H-4 null-IHD/reverse-causation, H-9 null-healthy-Western, H-10 null-global,
# H-12 residual direction-varies]. Anchored on H-9 = 1 (rule 7); others are ratios to it.
#
# A-3 is `corrected` (step 6) and this constrains the whole block: the corrected statement is that reverse
# causation *contributes* and near-null is *consistent* - NOT that the attenuation demonstrates reverse
# causation. Dropping 4 years cuts case count and hence power, so losing significance is expected even under
# a constant true HR; a single baseline FFQ decays as an exposure measure and biases later periods toward the
# null anyway; and a genuine short-latency effect would also concentrate early. So H-4 is NOT rewarded as if
# it had a clean signature confirmation - the pattern is only mildly more expected under H-4 than under the
# other null variants. The three null members differ only by scope rider, so the differences below are driven
# by scope fit to THIS observation (a Western multi-country cohort, IHD endpoint), not by direction.

lik_epic_H9 = 1.0    # ANCHOR. H-9 (no material excess CVD risk up to ~1/day in general adult populations) is
                     # the best scope match: EPIC is exactly a large general Western adult population with an
                     # IHD endpoint. Under H-9 you expect a small, unstable, roughly-null estimate that
                     # wobbles across sensitivity analyses - which is precisely this pattern.
lik_epic_H4 = 1.15   # ~1.15x the anchor. H-4's scope (IHD specifically) is the endpoint actually measured
                     # here, and its rider does anticipate a weak apparent inverse that softens on lagging.
                     # But given A-3-corrected, the lag result is only weak support: the loss of significance
                     # is largely a power artefact, and a null-by-any-route member predicts a wobbling small
                     # inverse nearly as well. Hence a small edge, not the 2-3x a clean reverse-causation
                     # signature would buy. This number is the one A-3's correction moved most.
lik_epic_H10 = 0.95  # ~0.95x. Same near-null prediction as H-9; scope is broader (low/middle-income
                     # populations too) which this Western-only cohort neither tests nor fits, so it is very
                     # slightly less specific to the observation. Not materially discriminated by this edge.
lik_epic_H2 = 0.70   # 0.70x. H-2 (protective at ~1/day) predicts the inverse sign, and HR 0.93/20g is in the
                     # right direction - but H-2 is a genuine causal protection, which should NOT weaken when
                     # early follow-up is dropped, and here it does (point estimate plus significance both
                     # soften). Also EPIC's intake range is low relative to the Chinese setting H-2 was drawn
                     # from. Docked, not crushed: the power loss means the lag result does not refute H-2.
lik_epic_H3 = 0.35   # 0.35x. Wrong sign entirely - H-3 (harmful at >=7/week) has to explain an inverse point
                     # estimate in 7198 IHD cases as confounding. Possible (healthy-user confounding is real
                     # and EPIC's high-egg eaters are not extreme), and H-3 is about all-cause mortality not
                     # IHD, so the endpoint mismatch softens the conflict. Lowest of the six, but not near zero.
lik_epic_H12 = 0.85  # 0.85x. Unconstrained residual (rule 3): a J-shaped/population-varying effect readily
                     # produces a small net inverse in a cohort whose intake range sits mostly on the flat or
                     # descending limb, and readily produces an unstable sensitivity result. Middling-high,
                     # because "the direction is not one number" positively expects exactly this kind of
                     # small, non-robust estimate. Not above the null members: it does not predict the
                     # specific magnitude any better than they do.
t_epic = 0.60        # cap = trust_score of S-16 = 0.75 (both observations, same source). Docked to 0.60 for
                     # the raw-data-to-stated-observation gap: single baseline FFQ across 9 countries with
                     # non-harmonised instruments, self-reported egg intake, and - per A-3 corrected - the
                     # stated O-10 conflates loss of significance with movement of the point estimate, so the
                     # observation as phrased is itself a partly-degraded rendering of the underlying result.
evidence("HC-2", ["O-9", "O-10"],
         [lik_epic_H2, lik_epic_H3, lik_epic_H4, lik_epic_H9, lik_epic_H10, lik_epic_H12], t=t_epic)
```
