Run the full FLF EpiStack pipeline (flf-epistack step 0) on the case below. curated_target_N is passed at invocation; the analysis directory is this folder.

Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"

Case framing — from the FLF EpiStack competition page, quoted verbatim as scope/intent (NOT the main question). This is the entire brief FLF gives; there is no starting-material list.

> Are eggs good to eat? Bad to eat? Great in moderation? How can we tell? Does it vary across people, and what predicts this? What else should we be paying attention to here?
> This vague and open-ended topic, though mundane, is representative of a huge number of everyday questions — and hopefully also a microcosm of many more impactful debates. Sometimes getting resolution on what are the important things to answer and what are the appropriate ways of knowing is (more than) half of the challenge.

---

For step 10, give those instructions to the agent: Write the analysis in a way it is well-readable by humans without much context. Explain the key observations and arguments. Have a summary section at the top and feel free to go into more detail in the arguments below. The step 10 instructions aren't that great yet. When you mention the posteriors, make sure you state/link each hypothesis a number attaches to.
Write the top summary of step 10 at the end. Otherwise start by mentioning each HC in a (potentially large) paragraph where you mention the top hypotheses and their probabilities and the key reason why they are the way they are. Consider that readers are not experts in the field and that you may need to explain background.
Then tie together how the overall question can be combined from the HCs and where cross-dependencies between HCs are and evaluate.
Similar stuff applies to a lesser extent to summary sections of step 9.

Apart from the default instructions, please make sure you use the following model and effort settings:
general default effort: xhigh
for step 6, use effort high but use 4x more subagents so subagents should usually only evaluate 5 arguments.
for cluster hypotheses (4b), use effort max.

use model opus for steps 3, 4a, 6, and 8.

oh yeah btw, for 2b, don't lower the trust threshold significantly.

