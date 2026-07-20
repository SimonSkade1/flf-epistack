"""Wire step-3 arguments onto step-5 evidence-link edges by their backlinks.

An argument that bears on a specific observation records that observation in
its `affects_observations` field (step 3). Step 5's cluster-children mint the
observation -> cluster edges but never touch arguments. This consolidator script
closes the loop: for every `evidence-link` E, it appends to `E.arguments` every
argument whose `affects_observations` names E's `from` observation. So one
argument about one observation lands on that observation's edge into every
cluster automatically, and the cluster-child never had to see the argument.

An argument must still be attached to the live KB somewhere: it stays in
`arguments/` iff it has at least one `affects_hypotheses` entry OR at least one
of its `affects_observations` sits on a live edge. Otherwise nothing points at
it any more, and this script moves it to `arguments/orphan/` (keeping its
`source`), mirroring how the observation orphan-move works.

The script is derive-and-overwrite, so it is idempotent: each edge's
`arguments` list is recomputed from the backlinks every run, and an argument is
moved to (or back out of) `arguments/orphan/` to match the stay-rule above.
Run it once, after every step-5 cluster-child has returned and before
`link_state` is set.

Usage:
    python3 attach_argument_backlinks.py <analysis-dir>
"""

import argparse
import pathlib
import re
import sys

# Captures the id at the head of an Obsidian wikilink, e.g. [[O-14 - title]] -> O-14.
WIKILINK = re.compile(r"\[\[\s*([A-Za-z]+-\d+)")
# A top-level frontmatter key line (not an indented block-list continuation).
KEY = re.compile(r"^([A-Za-z0-9_-]+)\s*:")


def split_note(text):
    """Return (frontmatter, body_with_delims) or (None, text) if there is no frontmatter.

    body_with_delims keeps the closing `---` line and everything after it, so
    reassembly is exactly `"---\n" + new_fm + "\n" + body_with_delims`.
    """
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    fm = text[4:end]  # between the opening "---\n" and the "\n---"
    body = text[end + 1 :]  # from the closing "---" line onward
    return fm, body


def fm_segments(fm):
    """Split frontmatter into ordered (key, raw_lines) segments.

    A segment is a top-level `key:` line plus any following indented / block-list
    lines. Leading lines before the first key (rare) get key=None. This keeps
    every field's original text intact so we can rewrite one field and leave the
    rest byte-for-byte.
    """
    segments = []
    key = None
    lines = []
    for line in fm.split("\n"):
        m = KEY.match(line)
        if m and not line[:1].isspace():
            if lines or key is not None:
                segments.append((key, lines))
            key = m.group(1)
            lines = [line]
        else:
            lines.append(line)
    if lines or key is not None:
        segments.append((key, lines))
    return segments


def field_ids(fm, key):
    """Ids linked in one frontmatter field, or None if the field is absent."""
    for k, raw in fm_segments(fm):
        if k == key:
            return WIKILINK.findall("\n".join(raw))
    return None


def id_sort_key(link):
    """Sort links by (prefix, number) so `arguments` lists come out stable."""
    m = WIKILINK.match(link)
    if not m:
        return ("", 0)
    prefix, num = m.group(1).rsplit("-", 1)
    return (prefix, int(num))


def set_arguments(text, arg_links):
    """Return `text` with its `arguments` field replaced by arg_links (or removed)."""
    fm, body = split_note(text)
    if fm is None:
        return text  # no frontmatter to edit
    kept = [(k, raw) for k, raw in fm_segments(fm) if k != "arguments"]
    out = []
    for _, raw in kept:
        out.extend(raw)
    while out and out[-1].strip() == "":
        out.pop()
    if arg_links:
        out.append("arguments:")
        for link in sorted(arg_links, key=id_sort_key):
            out.append('  - "%s"' % link)
    return "---\n" + "\n".join(out) + "\n" + body


def link_of(path):
    """The wikilink for a node file: `[[A-7 - title]]` from `A-7 - title.md`."""
    return "[[%s]]" % path.stem


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("analysis_dir")
    args = ap.parse_args()

    root = pathlib.Path(args.analysis_dir)
    if not root.is_dir():
        sys.exit("no such analysis directory: %s" % root)

    args_dir = root / "arguments"
    orphan_dir = args_dir / "orphan"
    edges_dir = root / "evidence-links"

    # 1. Index arguments (active + already-orphaned, so re-runs can move one back).
    #    args_by_obs[obs_id] -> wikilinks of the arguments naming that observation.
    args_by_obs = {}
    arg_files = []  # (path, affects_observations ids, affects_hypotheses ids)
    for sub in (args_dir, orphan_dir):
        if not sub.is_dir():
            continue
        for path in sorted(sub.glob("*.md")):
            text = path.read_text()
            affects_obs = field_ids(text, "affects_observations") or []
            affects_hyp = field_ids(text, "affects_hypotheses") or []
            arg_files.append((path, affects_obs, affects_hyp))
            for obs_id in affects_obs:
                args_by_obs.setdefault(obs_id, []).append(link_of(path))

    # 2. Rewrite each edge's `arguments` from the backlinks of its `from` observation.
    edges_updated = 0
    attached_obs = set()
    if edges_dir.is_dir():
        for path in sorted(edges_dir.glob("*.md")):
            text = path.read_text()
            from_ids = field_ids(text, "from") or []
            if not from_ids:
                continue
            obs_id = from_ids[0]
            attached_obs.add(obs_id)
            arg_links = sorted(set(args_by_obs.get(obs_id, [])), key=id_sort_key)
            new_text = set_arguments(text, arg_links)
            if new_text != text:
                path.write_text(new_text)
                edges_updated += 1

    # 3. Stay-rule: an argument stays in arguments/ iff it names >=1 hypothesis,
    #    or >=1 of its observations sits on a live edge (so the argument sits on
    #    that edge's `arguments` list). Move to/from orphan/ to match.
    moved_out = moved_back = 0
    for path, affects_obs, affects_hyp in arg_files:
        stays = bool(affects_hyp) or any(o in attached_obs for o in affects_obs)
        in_orphan = path.parent == orphan_dir
        if not stays and not in_orphan:
            orphan_dir.mkdir(parents=True, exist_ok=True)
            path.rename(orphan_dir / path.name)
            moved_out += 1
        elif stays and in_orphan:
            path.rename(args_dir / path.name)
            moved_back += 1

    print("edges with arguments rewritten: %d" % edges_updated)
    print("arguments moved to arguments/orphan/: %d" % moved_out)
    print("arguments moved back to arguments/: %d" % moved_back)


if __name__ == "__main__":
    main()
