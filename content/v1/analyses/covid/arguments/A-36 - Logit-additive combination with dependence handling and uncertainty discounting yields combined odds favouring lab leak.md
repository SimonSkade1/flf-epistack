---
id: A-36
type: argument
statement: "Combining the individual likelihood-ratio factors additively in log-odds (logits), while avoiding double-counting dependent factors and discounting each factor by its uncertainty, yields net odds favouring a research-related origin."
source: "[[S-64 - Weissman's 'An Inconvenient Probability' Bayesian analysis]]"
locator: "Methods / combination section (Substack, v5.x)"
affects_observations: []
affects_hypotheses: ["[[H-43 - Research-related origin of a laboratory-manipulated virus (engineered lab leak)]]"]
status: approved
reason_if_not_false: checked
---
## Reasoning
Weissman writes the posterior log-odds as a sum of logit contributions, ln(P(LL)/P(ZW)) = L0 + L1 + L2 + ..., with approximate values: prior L0 ~= -4.2 +/- 2.3 (about 1/70 favouring zoonosis), sarbecovirus-type L1 ~= 2.3, Wuhan-location L2 ~= 4.4, furin cleavage site ~= 2-3, and a restriction-enzyme / DEFUSE-matching pattern ~= 1-2. Dependence between factors is handled explicitly: the case-location data and the phylogenetic data are not treated as independent updates when they bear on the same particular version of the market-zoonosis hypothesis (the location data supported a version the phylogenetic data make implausible), so they are not multiplied as if independent. Uncertainty is propagated as distributions on each logit: uncertainty in a likelihood ratio discounts that ratio toward 1 but does not discount the prior, whereas uncertainty in the prior discounts both - so integrating over realistic uncertainty pulls extreme point odds back toward 1. The net still leaves lab leak favoured: point estimates drive P(zoonosis) below ~1%, and the uncertainty-integrated odds remain single-digit to low-double-digit favouring a research-related origin. This is the combination machinery that produces H-17's headline odds.

## Validity
Reconstruction. Premises: the individual logit values (L0 ≈ −4.2, L1 ≈ 2.3, L2 ≈ 4.4, FCS ≈ 2–3, RE ≈ 1–2); that dependent factors are not multiplied as independent; and that uncertainty is propagated as distributions on each logit. Load-bearing step: Bayes in odds form is additive in log-odds (ln posterior-odds = ln prior-odds + Σ ln LRᵢ for conditionally-independent evidence), so combining these logits and integrating over uncertainty yields net odds whose sign favours lab.

Checked. (1) The additivity itself is a valid theorem of Bayesian updating; the dependence caveat (not multiplying the case-location and phylogenetic factors, which bear on the same market-zoonosis sub-hypothesis) is the correct guard against double-counting and moves in the right direction. (2) The uncertainty claim — "uncertainty in a likelihood ratio pulls that ratio toward 1 but not the prior; uncertainty in the prior pulls both" — is defensible read as marginalizing the posterior probability over parameter uncertainty: E[P(zoonosis)] of a bounded quantity is pulled toward less-extreme values, i.e. odds toward 1. (3) The conclusion's *sign* is robust conditional on the premises: the positive logits (≈2.3+4.4+2.5+1.5 = 10.7) dominate the prior (−4.2) by a wide margin, so any symmetric discounting toward 1 leaves the net favouring lab without flipping.

Probed defeater: L1/FCS/RE all condition on the same DEFUSE plan, a shared dependence that could inflate the sum beyond what the explicitly-handled case-location/phylogenetic dependence covers. This bears on the *magnitude* of the net odds, not the validity of the additive-combination step or the sign of the result (priced at step 7/8), so it does not undercut the stated conclusion. Approved.
