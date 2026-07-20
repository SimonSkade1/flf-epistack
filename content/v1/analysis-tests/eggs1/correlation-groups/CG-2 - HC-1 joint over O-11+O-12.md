---
type: correlation-group
id: CG-2
to: "[[HC-1 - Magnitude and mechanism of egg's effect on atherogenic blood lipids]]"
members:
  - "[[E-3 - O-11 × HC-1 — whole-egg cholesterol poorly absorbed]]"
  - "[[E-4 - O-12 × HC-1 — acute whole-egg meal did not raise plasma total cholesterol]]"
---

Joint likelihood for correlated observations O-11, O-12 (shared basis: S-19). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-2 (HC-1) - ONE joint estimate over E-3 + E-4: O-11 (whole-egg cholesterol poorly absorbed) and
# O-12 (acute whole-egg meal did not raise plasma TC) both come out of the same two-crossover S-19
# study, self-basis (rule 1). One witness: if S-19's absorption assay or its acute protocol is off,
# both halves fall together, so this is priced as a single pattern, not two updates.
# The pattern judged whole: a measured low absorption fraction AND a flat acute TC curve.
# Note the acute half carries almost no discriminating load - single-meal plasma TC is
# homeostatically buffered and is near-null under EVERY member including H-1 (S-19's own trust_reason
# says as much), so essentially all the discrimination here comes from the absorption measurement.
# These are H-5's own defining claims (its `source` IS S-19), so the ratios are deliberately kept
# modest: a hypothesis extracted from a study cannot be allowed to score a near-infinite likelihood
# on the very data it was read off, or the update is circular by construction.
# Anchored on H-5 = 1 (rule 7a).

lik_absorb_H5 = 1.0   # anchor: poor bioavailability of egg-matrix cholesterol is exactly this claim;
                      # under H-5 both halves are what you expect. Not treated as a perfect fit -
                      # H-5 also requires the deficit to be *specific to the egg matrix* vs other
                      # cholesterol sources, which a single-food study cannot establish.

lik_absorb_H1 = 0.30  # ~0.3x as expected as under H-5. H-1 needs absorption sufficient to drive a
                      # habitual ApoB rise, so a low measured absorption fraction is a genuine
                      # surprise for it. Not lower because (a) the acute-TC half is expected under
                      # H-1 too, (b) "poorly absorbed" is a relative verdict on a fractional measure
                      # (~50% typical) that can still deliver a chronic load, and (c) the ApoB claim
                      # is about habitual intake, which an acute design does not address at all.

lik_absorb_H8 = 0.55  # ~0.55x. H-8 explains the small effect by hepatic/homeostatic saturation, not
                      # malabsorption, so it does not predict O-11 - but neither does it forbid it:
                      # cholesterol absorption is itself down-regulated at high load, so a saturating
                      # account and a low measured absorption fraction sit together comfortably. The
                      # acute-TC null is fully expected under H-8. Its shortfall vs H-5 is that the
                      # mechanistic reading is not what H-8 points at, not that the data conflict.

lik_absorb_H11 = 0.60 # residual, unconstrained (rule 3). The main unlisted variants - "no lipid
                      # effect at all" and "effect runs via particle size / HDL rather than ApoB
                      # mass" - both sit fine with poor absorption and a flat acute TC; the no-effect
                      # variant positively predicts the acute null. Slightly above H-8 because it
                      # accommodates the pattern without owing an account of it, and well below the
                      # anchor because it does not specifically predict a low absorption fraction.

t_s19 = 0.45          # cap = trust_score of S-19 = 0.65 (both observations, same source). Docked
                      # below the cap for the step from raw data to the stated observations, not for
                      # truth: the absorption measurement's method could not be inspected, the design
                      # is acute so "poorly absorbed" is a single-meal fraction being read as a
                      # standing property, and the Campbell/Purdue lab has Egg Nutrition Center /
                      # American Egg Board funding on related papers (S-19.motivatedness), which bears
                      # on how a borderline absorption number gets framed. n and the analysis pipeline
                      # were not audited.

evidence("HC-1", ["O-11", "O-12"], [lik_absorb_H1, lik_absorb_H5, lik_absorb_H8, lik_absorb_H11], t=t_s19)
```
