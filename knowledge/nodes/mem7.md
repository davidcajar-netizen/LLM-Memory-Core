---
tags: [memory-system, naming-convention, semantic-filenames, human-readability, search-retrieval]
links:
  - file: memory-system-architecture.md
    relation: supports-method
---

## Semantic Naming Convention for Memory Files

Memory files use semantic filenames for human readability, while tags handle machine retrieval.

**Filename format:**
`{topic}-{key-concept}.md`

**Examples:**
- `marker-pdf-conversion.md`
- `atomicity-constraint.md`
- `trust-llm-formatting.md`

**Rationale:**
- Semantic names are human-readable when browsing the GitHub repository
- Tags enable search-based retrieval by the LLM
- The filename itself doesn't affect retrieval since search uses tags and content
- Sequential numbering (001.md, 002.md) loses self-documenting property

**Trade-off:**
Semantic names require the LLM to generate meaningful filenames, but this is a formatting task the LLM handles well. The retrieval system doesn't depend on filenames.
