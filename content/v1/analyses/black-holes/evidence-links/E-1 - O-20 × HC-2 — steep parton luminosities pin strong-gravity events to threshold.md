---
id: E-1
type: evidence-link
from: "[[O-20 - LHC parton luminosities fall steeply with invariant mass, concentrating any threshold process just above threshold]]"
to: "[[HC-2 - Dominant collider manifestation of low-scale quantum gravity]]"
arguments:
  - "[[A-11 - Thermality criteria require black-hole masses several times the Planck scale, out of reach of near-threshold LHC production]]"
---
![[O-20 - LHC parton luminosities fall steeply with invariant mass, concentrating any threshold process just above threshold]]

## Why this is evidence

H-15 predicts exactly this regime: with production overwhelmingly concentrated just above the accessible threshold, the first strong-gravity events sit at the lowest mass scale, where a semiclassical thermal multiparticle black hole cannot yet form and the signal is instead an enhancement of transverse two-body final states. H-3's advertised dominant manifestation — copious thermal black holes with high multiplicity — requires events well above the fundamental scale, which the steeply falling parton luminosities suppress; if that signature were nonetheless the first and dominant one, one would expect substantial parton luminosity well above threshold rather than the observed steep fall. H-5's few reconstructable graviton resonances sit at fixed masses and are less affected either way, so the observation separates H-15 from H-3 in particular (toward H-15).

## Likelihood

```python
# E-1 (HC-2) — lone edge, one observation O-20 "steeply falling parton luminosities concentrate any
# above-threshold process just above its threshold". Members in HC-2.hypotheses order:
# [H-3 black holes + Regge, H-5 RS1 spin-2 graviton resonances, H-15 two-body enhancement first, H-34 residual].
# Anchored on H-15 = 1 (rule 7): H-15 is the member the observation directly predicts, so it is the
# natural unit; every other member priced as "how expected is this exact luminosity shape if that member
# were the dominant first signature instead".
lik_lumi_H15 = 1.0   # anchor: H-15 IS the near-threshold regime — production piled just above threshold is
                     # exactly where a sub-thermal two-body/contact enhancement, not a thermal object,
                     # appears first. The steep fall is what this member predicts.
lik_lumi_H3  = 0.3   # 0.3× vs anchor: for H-3's advertised dominant signature (copious high-multiplicity
                     # thermal black holes) to be the FIRST thing seen you need substantial luminosity
                     # well above the scale; the observed steep fall makes that comparatively surprising.
                     # A-11 (approved) sharpens the dock — thermality criteria need xmin ~ 3-16 above the
                     # Planck scale, exactly the rate-suppressed tail, so near-threshold objects aren't the
                     # thermal BHs H-3 advertises. Not zero: H-3 is still a live strong-gravity world.
lik_lumi_H5  = 0.7   # 0.7×: H-5's KK-graviton bumps sit at fixed masses and are, per the body, "less
                     # affected either way" — the luminosity shape neither predicts nor forbids them, so a
                     # middling value between the predicted anchor and the disfavoured H-3, not near either.
lik_lumi_H34 = 0.6   # 0.6×: unlisted first signature, unconstrained — could sit near or above threshold, so
                     # neither predicts nor forbids the steep-fall pattern (rule 3). Lower would assert no
                     # unlisted signature is compatible with threshold-dominated production, which I don't know.
t_lumi = 0.8         # cap = trust_score of O-20's source S-50 = 0.8. Held at the cap: O-20 is a firmly
                     # established property of externally global-fit proton PDFs (not this paper's own
                     # measurement), with no measurement/selection/pipeline weakness between the raw PDF
                     # data and the stated luminosity fall to dock for.
evidence("HC-2", ["O-20"], [lik_lumi_H3, lik_lumi_H5, lik_lumi_H15, lik_lumi_H34], t=t_lumi)
```
