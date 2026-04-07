# Spec Analysis: 19 - Orchestration & Automation

**Analysis Date**: 2026-04-07
**Source File**: `gobi-monorepo/specs/19-orchestration-and-automation.md`
**Vibe Guiding Relevance**: ⭐⭐⭐ Core (implementation mechanism)

---

## Summary

Orchestration is a system where a per-Vault background daemon detects file changes, manual triggers, and schedules, then automatically executes agent workflows. **Reflex = configurable automation rules**. This is the core mechanism for implementing Vibe Guiding inside the app.

---

## Key Features

| Feature | Description |
|---------|-------------|
| Orchestrator Daemon | One per Vault, background process, auto-starts when Vault is activated |
| Orchestrator Settings | Configured in `.gobi/settings.yaml` (prompt paths, output paths, tools, Watch Patterns) |
| Workflow Nodes | Automation units consisting of triggers + actions |
| Trigger Types | File change / Manual execution / Schedule (future) |
| Claude Session Pool | Ready / Running / Dormant state management, parallel execution support |
| Skills | Per-Vault orchestrator capability library |
| Tools | List of tools available to the agent (file operations, search, etc.) |
| Logs | Real-time log streaming, persistent storage |

---

## `.gobi/settings.yaml` Structure (Configuration Points)

```yaml
orchestrator:
  enabled: true
  prompt_paths:
    - .gobi/prompts/main.md        # ← Add Vibe Guiding prompt here
  output_paths:
    - .gobi/outputs/
  watch_patterns:
    - _Gobi_/Captures/**/*.md      # ← Detect captures
    - _Gobi_/Notes/**/*.md
  tools:
    - file_read
    - file_write
    - search
    # ← Add Vibe Guiding-specific tools here
```

---

## Vibe Guiding Touchpoint Analysis

### 🎯 Touchpoint 1: Implement Vibe Guiding as a Reflex (Workflow Node)

**The most realistic and immediately achievable approach**

```yaml
# .gobi/settings.yaml
watch_patterns:
  - _Gobi_/Captures/**/*.md    # Detect new captures
  - _Gobi_/Notes/**/*.md       # Detect new notes
```

```
Trigger: New capture file created
        ↓
Reflex runs:
  Agent reads capture content
  → Searches Brain for related knowledge
  → Suggests connection points / next actions
  → Saves result to .gobi/outputs/vibe-guide-{date}.md
```

**Feasibility**: ✅ Very high — implementable immediately with current architecture

### 🎯 Touchpoint 2: Vibe Guiding-Dedicated System Prompt
Add a Vibe Guiding-specific prompt to `prompt_paths` in `.gobi/settings.yaml`:

```markdown
# .gobi/prompts/vibe-guiding.md
You are a Vibe Guide for the GOBI ecosystem.
When the user captures new content, your role is to:
1. Connect new captures to existing Brain knowledge
2. Suggest next learning actions based on the VibeLearn AI methodology
3. Surface relevant GOBI features the user might not know about

Context: [Core Concepts extracted from specs inserted here]
```

**Feasibility**: ✅ Very high — implemented simply by adding a prompt file

### 🎯 Touchpoint 3: Package Vibe Guiding as a Skill
Skills = per-Vault capability library. Package Vibe Guiding as an independent Skill and distribute it:

```
vibe-guiding-skill/
├── SKILL.md          # Vibe Guiding behavior definition
├── prompts/          # Per-product guiding prompts
└── tools/            # Vibe Guiding-specific tools
```

Users activate Vibe Guiding by adding this Skill to their Vault.

**Feasibility**: ✅ High — Skills architecture already exists

### 🎯 Touchpoint 4: Schedule-Based Vibe Guiding (Future)
The spec explicitly lists "schedule-based triggers" as a future feature. Once implemented:
- Automatic "Daily Vibe Guide" generation each morning
- Weekly learning progress summary
- Discovery and guidance for unused features

**Feasibility**: ⭐ Future — depends on schedule trigger implementation

---

## Vibe Guiding Design Implication

> **Orchestration = the core mechanism for in-app Vibe Guiding**

Three implementation paths (ordered by complexity):

1. **Immediate (Phase 1)**: Add `.gobi/settings.yaml` + Vibe Guiding prompt file
   - No GOBI team code changes required
   - Configurable by the user directly
   - Fast prototyping possible

2. **Short-term (Phase 2)**: Package Vibe Guiding as a Skill + optimize Watch Patterns
   - Distributable to all GOBI users
   - Integrate VibeLearn AI-generated guides into the Skill

3. **Long-term (Phase 3)**: Schedule triggers + app UI integration (requires GOBI team collaboration)
   - Users experience Vibe Guiding without any manual setup
