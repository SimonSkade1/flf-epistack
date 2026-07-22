---
id: A-19
type: argument
statement: Conditioning on the existence of present observers biases historically inferred catastrophe frequencies downward - Bayes' formula gives posterior P(catastrophe occurred | we exist) = PQ/(1 - P + PQ) for prior probability P and survival probability Q, so the overconfidence factor eta = (1 - P + PQ)/Q grows beyond 1 as events become more destructive and diverges as Q -> 0; frequency estimates for near-certainly-fatal event classes can understate the true rate by orders of magnitude.
source: "[[S-79 - Ćirković, Sandberg & Bostrom 2010, Anthropic Shadow- Observation Selection Effects and Human Extinction Risks]]"
locator: "§2 (eqs. 1-6, Fig. 2); §3 (eqs. 7-10); §4 (Figs. 6-8)"
quote: "lim Q→0 η = ∞"
affects_observations: ["[[O-17 - Human observers exist today, so every historical record is conditioned on no observer-extinguishing catastrophe having occurred]]"]
---
## Reasoning

1. Single-event toy model: let B2 = "the catastrophe occurred in the past interval" with prior P, and let Q = P(humanity survives | catastrophe). The evidence is E = our present existence, with P(E|B2) = Q and P(E|not-B2) = 1. Bayes: P(B2|E) = PQ / ((1-P) + PQ).
2. Overconfidence parameter eta := P(a priori)/P(a posteriori) = (1 - P + PQ)/Q. For Q = 1 (harmless events) eta = 1: the record is unbiased. As Q falls, eta rises; eta -> infinity as Q -> 0. Worked example: Q = 0.1, P = 0.5 (a Toba-scale event at ~1/Myr over human evolution) gives eta = 5.5 - the true probability is 5.5x the naive past-frequency estimate.
3. Generalization (§3): for N possible disasters with per-slot probability alpha and lethality beta, P(k observed disasters and observers | alpha, beta) = C(N,k) alpha^k (1-alpha)^(N-k) (1-beta)^k; with uniform priors, P(alpha, beta | O, k) is depressed at high beta - the surviving observer's record systematically under-samples severe events ("anthropic shadow", the biased-sampling region above the anthropic compatibility boundary in the time-severity plane).
4. The bias is cumulative with classical selection effects (erosion of traces etc.) and must be corrected after them when constructing the a-priori distribution used for prediction; the terrestrial cratering record (Earth Impact Database: no >100-km craters in the recent past except Chicxulub) illustrates the censored region.
5. Scope: the bias afflicts hazards that (1) could have destroyed our species or its predecessors, (2) are uncertain, and (3) whose frequency estimates rest largely on terrestrial records.
