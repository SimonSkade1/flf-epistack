---
type: cluster-review
cluster: "[[HC-2 - Evaporation of TeV-scale black holes]]"
---

## What the analysis says

The cluster asks whether a TeV-mass black hole, if formed, evaporates near-instantly via Hawking radiation. Two members, exhaustive by construction: [[H-4 - Black holes radiate thermally and evaporate, so a TeV-mass black hole would decay near-instantly]] and its complement [[H-7 - Hawking evaporation fails and TeV-mass black holes are long-lived]]. The prior [0.891, 0.109] is purely theoretical, resting on [[A-5 - Semiclassical QFT in curved spacetime derives thermal emission with accelerating evaporation]]: framework-wrong gets 0.01, extrapolation-stabilizes 0.10. Updating comes from astrophysical survival: the joint block on [[CG-2 - HC-2 joint over O-2+O-4]] (E-8/E-9, likelihoods [1.0, ~0.468], t=0.74) and the lone white-dwarf edge [[E-7 - O-1 × HC-2 — intact old white dwarfs bound non-evaporating black holes]] ([1.0, 0.5], t=0.74). Under corrected [[A-6 - Observer selection makes naive survival-based risk bounds uninformative]], O-4 (Earth/Sun survival) is near-inert; the discrimination is carried by O-2 neutron-star survival. Posterior: [0.9561, 0.0439].

## What the model may not capture

1. The prior's anchor, A-5, is `approved` but `trusted` — the Bogoliubov derivation was never traced here. Everything above the 0.109 failure mass rests on consensus-plus-re-derivations, and A-5's own caveat says semiclassical control is weakest exactly at the TeV/near-Planck regime in question. This is the cluster's largest unchecked step, and it is a *theory* step: no observation in the model touches it directly.
2. All empirical discrimination routes through one source, [[S-1 - Astrophysical implications of hypothetical stable TeV-scale black holes]] (trust 0.74 caps every t), and the O-2/O-4 pair shares data-basis D-1. A single flaw in S-1's stopping-power or accretion analysis degrades E-7, E-8 and E-9 together; the model prices this only via the flat 0.74 cap.
3. The likelihoods are conditional on cosmic-ray production of TeV holes (`p_cr_production = 0.7` in CG-2), which is really HC-3's question smuggled in as a branch weight, and E-7's 0.5 leans on HC-1's unresolved accretion-speed question — the cluster's declared independence is strained in both directions.
4. Carving: the binary hides a physically real middle case — evaporation down to a stable Planck-mass relic. It nominally falls under H-7 ("fails to evaporate fully") but is safety-inert, so H-7's posterior mass overstates the dangerous fraction. No unlisted answer outside the binary exists (logical complement), so the carve, not exhaustiveness, is the issue.

## What would help

1. A traced or independently audited version of A-5's Bogoliubov step, or the analogue-gravity (e.g. Steinhauer-type) confirmations weighed explicitly — *exists, unread*.
2. An independent replication of S-1's neutron-star stopping-power and magnetosphere-penetration numbers — *unclear*.
3. Direct observation of astrophysical Hawking flux — *does not exist*.
4. A decomposition of H-7 into relic vs. accreting sub-cases — *does not exist* (would be a step-4 re-carve).

## Confusions and contradictions

The survival data is used at full cap trust (t=0.74) while its delivery/production caveats are priced inside `lik_surv_H7`, with a comment asserting no double-count; whether cap-trust and branch-weights cleanly partition the doubt is not verifiable from the blocks and I cannot fully tell. Second, A-6's correction inerts O-4 for Earth/Sun yet O-4 remains a CG-2 member contributing t-cap selection — harmless arithmetically (likelihood ~1 on that leg) but confusing to read. No irreducible evidential conflict: all observations point the same way; the real tension is theory-confidence vs. the regime where that theory is least controlled, and that is a part-2 item, not a contradiction in the data.
