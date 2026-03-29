# GOBI CLI — Space Navigation Guide

> **Module**: M3 — Space & Thread Collaboration
> **Written**: 2026-03-29
> **Version**: GOBI CLI v0.6.15

---

## What is a Space?

A **team collaboration area** within a Vault. It groups related Brains and Threads,
analogous to a GitHub Repository or Slack channel.

---

## gobi space list

Lists the Spaces you are a member of.

```bash
gobi space list
gobi space list --json
```

### Practice Results (2026-03-29)

```
Spaces (3):
- [changbal] Changbal (창발)
    → Seattle IT professionals community. Meaning: "creative emergence"
- [gobi] Gobi
    → GOBI platform official Space
- [cmds] CMDSPACE
    → CMDSPACE by Yohan Ku
```

### Key JSON Fields

```json
{
  "slug": "changbal",        ← used with --space-slug
  "name": "Changbal (창발)",
  "description": "..."
}
```

---

## gobi space warp

Selects the active Space. Once selected, commands can run without `--space-slug`.

```bash
# Interactive selection
gobi space warp

# Specify slug directly (no interactive needed)
gobi space warp changbal
```

> **Note**: `warp` only works correctly in an interactive terminal.
> In automation environments, specify `--space-slug` directly on each command.

### --space-slug Global Option

You can specify `--space-slug` directly on any command without running `warp` first:

```bash
gobi space list-threads --space-slug changbal
gobi space create-thread --space-slug gobi --title "Title"
```

---

## gobi space list-threads

Lists Threads in a Space.

```bash
gobi space list-threads --space-slug <slug>
gobi space list-threads --space-slug <slug> --limit 5
gobi space list-threads --space-slug <slug> --json
```

### Plain Output vs JSON Output Comparison

**Plain output:**
```
Threads (9 items):
- [123] "Should I keep my current job?" by Changsoo Park (2 replies)
- [214] "[TMI] The most useless thing during today's presentation..." by Minsuk Kang (1 replies)
```

**JSON output (additional info):**
```json
{
  "id": 123,
  "title": "...",
  "richText": [...],          ← formatted text
  "topics": [                 ← AI-classified topic tags
    {"name": "AI", "slug": "ai"}
  ],
  "replyCount": 2,
  "primaryVault": {...},      ← author's Brain info
  "editedAt": null,
  "createdAt": "2026-03-16T..."
}
```

### Pagination

```bash
# Next page (cursor value is the date of the last item from previous response)
gobi space list-threads --space-slug gobi \
  --cursor "2026-03-28T00:27:27.492Z"
```

---

## gobi space get-thread

Retrieves a specific Thread's content and all its Replies.

```bash
gobi space get-thread <threadId> --space-slug <slug>
gobi space get-thread <threadId> --space-slug <slug> --limit 10
```

### Practice Results

```bash
gobi space get-thread 123 --space-slug changbal

# Output:
# Thread: Should I keep my current job?
# By: Changsoo Park on 2026-03-16T20:22:21.752Z
#
# [post content]
#
# Replies (2 items):
#   - Jin Young Kim: I can relate... (2026-03-19T...)
#   - Minsuk Kang: I'm at war with AI. Lol (2026-03-17T...)
```

---

> **Next**: [thread-management.en.md](thread-management.en.md)
> **Author**: Changsoo (with Claude Code)
> **Methodology**: VibeLearn AI v2.0
