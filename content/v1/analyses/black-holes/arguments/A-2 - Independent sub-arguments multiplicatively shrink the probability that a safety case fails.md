---
id: A-2
type: argument
statement: "The residual 'grey area' left by possible argument failure can never be removed entirely, but if a safety case contains multiple independent arguments A1, A2, ... then P(¬A1 ∧ ¬A2) < P(¬A1): total failure requires every layer to fail, so layered cases like Giddings-Mangano 2008 (rapid decay robust across theories; stable holes could not shed charge, making the cosmic-ray bound apply; astrophysical accretion limits) are substantially more reliable than any single argument."
source: "[[S-44 - Ord, Hillerbrand and Sandberg, Probing the Improbable]]"
locator: "§2 (objection ¶ on P(¬A1,¬A2) < P(¬A1)) and §4.2 (analysis of Giddings-Mangano's A1, A2, A3)"
affects_hypotheses: ["[[H-11 - The actionable LHC catastrophe probability is dominated by the chance the safety argument itself is flawed]]"]
status: approved
reason_if_not_false: checked
---
Reasoning:

1. For genuinely independent arguments, the joint failure probability is the product of individual failure probabilities (or at least strictly smaller than any single one): P(¬A1, ¬A2) < P(¬A1). Each added independent argument shrinks the grey area of eq. (1); a small residual grey area is acceptable when P(X|¬A)P(¬A) is small relative to the stakes.
2. The paper reads Giddings-Mangano 2008 as exactly this structure, three sequential layers each covering the failure of the previous: (A1) rapid black-hole decay is a robust consequence of several distinct physical frameworks; (A2) even absent decay, a stable hole could not shed its charge, so cosmic-ray-produced stable holes would also stop in matter, making Earth's and other bodies' survival evidentially relevant; (A3) even for stable neutral holes, if multidimensional gravity's scale is below ~20 nm Earth-accretion takes longer than the planet's natural lifetime, while fast-accretion scenarios would destroy white dwarfs and neutron stars on timescales contradicting their observed lifetimes and cooling.
3. Hence the total case (A1,A2,A3) is significantly stronger than any component - this argument cuts against treating a single-argument failure rate as the failure rate of the whole safety case, i.e. it moderates (without eliminating) the argument-fragility concern: what remains required is that the layers be genuinely independent and that each layer's own modelling be sound.
4. Corollary the paper endorses: independent replication of calculations, independent derivations of the same bound, and adversarial red-teaming can reduce the effective P(¬A) by orders of magnitude.

## Validity verdict (step 6)

Reconstruction: premise = the sub-arguments are genuinely independent; conclusion = joint failure probability strictly below any single one. Elementary: P(notA1 and notA2) = P(notA1)P(notA2) < P(notA1) whenever P(notA2) < 1. Undercutting probe: correlated failures via shared modelling assumptions would break the product rule - but independence is an explicit premise here, and the body itself flags "layers be genuinely independent" as the required condition; whether GM's layers actually are independent is premise-truth, priced in steps 7-8. Inference holds as stated.
