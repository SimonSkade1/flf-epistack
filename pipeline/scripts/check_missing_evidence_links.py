"""Flag (observation, argument) pairs that imply a missing evidence link.

End-of-step-5 check: an argument that names an observation O in
`affects_observations` AND a hypothesis in cluster HC in `affects_hypotheses`
implies O bears on HC -- so an evidence-link `from: O, to: HC` should exist.
This script lists every such pair with no matching live edge yet. Hypothesis
ids resolve by following `merged_into` one hop to the live survivor (ids whose
live hypothesis is dropped are skipped) and reading its `cluster`.

Read-only: it reports; the agent decides whether each missing link should be
minted. Only arguments directly under `arguments/` are scanned (`orphan/` and
`dropped/` are skipped), and only edges directly under `evidence-links/` count
as existing.

Usage:
    python3 check_missing_evidence_links.py <analysis-dir> --cluster HC-3
    python3 check_missing_evidence_links.py <analysis-dir> --cluster all
"""

import argparse
import pathlib
import re
import sys

# Head id of an Obsidian wikilink, e.g. [[O-14 - title]] -> O-14.
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


def id_of(path):
    m = re.match(r"^([A-Za-z]+-\d+) - ", path.name)
    return m.group(1) if m else None


def num_key(node_id):
    prefix, num = node_id.rsplit("-", 1)
    return (prefix, int(num))


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


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("analysis_dir", type=pathlib.Path)
    ap.add_argument("--cluster", required=True,
                    help='cluster id (e.g. HC-3), or "all"')
    args = ap.parse_args()

    root = args.analysis_dir
    if not root.is_dir():
        sys.exit("no such analysis directory: %s" % root)

    # Index every node by id, so hypothesis ids resolve wherever the file sits.
    index = {}
    for p in root.rglob("*.md"):
        nid = id_of(p)
        if nid and nid not in index:
            index[nid] = p

    # Existing live edges as (from observation, to cluster) pairs.
    existing = set()
    edges_dir = root / "evidence-links"
    if edges_dir.is_dir():
        for p in sorted(edges_dir.glob("*.md")):  # non-recursive: live edges only
            text = p.read_text(encoding="utf-8")
            frm, to = field_ids(text, "from"), field_ids(text, "to")
            if frm and to:
                existing.add((frm[0], to[0]))

    # missing[hc][obs] -> argument ids implying the obs -> hc link.
    missing = {}
    args_dir = root / "arguments"
    if args_dir.is_dir():
        for p in sorted(args_dir.glob("*.md")):  # non-recursive: skips orphan/, dropped/
            text = p.read_text(encoding="utf-8")
            if scalar_of(text, "type") != "argument":
                continue
            obs = field_ids(text, "affects_observations")
            if not obs:
                continue
            hcs = {resolve_cluster(h, index, root)
                   for h in field_ids(text, "affects_hypotheses")}
            for hc in hcs:
                if not hc or (args.cluster != "all" and hc != args.cluster):
                    continue
                for o in obs:
                    if (o, hc) not in existing:
                        missing.setdefault(hc, {}).setdefault(o, []).append(
                            id_of(p) or p.stem)

    if not missing:
        print("no missing evidence links implied by arguments%s"
              % ("" if args.cluster == "all" else " for %s" % args.cluster))
        return
    total = sum(len(v) for v in missing.values())
    print("%d missing evidence link(s) implied by arguments "
          "(mint the link or fix the argument's attachments):" % total)
    for hc in sorted(missing, key=num_key):
        for o in sorted(missing[hc], key=num_key):
            print("  %s -> %s  (implied by %s)"
                  % (o, hc, ", ".join(sorted(set(missing[hc][o]), key=num_key))))


if __name__ == "__main__":
    main()
