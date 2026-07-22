---
id: HC-11
type: hypothesis-cluster
question: "Why do the measured Higgs-potential parameters lie so close to the stability-metastability boundary?"
hypotheses:
  - "[[H-6 - The near-criticality of the Higgs potential parameters reflects an underlying dynamical or statistical principle]]"
  - "[[H-43 - The near-criticality of the Higgs potential is an unexplained coincidence]]"
exclusivity: "Either an underlying dynamical or statistical mechanism places the parameters near the phase boundaries or the proximity is a coincidence; the members are a claim and its negation."
exhaustive_by_construction: true
independence: "Whether a principle underlies the parameter values factorizes, to good approximation, from the other clusters' base rates."
depends_on:
  - "HC-10: a mechanism driving the quartic coupling toward zero mildly favours the metastable side of the stability question; judged small"
relevance: "Bears on how surprised we should be by the vacuum's borderline status and thus on how the vacuum-decay branch of the main question is framed."
---
![[H-6 - The near-criticality of the Higgs potential parameters reflects an underlying dynamical or statistical principle]]
![[H-43 - The near-criticality of the Higgs potential is an unexplained coincidence]]

Principle against coincidence for the same explanandum. Exhaustive by construction: proposition and logical complement. A failure of the analysis — e.g. the near-criticality itself dissolving under shifted top-mass or coupling inputs — would remove the explanandum and thereby favour the second member (nothing left to explain).

## Prior

```python
# HC-11 prior — why the measured Higgs-potential parameters lie so close to the
# stability–metastability boundary. Members in HC-11.hypotheses order:
# [H-6 underlying dynamical/statistical principle, H-43 unexplained coincidence].
# Cluster is exhaustive_by_construction (a claim and its negation), so there is NO
# residual member and rule 4 does not apply.
#
# Inputs: the OUTSIDE VIEW only — the historical base rate at which apparent
# near-coincidences among fundamental-physics parameters turn out to rest on a genuine
# mechanism versus staying accidents. `no_observation_arguments.py --cluster HC-11`
# returned none. The cluster's three inbound E edges (E-20 / E-22 / E-23, correlation
# group CG-8) all carry the case-specific MEASURED near-criticality itself — the very
# datum that discriminates a principle from a coincidence — so NONE is marked
# used_for_prior; the whole group is priced at step 8. (A-6, the top-mass /
# no-new-physics scope caveat, attaches to those observations, not to a member, so it is
# likewise a step-8 concern and is not folded in here.)
#
# depends_on HC-10 (noted, NOT imported): an H-6 variant that dynamically drives
# lambda(M_Pl) -> 0 mildly correlates with HC-10's metastable-side outcome. Step 4 judged
# this cross-cluster coupling small, so the prior factorizes to good approximation; per
# rule 3 it is treated as an approximation in prose and no HC-10 weight enters this block.

# H-43 unexplained coincidence — the anchor / null. For this to be the answer, the
# proximity of m^2 and lambda to their critical boundaries is just an unforced draw of
# otherwise unrelated parameters, with no mechanism selecting it. Reference class:
# apparent fine-tunings and "large-number" coincidences in physics, a fair fraction of
# which have stayed bare accidents (or been dismissed as such) despite decades of
# mechanism-hunting. Anchored at unit weight; the more confident member because it posits
# no unobserved new physics.
w_coincidence = 1.0

# H-6 underlying principle — priced as odds against the coincidence anchor. For this to
# hold, some dynamical or statistical attractor (a multiverse distribution peaked on
# critical lines, self-organized criticality, or transplanckian dynamics pushing
# lambda(M_Pl) -> 0) must actually place the parameters near the boundary. The odds are
# built outside-view first, WITHOUT using this case's measured near-criticality (that is
# step 8's discriminating datum), so the prior mildly favours the null and lets the
# step-8 observations do the lifting toward H-6 if they warrant it.
r_base = 1.0   # reference-class odds: across fundamental-physics parameter near-coincidences,
               # a genuine underlying principle is eventually confirmed about as often as the
               # puzzle stays an accident — even odds, naturalness intuition offset by the weak
               # historical track record of actually confirming such principles.
r_spec = 0.7   # downward adjustment: the specific mechanisms proposed for THIS case
               # (multiverse self-organized criticality, transplanckian attractor) sit at the
               # speculative end with no confirmed analog, and the source (Degrassi et al. 2012)
               # itself flags H-6 as "explicitly speculative" — so shade below even in the prior.
w_principle = r_base * r_spec * w_coincidence

prior("HC-11", [w_principle, w_coincidence])
```
