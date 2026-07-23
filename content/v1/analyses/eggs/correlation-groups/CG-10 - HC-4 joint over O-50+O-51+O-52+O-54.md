---
type: correlation-group
id: CG-10
to: "[[HC-4 - Cardiometabolic effect of eggs in people with diabetes, prediabetes, or metabolic syndrome]]"
members:
  - "[[E-79 - O-50 x HC-4 — eggs less LDL-lowering than high-carb breakfast]]"
  - "[[E-80 - O-51 x HC-4 — non-HDL, HDL, TG, CRP null egg vs high-carb]]"
  - "[[E-81 - O-52 x HC-4 — HOMA-IR favored eggs over high-carb breakfast]]"
  - "[[E-82 - O-54 x HC-4 — systolic BP fell more on egg breakfast]]"
---

Joint likelihood for correlated observations O-50, O-51, O-52, O-54 (shared basis: S-57). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-10 (HC-4) — ONE joint estimate over E-79+E-80+E-81+E-82: O-50 (eggs less LDL-lowering than high-carb),
# O-51 (HDL/TG/nonHDL/hsCRP null), O-52 (HOMA-IR rose far less on eggs), O-54 (SBP fell more on eggs), all
# from the Maki 2020 crossover (S-57), priced jointly (rule 1). Whole pattern: eggs modestly worse on LDL vs
# the high-carb comparator but markedly better on insulin resistance + BP, neutral elsewhere.
# Anchored on H-19 = 1.0 (rule 7). Members in HC-4.hypotheses order.
lik_maki_H19 = 1.0   # anchor: this IS the substitution design — the large HOMA-IR advantage (O-52) is exactly
                     # H-19's prediction; SBP/other-lipid results consistent; silent on LDL
lik_maki_H4  = 0.7   # 0.7x: broad neutrality fits the nulls, but the SIGNIFICANT HOMA-IR + SBP benefits go
                     # beyond "neutral"; the LDL between-condition gap is mostly the comparator's carb effect
                     # (A-15 corrected: egg-attributable LDL worsening small), so it barely dents H-4
lik_maki_H24 = 0.4   # 0.4x: net-favorable surrogate profile (HOMA-IR, SBP down) runs against the harm pole;
                     # H-24 is endpoint-level so only weakly bears on surrogates
lik_maki_H33 = 0.42  # 0.42x: gets its one hit from O-50 (eggs less LDL-favorable) but O-51 non-HDL/hsCRP null
                     # contradicts its atherogenic-marker prediction and A-15 attributes the LDL gap to carbs
lik_maki_H52 = 0.55  # 0.55x: unlisted effect — the active HOMA-IR/SBP benefits are consistent with a residual
                     # net-benefit (per E-82 body); middling (rule 3)
t_maki = 0.62        # cap = min trust over {O-50,O-51,O-52,O-54} = S-57 0.62; kept at cap — n=30 own-control
                     # crossover, % changes directly reported (small n already in the trust score)
evidence("HC-4", ["O-50", "O-51", "O-52", "O-54"], [lik_maki_H4, lik_maki_H19, lik_maki_H24, lik_maki_H33, lik_maki_H52], t=t_maki)
```
