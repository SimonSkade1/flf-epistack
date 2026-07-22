---
id: A-9
type: argument
statement: "Catastrophic growth in the Casadio-Harms framework requires the critical mass M_c to exceed ~1.3x10^4 kg; Casadio et al.'s own defining conditions give M_c above that threshold for all warping lengths L > ~15 microns, and the experimental limit allows L up to 44 microns (M_c up to 1.1x10^5 - 2.2x10^6 kg, or 5.9x10^22 kg under their alternative eq. 16) - so their benign verdict rests on an unexplained restriction to L ~ 1 micron, not on evidence."
source: "[[S-30 - Plaga, On the potential catastrophic risk from metastable quantum black holes]]"
locator: "§8.2"
affects_observations: ["[[O-7 - Torsion-balance experiments limit the RS2 warping length L to below 44 microns]]"]
affects_hypotheses: ["[[H-8 - An LHC-produced metastable black hole could accrete at the Eddington limit and become catastrophic]]"]
status: approved
reason_if_not_false: checked
---
## Reasoning

1. Threshold: a collider mBH reaches the exponential Bondi-accretion regime after t_accr ~ 0.6 ms of subatomic accretion (from G-M eq. 4.22 with Casadio et al.'s parameters M_5 = 1 TeV, A = 53, K = 224 J/m^2, D = 5, thermal velocity 1500 m/s). Growth is catastrophic iff the decay time t_decay exceeds t_accr, which in the Casadio-Harms luminosity law happens once M_c > ~1.3x10^4 kg. Plaga agrees with Casadio et al.'s technical conclusion that for M_c < 10^4 kg growth is never catastrophic.
2. The gap: M_c is a free parameter fixed only as a function of L by Casadio et al.'s eq. (18)/(25); these give M_c > 1.3x10^4 kg for L > 15.3 (12.2) microns. The experimental bound is L < 44 microns at 95 percent CL (O-7), so L in 15.3-44 microns is not excluded; at L = 44 microns their eq. (18) [(25)] gives M_c = 1.1x10^5 kg [2.2x10^6 kg], for which t_decay ~ 0.3 s exceeds t_accr by ~50x - catastrophic growth. Their alternative 'possible choice' eq. (16) gives M_c = 5.9x10^22 kg, catastrophic for all reasonable L.
3. Casadio et al. instead set 'for example' L ~ 1 micron (M_c ~ 10^2 kg) and thereafter treated that value as an upper limit without stated reason. Until L > 15.3 microns (and the eq.-16 normalisation) are excluded with reasons, catastrophic growth remains an open possibility - this is the concrete content of the charge that parameter ranges were excluded 'without giving any reason'.

## Step 6 verdict

Verdict: approved (checked). Reconstruction: (P1) growth is catastrophic iff t_decay > t_accr, which in the Casadio-Harms luminosity law occurs once M_c >~ 1.3e4 kg (t_accr ~ 0.6 ms from G-M eq. 4.22 with Casadio et al.'s own parameters); (P2) Casadio et al.'s defining eqs. (18)/(25) give M_c as a function of L, crossing the threshold at L ~ 15.3 (12.2) microns; (P3) O-7 allows L up to 44 microns. (C) the benign verdict rests on an unargued restriction to L ~ 1 micron, so catastrophic growth remains open within the allowed range. Valid conditional on the equations as premises; the conclusion is an existence-of-gap claim at appropriately weak strength. The inter-source hybrid (G-M accretion time + Casadio-Harms decay law) is legitimate as an internal-consistency probe of Casadio et al.'s framework. Minor numeric note: 0.3 s vs 0.6 ms is ~500x, not the body's "~50x" - direction unaffected (only t_decay/t_accr > 1 is load-bearing). Valid.
