---
id: A-14
type: argument
statement: "The energy E_1/2 at which the integral spectrum falls to half its no-cutoff expectation is predicted to be 10^19.72 eV for protons under a wide range of assumptions about extragalactic sources (Berezinsky et al. 2006); TA measures log10(E_1/2/eV) = 19.72 +/- 0.05 (HiRes: 19.73 +/- 0.07), so the observed suppression sits quantitatively where the GZK proton mechanism - and not generic source physics - puts it."
source: "[[S-71 - Abu-Zayyad et al. 2013- Telescope Array surface-detector spectrum]]"
locator: "§4 Spectrum (E_1/2 paragraph); §5 Conclusions"
affects_observations: ["[[O-10 - Telescope Array SD spectrum shows an ankle at 4.6e18 eV and a 5.5-sigma flux suppression at 5.4e19 eV]]"]
affects_hypotheses: ["[[H-9 - The UHECR ankle and suppression are caused by GZK interactions of extragalactic protons with the CMB]]"]
status: approved
reason_if_not_false: checked
---
## Reasoning

1. The GZK mechanism (photo-pion production on the CMB) fixes an absolute energy scale set by the CMB photon field and the pion production threshold, nearly independent of source spectra, evolution, or distribution; Berezinsky et al. computed the summary statistic E_1/2 = 10^19.72 eV for protons across a wide range of such assumptions.
2. An instrumental artifact or an intrinsic source cutoff carries no reason to reproduce this particular energy: a priori it could fall anywhere. The measured value 19.72 +/- 0.05 landing exactly on the parameter-insensitive prediction is therefore evidence specifically for the propagation-loss (GZK, protonic) interpretation of the break rather than a coincidental cutoff.
3. Same for the ankle: the dip at ~5e18 eV coincides with the predicted e+e- pair-production dip for protons on the CMB, while heavier nuclei would not produce such a dip.
4. Caveat contained in the same paper: Auger's composition measurements (Xmax) suggest heavy primaries in the South, under which the suppression energy would instead reflect photodisintegration of nuclei; the E_1/2 match is strong but not decisive.

## Validity verdict (step 6)

Reconstruction: premise = E_1/2 = 10^19.72 eV is a near-parameter-free prediction of proton-GZK propagation; observation = TA measures 19.72 +/- 0.05. Load-bearing step: an alternative cause (instrument artifact, intrinsic source cutoff) has no reason to land on that particular energy, so the match is evidence specifically for the propagation-loss interpretation - a valid likelihood-ratio-shaped inference. Undercutting probe: heavy-composition photodisintegration can suppress near a similar energy; the body concedes this ("strong but not decisive") and the statement claims a quantitative location match with specificity against generic source physics, not proof - it survives as stated.
