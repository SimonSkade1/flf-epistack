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
