---
id: A-1
type: argument
status: approved
reason_if_not_false: checked
statement: "Worobey et al.'s Monte Carlo test can only reject the null that cases are scattered like the population; because a contagious disease clusters, that null is rejected for essentially any central Wuhan landmark, so a small p-value carries no information that the market specifically was the origin."
source: "[[S-23 - Stoyan & Chiu 2024 JRSS-A — statistical critique of the market-epicenter geospatial claim]]"
locator: "Sections 3-4"
affects_observations: ["[[O-1 - Recomputed Monte Carlo p-values for the market as case center are marginal and weaken toward non-significance as the case sample shrinks]]", "[[O-2 - Bootstrap places the market at the edge of the case-centroid cloud with Wanda Plaza an equally admissible center]]"]
---
Worobey's test compares the observed cases' median distance-to-market against 1,000 inhomogeneous-Poisson patterns whose intensity is proportional to residential population density — a null in which case locations are scattered like the resident population, with no person-to-person contagion. A contagious respiratory disease necessarily produces spatial clustering tighter than that population-proportional scatter. Hence the observed cases will look "too concentrated" relative to this null around essentially any central reference point, not uniquely around the market. Stoyan & Chiu make this explicit: substituting another landmark (e.g. Wanda Plaza) for the market in the same test reproduces the rejection. The alternative hypothesis actually being tested ("cases are not distributed proportionally to population density") is therefore mismatched to the conclusion drawn ("the market is the origin"): rejecting the former licenses only the statement that transmission clusters cases, not any statement locating the source. A low p-value is thus uninformative about origin.

## Validity verdict

status: approved; reason_if_not_false: checked.

Reconstructed step: the test's alternative hypothesis is "cases are not distributed proportionally to residential population density"; a contagious respiratory disease clusters tighter than population scatter, so this null is rejected around any sufficiently central reference point, not uniquely the market → therefore rejecting it does not discriminate the market from other central landmarks as the source. Traced myself: locating a point source requires a test that discriminates the candidate location against alternative central points; a null of "no contagion / population-proportional scatter" cannot do this because its rejection is entailed by contagion alone, wherever the source. The empirical claim that substituting Wanda Plaza reproduces the rejection is here a premise (its truth is priced at step 8); conditional on it, no undercutting defeater survives. The inference holds exactly as stated.
