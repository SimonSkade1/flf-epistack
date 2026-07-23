---
type: correlation-group
id: CG-20
to: "[[HC-6 - Effect of egg-egg-cholesterol intake on the atherogenic blood-lipid profile]]"
members:
  - "[[E-18 - O-50 x HC-6 — eggs lowered LDL-C less than high-carb breakfast]]"
  - "[[E-19 - O-51 x HC-6 — HDL-TG-nonHDL null between egg and high-carb]]"
---

Joint likelihood for correlated observations O-50, O-51 (shared basis: S-57). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-20 (HC-6) — ONE joint estimate over O-50 + O-51, both from Maki 2020 (S-57, shared basis), rule 1.
# Pattern whole: in metabolic-syndrome/prediabetes adults, eggs lowered LDL-C LESS than an energy-matched
# high-carb breakfast (-2.9% vs -6.0%, between-diet P=0.023) but LDL still FELL ~3.5 mg/dL absolutely;
# HDL/TG/non-HDL/hs-CRP did not differ. Members in HC-6.hypotheses order [H-20, H-34, H-40, H-53]. Anchored
# on H-20 (rule 7): a comparator-relative LDL worsening with LDL still falling absolutely is its signature.
lik_maki_H20 = 1.0    # anchor: eggs leaving a smaller LDL decrease than a high-carb comparator, in exactly
                      # the dysglycemic population H-20 names, is its defining pattern
lik_maki_H34 = 0.5    # 0.5×: the comparator gap is loosely consistent with H-34 (eggs add cholesterol,
                      # blunting the drop), but LDL FELL absolutely on eggs — against H-34's absolute-rise
                      # claim (A-15 corrected: observed change far below the +7.4 mg/dL dose-response
                      # prediction, though the between-condition design can't isolate the egg effect from
                      # the comparator's carb effect). Flat HDL (O-51) fits H-34
lik_maki_H40 = 0.35   # 0.35×: eggs did comparator-WORSE on LDL and HDL was flat (O-51, E-19) — both against
                      # the net-favourable reading; only "LDL didn't rise absolutely" fits. Non-CRD
                      # background excuses the missing HDL rise, but the comparator-relative worsening is
                      # specifically against "favourable", so below H-34
lik_maki_H53 = 0.45   # 0.45×: unlisted effect, unconstrained — could accommodate "eggs mildly worse LDL,
                      # rest flat"; middling (rule 3)
t_maki = 0.56         # cap = min trust over {O-50,O-51} = S-57 = 0.62; docked for the discrimination
                      # resting on a single borderline, uncorrected between-diet P=0.023 in n=30 completers
                      # (the "eggs worse" gap could be noise), a raw-data→observation fragility
evidence("HC-6", ["O-50", "O-51"], [lik_maki_H20, lik_maki_H34, lik_maki_H40, lik_maki_H53], t=t_maki)
```
