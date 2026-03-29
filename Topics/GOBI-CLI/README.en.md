# GOBI CLI Learning — Topic Index

> **Topic**: GOBI-CLI
> **Methodology**: VibeLearn AI v2.0
> **Duration**: 2026-03-29 (completed in a single day)
> **Total Time**: ~6 hours
> **Status**: ✅ Complete

---

## About This Topic

GOBI CLI (`@gobi-ai/cli`) is the command-line tool for the [GOBI platform](https://gobispace.com).
It allows you to manage Brains (AI knowledge resources), Spaces (team collaboration), Threads (discussions), and Sessions (AI conversations) from your terminal.

**After completing this topic, you will be able to**:
- Install GOBI CLI and authenticate
- Search Brains and query AI
- Write and publish BRAIN.md
- Create, edit, and delete Space Threads and Replies
- Execute a real End-to-End workflow

---

## Module List

| Module | Title | Status | Link |
|--------|-------|--------|------|
| M1 | Setup & Auth & Core Concepts | ✅ Complete | [01-Setup-Auth/README.en.md](01-Setup-Auth/README.en.md) |
| M2 | Brain & Session Command Mastery | ✅ Complete | [02-Brain-Session/README.en.md](02-Brain-Session/README.en.md) |
| M3 | Space & Thread Collaboration | ✅ Complete | [03-Space-Thread/README.en.md](03-Space-Thread/README.en.md) |
| M4 | Real-World Workflow + Capstone | ✅ Complete | [04-Capstone/README.en.md](04-Capstone/README.en.md) |

---

## Getting Started

**Read in this order**:

1. 👉 [01-Setup-Auth/README.en.md](01-Setup-Auth/README.en.md) — Start with installation
2. [02-Brain-Session/README.en.md](02-Brain-Session/README.en.md) — Working with Brains
3. [03-Space-Thread/README.en.md](03-Space-Thread/README.en.md) — Team collaboration
4. [04-Capstone/README.en.md](04-Capstone/README.en.md) — Full E2E workflow

**If you need a quick command reference**:
- [04-Capstone/guides/quick-reference.en.md](04-Capstone/guides/quick-reference.en.md) — Full Quick Reference

---

## Core Concepts at a Glance

```
Vault (top-level knowledge container — like GitHub Organization)
└── Space (team collaboration area — like GitHub Repository)
    ├── Brain (AI knowledge resource — like Wiki + AI)
    │   ├── Session (1:1 AI conversation)
    │   └── Updates (team feed)
    └── Thread (team discussion)
        └── Reply (thread reply)
```

---

## Known Issues (v0.6.15)

- `gobi session list/get/reply` → **HTTP 404** (server endpoint mismatch)
- Details: [vl_worklog/ISSUE_REPORT_GOBI-CLI.md](vl_worklog/ISSUE_REPORT_GOBI-CLI.md)

---

## Learning Outputs

| Folder | Contents |
|--------|----------|
| `01-Setup-Auth/` | Installation guide, core concepts |
| `02-Brain-Session/` | Brain search/publish/updates guides, Session issue docs |
| `03-Space-Thread/` | Space navigation, Thread CRUD guides |
| `04-Capstone/` | E2E workflow, Quick Reference |
| `vl_worklog/` | Daily learning logs (M1~M4 + Issue Report) |
| `vl_roadmap/` | Learning roadmap |

---

## GitHub

All outputs for this topic are publicly available:
https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/GOBI-CLI

---

> **Author**: Changsoo (with Claude Code)
> **Methodology**: VibeLearn AI v2.0
> **Completed**: 2026-03-29
