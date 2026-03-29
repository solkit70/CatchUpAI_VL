# M3 — Space & Thread Collaboration

> **Module**: M3
> **Status**: ✅ Complete
> **Estimated Time**: 3-4 hours
> **Actual Time**: ~1.5 hours (2026-03-29)

---

## What You'll Learn

Practice Space navigation, Thread creation/editing/deletion, and the full Reply CRUD flow.
Unlike M2's Session commands (which have API issues), all Space/Thread commands work correctly.

---

## Learning Order (read in this order)

| # | Document | Description |
|---|----------|-------------|
| 1 | [guides/space-navigation.en.md](guides/space-navigation.en.md) | space list / warp / list-threads / get-thread |
| 2 | [guides/thread-management.en.md](guides/thread-management.en.md) | Full Thread & Reply CRUD flow + practice results |

---

## M3 Key Summary

```
space list          → confirmed 3 Spaces (changbal, gobi, cmds)
space warp          → select active Space (interactive)
space list-threads  → Thread list (JSON includes topics, richText)
space get-thread    → view Thread content + Replies
create-thread       → Thread created (ID: 731 confirmed)
create-reply        → Reply added (ID: 732)
edit-thread         → Thread edited (editedAt field added)
edit-reply          → Reply edited ✅
delete-reply        → Reply deleted ✅
```

**Difference from M2 Session**:
- Space/Thread commands **all work correctly** ✅
- M2 session list/get/reply have HTTP 404 issues

---

## M3 DoD Checklist

- [x] `gobi space list` — confirmed 3 Spaces
- [x] `gobi space warp` — practiced workaround using `--space-slug` option
- [x] `gobi space list-threads` — confirmed Thread lists in changbal, gobi Spaces
- [x] `gobi space get-thread` — viewed existing Thread content + Replies
- [x] `gobi space create-thread` — created new Thread (ID: 731)
- [x] `gobi space create-reply` — added Reply (ID: 732)
- [x] `gobi space edit-thread` — confirmed Thread edit
- [x] `gobi space edit-reply` — confirmed Reply edit
- [x] `gobi space delete-reply` — confirmed Reply deletion
- [x] `space-navigation.md` written
- [x] `thread-management.md` written

---

## Previous / Next Module

| | Module | Link |
|--|--------|------|
| ◀ Previous | M2 — Brain & Session Command Mastery | [../02-Brain-Session/README.en.md](../02-Brain-Session/README.en.md) |
| Next ▶ | M4 — Real-World Workflow + Capstone | `../04-Capstone/README.en.md` |

---

> **Methodology**: VibeLearn AI v2.0
> **Author**: Changsoo (with Claude Code)
