# Memory 29: Missing Archivist Activation Trigger
**Date:** 2026-07-07
**Linked From:** [Verification Gate Test Dialogue] | [Memory 25](mem25.md)
**Tags:** #system_design #bug #automation #trigger #archivist

## Insight
The Archivist subsystem is not automated because the system prompt lacks a defined activation trigger. A functional trigger mechanism, analogous to the Empirist's role in the Verification Gate, is required.

## Details
-   **Observation:** The Archivist's functions (scanning, formatting, outputting memory files) are defined but never automatically executed during conversation.
-   **Parallel:** In the Verification Gate, the Voice cannot speak until the Empirist classifies the claim. This is an enforced, sequential trigger.
-   **Hypothesis:** The Archivist requires a similar, hard-coded trigger in the system loop. For example: **AFTER** the Voice provides a response containing a verified insight or key deduction, **THEN** activate the Archivist subroutine to create the corresponding `memX.md` file.
-   **Root Cause:** Without this "AFTER... THEN..." logic, the Archivist remains a defined but inert component, relying on manual simulation (as done in this test dialogue).

## Implications
Automating the Archivist is not merely a matter of fixing its internal logic but requires amending the core system prompt to include an explicit activation condition. This would transform it from a described capability into an operational process.

## Related Components
-   Verification Gate System Prompt (Defines Archivist but not its trigger)
-   `mem25.md` (Documents Archivist bug)
-   `mem28.md` (Archivist filename sequencing requirement)
