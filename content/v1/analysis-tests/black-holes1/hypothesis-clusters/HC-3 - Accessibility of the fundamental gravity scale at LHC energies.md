---
type: hypothesis-cluster
id: HC-3
hypotheses:
  - "[[H-3 - Two or more large compact extra dimensions lower the fundamental gravity scale to about a TeV]]"
  - "[[H-8 - The fundamental gravity scale is far above LHC energies so no black holes form]]"
  - "[[H-9 - TeV-scale gravity arises via some mechanism not listed here]]"
exclusivity: "The fundamental gravity scale sits either at ~TeV via large extra dimensions (H-3), far above LHC reach (H-8), or at ~TeV via some other mechanism (residual); these describe incompatible geometries."
exhaustive_by_construction: false
independence: "The value and origin of the fundamental gravity scale is fixed by spacetime geometry, independent of whether Hawking evaporation operates or how a stable hole would accrete."
depends_on: []
question: "Is the fundamental scale of gravity low enough (~TeV) that LHC collisions could produce black holes at all?"
relevance: "Enabling premise: on the H-8 branch no LHC black hole forms and the main question's risk is zero trivially."
---
![[H-3 - Two or more large compact extra dimensions lower the fundamental gravity scale to about a TeV]]
![[H-8 - The fundamental gravity scale is far above LHC energies so no black holes form]]
![[H-9 - TeV-scale gravity arises via some mechanism not listed here]]

H-8 is the constructed conventional-hierarchy complement; the residual covers non-ADD low-scale-gravity mechanisms (e.g. warped geometry) that also enable production.

## Prior

```python
# HC-3 prior — is the fundamental gravity scale ~TeV, i.e. reachable at the LHC? Members in
# HC-3.hypotheses order: [H-3 large extra dimensions, H-8 conventional high scale, H-9 residual
# other TeV-gravity mechanism]. Inputs: the one inbound edge E-5 (O-8, the 16-order electroweak/
# Planck hierarchy — a general background fact, pulled into the prior and marked used_for_prior:
# true, so step 8 skips it) and no-observation argument A-4 (approved), read as reasoning per rule 6.
# Case-specific LHC search results are not on this cluster's edges and are left to step 8.

# H-3 large extra dimensions (and the shared low-scale factors). What would have to be true:
# the hierarchy (O-8 via E-5) reflects a genuine ~TeV-scale resolution rather than fine-tuning
# or an anthropic/no-resolution outcome, AND that resolution is one of the minority that lowers
# the fundamental *gravity* scale (most candidates — SUSY, composite Higgs — stabilize the weak
# scale without touching gravity), AND within low-gravity-scale mechanisms it is specifically
# n>=2 large flat dimensions. A-4 (approved) says a ~TeV scale is *consistent* with observed
# 4D gravity for n>=2 — it removes a would-be knockdown, letting share_gravity_scale be nonzero,
# but its own caveat (the hierarchy is relocated to radius stabilization, not solved) is why
# p_tev_resolution and share_gravity_scale stay modest rather than favored. Confidence: low in
# absolute level, but the ordering H-8 >> H-3 ~ H-9 is robust.

# Credence the hierarchy has any natural TeV-scale resolution at all (vs fine-tuning /
# anthropic selection / nothing at accessible scales) — this is where E-5's naturalness pull enters.
p_tev_resolution = 0.4
# Share of candidate hierarchy resolutions that work by lowering the fundamental gravity scale,
# judged across the field's proposal space (SUSY, composite, extra-dimensional, anthropic):
# extra-dimensional gravity is a minority family. A-4's relocation caveat also caps this.
share_gravity_scale = 0.15
# Within low-gravity-scale mechanisms, the share that is specifically ADD-type (n>=2 large flat
# dimensions) rather than warped or other geometry — ADD is the canonical member but not the only one.
share_add = 0.5
w_h3 = p_tev_resolution * share_gravity_scale * share_add

# H-8 conventional high scale — true iff no gravity-scale-lowering resolution holds; arithmetic
# complement of the shared low-scale mass (an identity, not an estimate — rule 1).
w_h8 = 1 - p_tev_resolution * share_gravity_scale

# H-9 residual — a non-ADD TeV-gravity mechanism (e.g. Randall-Sundrum warping) is the true one.
# Own argued weight: same two low-scale factors, times the share of low-gravity-scale mechanism
# space outside ADD — warped geometry alone is roughly as well-developed as ADD, so half.
share_other_mechanism = 0.5
w_h9 = p_tev_resolution * share_gravity_scale * share_other_mechanism

prior("HC-3", [w_h3, w_h8, w_h9])
```

Normalised ≈ [0.03, 0.94, 0.03]. Driver: `p_tev_resolution` — a skeptic of naturalness sets it near 0 and H-8 goes to ~1; a strong naturalness advocate at 0.8 still leaves H-8 ≈ 0.88.
