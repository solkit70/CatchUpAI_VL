# GOBI CLI — Complete End-to-End Workflow

> **Module**: M4 — Real-World Workflow + Capstone
> **Written**: 2026-03-29
> **Version**: GOBI CLI v0.6.15

---

## Workflow Overview

A real-world scenario connecting every command learned in M1~M3.

```
Auth check → Brain search/query → Space Thread post → Brain update broadcast
    ↓              ↓                    ↓                      ↓
auth status   brain search        create-thread           post-update
              brain ask           create-reply            list-updates
```

---

## Scenario: "Learning Completion Announcement + Team Share" Workflow

### Step 1: Verify Authentication

```bash
gobi auth status

# Output:
# Authenticated
# User: Changsoo Park (solkit70@gmail.com)
# Vault: gobi-cli-study
```

**M4 Practice Result**: Authentication OK ✅

---

### Step 2: Search Brains to Find Relevant Knowledge

```bash
gobi brain search --query "GOBI CLI"

# Output:
# Brain Search Results:
# 1. [gobi-cli-study] GOBI CLI Study Brain  ← our Brain!
#    Similarity: 0.911
#    By: Changsoo Park
#    Tags: gobi-cli, learning, vibelearn-ai, cli-tool
#
# 2. [gobi-brain] Gobi Brain
#    Similarity: 0.743
#
# 3. [changbal-brain] Changbal Brain
#    Similarity: 0.512
```

**Key Finding**: Our published `gobi-cli-study` Brain ranks **#1 with similarity 0.911** ✅
→ Confirms BRAIN.md content was correctly indexed

---

### Step 3: Query Brain (Create AI Conversation Session)

```bash
gobi brain ask \
  --vault-slug gobi-cli-study \
  --question "What GOBI CLI commands are covered in this brain?" \
  --json

# Response:
# {
#   "id": 679,
#   "sessionId": "uuid-...",
#   "answer": "This brain covers the following GOBI CLI commands:
#     1. gobi auth (login/status/logout)
#     2. gobi brain (search/ask/publish/post-update...)
#     3. gobi space (list/warp/list-threads/get-thread/create-thread...)
#     4. gobi session (list/get/reply - v0.6.15 issues noted)
#     ...",
#   "vaultSlug": "gobi-cli-study",
#   "createdAt": "2026-03-29T..."
# }
```

**Result**: Session 679 created ✅ — Brain accurately answered M1~M3 content

> **Note**: `session list/get/reply` have HTTP 404 issues in v0.6.15. Sessions created by Brain ask
> can be viewed at gobispace.com web platform.

---

### Step 4: Post Thread to Space Announcing Completion

```bash
gobi space create-thread \
  --space-slug changbal \
  --title "GOBI CLI M4 Capstone: End-to-End Workflow Complete" \
  --content "Completed the full GOBI CLI learning journey through M1~M4 Capstone. 🎉

What I learned:
- M1: Install/Auth/Core Concepts (Vault/Space/Brain/Thread/Session)
- M2: Brain search, BRAIN.md publishing, Brain Updates CRUD
- M3: Full Space/Thread CRUD (8 commands)
- M4: End-to-End workflow + Quick Reference

All outputs: https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/GOBI-CLI

Learned with VibeLearn AI v2.0 methodology — anyone can follow along with these materials." \
  --json

# Response:
# {
#   "id": 735,
#   "title": "GOBI CLI M4 Capstone: End-to-End Workflow Complete",
#   "replyCount": 0,
#   "createdAt": "2026-03-29T..."
# }
```

**Result**: Thread 735 created ✅

---

### Step 5: Broadcast Completion via Brain Update

```bash
gobi brain post-update \
  --vault-slug gobi-cli-study \
  --content "🎓 GOBI CLI Learning — M4 Capstone Complete!

All modules done:
✅ M1: Setup/Auth/Core Concepts
✅ M2: Brain & Session Mastery
✅ M3: Space & Thread Collaboration
✅ M4: Real-World Workflow + Quick Reference

Learning outputs are publicly available on GitHub.
Organized systematically with VibeLearn AI v2.0. 💪"

# Result: Update posted successfully ✅
```

---

## Full Workflow Summary

```
1. gobi auth status              → verify authentication
2. gobi brain search --query ... → discover relevant Brains
3. gobi brain ask --vault-slug   → AI query (creates Session)
4. gobi space create-thread      → post team-share Thread
5. gobi brain post-update        → broadcast Brain feed update
```

**5 commands, 5 steps — the core GOBI CLI workflow** ✅

---

## Automation Script Example

Repetitive tasks can be automated with a shell script:

```bash
#!/bin/bash
# gobi-daily-check.sh — run every morning

VAULT="gobi-cli-study"
SPACE="changbal"
DATE=$(date +%Y-%m-%d)

echo "=== GOBI Daily Check: $DATE ==="

# 1. Auth check
echo "[1] Auth status:"
gobi auth status

# 2. Latest Brain updates
echo ""
echo "[2] Latest Brain Updates:"
gobi brain list-updates --vault-slug $VAULT --limit 3

# 3. Latest Threads
echo ""
echo "[3] Latest Threads:"
gobi space list-threads --space-slug $SPACE --limit 5

echo ""
echo "=== Done ==="
```

---

## Troubleshooting Quick Reference

| Symptom | Cause | Solution |
|---------|-------|----------|
| `session list/get/reply` → HTTP 404 | v0.6.15 server endpoint mismatch | Check at gobispace.com web |
| `gobi init` → "User force closed the prompt" | Non-interactive environment | Run in interactive terminal |
| Low Brain search similarity | Language mismatch (English query on Korean Brain) | Match query language to Brain language |
| Error without `--space-slug` | `gobi space warp` not run | Specify `--space-slug` directly on each command |

---

> **Next**: [quick-reference.en.md](quick-reference.en.md)
> **Author**: Changsoo (with Claude Code)
> **Methodology**: VibeLearn AI v2.0
