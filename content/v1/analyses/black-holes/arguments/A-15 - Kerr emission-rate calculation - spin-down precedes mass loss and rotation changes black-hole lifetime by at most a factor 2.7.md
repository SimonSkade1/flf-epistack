---
id: A-15
type: argument
statement: Numerically integrating the Teukolsky-equation absorption probabilities (greybody factors, including superradiance) for massless spin 1/2, 1, and 2 fields on a Kerr background gives emission rates that rise steeply with specific angular momentum - power enhanced up to 13.35x (neutrinos), 107.5x (photons), 26,380x (gravitons) at extremality versus a Schwarzschild hole of equal mass - with angular momentum radiated several times faster than energy, so a fast-spinning hole spins down to near-zero rotation before losing most of its mass, and its total lifetime differs from the nonrotating case by only a factor 2.0-2.7.
source: "[[S-72 - Page 1976 — Particle emission rates from a black hole II (rotating)]]"
locator: "abstract; results tables (Phys. Rev. D 14, 3260-3273)"
affects_hypotheses: ["[[H-10 - Rotating micro black holes evaporate essentially as fast as nonrotating ones - lifetime differs by at most a factor 2.7]]"]
status: approved
reason_if_not_false: trusted
---
## Reasoning

1. Semiclassical QFT on a Kerr background: each massless field mode of frequency omega and angular numbers (l,m) is emitted at the Hawking rate dN/dt = Gamma_lm(omega) / (exp[(omega - m*Omega_H)/T_H] -/+ 1), with Gamma the greybody (absorption) probability from the Teukolsky equation, Omega_H the horizon angular velocity, T_H the Hawking temperature. Rotation both lowers the effective Boltzmann factor for co-rotating modes (m*Omega_H term) and opens superradiant amplification, so emission grows steeply with spin - most for high-spin fields (gravitons, factor up to 26,380).
2. Integrating dM/dt and dJ/dt over all modes shows d(ln J)/dt exceeds d(ln M)/dt several-fold at every spin; hence J is exhausted first and the hole asymptotically approaches the Schwarzschild evaporation track for the remainder of its life (also proving the third law - extremality cannot be reached - for small perturbations).
3. Because the enhanced-emission (spinning) phase removes only an order-unity fraction of the mass, the total lifetime is bracketed within 2.0-2.7x of the nonrotating value for any initial spin; e.g. an initially maximally rotating primordial hole of ~7e14 g decays within the age of the universe versus ~5e14 g nonrotating.
4. Bearing on the collider scenario: two-parton collisions at nonzero impact parameter generically produce rotating holes, so this calculation - not the idealized Schwarzschild one - is the applicable evaporation rate; it says rotation cannot stabilize a micro black hole or extend its life by more than a factor ~3, conditional on semiclassical Hawking emission being real.

## Validity verdict (step 6)

Reconstruction: premises = semiclassical Hawking emission on Kerr with Teukolsky greybody factors; conclusion = spin-down precedes mass loss and total lifetime is within 2.0-2.7x of Schwarzschild. Qualitative structure checked: the m*Omega_H chemical-potential term and superradiance enhance co-rotating emission, and d(lnJ)/dt > d(lnM)/dt implies J is exhausted first, after which the hole follows the Schwarzschild track. The quantitative load-bearing results (enhancement factors up to 26,380x; the 2.0-2.7 bracket) rest on Page's numerical mode-sum integrations, infeasible to redo at reasonable cost - trusted: these are standard results independently reproduced by later evaporation codes, with no published refutation.
