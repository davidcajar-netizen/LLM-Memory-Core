---
tags: [memory-system, automation, tooling, retrieval, local-first, python, archivist, scepticism-engine]
links:
  - file: mem29.md
    relation: extends
  - file: mem30.md
    relation: extends
  - file: mem5.md
    relation: shares-pattern
---

## Automated Memory System (scripts/memory.py) + Memory Gate

A stdlib-only CLI (`scripts/memory.py`) turns the memory store into an executable system, and the Scepticism Engine's new **Memory Gate** makes it policy.

**Retrieval (local-first, before web):** `python3 scripts/memory.py retrieve "<query>" [--tags a,b]` ranks nodes by YAML `tags` (weight 5) > title (3) > body (1). Exit 0 = local hit (treat as high-confidence, project-verified); exit 3 = miss, which is the ONLY signal that authorises a web search. This directly answers mem29's missing-trigger problem for the read path.

**Creation (capture on learning):** `python3 scripts/memory.py remember --title ... --tags ... --link memX:relation --content ...` auto-assigns the next `memN`, writes YAML frontmatter, and warns on duplicate titles. Atomic: one concept per call.

**Honest limit:** a markdown prompt cannot force tool execution — the host platform controls tool-calling. The Engine defines the policy (Memory Gate); the script makes honouring it cheap and deterministic. An agent (e.g. in Cursor) runs retrieve before external search and remember after learning something durable, including coding lessons.

**Parsing note:** the reader handles BOTH frontmatter styles present in the store — YAML `tags: [..]` and the inline `**Tags:** #a #b` style — so retrieval is uniform across old and new nodes.
