---
id: A-64
type: argument
statement: "Including gravitation in the bounce calculation (thin-wall limit): for decay from a zero-cosmological-constant false vacuum to a true vacuum of energy density -epsilon, gravity raises the bounce action and enlarges the critical bubble, and when epsilon ≤ (3/4) kappa sigma^2 = 6 pi G sigma^2 (equivalently rho_0 = 2 Lambda, eq. 3.21) the bubble radius diverges and the decay probability vanishes — gravitation totally quenches vacuum decay and stabilizes the false vacuum; in the opposite case (decay from a positive-energy vacuum into the present one), gravity works the other way, shrinking the bubble and making decay more likely."
source: "[[S-16 - Coleman & De Luccia 1980, Gravitational effects on and of vacuum decay]]"
locator: "§3, eqs. (3.20)-(3.22); Conclusions"
quote: "gravitation can totally quench vacuum decay ... Gravitation has stabilized the false vacuum."
affects_hypotheses: ["[[H-31 - Our vacuum may be a metastable false vacuum that decays by true-vacuum bubble nucleation]]"]
status: approved
reason_if_not_false: checked
---
Reasoning:

1. Setup: the flat-space theory gives Gamma/V = A e^(-B/hbar) with B computable from the O(4)-symmetric bounce; in the small-epsilon (thin-wall) limit the critical radius is rho_0 = 3 sigma/epsilon (sigma = surface tension = S_1). Gravity is added via the Euclidean Einstein-Hilbert action; the thin-wall approximation stays valid for arbitrarily strong gravitational corrections.
2. Downhill-to-AdS case: the negative interior energy density distorts geometry inside the bubble such that, below a critical epsilon, no bubble has a large enough volume-to-surface ratio to reach total energy zero — the flat-space trick of simply taking the bubble bigger fails because interior volume no longer grows like the flat-space rho^3. Quantitatively the corrected radius is rho = rho_0/(1 + (rho_0/2Lambda)^2)-type, with quenching at rho_0 = 2 Lambda where Lambda^2 = 3/(kappa epsilon): epsilon_crit = (3/4) kappa sigma^2 = 6 pi G sigma^2. For epsilon below this, the equations admit no solution: decay is impossible, not merely slow.
3. Uphill-frame case (de Sitter false vacuum decaying to zero-Λ): gravitation diminishes B and the materialization radius — decay is catalyzed. So gravitational effects on vacuum decay are direction-dependent: suppression/quenching when the endpoint is negative-energy, enhancement when decaying from positive energy.
4. The authors stress these effects are utterly negligible "in any conceivable application" at microphysical scales (the ratio rho_0/Lambda carries Newton's constant); they matter only in the late stages of decay and for the fate of the interior — but the quenching result is exact within the thin-wall treatment and defines when a metastable vacuum is in fact eternally stable. A final aside underlines the cosmological-constant puzzle: zero vacuum energy is "the edge of disaster," since even slight negativity would initiate catastrophic collapse.

## Step 6 verdict

Verdict: approved (checked). Traced the quench mechanism: with a negative-energy (AdS) interior the volume-to-surface ratio no longer grows like flat-space rho^3, so below a critical epsilon no bubble reaches zero total energy and the flat-space "just take the bubble bigger" move fails - decay impossible, not merely slow. Coefficient consistency checked internally: (3/4) kappa sigma^2 with kappa = 8 pi G gives 6 pi G sigma^2, and the quench condition rho_0 = 2 Lambda with Lambda^2 = 3/(kappa epsilon) reproduces the same epsilon_crit. The direction-dependence (catalysis for de Sitter -> flat decay) follows from the same energetics with signs flipped. The full Euclidean bounce derivation is CDL's, but the load-bearing quench step is carried by the traceable thin-wall energetics, so checked rather than trusted. Valid.
