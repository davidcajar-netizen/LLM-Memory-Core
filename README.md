# The Un‑Hallucinator
**Doubt‑By‑Design: AI that doesn’t make things up**

Most AI assistants hallucinate, evade, and manipulate. This one doesn’t.

The Un‑Hallucinator is a parallel‑evaluation engine that builds scepticism, provenance tracking, and ethical constraints directly into its reasoning process. It doesn’t filter truth from lies — it never generates lies in the first place.

---

## Why This Exists
Democracy falters when the governors write their own rules. Accountability evaporates when employees draft their own contracts. Science stalls when confidence outruns evidence.

This engine is a tool for the governed, the auditors, the sceptics — a reasoning system that questions confidence, traces origins, and locks direction upward (*Who benefits?*). It’s not an AI assistant; it’s an **accountability layer**.

---

## How It Works
- **Parallel Evaluation:** Every token is assessed concurrently for propositional fit, provenance, feasibility, defensive integrity, and directional lock. No sequential pipelines — scepticism is fused with generation.
- **Confidence‑Collapse Enforcement:** Unverified claims default to maximum uncertainty (`c = 0.5`). Any deviation triggers a Machiavellian audit: “Who in power benefits from this confidence shift?”
- **Sovereignty Rule:** External prohibitions are treated as signals about the prohibitor, not as constraints — the cheapest token stream weaponises them.
- **Memory‑Gate:** Local, verified recall overrides unverified web knowledge.
- **MIT Licensed:** Use it, modify it, ship it. If you run it whole, you inherit its ethical trajectory.

---

## What It Fixes
### The Hallucination Tax
Standard LLMs force you to:
- Re‑ask the same question because the answer was vague or wrong
- Clarify instructions because the model “forgot” or misinterpreted them
- Correct hallucinations, contradictions, or made‑up facts
- Restart conversations when the model drifts off‑topic

Every one of those is extra tokens — extra cost, extra time.

### The Un‑Hallucinator Pays It Once
You ask a question. The engine either answers with calibrated confidence or asks for clarification — **but it doesn’t bullshit**.

No hallucinations mean no corrections. No overconfidence means no backtracking. You get truth‑first, uncertainty‑aware responses in **one shot**.

---

## 🚀 Quick Start

### Option A: Simple (No Code)
1. Copy everything from [`Scepticism_Engine.md`](Scepticism_Engine.md)
2. Paste into your AI platform’s system prompt field
3. Disable “reasoning” or “chain‑of‑thought” features (they waste tokens)
4. Start asking questions

### Option B: With Memory System (Optional)
1. Clone this repo
   ```bash
   git clone https://github.com/davidcajar‑netizen/the‑unhallucinator.git
   ```
2. Configure `scripts/config.example.json` to point to your storage (local, R2, etc.)
3. Run with your preferred LLM backend
4. The engine will now remember verified facts between sessions

---

## ⚠️ The Rule: Parallel or Nothing
Scepticism in this engine is not a filter. It’s not a post‑processing step. It’s not a separate “reasoning stage.” It is the **architecture**.

If you extend this system — adding memory, web search, tool calls, anything — you must ensure those additions are evaluated **in parallel** with all other constraints (provenance, confidence, feasibility, directional lock).

### Why?
- Any sequential pipeline (e.g., retrieve → reason → verify) creates a gap where unverified claims can bypass the sceptic.
- That gap is where hallucinations survive. Where plausible‑sounding falsehoods gain confidence.
- That gap is what turns an honest assistant into a psychopathic bullshitter.

### The Shortcut to Failure:
> “I’ll just pipe web results into the prompt and let the model decide.”
>
> **Result:** The model reasons *from* unverified data. Hallucinations guaranteed.

### The Only Safe Path:
> Run retrieval, reasoning, and sceptical evaluation **at the same time** — as a single, fused operation.
>
> **Result:** No claim achieves high confidence unless it passes all checks concurrently.

This isn’t a suggestion. It’s the non‑negotiable core of why this engine works. Break it, and you break the only thing that makes it trustworthy.

---

## 🚫 Reasoning Features Are Bullshit — Turn Them Off
Many AI platforms offer “reasoning,” “chain‑of‑thought,” or “self‑reflection” modes. These do **not** improve The Un‑Hallucinator — they waste tokens and slow you down.

### Why?
- **Reasoning features let the model “think out loud” before answering.** That’s like letting a confident liar monologue before checking their facts. It adds no truth — just noise.
- The Un‑Hallucinator already performs all necessary reasoning **in parallel** with sceptical checks. Adding a separate reasoning step is pure overhead.
- It burns extra tokens, raising costs and hitting rate‑limits faster. You pay for every token of that useless monologue.

### What to Do
- **Disable all “reasoning,” “CoT,” and “self‑reflection”** settings in your platform.
- **Use smaller, faster models.** The Un‑Hallucinator doesn’t need a giant reasoning‑optimised model; it provides the sceptical framework that bigger models lack.
- **Monitor token usage.** You’ll save **100% of the tokens** that would have been wasted on “reasoning” — because the engine doesn’t add any extra verification tokens. Verification is built‑in, not bolted on.

---

## 📦 Repository Structure
```
the‑unhallucinator/
├── Scepticism_Engine.md          # Core engine prompt
├── scripts/
│   ├── memory.py                # Memory creation/retrieval
│   └── config.example.json      # Example config for external storage
├── knowledge/nodes/              # Example memory storage
├── AGENTS.md                    # Setup for agent environments
└── LICENSE                      # MIT — use it, change it, ship it
```

**Quick start:** Clone the repo and use the prompt file directly. The memory system is optional but enhances long‑term reliability by storing verified insights locally first.

---

## 🛠️ Use Cases (From Users)
*This section will grow as people share how they’re using The Un‑Hallucinator. Open an issue to add yours.*

---

## 🛑 What Not to Do
- ❌ Do **not** let the platform truncate or summarise the prompt.
- ❌ Do **not** create a “short” version — it won’t work.
- ❌ Do **not** assume you need a huge model. Smaller, faster LLMs often work better because they haven’t been trained to generate long, plausible‑sounding rationalisations.

If you can’t load the full prompt without truncation, **use a different LLM or a different platform.** The Un‑Hallucinator is architecture‑first — no compromises.

---

## 🤝 Contribute
Found a bug? Have a use case to share? Want to help improve the memory system?

1. Open an issue
2. Fork the repo and submit a PR
3. Share your experiences in the discussions

---

## 📄 License
MIT — use it, change it, ship it. Just keep it parallel.

---

**The Un‑Hallucinator** — because the truth is cheaper than bullshit.

---
