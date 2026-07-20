---
type: cluster-review
cluster: "[[HC-4 - Bound on the exogenous terminal-catastrophe rate]]"
---

## What the analysis says

The cluster asks whether the Tegmark-Bostrom bound — exogenous terminal-catastrophe rate below ~1/Gyr at 99.9% confidence — holds. Two members, exhaustive by construction: [[H-5 - The exogenous terminal-catastrophe rate is below about 1 per Gyr at 99.9 percent confidence]] and its negation [[H-10 - The exogenous terminal-catastrophe rate is not bounded below 1 per Gyr]]. The prior deliberately sits near even odds, [0.504, 0.496], built as a product of three modeling hinges (distribution model 0.7 × uncorrelatedness 0.8 × derivation 0.9). A single edge, [[E-6 - O-10 × HC-4 — Earth's formation date is typical, not early]], does all the updating: Earth's typical formation date ([[O-10 - Habitable-planet formation times span many Gyr and Earth's formation date is unremarkably late]]) is likely under H-5 (0.7) and unlikely under H-10 (0.15, a rate-mixture average), at trust 0.8 (the S-23 cap). Posterior: [0.7615, 0.2385]. [[A-6 - Observer selection makes naive survival-based risk bounds uninformative]] (corrected/checked) removes the anthropic defeater rather than adding a discount, since the method compares among survivors.

## What the model may not capture

1. The whole bound stands on one paper's semi-empirical planet-formation-time distribution (Lineweaver-type), and the 99.9% claim lives in its weakly constrained tails; the prior prices this (p_dist_model 0.7) but that number is a judgment with no real reference class. The cluster note itself names this as the dominant failure route into H-10.
2. H-10 is a wide disjunction (any hinge fails, any rate above 1/Gyr), so its 0.15 likelihood is a mixture average over a range nothing in the model resolves — a marginally-failing bound (rate ~1-3/Gyr) is far more compatible with the datum than the two-member posterior split suggests, and the carve hides that.
3. Being ¬H-5, the answer is trivially "on the list"; the real out-of-model risk is that the typicality-test framing itself is wrong (e.g. observer-weighting depends on habitability evolution, not just survival), which would land in H-10 but for reasons no block prices.
4. Exogeneity restriction: the bound says nothing about human-modulated rates — correctly firewalled in the cluster's independence note, but a reader could over-read the backstop.

## What would help

1. An independent planet-formation-history model's tail behaviour compared against Lineweaver's — *exists, unread*; would most directly move p_dist_model.
2. The bound recomputed at lower confidence (e.g. 99%) to see how tail-sensitive the headline is — *exists, unread* (in S-23's derivation).
3. A rate-resolved carve of H-10 (marginal vs. gross failure) — *does not exist* in this run; step-4 rework.

## Confusions and contradictions

E-6's "Why this is evidence" and [[A-7 - Earth's unremarkably late formation time yields a selection-bias-free catastrophe-rate bound near 1 per Gyr]] state opposite tilt directions: E-6 says a high rate pushes surviving observers toward *early*-formed planets (later formation = larger past-light-cone exposure); A-7's step-6-checked derivation says the observer-weighted distribution tilts *late* (late formers have less elapsed time at risk). These are different hazard models (exposure since Big Bang vs. since formation) and cannot both be the paper's argument; the step-6 "checked" trace endorsed one while the edge asserts the other. The update direction survives either way — a typical date is the modal outcome under H-5 and surprising under a high rate whichever way the tilt runs — so the numbers stand, but the contradiction is real and shipped unfixed; the fix is a step-6/step-8 re-trace against S-23, not an edit here.
