# M1 — Setup & Auth & Core Concepts

> **Module**: M1
> **Status**: ✅ Complete
> **Estimated Time**: 3-4 hours
> **Actual Time**: ~2 hours (2026-03-29)

---

## What You'll Learn

Install GOBI CLI for the first time, complete authentication, and understand the 5 core platform concepts.
By the end of this module, you'll be fully ready to use GOBI CLI.

---

## Learning Order (read in this order)

| # | Document | Description |
|---|----------|-------------|
| 1 | [concepts/installation-guide.en.md](concepts/installation-guide.en.md) | Step-by-step guide: install → authenticate → initialize vault |
| 2 | [concepts/core-concepts.en.md](concepts/core-concepts.en.md) | Vault / Space / Brain / Session / Thread core concepts + full command Quick Reference |

---

## M1 Key Summary

```
Install:   npm install -g @gobi-ai/cli  →  gobi v0.6.15
Auth:      gobi auth status  →  already logged in (Changsoo Park)
Init:      gobi init  →  created vault "gobi-cli-study"
             generated: .gobi/settings.yaml, BRAIN.md
```

**5 Core Concepts**:
```
Vault   → top-level container (= GitHub Org)
Space   → team collaboration area (= GitHub Repo)
Brain   → AI knowledge resource (= Wiki + AI)
Session → 1:1 conversation with Brain (= ChatGPT chat window)
Thread  → team discussion (= GitHub Issues)
```

---

## M1 DoD Checklist

- [x] `npm install -g @gobi-ai/cli` installed (v0.6.15)
- [x] `gobi auth status` — auth confirmed (Changsoo Park)
- [x] `gobi init` — vault "gobi-cli-study" created
- [x] Full command exploration via `--help`
- [x] `core-concepts.md` written
- [x] `installation-guide.md` written
- [x] Additional discovered commands documented (`sense`, `sync`)

---

## Previous / Next Module

| | Module | Link |
|--|--------|------|
| ◀ Previous | - | (M1 is the first module) |
| Next ▶ | M2 — Brain & Session Command Mastery | `../02-Brain-Session/README.en.md` |

---

> **Methodology**: VibeLearn AI v2.0
> **Author**: Changsoo (with Claude Code)
