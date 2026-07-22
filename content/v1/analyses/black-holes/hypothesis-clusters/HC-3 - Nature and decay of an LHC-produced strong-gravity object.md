---
id: HC-3
type: hypothesis-cluster
question: "If an LHC collision produces a strong-gravity object, what is it and how fast does it decay?"
hypotheses:
  - "[[H-7 - Micro black holes follow the microcanonical Casadio-Harms Hawking law and can be metastable]]"
  - "[[H-10 - Rotating micro black holes evaporate essentially as fast as nonrotating ones - lifetime differs by at most a factor 2.7]]"
  - "[[H-14 - LHC strong-gravity objects would be near-threshold quantum or stringy states, not semiclassical thermal black holes]]"
  - "[[H-24 - Micro black holes fail to Hawking-radiate yet still discharge, remaining stable and neutral]]"
  - "[[H-35 - An LHC strong-gravity object would behave in some way not listed here]]"
exclusivity: "Each member asserts a different physical character and decay law for the same object — prompt canonical Hawking evaporation, microcanonically suppressed metastability, non-thermal near-threshold stringy states, or a stable neutral non-radiating hole; at most one describes what such objects would actually do."
exhaustive_by_construction: false
independence: "Conditional on an object being produced, its decay physics is fixed by quantum gravity and factorizes from the astrophysical, strange-matter, and vacuum clusters' base rates."
depends_on:
  - "HC-1: whether such objects form at all, and in which geometry (the microcanonical member presupposes a warped dimension), is set by the short-distance structure of gravity"
  - "HC-2: if the dominant products of low-scale gravity are non-black-hole signatures, the members here apply only to a rarer subpopulation of events"
relevance: "Prompt decay is the first line of the LHC safety case; the metastable and stable members are exactly the scenarios the risk debate turns on."
---
![[H-7 - Micro black holes follow the microcanonical Casadio-Harms Hawking law and can be metastable]]
![[H-10 - Rotating micro black holes evaporate essentially as fast as nonrotating ones - lifetime differs by at most a factor 2.7]]
![[H-14 - LHC strong-gravity objects would be near-threshold quantum or stringy states, not semiclassical thermal black holes]]
![[H-24 - Micro black holes fail to Hawking-radiate yet still discharge, remaining stable and neutral]]
![[H-35 - An LHC strong-gravity object would behave in some way not listed here]]

One sub-question — what happens to a produced strong-gravity object — with four incompatible answers from the corpus: the canonical semiclassical picture (real thermal Hawking flux, essentially instant decay, rotation immaterial), the microcanonical correction under which holes can be metastable for macroscopic times, the near-threshold view on which the objects are low-entropy stringy states outside the thermal regime altogether, and the deliberately extreme no-Hawking-but-discharging stable neutral hole. These cannot co-hold as descriptions of the same objects, which is what makes the cluster a probability space; the residual covers decay behaviours no paper proposes. This cluster, not the production clusters, is where the Hawking-radiation hinge of the main question lives — carving it separately from HC-2 keeps "what is produced" and "what a produced object does" from double-counting the same evidence.

## Prior

```python
# HC-3 prior — nature and decay of an LHC-produced strong-gravity object. Members in HC-3.hypotheses order:
#   [H-7  microcanonical Casadio-Harms metastable (Plaga),
#    H-10 canonical thermal Hawking, prompt ~1e-27 s decay,
#    H-14 near-threshold low-entropy quantum/stringy state, not a thermal hole (Meade-Randall),
#    H-24 stable neutral, non-Hawking-radiating but Schwinger-discharging hole,
#    H-35 residual — some decay behaviour none of the four describes].
# Conditional cluster: every weight is P(character | an object was produced). depends_on (rule 3, noted not
# imported): HC-1 sets whether such objects form at all and in which geometry — H-7 presupposes an RS2 warped
# dimension, so its weight here is further conditional on HC-1 delivering one; HC-2 sets whether the dominant
# low-scale-gravity signature is even a black hole — if not, these members describe a rarer subpopulation.
# Evidence split: NO inbound E edge is marked used_for_prior. All six (E-33 astronomical survival, E-34 white
# dwarfs, E-35 neutron stars, E-36 Earth/Sun, E-37 torsion-balance null, E-38 threshold concentration) are
# case-specific and discriminating, left for step 8. The no-observation arguments from
# `no_observation_arguments.py <dir> --cluster HC-3` (A-12,A-15,A-27,A-28,A-34..A-41,A-44 — all step-6
# approved, none corrected/rejected) enter only as reasoning below (rule 6), never as a term.

# --- Outside view first (rule: take the reference class before the specifics) ---
# H-10 is the consensus / prompt-decay description; Hawking radiation has never been directly observed in a
# real gravitational hole. Price it by the base rate at which a *multiply-derived consensus* mechanism of
# accepted theory, unobserved in its target regime, later proves essentially right. Reference class: general
# relativity's gravitational waves (predicted 1916, directly confirmed 2015), the Higgs (1964 -> 2012),
# neutrino oscillation, antimatter — predictions carried by several independent derivations have a high hit
# rate. Hawking flux specifically has four independent derivations in this corpus (A-38 Bogoliubov mixing,
# A-34 past-horizon boundary conditions, A-39 renormalized stress tensor, A-40 thermodynamic/GSL consistency)
# plus BEC analog-Hawking confirmation of a thermal spectrum. The trans-Planckian (A-37) and 2D
# regularization-scheme (A-36) caveats are the reasons this is not ~0.99: both are known and neither has
# overturned the result. For this value to be right, the consensus derivations must not share a hidden common
# failure the caveats hint at.
p_ref = 0.90   # outside-view base rate for a multiply-derived, in-regime-unobserved consensus mechanism

# H-10 canonical thermal Hawking — the anchor (scale is free, rule 3). Held up by p_ref AND a second,
# near-independent route: the model-independent decay argument (A-28/A-44 approved) — a hole made from partons
# carries no conserved charge they lack, so it can decay back and its rate is tied to its production rate,
# regardless of Hawking details. Rotation does not buy longevity (A-15: lifetime changes by at most 2.0-2.7x).
# Two independent routes to prompt decay are why the mainstream mass is large. Most confident member.
w_H10 = p_ref

# H-14 near-threshold non-thermal stringy state — also a prompt-decay, astrophysically-safe description,
# differing from H-10 in physical character, not in danger. Strong no-observation support: A-11 (thermality
# criteria demand M several x the higher-dimensional Planck scale) and A-12 (collisional inelasticity leaves
# <=60% of parton energy behind the horizon, cutting cross sections by orders of magnitude) both argue genuine
# thermal holes are rarely if ever produced. But the *observation* pinning production to threshold (O-20, edge
# E-38) is reserved for step 8, so the prior lift from that channel is kept modest to avoid pre-counting it,
# and the canonical description still covers whatever genuine-thermal parameter space exists. Slightly below
# the anchor a priori; second most confident.
f_H14 = 0.85          # H-14 : H-10 odds — comparable mainstream regime, A-11/A-12 support, E-38 held for step 8
w_H14 = f_H14 * w_H10

# H-7 microcanonical Casadio-Harms metastability (Plaga scenario 3): lifetimes ms-to-years via a microcanonical
# Hawking law in an RS2 warped geometry. Peer-reviewed but a minority correction; the mainstream
# (Giddings-Mangano, LSAG) holds the canonical + model-independent decay applies and rejects macroscopic
# metastability. For it to be right the microcanonical treatment must not merely refine but change the lifetime
# by many orders of magnitude AND the required RS2 geometry must obtain (the HC-1 conditional). The
# torsion-balance null (E-37) and threshold data strain it further but are step 8. Low odds.
o_H7 = 0.06           # H-7 : H-10 odds — peer-reviewed minority law needing a specific geometry
w_H7 = o_H7 * w_H10

# H-24 stable, neutral, non-radiating but Schwinger-discharging hole — the deliberately extreme scenario
# Giddings-Mangano built to bound. A-44 (approved): every framework in which Schwinger discharge operates also
# produces Hawking decay, and no conserved charge blocks decay, so "discharges but never radiates" is nearly
# self-contradictory. It must defeat BOTH routes supporting prompt decay at once, so its prior sits below H-7;
# nonzero only because no theorem strictly forbids it.
o_H24 = 0.02          # H-24 : H-10 odds — near self-contradictory per A-44
w_H24 = o_H24 * w_H10

# H-35 residual (rule 4: its own argued weight, never 1 - sum of the others). Concretely, an unmodelled fate:
# decay to a stable Planck-mass remnant, evaporation stalling on an intermediate timescale, or dynamics from a
# quantum-gravity completion no one has written down. Priced by the outside-view rate at which, in a question
# this thoroughly mapped (canonical, microcanonical, stringy-threshold, and a deliberate extreme all
# enumerated) and backstopped by the model-independent decay argument, the truth still falls outside the menu —
# uncommon but real. On the same pseudo-probability scale as the others; independent of every w_* above.
w_H35 = 0.045         # ~2-3% of the normalised mass — an unmodelled decay law, argued on its own

prior("HC-3", [w_H7, w_H10, w_H14, w_H24, w_H35])
```

Normalises to ≈ `[0.030, 0.505, 0.429, 0.010, 0.025]` for `[H-7, H-10, H-14, H-24, H-35]` — the two mainstream prompt-decay descriptions (H-10+H-14) hold ≈0.93, leaving ≈0.07 across metastable/stable/other for the compact-star survival family (E-33..E-36) to act on at step 8. `p_ref` and `f_H14` are the drivers: dropping `f_H14` to 0.45 moves ≈14 points from H-14 onto H-10 without touching the safe total; lowering `p_ref` is the whole cost of doubting the consensus Hawking picture.
