---
tags: [protocol-design, llm-trust, anti-overengineering, epistemic-constraints, formatting, token-efficiency]
links:
  - file: atomicity-constraint.md
    relation: shares-pattern
  - file: protocol-modularization.md
    relation: shares-pattern
---

## Trust LLM for Formatting

The protocol should enforce epistemic constraints (verification, uncertainty admission, source attachment) but not over-structure output formatting. The LLM already knows how to write markdown, YAML, and structure documents.

**Core principle:**
Over-engineering the output format adds token count without improving quality. The hard part is not hallucinating and admitting uncertainty; the easy part is formatting. Focus protocol enforcement on the hard part.

**Application:**
- Memory file creation (Gate 21): Trust the LLM to generate appropriate tags and natural structure
- Drafting tasks: Trust the LLM to format markdown correctly
- Focus verification gates on factual claims and source attachment, not stylistic choices

**Token efficiency gain:**
Removing rigid formatting templates reduces protocol token count by 20-30% while maintaining epistemic rigor.
