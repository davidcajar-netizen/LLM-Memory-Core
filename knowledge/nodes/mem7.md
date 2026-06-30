---
tags: [memory-system, naming-convention, sequential-numbering, upload-efficiency, intentional-friction]
links:
  - file: mem4.md
    relation: supports-method
  - file: mem2.md
    relation: shares-pattern
---

## Sequential Numbering Convention for Memory Files

Memory files use sequential numbering (mem1.md, mem2.md, mem3.md, etc.) rather than semantic naming.

**Rationale:**
- Faster upload process: just increment the number instead of generating meaningful filenames
- Intentional friction: prevents casual human browsing and editing of the memory system
- Faster targeted updates: reference "mem3" instead of searching for the right semantic name
- Retrieval uses tags and GitHub search, not filenames, so semantic names aren't needed for LLM access

**Trade-off:**
- Humans cannot easily infer content from filename
- This is acceptable because the LLM retrieves via tags, and humans only update files when explicitly directed by the LLM

**Update workflow:**
When a memory needs updating, the LLM references the specific mem number (e.g., "update mem3"), and the human counts to that file in the repository. This is faster than searching for a semantic filename.

**Implementation:**
The memory_system.md gate (Gate 21) enforces atomicity but does not require semantic filenames. The LLM generates sequential numbers (mem1, mem2, mem3...) and the human uploads them as-is.
