---
type: correlation-group
id: CG-9
to: "[[HC-4 - Cardiometabolic effect of eggs in people with diabetes, prediabetes, or metabolic syndrome]]"
members:
  - "[[E-74 - O-4 x HC-4 — no HDL-C difference in 3-month egg RCT (prediabetes-T2D)]]"
  - "[[E-75 - O-5 x HC-4 — null TC-LDL-TG in 3-month egg RCT (prediabetes-T2D)]]"
  - "[[E-76 - O-6 x HC-4 — no glycemic-control difference in 3-month egg RCT]]"
---

Joint likelihood for correlated observations O-4, O-5, O-6 (shared basis: D-3). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-9 (HC-4) — ONE joint estimate over E-74+E-75+E-76: O-4 (null HDL-C), O-5 (null TC/LDL/TG),
# O-6 (null glycemic) all rest on the DIABEGG 3-mo RCT (S-26, basis D-3), so priced jointly (rule 1).
# Pattern judged whole: a complete surrogate null (lipids + glycemia) at ~12 eggs/wk in prediabetes/T2D.
# Anchored on H-4 = 1.0; others as ratios (rule 7). Members in HC-4.hypotheses order.
lik_diabegg_H4  = 1.0   # anchor: broad surrogate lipid/glycemic neutrality predicts EXACTLY this joint null
lik_diabegg_H19 = 0.9   # 0.9x: "improves or does not worsen" glycemia — the glycemic null is fully consistent
                        # and lipids are neutral for it; just short of H-4, which tailors all three nulls
lik_diabegg_H24 = 0.55  # 0.55x: endpoint-level CVD harm needn't leave a 3-mo surrogate footprint, so a null is
                        # compatible but less expected than under the safe pole (per E-76 body)
lik_diabegg_H33 = 0.25  # 0.25x: this member predicts an adverse LDL/TC shift in diabetics; a pre-specified lipid
                        # null in exactly this population is strong counter-evidence. Not lower: A-2 (approved)
                        # caps the null — both arms matched on MUFA/PUFA background, biasing toward null
lik_diabegg_H52 = 0.5   # 0.5x: unlisted net effect, unconstrained — a surrogate null neither predicted nor forbidden (rule 3)
t_diabegg = 0.7         # cap = min trust over {O-4,O-5,O-6} = S-26 0.7; kept at cap — the null DIRECTION is the
                        # headline abstract result (O-5/O-6 depth-limited only on exact per-arm values, not the sign)
evidence("HC-4", ["O-4", "O-5", "O-6"], [lik_diabegg_H4, lik_diabegg_H19, lik_diabegg_H24, lik_diabegg_H33, lik_diabegg_H52], t=t_diabegg)
```
