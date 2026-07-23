---
id: E-13
type: evidence-link
from: "[[O-81 - APOE genotype did not modify the LDL-C response to dietary cholesterol (or trans-fat) in a pooled n=395 feeding dataset]]"
to: "[[HC-7 - Nature of inter-individual variation in cholesterol response to dietary cholesterol]]"
arguments:
  - "[[A-28 - Small, CI-crossing genotype effects for fat and cafestol and none for dietary cholesterol imply APOE genotyping has little practical value for identifying diet-responders]]"
---
![[O-81 - APOE genotype did not modify the LDL-C response to dietary cholesterol (or trans-fat) in a pooled n=395 feeding dataset]]

## Why this is evidence
The largest pooled-genotype feeding dataset showing no ApoE-genotype difference in the dietary-cholesterol response is H-36's core prediction. It argues against the reading of H-55 in which ApoE genotype is the dominant measured determinant that tags hyper-responders. H-1/H-2/H-35 make no ApoE prediction.

## Likelihood

```python
# E-13 (HC-7) — lone edge, one observation O-81: in a pooled n=395 controlled-feeding reanalysis, APOE
# genotype did not modify the LDL-C/serum-cholesterol response to a dietary-cholesterol (or trans-fat)
# challenge (S-62, Weggemans 2001). Members in HC-7.hypotheses order [H-1, H-2, H-35, H-36, H-55]. Anchored
# on H-36 = 1.0 (core prediction). A-28 (approved) used as reasoning: even the fat/cafestol genotype effects
# are small, CI-crossing and opposite-signed while dietary cholesterol shows none, so ApoE carries little
# responder-discriminating information — exactly H-36.
lik_apoe_H36 = 1.0  # anchor: the largest pooled-genotype feeding dataset showing NO ApoE difference for the
                    # dietary-cholesterol challenge is H-36's core prediction; A-28 (approved) reinforces it
lik_apoe_H1 = 0.55  # 0.55x: H-1 makes no ApoE prediction — a hypo/hyper split need not be ApoE-tagged, so
                    # O-81 is roughly neutral for it (marginal level)
lik_apoe_H2 = 0.55  # 0.55x: H-2 makes no ApoE prediction; neutral/marginal
lik_apoe_H35 = 0.6  # 0.6x: H-35 makes no direct ApoE prediction, but a continuous polygenic trait is mildly
                    # consistent with the absence of a single-locus tag, so a hair above the other agnostics
lik_apoe_H55 = 0.4  # 0.4x: residual real but below middling — its "ApoE genotype is the dominant measured
                    # determinant that tags hyper-responders" sub-reading is directly contradicted by the null;
                    # a different-determinant or noise reading stays neutral
t_apoe = 0.52       # cap = trust_score(S-62) = 0.60; docked slightly: extracted from abstract + step-2 summary
                    # (full text paywalled), retrospective genotyping on pooled heterogeneous feeding trials
evidence("HC-7", ["O-81"], [lik_apoe_H1, lik_apoe_H2, lik_apoe_H35, lik_apoe_H36, lik_apoe_H55], t=t_apoe)
```
