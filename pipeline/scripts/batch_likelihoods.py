"""Distribute step-8 likelihood work into subagent-sized units.

Step 8 prices one `evidence()` call per unit of correlated data:
  - a **correlation group** (`CG-N`, built by step 5's consolidator) is ONE unit
    -- its member edges share a data basis and must be judged jointly, in a
    single `## Likelihood` block written on the CG node;
  - every other edge is a **lone** edge, priced on its own note, and lone edges
    are handed out in small independent batches (default 3 per child).

So a step-8 child is briefed with EITHER one correlation group OR up to 3
independent edges -- exactly the two shapes this script emits. The orchestrator
runs it to get the assignment; it only reads and reports, never editing a file.

Step 7 marks every edge it folded into a cluster's prior with
`used_for_prior: true`. Those edges are already accounted for and must not be
priced again: each such lone edge is excluded from the emitted units, and a
correlation group is excluded as a whole if ANY member edge is used_for_prior
(its joint block would re-count what the prior absorbed). The exclusions --
plus each cluster's no-observation arguments (empty `affects_observations`,
`affects_hypotheses` resolving to a hypothesis in that cluster), which step 7
likewise consulted -- are printed under "ALREADY ACCOUNTED FOR IN THE PRIOR"
so no step-8 child double-counts them. The JSON units exclude them too.

Because step 5 already materialised each correlated cluster as a `CG` node,
the distribution is just: one unit per live CG, plus the leftover edges batched.
An edge is grouped iff it is a member of a live CG (folder `correlation-groups/`,
non-recursively -- orphaned CGs under `correlation-groups/orphan/` don't count,
and `build_correlation_groups.py` has already stripped their edges' `group`).

Usage:
    python3 batch_likelihoods.py <analysis-dir> [--batch-size 3]
"""

import argparse
import collections
import json
import pathlib
import re
import sys

# Head id of an Obsidian wikilink, e.g. [[E-14 - title]] -> E-14.
WIKILINK = re.compile(r"\[\[\s*([A-Za-z]+-\d+)")
KEY = re.compile(r"^([A-Za-z0-9_-]+)\s*:")


def split_note(text):
    """(frontmatter, body) or (None, text) when there is no frontmatter."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    return text[4:end], text[end + 1:]


def fm_segments(fm):
    """Ordered (key, raw_lines) segments, each field (incl. block lists) intact."""
    segments, key, lines = [], None, []
    for line in fm.split("\n"):
        m = KEY.match(line)
        if m and not line[:1].isspace():
            if lines or key is not None:
                segments.append((key, lines))
            key, lines = m.group(1), [line]
        else:
            lines.append(line)
    if lines or key is not None:
        segments.append((key, lines))
    return segments


def field_ids(text, key):
    """Ids linked in one frontmatter field (inline or block list); [] if absent."""
    fm, _ = split_note(text)
    if fm is None:
        return []
    for k, raw in fm_segments(fm):
        if k == key:
            return WIKILINK.findall("\n".join(raw))
    return []


def scalar_of(text, key):
    """The raw scalar value of one frontmatter field, or None if absent."""
    fm, _ = split_note(text)
    if fm is None:
        return None
    for k, raw in fm_segments(fm):
        if k == key:
            return raw[0].split(":", 1)[1].strip().strip("\"'")
    return None


def type_of(text):
    return scalar_of(text, "type")


def used_for_prior(text):
    return (scalar_of(text, "used_for_prior") or "").lower() == "true"


def id_of(path):
    m = re.match(r"^([A-Za-z]+-\d+) - ", path.name)
    return m.group(1) if m else None


def num_key(node_id):
    prefix, num = node_id.rsplit("-", 1)
    return (prefix, int(num))


def batched(items, size):
    return [items[i:i + size] for i in range(0, len(items), size)]


def resolve_cluster(h_id, index, root):
    """Cluster (HC id) of a hypothesis, following `merged_into` one hop to the
    live survivor; None if the live hypothesis is dropped or unresolvable."""
    p = index.get(h_id)
    if p is None:
        return None
    text = p.read_text(encoding="utf-8")
    merged = field_ids(text, "merged_into")
    if merged:
        p = index.get(merged[0])
        if p is None:
            return None
        text = p.read_text(encoding="utf-8")
    if "dropped" in p.relative_to(root).parts:
        return None
    cluster = field_ids(text, "cluster")
    return cluster[0] if cluster else None


def collect(root, batch_size):
    edges_dir = root / "evidence-links"
    cg_dir = root / "correlation-groups"
    if not edges_dir.is_dir():
        sys.exit("no evidence-links/ folder under %s -- run step 5 first" % root)

    # 1. Read the edges once: id -> (to-cluster, relative path, used_for_prior).
    edge_info = {}
    for p in sorted(edges_dir.glob("*.md")):  # non-recursive: no edge sub-folders
        eid = id_of(p)
        if eid is None:
            continue
        text = p.read_text(encoding="utf-8")
        to = field_ids(text, "to")
        edge_info[eid] = (to[0] if to else None, str(p.relative_to(root)),
                          used_for_prior(text))

    # accounted[hc] -> what step 7 already folded into that cluster's prior.
    accounted = collections.defaultdict(
        lambda: {"edges": [], "args": [], "cg_notes": []})
    for eid, (hc, _, prior) in edge_info.items():
        if prior:
            accounted[hc]["edges"].append(eid)

    # 2. Live correlation groups: one unit each -- unless ANY member edge is
    #    used_for_prior, in which case the whole joint unit is excluded (its
    #    members stay out of the lone batches too: they are correlated with
    #    data the prior already absorbed).
    cg_units, grouped = [], set()
    if cg_dir.is_dir():
        for p in sorted(cg_dir.glob("*.md")):
            text = p.read_text(encoding="utf-8")
            if type_of(text) != "correlation-group":
                continue
            members = field_ids(text, "members")
            to = field_ids(text, "to")
            hc = to[0] if to else None
            grouped.update(members)
            prior_members = sorted(
                (m for m in members if edge_info.get(m, (None, None, False))[2]),
                key=num_key)
            if prior_members:
                rest = sorted(set(members) - set(prior_members), key=num_key)
                accounted[hc]["cg_notes"].append(
                    "%s unit dropped (%s used_for_prior)%s"
                    % (id_of(p), ", ".join(prior_members),
                       "; correlated members also not emitted: %s" % ", ".join(rest)
                       if rest else ""))
                continue
            cg_units.append({
                "kind": "correlation-group",
                "unit": id_of(p),
                "cluster": hc,
                "assess": sorted(members, key=num_key),
                "block_on": [str(p.relative_to(root))],
            })
    cg_units.sort(key=lambda u: num_key(u["unit"]))

    # 3. Lone edges: every edge not in a live CG and not used for the prior.
    lone = [(eid, hc, rel) for eid, (hc, rel, prior) in edge_info.items()
            if eid not in grouped and not prior]
    lone.sort(key=lambda e: num_key(e[0]))

    indep_units = []
    for i, batch in enumerate(batched(lone, batch_size), 1):
        indep_units.append({
            "kind": "independent",
            "unit": "batch-%d" % i,
            "assess": [e[0] for e in batch],
            "clusters": [e[1] for e in batch],
            "block_on": [e[2] for e in batch],
        })

    # 4. Per cluster, the no-observation arguments step 7 consulted for the
    #    prior: empty `affects_observations`, `affects_hypotheses` resolving
    #    (via merged_into, skipping dropped) to a hypothesis in that cluster.
    index = {}
    for p in root.rglob("*.md"):
        nid = id_of(p)
        if nid and nid not in index:
            index[nid] = p
    args_dir = root / "arguments"
    if args_dir.is_dir():
        for p in sorted(args_dir.glob("*.md")):  # non-recursive: skips orphan/, dropped/
            text = p.read_text(encoding="utf-8")
            if type_of(text) != "argument" or field_ids(text, "affects_observations"):
                continue
            hcs = {resolve_cluster(h, index, root)
                   for h in field_ids(text, "affects_hypotheses")}
            for hc in hcs:
                if hc:
                    accounted[hc]["args"].append(id_of(p) or p.stem)

    return cg_units, indep_units, accounted


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("analysis_dir", type=pathlib.Path)
    ap.add_argument("--batch-size", type=int, default=3,
                    help="lone edges per independent child (default 3)")
    args = ap.parse_args()

    if not args.analysis_dir.is_dir():
        sys.exit("no such analysis directory: %s" % args.analysis_dir)

    cg_units, indep_units, accounted = collect(args.analysis_dir, args.batch_size)
    n_lone = sum(len(u["assess"]) for u in indep_units)
    n_prior_edges = sum(len(v["edges"]) for v in accounted.values())
    n_cg_dropped = sum(len(v["cg_notes"]) for v in accounted.values())

    print("step 8 work distribution: %d correlation-group unit(s) + %d lone edge(s) "
          "-> %d independent batch(es) of <=%d = %d subagent(s) total"
          % (len(cg_units), n_lone, len(indep_units), args.batch_size,
             len(cg_units) + len(indep_units)))
    if n_prior_edges or n_cg_dropped:
        print("(excluded as accounted for in the prior: %d used_for_prior edge(s), "
              "%d correlation-group unit(s))" % (n_prior_edges, n_cg_dropped))
    print()

    if cg_units:
        print("Correlation-group units (assess jointly; ONE ## Likelihood block on the CG node):")
        for u in cg_units:
            print("  %s (%s): %s" % (u["unit"], u["cluster"] or "?", ", ".join(u["assess"])))
        print()
    if indep_units:
        print("Independent units (assess separately; one ## Likelihood block per edge):")
        for u in indep_units:
            pairs = ", ".join("%s (%s)" % (e, c or "?")
                              for e, c in zip(u["assess"], u["clusters"]))
            print("  %s (%d): %s" % (u["unit"], len(u["assess"]), pairs))
        print()

    if any(v["edges"] or v["args"] or v["cg_notes"] for v in accounted.values()):
        print("ALREADY ACCOUNTED FOR IN THE PRIOR — do not double-count:")
        for hc in sorted(accounted, key=lambda h: num_key(h) if h else ("", 0)):
            v = accounted[hc]
            if not (v["edges"] or v["args"] or v["cg_notes"]):
                continue
            print("  %s:" % (hc or "?"))
            if v["edges"]:
                print("    used_for_prior edges: %s"
                      % ", ".join(sorted(v["edges"], key=num_key)))
            for note in v["cg_notes"]:
                print("    %s" % note)
            if v["args"]:
                print("    no-observation arguments: %s"
                      % ", ".join(sorted(set(v["args"]), key=num_key)))
        print()

    print("JSON:")
    print(json.dumps(cg_units + indep_units))


if __name__ == "__main__":
    main()
