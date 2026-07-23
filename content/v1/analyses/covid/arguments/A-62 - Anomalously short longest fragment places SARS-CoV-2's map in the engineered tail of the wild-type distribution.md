---
type: argument
id: 'A-62'
status: approved
reason_if_not_false: checked
statement: Given the in-vitro-genome-assembly constraints (5-8 fragments, longest <8 kb, even spacing), SARS-CoV-2's BsaI/BsmBI longest fragment (25% of genome) falls in the bottom 1% of a wild-type distribution of natural coronavirus digests and yields a more extreme z-score than any non-engineered virus examined (implying under 0.07% chance naturally), matching published synthetic clones.
source: '[[S-48 - Bruttel, Washburne & VanDongen 2022-23 — Endonuclease fingerprint indicates a synthetic origin]]'
locator: Results / Conclusion; Figs 3C-D, S2
affects_observations:
- '[[O-66 - SARS-CoV-2''s longest BsaI-BsmBI fragment is 7,578 bp (25% of genome) and it lacks two conserved BsaI sites]]'
- '[[O-65 - SARS-CoV-2 has five BsaI-BsmBI sites yielding six fragments with unique overhangs]]'
affects_hypotheses: ["[[H-43 - Research-related origin of a laboratory-manipulated virus (engineered lab leak)]]"]
---

Given the in-vitro-genome-assembly constraints (5-8 fragments, longest <8 kb, even spacing), SARS-CoV-2's BsaI/BsmBI longest fragment (25% of genome) falls in the bottom 1% of a wild-type distribution of natural coronavirus digests and yields a more extreme z-score than any non-engineered virus examined (implying under 0.07% chance naturally), matching published synthetic clones.

## Reasoning

The authors build an empirical 'wild-type distribution' by digesting ~70 natural coronavirus genomes in silico with a large enzyme set, recording the longest-fragment length as a function of fragment number. Engineered reverse-genetics clones sit anomalously low because researchers deliberately even-space sites to keep fragments short and few (e.g. iMERS-CoV longest fragment 19% vs an expected 40%; iWIV1 similarly short). SARS-CoV-2's BsaI/BsmBI longest fragment is 7,578 bp (25% of genome) versus an expected 43% for a 6-fragment digest, placing it in the bottom 1% of longest fragments among non-engineered CoVs. Restricting the reference set to Type IIS enzymes with 6-7 nt sites and 3-4 nt overhangs yields 1,491 digestions in the ideal 5-7 fragment range, within which SARS-CoV-2 has a more extreme z-score below the mean than any non-engineered virus found - translated by the authors to under 0.07% probability of such an anomalous map in a wild virus. Because these features are exactly what engineers impose for efficient assembly, the map is argued to be characteristic of synthetic assembly. The authors' stated limitations include no correction for phylogenetic dependence among CoVs, a uniform mutation-rate assumption, and consideration of point mutations but not recombination.

## Validity verdict — approved (checked)

Per the batch brief I judge only whether the inference follows from its stated premises, not whether the rarity statistic itself is correct. The step has a valid likelihood-ratio structure: engineered reverse-genetics clones deliberately even-space Type IIS sites to keep fragments short and few, so P(anomalously short longest fragment | engineered) is high, while the empirical wild-type distribution puts SARS-CoV-2's 25% longest fragment in the bottom ~1% (z-score more extreme than any non-engineered CoV examined; ~0.07% under the ideal-fragment-count reference set). Granting those figures, "the map sits in the engineered tail of the wild distribution" is close to a restatement of the premise, and the diagnosticity toward a synthetic origin follows because the map is both rare under nature and characteristic of engineering practice — a genuine high/low likelihood contrast, not a bare rarity-implies-cause fallacy. Probed defeaters that would not deny the statistic: the statement is descriptive/evidential ("places in the engineered tail," "under 0.07% chance naturally"), not "proves synthetic," so it does not overreach and needs no weakening. The look-elsewhere / enzyme-selection and phylogenetic-dependence / recombination objections all bear on whether the 0.07% figure is correctly computed — i.e. on the rarity statistic — which the brief places out of scope here and which is priced as a likelihood at step 8. Conditional on the premises, the inference holds. Approved.
