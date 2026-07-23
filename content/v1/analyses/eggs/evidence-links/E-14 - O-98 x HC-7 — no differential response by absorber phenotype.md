---
id: E-14
type: evidence-link
from: "[[O-98 - LDL-C and the LDL-HDL ratio did not change with egg intake, including in dietary-cholesterol hyper-absorbers]]"
to: "[[HC-7 - Nature of inter-individual variation in cholesterol response to dietary cholesterol]]"
arguments:
  - "[[A-34 - HDL rose while LDL and the LDL-HDL ratio held across absorber phenotypes, so the egg lipid effect is neutral-to-favorable rather than atherogenic]]"
---
![[O-98 - LDL-C and the LDL-HDL ratio did not change with egg intake, including in dietary-cholesterol hyper-absorbers]]

## Why this is evidence
Hyper-absorbers of dietary cholesterol showing no more LDL rise than hypo-absorbers is what H-2 predicts (synthesis-side feedback still buffers even when absorption is high). It argues against H-1's discrete responder minority being identifiable by absorption phenotype, and against the H-55 reading in which an absorption determinant dominates the response structure.

## Likelihood

```python
# E-14 (HC-7) — lone edge, one observation O-98: adding 3 whole eggs/day (~640 mg cholesterol/day) did not
# change LDL-C or the LDL:HDL ratio, and the ratio held similarly in dietary-cholesterol hyper- AND
# hypo-absorbers (S-67, Mutungi 2008, small n, carbohydrate-restricted background). Members in
# HC-7.hypotheses order [H-1, H-2, H-35, H-36, H-55]. Anchored on H-2 = 1.0. A-34 (approved) is about the
# atherogenicity classification (a different cluster); for HC-7 the load-bearing content is the
# absorber-stratified null.
lik_absorber_H2 = 1.0    # anchor: no more LDL rise in hyper-absorbers than hypo-absorbers is what H-2 predicts
                         # — synthesis-side feedback still buffers even when fractional absorption is high
lik_absorber_H1 = 0.55   # 0.55x: an absorber-stratified null does not directly refute a hypo/hyper split (H-1's
                         # responders are not defined by absorption phenotype); mildly below middling because no
                         # visible hyper-responding subgroup emerged
lik_absorber_H35 = 0.65  # 0.65x: a continuous trait centred near zero is compatible with the overall no-LDL-rise,
                         # but H-35 does not specifically predict the absorber-stratified pattern
lik_absorber_H36 = 0.6   # 0.6x: O-98 concerns absorber phenotype, not ApoE — roughly orthogonal to H-36, with
                         # only mild thematic consistency with "a phenotype fails to tag responders"
lik_absorber_H55 = 0.45  # 0.45x: residual real but below middling — its "an absorption determinant dominates the
                         # response structure" sub-reading is argued against by the no-difference-by-absorber
                         # result; other sub-readings stay neutral
t_absorber = 0.45        # cap = trust_score(S-67) = 0.55; docked: small n with a small hyper-absorber subgroup,
                         # and a carbohydrate-restricted background that independently moves lipids, confounding
                         # the step from the data to a clean "egg effect" statement
evidence("HC-7", ["O-98"], [lik_absorber_H1, lik_absorber_H2, lik_absorber_H35, lik_absorber_H36, lik_absorber_H55], t=t_absorber)
```
