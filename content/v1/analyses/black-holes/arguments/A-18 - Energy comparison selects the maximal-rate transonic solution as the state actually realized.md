---
id: A-18
type: argument
statement: "Comparing the gas energy shell-by-shell across steady solutions shows the density (hence energy) in every spherical shell decreases as λ increases, and at λ = λc the transonic Type II state has lower density than Type I inside the sonic radius - so the maximal-rate transonic solution is the lowest-energy steady state and is the one expected to be physically realized."
source: "[[S-51 - Bondi 1952 — On spherically symmetrical accretion]]"
locator: "§7, penultimate and final ¶¶"
affects_hypotheses: ["[[H-16 - Physical accretion realizes the maximal transonic rate, with an interpolation formula covering the moving-star case]]"]
status: approved
reason_if_not_false: checked
---
Reasoning:

1. The steady-state equations leave λ ∈ (0, λc] free, so a selection principle outside them is needed (boundary conditions at the stellar surface impose nothing - the star swallows whatever falls in; a time-dependent entry calculation à la Bondi-Hoyle 1944 is intractable here).
2. The gas energy per unit mass is constant (Bernoulli with zero constant), so comparing states reduces to comparing densities. From eqs. (13), (15), (16): for u < 1, z decreases as λ increases at fixed x - every shell has lower energy in the λ = λc state than in any smaller-λ Type I state; and at λ = λc the Type II (transonic) branch has lower density than Type I for x < xm.
3. Expecting the lowest-energy available steady state to be the stable one, the system should sit in the Type II state with λ = λc. Bondi notes the caveats explicitly: the system is not isolated (the star is outside it) and is infinite in extent, so the energy-minimization principle is "not quite assured" - but the shell-by-shell agreement makes it "very likely", and it matches the intuition that nothing stops accretion, so it proceeds at the greatest possible rate.

## Validity verdict (step 6)

Reconstruction: premises = the shell-by-shell density comparison (z decreases with lambda at fixed x; Type II below Type I inside the sonic radius) plus the hidden premise, surfaced charitably, that an open steady system settles into the lowest-energy available steady state. Conclusion is already hedged to "expected to be physically realized". The hidden premise is a heuristic, not a theorem - Bondi flags exactly this (system not isolated, infinite extent) - so the argument is valid-but-weak: conditional on the premises the hedged conclusion follows, and its limited strength is for step 7 to price, not a validity failure. The density-comparison step itself is traced from the cited equations.
