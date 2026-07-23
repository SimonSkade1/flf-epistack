---
id: E-96
type: evidence-link
from: "[[O-57 - The E-value is the minimum RR-scale confounder strength needed to fully explain away an observed association]]"
to: "[[HC-15 - Whether nutritional-cohort associations can support causal egg-health claims]]"
arguments:
  - "[[A-20 - The closed-form E-value formula shows small cohort hazard ratios need only modest unmeasured confounding to be explained away]]"
---
![[O-57 - The E-value is the minimum RR-scale confounder strength needed to fully explain away an observed association]]

## Why this is evidence
The E-value turns the confounding worry into a threshold. The egg-cohort estimates are small (HR ~1.06-1.14), so their E-values are small: a modest unmeasured healthy-user confounder would suffice to nullify them. H-31 reads this as the associations being within reach of plausible residual confounding (cannot carry causal weight); H-41 holds that replication across differently-confounded cohorts plus this same sensitivity analysis shows well-conducted estimates survive.

## Likelihood

```python
# E-96 (HC-15) — lone edge, one observation O-57 "E-value threshold". Discriminating content (via A-20 approved/
# checked): small egg-cohort HRs (~1.06-1.14) have small E-values (~1.5-1.7), so a modest unmeasured healthy-user
# confounder suffices to null them. Members in HC-15.hypotheses order [H-31 reform/cannot; H-41 defence/can;
# H-59 residual intermediate]. Anchored on H-31 = 1 (best fit); others as ratios (rule 7). Condition strictly on H.
lik_evalue_H31 = 1.0   # anchor: the reform pole (associations are within reach of plausible residual confounding,
                       # cannot carry causal weight) directly predicts the tiny egg HRs sitting at small E-values
lik_evalue_H41 = 0.5   # 0.5x: the strong defence pole must invoke replication across differently-confounded cohorts
                       # + this same sensitivity analysis to argue survival; tiny-HR eggs are exactly the regime where
                       # a small E-value is least reassuring for a policy-grade claim. Not lower: the E-value framework
                       # is itself a manageability tool defenders embrace
lik_evalue_H59 = 0.85  # 0.85x: the intermediate view (cohorts reliable only for LARGE effects, not tiny egg HRs)
                       # predicts small-E-value fragility nearly as well as H-31; unconstrained middle, slightly under
t_evalue = 0.83        # cap = trust_score(O-57 via S-94) = 0.83; O-57 is a checked mathematical identity (A-20
                       # approved/checked), no raw-data->observation weakness to dock for
evidence("HC-15", ["O-57"], [lik_evalue_H31, lik_evalue_H41, lik_evalue_H59], t=t_evalue)
```
