# GOBI CLI — Thread & Reply Management Guide

> **Module**: M3 — Space & Thread Collaboration
> **Written**: 2026-03-29
> **Version**: GOBI CLI v0.6.15

---

## Full Thread CRUD Flow

```
create-thread → verify with get-thread
     ↓
create-reply → edit-reply → delete-reply
     ↓
edit-thread
     ↓
delete-thread (if needed)
```

---

## 1. create-thread

Creates a new Thread in a Space.

```bash
gobi space create-thread \
  --space-slug <slug> \
  --title "Thread title" \
  --content "Thread body (markdown supported)"
```

### Practice Results

```bash
gobi space create-thread \
  --space-slug changbal \
  --title "Learning GOBI CLI with VibeLearn AI 👋" \
  --content "Hello! ..." \
  --json

# Response:
# {
#   "id": 731,
#   "title": "Learning GOBI CLI with VibeLearn AI 👋",
#   "replyCount": 0,
#   "createdAt": "2026-03-29T13:47:40.049Z"
# }
```

**Key return value**: `id` → used for subsequent reply/edit/delete operations

---

## 2. create-reply

Adds a reply to a Thread.

```bash
gobi space create-reply <threadId> \
  --space-slug <slug> \
  --content "reply content (markdown supported)"
```

### Practice Results

```bash
gobi space create-reply 731 \
  --space-slug changbal \
  --content "CRUD test in progress. ✅" \
  --json

# Response:
# {
#   "id": 732,
#   "content": "CRUD test in progress. ✅",
#   "parentThreadId": 731,
#   "createdAt": "2026-03-29T13:47:49.049Z"
# }
```

---

## 3. edit-thread

Edits Thread content (own threads only).

```bash
gobi space edit-thread <threadId> \
  --space-slug <slug> \
  --title "updated title" \
  --content "updated content"
```

> You can update just `--title` or just `--content` individually.

---

## 4. edit-reply

Edits a Reply (own replies only).

```bash
gobi space edit-reply <replyId> \
  --space-slug <slug> \
  --content "updated content"
```

### Verification with get-thread

```bash
gobi space get-thread 731 --space-slug changbal

# Thread: Learning GOBI CLI with VibeLearn AI 👋
# By: Changsoo Park
# [updated body]
#
# Replies (1 items):
#   - Changsoo Park: [updated reply] (edited)
```

---

## 5. delete-reply / delete-thread

```bash
# Delete Reply
gobi space delete-reply <replyId> --space-slug <slug>
# → Reply 732 deleted.

# Delete Thread (own only — WARNING: cannot be undone)
gobi space delete-thread <threadId> --space-slug <slug>
# → Thread <id> deleted.
```

---

## Full Command Options Summary

| Command | Required | Optional |
|---------|----------|----------|
| `list-threads` | `--space-slug` | `--limit`, `--cursor` |
| `get-thread <id>` | `--space-slug` | `--limit`, `--cursor` |
| `create-thread` | `--space-slug`, `--content` | `--title`, `--auto-attachments` |
| `edit-thread <id>` | `--space-slug` | `--title`, `--content` |
| `delete-thread <id>` | `--space-slug` | - |
| `create-reply <threadId>` | `--space-slug`, `--content` | `--auto-attachments` |
| `edit-reply <id>` | `--space-slug` | `--content` |
| `delete-reply <id>` | `--space-slug` | - |

---

## M2 session vs M3 thread Comparison

| Item | session (Brain AI chat) | thread (team discussion) |
|------|------------------------|--------------------------|
| **Target** | AI Brain | Team members |
| **Start** | `brain ask` | `space create-thread` |
| **Reply** | `session reply` (⚠️ v0.6.15 issue) | `space create-reply` ✅ |
| **View** | `session get` (⚠️ issue) | `space get-thread` ✅ |
| **Edit** | N/A | `edit-thread`, `edit-reply` ✅ |
| **Delete** | N/A | `delete-thread`, `delete-reply` ✅ |

→ **Space/Thread commands all work correctly, unlike M2 Session** ✅

---

> **Author**: Changsoo (with Claude Code)
> **Methodology**: VibeLearn AI v2.0
