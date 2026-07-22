---
id: A-1
type: argument
statement: "Any risk report's stated probability is P(X|A), the probability of catastrophe given its argument is sound; by the law of total probability P(X) = P(X|A)P(A) + P(X|¬A)P(¬A), so whenever the stated P(X|A) is far smaller than P(X|¬A)P(¬A), the actionable probability is set by the chance the argument is flawed - and a claim of strict impossibility (P(X|A)=0) is fully consistent with P(X) > 0."
source: "[[S-44 - Ord, Hillerbrand and Sandberg, Probing the Improbable]]"
locator: "§2, eqs. (1)-(3) and Figure 1; §3 eqs. (2)-(3)"
affects_observations: ["[[O-12 - Measured error rates in published scientific arguments and calculations are of order 1e-3 or higher]]"]
affects_hypotheses: ["[[H-11 - The actionable LHC catastrophe probability is dominated by the chance the safety argument itself is flawed]]"]
status: approved
reason_if_not_false: checked
---
Reasoning:

1. Let X = the catastrophe occurs, A = the report's argument is sound. A report can at best deliver P(X|A): no argument can internally account for the possibility that it is itself flawed (that would need a further, higher-level argument; at most it can hedge specific sub-arguments).
2. Law of total probability: P(X) = P(X|A)P(A) + P(X|¬A)P(¬A). Worked example: stated P(X|A) = 1e-9 with P(¬A) = 1e-3 and P(X|¬A) = 1e-3 gives P(X) ≈ 1e-6 - a thousandfold increase over the stated figure. If the catastrophe were to occur, it would far more likely be because the argument was flawed than because a 1-in-a-billion event happened.
3. Asymmetry: the correction matters specifically for very small stated P(X|A) - practically any P(X|¬A) is then larger, so added argument-uncertainty pushes the estimate upward (for moderate P(X|A), e.g. 10%, the same term shifts 10% to ~10.001% and is negligible). The situation is mirror-symmetric for claims of near-certainty.
4. Refinement: A can be decomposed into T (theories adequate), M (model adequate given theories), C (calculations correct), with P(T,M,C) = P(T)P(M|T)P(C) since calculational correctness is independent of the adequacy of what is being calculated. Each component has a historically nonzero failure rate, and T and M failures are not independent of each other in general.
5. The decomposition is pure probability theory; the empirical content (how large P(¬A) actually is) enters through track-record data such as retraction rates - hence this argument turns on the measured error-rate observation.

## Validity verdict (step 6)

Reconstruction: premise = a report can internally state only P(X|A); law of total probability; conclusion is explicitly conditional ("whenever stated P(X|A) is far smaller than P(X|N(not-A))P(not-A)"). Load-bearing step is pure probability algebra; traced it and the worked example (1e-9 + 1e-3*1e-3 ~ 1e-6). Undercutting probe: cases where P(X|not-A)P(not-A) is itself tiny do not undercut the claim, because the conclusion is stated as a conditional. The independence assumption in the T/M/C decomposition is a premise, priced downstream, not part of the validity call.
