# M2: Catch Up AI BRD/PRD Hands-on Practice

> **[← Korean Version](README.md)**

**Topic**: Clearly-BRD-PRD
**Module**: M2
**Period**: 2026-02-08 ~ 2026-02-15
**Status**: ✅ Complete

---

## What You Learn in This Module

This module records the full hands-on experience of using Clearly's AI Wizard to generate a BRD and PRD for the "Catch Up AI 2026 Homepage" project — from start through "Choose Output Tool (Claude Code)". It documents real sessions including bugs encountered, bug reports filed, and the iterative quality improvements across versions.

---

## Document List (Recommended Reading Order)

| # | Document | Description |
|---|----------|-------------|
| 1 | [notes/wizard-experience.md](notes/wizard-experience.md) | Detailed record of the AI Wizard experience (3-session process) |
| 2 | [brd/catchupai-2026-brd-v3.md](brd/catchupai-2026-brd-v3.md) | Final BRD v3 (Catch Up AI 2026 Homepage) |
| 3 | [prd/catchupai-2026-prd-v2.md](prd/catchupai-2026-prd-v2.md) | Final PRD v2 (12 sections, detailed specs) |
| 4 | [claude-code-output/REFERENCE_DOCUMENT.md](claude-code-output/REFERENCE_DOCUMENT.md) | Integrated BRD/PRD reference document (Claude Code Output) |
| 5 | [claude-code-output/CLAUDE.md](claude-code-output/CLAUDE.md) | Claude Code project instructions (auto-generated) |
| 6 | [notes/clearly-bug-report.md](notes/clearly-bug-report.md) | Clearly app bug report — 4 bugs (real QA record) |

**Previous Module**: [01-Clearly-Overview](../01-Clearly-Overview/) | **Next Module**: [03-Clearly-Intro-Video](../03-Clearly-Intro-Video/)

---

## Folder Structure

```
02-CatchUpAI-BRD-PRD/
├── README.md / README.en.md                           ← This file
├── brd/
│   ├── catchupai-2026-brd.md                          # BRD v1 (2026-02-08, before bug fix)
│   ├── catchupai-2026-brd-v2.md                       # BRD v2 (2026-02-14, after bug fix)
│   ├── brd-catch-up-ai-2026-homepage-2026-02-15.pdf   # BRD v2 PDF version
│   └── catchupai-2026-brd-v3.md                       # BRD v3 (2026-02-15, iteratively improved)
├── prd/
│   ├── catchupai-2026-prd.md                          # PRD v1 (2026-02-14)
│   └── catchupai-2026-prd-v2.md                       # PRD v2 (2026-02-15, 12 sections)
├── claude-code-output/                                # Choose Output Tool deliverables (2026-02-15)
│   ├── CLAUDE.md                                      # Claude Code project instructions
│   ├── PRD.md                                         # Output Tool PRD
│   ├── REFERENCE_DOCUMENT.md                          # Comprehensive BRD/PRD reference
│   └── claude-code-project-files.zip                  # Original ZIP backup
└── notes/
    ├── wizard-experience.md                           # AI Wizard experience record
    └── clearly-bug-report.md                          # Bug report (4 bugs)
```

---

## Practice Sessions

### Session 1 (2026-02-08)

1. Created "Catch Up AI 2026 Homepage" project in Clearly app
2. Answered 5 BRD Wizard questions → BRD v1 generated
3. Reviewed BRD, exported Markdown, Approved
4. Started PRD Wizard → **interrupted by session expiry bug**
5. Could not access project after re-login (Critical bug)
6. Wrote bug report and shared with developer

### Session 2 (2026-02-14)

1. Confirmed developer bug fixes (all 3 bugs fixed)
2. Re-generated BRD v2 with new project → confirmed date bug fixed
3. BRD Approved → answered 4 PRD Wizard questions → PRD v1 generated
4. PRD Approved → Project Progress 67% (2/3 completed)
5. Bug #4 discovered: project disappears on dashboard return

### Session 3 (2026-02-15) — Full Completion

1. Bug #4 reproduction confirmed (dashboard: Total Projects 0)
2. New project → BRD v3 (4 questions, previous answers reinforced)
3. PRD v2 generated (5 questions, 12 sections, GA4/design system/privacy added)
4. **First-ever "Choose Output Tool" completion** — selected Claude Code
5. Downloaded and saved output deliverables locally
6. Bug #4 reproduction confirmed (still Open)

---

## Document Summary

### BRD (Business Requirements Document)

- **Project**: Catch Up AI 2026 Homepage
- **Core Goal**: Information hub for 5 key content areas, YouTube subscription conversion, community growth
- **Tech Stack**: Static website (HTML/CSS/JS), Amazon S3 hosting
- **Version Comparison**: v1 (5Q) → v2 (3Q) → v3 (4Q) — fewer questions but higher quality with each iteration

### PRD (Product Requirements Document)

- **BRD-based**: Detailed product specifications built on the BRD
- **Core Features**: Main page, 5 project detail pages, multilingual support, responsive design, newsletter subscription
- **Version Comparison**: v1 (4Q, basic structure) → v2 (5Q, 12 sections, with Timeline/Performance/Deployment)

### Claude Code Output

- **CLAUDE.md**: Claude Code project instructions including architecture, coding conventions, file structure
- **REFERENCE_DOCUMENT.md**: Comprehensive reference document integrating BRD and PRD
- **Usage**: Place at the project root so Claude Code automatically understands project context

---

## Bug Report Summary

| # | Bug | Severity | First Reported | Final Status |
|---|-----|----------|----------------|--------------|
| 1 | BRD date auto-generation error | Low | 2/8 | ✅ Fixed |
| 2 | Session expiry during PRD Wizard | High | 2/8 | ✅ Fixed |
| 3 | Project inaccessible after re-login | Critical | 2/8 | ✅ Fixed |
| 4 | Project disappears from dashboard | Critical | 2/14 | 🔴 Open (reproduced 3×) |

---

## M2 Learning Objectives Status

- [x] Completed real BRD creation with Clearly's AI Wizard
- [x] Completed real PRD creation (BRD → PRD flow)
- [x] Completed full workflow through Choose Output Tool
- [x] Documented iterative quality improvement (v1 → v3)
- [x] Filed real-world bug report and tracked fixes

**Achievement Rate**: 100% ✅

---

## Key Insights (The "Aha!" Moments of This Module)

1. **BRD/PRD iteration is not a one-time task** — quality improves with each pass
2. **Claude Code Output = project context for AI** — drop it in the root and Claude Code understands everything
3. **The AI Wizard adapts** — questions change slightly each time based on your Initial Idea
4. **Always back up locally** — cloud apps can have critical bugs; Markdown export is essential

---

**Author**: Claude with VibeLearn AI
**Methodology**: VibeLearn AI v2.0
**WorkLog Reference**: [notes/wizard-experience.md](notes/wizard-experience.md)
