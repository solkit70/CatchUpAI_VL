# Clearly App Bug Report

> **[← Korean Version](clearly-bug-report.md)**

**Reporter**: Changsoo Park
**App URL**: https://www.clearlyreqs.com/
**Project**: Catch Up AI 2026 Homepage (Unified Mode)

---

## Session 1 Bugs (2026-02-08) — All Fixed

### Bug #1: BRD Document Date Auto-Generation Error

**Severity**: Low
**Status**: ✅ Fixed (confirmed 2026-02-14)
**Reproduction Path**: Create Project → Complete BRD Wizard → Generate BRD → View Document

**Symptom**:
- BRD Document Header Date auto-generated as `2023-11-20`
- Actual project creation date: 2026-02-08
- Project Details shows "Created 2/8/2026" correctly

**Expected Behavior**:
- BRD Document Header Date should match the actual project creation date

**Fix Confirmed**: Re-tested 2026-02-14; Date correctly generated as `2026-02-15`

---

### Bug #2: Session Timeout During PRD Wizard

**Severity**: High
**Status**: ✅ Fixed (confirmed 2026-02-14)
**Reproduction Path**: BRD Approve → Start PRD Wizard → Answering questions → Suddenly redirected to login screen

**Symptom**:
- While typing an answer to the second PRD Wizard question, forcibly redirected to the login screen
- The answer to the first question had already been submitted
- Logged out without any session expiry warning during Wizard

**Expected Behavior**:
- Session should remain active throughout the Wizard (at least 30 minutes)
- Show a warning before session expiry, and ensure answers in progress are not lost

**Fix Confirmed**: Re-tested 2026-02-14; session maintained normally through all 4 PRD Wizard questions

---

### Bug #3: Project List Not Displayed After Re-Login

**Severity**: Critical
**Status**: ✅ Fixed (confirmed 2026-02-14) → Note: may recur as Bug #4
**Reproduction Path**: Session expiry → logout → re-login → dashboard

**Symptom**:
- After re-login, dashboard stats showed "Total Projects: 2, Documents: 1"
- However, "Your Projects" section showed "No projects yet"
- Searching by project name in the search bar returned no results
- Page refresh (F5) did not resolve the issue
- **Result: Could not access the BRD-approved project to continue the PRD Wizard**

**Expected Behavior**:
- Previously created projects should display normally in the list after re-login
- Project data should be preserved

**Impact**:
- ~30 minutes of Wizard answers and the generated BRD were inaccessible
- Could not proceed with PRD generation
- May have required starting over from scratch

---

## Session 2 Bugs (2026-02-14) — New

### Bug #4: Project Disappears from Dashboard After PRD Approve

**Severity**: Critical
**Status**: 🔴 Open
**Reproduction Path**: Generate BRD → BRD Approve → Generate PRD → PRD Approve → Return to dashboard

**Symptom**:
- Created project "Catch Up AI 2026 Homepage" and completed both BRD and PRD
- After PRD Approve, Project Progress normally showed 67% (2/3 completed)
- Proceeded normally to the "Choose Output Tool" screen
- However, upon returning to the dashboard:
  - **Total Projects: 0** (the just-created project is not counted)
  - **Completed: 0**
  - **Documents: 0** (BRD and PRD were generated but not counted)
  - **Completion Rate: 0%**
  - "Your Projects" section shows "No projects yet"
- Similar to Bug #3 but **stats also show 0** — that's the difference
  - Bug #3 (2/8): Stats showed "Total Projects: 2" but project not listed
  - Bug #4 (2/14): Stats themselves all show 0

**Expected Behavior**:
- Dashboard should show "Total Projects: 1", "Documents: 2" (BRD + PRD)
- "Your Projects" list should show "Catch Up AI 2026 Homepage" at 67% progress
- Clicking the project should allow continuing the "Choose Output Tool" step

**Impact**:
- Cannot continue the remaining "Choose Output Tool" step from 67% progress
- May require starting over from scratch
- BRD and PRD were exported to Markdown locally so document data is not lost

**Note**:
- Appears to be an incomplete fix of Bug #3
- The pattern repeats: project data is stored in the database but not queryable in the dashboard UI

**Session 3 (2026-02-15) Reproduction Confirmed**:
- Bug #4 still reproduced
- This session completed the full flow: BRD → PRD → **Choose Output Tool (Claude Code)**
- Dashboard: Total Projects: 0, Documents: 0, Completion Rate: 0% — same as before
- Output Tool generation completed normally, but project not shown in dashboard
- 3 consecutive reproductions (Session 1: Bug #3, Session 2: Bug #4, Session 3: Bug #4)
- **Workaround**: Complete all steps within the project page without returning to the dashboard; export deliverables immediately via Markdown Export to prevent data loss

---

## Environment Information

### Session 1 (2026-02-08)
- **OS**: Windows 11
- **Clearly App Mode**: Unified
- **Account**: Changsoo Park
- **Time**: ~5:00–5:45 AM PST

### Session 2 (2026-02-14)
- **OS**: Windows 11
- **Clearly App Mode**: Unified
- **Account**: Changsoo Park
- **Time**: ~6:00–6:30 PM PST

### Session 3 (2026-02-15)
- **OS**: Windows 11
- **Clearly App Mode**: Unified
- **Account**: Changsoo Park
- **Time**: ~4:40–5:30 AM PST
- **Scope**: BRD → PRD → Choose Output Tool (Claude Code) — full completion
- **Bug #4 reproduced**: 0 projects shown upon dashboard return

---

## Summary

| # | Bug | Severity | First Reported | Status |
|---|-----|----------|----------------|--------|
| 1 | BRD date auto-generation error (2023-11-20) | Low | 2026-02-08 | ✅ Fixed |
| 2 | Session expiry during PRD Wizard (no warning) | High | 2026-02-08 | ✅ Fixed |
| 3 | Project list inaccessible after re-login (stats visible) | Critical | 2026-02-08 | ✅ Fixed |
| 4 | Project disappears from dashboard after PRD Approve (stats also 0) | Critical | 2026-02-14 | 🔴 Open |

**Note**: BRD and PRD have been exported locally as Markdown/PDF so document data is preserved. However, it is currently impossible to continue the "Choose Output Tool" step from within the Clearly app.
