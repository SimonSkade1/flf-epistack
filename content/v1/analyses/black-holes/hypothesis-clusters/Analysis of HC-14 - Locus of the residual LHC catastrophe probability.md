---
type: cluster-review
cluster: "[[HC-14 - Locus of the residual LHC catastrophe probability]]"
---

#### What the analysis says

Does the actionable LHC catastrophe probability come from the physics or from the chance the safety *argument* is flawed? Two members, a proposition and its complement: [[H-11 - The actionable LHC catastrophe probability is dominated by the chance the safety argument itself is flawed]] and [[H-46 - The published LHC safety arguments are robust and their conditional bounds carry through]]. Prior `[0.856, 0.144]`, built on the Ord–Hillerbrand–Sandberg decomposition ([[A-1 - A stated catastrophe probability is conditional on the argument's soundness and is dominated by argument-failure when very small]]): `P(X)=P(X|A)P(A)+P(X|¬A)P(¬A)`, so H-11 holds iff `P(¬A)·P(X|¬A) > b ≈ 1e-9`. H-46's `0.144` is a product of two asserted gates — `p_layering=0.40` (that [[A-2 - Independent sub-arguments multiplicatively shrink the probability that a safety case fails]] buys ~2–3 orders over the O-12 ~1e-3 base rate) times `p_low_pXnotA=0.36`. E-24 (error rates ~1e-3) and E-26 (Castle Bravo) were priced into the prior; the lone update is E-27 (RHIC flaw, `lik [1.0, 0.55]`, `t=0.75`), lifting the posterior to `[0.9005, 0.0995]`.

#### What the model may not capture

The binary is exhaustive on paper but not a well-posed empirical question: no world-state makes H-11 vs H-46 true the way strangelet stability has one. The `0.90` is a credence about a credence — the OHS framing's own conclusion re-priced. The source calls its figures "illustrative, not calibrated" (H-11 body), so the ~6-order `b`-vs-`P(¬A)` gap the cluster turns on rests on an uncalibrated illustration hardened into a gate.

The reference class is a poor fit, partly availability-driven: general published-paper error rates (O-12) and Castle Bravo (O-13, n=1, non-accelerator, famous *because* it failed) stand in for a multiply-replicated, red-teamed safety case — exactly the mismatch A-2 exists to correct, yet A-2 enters as one hand-set factor rather than a derivation.

E-27 is priced only half-honestly. The RHIC episode is double-edged: a serious flaw persisted ~5 yr (favours H-11) *and* was corrected with the bound holding <1e-12/yr (the self-repair H-46 leans on). The model charges only the first into `lik_H46=0.55` and lets the second merely cap the drop — arguably it should push `lik_H46` back up.

Anthropic-shadow consistency is the load-bearing point. The RHIC flaw *was* an observation-selection flaw, and HC-4/HC-10 price that shadow per-edge (E-43 docks trust; E-12 `t=0.3`). So the physics clusters already treat survival evidence as unsafe-biased — itself an instance of H-11's thesis, cohering with the high H-11 mass. The risk runs opposite: shadow discounted per-edge *and* argument-failure mass applied again at HC-14 lets step 10 double-count. Flag, don't resolve here.

Is the answer on the list? Both members inherit OHS's decomposition. A suppressed third framing: `P(X|A)` is ill-defined because "the argument" is a shifting corpus, not one object with a soundness bit. If distributed safety cases fail that way, both members are wrong together — and that failure is more consequential than either listed one.

#### What would help

1. A calibrated `P(¬A)` for adversarially-replicated safety cases specifically — *does not exist*.
2. Flaw base rate in the narrow accelerator/cosmic-ray-safety genre (currently n=1) — *does not exist*.
3. Whether GM's ~3 layers share modelling assumptions, the real `p_layering` — *exists, unread*.
4. OHS's own sensitivity of their conclusion to the illustrative figures — *exists, unread*.

#### Confusions and contradictions

The RHIC episode points both ways and is collapsed by fiat into one sub-unity likelihood ratio; whether an error-correction track record is evidence *for* fragility or robustness is irreducible here. And the anthropic shadow is both the *content* of E-27's flaw and a separately-priced discount in the physics clusters — without step 10 you cannot tell if it has been counted once or twice.

#### External consensus

OHS "Probing the Improbable" (2010) is a standard GCR/x-risk reference; its claim that internal extreme-risk estimates are floored by argument-error rates is broadly accepted there. The particle-physics mainstream effectively takes H-46 (reports treated as settled). The `0.90` on H-11 sits with the x-risk methodologists and against the physics establishment — the expected divergence given which literature the analysis weights.
