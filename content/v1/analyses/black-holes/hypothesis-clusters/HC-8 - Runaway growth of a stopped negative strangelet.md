---
id: HC-8
type: hypothesis-cluster
question: "Would a stopped negatively charged (meta)stable strangelet grow without limit by absorbing nuclei?"
hypotheses:
  - "[[H-29 - A metastable negatively charged strangelet stopped in matter would grow exponentially by alternating nuclear absorption and electron capture]]"
  - "[[H-40 - A stopped negative strangelet would not grow without limit]]"
exclusivity: "Either the absorption-and-electron-capture cycle runs away without an absolute barrier or some barrier halts it; the members are a claim and its negation."
exhaustive_by_construction: true
independence: "Conditional on the stability answer, whether growth self-limits is nuclear-surface and Coulomb physics that does not shift the other clusters' base rates."
depends_on:
  - "HC-7: runaway growth presupposes (meta)stable bulk strange matter — the members are conditionals on production, stopping, and negative bulk charge"
relevance: "This is the step that turns a hypothetical strangelet into an Earth-conversion mechanism; without runaway growth the strangelet branch of the main question is closed."
---
![[H-29 - A metastable negatively charged strangelet stopped in matter would grow exponentially by alternating nuclear absorption and electron capture]]
![[H-40 - A stopped negative strangelet would not grow without limit]]

The runaway mechanism against its self-limiting complement, both conditional on the strangelet existing, stopping, and being negatively charged in bulk. Exhaustive by construction: proposition and logical complement. A failure of the analysis — e.g. the growth argument and its critiques sharing a wrong picture of the strangelet surface — would favour the second member, since the runaway claim is the one carrying the extraordinary conclusion.

## Prior

```python
# HC-8 prior — runaway growth of a stopped negative strangelet. Members in HC-8.hypotheses order:
# [H-29 runs away without limit, H-40 some barrier halts it]. exhaustive_by_construction: true, so there is
# no residual member (rule 4 does not apply): the two are a proposition and its exact logical negation.
#
# Conditioning (depends_on HC-7, prose not imported): every weight here is CONDITIONAL on the antecedent the
# cluster fixes — a (meta)stable strangelet was produced, stopped (v < 0.1c, lifetime > ~1e-7 s), and is
# NEGATIVELY charged in bulk. Whether that antecedent holds is HC-7's business (bulk stability) plus the
# production/charge conditions priced elsewhere; A-57's headline claim that stable strange matter is almost
# surely POSITIVE bears on that antecedent, so it is NOT re-used here to avoid double-counting the conditioning.
# Only the growth-vs-no-growth content of A-56/A-57 (approved, no-observation args reaching H-29 via
# affects_hypotheses; rule 6) enters as reasoning below.
#
# Evidence split (rule 5): HC-8's three inbound E edges — E-30 (O-23 lunar persistence), E-31 (O-39 cosmic-ray
# collision counts), E-32 (O-22 stars/Sun/WD/NS persist) — are all DISCRIMINATING survival bounds (each edge's
# "why this is evidence" points toward H-40 with strength scaling with the per-collision production-and-stopping
# probability). None is an outside-view base rate the prior should rest on, so NONE is marked used_for_prior;
# all three are left for step 8. This prior therefore marks no edges.

# --- H-29 (runaway): the danger hypothesis. What would have to be true: given the worst-case antecedent, the
# absorb-nucleus / electron-capture cycle meets NO barrier across ~50 orders of magnitude of baryon-number
# growth. BJSW's own text supports only the weak "we know of no absolute barrier" — an absence-of-knowledge
# claim, not a positive case — while listing three concrete candidate terminators. Priced well below H-40. ---

# Outside view first (rule 2). Reference class: proposed self-amplifying / unbounded-runaway catastrophe
# mechanisms in physics whose proposers could not name a barrier. Degenerate/bound many-body systems generically
# grow a surface, Coulomb, or charge barrier as they scale, so "truly no barrier anywhere" is the rare outcome.
p_no_barrier_outside = 0.10   # base rate that a proposed unbounded runaway has no self-limiting barrier at all

# Mechanistic view: the three BJSW terminators (H-29 note a/b/c; A-56 wrinkle 3a/3b; A-57), each a chance to
# halt growth. Probabilities below are that the terminator does NOT fire (growth survives it). A-56 flags these
# "cannot be modeled accurately enough to carry the safety case", so each is plausible-but-uncertain, not ~1.
p_no_chargefreeze = 0.45  # (a) A-57: Fermi-gas kinematics drives Z/A positive as A climbs; a stable positive
                          #     species then freezes growth via electron shielding. Likely to fire -> 0.45 survives.
p_no_gap = 0.60           # (b) A-56 3b: a stability gap (like the A=8 gap halting alpha-alpha fusion) can isolate
                          #     the metastable strangelet so single-nucleon climb stalls; plausible, not assured.
p_no_fragment = 0.70      # (c) capture-energy release may shatter the strangelet into small unstable pieces;
                          #     the least compelling of the three, so most mass survives it.
p_runaway_mech = p_no_chargefreeze * p_no_gap * p_no_fragment  # all three terminators fail -> no barrier

# Two frameworks -> inline mixture (rule 7). c_mech is the credence the three named terminators exhaust the
# barrier space; the outside view warns there are likely MORE barriers than the three modelled, pulling lower.
c_mech = 0.60   # credence the explicit-terminator decomposition captures the full set of halting mechanisms
p_runaway = c_mech * p_runaway_mech + (1 - c_mech) * p_no_barrier_outside

# --- H-40 (no runaway): some barrier halts growth before macroscopic conversion. The outside-view-favoured and
# BJSW-flagged outcome; carries the bulk of the conditional mass. Anchored at unit weight; H-29 is priced as
# odds against it, so a skeptic overrides p_runaway (or any terminator factor) and both weights move together. ---
w_no_runaway = 1.0
w_runaway = p_runaway / (1 - p_runaway)   # odds of runaway vs. not; arithmetic identity over H-29's own p

prior("HC-8", [w_runaway, w_no_runaway])
```

