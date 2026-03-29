# GOBI CLI — Installation & Auth Guide

> **Module**: M1 — Setup & Auth & Core Concepts
> **Written**: 2026-03-29
> **Environment**: Windows 11, Node.js v22.15.0, npm v11.6.2
> **GOBI CLI Version**: v0.6.15

---

## Prerequisites

| Item | Min Version | Check Command | Status |
|------|-------------|---------------|--------|
| Node.js | 18+ | `node --version` | v22.15.0 ✅ |
| npm | - | `npm --version` | v11.6.2 ✅ |
| GOBI account | - | gobispace.com | ✅ |

---

## Step 1: Install

```bash
# Install globally
npm install -g @gobi-ai/cli

# Verify installation
gobi --version    # → 0.6.15
gobi --help       # → full command list
```

> **Note**: A `prebuild-install@7.1.3 deprecated` warning may appear, but installation completes normally.

---

## Step 2: Check Authentication

```bash
# Check auth status first
gobi auth status

# Output if already logged in:
# Authenticated as Changsoo Park (solkit70@gmail.com)
# Run 'gobi init' to set up, then 'gobi space warp' to select a space.

# If not logged in:
gobi auth login    # opens browser → complete login
```

---

## Step 3: Initialize Vault (gobi init)

```bash
# Navigate to your project folder
cd <project-folder>

# Initialize (interactive)
gobi init
```

**Interactive flow**:
```
? How would you like to set up your vault?
❯ Select an existing vault    ← use existing vault
  Create a new vault          ← create new vault

# When "Create a new vault" is selected:
? Vault name: gobi-cli-study
→ Created vault "gobi-cli-study" (gobi-cli-study)
→ Vault set to "gobi-cli-study" (gobi-cli-study)
→ Updated .gobi/settings.yaml
→ Created BRAIN.md
```

**Files generated**:
```
<project-folder>/
├── .gobi/
│   └── settings.yaml    ← vaultSlug: gobi-cli-study
└── BRAIN.md             ← source file for brain publish (with frontmatter)
```

**BRAIN.md initial content**:
```markdown
---
title: gobi-cli-study
tags: []
description:
thumbnail:
prompt:
---
```

---

## Step 4: Logout (if needed)

```bash
gobi auth logout
```

---

## Quick Verification Checklist

```bash
node --version      # confirm v18+
gobi --version      # confirm installation
gobi auth status    # confirm authentication
ls .gobi/           # confirm settings.yaml exists (after gobi init)
```

---

> **Next**: [core-concepts.en.md](core-concepts.en.md)
> **Author**: Changsoo (with Claude Code)
> **Methodology**: VibeLearn AI v2.0
