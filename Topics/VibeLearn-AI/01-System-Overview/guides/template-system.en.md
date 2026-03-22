# VibeLearn AI — Complete Template System Guide
> **[<- Korean Version](template-system.md)**


**Created**: 2026-02-26
**Module**: M1 - System Analysis & Concept Definition

---

## Why Is the Template System Important?

The most powerful feature of VibeLearn AI is that **anyone can start the same way**.
What makes this possible is the template system.

```
Without templates:
  Different approach per person → hard to share → can't reuse

With templates:
  Standard structure → easy sharing → immediately reusable
```

---

## Template File List

The `templates/` folder contains 5 core files:

| File | Role | Phase Used | Frequency |
|------|------|-----------|-----------|
| `topic_starter.md` | Topic information input template | Phase 1 | Once per Topic |
| `roadmap_prompt_template.md` | Roadmap generation prompt | Phase 2 | Once per Topic |
| `daily_learning_prompt.md` | Daily learning plan prompt | Phase 3 | **Daily** |
| `workflow_guide.md` | Full workflow reference | Anytime | As needed |
| `quick_start_prompt.md` | For first-time starters | Before Phase 1 | Once |

---

## Detailed Description of Each Template

---

### 1. topic_starter.md

**Purpose**: Systematically collect all information needed when starting a new Topic

**How to use**:
```
"I want to learn Python basics." → AI asks questions based on topic_starter.md and auto-collects
→ After collection, AI generates topic_info.md + auto-configures folder structure
```

Users never need to open or modify the file directly. AI collects all information through conversation and processes it automatically.

**Information collected**:
- Topic name, description, learning purpose
- Estimated learning period
- Learning objectives (3–5)
- Learning environment (OS, tools)
- Prerequisites (required/recommended)
- Reference materials

**Next step**: AI automatically generates topic_info.md → folder structure setup → leads to Roadmap generation

---

### 2. roadmap_prompt_template.md

**Purpose**: Pass to AI to generate a Topic-specific learning Roadmap

**How to use**:
```
AI automatically proceeds to Roadmap generation after Topic setup is complete.
No need to open any file or enter any command.
```

> Internal operation: AI reads vl_prompts/roadmap_prompt.md (the file with Topic info injected) and generates an optimized Roadmap, saving it to the vl_roadmap/ folder.

**Topic information injected**:
- Topic name and description
- Learning objectives
- Estimated period
- Learning environment

**Roadmap structure generated** (9 items per module):
1. Module basic information
2. Learning objectives
3. Core concepts (20–30% theory)
4. Practice tasks (70–80% hands-on)
5. Expected outputs
6. Definition of Done (DoD)
7. Self-Assessment checklist
8. Time allocation
9. Reference materials

---

### 3. daily_learning_prompt.md

**Purpose**: Pass to AI at the start of every learning session to establish that day's learning plan

**How to use**:
```
Every day to start learning: Just say "Start today's learning."
→ AI reads Roadmap + WorkLog, identifies current progress → creates today's plan
```

**What AI does** (5-step process):
1. Read Roadmap + latest WorkLog → understand current state
2. Create today's learning plan (priorities, time allocation)
3. Present plan to user → **await approval**
4. After approval, begin practice-focused learning guide
5. WorkLog writing guidance + Daily Retrospective

**Key feature**: Approval step — user reviews and revises plan before starting

---

### 4. workflow_guide.md

**Purpose**: A guide for referencing the full workflow at a glance

**When to use**:
- When first learning VibeLearn AI
- When checking what the next step is during a Phase transition
- When explaining the methodology to a team member

**Contents**:
- Phase 1–3 prompt templates
- Full folder structure reference
- Retrospective templates (Daily, Module, Topic)
- Tips & best practices

---

### 5. quick_start_prompt.md

**Purpose**: An all-in-one prompt so first-time users can start in 30 minutes

**How to use**:
```
Copy and paste this entire file to AI
Add at the end: "Topic I want to learn: [topic]"
```

**What AI does** (7 steps):
1. Collect Topic information via conversation
2. Summarize and confirm collected information
3. Guide folder structure creation
4. Generate topic_info.md
5. Confirm whether to generate Roadmap
6. Generate Roadmap
7. Guide learning start

**When to use**: When you want to start faster than GETTING_STARTED.md

---

## Template → Prompt Injection Mechanism

This is the core engine of VibeLearn AI.

```
templates/roadmap_prompt_template.md
(universal template without Topic info)
          +
topic_info.md
(specific info for this Topic)
          │
          ▼
vl_prompts/roadmap_prompt.md
(prompt customized for this specific Topic)
          │
          ▼
Pass to AI → generates Roadmap optimized for this Topic
```

**Why do it this way?**
- templates/ is never modified → reusable for the next Topic
- vl_prompts/ is for this Topic only → optimized for this Topic
- In a new chat session, passing vl_prompts/ to AI → context immediately restored

> ⚠️ **Injection Method (must follow)**
> - Copy the template file **entirely as-is**
> - Fill in only the placeholders in the `[Step 1] Topic Info` section (`{TOPIC_NAME}`, `{DURATION}`, `{LEARNING_GOALS}`, etc.) with actual values from `topic_info.md`
> - Keep all other sections (`[Step 2]`, `[Step 3]`, etc.) **completely unchanged** (no arbitrary abbreviation)
>
> **Why it matters**: If AI arbitrarily abbreviates [Step 2]/[Step 3], the quality of Roadmap/WorkLog generation degrades.
> Real bug that occurred: 652-line template → AI abbreviated to 176 lines (27%), causing degraded output quality.

---

## Template Usage Checklist

### Before Phase 1 Starts
- [ ] Say to AI: "I want to learn Python basics."
- [ ] Provide answers as AI asks questions to gather Topic information
- [ ] Confirm auto-generated folder structure from AI

### Before Phase 2 Starts
- [ ] Phase 1 complete (AI automatically proceeds to Roadmap generation)
- [ ] Review and approve generated Roadmap

### Daily in Phase 3
- [ ] Say to AI: "Start today's learning."
- [ ] Review today's plan presented by AI, then approve
- [ ] Proceed with learning and confirm WorkLog

---

## Frequently Asked Questions

**Q: Can I modify the template files?**
A: Strongly recommended not to modify files in the templates/ folder. If modification is necessary, make a copy and modify that. templates/ must be preserved as the "universal original" so it can be reused for the next Topic.

**Q: I want to proceed in English.**
A: Fully supported. There are `.en.md` versions in the `templates/` folder. Use `roadmap_prompt_template.en.md`, `daily_learning_prompt.en.md`, etc.

**Q: Does AI read the template files directly?**
A: With AI tools that can read files like VS Code + GitHub Copilot, Claude Code, and Cursor, just say "read [filename]" and it will. For AI that can't read files (ChatGPT web), you need to copy and paste the file contents. Using editor-integrated AI tools is strongly recommended.

---

**Author**: Claude with VibeLearn AI
**Reference**: Full templates/ folder, GETTING_STARTED.md Steps 2–5
