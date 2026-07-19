---
title: Running the model
---

> [!note] Draft.

The Bayesian layer of an analysis is not stored as cached numbers — it is **computed on demand** from small python blocks embedded in the notes. This keeps every value auditable and overridable.

## The two block kinds

1. A **`## Prior`** block lives on each `hypothesis-cluster` (`HC-N`). It builds a relative weight per member — a Fermi decomposition of named variables — and ends in one `prior(hc, w)` call.
2. A **`## Likelihood`** block lives on each `evidence-link` (`E-N`). It states P(observation | member) for each member and ends in one `evidence(hc, obs, lik, t)` call, where `t` is how far the data's reliability lets the evidence move you off the prior.

The runner (`pipeline/runner/run.py`) reads every note, extracts these blocks, and composes each cluster's posterior:

```
python3 pipeline/runner/run.py content/v1/analyses/sample-sahul-megafauna
# HC-1  prior [0.2172, 0.4034, 0.2793, 0.1001]  posterior [0.2303, 0.5812, 0.115, 0.0735]  (2 evidence block(s))
```

## Pricing an assumption

Any named variable can be overridden and the model re-run, so a skeptic can price exactly what a number is worth:

```
python3 pipeline/runner/run.py content/v1/analyses/sample-sahul-megafauna --set E-14:t_dates=1.0
# fully trusting the one age compilation lifts the human branch to ~0.89
```

Determinism is enforced: blocks are arithmetic over named variables only — no imports, randomness, clock, or I/O — so the same notes always give the same numbers.
