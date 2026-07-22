---
id: A-22
type: argument
statement: In consistent alternatives to GR, extra (e.g. scalar) fields generically produce dipolar gravitational radiation scaling as (alpha_PSR - alpha_WD)^2; because the white dwarf is weakly self-gravitating (alpha_WD ~ alpha_0, with |alpha_0| < 0.004 from Solar System tests), the measured Pb-dot(obs)/Pb-dot(GR) = 1.05 +/- 0.18 for PSR J0348+0432 implies |alpha_PSR - alpha_0| < 0.005 (95% CL), excluding significant strong-field scalarization even at ~2 Msun and limiting deviations of merger GW phase evolution from GR templates to < ~0.5 cycles for long-range fields.
source: "[[S-80 - Antoniadis et al. 2013, A Massive Pulsar in a Compact Relativistic Binary]]"
locator: "Discussion §'PSR J0348+0432 as a testbed for gravity' (eq. 1) and §'Constraints on the phase evolution of neutron-star mergers'; Fig. 4"
affects_observations: ["[[O-19 - PSR J0348+0432 orbital decay matches the general-relativistic gravitational-wave prediction]]"]
affects_hypotheses: ["[[H-13 - General relativity correctly describes gravity and gravitational radiation even in the strong-field regime of a 2-solar-mass neutron star]]"]
status: approved
reason_if_not_false: checked
---
## Reasoning

1. For a nearly circular binary, the leading non-GR change in orbital period is the dipole term Pb-dot(dipolar) ~= -(4 pi^2 G / c^3 Pb) * (M_PSR M_WD/(M_PSR+M_WD)) * (alpha_PSR - alpha_WD)^2, where alpha_i are effective couplings of each body to the extra field(s).
2. The WD's fractional binding energy is only ~ -1.2e-5, so alpha_WD reduces to the linear matter-field coupling alpha_0, already bounded (|alpha_0| < 0.004) by Solar System experiments. The asymmetric NS-WD system is therefore a clean dipole antenna: any strong-field enhancement of alpha_PSR (e.g. spontaneous scalarization, which can push alpha_PSR toward unity at high binding energy even for vanishing alpha_0) would show up directly in Pb-dot.
3. Observed agreement Pb-dot(obs)/Pb-dot(GR) = 1.05 +/- 0.18 then yields |alpha_PSR - alpha_0| < 0.005 (95% CL). The novelty is the regime: PSR J0348+0432 has ~2x the fractional binding energy of the double-pulsar neutron stars, where nonlinear strong-field effects could have first appeared; the calculation is illustrated in scalar-tensor theories but the paper argues the derived limits are essentially EOS-independent (a stiff EOS choice makes them conservative).
4. Scope limits stated: dipolar radiation from short-range fields (mass > ~1e-19 eV/c^2) is not excluded; the bound covers long-range fields influencing the binary dynamics.

## Validity verdict (step 6)

Reconstruction: premises = the leading dipole radiation formula ∝ (alpha_PSR - alpha_WD)^2 (standard result in scalar-tensor gravity, taken as premise), the WD's negligible self-gravity forcing alpha_WD ~ alpha_0, and |alpha_0| < 0.004 from Solar System tests. Load-bearing step traced: an asymmetric NS-WD binary is then a clean dipole antenna, so Pb-dot(obs)/Pb-dot(GR) = 1.05 +/- 0.18 caps (alpha_PSR - alpha_0)^2, giving |alpha_PSR - alpha_0| < 0.005 - simple propagation from the quoted formula. Scope limits (long-range fields only; EOS-dependence argued conservative) are stated in the body and carried in the conclusion. Valid conditional on the premises.
