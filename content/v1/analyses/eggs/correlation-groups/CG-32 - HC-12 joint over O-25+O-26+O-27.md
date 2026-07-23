---
type: correlation-group
id: CG-32
to: "[[HC-12 - Intact Grade A shell eggs as the major internally-contaminated vehicle of the Salmonella enteritidis epidemic]]"
members:
  - "[[E-2 - O-25 × HC-12 — 77% of NE SE outbreaks traced to intact Grade A eggs]]"
  - "[[E-3 - O-26 × HC-12 — SE outbreaks egg-associated 44% vs 15% other serotypes]]"
  - "[[E-4 - O-27 × HC-12 — NE bulk raw eggs yield SE 10% vs 0%, tracks illness geography]]"
---

Joint likelihood for correlated observations O-25, O-26, O-27 (shared basis: S-20). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-32 (HC-12) — ONE joint estimate over members E-2 (O-25) + E-3 (O-26) + E-4 (O-27): all three are the same
# CDC surveillance analysis, shared basis S-20 (rule 1). Members in HC-12.hypotheses order [H-11 internal
# trans-ovarian route drives it, H-12 eggs a MAJOR vehicle (magnitude), H-58 residual negation]. NON-exhaustive:
# H-58 gets a real, argued likelihood (rule 3). Judge the whole pattern: 77% of vehicle-identified NE outbreaks
# traced to INTACT, uncracked, refrigerated Grade A eggs; SE egg-associated 44% vs 15% for other serotypes;
# bulk-raw-egg cultures 10% NE vs 0% elsewhere tracking illness geography. Anchored on H-11 = 1 (rule 7).
lik_se_H11 = 1.0   # anchor: the internal-route thesis entails eggs being the major vehicle (so it predicts all
                   # three magnitude signals) AND uniquely explains the distinctive detail that intact,
                   # refrigerated eggs still cause illness. A-7 (corrected): intact/refrigerated illness strongly
                   # disfavours external routes, making internal trans-ovarian the best-supported explanation
                   # (corrected from "excluded/forced" — external route disfavoured, not eliminated).
lik_se_H12 = 0.8   # ~0.8x the anchor: the pure magnitude claim predicts the 77% / 44-vs-15 / geography signals
                   # just as well, but is route-agnostic, so it is slightly more surprised by the
                   # intact-refrigerated detail (only H-11 puts full mass on the internal route). A-8 (approved):
                   # the serotype specificity (44 vs 15) ties the vehicle to SE — nailed equally by both facets.
lik_se_H58 = 0.15  # ~0.15x the anchor: the residual negation (external shell route controllable by handling, OR
                   # eggs not the principal vehicle) must reproduce THREE convergent, multi-stream signals at
                   # once — attribution, SE-serotype specificity, and direct egg-culture geography. External
                   # route is contradicted by intact/refrigerated illness; "not the vehicle" by the 77% and the
                   # cultures. Kept non-trivial (rule 3): an unlisted account — e.g. a shared upstream source —
                   # could partly reproduce the pattern.
t_se = 0.8         # cap = min trust_score over {O-25, O-26, O-27} = 0.83 (all via S-20). Docked lightly to 0.8
                   # for the vehicle-identification / ascertainment selection effect A-8 flags on the raw
                   # attribution figures (O-25/O-26); dock kept small because O-27 is direct microbiology immune
                   # to that bias and the signals span independent data streams (1973-84 national, 1985-87 NE,
                   # plant cultures).
evidence("HC-12", ["O-25", "O-26", "O-27"], [lik_se_H11, lik_se_H12, lik_se_H58], t=t_se)
```
