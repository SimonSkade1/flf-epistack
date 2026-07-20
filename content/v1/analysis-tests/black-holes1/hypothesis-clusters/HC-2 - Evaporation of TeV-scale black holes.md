---
type: hypothesis-cluster
id: HC-2
hypotheses:
  - "[[H-4 - Black holes radiate thermally and evaporate, so a TeV-mass black hole would decay near-instantly]]"
  - "[[H-7 - Hawking evaporation fails and TeV-mass black holes are long-lived]]"
exclusivity: "Near-instant decay and stability/longevity are contradictory fates for the same TeV-mass object."
exhaustive_by_construction: true
independence: "Whether semiclassical evaporation survives into the quantum-gravity regime is a separate physical question from what the fundamental gravity scale is or how fast a stable hole would accrete."
depends_on: []
question: "Does a micro black hole, if formed at the LHC, evaporate near-instantly via Hawking radiation?"
relevance: "First line of the safety case: if H-4 holds at the TeV scale, the danger cluster never engages."
---
![[H-4 - Black holes radiate thermally and evaporate, so a TeV-mass black hole would decay near-instantly]]
![[H-7 - Hawking evaporation fails and TeV-mass black holes are long-lived]]

Exhaustive by construction: H-7 is the logical complement of H-4 (a TeV hole either decays near-instantly or it does not). Failure mode of the analysis: the semiclassical derivation extrapolated to the near-Planck/TeV regime, where the approximation is weakest, could break down — that failure would favour H-7.

## Prior

```python
# HC-2 prior — does a TeV-mass black hole evaporate near-instantly? Members in HC-2.hypotheses order:
# [H-4 evaporates near-instantly, H-7 evaporation fails / long-lived]. Exhaustive by construction, no residual.
# Evidence partition: all three inbound edges (E-7 WD survival, E-8 NS survival, E-9 Earth/Sun survival)
# are case-specific discriminating astrophysical observations — left UNMARKED for step 8; none used here.
# The prior rests purely on the theoretical outside view, informed by no-observation argument A-5
# (approved: QFT on the collapse background gives T ∝ 1/M, lifetime ∝ M³, so micro holes decay ~instantly).

# H-4 — the anchor. Holds if the semiclassical thermal-flux prediction (A-5) is qualitatively right at the
# TeV scale. Reference class: predictions of QFT-in-curved-spacetime that follow from several independent
# derivations (collapse calculation, Euclidean path integral, tunneling picture, string microstate counting)
# and have analogue-system confirmations. Does not cover: direct observation of astrophysical Hawking flux
# (none exists). Confidence relative to H-7: high — the anchor of the cluster.
w_evaporates = 1.0

# H-7 — evaporation fails. Two routes, combined as a union (mixture written inline, rule 7):
# (a) the framework itself is wrong even in its stated domain of validity. Very low: the reference class is
#     "robust multi-derivation predictions of well-tested effective field theory frameworks" — such
#     predictions almost never turn out simply wrong; A-5's derivation is the consensus calculation.
p_framework_wrong = 0.01
# (b) the framework is right where valid but the extrapolation to the near-Planck/TeV regime (exactly where
#     a TeV hole lives, per the cluster's own noted failure mode) breaks in a way that yields stability.
#     Base rate: semiclassical results do get quantum-gravity corrections, but in most candidate QG
#     completions (string theory, loop approaches) decay survives; stable-remnant scenarios are a real but
#     minority theoretical position, so this gets noticeably more mass than (a) but stays well under 50%.
p_extrapolation_stabilizes = 0.10
# Union of the two failure routes (arithmetic identity, no new estimate):
p_fails = p_framework_wrong + (1 - p_framework_wrong) * p_extrapolation_stabilizes
# Convert to odds against the H-4 anchor (identity):
w_fails = p_fails / (1 - p_fails)

prior("HC-2", [w_evaporates, w_fails])
```

