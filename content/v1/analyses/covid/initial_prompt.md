Run the full FLF EpiStack pipeline (flf-epistack step 0) on the case below. curated_target_N is passed at invocation; the analysis directory is this folder.

Main question (verbatim): "Did SARS-CoV-2 first infect humans through natural zoonotic spillover (e.g. via the wildlife trade / Huanan Seafood Market) or through a research-related incident (a lab leak)?"

Case framing — from the FLF EpiStack competition page, quoted verbatim as scope/intent (this is the judged case; it is NOT the main question). Competitor-facing sentences omitted where marked.

> In early 2024, a $100,000 judged debate took place between Saar Wilf (founder of Rootclaim) and Peter Miller on the origins of COVID-19. Over 15 hours of structured argument, two smart people marshalled epidemiological data, viral genetics, Bayesian inference, and institutional analysis to reach opposite conclusions. Two expert judges ruled decisively for zoonosis. Six independent Bayesian analyses of the same evidence spanned 23 orders of magnitude.
>
> [...] the debate videos, judge decisions, and comment threads [...] form one of the richest publicly available records of a complex real-world epistemic dispute on an important issue.
>
> And yet all this information is still incredibly difficult to navigate, interrogate, and use to inform one's beliefs.
> - It requires significant background expertise to understand the state of play of the debate and make a considered judgement.
> - The format, a live video debate, may not be the optimal way for a judge to interact with the material.
>
> Further, this intense epistemic effort represents a point in time in a conversation which continues to evolve.
> [competitor-facing framing — "Your job: craft the AI-assisted methodologies…" — omitted]

Starting material (seed sources for step 1; reach the primary artifacts behind these, not the summaries):
> - Scott Alexander's writeup of the COVID origins debate: https://www.astralcodexten.com/p/practically-a-book-review-rootclaim
> - Judge Will's decision: https://drive.google.com/file/d/1YhmkYB32RpGsXvQTsX4xZ0Yul1wiwh8Z/view | Judge Eric's decision: https://drive.google.com/file/d/1aHlhPd-16EOabzXhiajT5PBm3uVCAG3T/view
> - Michael Weissman's Bayesian analysis: https://michaelweissman.substack.com/p/an-inconvenient-probability-v57
> - Rootclaim's response: https://blog.rootclaim.com/covid-origins-debate-response-to-scott-alexander/
> - Debate videos: https://www.youtube.com/watch?v=Y1vaooTKHCM | https://www.youtube.com/watch?v=KdORmvU8MLI | https://www.youtube.com/watch?v=d1dbfoK8nSE

---

For step 10, give those instructions to the agent: Write the analysis in a way it is well-readable by humans without much context. Explain the key observations and arguments. Have a summary section at the top and feel free to go into more detail in the arguments below. The step 10 instructions aren't that great yet. When you mention the posteriors, make sure you state/link each hypothesis a number attaches to.
Similar stuff applies to a lesser extent to summary sections of step 9.

Apart from the default instructions, please make sure you use the following model and effort settings:
general default effort: xhigh
for step 6, use effort high but use 4x more subagents so subagents should usually only evaluate 5 arguments.
for cluster hypotheses (4b), use effort max.

use model opus for steps 3, 4a, 6, and 8.





