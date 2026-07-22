---
id: A-17
type: argument
statement: "For steady, spherically symmetric accretion of a polytropic gas (p ∝ ρ^γ, 1 ≤ γ ≤ 5/3) at rest at infinity onto a point mass M, the hydrodynamic equations admit solutions only for accretion rates Ṁ = 4πλ(GM)²ρ∞/c∞³ with λ ≤ λc(γ), where λc runs from e^{3/2}/4 ≈ 1.12 at γ=1 to 1/4 at γ=5/3 - the rate scales as M² ρ∞ c∞^-3 and is bounded above."
source: "[[S-51 - Bondi 1952 — On spherically symmetrical accretion]]"
locator: "§§2-6, eqs. (3)-(19) and Table I"
affects_hypotheses: ["[[H-16 - Physical accretion realizes the maximal transonic rate, with an interpolation formula covering the moving-star case]]"]
status: approved
reason_if_not_false: checked
---
Reasoning (exact closed-form analysis; no data, no free parameters beyond γ):

1. Setup: continuity 4πr²ρv = Ṁ and Bernoulli ½v² + ∫dp/ρ - GM/r = 0 with p/p∞ = (ρ/ρ∞)^γ. Non-dimensionalize with r = x·GM/c², v = y·c, ρ = z·ρ∞ (c = sound speed at infinity), giving x²yz = λ (with Ṁ = 4πλ(GM)²c⁻³ρ∞) and ½y² + (z^{γ-1}-1)/(γ-1) = 1/x.
2. Substituting the local Mach number u = y z^{-(γ-1)/2} reduces the system to f(u) = λ^{2(γ-1)/(γ+1)} g(x), where f and g are each the sum of a positive and a negative power, hence each has a positive minimum (f at u=1, g at x = (5-3γ)/4).
3. Since the physical range of x (from the stellar surface, x ~ 1e-5 for the Sun, to infinity) contains g's minimum, a solution exists only if λ ≤ λc = [(γ+1)/2]^{-(γ+1)/2(γ-1)} · [(5-3γ)/4]^{-(5-3γ)/2(γ-1)}; Table I: λc = 1.12 (γ=1), 0.625 (γ=1.4), 0.5 (γ=1.5), 0.25 (γ=5/3). For λ > λc no steady solution exists at all.
4. Solution taxonomy: for λ < λc the flow is everywhere subsonic (Type I); exactly at λ = λc a smooth monotonic transonic solution exists (Type II, subsonic outside xm, supersonic inside - the case whose limiting γ→5/3 form makes Types I and II coincide). u → 0 at infinity by the boundary conditions.
5. Hence the derived scaling Ṁ ∝ M²ρ∞c∞⁻³ is forced by the equations; only the O(1) factor λ within (0, λc] is left undetermined by the steady-state analysis. This is the macroscopic gravitational-capture rate formula later applied (e.g. by Giddings-Mangano) to hypothetical stable black holes accreting stellar or planetary matter.

## Validity verdict (step 6)

Reconstruction: long but elementary closed-form fluid mechanics - continuity + Bernoulli + polytrope, nondimensionalized, reduced via the Mach variable to f(u) = lambda^(2(gamma-1)/(gamma+1)) g(x) with f, g each a sum of a positive and negative power. Traced the load-bearing existence step: f and g each have positive minima, the physical x-range contains g's minimum, so a steady solution exists only for lambda <= lambda_c; the scaling Mdot ∝ M^2 rho_inf c_inf^-3 is forced by the nondimensionalization itself. The lambda_c values follow from the stated closed form. Checked; no defeater conditional on the steady spherical polytropic premises.
