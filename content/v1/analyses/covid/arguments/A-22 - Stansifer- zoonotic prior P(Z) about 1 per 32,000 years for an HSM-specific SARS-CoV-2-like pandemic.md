---
id: A-22
type: argument
statement: "Stansifer estimates the zoonotic prior — the annual rate at which a SARS-CoV-2-like pandemic emerges specifically at the Huanan market — as P(Z) about 1/32000, from 1/20 (novel sars-like coronavirus emergence per year) x 1/4 (fraction pandemic-capable) x 1/2 (SARS-CoV-2 uniquely transmissible) x 1/200 (chance the spillover is at HSM given an east-Asian market)."
source: "[[S-70 - Judge Eric Stansifer's written decision]]"
locator: "§7.1 Zoonotic prior"
affects_observations: []
affects_hypotheses: ["[[H-41 - Natural zoonotic spillover with no research involvement]]"]
status: approved
reason_if_not_false: checked
---
## reasoning
Stansifer builds P(Z) from first principles as an annualized rate. (1) Novel sars-like coronavirus emergence: SARS-1 (2002) and MERS (2012) are the only suitable precedents; counting "gaps" over the last ~40 years (allowing that pandemic risk has risen with land-use/agriculture/population change) gives ~1 per 20 years. Multiple spillovers of the same virus (SARS-1 several, MERS dozens-hundreds) count once each, since the limiting factor is evolution of a suitable virus, not the spillover event itself. (2) Not all sars-like viruses cause pandemics: from SARS-1 and MERS he estimates (0+1)/(2+2)=1/4. (3) SARS-CoV-2 seems uniquely terrible (very high presymptomatic transmission), so a less severe virus might not have produced a pandemic: an extra 1/2. (4) Location: given emergence at an east-Asian wildlife market, the chance it is HSM specifically is assessed at 1/200 (Peter gave 1/50, Saar 1/500; HSM is the largest market of its kind in central China with atypically high live-wildlife presence, and Eddie Holmes/Wuhan CDC had pre-identified HSM as a spillover risk). Product: (1/20)(1/4)(1/2)(1/200) = 1/32000, i.e. HSM should produce a SARS-CoV-2-like pandemic roughly once every 32,000 years. Flu dynamics are judged too different to inform this prior.

## Validity assessment
Reconstruction. The load-bearing step is a chain-rule decomposition of an annualized rate into a product of conditional factors: P(Z) = [rate of novel sars-like emergence/yr] × [P(pandemic-capable | emergence)] × [P(SARS-CoV-2-grade transmissibility | pandemic-capable)] × [P(at HSM | such a market spillover)]. Conclusion: the product is the annualized rate of an HSM-specific SARS-CoV-2-like pandemic.

Evaluation (checked). Arithmetic verified: (1/20)(1/4)(1/2)(1/200) = 1/32000. Structural check of the decomposition: the four factors form a coherent nested conditional chain — factor 4 conditions on emergence at an east-Asian wildlife market, which the SARS-1/MERS precedent underpinning factors 1-2 supplies charitably (sars-like pandemic emergence is modelled as occurring at such markets), so there is no dangling condition. Probed for an undercutting defeater to the multiplication itself: the only way the product fails is if the factors are not properly nested conditionals (double-counting or a missing condition); under the charitable chain reading they are, so no defeater survives. Note per Rule 1: whether each magnitude (1/20, 1/4, 1/2, 1/200) is well-calibrated is a step-7 prior question, not a validity question — the inferential step is that these conditionals multiply to the joint rate, which holds. Approved; the decomposition and arithmetic are elementary and traced directly, hence checked.
