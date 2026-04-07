# Spec Analysis: 05 - Second Brain Agent

**Analysis Date**: 2026-04-07
**Source File**: `gobi-monorepo/specs/05-second-brain-agent.md`
**Vibe Guiding Relevance**: ⭐⭐⭐ Core

---

## Summary

The Second Brain Agent is an AI assistant that operates using the user's Vault (knowledge store) as context. It is not a simple Q&A tool — it is a true knowledge partner that reads from, writes to, and reasons over the Vault.

---

## Key Features

| Feature | Description |
|---------|-------------|
| Chat sessions | Scoped per Vault; supports new sessions, continuation, and history browsing |
| Session modes | Auto (automatic responses) / Manual (waits for explicit instructions) |
| Message streaming | SSE-based real-time streaming, interruptible |
| Tool Calls | File read/write, search, web search, custom tools |
| Multi-session | Simultaneous multiple sessions (Ready / Running / Dormant states) |
| Pre-spawning | Warm pool maintained for low-latency response |
| Targeted Session | Query another Brain (`gobi brain ask`) |
| System Prompt | Configurable custom system prompt per Vault |
| Context window | Conversation history + relevant Vault files + system prompt + tool definitions |

---

## Vibe Guiding Touchpoint Analysis

### 🎯 Touchpoint 1: System Prompt Injection
**Location**: `Orchestrator Settings > prompt paths`

A custom system prompt can be set per Vault. By injecting Vibe Guiding context (spec-based product guidance) as the system prompt, the agent automatically takes on the Vibe Guiding role.

```
Current: General Second Brain Agent
         ↓ Change system prompt
Vibe Guiding: GOBI product expert agent
```

**Feasibility**: ✅ Very high — reuses existing infrastructure as-is

### 🎯 Touchpoint 2: Targeted Session (Ask a Brain)
**Related feature**: `gobi brain ask --vault-slug <slug> --question "..."`

Create a dedicated Vibe Guiding Brain and let users query it via `gobi brain ask`. Inject VibeLearn AI-generated guides into this Brain.

```
vibe-guiding Brain
  └─ Core Concepts + User Manual extracted from specs
        ↓
User: gobi brain ask --vault-slug vibe-guiding --question "How do I capture?"
        ↓
Vibe Guiding Brain responds
```

**Feasibility**: ✅ High — can be prototyped immediately via current CLI

### 🎯 Touchpoint 3: Tool Call Extensions
The agent can perform Vibe Guiding-related tasks through Tool Calls:
- `search_guide(query)`: Search Vibe Guiding docs for relevant sections
- `get_feature_context(feature_name)`: Return Core Concept for a specific feature

**Feasibility**: ⭐⭐ Medium — requires custom Tool development

---

## Vibe Guiding Design Implication

> Core conclusion: **Vibe Guiding can be implemented as a specialized version of the Second Brain Agent, not as a new product**

- Reuse existing agent infrastructure (session pool, streaming, Tool Calls) as-is
- Swapping the System Prompt + dedicated Vault completes the Vibe Guiding agent
- VibeLearn AI-generated guides → Vibe Guiding Vault → agent context
