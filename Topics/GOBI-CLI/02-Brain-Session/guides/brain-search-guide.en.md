# GOBI CLI — Brain Search & Ask Guide

> **Module**: M2 — Brain & Session Command Mastery
> **Written**: 2026-03-29
> **Version**: GOBI CLI v0.6.15

---

## 1. gobi brain search

Searches public Brains using **text + semantic similarity**.

### Basic Usage

```bash
gobi brain search --query "keyword"
gobi brain search --query "keyword" --json    # JSON output
```

### Practice Results (2026-03-29)

```bash
# English query
gobi brain search --query "getting started"
# → highest similarity: 0.409 (relatively low)

# Korean query
gobi brain search --query "건강 앱"
# → highest similarity: 0.605 (high — increases with content match)

# Tech query
gobi brain search --query "CLI tool"
# → highest similarity: 0.396
```

### Output Structure (JSON)

```json
{
  "success": true,
  "data": [
    {
      "vault": {
        "id": 70,
        "vaultId": "happy-light-dz3ttx",
        "name": "Happy Light",
        "description": "...",
        "tags": ["profile"]
      },
      "owner": {
        "id": 25,
        "name": "이문기"
      },
      "similarity": 0.605
    }
  ]
}
```

### Key Insights

| Finding | Detail |
|---------|--------|
| **Semantic search** | Ranked by meaning similarity, not keyword match |
| **Language match matters** | Korean queries return much higher similarity for Korean Brains |
| **Always returns 20** | Fixed 20 results, no pagination |
| **Public Brains only** | Private Brains are not searchable |

---

## 2. gobi brain ask

Ask a specific Brain a question, **creating a new Session**.

### Basic Usage

```bash
gobi brain ask \
  --vault-slug <vaultSlug> \
  --question "your question"

# Options
gobi brain ask \
  --vault-slug <vaultSlug> \
  --question "question" \
  --mode auto        # auto (default) or manual
```

### Practice Results

```bash
gobi brain ask \
  --vault-slug changsoo_vault-df7y0c \
  --question "What is this brain about?" \
  --json

# Response:
{
  "session": {
    "id": 677,
    "sessionId": "9b73ebfd-f32b-4171-b411-25c56f507ab1",   ← UUID
    "mode": "manual",
    "messageCount": 0
  },
  "userMessage": {
    "id": "13a3d6a7-...",
    "content": "What is this brain about?",
    "role": "user"
  }
}
```

### Important: Session ID Formats

`gobi brain ask` returns **two ID types**:

| Field | Format | Example |
|-------|--------|---------|
| `session.id` | Numeric | `677` |
| `session.sessionId` | UUID | `9b73ebfd-f32b-4171-b411-25c56f507ab1` |

> ⚠️ See the issues section for which ID format works with `gobi session reply/get`

### How to Find vault-slug

```bash
# The vaultId field in brain search results is the vault-slug
gobi brain search --query "my name" --json
# → use data[].vault.vaultId value
```

---

## 3. Known Issues (v0.6.15)

### ⚠️ session list / get / reply → HTTP 404

```bash
gobi session list
# Error: API error (HTTP 404): Cannot GET /chat/my-sessions?limit=20

gobi session get 677
# Error: API error (HTTP 404): Cannot GET /chat/677?limit=20

gobi session reply 677 --content "..."
# Error: API error (HTTP 404): Cannot POST /chat/677/reply
```

**Suspected cause**: CLI v0.6.15 session API endpoints don't match server
**Workaround**: View created sessions directly on gobispace.com web platform
**Reporting**: https://github.com/gobi-ai/gobi-cli/issues

---

> **Next**: [session-management.en.md](session-management.en.md)
> **Author**: Changsoo (with Claude Code)
> **Methodology**: VibeLearn AI v2.0
