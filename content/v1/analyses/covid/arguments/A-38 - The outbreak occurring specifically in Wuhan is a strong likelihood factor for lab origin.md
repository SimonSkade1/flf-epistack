---
id: A-38
type: argument
statement: "That the pandemic began in Wuhan - home to the main labs studying SARS-related bat coronaviruses - is more expected under a lab origin than under zoonosis and is thus a positive likelihood factor favouring lab origin; the size of that factor (Weissman's ~4.4 logits) is contingent on treating zoonotic-spillover probability as tracking raw wildlife-trade volume rather than human population, urbanisation, or detectability."
source: "[[S-64 - Weissman's 'An Inconvenient Probability' Bayesian analysis]]"
locator: "Wuhan-location factor section (Substack, v5.x)"
affects_observations: []
affects_hypotheses: ["[[H-43 - Research-related origin of a laboratory-manipulated virus (engineered lab leak)]]"]
status: corrected
reason_if_not_false: checked
---
## Reasoning
Under a zoonotic-wildlife hypothesis, a spillover could occur anywhere along China's (and SE Asia's) wildlife-trade geography, of which Wuhan handles a tiny fraction; Wuhan's markets handled under 0.01% of China's mammalian wildlife trade (raccoon dogs perhaps 1/2000 of national trade). Conditioning on the outbreak starting in Wuhan therefore removes ~99% of the zoonotic probability mass. Under a research-related origin, the relevant work (WIV and Wuhan CDC) was concentrated in Wuhan, so a Wuhan onset is near-expected. The ratio of these conditional probabilities gives a large positive logit, L2 ~= 4.4, in favour of lab origin. This is one of the dominant terms in the H-17 synthesis; it is partially dependent on the market-ascertainment issue (see the ascertainment argument), which is why it is not multiplied naively with the case-location evidence.

## Original
statement: "That the pandemic began in Wuhan - a city with under 1% of China's population but home to the main labs studying SARS-related bat coronaviruses - is far more expected under a lab origin than under zoonosis, contributing a large positive likelihood factor (about 4.4 logits)."

## Validity
Reconstruction. Premises: WIV/Wuhan-CDC work was concentrated in Wuhan (→ P(Wuhan onset | lab) near 1); Wuhan handles a tiny share (<0.01%) of China's mammalian wildlife trade. Load-bearing step: because zoonotic spillover "could occur anywhere along the wildlife-trade geography," conditioning on Wuhan removes ~99% of zoonotic probability mass, so the ratio P(Wuhan|lab)/P(Wuhan|zoonosis) ≈ e^4.4 ≈ 81.

Corrected. The step from "Wuhan's trade share is tiny" to "conditioning on Wuhan removes ~99% of zoonotic mass" requires the hidden premise that zoonotic-spillover probability is proportional to raw wildlife-trade volume. An undercutting defeater survives without denying the trade-share premise: spillovers that *seed a detected pandemic* are weighted toward large, dense, well-connected cities with early detection capacity (Wuhan is an 11M-person hub whose markets sold live susceptible mammals), so P(zoonotic outbreak first detected in Wuhan) can be far higher than Wuhan's raw trade share — this is precisely the contested crux in the Worobey/Pekar-vs-Weissman dispute. The defeater undercuts the *magnitude* (4.4 logits) but not the *direction*: the labs are pinned to Wuhan while a zoonotic origin retains geographic freedom, so P(Wuhan|lab) > P(Wuhan|zoonosis) still holds and the factor still favours lab. Per the step-06 pattern (a strong-magnitude / "far more expected" claim that survives only as an "is evidence for"), corrected to the direction-plus-caveated-magnitude form. Checked — I traced the reference-class dependence myself; it does not rest on author or venue.
