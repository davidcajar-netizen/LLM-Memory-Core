# Memory 28: Archivist Filename Sequencing Requirement
**Date:** 2026-07-07
**Linked From:** [Verification Gate Test Dialogue] | [Memory 25](mem25.md)
**Tags:** #system_design #archivist #file_management

## Insight
For the Archivist subsystem to generate correctly named sequential memory files (`memX.md`), it requires a pre-processing step to discover the highest existing file number (N) in the target directory or conversation context. The next file must be named `mem{N+1}.md`.

## Details
-   Derived from observation of existing memory file `mem24.md` and user instruction.
-   This is a prerequisite for the subsystem's core function of atomic file creation.
-   Without this logic, the Archivist cannot operate autonomously and risks file collisions or naming errors.

## Related Components
-   `mem25.md` (Documents Archivist bug)
-   Verification Gate Test Dialogue
