"""Create one id'd node file in an FLF EpiStack analysis directory.

The pipeline runs steps in parallel, so several agents mint node files at the
same moment. If each picked its own `PREFIX-N` they would collide. This script
owns id assignment instead: it takes the next free number under an exclusive
lock, so concurrent callers always get distinct ids.

The caller passes the node type and the descriptive title *without* the id, and
pipes the file's markdown (frontmatter + body) on stdin. Every `{{ID}}` in that
markdown is replaced with the assigned id, and the file is written to the type's
folder as `PREFIX-N - Title.md`. The assigned id and path go to stdout.

Plain files carry no id — `initial_prompt.md`, everything under `agent-notes/`,
the per-cluster `Analysis of HC-N - ….md`, and the final `main report - ….md`
are written directly by the agent, not through this script.

(Intended to grow: further file types can be added to TYPES as the pipeline
gains them.)

Usage:
    python3 create_node.py <analysis-dir> --type source --title "Some title" < node.md
    ... | python3 create_node.py <analysis-dir> --type observation --title "Some title"
"""

import argparse
import fcntl
import pathlib
import re
import sys

# node type -> (id prefix, folder). Ids are unique per prefix across the whole
# analysis directory and are never reused, so retired nodes in sub-folders
# (non-curated/, merged/, dropped/, orphan/) still hold their numbers.
TYPES = {
    "source": ("S", "sources"),
    "data-basis": ("D", "data-bases"),
    "observation": ("O", "observations-and-facts"),
    "hypothesis": ("H", "hypotheses"),
    "hypothesis-cluster": ("HC", "hypothesis-clusters"),
    "argument": ("A", "arguments"),
    "evidence-link": ("E", "evidence-links"),
    "correlation-group": ("CG", "correlation-groups"),
}

ILLEGAL = re.compile(r'[/\\:*?"<>|]')
LOCKFILE = ".create_node.lock"


def clean_title(title, prefix):
    """Strip a leading id the caller shouldn't have passed, drop illegal chars."""
    title = re.sub(r"^%s-\d+\s*-\s*" % prefix, "", title.strip())
    title = ILLEGAL.sub("-", title)
    return re.sub(r"\s+", " ", title).strip(" .")


def next_id(root, prefix):
    """Highest existing PREFIX-N anywhere under root, plus one."""
    pattern = re.compile(r"^%s-(\d+) - " % prefix)
    highest = 0
    for path in root.rglob("*.md"):
        m = pattern.match(path.name)
        if m:
            highest = max(highest, int(m.group(1)))
    return highest + 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("analysis_dir")
    ap.add_argument("--type", required=True, choices=sorted(TYPES))
    ap.add_argument("--title", required=True, help="descriptive title, without the id")
    args = ap.parse_args()

    root = pathlib.Path(args.analysis_dir)
    if not root.is_dir():
        sys.exit("no such analysis directory: %s" % root)

    prefix, folder = TYPES[args.type]
    title = clean_title(args.title, prefix)
    if not title:
        sys.exit("empty title after cleaning")
    if title != args.title.strip():
        print("note: title cleaned to %r" % title, file=sys.stderr)

    content = sys.stdin.read()
    if not content.strip():
        sys.exit("no content on stdin")
    if "{{ID}}" not in content:
        print("warning: no {{ID}} placeholder in content — the node may lack an id",
              file=sys.stderr)

    lock = open(root / LOCKFILE, "w")
    try:
        # Everything from picking the number to writing the file is one atomic
        # section; a concurrent caller waits here rather than reusing the id.
        fcntl.flock(lock, fcntl.LOCK_EX)
        node_id = "%s-%d" % (prefix, next_id(root, prefix))
        out = root / folder
        out.mkdir(parents=True, exist_ok=True)
        path = out / ("%s - %s.md" % (node_id, title))
        path.write_text(content.replace("{{ID}}", node_id))
    finally:
        fcntl.flock(lock, fcntl.LOCK_UN)
        lock.close()

    print(node_id)
    print(path)


if __name__ == "__main__":
    main()
