---
type: cluster-review
id: CR-1
cluster: "[[HC-1 - Dominant driver of the extinction pulse]]"
---

*Numbers quoted below are the model's own (from `runner/run.py`); rough magnitudes I introduce are marked as mine. This is a structural demo, so treat the values as illustrative.*

## What the analysis says

[[HC-1 - Dominant driver of the extinction pulse]] asks which single driver dominated the ~45-40 ka pulse, across four mutually-exclusive members: direct predation ([[H-3 - Direct predation by arriving humans drove the extinction]]), indirect human impact via burning ([[H-11 - Indirect human impact through burning and habitat transformation drove the extinction]]), climate aridification ([[H-21 - Climate-driven aridification drove the extinction]]), and a residual. The prior started `[0.22, 0.40, 0.28, 0.10]` — a human driver favoured but climate left a real share — and the posterior landed `[0.23, 0.58, 0.12, 0.07]`. Two evidence blocks did the updating: the correlated dating pair [[O-14 - Youngest reliable ages for 8 of 12 dated genera fall within ~2 kyr of first human occupation]] + [[O-22 - Three megafauna genera persist more than 5 kyr after first human arrival]], priced jointly because both rest on [[D-4 - Continental late-Quaternary age compilation, group R]], which pulls toward indirect human impact (only H-11 predicts both the tight arrival cluster *and* the >5 kyr survivor tail); and [[O-31 - The interior aridity maximum postdates the first-occupation window by several kyr]], which pushes climate down further. Climate is also where the prior did the most work: [[A-31 - No comparable extinction pulse at earlier glacial terminations]] cut its weight before any observation was read.

## What the model may not capture

The split between [[H-3 - Direct predation by arriving humans drove the extinction]] and [[H-11 - Indirect human impact through burning and habitat transformation drove the extinction]] rests on one prior factor, `p_direct_given_human`, with essentially no reference class behind it — yet the two posterior entries (0.23 vs 0.58) present it as if the evidence resolved the mechanism, which it barely does. Their asserted mutual exclusivity is the deeper doubt: if arriving humans hunted *and* burned, the true story is "partly both," which an exclusive member set cannot express — the pulse may have no single dominant driver at all. [[A-31 - No comparable extinction pulse at earlier glacial terminations]] was trusted without its inference traced, and absence-of-record is weak where the earlier terminations are far more poorly dated than the 45-40 ka window (my estimate: perhaps half the relevant earlier-termination sites were never dated to comparable precision) — this is the largest unchecked step in the cluster. Finally: could the driver be one nobody listed — a disease pulse, a trophic cascade? The residual holds 0.07, but nothing outside the human-vs-climate framing was actually weighed, and an unlisted driver need not be less consequential than the listed ones.

## What would help

1. The full screening protocol behind [[D-4 - Continental late-Quaternary age compilation, group R]], with the ages it excluded — *exists, inaccessible*. It is the single dataset almost everything here rests on.
2. A second dating compilation built independently of D-4, to break the shared-basis correlation — *does not exist* (as far as this source set shows).
3. A trace of [[A-31 - No comparable extinction pulse at earlier glacial terminations]]'s inference against a precisely-dated earlier-termination record — *exists, unread*.
4. Any evidence that could separate direct predation from indirect habitat impact — *unclear* whether such evidence is obtainable at all.

## Confusions and contradictions

[[O-14 - Youngest reliable ages for 8 of 12 dated genera fall within ~2 kyr of first human occupation]] reads as a rapid-arrival-clustering signal while [[O-22 - Three megafauna genera persist more than 5 kyr after first human arrival]] reads as a slow-habitat-squeeze signal — opposite-looking patterns that both rest on the same compilation [[D-4 - Continental late-Quaternary age compilation, group R]]. Pricing them jointly is correct (they are one witness, not two), but the single joint likelihood states P(both | H) and therefore *cannot show which half of the pattern each member fits* — the very thing that would sharpen the H-3/H-11 split. Shipped unfixed at submission, deliberately: the honest repair is the prose in [[E-14 - O-14 × HC-1 +A-7 — youngest ages cluster in the arrival window]]'s comment, not a second estimate that would double-count D-4.
