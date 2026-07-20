---
type: argument
id: "A-1"
statement: "The all-negative animal-sample result is much weaker evidence against an infected market animal than a timely sample would be, because sampling occurred after closure/disinfection and removal of live animals; it does not by itself exclude an infected animal, but it is not wholly uninformative either."
source: "[[S-2 - Liu 2023 Nature - China CDC environmental and animal surveillance at the Huanan market]]"
locator: "Methods/Discussion"
affects_observations:
  - "[[O-2 - No Huanan animal-origin sample (457 samples, 18 species) tested SARS-CoV-2-positive]]"
affects_hypotheses: []
status: corrected
reason_if_not_false: checked
---

The market was closed and disinfected from 1 Jan 2020 and most live animals removed before animal-material collection began on 18 Jan. A test can only detect virus in animals that are (a) still present and (b) not decontaminated. Both conditions were largely violated by the sampling timeline: the animals most likely to have been infected (live wildlife) were gone, and surfaces had been disinfected. Therefore the negative result has near-zero power to distinguish "no infected animal was ever present" from "infected animals were present but removed/decontaminated before sampling." The observation should not be read as evidence against a market animal reservoir; it is uninformative on that point rather than exculpatory.

## Original

statement (pre-edit): "The all-negative animal-sample result does not evidence against an infected market animal, because sampling occurred after closure/disinfection and removal of live animals."

## Step 6 verdict — corrected, checked

Reconstruction. P1: closure/disinfection began 1 Jan 2020 and most live animals were removed before animal-material collection started 18 Jan. P2 (hidden, load-bearing): a negative test carries evidential weight against "an infected animal was present" only in proportion to the probability that, had an infected animal been present, detectable viral material would still have been in the sampled pool. C: the negative result carries no weight against a market animal reservoir.

Traced load-bearing step. P2 is the standard likelihood-ratio-of-a-negative-test move and it does go through directionally: removal of exactly the taxa most likely to have been infected plus surface decontamination both push P(negative | infected animal present) upward toward P(negative | no infected animal present), collapsing the ratio toward 1.

Undercutting defeater that survives. The collapse is partial, not total. 457 animal-origin samples across 18 species were in fact obtained, so the sampled pool was not empty; the premises establish severe attenuation, not the near-zero power the as-stated conclusion asserts. "Most live animals removed" also leaves a residue, and frozen/carcass material is not fully addressed by surface disinfection. So the strong claim ("does not evidence against", "near-zero power") overreaches, while the weaker claim — that the negative is heavily discounted and cannot exclude an infected animal — is immune to this defeater. Corrected to that weaker evidential form; how much discount remains is step 8's to price.
