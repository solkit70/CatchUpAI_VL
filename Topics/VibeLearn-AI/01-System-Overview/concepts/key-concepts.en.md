# VibeLearn AI — Key Concepts Glossary
> **[<- Korean Version](key-concepts.md)**


**Created**: 2026-02-26
**Module**: M1 - System Analysis & Concept Definition

---

## How to Use This Document

When you first encounter VibeLearn AI, unfamiliar terms will appear.
This document clearly defines those terms and explains the relationships between them.

---

## Key Terms

---

### Topic

**Definition**: A single unit of subject matter learned in VibeLearn AI

**Examples**:
- `Clearly-BRD-PRD` — Learning BRD/PRD writing with the Clearly app
- `Remotion-VideoCreation` — Creating videos with Remotion
- `VibeLearn-AI` — Learning the VibeLearn AI system itself

**Characteristics**:
- Use English with hyphens (no spaces)
- Used directly as a folder name: `Topics/VibeLearn-AI/`
- One Topic = one complete learning journey

**Note**: Different from "subject" — a Topic is a systematic unit connected to folder structure, file names, and the Roadmap

---

### Phase

**Definition**: The 4 major process stages of VibeLearn AI

```
Phase 1: Topic Setup (once)
Phase 2: Roadmap Generation (once per Topic)
Phase 3: Daily Learning (repeating)
Phase 4: Completion & Retrospective (once per Topic)
```

**Analogy**: In a trip, Phases are like "departure prep → route planning → traveling → returning home"

---

### Module

**Definition**: A detailed learning unit within the Roadmap. Represented as `M1`, `M2`, `M3`, etc.

**Components**:
- 3–5 learning objectives
- Core concepts (20–30% theory)
- Practice tasks (70–80% hands-on)
- Definition of Done (DoD)
- Expected outputs

**Examples**:
- M1: System Analysis & Concept Definition (4h)
- M2: User Guide & Case Studies (4–5h)
- M3: Introduction Video Production (6–8h)

---

### Roadmap

**Definition**: A learning plan for the entire Topic. A document containing detailed plans for all modules.

**File naming convention**: `YYYYMMDD_RoadMap_{TopicName}.md`

**Contents**:
- Total learning period and estimated time
- Module-by-module objectives, practice, DoD
- Self-Assessment checklist
- Reference materials

**Role**: Compass — reference at every learning session to confirm current position

---

### WorkLog

**Definition**: A daily learning work record file

**File naming convention**: `YYYYMMDD_MX_{TopicName}.md`

**Example**: `20260226_M1_VibeLearn-AI.md`

**Required sections**:
1. Today's learning objectives (checklist)
2. Learning content (detailed)
3. Completed tasks
4. Problem-solving log
5. DoD checklist
6. Daily Retrospective
7. Next session preparation

**Role**: Ship's log — records where you've been and where you're going

---

### topic_info.md

**Definition**: A file containing basic information about a Topic. Generated based on the `topic_starter.md` template.

**Location**: `Topics/{TopicName}/topic_info.md`

**Contents**:
- Topic name and description
- Learning purpose and goals
- Learning environment (OS, tools)
- Reference materials

**Role**: Topic's ID card — understand what this learning is about at a glance

---

### vl_prompts/ Folder

**Definition**: A folder storing Topic-specific prompt files

**Contents**:
- `roadmap_prompt.md` — Roadmap generation prompt with Topic info already injected
- `daily_learning_prompt.md` — Daily learning plan prompt

**Role**: AI collaboration interface — provides consistent guidance even in new chat sessions

> ⚠️ **Creation Rule**: When generating these files from a template, fill in only the `[Step 1]` placeholders and keep all other sections (`[Step 2]`, `[Step 3]`, etc.) **completely unchanged**. Arbitrary abbreviation degrades AI guide quality.

---

### vl_worklog/ Folder

**Definition**: A folder storing all WorkLog files for a Topic

**Characteristics**:
- Same day = append to same file
- Next day = create new file
- Module connection clearly stated (by filename)

---

### vl_roadmap/ Folder

**Definition**: A folder storing the Roadmap file for a Topic

**Contents**: One `YYYYMMDD_RoadMap_{TopicName}.md` file

---

### NN-ModuleName/ Folder (Output Folder)

**Definition**: A folder storing actual learning outputs (the "textbook")

**Naming convention**: `sequence_number-ModuleName/`

**Examples**:
- `01-System-Overview/`
- `02-User-Guide/`
- `03-Intro-Video/`

**Subfolder structure**:
```
01-System-Overview/
├── README.md          ← Required: overview of what this module is
├── concepts/          ← Concept documents
├── examples/          ← Verified practice examples
└── guides/            ← Step-by-step guides
```

**Textbook quality standard**: Someone else can learn from this folder alone

---

### DoD (Definition of Done)

**Definition**: A clear checklist defining when a module is considered complete

**Example**:
```
- [ ] README.md, GETTING_STARTED.md reading complete
- [ ] Workflow diagram created
- [ ] 3 target user personas documented
- [ ] At least 3 core concept documents written
```

**Role**: Objective criteria for completion — removes the subjectivity of "I think I'm done"

---

### CVL (Continuous Vibe Learning)

**Definition**: A process for detecting changes and synchronizing learning content when the subject of study changes

**When applied**: When learning a project that has a remote repository (GitHub)

**Process**:
1. Run `git fetch` at the start of every learning session
2. Analyze changes
3. Assess impact (large/medium/small)
4. Record sync in WorkLog if needed

**Impact scale criteria**:
| Scale | Example | Action |
|-------|---------|--------|
| Large | Core architecture change | Separate update session |
| Medium | New feature added | Process before current day's learning |
| Small | Documentation update | Note only in WorkLog |

---

### Automation System

**Definition**: A quality management pipeline that runs automatically on every git commit

**Components**:
| File | Role |
|------|------|
| `scripts/pre-commit` | git hook — shell script that runs automatically on commit |
| `scripts/translate-claude.py` | Auto-translates CLAUDE.md → CLAUDE.en.md (uses Claude API) |
| `scripts/install-hooks.ps1` | One-click PowerShell script to install hooks after cloning |
| `requirements.txt` | Python packages (`anthropic>=0.40.0`) |

**Workflow**:
```
git commit
    ↓
pre-commit hook starts automatically
    ↓
CLAUDE.md changed? → run translate-claude.py (calls Claude API)
    ↓
sync-prompts.ps1 → copies CLAUDE.md to GEMINI.md + AGENTS.md
    ↓
validate-localization.ps1 → quality check
    ↓
Pass → commit complete / Fail → commit aborted
```

**Design Principles**:
- **Translation failure**: Warning only, commit continues (non-blocking) — commit works even without API key
- **sync/validate failure**: Commit aborted (blocking) — quality standards enforced

**Post-clone Setup**:
```bash
# 1. Install hooks
powershell -ExecutionPolicy Bypass -File scripts/install-hooks.ps1

# 2. Install packages
pip install -r requirements.txt

# 3. (Optional) Set API key - for auto-translation
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

**Role**: Eliminates manual translation/sync/validation effort → all quality checks automated with a single commit

---

### Daily Retrospective

**Definition**: A 5–10 minute retrospective conducted at the end of each learning session

**4 questions**:
1. What went well?
2. What could be improved?
3. Insights (new realizations)
4. Tomorrow's focus

---

### Self-Assessment

**Definition**: A checklist for evaluating your own competency upon module completion

**VibeLearn AI's evaluation philosophy**:
- "Have I memorized everything?" ❌
- "Can I execute this with AI?" ✅

**Scoring criteria**:
- All checked: ⭐⭐⭐⭐⭐ (Perfect)
- 10–11: ⭐⭐⭐⭐ (Excellent)
- 8–9: ⭐⭐⭐ (Average)
- 6–7: ⭐⭐ (Needs review)
- 5 or fewer: ⭐ (Re-study recommended)

---

### Templates/ Folder

**Definition**: Universal template files reusable across all Topics

**Location**: `templates/` in the VibeLearn AI root folder

**File list**:
| File | Purpose | When Used |
|------|---------|----------|
| `topic_starter.md` | Topic information gathering | Start of Phase 1 |
| `roadmap_prompt_template.md` | Roadmap generation guide | Phase 2 |
| `daily_learning_prompt.md` | Daily learning plan | Phase 3 daily |
| `workflow_guide.md` | Full workflow reference | Anytime |
| `quick_start_prompt.md` | Fast-start prompt | First start |

**Feature**: Topic-agnostic — reusable for any subject

---

## Term Relationship Diagram

```
VibeLearn AI
├── Templates/ (universal templates)
│   ├── topic_starter.md ──────────────────────────►
│   ├── roadmap_prompt_template.md ────────────────►
│   └── daily_learning_prompt.md ──────────────────►
│                                                   │
└── Topics/ (learning projects)                     │
    └── {Topic}/ ◄──────────────────────────────────┘
        ├── topic_info.md            (Phase 1 output)
        ├── vl_prompts/              (Phase 1 output)
        │   ├── roadmap_prompt.md    ← template + Topic info injected
        │   └── daily_learning.md   ← template copy
        ├── vl_roadmap/              (Phase 2 output)
        │   └── YYYYMMDD_RoadMap.md
        ├── vl_worklog/              (Phase 3 output)
        │   └── YYYYMMDD_M1.md
        └── 01-ModuleName/           (Phase 3 output = textbook)
            ├── README.md
            ├── concepts/
            └── guides/
```

---

**Author**: Claude with VibeLearn AI
**Reference**: README.md (full), GETTING_STARTED.md
