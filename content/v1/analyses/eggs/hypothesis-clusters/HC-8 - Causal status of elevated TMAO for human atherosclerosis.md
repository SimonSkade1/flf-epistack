---
type: hypothesis-cluster
id: HC-8
hypotheses:
  - "[[H-15 - Gut flora convert dietary phosphatidylcholine-choline to TMAO, which causally promotes atherosclerosis independent of lipids]]"
  - "[[H-16 - Elevated plasma TMAO is a clinically meaningful (causal) cardiovascular risk factor in humans]]"
  - "[[H-45 - TMAO is a non-causal marker not itself atherogenic in humans]]"
exclusivity: "Assigned to the highest causal rung that holds, the members are mutually exclusive: a real animal-model mechanism whose human translation is open (H-15), human clinical causality (H-16), or a non-causal marker (H-45)."
exhaustive_by_construction: true
independence: "TMAO's intrinsic causal status is a property of the molecule and biology, independent of how much any particular food raises it (HC-9); its base rate does not move with the egg-exposure answer."
depends_on:
  - "HC-9: TMAO causality gates whether the egg->TMAO exposure matters"
question: "Is elevated plasma TMAO itself causally atherogenic in humans, or a non-causal marker?"
relevance: "Whether the whole choline/TMAO harm thread is real at all."
---

![[H-15 - Gut flora convert dietary phosphatidylcholine-choline to TMAO, which causally promotes atherosclerosis independent of lipids]]

![[H-16 - Elevated plasma TMAO is a clinically meaningful (causal) cardiovascular risk factor in humans]]

![[H-45 - TMAO is a non-causal marker not itself atherogenic in humans]]

## Carving

The sub-question is TMAO's causal standing for human atherosclerosis, read as mutually exclusive rungs. H-15: the gut-flora choline->TMAO->macrophage-foam-cell mechanism is genuine, established in Apoe-null mice and antibiotic/germ-free manipulation, but its human translation is open. H-16: beyond the mechanism, elevated TMAO is a clinically meaningful causal cardiovascular risk factor in humans. H-45 (constructed): TMAO is a non-causal marker of impaired renal clearance, dysbiosis, or an unhealthy dietary pattern, not itself a cause. Assigning each scenario to the highest rung that holds makes the three exclusive and jointly exhaustive of the causal-status space, so exhaustive_by_construction is set and no residual is needed. Analysis-failure mode: if the human TMAO-outcome associations are confounded by renal function or dietary pattern, or reflect reverse causation, the analysis would wrongly seat probability on H-16 when H-45 (marker-only) is correct - the failure favours the constructed marker member. H-45 is minted because no curated paper states the null outright yet the space requires it.

## Prior

```python
# HC-8 prior — causal status of elevated plasma TMAO for human atherosclerosis. Members in HC-8.hypotheses order:
# [H-15 real gut-flora choline->TMAO mechanism, human translation open; H-16 TMAO clinically causal in humans;
#  H-45 non-causal marker in humans]. exhaustive_by_construction: true -> no residual member (rungs cover the space).
# Evidence split: all eight inbound E edges (E-59/67/68/69 mouse causal chain in CG-24, E-70/71 human angiography
# associations in CG-25, E-72/73 human TMAO->platelet coupling in CG-26) are TMAO-SPECIFIC discriminating
# observations — they separate the marker pole from the mechanism poles, or H-16 from H-45 — so NONE is marked
# used_for_prior; they are priced at step 8, which will lift H-15/H-16 above this blind prior. no_observation_arguments.py
# --cluster HC-8 returns none. So this prior is a pure OUTSIDE VIEW: treat TMAO as an as-yet-unadjudicated
# CVD-associated metabolite proposed with a mechanism, and price the three rungs from the base rate of such candidates.

# H-15 — the mouse choline->flora->TMAO->foam-cell mechanism is genuine but its human translation is unresolved
# (the middle rung). What must hold: a real, replicable animal mechanism AND human clinical causality not (yet)
# established. Reference class: metabolites with a concrete proposed CVD mechanism plus observational human
# associations — most that carry any genuine causal role sit here (mechanism real, human effect open/modest) rather
# than clearing the top rung. Omits the TMAO-specific mouse and human data (step 8). This is the largest of the two
# causal rungs; I hold it more likely than H-16 but less likely than the marker H-45.

# H-45 marker anchor — the unit weight. Outside-view base rate: a novel CVD biomarker with an observational
# association is, more often than not, non-causal. Reference class of overturned candidates: homocysteine, CRP,
# HDL-cholesterol, vitamin E and beta-carotene all showed CVD associations later excluded by Mendelian-randomization
# or RCT. Blind to TMAO's own manipulation/genetic evidence, the marker reading carries the plurality of prior mass.
w_marker = 1.0  # H-45 anchor: high outside-view base rate that an observationally-associated CVD biomarker is non-causal

# Causal family (H-15 + H-16) as odds vs the marker. A metabolite proposed WITH a concrete gut-flora mechanism is a
# little more likely than the average association-only biomarker to carry some real causal role, so the causal family
# slightly outweighs the marker before any TMAO-specific evidence — but the reference class still cautions strongly.
causal_family_vs_marker = 1.2  # would be right if ~55% of mechanism-backed CVD-metabolite candidates carry some causal role
w_causal_family = causal_family_vs_marker * w_marker

# Split the causal family between the top rung (H-16, established human clinical causality) and the middle rung
# (H-15, real mechanism / human translation open). The top rung is a high bar — even LDL and Lp(a) needed decades and
# genetic proof — so a minority of genuinely-causal candidates are already ESTABLISHED as human-clinical; most sit at
# "real but human-open". Hence the smaller share to H-16.
share_human_established = 0.4  # would be right if ~40% of the causal-role mass is already at established-human-causality
w_h16 = w_causal_family * share_human_established              # H-16 top rung
w_h15 = w_causal_family * (1 - share_human_established)        # H-15 middle rung (complement, an identity not an estimate)

prior("HC-8", [w_h15, w_h16, w_marker])
```
