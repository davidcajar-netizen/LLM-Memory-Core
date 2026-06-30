---
tags: [protocol-design, token-efficiency, modular-architecture, file-organization, gate-placement]
links:
  - file: mem3.md
    relation: shares-pattern
  - file: mem4.md
    relation: shares-pattern
  - file: mem6.md
    relation: supports-method
---

## Protocol Modularization for Token Efficiency

The epistemic protocol is split into separate files to minimize token load by loading only what's needed for each task.

**File structure:**
- `Epistemic_Protocol.md`: Core engine (always loaded) - contains SRCA 4-layer descent, core constraints, retrieval gates
- `verification_gates.md`: Source verification and failure handling (load when drafting sourced content)
- `drafting_standards.md`: Formatting and publication standards (load when formatting for others)
- `memory_system.md`: Memory creation gate (load only when creating memories)
- `character_voice.md`: Kate Aare persona overlay (load when using voice)

**Token efficiency gains:**
- Quick analytical question: Load only core protocol = ~1,500 tokens (62% reduction from monolithic)
- Drafting an article: Load core + verification + drafting = ~3,000 tokens (25% reduction)
- Memory operations: Load core + memory system = ~2,000 tokens (50% reduction)

**Implementation:**
The core protocol references the other files. Each file contains its relevant sections. The system loads only what's needed for each task.
