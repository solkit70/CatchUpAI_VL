# The Role of BRD/PRD in Vibe Coding

> **[← Korean Version](vibe-coding-role.md)**

## What is Vibe Coding?

> **Vibe Coding**: A development methodology where instead of writing code directly, you convey your vision ("vibe") to AI to generate code

Coined by Andrej Karpathy in February 2025, this concept fundamentally transforms the developer's role:

| Traditional Development | Vibe Coding |
|------------------------|-------------|
| Code writer | Architect + Communicator |
| Focused on How | Focused on What |
| Implementation details | Vision and requirements |

---

## Core Principle

### "Clear requirements = better AI-generated code"

The golden rule of the AI coding era:

```
Requirements quality = AI output quality
```

- **Clear requirements** → Accurate code generation
- **Vague requirements** → Revisions and rework needed
- **Garbage in, garbage out** has never been more important

---

## Why BRD/PRD Matters

### 1. Providing Context for AI

AI coding tools (Cursor, Claude Code, V0, etc.) need clear instructions:

| Without BRD/PRD | With BRD/PRD |
|-----------------|--------------|
| "Build me a login feature" | Detailed prompt based on BRD/PRD |
| Implemented with guesses and assumptions | Accurate implementation matching requirements |
| Repeated revisions | Results close to what you want on the first try |

### 2. Documenting the Vision

If the idea only exists in your head:
- AI cannot understand it
- Cannot be shared with the team
- You'll forget it yourself later

When documented in BRD/PRD:
- Can be used directly as an AI prompt
- The whole team shares the same vision
- Can be referenced before, during, and after development

### 3. Ensuring Quality

```
[Idea] → [BRD] → [PRD] → [AI Prompt] → [Code]
   ↑                              ↓
   └───────── Validation Criteria ─┘
```

BRD/PRD becomes the criteria for validating the final result.

---

## Vibe Coding Workflow

### Three Complexity Tiers

| Tier | Complexity | BRD/PRD Need | Example |
|------|-----------|--------------|---------|
| **Tier 1** | Low | Optional | Simple scripts, utilities |
| **Tier 2** | Medium | Recommended | Feature additions, module development |
| **Tier 3** | High | Required | New projects, architecture design |

### Clearly's Role

```
[Vision / Idea]
      ↓
  [Clearly]  ← Organize requirements with AI Wizard
      ↓
  [BRD]  ← Business requirements
      ↓
  [PRD]  ← Product specifications
      ↓
[Vibe Coding Prompt] ← Prompt for AI coding tools
      ↓
  [Code Generation]
```

---

## Practical Tips

### 1. Choosing Plain Mode vs Technical Mode

| Situation | Mode | Reason |
|-----------|------|--------|
| Using V0, Bubble | Plain Mode | Generates vibe coding prompts |
| Using Cursor, Claude Code | Technical Mode | Task lists + dependencies |
| Prototype | Plain Mode | Fast start |
| Production | Technical Mode | Detailed specs |

### 2. Principles for Good BRD/PRD Writing

- **Be specific**: "fast" → "loads within 3 seconds"
- **Make it verifiable**: "easy to use" → "completed in 3 steps or fewer"
- **Specify priority**: Must have / Should have / Nice to have

### 3. Effective Collaboration with AI

```markdown
# Example of a good prompt
"Please implement a React component based on the following PRD:
[Paste PRD content here]

Focus particularly on:
- User authentication flow
- Error handling
- Responsive design"
```

---

## Summary

| Question | Answer |
|----------|--------|
| What is Vibe Coding? | A methodology for generating code by conveying vision to AI |
| Why is BRD/PRD needed? | To provide AI with clear context |
| What is Clearly's role? | A tool to convert vision into BRD/PRD |
| Core principle? | Clear requirements = better AI-generated code |

---

**Created**: 2026-02-01
**Topic**: Clearly-BRD-PRD / M1
