---
id: S-43
type: source
source_type: journal-article
url: https://doi.org/10.1093/ve/vead089
venue: Virus Evolution
publication_date: 2023-12-30
citation_count: 3
citation_count_asof: 2026-07-23
field: computational virology
authors: [Jesse D. Bloom]
found_via: citation-chase from [[S-42 - Débarre — What we can and cannot learn from SARS-CoV-2 and animals in metagenomic samples from the Huanan market]]
motivatedness: same as [[S-39 - Bloom — Association between SARS-CoV-2 and metagenomic content of Huanan market samples]]; explicit rejoinder to [[S-42 - Débarre — What we can and cannot learn from SARS-CoV-2 and animals in metagenomic samples from the Huanan market]] and other critics.
trust_score: 0.66
trust_reason: reproducible pipeline (minimap2/coverM) with an internal positive control — other CoVs in the same dataset do correlate with their host mtDNA while SARS-CoV-2 does not — a genuine methodological strength; but an interested-party reanalysis of post-outbreak samples, subject to the same spatial-confound caveat and unreplicated
usefulness: 2.7
usefulness_reason: the internal positive-control comparison is a genuinely discriminating contribution to the host-association question, though still on the contested market metagenomic data
method_read: read-count quantification with a positive control (bamboo-rat/canine/rat CoVs track their hosts, SARS-CoV-2 doesn't); very low absolute SARS-CoV-2 reads (≤7) limit power
standing: Virus Evolution 2023 (peer-reviewed), 3 citations; explicit rejoinder to Débarre in the same exchange
angle: environmental-sampling
data_basis: ["[[D-1]]"]
combined_score: 0.432
curated: false
curation_reason: "Not curated: narrower Bloom read-count follow-up; S-39 is the curated Bloom representative on D-1."
---
Follow-up to [[S-39 - Bloom — Association between SARS-CoV-2 and metagenomic content of Huanan market samples]], responding to [[S-42 - Débarre — What we can and cannot learn from SARS-CoV-2 and animals in metagenomic samples from the Huanan market]] and other critiques. Shows absolute SARS-CoV-2 read counts are very low in most positive samples, and that other animal coronaviruses present in the same dataset (infecting known hosts) show much stronger read-count correlations with their true host's DNA than SARS-CoV-2 shows with raccoon-dog (or any other candidate host) DNA — used as an internal positive control showing the method can detect a real host association when one exists, and does not find one for SARS-CoV-2 and raccoon dogs.
relevance_note: strengthens Bloom's methodological objection with an internal positive-control comparison (other animal coronaviruses in the same dataset).
