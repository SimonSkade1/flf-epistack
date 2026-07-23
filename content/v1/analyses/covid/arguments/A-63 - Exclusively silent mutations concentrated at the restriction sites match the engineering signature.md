---
type: argument
id: 'A-63'
status: approved
reason_if_not_false: checked
statement: That the BsaI/BsmBI sites differ from RaTG13 (12/12) and BANAL-52 (5/5) by exclusively synonymous mutations at a significantly elevated rate, with only 1.2% (RaTG13) / 0.1% (BANAL-52) of random in-silico mutants reaching an equal-or-greater z-score, matches the requirement that IVGA site modifications be silent and is argued to be unlikely under chance evolution.
source: '[[S-48 - Bruttel, Washburne & VanDongen 2022-23 — Endonuclease fingerprint indicates a synthetic origin]]'
locator: Results (mutation analysis); Fig 4
affects_observations:
- '[[O-67 - All BsaI-BsmBI-site differences from RaTG13-BANAL-52 are silent, at an elevated rate]]'
affects_hypotheses: ["[[H-43 - Research-related origin of a laboratory-manipulated virus (engineered lab leak)]]"]
---

That the BsaI/BsmBI sites differ from RaTG13 (12/12) and BANAL-52 (5/5) by exclusively synonymous mutations at a significantly elevated rate, with only 1.2% (RaTG13) / 0.1% (BANAL-52) of random in-silico mutants reaching an equal-or-greater z-score, matches the requirement that IVGA site modifications be silent and is argued to be unlikely under chance evolution.

## Reasoning

To modify restriction sites for in-vitro genome assembly without changing the encoded protein, engineers introduce only synonymous (silent) mutations, typically at wobble positions. SARS-CoV-2's BsaI/BsmBI sites differ from its two closest relatives by exactly such silent-only changes, and the density of silent mutations inside these sites is ~5-9x higher than in the rest of the genome (odds ratios 8.9 for RaTG13 and 5.2 for BANAL-52). In a simulation drawing the same number of substitutions in proportion to nucleotide frequencies, only 1.2% of RaTG13-derived mutants and 0.1% of BANAL-52-derived mutants produced a BsaI/BsmBI map with a z-score as extreme as SARS-CoV-2's. The authors argue the coincidence of (a) silent-only changes and (b) their concentration precisely at the sites that would be edited for assembly is the expected fingerprint of engineering and improbable under neutral natural evolution. They note the odds calculation for obtaining the specific wobble mutations is left to future work.

## Validity verdict — approved (checked)

Per the batch brief, I judge only whether the inference follows from the stated premises, not whether the rarity statistic is correct. Premises granted: the BsaI/BsmBI-site differences from RaTG13 (12/12) and BANAL-52 (5/5) are exclusively synonymous; silent-mutation density inside the sites is elevated ~5-9x (OR 8.9 / 5.2); and a substitution-resampling simulation puts only 1.2% (RaTG13) / 0.1% (BANAL-52) of mutants at an equal-or-greater map z-score. Conclusion: this matches the engineering requirement (site edits for IVGA must be silent to preserve the protein) and is improbable under neutral evolution. The first conjunct is near-definitional — engineering demands silent edits, the observed edits are silent. The second is supplied directly by the granted simulation figure, so "unlikely under chance" is the premise restated, not an inferential leap. Probed defeater not touching the statistic: synonymous changes dominate between closely related CoVs under strong purifying selection, so "exclusively silent" alone is weak — but the premise adds *elevated concentration precisely at the assembly-relevant sites* (the OR), which is what the neutral-evolution explanation does not predict, so granting that premise the defeater does not survive. A conflation exists (the 1.2%/0.1% z-score is the fragment-map anomaly of A-62, not a direct probability for the wobble pattern, which the authors defer), but the statement hedges accordingly ("matches the requirement... argued to be unlikely"), does not claim proof, and stays within what the granted premises license. Conditional on premises, the inference holds. Approved.
