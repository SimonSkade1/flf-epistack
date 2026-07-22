---
id: HC-1
type: hypothesis-cluster
question: "What is the structure and fundamental scale of gravity at short distances — is the quantum-gravity scale within LHC reach?"
hypotheses:
  - "[[H-2 - TeV-scale type-I string theory with large extra dimensions solves the hierarchy problem]]"
  - "[[H-4 - A single warped extra dimension (RS1) generates the weak-Planck hierarchy exponentially]]"
  - "[[H-27 - Under standard gravity, collider collisions are at least 22 orders of magnitude too weak to form a black hole]]"
  - "[[H-33 - The short-distance structure of gravity is something not listed here]]"
exclusivity: "Each member names a different short-distance completion of gravity — ordinary Einstein gravity with a Planckian fundamental scale, large flat extra dimensions, or a single warped dimension; nature realizes at most one."
exhaustive_by_construction: false
independence: "What gravity is at short distances is fundamental physics that does not shift the base rates of the astrophysical, strange-matter, monopole, or vacuum clusters."
depends_on: []
relevance: "Black-hole production at the LHC is possible at all only if the fundamental gravity scale sits within collider reach — this cluster is the gate to the whole black-hole branch of the main question."
---
![[H-2 - TeV-scale type-I string theory with large extra dimensions solves the hierarchy problem]]
![[H-4 - A single warped extra dimension (RS1) generates the weak-Planck hierarchy exponentially]]
![[H-27 - Under standard gravity, collider collisions are at least 22 orders of magnitude too weak to form a black hole]]
![[H-33 - The short-distance structure of gravity is something not listed here]]

The members carve the space of short-distance completions of gravity: the ordinary Planckian-scale answer (on which collider collisions are hopelessly far from gravitational collapse), the two low-scale scenarios the corpus proposes (large flat extra dimensions with a TeV string scale; one warped dimension), and a residual for any completion not stated in this literature. Exclusivity holds because these are incompatible claims about the same underlying geometry; the cluster is not exhaustive by construction (other low-scale mechanisms exist in principle), so the residual closes it. Torsion-balance limits, the absence-of-constraints situation of the late nineties, and collider null results are the discriminating evidence.

## Prior

```python
# HC-1 prior — short-distance structure / fundamental scale of gravity: is the QG scale within LHC reach?
# Members in HC-1.hypotheses order:
# [H-2 ADD / TeV-string large flat extra dimensions, H-4 RS1 single warped dimension,
#  H-27 ordinary Einstein gravity with a Planckian fundamental scale, H-33 residual].
# Inputs: the outside view on weak-scale naturalness solutions; one base-rate observation pulled into the
# prior (O-43 via E-25, now used_for_prior: true — gravity untested below ~1 cm in 1998, 33 orders above the
# Planck length — so step 8 skips it); and the cluster's no-observation arguments from
# `no_observation_arguments.py <dir> --cluster HC-1` (A-3, A-4, A-5, A-54, A-62; all approved/corrected).
# The case-specific discriminators — the torsion-balance null (E-28) and the 1998 survival-of-constraints
# datum (E-29) — are left UNMARKED for step 8.

# H-27 ordinary Einstein gravity, Planckian fundamental scale — the anchor (unit weight). Outside view: the
# Planck scale (~1e19 GeV) is the default fundamental scale, and O-43 (E-25) records that no gravitational
# measurement reached below ~1 cm in 1998 — so nothing in the data distinguished a Planckian scale from a
# low one, and the split below rests on theory/naturalness priors, not evidence. A-54 (corrected, -> H-27)
# confirms the internal physics: even on wildly conservative overestimates the collapse parameter is ~1e-33,
# so this is the well-understood, physically default member. Anchored at 1.
w_standard = 1.0

# Combined low-scale (H-2 + H-4) mass as odds vs standard. Reference class: bold weak-scale naturalness
# solutions to a hierarchy problem (low-scale SUSY, technicolor, extra dimensions) proposed 1970s-2000s —
# a minority ever realized, none confirmed as of this corpus. These two are serious, calculable proposals
# by leading theorists (A-3 gives H-2 a concrete type-I string embedding; A-4 shows RS1 needs only an O(10)
# input), and A-62 (approved) shows the ADD premise was not excluded by any 1998 dataset — so the low-scale
# odds are small but not negligible. ~0.12 : 1 puts combined low-scale near 10%.
p_lowscale = 0.12   # odds that the fundamental gravity scale is ~TeV rather than Planckian

# Split of the low-scale mass between H-2 (ADD/TeV-string) and H-4 (RS1). Roughly even; a modest edge to ADD
# because within HC-1 it is the broader target — a family spanning field-theoretic ADD, type-I string, and
# n = 2-6 (A-3). RS1 is the more economical single-dimension mechanism and A-5 (approved) notes it is exempt
# from the ADD-type astrophysical/cosmological bounds, so it is not a priori disfavored; hence only a slight
# tilt. The discriminating torsion-balance truncation (E-28) is NOT baked in here — it is step-8's job.
share_add = 0.55
w_add = p_lowscale * share_add          # H-2
w_rs1 = p_lowscale * (1 - share_add)    # H-4

# H-33 residual — a short-distance completion that is neither Planckian-standard, nor ADD, nor RS1: e.g. some
# other low-scale mechanism, a different brane/warping setup, or a genuinely different QG scale nobody in this
# literature named. Its own argued weight (rule 4), not a leftover. The theory space of QG completions is not
# exhausted and O-43 leaves 33 untested orders of magnitude of physical room; but O-43 also excludes any
# completion that would have modified gravity above ~1 cm, and by ~2005 the proposed-completion space was
# well canvassed by a large community — so modest. ~0.14 : 1 vs standard, ~11% once normalised.
w_residual = 0.14

prior("HC-1", [w_add, w_rs1, w_standard, w_residual])
```
