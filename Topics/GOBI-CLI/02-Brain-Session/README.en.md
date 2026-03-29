# M2 — Brain & Session Command Mastery

> **Module**: M2
> **Status**: ✅ Complete
> **Estimated Time**: 4-5 hours
> **Actual Time**: ~2 hours (2026-03-29)

---

## What You'll Learn

Practice Brain search/query, BRAIN.md authoring and publishing, Brain Updates CRUD, and Session management commands.
By the end of this module, you'll be able to use GOBI CLI's core knowledge management features.

---

## Learning Order (read in this order)

| # | Document | Description |
|---|----------|-------------|
| 1 | [guides/brain-search-guide.en.md](guides/brain-search-guide.en.md) | brain search + brain ask usage and practice results |
| 2 | [guides/brain-publish-guide.en.md](guides/brain-publish-guide.en.md) | BRAIN.md authoring → publish + brain updates CRUD |
| 3 | [guides/session-management.en.md](guides/session-management.en.md) | session commands + v0.6.15 issue details |
| 4 | [examples/sample-brain.en.md](examples/sample-brain.en.md) | Reusable BRAIN.md template |

---

## M2 Key Summary

```
brain search  →  semantic search across public Brains (similarity score)
brain ask     →  ask Brain AI a question → creates Session
brain publish →  upload BRAIN.md → vault publish
brain updates →  post / list / edit / delete CRUD — all complete
session       →  ⚠️ list/get/reply all return HTTP 404 (v0.6.15 issue)
```

**Key Findings**:
- `gobi brain search`: Korean queries return much higher similarity for Korean Brains
- `gobi brain ask` → use `--content` (not `--message`) option
- `gobi brain ask` returns two Session ID formats: numeric (`id`) and UUID (`sessionId`)
- `publish` vs `post-update` serve different purposes (knowledge base update vs progress sharing)

---

## M2 DoD Checklist

- [x] `gobi brain search` tested with various queries
- [x] `gobi brain ask` — Session created successfully
- [x] `gobi session list/get/reply` attempted (⚠️ v0.6.15 API issue confirmed and documented)
- [x] `BRAIN.md` written → `gobi brain publish` successfully published
- [x] `gobi brain post-update / list-updates / edit-update / delete-update` CRUD complete
- [x] `brain-search-guide.md` written (includes actual output)
- [x] `session-management.md` written (includes issue details)
- [x] `brain-publish-guide.md` + `sample-brain.md` written
- [x] `02-Brain-Session/README.md` written

---

## Previous / Next Module

| | Module | Link |
|--|--------|------|
| ◀ Previous | M1 — Setup & Auth & Core Concepts | [../01-Setup-Auth/README.en.md](../01-Setup-Auth/README.en.md) |
| Next ▶ | M3 — Space & Thread Collaboration | `../03-Space-Thread/README.en.md` |

---

> **Methodology**: VibeLearn AI v2.0
> **Author**: Changsoo (with Claude Code)
