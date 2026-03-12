# Clearly App Usage Guide: From BRD/PRD Creation to AI Coding Tool Integration

> **[← Korean Version](clearly-usage-guide.md)**

**Created**: 2026-02-15
**Based on**: 3 hands-on sessions (2026-02-08, 02-14, 02-15)
**Audience**: First-time Clearly app users, developers/non-developers interested in Vibe Coding

---

## 1. What is the Clearly App?

Clearly (https://www.clearlyreqs.com/) is an AI-powered BRD/PRD generation platform. Through a conversational Wizard, you can systematically create requirements documents by answering questions. The core value is converting those documents into configuration files optimized for AI coding tools (Claude Code, Cursor, v0, etc.).

### Core Workflow

```
Create Project → BRD Wizard → Approve BRD → PRD Wizard → Approve PRD → Choose Output Tool
    (0%)           (20%)        (33%)         (50%)        (67%)           (100%)
```

### Who Is It For?

- **Non-technical users**: The AI Wizard guides with questions and example answers, so no technical knowledge is needed
- **Solo developers / POs**: Systematize requirements before Vibe Coding and auto-generate AI coding tool config files
- **Learners**: A hands-on tool for learning BRD/PRD writing through practice

---

## 2. Getting Started: Creating a Project

### Step 1: Log In and Create a New Project

1. Go to https://www.clearlyreqs.com/
2. Log in (with Google account, etc.)
3. Click **"New Project"** or **"+ Create Project"** on the dashboard

### Step 2: Enter Project Basic Information

| Field | Description | Tips |
|-------|-------------|------|
| **Project Title** | Project name (required) | Clear and specific name recommended |
| **Initial Idea** | Project description (min 20 chars, max ~2,000 words) | More detail = higher quality Wizard questions |
| **Output Language** | Select output language | Korean, English, etc. available |

### Tip: Writing a Good Initial Idea

The level of detail in the Initial Idea affects the number and depth of Wizard questions.

**Bad example**: "I want to build a homepage"
**Good example**: "I want to build a static website introducing 5 core content areas from a YouTube channel. The target audience is developers and non-developers interested in AI, it will be hosted on Amazon S3, and it needs to support Korean/English multilingual."

Helpful things to include:
- Project purpose and background
- Target audience
- 3–5 core features
- Technical constraints (budget, tech stack limitations)
- Specific URLs, resource links

---

## 3. BRD Wizard: Defining Business Requirements

### How It Works

- The AI presents questions one at a time in a conversational format, with **3 Example Answers** per question
- Progress shown: "Questions answered: X/5+" and a percentage bar
- **"Generate BRD"** button activates once the minimum question count is reached
- You can continue answering more questions or generate when ready

### Main Question Areas

Confirmed across 3 sessions:

| Area | Description | Answer Tips |
|------|-------------|-------------|
| Business Objectives | Ultimate project goals, existing problem to solve | Include measurable success metrics (KPIs) |
| Tech Stack/Architecture | System structure, external service integrations, constraints | State specific technologies and reasons |
| Target Users/UX | Core users, UX design priorities | Describe expected behavior by user type |
| Content Management | Update approach, consistency maintenance | Be specific about who operates it and the process |
| Risks/Constraints | Budget, timeline, technical risks | Include risk mitigation strategies |

### Tip: Wizard Questions Change Every Time

Even for the same project, Wizard questions vary slightly each session. The AI adapts questions based on the detail level of the Initial Idea and previous answers.

- Session 1: 5 questions
- Session 2: 3 questions (Initial Idea was more detailed)
- Session 3: 4 questions

### After BRD Generation

1. **Review**: Read the generated BRD carefully and check for inaccuracies
2. **Export**: Save locally as Markdown (recommended) or PDF — **always backup!**
3. **Approve**: Click "Approve Document" → unlocks the PRD Wizard

---

## 4. PRD Wizard: Elaborating on Product Requirements

### Difference from BRD

- **BRD**: "Why" and "What" — business perspective
- **PRD**: "What" and "How" — technical/implementation perspective

The PRD Wizard automatically references BRD content and generates more concrete, technical questions.

### Main Question Areas

Confirmed across 3 sessions:

| Area | Description | Connection to BRD |
|------|-------------|------------------|
| Tech Stack Details | Framework, build tools, implementation approach | Elaborates on BRD's Technical Context |
| API/Data Integration | External service integration, data model | Details BRD's Dependencies |
| Multilingual/Scalability | Implementation approach, long-term migration plan | Concretizes BRD's Scalability |
| Design System | UI consistency, CSS structure, AI tool usage | Converts BRD's Usability to implementation level |
| Interaction/Analytics | User data collection, GA4 setup | Measurement method for BRD's Success Metrics |

### PRD Generation Result

PRD is a much more detailed document than BRD (12 sections):

1. Product Overview (vision, goals, target, success criteria)
2. Technical Architecture (system structure, tech stack, components, integration points)
3. User Stories & Use Cases
4. Feature Requirements (Core Features table, Feature Specs, UI Requirements)
5. API Specifications
6. Data Models
7. Security & Compliance
8. Performance Requirements
9. Testing & Quality Assurance
10. Deployment & DevOps
11. Timeline & Milestones
12. Assumptions & Constraints

---

## 5. Choose Output Tool: Integrating with AI Coding Tools

### Available Tools

After PRD Approve, select your development tool on the "Choose Output Tool" screen:

**Vibe Coding Tools** (AI-based visual builders):
- v0 (Vercel), Loveable, Bolt.new, Replit, Firebase Studio

**AI Coding Tools** (code-centric development):
- **Claude Code**, Cursor, OpenAI Codex, Google Antigravity

### Deliverables When Selecting Claude Code

| File | Purpose |
|------|---------|
| **CLAUDE.md** | Project instructions (architecture, coding conventions, file structure) |
| **.claude/settings.json** | Project metadata, tech stack, target settings |
| **REFERENCE_DOCUMENT.md** | Comprehensive reference document integrating BRD and PRD |

### How to Use

1. Place the downloaded ZIP at the project root
2. Run Claude Code with the `claude` command
3. Claude Code automatically reads CLAUDE.md and understands the project context
4. Start Vibe Coding!

---

## 6. Practical Tips

### Tip 1: Improve Quality Through Iteration

Writing BRD/PRD is not a one-time task — **quality improves with repetition**.

| Session | Characteristics | Effect |
|---------|----------------|--------|
| 1st | First attempt, learning the Wizard | Understand basic structure |
| 2nd | Reuse previous answers, move quickly | Efficiency from experience |
| 3rd | Previous answers + fill gaps from new questions | Highest quality with additions |

Real experience: Session 1 (2h, BRD only) → Session 3 (1.5h, full completion)

**Method**: Organize your Wizard answers by topic beforehand, reuse them in new sessions, and add perspectives discovered from new questions.

### Tip 2: Prepare Answers in Advance

If you write Wizard answers in a text file beforehand:
- Copy/paste for fast progress
- Minimize session expiry risk
- Maintain consistent quality

### Tip 3: Always Backup Locally

There can be bugs with dashboard display in the Clearly app, so:
- **Export as Markdown immediately** after generating BRD/PRD and save locally
- **Download ZIP immediately** for Output Tool deliverables
- Complete all deliverable backups before returning to the dashboard

### Tip 4: How to Use Example Answers

The Wizard's Example Answers are useful for finding direction:
- Read all 3 examples and identify common patterns
- Reference the structure (section breaks, including specific numbers)
- But don't copy examples verbatim — customize to your actual project

### Tip 5: Connect BRD and PRD Answers

BRD Wizard answers are reflected in PRD Wizard questions:
- If you say "static website" in BRD, PRD will ask "which build tool will you use?"
- If you mention "multilingual support" in BRD, PRD will ask about the "specific implementation approach"
- Therefore, answering as specifically as possible in BRD leads to more accurate PRD questions

---

## 7. Known Issues and Workarounds

### Bug: Project Disappears from Dashboard

**Symptom**: After completing BRD/PRD/Output, returning to the dashboard shows "No projects yet"
**Frequency**: 3 consecutive reproductions (2026-02-08 ~ 02-15)
**Workaround**:
1. Complete all steps consecutively within the project page without returning to the dashboard
2. Immediately export as Markdown/PDF at each step completion for local backup
3. Download Output Tool as ZIP immediately

### Previously Fixed Bugs

| Bug | Status |
|-----|--------|
| BRD date auto-generation error (shown as 2023) | ✅ Fixed |
| Session expiry during PRD Wizard | ✅ Fixed |
| Project list inaccessible after re-login | ✅ Fixed |

---

## 8. Clearly Usage Scenarios

### Scenario 1: Starting a Vibe Coding Project

```
Organize ideas → Write BRD/PRD in Clearly → Generate Claude Code config via Output Tool
→ Place CLAUDE.md at project root → Start Vibe Coding with Claude Code
```

### Scenario 2: Learning Requirements Documentation

```
Try BRD Wizard with a sample project → Understand BRD structure and sections
→ Try PRD Wizard → Understand the difference between BRD and PRD → Repeat to improve quality
```

### Scenario 3: Organizing Team Project Requirements

```
PM writes Initial Idea → Generate BRD in Clearly → Stakeholder review
→ Generate PRD → Share with dev team → Set up dev environment via Output Tool
```

---

**Author**: VibeLearn AI learner
**Methodology**: VibeLearn AI v2.0
**Based on**: 3-session hands-on practice of Catch Up AI 2026 Homepage project
