---
id: E-37
type: evidence-link
from: "[[O-7 - Torsion-balance experiments limit the RS2 warping length L to below 44 microns]]"
to: "[[HC-3 - Nature and decay of an LHC-produced strong-gravity object]]"
arguments:
  - "[[A-9 - The allowed warping-length range up to 44 microns permits Casadio-Harms critical masses for which black-hole growth is catastrophic]]"
---
![[O-7 - Torsion-balance experiments limit the RS2 warping length L to below 44 microns]]

## Why this is evidence

H-7 is the only member whose decay law predicates on a specific geometry: microcanonical metastability requires an RS2 warped dimension of curvature length L, and longer lifetimes need larger L. RS2 predicts deviations from Newtonian gravity at ranges below L, so sub-millimeter torsion-balance tests could have detected — and progressively failed to detect — the regime H-7 needs: a Newtonian null down to 44 microns is less probable under H-7 (which requires some L that experiments were probing) than under H-10, H-14, or H-24, none of which needs any short-distance deviation. Direction: against H-7, though not decisively — the 15–44 micron window Plaga's quasistability argument uses remains open.

## Likelihood

```python
# E-37 (HC-3) — lone edge, one observation O-7 "torsion-balance Newtonian null down to L<44 microns
# (Kapner 2007)". Per `## Why this is evidence`, H-7 is the ONLY member whose decay law predicates on a
# specific RS2 warped geometry of curvature length L (longer lifetimes need larger L), and RS2 predicts
# sub-L deviations from Newtonian gravity that these tests probe. H-10, H-14, H-24 need no short-distance
# deviation, so a null is fully expected — anchor them at 1 (rule 7). A-9 (approved): the benign verdict
# rests on an unargued restriction to L~1 micron, and the 15.3–44 micron window remains experimentally OPEN,
# so the null docks H-7 (it excludes the L>44 micron slice it was probing) but is NOT decisive.
lik_null_H7  = 0.55  # null less expected under H-7: excludes the L>44 micron portion of H-7's geometry, but
                     # the operative 15.3–44 micron quasistability window (A-9) survives — partial, not decisive
lik_null_H10 = 1.0   # anchor: canonical decay needs no warped dimension, null expected
lik_null_H14 = 1.0   # near-threshold state needs no short-distance deviation, null expected
lik_null_H24 = 1.0   # stable neutral hole needs no warped dimension, null expected
lik_null_H35 = 0.85  # unlisted behaviour, unconstrained and mostly geometry-independent; mildly below 1
                     # since a slice of it could also require a detectable deviation (rule 3)
t_null = 0.30        # cap = trust_score of O-7's source S-30 (Plaga) = 0.30; the Kapner limit itself is a
                     # firmly established experimental datum, so no dock below the (already low) cap (rule 4)
evidence("HC-3", ["O-7"], [lik_null_H7, lik_null_H10, lik_null_H14, lik_null_H24, lik_null_H35], t=t_null)
```
