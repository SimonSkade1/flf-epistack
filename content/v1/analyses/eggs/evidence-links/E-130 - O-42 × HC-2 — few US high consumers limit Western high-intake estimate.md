---
id: E-130
type: evidence-link
from: "[[O-42 - Only 8 percent of participants ate at least one egg serving per day in the pooled US cohorts]]"
to: "[[HC-2 - Regional-population modification of the egg-cardiovascular association]]"
arguments:
  - "[[A-14 - Full-serving-per-day substitution benefits apply only to the small high-intake minority, so population impact of cutting eggs is smaller]]"
---
![[O-42 - Only 8 percent of participants ate at least one egg serving per day in the pooled US cohorts]]

## Why this is evidence

In the pooled US cohorts only 8% eat >=1 egg/day, so the Western estimates carry little information at higher intakes. This supports H-50's exposure-range / statistical-power origin of the region contrast (the West cannot resolve high-intake effects); H-22 and H-7 do not predict it.

## Likelihood

```python
# E-130 (HC-2) — lone edge, one observation O-42 "in pooled US cohorts 58.5% eat >=1 egg/week but only 8.0%
# eat >=1 egg/day — the West carries little information at higher intakes." Members in HC-2.hypotheses order
# [H-7, H-22, H-50]. Anchored on H-50 = 1 (best fit); others as ratios (rule 7).
lik_o42_H50 = 1.0   # anchor: the West's sparse high-intake data is exactly H-50's exposure-range / statistical-
                    # power origin of the region contrast — the Western "null" is partly non-informativeness
                    # (cannot resolve high-intake effects), not a genuine regional difference; A-14 (approved)
                    # confirms the per-day estimates rest on the 8% high-intake minority
lik_o42_H22 = 0.6   # 0.6×: genuine region-modification does not predict/need the Western null to stem from
                    # sparse high-intake sampling; this observation supplies a power-artefact alternative to
                    # H-22's "genuinely null in the West," mildly against
lik_o42_H7  = 0.7   # 0.7×: H-7 concerns the ASIAN inverse being confounding and is largely silent on Western
                    # exposure ranges — roughly neutral; slightly above H-22 because H-7 stakes no claim on
                    # the West being a genuine null that this power-artefact could undercut
t_o42 = 0.62        # cap = trust_score of O-42's source S-89 = 0.62. O-42 is a simple descriptive intake-
                    # distribution tabulation (% consuming), reliable at the source level; no dock, at cap
evidence("HC-2", ["O-42"], [lik_o42_H7, lik_o42_H22, lik_o42_H50], t=t_o42)
```
