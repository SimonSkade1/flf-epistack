---
type: hypothesis-cluster
id: HC-1
hypotheses:
  - "[[H-1 - Stable LHC black holes trapped in Earth would accrete it catastrophically within the solar lifetime]]"
  - "[[H-2 - Stable LHC black holes pose no macroscopic risk to Earth within the solar lifetime]]"
  - "[[H-6 - Stable LHC black holes have some fate or impact not listed here]]"
exclusivity: "H-1 asserts catastrophic accretion within the solar lifetime and H-2 asserts no macroscopic risk of any significance; both cannot hold of the same physics, and the residual covers every other fate."
exhaustive_by_construction: false
independence: "Conditional on stable black holes being produced and trapped (the shared antecedent of all members), which member holds is set by accretion physics and astrophysical exclusion arguments, not by the answers to the production, evaporation, or catastrophe-rate clusters."
depends_on:
  - "HC-2: all members condition on Hawking evaporation failing (the H-7 branch); if H-4 holds this cluster is moot rather than resolved"
  - "HC-3: all members condition on TeV-scale gravity making LHC black-hole production possible at all"
question: "If stable TeV-scale black holes were produced at the LHC and trapped in Earth, would they destroy it within the solar lifetime?"
relevance: "This is the main question's core: the ~zero-risk verdict is H-2 winning this cluster given its conditioning premises."
---
![[H-1 - Stable LHC black holes trapped in Earth would accrete it catastrophically within the solar lifetime]]
![[H-2 - Stable LHC black holes pose no macroscopic risk to Earth within the solar lifetime]]
![[H-6 - Stable LHC black holes have some fate or impact not listed here]]

The Giddings-Mangano danger-vs-safety question itself, carved as a conditional cluster: it only bites on the branch where evaporation fails (HC-2) and production is possible (HC-3). Not exhaustive by construction — the residual absorbs intermediate-damage fates and accretion regimes outside the analyzed bracket.

## Prior

```python
# HC-1 prior — fate of a stable LHC black hole trapped in Earth, conditional on the shared
# antecedent (evaporation fails per HC-2's H-7 branch, production possible per HC-3).
# Members in HC-1.hypotheses order: [H-1 catastrophic accretion, H-2 no macroscopic risk, H-6 residual].
# Evidence partition: no_observation_arguments.py --cluster HC-1 returns none. All four inbound
# edges — the lone edge [[E-1 - O-1 × HC-1 — old low-field white dwarfs observed intact]] and the
# CG-1 group ([[E-2 - O-2 × HC-1 — Gyr-old neutron stars observed intact]],
# [[E-3 - O-3 × HC-1 — super-LHC cosmic-ray exposure of Earth, WDs and NSs]],
# [[E-4 - O-4 × HC-1 — Earth and Sun survived 4.5 Gyr of UHECR bombardment]]) carry the case-specific
# astrophysical survival/exposure record that discriminates H-1 from H-2 — exactly the evidence
# whose strength (incl. A-3's observer-selection correction) step 8 must price. None is an
# outside-view base rate, so NO edge is marked used_for_prior; this prior is evidence-blind
# outside-view only. Arguments A-1/A-2/A-3 ride those edges and are likewise left to step 8.

# H-2 no macroscopic risk — the anchor. Pre-evidence, a ~10^-23 kg object accreting a planet
# faster than 5 Gyr requires an unusually efficient accretion regime; in generic (4D-like)
# gravity Bondi-type rates are hopelessly slow, so "too slow to matter" is the default outcome
# across the space of TeV-gravity scenarios and takes unit weight.
w_no_risk = 1.0

# H-1 catastrophic accretion, as odds vs H-2. Basis: before consulting any survival data, the
# trapped-BH accretion timescale is uncertain over very many decades (it swings with the number
# and geometry of extra dimensions and the crossover radius); treating log-timescale as roughly
# uniform over the plausible range, a substantial minority of that range lands below the ~5 Gyr
# solar-lifetime cutoff — the scenario was theoretically live enough to warrant G-M's analysis,
# so this is not sanded toward zero. Does not cover: the survival evidence (step 8's job).
# Confidence: low; this fraction is the cluster's main driver and an honest guess.
frac_log_range_fast = 0.35  # right iff ~a third of the a-priori-plausible log-timescale range for D>=5 scenarios lies below 5 Gyr
w_danger = w_no_risk * frac_log_range_fast / (1 - frac_log_range_fast)  # ~0.54 : 1 odds vs H-2

# H-6 residual — a fate neither member expresses: e.g. significant but sub-catastrophic damage,
# or a trapping/accretion regime outside the bracket the literature analyzed. Concretely: a BH
# that hollows out a lethal-but-not-terminal cavity, or exotic charged-remnant dynamics nobody
# modeled. In novel-physics questions carved into a stark binary like this, the truth falls
# outside the two named outcomes non-negligibly often — but the binary here is close to a
# dichotomy on "macroscopic damage within solar lifetime", so the miss rate is modest.
w_residual = 0.2  # ~0.2 : 1 vs H-2; ~11-12% of mass once normalised — its own argued weight, not a leftover

prior("HC-1", [w_danger, w_no_risk, w_residual])
```
