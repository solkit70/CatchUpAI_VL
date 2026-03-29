# GOBI CLI — Session Management Guide

> **Module**: M2 — Brain & Session Command Mastery
> **Written**: 2026-03-29
> **Version**: GOBI CLI v0.6.15

---

## What is a Session?

A **1:1 AI conversation session with a Brain**, started by `gobi brain ask` and continued via `gobi session reply`.

```
gobi brain ask  →  Session created  →  gobi session reply  →  continue conversation
```

---

## Session Commands (v0.6.15 Status)

### gobi session list

```bash
gobi session list            # list your Sessions
gobi session list --limit 5  # show only 5
```

> ⚠️ **v0.6.15 Issue**: Returns HTTP 404 — API endpoint mismatch

### gobi session get

```bash
gobi session get <sessionId>             # view Session content
gobi session get <sessionId> --limit 10  # show only 10 messages
```

> ⚠️ **v0.6.15 Issue**: Returns HTTP 404

### gobi session reply

```bash
gobi session reply <sessionId> --content "follow-up question"
```

> ⚠️ **v0.6.15 Issue**: Returns HTTP 404

---

## Session Creation Flow (brain ask)

```bash
# 1. Create Session
gobi brain ask \
  --vault-slug <vaultSlug> \
  --question "first question" \
  --json

# Check sessionId in JSON response:
# "session": {
#   "id": 677,                                        ← numeric ID
#   "sessionId": "9b73ebfd-f32b-4171-b411-25c56f507ab1"  ← UUID
# }

# 2. Continue conversation (when working normally)
gobi session reply 677 --content "Tell me more..."

# 3. Review conversation (when working normally)
gobi session get 677
```

---

## v0.6.15 Issue Details

### Issue Summary

| Command | Expected | Actual Result |
|---------|----------|---------------|
| `gobi session list` | Return Session list | HTTP 404 |
| `gobi session get <id>` | Return Session content | HTTP 404 |
| `gobi session reply <id>` | Send reply | HTTP 404 |
| `gobi brain ask` | Create Session | ✅ Works normally |

### Error Messages

```
Error: API error (HTTP 404): Cannot GET /chat/my-sessions?limit=20
Error: API error (HTTP 404): Cannot GET /chat/677?limit=20
Error: API error (HTTP 404): Cannot POST /chat/677/reply
```

### Root Cause Analysis

- `gobi brain ask` → Session **creation succeeds** (IDs 677, 678 confirmed returned)
- Session query/reply API endpoints appear to have changed server-side
- CLI v0.6.15 is using outdated endpoints

### Workarounds

1. **Web platform**: https://www.gobispace.com → manage Sessions from the Session menu
2. **GitHub Issues**: Report at https://github.com/gobi-ai/gobi-cli/issues

---

## Correct session reply Option (Roadmap Correction)

The Roadmap listed `--message` flag, but the actual option is `--content`:

```bash
# ❌ Incorrect example from Roadmap
gobi session reply <id> --message "content"

# ✅ Correct option
gobi session reply <id> --content "content"
```

---

> **Author**: Changsoo (with Claude Code)
> **Methodology**: VibeLearn AI v2.0
