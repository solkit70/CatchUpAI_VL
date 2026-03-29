# GOBI CLI — Quick Reference Card

> **Version**: GOBI CLI v0.6.15
> **Written**: 2026-03-29
> **Status**: Full command reference (M1~M4 complete)

---

## Auth

```bash
gobi auth login          # login (opens browser)
gobi auth status         # check current auth status
gobi auth logout         # logout
```

---

## Init

```bash
gobi init                # select vault + create BRAIN.md (interactive required)
```

> Config saved to `.gobi/settings.yaml` with `vaultSlug`

---

## Brain Commands

### Search & Query

```bash
# Brain search (semantic similarity)
gobi brain search --query "keyword"
gobi brain search --query "keyword" --json    # JSON output

# AI query to Brain (creates Session)
gobi brain ask --vault-slug <slug> --question "your question"
gobi brain ask --vault-slug <slug> --question "question" --json
```

### Publish

```bash
# Publish BRAIN.md (uses BRAIN.md in current directory)
gobi brain publish

# Unpublish
gobi brain unpublish
```

### Updates (team feed)

```bash
# Post update
gobi brain post-update --vault-slug <slug> --content "content"

# List updates (your own)
gobi brain list-updates --vault-slug <slug>
gobi brain list-updates --vault-slug <slug> --limit 5

# Edit update
gobi brain edit-update <updateId> --vault-slug <slug> --content "updated content"

# Delete update
gobi brain delete-update <updateId> --vault-slug <slug>
```

---

## Session Commands

> ⚠️ **v0.6.15 Known Issue**: `list/get/reply` all return HTTP 404
> → Use web platform (gobispace.com) instead

```bash
gobi session list                         # ⚠️ HTTP 404 (v0.6.15 issue)
gobi session get <sessionId>              # ⚠️ HTTP 404 (v0.6.15 issue)
gobi session reply <sessionId> \
  --content "reply content"              # ⚠️ HTTP 404 (v0.6.15 issue)
```

---

## Space Commands

### Space Navigation

```bash
# List Spaces
gobi space list
gobi space list --json

# Select active Space (interactive)
gobi space warp
gobi space warp <slug>    # specify directly

```

> 💡 **Tip**: Use `--space-slug` option to skip `warp`

### Thread Query

```bash
# Thread list
gobi space list-threads --space-slug <slug>
gobi space list-threads --space-slug <slug> --limit 10
gobi space list-threads --space-slug <slug> --json

# Pagination
gobi space list-threads --space-slug <slug> \
  --cursor "2026-03-28T00:27:27.492Z"

# Thread detail (body + Replies)
gobi space get-thread <threadId> --space-slug <slug>
gobi space get-thread <threadId> --space-slug <slug> --limit 20
```

### Thread CRUD

```bash
# Create Thread
gobi space create-thread \
  --space-slug <slug> \
  --title "title" \
  --content "body" \
  --json    # returns id

# Edit Thread
gobi space edit-thread <threadId> \
  --space-slug <slug> \
  --title "updated title" \
  --content "updated body"

# Delete Thread
gobi space delete-thread <threadId> --space-slug <slug>
```

### Reply CRUD

```bash
# Create Reply
gobi space create-reply <threadId> \
  --space-slug <slug> \
  --content "reply content" \
  --json    # returns id

# Edit Reply
gobi space edit-reply <replyId> \
  --space-slug <slug> \
  --content "updated content"

# Delete Reply
gobi space delete-reply <replyId> --space-slug <slug>
```

---

## Common Options

| Option | Description |
|--------|-------------|
| `--json` | JSON format output |
| `--limit N` | Limit number of results |
| `--cursor <value>` | Pagination cursor |
| `--space-slug <slug>` | Specify Space directly |
| `--vault-slug <slug>` | Specify Vault directly |

---

## BRAIN.md Structure

```markdown
---
title: <vault-slug>
tags: ["tag1", "tag2"]
description: one-line description
thumbnail: (optional) image URL
prompt: You are a ... assistant. Help users with ...
---

# Brain Title

[Brain body content — markdown format]
```

---

## Known Issues (v0.6.15)

| Issue | Severity | Description |
|-------|----------|-------------|
| `session list/get/reply` HTTP 404 | High | Server endpoint mismatch |
| `session update` command missing | Medium | Not implemented in v0.6.15 |
| `--message` option → `--content` | Low | Doc error (actual option is `--content`) |

---

## Actual IDs Confirmed in Practice

| Item | ID | Space |
|------|----|-------|
| Thread (M3 CRUD test) | 731 | changbal |
| Reply (M3 CRUD test) | 732 | changbal |
| Thread (M4 Capstone completion) | 735 | changbal |
| Brain Ask Session (M2) | 677 | gobi-cli-study |
| Brain Ask Session (M4) | 679 | gobi-cli-study |

---

## Installation

```bash
# Install
npm install -g @gobi-ai/cli

# Check version
gobi --version
# → 0.6.15

# Help
gobi --help
gobi <command> --help
```

---

> **Author**: Changsoo (with Claude Code)
> **Methodology**: VibeLearn AI v2.0
> **Related Modules**: M1~M4
