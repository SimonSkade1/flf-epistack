---
id: E-77
type: evidence-link
from: "[[O-45 - Significant egg x type-2-diabetes interaction on CVD in Harvard cohorts, though stratum-specific egg-CVD HRs were null]]"
to: "[[HC-4 - Cardiometabolic effect of eggs in people with diabetes, prediabetes, or metabolic syndrome]]"
---
![[O-45 - Significant egg x type-2-diabetes interaction on CVD in Harvard cohorts, though stratum-specific egg-CVD HRs were null]]

## Why this is evidence
A significant egg-by-T2D interaction on CVD is what H-24 (harm specific to diabetics) predicts and what the safe pole (H-4/H-19, no differential effect by diabetes status) does not. But both the diabetic and non-diabetic stratum HRs were individually null, so this is weak, direction-only support for H-24.

## Likelihood

```python
# E-77 (HC-4) — lone edge, one observation O-45: a significant egg x T2D interaction on CVD (P<0.001) in the
# Harvard cohorts, but BOTH stratum HRs individually null (T2D 1.06, non-T2D 0.93); T2D the only significant
# modifier among ~10 tested. Anchored on H-24 = 1.0 (rule 7). Members in HC-4.hypotheses order.
lik_dc_int_H24 = 1.0   # anchor: a significant egg x diabetes interaction is the direction H-24 predicts — but
                       # weak, direction-only, since the diabetic stratum HR is itself null (E-77 body)
lik_dc_int_H33 = 0.85  # 0.85x: the harm mechanism predicts the same interaction; just below H-24 because the
                       # null diabetic-stratum HR gives no positive lipid-mediated signal H-33 wants
lik_dc_int_H4  = 0.5   # 0.5x: H-4 predicts NO interaction (against), yet both strata being null (no egg-CVD
                       # association anywhere) is strongly consistent with it — the two roughly offset
lik_dc_int_H19 = 0.5   # 0.5x: same as H-4 on this CVD observation — safe pole penalised by the interaction, aided by null strata
lik_dc_int_H52 = 0.6   # 0.6x: unlisted effect — an interaction with null strata neither predicted nor forbidden; middling (rule 3)
t_dc_int = 0.75        # cap = trust S-19 0.82; docked for multiplicity — T2D was the ONLY significant modifier
                       # among ~10 interaction tests, so the interaction's significance carries look-elsewhere inflation
evidence("HC-4", ["O-45"], [lik_dc_int_H4, lik_dc_int_H19, lik_dc_int_H24, lik_dc_int_H33, lik_dc_int_H52], t=t_dc_int)
```
