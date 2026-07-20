---
type: argument
id: A-6
status: corrected
reason_if_not_false: checked
statement: "That a body whose survival is a precondition for our existence (Earth, Sun) has survived past exposure cannot by itself bound the true catastrophe rate, because observers necessarily find themselves where catastrophe has not yet occurred; for independently observed distant bodies (white dwarfs, neutron stars) the selection bias is only partial and their survival retains most of its evidential force."
source: "[[S-23 - Is a doomsday catastrophe likely - the observer-selection bound (Tegmark and Bostrom 2005)]]"
locator: "Nature 438 (2005) 754, opening argument; arXiv §1"
affects_hypotheses:
  - "[[H-5 - The exogenous terminal-catastrophe rate is below about 1 per Gyr at 99.9 percent confidence]]"
---

**reasoning** - Condition on the existence of the observer: every observer able to ask "has a terminal catastrophe happened here?" is guaranteed to find the answer "no", whatever the true rate. So P(observed survival | high rate) = P(observed survival | low rate) = 1 once observer existence is conditioned on; the likelihood ratio is ~1 and the survival record is (to first order) uninformative about the rate. Hence any survival-based reassurance — explicitly including the cosmic-ray-survival premise ([[D-1 - Cosmic-ray survival premise - high-energy cosmic rays have bombarded astronomical bodies over Gyr without catastrophe]]) underlying collider-safety arguments — is valid only after an anthropic correction, e.g. by using data whose distribution is not conditioned on our own survival (as the formation-time bound does). Scope note: the schema only allows attachment to same-paper nodes; this argument's principal external force is against evidence links resting on D-1 (survival of Earth/Sun specifically; survival of independently observed bodies like neutron stars is only partially shielded from the bias), which steps 5-6 should price using this reasoning.

## Original
"That Earth (or any observed body) has survived past exposure cannot by itself bound the true catastrophe rate, because observers necessarily find themselves only where catastrophe has not yet occurred."

## Verdict (step 6)
corrected / checked. The core step is valid and traced: conditioning on observer existence forces P(observed survival | high rate) = P(observed survival | low rate) = 1 for any body whose destruction would have precluded the observation (Earth, Sun), so the likelihood ratio is ~1 and such survival is uninformative. But the parenthetical "(or any observed body)" overreaches: for causally quasi-independent distant bodies (WD/NS), our existence does not require their survival, so P(observing intact specimens | high rate) genuinely falls with the rate and the likelihood ratio departs from 1 — only a partial bias remains (selection of observable/catalogued objects). The body's own scope note already concedes this. Statement narrowed to the version immune to that defeater; filename left as-is.
