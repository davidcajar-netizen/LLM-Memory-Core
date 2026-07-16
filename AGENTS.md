# AGENTS.md

## Cursor Cloud specific instructions

This repository is **not a runnable application**. It is a markdown-only knowledge
base and prompt architecture (the "LLM Memory Core" + "Scepticism Engine") meant to
be pasted into an LLM chat. There is nothing to compile, serve, or listen on a port.

### What lives here
- `Sceptic_Engine.md` — the prompt users copy into a chat (per `README.md`).
- `Memory_Retrieval.md` / `Memory_Creation.md` — the Archivist retrieval rules and the
  `> LEDGER` file-creation workflow.
- `knowledge/nodes/mem*.md` — atomic memory files, most with YAML frontmatter
  (`tags`, `links`). Some newer nodes use inline `**Tags:**`/`**Linked From:**` instead
  of frontmatter — both styles are valid, so do not "fix" one into the other.

### Build / test / lint / run
- There is **no** package manager, dependency, build, dev server, or test suite, so the
  update script is intentionally a no-op.
- The closest analog to lint/test is a **content check** of the knowledge nodes
  (non-empty markdown; valid YAML frontmatter where present; `links: file:` targets
  exist). A throwaway validator was used during setup; nothing needs to be installed
  to re-run such a check with `python3` (PyYAML is optional — the check falls back to a
  regex scan when it is absent).
- The product's core action is **memory retrieval**. In an LLM chat it uses GitHub repo
  search: `repo:davidcajar-netizen/LLM-Memory-Core path:/^knowledge\/nodes\// [keyword]`.
  Locally you can mirror this with a path-scoped keyword search, e.g.
  `rg -l -i "<keyword>" knowledge/nodes/`.

### Gotchas
- Retrieval depends on this repo being reachable via the LLM platform's GitHub/repo
  search; that part cannot be exercised from a local checkout alone (local `rg` search
  simulates it).
- Creating memories (`> LEDGER`) produces new `memX.md` files that a human commits; do
  not auto-commit contrived memory nodes.
