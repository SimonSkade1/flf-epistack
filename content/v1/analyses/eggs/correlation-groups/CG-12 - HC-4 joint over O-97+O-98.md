---
type: correlation-group
id: CG-12
to: "[[HC-4 - Cardiometabolic effect of eggs in people with diabetes, prediabetes, or metabolic syndrome]]"
members:
  - "[[E-85 - O-97 x HC-4 — 3 eggs-day raised HDL-C in metabolic-syndrome men]]"
  - "[[E-86 - O-98 x HC-4 — LDL-C and LDL-HDL ratio unchanged incl hyper-absorbers]]"
---

Joint likelihood for correlated observations O-97, O-98 (shared basis: S-67). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-12 (HC-4) — ONE joint estimate over E-85+E-86: O-97 (3 eggs/day raised HDL-C, egg-substitute did not)
# and O-98 (LDL-C and LDL:HDL ratio held, incl. hyper-absorbers, despite 640 mg/day cholesterol), both from
# Mutungi 2008 (S-67), priced jointly (rule 1). Population = metabolic-syndrome/overweight men on CRD (in
# HC-4 scope). Whole pattern: HDL up, atherogenic ratio preserved across absorber phenotypes = neutral-to-
# favorable lipid response. Anchored on H-4 = 1.0 (rule 7). Members in HC-4.hypotheses order.
lik_mut_H4  = 1.0   # anchor: LDL held + ratio preserved (O-98) is exactly H-4's lipid safety; HDL rise is
                    # favorable and comfortably within "does not harm lipids" (A-34 approved: neutral-to-favorable)
lik_mut_H19 = 0.75  # 0.75x: H-19 is silent on lipids (glycemic member); a favorable/neutral lipid result is
                    # consistent but not its own prediction
lik_mut_H24 = 0.5   # 0.5x: no CVD endpoint here; the favorable surrogate lipids mildly oppose the harm pole,
                    # but H-24 is endpoint-level so only weakly constrained by these
lik_mut_H33 = 0.18  # 0.18x: strongest single refutation — LDL and LDL:HDL held even in hyper-absorbers under
                    # 640 mg/day added cholesterol (O-98), directly against H-33's atherogenic-handling prediction (E-86 body)
lik_mut_H52 = 0.6   # 0.6x: HDL rise is consistent with a residual net-benefit; middling-to-slightly-favorable (rule 3)
t_mut = 0.55        # cap = min trust over {O-97,O-98} = S-67 0.55; kept at cap — O-97's egg-substitute control
                    # isolates the egg-attributable HDL rise; CRD-background HDL confound is a sign/size caveat
                    # (A-34), already reflected by not over-crediting HDL, not a data-reliability defect
evidence("HC-4", ["O-97", "O-98"], [lik_mut_H4, lik_mut_H19, lik_mut_H24, lik_mut_H33, lik_mut_H52], t=t_mut)
```
