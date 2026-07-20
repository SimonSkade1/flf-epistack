# Hypothesis structure (step 4b)

generated: 2026-07-20

## Cluster inventory

1. [[HC-1 - Route of the first human SARS-CoV-2 infection]] — *By what route did SARS-CoV-2 first infect a human?*
	1. [[H-1 - SARS-CoV-2 first infected humans via zoonotic spillover at the Huanan market]]
	2. [[H-5 - SARS-CoV-2 first infected humans through a research-related incident at the WIV]]
	3. [[H-6 - The first human infection arose by neither route listed here]] (residual)

The whole question decomposes into a single cluster: this analysis's main question is itself one sub-question — one event, one route — and the curated evidence pulls apart exactly that dimension.

## Counts

| | |
|---|---|
| H in (from step 3) | 5 |
| active | 3 (H-1, H-5, H-6) |
| merged (4a) | 1 (H-2 → H-1) |
| dropped | 2 (H-3 dropped at 4b; H-4, absorbed into H-3 at 4a, cascaded to `dropped` with its merge preserved in `former_merged_into`) |
| minted at 4b | H-6 (residual), HC-1 |
| clusters | 1 |

## Carving decision (4b)

A second cluster on the *evolutionary origin* dimension — {H-3 natural evolution, + a constructed "laboratory-manipulated genome" complement, + residual} — was considered and rejected: the constructed complement restates H-5's own engineered-furin-site clause, and O-10, O-11, O-12 would discriminate both clusters in the same direction, double-counting that evidence at step 8 (rule 3; no `depends_on` note repairs it). H-3 was instead dropped as a straggler that clusters nowhere — it is true-but-non-competing, entailed by H-1 and consistent with H-5. Full reasoning in HC-1's body.
