---
type: argument
id: A-20
statement: "The closed-form E-value formula quantifies exactly how strong the joint confounder–exposure and confounder–outcome associations must be to reduce an observed risk ratio to the null, and applied to typical cohort magnitudes it shows small hazard ratios require only modest unmeasured confounding to be explained away, larger ones require strong confounding."
source: "[[S-94 - The E-value- how much unmeasured confounding would it take to explain away an association]]"
locator: "Abstract; E-value formula (Methods)"
affects_observations: ["[[O-57 - The E-value is the minimum RR-scale confounder strength needed to fully explain away an observed association]]"]
affects_hypotheses: []
---
## Reasoning
Ding & VanderWeele's confounding bound: for an unmeasured confounder U, let RR_EU be the maximum risk ratio relating exposure to U (across its levels) and RR_UD the risk ratio relating U to the outcome. The maximum factor by which such confounding can inflate an observed risk ratio is the bias factor B = (RR_EU · RR_UD) / (RR_EU + RR_UD − 1). Setting the confounding-adjusted risk ratio to 1 (the association fully explained away) and taking the symmetric worst case RR_EU = RR_UD = E — the case that minimises the required joint strength — and solving B = RR gives the closed form

  E-value = RR + sqrt( RR · (RR − 1) )   for an observed RR ≥ 1.

For a protective estimate (RR < 1) the reciprocal 1/RR is used first. To ask what confounding would move the *confidence interval* to the null, the same formula is applied to the confidence limit nearer the null (the lower limit LL when RR > 1): E = LL + sqrt(LL·(LL − 1)); if that limit is already ≤ 1 the E-value is 1.

Worked application to nutrition-cohort magnitudes (numbers computed from the formula): an observed hazard ratio ≈ 1.2 — the order of magnitude reported for egg intake vs CVD/T2D — has E-value = 1.2 + sqrt(1.2 · 0.2) = 1.2 + sqrt(0.24) ≈ 1.2 + 0.49 = 1.69; a HR of 1.5 gives ≈ 2.37; a HR of 2 gives 2 + sqrt(2) ≈ 3.41. So an unmeasured confounder (e.g. an unadjusted healthy-user or dietary-pattern factor) associated with BOTH egg intake and the outcome by a risk ratio of roughly 1.7 each, beyond the measured covariates, would suffice to null a HR of 1.2, whereas a HR of 2 would need each of those two associations to be about 3.4. The inference is a valid algebraic consequence of the bounding factor B, which is itself a sharp (attainable) upper bound on confounding bias, so the E-value is the exact minimum joint strength required.
