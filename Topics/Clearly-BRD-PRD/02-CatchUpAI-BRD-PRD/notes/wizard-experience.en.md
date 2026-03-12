# Clearly AI Wizard Experience Record

> **[← Korean Version](wizard-experience.md)**

**Date**: 2026-02-08
**Project**: Catch Up AI 2026 Homepage
**Mode**: Unified (Plain/Technical Mode appears to have merged into Unified)

---

## 1. Project Creation Screen

### Create New Project
- **Project Title**: Enter project name (required)
- **Initial Idea**: Describe the project idea, goals, and what you want to achieve (max ~2,000 words, min 20 characters)
- **Output Language**: Select output language (Korean, English, etc.)
- **"Create & Start BRD →"** button launches the BRD Wizard

### Tips
- Providing as much context as possible in the Initial Idea leads to more precise Wizard questions
- Including specific resources like YouTube channel URLs and playlist URLs is helpful
- Pre-organizing your target audience, success metrics, and key content before entering makes the process more effective

---

## 2. BRD Wizard Process

### How It Works
- The AI Assistant presents questions one at a time in a conversational format
- Each question comes with **3 Example Answers** for reference
- Progress indicator: "Questions answered: X/5+" and a percentage bar
- Once the minimum question count is reached, the **"Generate BRD"** button appears
- You can continue answering additional questions or click Generate BRD when ready

### Question Flow (Actual Experience)

| Order | Question Topic | Core Content |
|-------|---------------|-------------|
| 1 | Business Objectives | Most important business goals, ultimate business value |
| 2 | Tech Stack | System architecture, tech stack, YouTube integration, functional requirements |
| 3 | Multilingual Support & AI Tools | Multilingual implementation approach, AI coding tool considerations |
| 4 | Content Management | Content update cadence, YouTube video curation, AI tool usage |
| 5 | Risks & Constraints | Business/technical constraints, budget, timeline, security, AI tool risks |

### Tips
- More specific answers produce higher quality BRDs
- Reference the Example Answers for direction but customize them to your actual project
- It's recommended to answer all minimum questions (5) before generating the BRD
- **Even after the "Generate BRD" button appears, answering more questions produces a more complete BRD**

---

## 3. BRD Generation Result

### Generated BRD Structure
1. Introduction
2. Stakeholder & User Analysis (RACI Matrix, Target Users, User Journey Map)
3. Business Objectives (Primary Objectives, Success Metrics, Business Value)
4. Technical Context (Architecture, Constraints, Scalability)
5. Functional Requirements (Core Features, User Stories)
6. Non-Functional Requirements (Performance, Security, Usability, Reliability)
7. Constraints & Assumptions (Budget, Timeline, Assumptions)
8. Risk Analysis (table format)
9. Dependencies
10. Approval

### Quality Assessment
- Systematically incorporates the information you entered
- RACI Matrix and User Journey Map are added automatically
- Success Metrics include specific KPIs and target values auto-generated (review needed)
- Risk Analysis is neatly organized in table format

### Notes
- **Date bug**: Document Header Date was incorrectly set to 2023-11-20 → manual correction needed
- Always review and verify the generated BRD before proceeding

---

## 4. BRD Document Management

### Export Options
- **Copy**: Copy full text
- **Markdown**: Download as .md file (recommended — best for local storage)
- **PDF**: Download as PDF
- **History**: View version history

### Edit Options
- **Edit**: Directly edit document content
- **Regenerate**: Regenerate the BRD
- **Approve Document**: Approve BRD → unlocks PRD Wizard

---

## 5. PRD Wizard Process (Partial Experience)

### After BRD Approval
- Approving the BRD updates Project Progress to 33% (1/3)
- "Start PRD Wizard" button becomes active
- PRD Wizard uses the same conversational format as the BRD Wizard

### PRD Wizard Questions (Portion Experienced)
| Order | Question Topic | Core Content |
|-------|---------------|-------------|
| 1 | Detailed Tech Stack | Specific choices for the tech stack mentioned in BRD, framework decisions |
| 2 | Core Feature Implementation | Specific implementation for YouTube embed, recommended videos, live schedule, language switching |

### Reason for Interruption
- Session expired during the second question, redirected to login screen
- Project inaccessible after re-login (bug)

---

## 6. Full Project Flow (Clearly App)

```
Create Project → BRD Wizard → Generate BRD → Review & Approve BRD
                                                       ↓
                              PRD Wizard → Generate PRD → Review & Approve PRD
                                                                    ↓
                                                              Tool Output (unlocked)
```

**Project Progress stages**: 0% → 33% (BRD complete) → 66% (PRD complete) → 100% (Tool Output complete)

---

## 7. Bugs Discovered

See `clearly-bug-report.md` for details.

| # | Bug | Severity |
|---|-----|----------|
| 1 | BRD date auto-generation error | Low |
| 2 | Session expiry during PRD Wizard | High |
| 3 | Project inaccessible after re-login | Critical |

---

## 8. Overall App Assessment

### What Works Well
- The conversational Wizard guides even non-technical users through BRD creation
- Example Answers are very useful (great for finding the right direction)
- Generated BRD structure is professional and systematic
- Markdown/PDF export is convenient
- Korean output quality is good

### Areas for Improvement
- Session stability (prevent session expiry during Wizard)
- Project data accessibility (project display issue after re-login)
- BRD date auto-generation accuracy
- Insufficient UI guidance on the change from Plain Mode/Technical Mode to Unified

---

**Created**: 2026-02-08
**Topic**: Clearly-BRD-PRD / M2
