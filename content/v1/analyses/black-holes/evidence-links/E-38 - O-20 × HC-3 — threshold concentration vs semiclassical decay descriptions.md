---
id: E-38
type: evidence-link
from: "[[O-20 - LHC parton luminosities fall steeply with invariant mass, concentrating any threshold process just above threshold]]"
to: "[[HC-3 - Nature and decay of an LHC-produced strong-gravity object]]"
arguments:
  - "[[A-11 - Thermality criteria require black-hole masses several times the Planck scale, out of reach of near-threshold LHC production]]"
---
![[O-20 - LHC parton luminosities fall steeply with invariant mass, concentrating any threshold process just above threshold]]

## Why this is evidence

The parton-luminosity fact itself is theory-independent; the discrimination runs through what it entails about the produced population: any LHC strong-gravity object sits just above production threshold, i.e. at masses comparable to the quantum-gravity scale. H-14 predicts exactly this — low-entropy near-threshold states outside the thermal regime — so the observation is central and expected on it. H-10 and H-7 both describe the object with semiclassical evaporation formulas (canonical and microcanonical respectively) whose validity requires the mass to sit well above the fundamental scale; the observation says the objects actually produced are concentrated where those descriptions are least trustworthy. Direction: toward H-14 and toward doubting that either semiclassical decay law describes what the LHC would actually make.

## Likelihood

```python
# E-38 (HC-3) — lone edge, one observation O-20 "steeply falling parton luminosities concentrate any
# threshold process just above threshold" (external global-fit PDFs). Per `## Why this is evidence`, this
# pins produced objects to masses ~ the quantum-gravity scale. H-14 (low-entropy near-threshold non-thermal
# state) predicts exactly this — anchor at 1 (rule 7). H-10 (canonical) and H-7 (microcanonical) both use
# SEMICLASSICAL evaporation laws whose validity needs M well above the fundamental scale; A-11 (approved):
# thermality criteria demand xmin~3–16 (≫1), and steep luminosities rate-suppress such production, so what is
# made sits where semiclassical descriptions are least trustworthy — against both. A-8 (approved) reinforces
# that sub-M_min objects fall outside the semiclassical regime. H-24 is non-thermal by construction, so
# near-threshold concentration does not disfavour it.
lik_thr_H7  = 0.45   # 0.45×: microcanonical semiclassical law least trustworthy near threshold (A-11) — disfavoured
lik_thr_H10 = 0.5    # 0.5×: canonical thermal description fails the xmin criteria near threshold (A-11) — disfavoured
lik_thr_H14 = 1.0    # anchor: near-threshold non-thermal state is exactly what the observation predicts
lik_thr_H24 = 0.85   # non-thermal by construction; a near-threshold quantum object is compatible — mildly consistent
lik_thr_H35 = 0.8    # unlisted behaviour, unconstrained; near-threshold favours non-semiclassical fates, so
                     # middling-to-mild rather than strongly for or against (rule 3)
t_thr = 0.8          # cap = trust_score of O-20's source S-50 = 0.8; PDFs are external global-fit data, very
                     # reliable, so no dock below the cap (rule 4)
evidence("HC-3", ["O-20"], [lik_thr_H7, lik_thr_H10, lik_thr_H14, lik_thr_H24, lik_thr_H35], t=t_thr)
```
