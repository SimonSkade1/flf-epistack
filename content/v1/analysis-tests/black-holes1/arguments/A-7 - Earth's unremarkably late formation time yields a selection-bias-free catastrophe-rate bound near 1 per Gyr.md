---
type: argument
id: A-7
status: approved
reason_if_not_false: checked
statement: "If the exogenous catastrophe rate were high, surviving observers would overwhelmingly find themselves on anomalously early-formed planets; Earth's typical formation date therefore bounds the rate at ~1/Gyr (99.9% c.l.)."
source: "[[S-23 - Is a doomsday catastrophe likely - the observer-selection bound (Tegmark and Bostrom 2005)]]"
locator: "Nature 438 (2005) 754; arXiv derivation sections"
affects_observations:
  - "[[O-10 - Habitable-planet formation times span many Gyr and Earth's formation date is unremarkably late]]"
affects_hypotheses:
  - "[[H-5 - The exogenous terminal-catastrophe rate is below about 1 per Gyr at 99.9 percent confidence]]"
---

**reasoning** - Under a spatially uncorrelated exogenous catastrophe process at rate 1/tau, the chance a planet formed at cosmic time t still hosts observers at time t+dt decays exponentially in elapsed time, so the observer-weighted formation-time distribution is the raw formation-time distribution exponentially tilted toward late formation dates (late formers have had less time at risk). If tau were short, essentially all observers would find their planet formed far later, relative to the formation-time distribution, than Earth's ~9.1 Gyr date — i.e. our unremarkable, near-typical date would be a huge coincidence. Computing P(formation date as typical as ours | tau) against the distribution gives tau > ~1.1 Gyr at 99.9% confidence. The inference is selection-bias-free because it compares among surviving observers rather than counting survival itself as evidence. Assumptions it hinges on: the adopted planet-formation-time distribution (model-dependent), spatial/temporal uncorrelatedness of the catastrophe process, and exogeneity (rates humans modulate are outside the bound).

## Verdict (step 6)
approved / checked. Traced the load-bearing step: for an exogenous, spatially/temporally uncorrelated catastrophe process at rate 1/tau, survival to observer-time decays as exp(-(t_obs - t_form)/tau), so the observer-weighted formation-time distribution is the raw one exponentially tilted toward late t_form; small tau pushes essentially all observers onto anomalously late-formed planets, so a near-typical formation date like Earth's ~9.1 Gyr becomes very improbable — a clean typicality test yielding tau >~ 1 Gyr at the stated confidence. Crucially the comparison is among surviving observers, so the anthropic defeater that kills naive survival bounds (A-6) does not apply. The statement already names its real hinges (formation-time distribution model, uncorrelatedness, exogeneity); their truth is priced at steps 7-8, not here.
