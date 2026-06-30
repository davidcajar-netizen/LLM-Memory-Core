---
tags: [protocol-design, gate-placement, scope, verification, anti-sycophancy, epistemic-constraints]
links:
  - file: protocol-modularization.md
    relation: supports-method
  - file: trust-llm-formatting.md
    relation: shares-pattern
---

## Gate Placement Principles

Gates should be placed in the protocol file that matches their scope of application.

**Core protocol (always loaded):**
- Gates that apply to ALL output
- Verification checklist (Gate 7)
- Anti-sycophancy gate (Gate 6)
- Long-term memory retrieval (Gate 8)
- SRCA 4-layer descent

**Secondary files (conditionally loaded):**
- Gates that apply only to specific tasks
- Source verification details → verification_gates.md
- Formatting standards → drafting_standards.md
- Memory creation → memory_system.md

**Principle:**
If a gate applies to every interaction, it belongs in the core protocol. If it applies only to specific tasks, it belongs in the relevant secondary file. This ensures critical constraints are always active while minimizing token load.
