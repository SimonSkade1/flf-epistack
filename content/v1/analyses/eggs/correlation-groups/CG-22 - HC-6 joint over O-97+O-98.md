---
type: correlation-group
id: CG-22
to: "[[HC-6 - Effect of egg-egg-cholesterol intake on the atherogenic blood-lipid profile]]"
members:
  - "[[E-26 - O-97 x HC-6 — 3 whole eggs-day raised HDL-C on carb-restricted diet]]"
  - "[[E-27 - O-98 x HC-6 — LDL-C and LDL-HDL ratio unchanged incl hyper-absorbers]]"
---

Joint likelihood for correlated observations O-97, O-98 (shared basis: S-67). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-22 (HC-6) — ONE joint estimate over O-97 + O-98, both from Mutungi 2008 (S-67, shared basis), rule 1.
# Pattern whole: on a carbohydrate-restricted background, 3 whole eggs/day (640 mg added cholesterol)
# raised HDL-C (egg-substitute arm did not) while LDL-C and the LDL:HDL ratio were unchanged, including in
# hyper-absorbers. Members in HC-6.hypotheses order [H-20, H-34, H-40, H-53]. Anchored on H-40 (rule 7):
# this is its defining study and context — HDL up, LDL:HDL preserved even in hyper-absorbers, on a
# carb-restricted diet.
lik_mutungi_H40 = 1.0    # anchor: exactly H-40. A-34 (approved): HDL rose while LDL:HDL held across absorber
                         # phenotypes → egg lipid effect neutral-to-favourable, not atherogenic. Egg-specific
                         # (substitute arm's flat HDL isolates it from the CRD background)
lik_mutungi_H34 = 0.25   # 0.25×: H-34 predicts ~+9 mg/dL LDL from 640 mg added cholesterol — not seen, even
                         # in hyper-absorbers (O-98), and HDL rose (H-34 expects HDL spared). Against, but
                         # softened by small n (28) and possible CRD/homeostatic blunting
lik_mutungi_H20 = 0.3    # 0.3×: not H-20's population/design (no high-carb comparator; the comparator is
                         # egg-substitute), and eggs did not worsen LDL vs substitute — against its "eggs
                         # worsen LDL" lean; roughly level with H-34
lik_mutungi_H53 = 0.4    # 0.4×: unlisted effect, unconstrained — could produce an HDL-up/LDL-preserved
                         # pattern; middling, but H-40 nails this specifically so residual is a poorer fit
                         # (rule 3)
t_mutungi = 0.5          # cap = min trust over {O-97,O-98} = S-67 = 0.55 (already low — egg-industry-funded
                         # Fernandez lab, small n); docked further for O-98's hyper-absorber subgroup claim
                         # resting on an underpowered n=28 split
evidence("HC-6", ["O-97", "O-98"], [lik_mutungi_H20, lik_mutungi_H34, lik_mutungi_H40, lik_mutungi_H53], t=t_mutungi)
```
