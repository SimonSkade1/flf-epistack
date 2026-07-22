---
id: A-12
type: argument
statement: "Classical trapped-surface calculations of ultrarelativistic collisions (D'eath-Payne; Eardley-Giddings; Yoshino et al.) show at most ~60% of the parton center-of-mass energy ends up inside the apparent horizon at zero impact parameter, and less at larger impact parameter (down to ~0 for 10D, ~0.2 for 5D at maximal b); folding this inelasticity into the impact-parameter-weighted cross section forces the PDFs to be probed at higher x and reduces the total black-hole production cross section by up to several orders of magnitude relative to the naive geometric estimate σ ≈ πrS²."
source: "[[S-50 - Meade, Randall 2008 — Black Holes and Quantum Gravity at the LHC]]"
locator: "§2.3, eqs. (2.20)-(2.21), Figures 3-4"
affects_hypotheses: ["[[H-14 - LHC strong-gravity objects would be near-threshold quantum or stringy states, not semiclassical thermal black holes]]"]
status: approved
reason_if_not_false: checked
---
Reasoning:

1. Define inelasticity y ≡ MBH/√ŝ. The energy not trapped behind the apparent horizon is radiated gravitationally in the collision; classical results (from Penrose / D'eath-Payne in 4D, extended to higher D and nonzero impact parameter by Eardley-Giddings and refined by Yoshino et al.) give y ≲ 0.6 at b=0 for both the 10D (ADD) and 5D (RS) cases, falling with b - to y ≈ 0 (ADD) and y ≈ 0.2 (RS) at the largest horizon-forming impact parameter.
2. To make a black hole of mass MBH one therefore needs parton energies larger by 1/y; because parton luminosities fall steeply, the impact-parameter-averaged cross section (eq. 2.21, weighting by 2z dz with z = b/bmax and threshold (xmin MD)²/(y(z)² s)) drops by orders of magnitude versus the geometric estimate (Figure 4), more strongly for ADD than RS.
3. These classical y values are lower bounds computed near the Planck scale where quantum-gravity corrections are unknown - one more way the naive production picture is unreliable near threshold.
4. Together with the thermality thresholds, this pushes genuinely semiclassical production even further out of the LHC's effective reach.

## Validity verdict (step 6)

Reconstruction: premises = classical trapped-surface inelasticity values (y <~ 0.6 at b=0, falling with b) and steeply falling parton luminosities; conclusion = impact-parameter-weighted cross section falls orders of magnitude below the geometric estimate. Traced the load-bearing step: making mass MBH requires parton CM energy MBH/y, and a steeply falling luminosity evaluated at higher invariant mass suppresses the rate by orders of magnitude; averaging over b with y(b) decreasing only strengthens this. Valid conditional on the y values; their classical near-Planck provenance is flagged in the body and priced downstream.
