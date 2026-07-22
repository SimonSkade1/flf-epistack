---
id: HC-5
type: hypothesis-cluster
question: "At what rate does a small trapped mass accrete from a surrounding medium?"
hypotheses:
  - "[[H-16 - Physical accretion realizes the maximal transonic rate, with an interpolation formula covering the moving-star case]]"
  - "[[H-38 - Steady accretion does not realize the maximal transonic rate]]"
exclusivity: "Either steady accretion realizes the maximal transonic rate (with the interpolation formula giving the right order of magnitude) or it does not; the members are a claim and its negation."
exhaustive_by_construction: true
independence: "The accretion law is classical fluid dynamics, independent of which quantum-gravity, astrophysical, or strange-matter answers hold."
depends_on: []
relevance: "Every quantitative account of what a trapped black hole would do to the Earth — catastrophic or innocuous — runs through this accretion law."
---
![[H-16 - Physical accretion realizes the maximal transonic rate, with an interpolation formula covering the moving-star case]]
![[H-38 - Steady accretion does not realize the maximal transonic rate]]

A background-physics cluster: the transonic (Bondi) accretion law is an explicit ingredient of both the catastrophic and the innocuous trapped-hole analyses, so its correctness is a hinge worth scoring separately. Exhaustive by construction: the members are a proposition and its logical complement, so no residual is needed. A failure of the analysis here would look like the corpus's accretion treatments all inheriting the same unexamined idealization — spherical symmetry, no feedback, no magnetic or angular-momentum effects — and would favour the complement member (the second listed).

## Prior

```python
# HC-5 prior — accretion law for a small trapped mass in an ambient medium. Members in HC-5.hypotheses order:
# [H-16 physical accretion realizes the maximal transonic (Bondi) rate + OOM interpolation formula,
#  H-38 constructed complement: the rate differs materially, so the interpolation misestimates growth].
# exhaustive_by_construction (rule 4 N/A — no residual): the two members are a proposition and its logical
# negation. This cluster has ZERO inbound evidence-links by design; its entire support is its two
# no-observation arguments A-17 and A-18 (from `no_observation_arguments.py <dir> --cluster HC-5`), both
# step-6 approved and both reaching H-16 via affects_hypotheses (rule 6). No E edges exist, so nothing is
# marked used_for_prior; HC-5.depends_on == [] (nothing to note). A-47/A-48 attach to H-22 in another
# cluster, not here, so they play no role. The prior is therefore the whole model for this cluster.

# --- Outside view first (process 2). Base rate that a clean closed-form idealized transport law, applied
# within its stated domain, captures the true rate to order of magnitude. Across physics idealizations used
# inside the regime they were derived for, this holds more often than not.
p_idealization_ok = 0.80   # OOM-correctness base rate for an in-domain idealized transport law

# A-18 (approved but explicitly "valid-but-weak"): the SELECTION λ = λc is a heuristic — lowest-energy steady
# state — not a theorem; Bondi himself calls it "very likely" / "not quite assured". A-17 (approved,
# "checked; no defeater conditional on the steady spherical polytropic premises"): the SCALING
# Ṁ ∝ M²ρ∞c∞⁻³ and the existence bound λ ≤ λc are FORCED by the equations — a closed-form theorem. So the
# functional-form failure channel is closed; what remains open is only where in (0, λc] the realized λ sits.
lift_A17_theorem = 1.10    # scaling+bound are a theorem (A-17), one failure mode removed

# Setting-specific adjustment (rule 2, visible factor): a *trapped* small mass sits nearly at rest in a
# dense, near-isotropic medium (Earth / stellar interior) — low angular momentum, with disk formation and
# large-scale magnetic fields far less relevant than in the galactic-gas accretion where Bondi's caveats
# usually bite. The spherical-symmetry idealization is unusually apt in exactly this regime.
adj_trapped_setting = 1.05

# Discount for what A-18 leaves open plus the moving-star piece: even if selection fails, the realized λ
# stays within (0, λc] — an O(1) factor, seldom a full order of magnitude — so A-18's weakness dents but does
# not break the OOM claim; and the moving-star interpolation is Bondi's own acknowledged OOM *conjecture*.
disc_A18_selection = 0.92  # heuristic λ-selection + OOM interpolation conjecture; sub-OOM discount

c_H16 = p_idealization_ok * lift_A17_theorem * adj_trapped_setting * disc_A18_selection  # ≈ 0.85

# H-16 — the standard Bondi result the corpus's accretion estimates run on. Would hold if the transonic law
# gives the growth rate to order of magnitude for a small trapped mass; anchored at its own credence, priced
# as odds vs its negation (rule 3). Most confident member — a theorem-backed scaling with an apt geometry.
w_H16 = c_H16

# H-38 constructed complement (step-4b mint): the true rate differs *materially* — angular momentum,
# radiation/heating feedback, magnetic fields or microphysics suppress or alter it enough that the
# interpolation misestimates growth by more than an order of magnitude. This is the genuine logical negation
# of H-16 in an exhaustive cluster (not a residual catch-all, so rule 4 does not apply), so its weight is
# 1 - c_H16, the aggregate of every failure channel the two approved arguments could not close. Kept
# non-trivial deliberately: the cluster note's own failure mode is the corpus inheriting one unexamined
# idealization, which lands entirely here. Less likely than H-16, but the systematic-error concern is real.
w_H38 = 1 - c_H16          # ≈ 0.15, the OOM-failure disjunction

prior("HC-5", [w_H16, w_H38])
```
