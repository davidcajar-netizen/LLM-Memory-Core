#!/usr/bin/env python3
"""LLM-Memory-Core: local-first memory retrieval and creation.

This is the executable half of the memory system. The Scepticism Engine's Memory
Gate is expected to call it on every turn:

  * `retrieve` runs BEFORE any web search. It ranks local `knowledge/nodes/*.md`
    by YAML tags first, then title, then body. Exit code 0 means "local memory
    answered, do not search the web"; exit code 3 means "nothing local, fall back
    to the web".
  * `remember` (alias `ledger`) writes a new atomic `memN.md` node with YAML
    frontmatter when a durable insight is learned, auto-assigning the next number.

Only the Python standard library is used, because this repository intentionally
has no package manager or dependencies.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import sys
from dataclasses import dataclass, field

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_NODES_DIR = os.path.join(REPO_ROOT, "knowledge", "nodes")

_WORD_RE = re.compile(r"[a-z0-9]+")
_MEM_FILE_RE = re.compile(r"^mem(\d+)\.md$")

# Scoring weights: a tag hit is worth far more than an incidental body hit,
# because tags are the deliberate retrieval index for this store.
TAG_WEIGHT = 5
TITLE_WEIGHT = 3
BODY_WEIGHT = 1


def nodes_dir(explicit: str | None = None) -> str:
    return explicit or os.environ.get("MEMORY_NODES_DIR") or DEFAULT_NODES_DIR


def tokenize(text: str) -> list[str]:
    return _WORD_RE.findall(text.lower())


@dataclass
class Node:
    path: str
    name: str
    number: int | None
    tags: list[str] = field(default_factory=list)
    title: str = ""
    body: str = ""

    @property
    def tag_tokens(self) -> set[str]:
        toks: set[str] = set()
        for tag in self.tags:
            toks.update(tokenize(tag))
        return toks


def _extract_frontmatter_tags(text: str) -> list[str]:
    """Read tags from YAML frontmatter (`tags: [..]` or a block list)."""
    if not text.startswith("---"):
        return []
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return []
    fm = m.group(1)
    inline = re.search(r"^tags:\s*\[(.*?)\]", fm, re.MULTILINE | re.DOTALL)
    if inline:
        return [t.strip().strip("'\"") for t in inline.group(1).split(",") if t.strip()]
    block = re.search(r"^tags:\s*\n((?:\s*-\s*.+\n?)+)", fm, re.MULTILINE)
    if block:
        return [
            line.strip()[1:].strip().strip("'\"")
            for line in block.group(1).splitlines()
            if line.strip().startswith("-")
        ]
    return []


def _extract_inline_tags(text: str) -> list[str]:
    """Read tags from the inline `**Tags:** #a #b` style used by newer nodes."""
    m = re.search(r"^\*\*Tags:\*\*\s*(.+)$", text, re.MULTILINE)
    if not m:
        return []
    return [t.lstrip("#") for t in m.group(1).split() if t.strip()]


def _extract_title(text: str) -> str:
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("#"):
            return s.lstrip("#").strip()
    return ""


def load_node(path: str) -> Node:
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    name = os.path.basename(path)
    mm = _MEM_FILE_RE.match(name)
    number = int(mm.group(1)) if mm else None
    tags = _extract_frontmatter_tags(text) or _extract_inline_tags(text)
    return Node(
        path=path,
        name=name,
        number=number,
        tags=tags,
        title=_extract_title(text),
        body=text,
    )


def load_nodes(directory: str) -> list[Node]:
    if not os.path.isdir(directory):
        return []
    nodes = []
    for name in sorted(os.listdir(directory)):
        if name.endswith(".md"):
            nodes.append(load_node(os.path.join(directory, name)))
    return nodes


def next_number(directory: str) -> int:
    highest = 0
    if os.path.isdir(directory):
        for name in os.listdir(directory):
            mm = _MEM_FILE_RE.match(name)
            if mm:
                highest = max(highest, int(mm.group(1)))
    return highest + 1


def score_node(node: Node, query_tokens: list[str], required_tags: list[str]) -> tuple[int, str]:
    if required_tags:
        node_tags_lower = {t.lower() for t in node.tags}
        if not all(rt.lower() in node_tags_lower for rt in required_tags):
            return 0, ""
    qset = set(query_tokens)
    if not qset and required_tags:
        return TAG_WEIGHT, "matched required tags"
    body_tokens = set(tokenize(node.body))
    title_tokens = set(tokenize(node.title))
    tag_tokens = node.tag_tokens
    score = 0
    hit_terms = []
    for tok in qset:
        if tok in tag_tokens:
            score += TAG_WEIGHT
            hit_terms.append(tok)
        elif tok in title_tokens:
            score += TITLE_WEIGHT
            hit_terms.append(tok)
        elif tok in body_tokens:
            score += BODY_WEIGHT
            hit_terms.append(tok)
    reason = "matched: " + ", ".join(sorted(set(hit_terms))) if hit_terms else ""
    return score, reason


def cmd_retrieve(args: argparse.Namespace) -> int:
    directory = nodes_dir(args.nodes_dir)
    required_tags = [t.strip() for t in (args.tags or "").split(",") if t.strip()]
    query_tokens = tokenize(args.query or "")
    scored = []
    for node in load_nodes(directory):
        s, reason = score_node(node, query_tokens, required_tags)
        if s > 0:
            scored.append((s, node, reason))
    scored.sort(key=lambda x: (-x[0], x[1].name))
    scored = scored[: args.limit]
    if not scored:
        print(f"[memory] no local match for {args.query!r} -> fall back to web search")
        return 3
    print(f"[memory] {len(scored)} local match(es) for {args.query!r} (search web only if insufficient):\n")
    for s, node, reason in scored:
        tags = ", ".join(node.tags) if node.tags else "(no tags)"
        print(f"  {node.name}  [score {s}]  {reason}")
        print(f"    title: {node.title or '(untitled)'}")
        print(f"    tags:  {tags}")
        if args.show_body:
            print("    ---")
            for line in node.body.splitlines():
                print(f"    {line}")
            print("    ---")
        print()
    return 0


def _read_content(args: argparse.Namespace) -> str:
    if args.content is not None:
        return args.content
    if args.content_file:
        with open(args.content_file, "r", encoding="utf-8") as fh:
            return fh.read()
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return ""


def build_node_markdown(title: str, tags: list[str], links: list[tuple[str, str]], content: str) -> str:
    tag_line = "[" + ", ".join(tags) + "]" if tags else "[]"
    lines = ["---", f"tags: {tag_line}"]
    if links:
        lines.append("links:")
        for target, relation in links:
            lines.append(f"  - file: {target}")
            lines.append(f"    relation: {relation}")
    else:
        lines.append("links: []")
    lines.append("---")
    lines.append("")
    lines.append(f"## {title}")
    lines.append("")
    lines.append(content.strip())
    lines.append("")
    return "\n".join(lines)


def _parse_links(raw_links: list[str]) -> list[tuple[str, str]]:
    parsed = []
    for item in raw_links or []:
        if ":" in item:
            target, relation = item.split(":", 1)
        else:
            target, relation = item, "related"
        target = target.strip()
        if not target.endswith(".md"):
            target += ".md"
        parsed.append((target, relation.strip() or "related"))
    return parsed


def cmd_remember(args: argparse.Namespace) -> int:
    directory = nodes_dir(args.nodes_dir)
    content = _read_content(args).strip()
    if not args.title:
        print("[memory] error: --title is required", file=sys.stderr)
        return 2
    if not content:
        print("[memory] error: no content (use --content, --content-file, or stdin)", file=sys.stderr)
        return 2

    tags = [t.strip() for t in (args.tags or "").split(",") if t.strip()]
    links = _parse_links(args.link)

    # Warn (do not block) if a node with the same title already exists, to avoid
    # trivially duplicated memories.
    for node in load_nodes(directory):
        if node.title.strip().lower() == args.title.strip().lower():
            print(f"[memory] warning: a node with this title already exists: {node.name}", file=sys.stderr)

    number = next_number(directory)
    filename = f"mem{number}.md"
    markdown = build_node_markdown(args.title, tags, links, content)

    if args.dry_run:
        print(f"[memory] dry-run: would write {filename}\n")
        print(markdown)
        return 0

    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(markdown)
    print(f"[memory] wrote {os.path.relpath(path, REPO_ROOT)} (tags: {', '.join(tags) or 'none'})")
    return 0


def cmd_tags(args: argparse.Namespace) -> int:
    directory = nodes_dir(args.nodes_dir)
    counts: dict[str, int] = {}
    for node in load_nodes(directory):
        for tag in node.tags:
            counts[tag] = counts.get(tag, 0) + 1
    for tag, n in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"{n:3d}  {tag}")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    directory = nodes_dir(args.nodes_dir)
    for node in load_nodes(directory):
        print(f"{node.name}: {node.title or '(untitled)'}  [{', '.join(node.tags)}]")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="memory", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nodes-dir", help="override knowledge/nodes directory (also MEMORY_NODES_DIR)")
    sub = p.add_subparsers(dest="command", required=True)

    r = sub.add_parser("retrieve", help="local-first search; run BEFORE web search")
    r.add_argument("query", nargs="?", default="", help="free-text query")
    r.add_argument("--tags", help="comma-separated tags that MUST all be present")
    r.add_argument("--limit", type=int, default=5)
    r.add_argument("--show-body", action="store_true", help="print full node body")
    r.set_defaults(func=cmd_retrieve)

    for alias in ("remember", "ledger"):
        w = sub.add_parser(alias, help="create the next memN.md node")
        w.add_argument("--title", required=True)
        w.add_argument("--tags", help="comma-separated tags")
        w.add_argument("--link", action="append", help="link as memX or memX:relation (repeatable)")
        g = w.add_mutually_exclusive_group()
        g.add_argument("--content", help="node body text")
        g.add_argument("--content-file", help="read body from a file")
        w.add_argument("--dry-run", action="store_true", help="print instead of writing")
        w.set_defaults(func=cmd_remember)

    sub.add_parser("tags", help="list tags with counts").set_defaults(func=cmd_tags)
    sub.add_parser("list", help="list nodes").set_defaults(func=cmd_list)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
