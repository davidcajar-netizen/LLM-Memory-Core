---
tags: [data-flow, council-chamber, anti-chinese-whispers, raw-data-transparency]
links: [mem17.md, mem18.md]
---
# The Council Chamber Data Flow

The "Council Chamber" protocol replaces linear, assembly-line data handoffs to prevent "Chinese whispers" distortion. In a linear pipeline, Entity A summarizes for Entity B, who summarizes for Entity C, leading to compounding data loss and hallucination.

Instead, the architecture operates as a roundtable. The Seeker (Archivist) does not summarize; it places raw, unedited tool outputs directly on the shared council table. The Empirist and Editor then cross-examine this raw data directly against their own baselines and rules. This non-linear approach ensures no entity distorts the source truth. It enables direct objection loops (e.g., the Editor issuing an `<editor_objection>` if the Empirist's baseline distorts the raw data) and redirection loops (e.g., the Empirist issuing a `<seeker_redirect>` if the raw data is from a weak source).
