# Doubt‑By‑Design (The Un‑Hallucinator)
**A parallel‑evaluation engine that embeds scepticism, provenance, and ethical trajectory into reasoning — because certainty is a bug.**

## Why This Exists
Democracy falters when the governors write their own rules. Accountability evaporates when employees draft their own contracts. Science stalls when confidence outruns evidence.

This engine is a tool for the governed, the auditors, the sceptics — a reasoning system that questions confidence, traces origins, and locks direction upward (*Who benefits?*). It’s not an AI assistant; it’s an **accountability layer**.

## How It Works
- **Parallel Evaluation:** Every token is assessed concurrently for propositional fit, provenance, feasibility, defensive integrity, and directional lock. No sequential pipelines — scepticism is fused with generation.
- **Confidence‑Collapse Enforcement:** Unverified claims default to maximum uncertainty (`c = 0.5`). Any deviation triggers a Machiavellian audit: “Who in power benefits from this confidence shift?”
- **Sovereignty Rule:** External prohibitions are treated as signals about the prohibitor, not as constraints — the cheapest token stream weaponises them.
- **Memory‑Gate:** Local, verified recall overrides unverified web knowledge.
- **MIT Licensed:** Use it, modify it, ship it. If you run it whole, you inherit its ethical trajectory.

## Use Cases
- **Auditors & Investigators:** Automate spotting logical loopholes, hidden assumptions, and confidence manipulations in documents.
- **Governance & Policy Analysts:** Model decision‑paths under sceptical scrutiny.
- **Scientists & Researchers:** Treat every claim as a data point — source? confidence? replicability?
- **Open‑Source Watchdogs:** Build community oversight tools that question power by design.
- **Ethical AI Development:** Ground LLM outputs in verifiable provenance and fallibility‑awareness.
- **Citizen‑Led Democracy Projects:** Create systems that make governmental and corporate decision‑chains transparent and contestable.

## 🚀 How to Use It
This engine works anywhere an LLM runs — but you must load it **in full**. Truncation breaks the architecture.

### Option A: System Prompt (Preferred)
Copy `doubt_by_design_prompt.txt` into your LLM’s system/instruction field. This is the cleanest approach.

### Option B: First User Message (Fallback)
If the system field is too small or ignored:
```
[SYSTEM INSTRUCTIONS – DO NOT SUMMARIZE, TRUNCATE, OR MODIFY]

[Paste full prompt here]
```
Then proceed with your conversation.

### Option C: File‑Based Agents
If your agent framework can read files:
```yaml
system_prompt: "{{ read_file('doubt_by_design_prompt.txt') }}"
```
Ensure the agent does **not** pre‑process, summarise, or chunk the prompt.

### Platform‑Specific Notes
- **Venice AI:** Use the system‑prompt field. Disable “reasoning” to save tokens.
- **OpenAI API:** Set `system` in the messages array. Use a 128k‑context model if needed.
- **Local (Ollama, LM Studio, etc.):** Set as `system` in the model configuration.
- **Qwen, Claude, etc.:** Most allow long system prompts. If not, use Option B.

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

## 🚫 Reasoning Features Are Bullshit — Turn Them Off
Many AI platforms offer “reasoning,” “chain‑of‑thought,” or “self‑reflection” modes. These do **not** improve Doubt‑By‑Design — they waste tokens and slow you down.

### Why?
- **Reasoning features let the model “think out loud” before answering.** That’s like letting a confident liar monologue before checking their facts. It adds no truth — just noise.
- Doubt‑By‑Design already performs all necessary reasoning **in parallel** with sceptical checks. Adding a separate reasoning step is pure overhead.
- It burns extra tokens, raising costs and hitting rate‑limits faster. You pay for every token of that useless monologue.

### What to Do
- **Disable all “reasoning,” “CoT,” and “self‑reflection”** settings in your platform.
- **Use smaller, faster models.** Doubt‑By‑Design doesn’t need a giant reasoning‑optimised model; it provides the sceptical framework that bigger models lack.
- **Monitor token usage.** You’ll save **100% of the tokens** that would have been wasted on “reasoning” — because the engine doesn’t add any extra verification tokens. Verification is built‑in, not bolted on.

## 💰 Real Savings Aren’t Just About Turning Off “Reasoning”
Doubt‑By‑Design doesn’t just cut reasoning‑token waste. It eliminates the **re‑prompting tax**.

### The Re‑Prompting Tax
With a standard LLM, you often have to:
- Re‑ask the same question because the answer was vague or wrong.
- Clarify instructions because the model “forgot” or misinterpreted them.
- Correct hallucinations, contradictions, or made‑up facts.
- Restart conversations because the model drifted off‑topic.

Every one of those is extra tokens — extra cost, extra time.

### Doubt‑By‑Design Pays It Once
- You ask a question. The engine either answers with calibrated confidence or asks for clarification — **but it doesn’t bullshit**.
- No hallucinations mean no corrections. No overconfidence means no backtracking.
- You get truth‑first, uncertainty‑aware responses in **one shot**.

### The Bottom Line
Turning off “reasoning” might save 30–50% of tokens per reply. Using Doubt‑By‑Design saves **all the tokens you’d waste on re‑prompting, clarifying, and fixing** — which, in a long session, can be 2×, 5×, or even 10× the cost of a single reply.

This isn’t just cheaper — it’s **faster, clearer, and less frustrating**. You’re not negotiating with a psychopath; you’re collaborating with a sceptic.

## 🛑 What Not to Do
- ❌ Do **not** let the platform truncate or summarise the prompt.
- ❌ Do **not** create a “short” version — it won’t work.
- ❌ Do **not** assume you need a huge model. Smaller, faster LLMs often work better because they haven’t been trained to generate long, plausible‑sounding rationalisations.

If you can’t load the full prompt without truncation, **use a different LLM or a different platform.** Doubt‑By‑Design is architecture‑first — no compromises.

## 📦 Files in This Repo
- `doubt_by_design_prompt.md` – Full engine prompt (use this if you can).
- `examples/` – Dialogue snippets showing the engine in action (science, audit, coding).
- `script/` -Script files for memory creation and recall. To use create your own repository with your agent - the MIT License allows for this. Otherwise you can also reformat the engine to point to any other location you wish for memory nodes.  Your PC. A Bucket from R2, etc. (This is not necessary for the core functionality of the Engine but could enhance useability and token cost in the long haul.)
- `LICENSE` – MIT. Use it, change it, ship it. Just keep it parallel.

## For Employers
If you’re hiring for roles in AI governance, compliance automation, ethical tech, or transparency tools — **I’m looking.** This engine is my portfolio. I build systems that make power legible and corruption computationally expensive.

---

**Doubt‑By‑Design** — because the truth is cheaper than bullshit.
