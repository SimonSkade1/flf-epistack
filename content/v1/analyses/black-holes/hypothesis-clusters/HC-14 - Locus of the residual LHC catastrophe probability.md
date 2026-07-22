---
id: HC-14
type: hypothesis-cluster
question: "Is the all-things-considered LHC catastrophe probability dominated by the chance that the safety arguments themselves are flawed?"
hypotheses:
  - "[[H-11 - The actionable LHC catastrophe probability is dominated by the chance the safety argument itself is flawed]]"
  - "[[H-46 - The published LHC safety arguments are robust and their conditional bounds carry through]]"
exclusivity: "Either the argument-failure term dominates the actionable catastrophe probability or the stated conditional bounds carry through essentially undiluted; the members are a claim and its negation."
exhaustive_by_construction: true
independence: "The reliability of expert safety arguments is estimated from reference classes of scientific and technical error — a base rate about arguments, factorizing from which physics answers are true."
depends_on: []
relevance: "This cluster is the 'what does the conclusion hinge on' half of the main question: it decides whether the physics clusters' verdicts transfer to the actionable risk number."
---
![[H-11 - The actionable LHC catastrophe probability is dominated by the chance the safety argument itself is flawed]]
![[H-46 - The published LHC safety arguments are robust and their conditional bounds carry through]]

The meta-level cluster: whether the safety conclusion inherits the error rate of the arguments that produced it. Exhaustive by construction: proposition and logical complement. A failure of this analysis — mis-chosen reference classes for expert error, or ignoring anthropic selection in the historical record — is itself an instance of what the first member describes, and would favour it.

## Prior

```python
# HC-14 prior — locus of the residual LHC catastrophe probability. Members in HC-14.hypotheses order:
# [H-11 argument-failure term dominates the actionable P(X), H-46 published arguments robust so the
# conditional bounds carry through undiluted]. exhaustive_by_construction: true — a proposition and its
# logical complement, so there is NO residual member (rule 4 does not apply); the two weights are a crux
# probability and its complement, each argued on its own basis below.
#
# The crux (Ord-Hillerbrand-Sandberg framing, argument A-1 approved): by total probability
# P(X) = P(X|A)P(A) + P(X|¬A)P(¬A); with the physics clusters' stated conditional bound b ≈ 1e-9 (down to
# ~1e-12 for accretion), H-11 holds — the argument-failure term dominates — iff T ≡ P(¬A)·P(X|¬A) > b.
# So the whole cluster reduces to: does the layered, replicated safety case drive T below the stated bound?
#
# Evidence split (rule 5). Inbound E edges: E-24/O-12 (measured scientific error rates ~1e-3), E-26/O-13
# (Castle Bravo model failure), E-27/O-14 (RHIC anthropic-selection flaw). O-12 is a pure reference-class
# base rate and O-13 a general (non-accelerator) reference-class example of model failure in the most-checked
# hard-physics work — both are outside-view facts a prior on argument-reliability should already rest on, so
# E-24 and E-26 are marked used_for_prior: true and priced here. O-14 (RHIC) is the ONE same-class datum — a
# published accelerator-safety argument in precisely the cosmic-ray/Earth-survival genre at issue — which
# E-27 itself flags as "the most direct discriminator" with likelihood-relevant detail; it is left unmarked
# for step 8. No E edge here belongs to a correlation group. No-observation argument A-2 (approved, layering
# shrinks the grey area) is folded in below as reasoning, not as a term (rule 6).

# --- H-11 (argument-failure dominates): the outside-view-favoured member ---
# What would have to be true: that no realistic combination of effective P(¬A) and P(X|¬A) drives the
# argument-failure term below the ~1e-9 stated bound — i.e. the safety conclusion inherits a non-trivial
# argument error rate. Reference class: checked professional scientific/technical work (O-12), where serious
# flaws run ~1e-3 and even flagship, safety-critical hard-physics calculations suffer model failure that
# internal rigor cannot catch (O-13, Castle Bravo: a neglected reaction channel supplied the *bulk* of the
# yield). This is the position of the source paper (S-44) and A-1 (pure probability theory, approved). It is
# priced as the complement of the robustness case below — the mass where either layering fails to buy true
# independence OR P(X|¬A) is not negligible, which the base rates make the majority case. Highest-confidence
# member of the two.

# --- H-46 (arguments robust, bounds carry through): priced from its two enabling factors ---
# What would have to be true for H-46: the multi-layer structure genuinely buys independence AND, even given
# a residual flaw, catastrophe is very unlikely — jointly pushing T below the stated bound.
# Factor 1: probability the layering (A-2: Giddings-Mangano's ~3 sequential layers — rapid decay across
# frameworks; charge-retention -> cosmic-ray bound; accretion/white-dwarf limits) actually delivers ~2-3
# orders of effective-independence gain over the O-12 single-argument base rate of ~1e-3, i.e. effective
# P(¬A) ~ 1e-6. Would be right if the layers share no common modelling assumption; A-2's own caveat and the
# correlated-failure undercut make full independence far from certain.
p_layering = 0.40   # A-2 layering buys the needed orders of independence vs the O-12 ~1e-3 single-arg base rate
# Factor 2: probability that, even conditional on a residual flaw, P(X|¬A) is low enough (≲1e-4) that T stays
# under the stated bound — i.e. "flawed" mostly means "the bound is wrong", not "Earth is destroyed".
# Tempered downward by O-13: a model failure in checked hard physics can move the true outcome by an
# order-unity factor in the catastrophic direction, so P(X|¬A) is not safely negligible.
p_low_pXnotA = 0.36   # given a flaw survives all layers, the effect stays below the catastrophe threshold
# H-46 needs both to hold (roughly independent gates on driving T under b):
w_H46 = p_layering * p_low_pXnotA   # ~0.14

# H-11 is the complement of the robustness case (exhaustive_by_construction; not a residual, so no rule-4
# bar): the outside view (A-1 + O-12/O-13 base rates) carries the majority mass.
w_H11 = 1 - w_H46

prior("HC-14", [w_H11, w_H46])
```

The weights `[0.856, 0.144]` are the normalised prior. Driver variables: `p_layering` and `p_low_pXnotA` — both gate H-46, so the robustness member is thin unless one is convinced the layered case is genuinely independent *and* that a surviving flaw is near-harmless. Overriding either upward moves points directly onto H-46; the stated physics bound `b` and the O-12 base rate set the ~6-order gap the argument-failure term must not close, and are the outside-view anchors this prior rests on.
