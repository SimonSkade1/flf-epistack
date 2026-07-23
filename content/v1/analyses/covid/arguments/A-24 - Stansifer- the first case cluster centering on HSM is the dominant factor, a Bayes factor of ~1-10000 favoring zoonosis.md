---
id: A-24
type: argument
statement: "The earliest significant covid cluster being centered on residents of the west half of the Huanan market yields a Bayes factor of ~1/10000 favoring zoonosis — P(H|Z)=1/600 vs P(H|LL)=1/(1.2e7), a raw ratio of 1/20000 softened by 2x for vendors' higher exposure — the single dominant factor in Stansifer's table and the crux of his conclusion."
source: "[[S-70 - Judge Eric Stansifer's written decision]]"
locator: "§4 / §7.3 First cluster in HSM"
affects_observations: []
affects_hypotheses: ["[[H-41 - Natural zoonotic spillover with no research involvement]]"]
status: approved
reason_if_not_false: checked
---
## reasoning
Stansifer models the probability that the first significant cluster appears where it did as 1 over the population of the smallest epidemiological circle containing both the primary and index case. Under zoonosis (Z) the spillover is at HSM, so that circle is essentially the west-half HSM population, P(H|Z)=1/600. Under lab leak (LL) the virus enters via a WIV researcher living anywhere in Wuhan, so the circle is all of Wuhan, P(H|LL)=1/(1.2x10^7); the ratio is ~1/20000. He then grants LL an extra factor of 2 (a market vendor is more likely than an average resident to catch a respiratory illness), giving ~1/10000 favoring Z. He rebuts Rootclaim's counter-model (that even under zoonosis the first *detected* cluster need not coincide with the spillover site, so HSM is "probably a coincidence"): conditioning on zoonotic spillover, the hypothesis that the first detected superspreading event is at the spillover site better explains the observed early-case geography, so the market centrality is not explained away. This "relative epidemiological proximity of the earliest indicators of covid to a plausible animal source rather than a potential laboratory source" is, in his words, the primary basis for the conclusion, and dominates the total (log-odds -9.2).

## Validity assessment
Reconstruction. Premise (model): the probability the first significant cluster appears where it did equals 1/(population of the smallest epidemiological circle containing both primary and index case). Given Z the spillover is at HSM → circle ≈ west-half HSM population, P(H|Z)=1/600; given LL the researcher lives anywhere in Wuhan → circle = all Wuhan, P(H|LL)=1/1.2e7. Conclusion: the likelihood ratio favours Z by ~1/10000 after a 2× exposure softening.

Evaluation (checked). Arithmetic verified: (1/1.2e7)/(1/600) = 600/1.2e7 = 1/20000; softening P(H|LL) upward by 2× gives 1/10000 favouring Z. Direction consistent (P(H|Z) ≫ P(H|LL)). The decisive question is whether an undercutting defeater breaks the step while granting the premises. The natural candidate — that under zoonosis the first *detected* cluster need not sit at the spillover site (ascertainment bias A-40; overdispersed superspreading A-41; centroid-≠-origin A-2) — challenges the circle model's premise that first-cluster-location tracks spillover-location; that is denial of a premise, and those competing models are minted as their own nodes and priced separately, not an undercutting defeater of this inference. Conditional on the circle model the arithmetic follows and no alternative breaks the reason→conclusion link without denying it. Per Rule 1, the model's realism and the magnitude (whether 1/600 vs 1/1.2e7 is right) are step-7/8 questions; the inferential step itself holds. Approved; ratio computation traced directly, hence checked.
