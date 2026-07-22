---
id: HC-2
type: hypothesis-cluster
question: "If the quantum-gravity scale lies within collider reach, what would LHC collisions dominantly produce and show first?"
hypotheses:
  - "[[H-3 - A TeV string scale would make LHC collisions produce strong-gravity phenomena including black holes]]"
  - "[[H-5 - RS1 predicts TeV-mass spin-2 graviton resonances with weak-scale couplings at colliders]]"
  - "[[H-15 - The first observable low-scale quantum-gravity signature at the LHC would be enhanced transverse two-body final states]]"
  - "[[H-34 - Low-scale quantum gravity would first show at the LHC as something not listed here]]"
exclusivity: "Each member names a different earliest/dominant collider manifestation of low-scale quantum gravity; at most one is what would actually appear first."
exhaustive_by_construction: false
independence: "Conditional on the gravity-scale answer, which signature appears first is set by production dynamics and does not shift the base rates of the non-collider clusters."
depends_on:
  - "HC-1: which low-scale mechanism (if any) is realized shifts which signature is expected — all members are conditionals on a low fundamental scale"
relevance: "Fixes whether the LHC would announce low-scale gravity loudly (and as what) before any dangerous object could be at issue, and what null results at the LHC say about the scenarios."
---
![[H-3 - A TeV string scale would make LHC collisions produce strong-gravity phenomena including black holes]]
![[H-5 - RS1 predicts TeV-mass spin-2 graviton resonances with weak-scale couplings at colliders]]
![[H-15 - The first observable low-scale quantum-gravity signature at the LHC would be enhanced transverse two-body final states]]
![[H-34 - Low-scale quantum gravity would first show at the LHC as something not listed here]]

The members compete over what low-scale quantum gravity would dominantly look like at the LHC: copious strong-gravity phenomena including black holes with Regge excitations, a few reconstructable spin-two graviton resonances, or an enhancement of transverse two-body final states arriving before any black-hole signature. These are exclusive as claims about the earliest/dominant manifestation — the corpus itself opposes the two-body claim to the advertised multiparticle black-hole signature. Not exhaustive by construction (other first signatures are conceivable), hence the residual. The dependence on the mechanism cluster is recorded rather than folded in: a combination cluster would multiply members without adding discriminable structure.

## Prior

```python
# HC-2 prior — dominant/earliest collider manifestation of low-scale quantum gravity, conditional on the
# QG scale lying within collider reach. Members in HC-2.hypotheses order:
# [H-3 strong-gravity/black holes + Regge, H-5 RS1 spin-2 KK graviton resonances,
#  H-15 enhanced transverse two-body final states first, H-34 residual].
# Inputs: the outside view on "which signature shows first" in BSM collider phenomenology, plus the general
# (textbook) requirement that a semiclassical thermal black hole needs a mass several times the fundamental
# scale. NOTE (rule 3): all members are conditionals on HC-1's low fundamental scale (depends_on HC-1); which
# mechanism is realized is HC-1's business — the mechanism-share factor below is an approximation noted here,
# not an imported HC-1 probability. The one inbound evidence-link E-1 (O-20: LHC parton luminosities fall
# steeply, concentrating production just above threshold) is case-specific and DISCRIMINATING — it separates
# H-15 from H-3 for this collider — so it is left UNMARKED for step 8, not priced here. No no-observation
# arguments exist for this cluster. Numbers are theoretical priors, not looked-up base rates.

# H-15 two-body enhancement first — the anchor (unit weight). Outside view: across BSM "what shows up first"
# questions, the lower-threshold soft effect (contact-operator / compositeness-type enhancement) generically
# precedes the dramatic high-multiplicity object, because a semiclassical thermal black hole needs a mass
# several times the fundamental scale while the two-body threshold sits just above the scale itself. This is
# the most model-agnostic claim of the three, so it takes the unit weight the others are priced against.
w_twobody = 1.0

# H-3 black holes + Regge as the dominant first signature — the historically advertised "black-hole factory"
# picture (Dimopoulos-Landsberg 2001). Theoretically serious, but disfavored as the EARLIEST manifestation by
# the threshold-mass requirement above (general theory, distinct from this collider's luminosity spectrum
# O-20 / E-1, which is left for step 8): thermal multiparticle production needs events well above the scale,
# a minority of near-threshold events. Priced as odds against the two-body anchor.
bh_vs_twobody = 0.45   # ~0.45:1 vs H-15 — live but sub-threshold non-thermal states generically come first
w_bh = bh_vs_twobody * w_twobody

# H-5 clean spin-2 KK graviton resonance first — the narrowest member: a conjunction of (a) the realized
# low-scale mechanism being warped/RS1-type rather than large-extra-dimensions/string, and (b) a KK graviton
# light and narrow enough to be reconstructed before any sub-resonance two-body/contact excess appears.
p_rs1_family = 0.40             # approx share of low-scale-gravity realizations that are RS1/warped; true split is HC-1's (rule 3), noted not imported
p_graviton_resolves_first = 0.55  # within RS1, credence a resolvable spin-2 bump is the first thing seen rather than a two-body enhancement
w_graviton = p_rs1_family * p_graviton_resolves_first * w_twobody

# H-34 residual — argued on its own (rule 4), not a leftover. What an unmodelled first signature would
# concretely look like: dominant monojet + large-missing-energy from real KK-graviton emission (a standard
# extra-dimension collider channel not named by any member), or narrow string Regge resonances of SM
# particles showing as the dominant signal without black holes, or a qualitatively different strong-gravity
# state. Non-trivial because the ORDERING of low-scale-QG signatures is not tightly pinned by theory; broad
# but not dominant since the three members cover the main advertised proposals. Odds on the same unit scale.
resid_odds = 0.32   # ~0.32:1 vs H-15 — a real gap in signature-ordering space, but the listed members catch the headline channels
w_residual = resid_odds

prior("HC-2", [w_bh, w_graviton, w_twobody, w_residual])
```
