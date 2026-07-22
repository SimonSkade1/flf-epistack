---
id: E-3
type: evidence-link
from: "[[O-26 - STAR found no strangelets - upper limit 1e-6 per central Au-Au collision for lifetime above 0.1 ns and mass above 30 GeV]]"
to: "[[HC-7 - Stability of bulk strange quark matter]]"
---
![[O-26 - STAR found no strangelets - upper limit 1e-6 per central Au-Au collision for lifetime above 0.1 ns and mass above 30 GeV]]

## Why this is evidence

Under H-28 there exist stable (hence long-lived) strangelet states that a Au+Au fireball could in principle populate, so a dedicated search has some chance of a positive; under H-39 no stable strangelet exists and only short-lived metastable candidates could appear, predicting the null within STAR's lifetime window essentially for sure. The null therefore favours H-39 — weakly, since thermal/coalescence production penalties suppress strangelet yields under H-28 as well, so much of the null's probability is shared.

## Likelihood

```python
# E-3 (HC-7) — lone edge, one observation O-26 "STAR found no strangelets: upper limit < 1e-6 per central
# Au+Au collision for lifetime > 0.1 ns, mass > 30 GeV". Members in HC-7.hypotheses order
# [H-28 stable in bulk, H-39 not stable]; exhaustive, no residual.
# Anchored on H-39 = 1 (rule 7): with no stable strangelet only short-lived metastable candidates could
# appear, so the null within STAR's window is essentially certain — the clean unit. H-28 priced as "how
# expected is this null if stable, long-lived strangelet states DID exist for a Au+Au fireball to populate".
# This edge rests on the RHIC/STAR collision-production absence (data-basis D-15), kept deliberately
# separate from E-2's terrestrial/astrophysical nulls — so the null's discrimination is judged on RHIC
# production alone and the terrestrial/astro absence is NOT re-used here.
lik_star_H39 = 1.0   # anchor: if strange matter is not stable (H-39) STAR sees nothing — predicted for sure.
lik_star_H28 = 0.8   # 0.8× vs anchor: only weakly surprising under H-28. Even with stable strangelets,
                     # thermal/coalescence penalties suppress the RHIC yield far below STAR's 1e-6
                     # sensitivity (the fireball is hot, a strangelet is cold; s-quarks and baryon number
                     # peak in different rapidity regions), so most of the null's probability is SHARED
                     # between the members and the ratio sits close to 1. Below 1 because a stable long-lived
                     # state still gives STAR some nonzero chance a metastable H-39 world lacks.
t_star = 0.82        # cap = trust_score of O-26's source S-1 = 0.82. Held at the cap: O-26 is a single
                     # published dedicated upper limit off RHIC hadron-production data (D-15); no
                     # measurement, selection or pipeline weakness between that data and the stated limit to
                     # dock for.
evidence("HC-7", ["O-26"], [lik_star_H28, lik_star_H39], t=t_star)
```
