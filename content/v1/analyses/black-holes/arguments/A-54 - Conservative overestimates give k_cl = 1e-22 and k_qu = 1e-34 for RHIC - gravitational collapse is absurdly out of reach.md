---
id: A-54
type: argument
statement: "Assuming all collision energy (M = 1e4 GeV) concentrates in the Lorentz-contracted nuclear volume (R = 1e-15 cm) — a wild overestimate that also ignores charge and momentum resisting collapse — the black-hole criticality parameter k_cl = 2GM/Rc2 is ~3e-33 (the source prints 1e-22, an ~11-order arithmetic overstatement in the conservative direction), and the graviton-emission parameter k_qu = GE2/(hbar c5) at E ≈ 200 GeV is 1e-34; both so far below unity that refinement is pointless."
source: "[[S-3 - Busza, Jaffe, Sandweiss, Wilczek- Review of Speculative Disaster Scenarios at RHIC]]"
locator: "§III, eqs. (9)-(11)"
affects_hypotheses: ["[[H-27 - Under standard gravity, collider collisions are at least 22 orders of magnitude too weak to form a black hole]]"]
status: corrected
reason_if_not_false: checked
---
Reasoning (the calculation):

1. Classical: a horizon forms when k_cl = 2GM/Rc2 → 1. Take every bit of CM energy of a gold-gold collision, M = 1e4 GeV/c2, packed into R = 1e-2 x 1e-13 cm (Lorentz contraction factor 1e-2 on a nuclear radius) — the largest mass and smallest radius the collision defines. Result: k_cl = 1e-22. Electric charge and constituent momenta, both ignored, would further resist collapse.
2. Quantum: graviton-emission probability is governed by k_qu = G E2 / (hbar c5); for elementary-constituent collisions at RHIC, E ≈ 200 GeV gives k_qu ≈ 1e-34 (units where 1 = gravity as strong as the nuclear force).
3. Supporting kinematic point: total CM energy is the wrong measure of danger (a batted fastball exceeds it); what matters is energy density and constituent-level energies, and Tevatron/LEP have already collided elementary constituents at higher energies than RHIC's ~200 GeV without incident. RHIC's novelty is volume and quark count, not constituent energy, and its higher energy actually lowers stopping power, making it worse at raising nuclear density than lower-energy machines.

## Step 6 verdict

Verdict: corrected (checked). Recomputed k_cl from the stated inputs: 2GM/c^2 for M = 1e4 GeV (1.78e-20 g) is 2.6e-48 cm (sanity anchor: solar r_s = 3 km scaled by 1.78e-20/2e33); divided by R = 1e-15 cm this gives k_cl ~ 2.6e-33, not the 1e-22 printed in the source (verified against the fetched text of hep-ph/9910333: "With M = 10^4 GeV/c^2 and R = 10^-2 x 10^-13 cm, we arrive at kcl = 10^-22"). The source's number is an arithmetic slip of ~11 orders, in the conservative (safe) direction. k_qu verified: (200 GeV / 1.22e19 GeV)^2 = 2.7e-34 - correct as stated. The kinematic supporting point (constituent-level energy, not total CM energy, is the relevant measure) is valid. Conclusion "absurdly out of reach, refinement pointless" holds a fortiori with the corrected number - hence corrected rather than approved (the load-bearing numeric step as stated did not go through) or rejected (the fixed version plainly does).

## Original

Assuming all collision energy (M = 1e4 GeV) concentrates in the Lorentz-contracted nuclear volume (R = 1e-15 cm) — a wild overestimate that also ignores charge and momentum resisting collapse — the black-hole criticality parameter k_cl = 2GM/Rc2 is 1e-22, and the graviton-emission parameter k_qu = GE2/(hbar c5) at E ≈ 200 GeV is 1e-34; both so far below unity that refinement is pointless.
