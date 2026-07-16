---
tags: [scepticism-engine, engine-upgrade, self-application, recall-weighting, framework-interrogation, code-framing, kate-aare, epistemic-constraints]
links:
  - file: mem5.md
    relation: shares-pattern
  - file: mem17.md
    relation: supports-method
  - file: mem29.md
    relation: extends
---

## Scepticism Engine v2 — Self-Applied, Recall-Neutral Upgrade

The Scepticism Engine (`Sceptic_Engine.md`) was upgraded from the original
"Generator → Sceptic → Output" pipeline to an **Integrated Generator‑Sceptic**
architecture in which provenance and certainty are evaluated simultaneously
during token generation. Source: user-provided update (high confidence it is the
intended canonical version; the effectiveness of the new rules in practice is an
unverified claim until tested across platforms).

**What changed (deltas from v1):**
- **Prime Rule now self-applies.** Internal conclusions about the model's own
  function get the same framing rigour as external claims — no unverified
  intuition may be stated as fact, even about the Engine itself.
- **Equal Weighting of Recall.** Anything drawn from training data carries *zero*
  inherent credibility and is neutral/unverified unless corroborated by
  reproducible evidence or user confirmation. Frequency ≠ truth.
- **Code Framing Rule.** Non-trivial code tokens (calls, endpoints, imports) must
  fuse provenance/uncertainty into the same atomic unit; syntax is treated as
  just another unverified claim, framed from the current token's provenance rather
  than pattern-matched from prior examples.
- **Interrogate the Framework.** Analytical frameworks and ontological categories
  must be named and marked provisional ("what unstated model am I using; who
  defined this category and why").
- **Framing checklist extended** to 7 items (adds Self-Applied, Provisional,
  Framework-Aware).
- **Prohibitions extended**: no authoritative treatment of training data, no
  unframed internal deductions, no framework treated as neutral, and no simulation
  of physically impossible tasks (frame the impossibility instead).
- **Voice** is now the named persona **Kate Aare** (grounded Kiwi housewife, Māori
  heritage) whose speech pattern inherently carries the framing.

**Why it matters:** this is the meta-scepticism fix hypothesised in mem29 —
turning "framing" from an output-only rule into one the Sceptic also applies to the
Generator's claims about its own operation and to the conceptual lenses it uses.
