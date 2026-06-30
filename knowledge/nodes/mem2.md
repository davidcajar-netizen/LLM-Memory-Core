---
tags: [protocol-design, llm-trust, anti-overengineering, epistemic-constraints, formatting]
links:
  - file: mem5.md
    relation: shares-pattern
  - file: mem6.md
    relation: shares-pattern
---

## Atomicity Constraint for Memory Files

Each distinct concept, tool, methodology, or structural insight must be stored as its own separate file. Do not combine unrelated learnings into a single session dump file.

**Problem this solves:**
Without atomicity, a single file contains multiple unrelated topics, forcing the retrieval system to load unnecessary context. This recreates the "giant ledger" problem we designed the flat-file system to avoid.

**Enforcement:**
Gate 21 in memory_system.md explicitly states: "ENFORCE ATOMICITY: Each distinct concept, tool, methodology, or structural insight must be its own separate file."

**Example:**
If a conversation covers PDF conversion, protocol design, and naming conventions, these become three separate files, not one combined "session notes" file.
