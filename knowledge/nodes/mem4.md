---
tags: [memory-system, github-repository, flat-files, yaml-frontmatter, search-retrieval, associative-network, davidcajar-netizen, architecture]
links:
  - file: atomicity-constraint.md
    relation: supports-method
  - file: protocol-modularization.md
    relation: shares-pattern
  - file: semantic-naming-convention.md
    relation: supports-method
---

## Memory System Architecture

The LLM Memory Core is hosted on GitHub at https://github.com/davidcajar-netizen/LLM-Memory-Core.

**Architecture:**
- Flat file structure (no subdirectories)
- Each insight stored as individual markdown file
- YAML frontmatter with tags and links
- Search-based retrieval via GitHub search
- Associative network built by following links

**File structure:**
```yaml
---
tags: [tag1, tag2, tag3]
links:
  - file: related-filename.md
    relation: [shares-pattern | supports-method | informs-preference]
---

## [Insight Title]

[Insight content]
```

**Retrieval process (Gate 8 in Epistemic_Protocol.md):**
1. Search repository for relevant files using tags/keywords
2. Load only matching files
3. Scan links metadata to identify related insights
4. Load linked files to build associative network
5. If no files exist, search external sources or request upload

**Replacement of old system:**
This replaces the single-file ledger approach (structural_insights.md) with a distributed, searchable memory system that minimizes token load.
