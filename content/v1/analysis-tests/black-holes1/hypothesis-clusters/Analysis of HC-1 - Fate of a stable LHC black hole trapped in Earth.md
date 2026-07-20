---
type: cluster-review
cluster: "[[HC-1 - Fate of a stable LHC black hole trapped in Earth]]"
---

## What the analysis says

The cluster asks: if stable TeV-scale black holes were produced at the LHC and trapped in Earth (conditional on evaporation failing, HC-2, and production being possible, HC-3), would Earth be destroyed within the solar lifetime? Members: [[H-1 - Stable LHC black holes trapped in Earth would accrete it catastrophically within the solar lifetime]], [[H-2 - Stable LHC black holes pose no macroscopic risk to Earth within the solar lifetime]], [[H-6 - Stable LHC black holes have some fate or impact not listed here]]. The prior [0.3097, 0.5752, 0.115] was deliberately evidence-blind outside-view: a log-uniform spread over accretion timescales put ~35% of the plausible range below the 5 Gyr cutoff (`frac_log_range_fast = 0.35`, flagged in-block as an honest low-confidence guess). Two evidence items do all the updating, both with H-1 likelihood 0.1 and trust 0.74: the CG-1 joint block over [[E-2 - O-2 × HC-1 — Gyr-old neutron stars observed intact]], [[E-3 - O-3 × HC-1 — super-LHC cosmic-ray exposure of Earth, WDs and NSs]], [[E-4 - O-4 × HC-1 — Earth and Sun survived 4.5 Gyr of UHECR bombardment]] (lik [0.10, 1.0, 0.55]), and the lone [[E-1 - O-1 × HC-1 — old low-field white dwarfs observed intact]] (lik [0.1, 1.0, 0.6]). Posterior: [0.0354, 0.8882, 0.0764]. The inferential machinery is [[A-1 - Relativistic-escape loophole in the Earth cosmic-ray argument is closed by white-dwarf and neutron-star stopping power]] and [[A-2 - Every fast-accretion scenario is excluded by white-dwarf and neutron-star survival]] (both approved/checked), with [[A-3 - Charged or EM-interacting stable black holes are excluded directly by Earth and Sun survival]] corrected to a weaker, observer-selection-adjusted form.

What the verdict hinges on, inside this cluster: (1) every likelihood routes through a single source, [[S-1 - Astrophysical implications of hypothetical stable TeV-scale black holes]] (trust 0.74) — its cosmic-ray survival/exposure premise is the shared basis (D-1) of the CG-1 group; (2) A-2's P1, that danger-to-Earth implies fast accretion in denser WD/NS — exactly where Plaga's accretion-modelling challenge lives; (3) A-1's P2, that cosmic rays actually reach and are stopped in low-B WD surfaces.

## What the model may not capture

1. Single-source dependence is structural, not just a trust number: S-1 is a motivated source (CERN staff co-author, written as a rebuttal to Plaga and a lawsuit). The 0.74 cap prices data reliability, but motivatedness also shapes which counterarguments were presented at all — the strongest anti-safety argument may simply not exist in the source set. The CG-1/E-1 split into two edges gives the appearance of two independent updates, but both rest on the same paper's stopping-power and accretion machinery; if A-1's kinematics or A-2's density-scaling premise fails, both likelihoods fail together, and the effective evidence is closer to one item than two.
2. The prior's main driver, `frac_log_range_fast = 0.35`, has no reference class — the block admits it. The posterior H-1 mass (0.0354) scales nearly linearly with this guess (my observation, not a model number).
3. Is the true answer on the list? The members near-dichotomize "macroscopic damage within solar lifetime", so the carve is better than most; but H-6's 0.2 prior weight and its 0.55/0.6 likelihoods are stacked guesses. An unlisted fate (slow lethal heating, exotic charged-remnant dynamics) could matter more than H-6's posterior 0.0764 suggests, because sub-catastrophic fates would look observationally identical to H-2 in every observation used here — the evidence cannot separate them, and the blocks' 0.55/0.6 values quietly concede this.
4. H-1 vs H-2 exclusivity holds, but the observer-selection correction (A-3/A-6) is applied only to O-4; the claim that anthropic conditioning does NOT extend to distant NSs is asserted via A-6, not traced inside this cluster's blocks.

## What would help

1. An independent (non-G-M) computation of trapped-BH accretion rates in WD/NS matter, engaging Plaga's contested modelling directly — *exists, unread* (Plaga S-16 is in the source set; a neutral third-party adjudication may be *does not exist*).
2. Quantified UHECR flux actually incident on low-B WD surfaces (magnetospheric screening) — *exists, unread* (later follow-up literature on the WD bound was not priced).
3. Modelling of sub-catastrophic "H-6-type" fates and their observational signatures in NS/WD populations — *does not exist*, as far as this source set shows.

## Confusions and contradictions

Little irreducible conflict: the survival observations all point one way. The one genuine tension is that the analysis simultaneously trusts S-1's accretion machinery enough to set lik(H-1)=0.1 twice, and flags (via Plaga and the trust dock to 0.74) that this machinery is contested — the same contested physics enters once as likelihood and once as trust, and I cannot tell from inside the cluster whether that is a double-count or a correct decomposition. Step 8's comments assert the split is deliberate ("weaknesses priced in lik, not docked again in t"), which is coherent but unverifiable here. Shipped unfixed.
