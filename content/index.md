---
title: EpiStack
---

**EpiStack** takes one contested empirical question and turns the debate about it into a Bayesian, navigable knowledge graph: every source, observation, hypothesis and inferential step is its own note with typed frontmatter, and the numbers that connect them are runnable code rather than prose. The output is a wiki you can read top-down (one report that answers the question) or bottom-up (follow any number to the datum it came from).

Two pieces, and they are versioned separately:

1. **The shell — general, reusable, lives at this root.** An Obsidian-style reading surface (wikilinks, transclusions, backlinks, interactive graph, full-text search) plus the [runnable pipeline](https://github.com/SimonSkade1/flf-epistack) that produces the notes. Neither is tied to any particular question.
2. **The content — one iteration per question set, versioned under `/vN/`.** An iteration is a run of the pipeline plus the docs describing that run's conventions. Its URLs are frozen, so a link into it keeps pointing at what it pointed at.

## Iterations

1. **[[v1/index|v1 — Future of Life Foundation epistemics competition]]** (current) — the analyses and docs built for the [FLF](https://futureoflife.org/) epistemics competition entry.

Later iterations that change the method or the question set will appear as `/v2/`, `/v3/`, … alongside v1, not in place of it.

## Elsewhere

1. [github.com/SimonSkade1/flf-epistack](https://github.com/SimonSkade1/flf-epistack) — site, content, and the pipeline (`pipeline/`: the 10 step specs and a runner that recomputes every posterior on the site).
2. [The competition prompt](https://www.lesswrong.com/posts/frizRHnA6AZpJSDqw/lab-leaks-black-holes-and-eggs-epistemic-case-study) that v1 answers.
