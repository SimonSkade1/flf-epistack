---
id: A-23
type: argument
statement: "Because the theoretical E1/2 value (10^19.76 eV, Berezinsky-Grigor'eva) is robust across a wide range of source spectral slopes, the agreement of HiRes's measured E1/2 = 10^(19.73 ± 0.07) eV with it is strong evidence that the observed break is the proton-GZK cutoff rather than a source-spectrum artifact - a test insensitive to the injection power law, though it does not by itself exclude a heavy-composition (photodisintegration) origin of a suppression at a similar energy."
source: "[[S-60 - Abbasi et al. 2008- HiRes first observation of the GZK suppression]]"
locator: "p. 4, E1/2 ¶ (method of Berezinsky & Grigor'eva 1988)"
affects_observations: ["[[O-37 - HiRes E-half energy of 10^19.73 eV matches the theoretical GZK prediction of 10^19.76 eV]]"]
affects_hypotheses: ["[[H-25 - The observed suppression at 6e19 eV is the GZK cutoff from photo-pion losses on the CMB]]"]
status: corrected
reason_if_not_false: checked
---
Reasoning:

1. A break in a measured spectrum could in principle reflect source properties rather than propagation: Berezinsky et al. show the local source density changes the power law above the cutoff, and the sources' average injection index could shift the apparent cutoff energy somewhat.
2. The E1/2 statistic - the energy at which the integral spectrum falls to half the no-cutoff extrapolation - is predicted to be 10^19.76 eV for GZK proton propagation over a wide range of injection spectral slopes, i.e. it is a nearly parameter-free signature of the propagation origin of the break.
3. HiRes computes E1/2 from its monocular spectra plus the fitted middle-segment power law and obtains 10^(19.73 ± 0.07) eV, statistically indistinguishable from the prediction.
4. Hence the break is identified as the GZK cutoff (not a source artifact) by a test largely orthogonal to the fit that located the break - the nontrivial step connecting the measured suppression to the GZK interpretation.

## Original

statement (pre-step-6): "Because the theoretical E1/2 value (10^19.76 eV, Berezinsky-Grigor'eva) is robust across a wide range of source spectral slopes, the agreement of HiRes's measured E1/2 = 10^(19.73 ± 0.07) eV with it identifies the observed break as the GZK cutoff in a way that is insensitive to the main free parameter (the injection power law) that could otherwise mimic or shift a break."

## Validity verdict (step 6)

Verdict: corrected. Reconstruction: premise = E1/2 is insensitive to the injection spectral index for proton-GZK propagation; observation = measured 10^(19.73 +/- 0.07) vs predicted 10^19.76. As originally stated, the conclusion - the match "identifies the observed break as the GZK cutoff" - overclaims: an undercutting defeater survives, namely a heavy-composition (photodisintegration) cutoff that produces a suppression near the same energy without the proton-GZK mechanism; the E1/2 test discriminates against source-spectrum explanations but not against that alternative (the same defeater A-14's source concedes). The weaker, evidential conclusion is immune to it, so the statement was edited to that form; original preserved below.
