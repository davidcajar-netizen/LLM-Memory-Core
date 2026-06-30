---
tags: [memory-system, github-repository, flat-files, yaml-frontmatter, search-retrieval, associative-network, davidcajar-netizen, architecture]
links:
  - file: mem2.md
    relation: supports-method
  - file: mem5.md
    relation: shares-pattern
  - file: mem7.md
    relation: supports-method
---

## Sequential Numbering Convention for Memory Files

Memory files use sequential numbering (mem1.md, mem2.md, mem3.md) rather than semantic naming.

**Rationale:**
- Faster upload process: just increment the number
- Intentional friction: prevents casual human browsing and editing
- Faster targeted updates: reference "mem3" instead of searching for semantic name
- Retrieval uses tags and GitHub search, not filenames, so semantic names aren't needed for LLM access

**Trade-off:**
- Humans cannot easily infer content from filename
- This is acceptable because the LLM retrieves via tags, and humans only update files when explicitly directed by the LLM

**Update workflow:**
When a memory needs updating, the LLM references the specific mem number (e.g., "update mem3"), and the human counts to that file in the repository.
