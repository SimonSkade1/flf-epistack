---
id: A-11
type: argument
statement: "Every reasonable criterion for a produced object to be a genuinely thermal (semiclassical) black hole - Compton wavelength inside the Schwarzschild radius, small temperature change per emission, no single degree of freedom carrying a large energy fraction, lifetime exceeding both 1/M and the light-crossing time rS - requires the black-hole mass to sit several times (xmin ~ 3-16, and strictly ≫1) above the higher-dimensional Planck scale; combined with steeply falling parton luminosities, values of xmin that satisfy the criteria yield production rates too low for the LHC, so near-threshold objects dominate and are not trustworthy thermal black holes."
source: "[[S-50 - Meade, Randall 2008 — Black Holes and Quantum Gravity at the LHC]]"
locator: "§2.1-2.2, eqs. (2.4)-(2.19), Figure 2"
affects_observations: ["[[O-20 - LHC parton luminosities fall steeply with invariant mass, concentrating any threshold process just above threshold]]"]
affects_hypotheses: ["[[H-14 - LHC strong-gravity objects would be near-threshold quantum or stringy states, not semiclassical thermal black holes]]"]
status: approved
reason_if_not_false: checked
---
Reasoning (each step is a calculation in the paper; xmin ≡ MBH/M measures how far above the relevant Planck scale M the object sits):

1. Convention ambiguity: the Planck scale M is convention dependent (Dimopoulos-Landsberg vs PDG vs RS normalizations differ by factors of ~1.6-2.9 in the implied threshold), so E > M is necessary but nowhere near sufficient, and quoted "black holes at ~1 TeV" claims are convention-laden.
2. Compton-wavelength criterion: requiring a colliding quantum of energy E/2 (wavelength 4π/E) to fit inside the Schwarzschild radius of a black hole of mass E gives xmin > 4.1 for ADD n=6 and xmin > 16 for RS1 (weaker variant rS > 1/E still gives 0.44 and ~3 respectively).
3. Thermodynamic criteria: |∂T/∂M| ≪ 1 (equivalently large entropy, satisfied already near xmin ~ 1); every degree of freedom carrying energy ≪ MBH, i.e. (n+3)T < M, satisfied only for xmin ≳ 2, and a single bulk mode carries essentially all the energy at MBH ~ 2-3 M; lifetime τ > 1/M needs xmin ~ 1.3 (ADD) / 1.6 (RS); τ > rS (re-equilibration during brane decay) needs xmin ≳ 3 (ADD).
4. Entropy/multiplicity: at the maximum experimentally reachable xmin (~6 for ADD n=6, ~10 for RS) the corresponding thermal state would consist of only ~3-6 quanta sharing the energy - inadequate for anything "thermal"; ⟨N⟩ > 2 already requires MBH > 1.5 MD (ADD) or > 4 M̃ (RS).
5. All criteria should really hold with margin (≫1, not ~1); but by the falling parton luminosities (the attached observation), production at such xmin is rate-suppressed below observability, while what is actually produced sits at the lowest allowed mass. Hence the highly studied thermal multiparticle signatures are unrealistic, and earlier analyses using low or no xmin overstate the semiclassical character of LHC objects.

## Validity verdict (step 6)

Reconstruction: premises = the per-criterion xmin calculations and the attached observation (steeply falling parton luminosities); conclusion = what the LHC would actually produce sits near threshold and fails the thermality criteria. Load-bearing step: each criterion is a necessary condition, so trustworthy thermality needs the max of the xmin values (~3-16, with margin); steep luminosity fall means production is dominated by the lowest allowed mass while high-xmin production is rate-suppressed. Traced this combination - it is a straightforward conjunction-plus-monotonicity argument. Undercutting probe: none survives conditional on the premises; whether the individual xmin numbers are right is premise-truth for steps 7-8.
