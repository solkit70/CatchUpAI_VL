# VibeLearn AI — 30-Minute Quick Start Guide
> **[<- Korean Version](quick-start-30min.md)**


**Created**: 2026-02-26
**Audience**: People encountering VibeLearn AI for the first time
**Goal**: Follow this guide and start your first learning session in 30 minutes

---

## Core Message

> **You don't need to learn this methodology.**
> Just saying "I want to learn Python basics" is enough.
> AI handles the rest.

**Design principle**: VibeLearn AI is designed to minimize the entry barrier for first-time users.
If AI isn't handling things automatically, it's not working as designed →
Let us know via [Issues report](https://github.com/solkit70/VibeLearn-AI/issues).

---

## Before You Start: What You Need

| Required | Have it? |
|----------|----------|
| AI tool (VS Code + Copilot, Claude Code, Cursor, etc.) | ✅/❌ |
| A topic you want to learn (anything) | ✅/❌ |
| GitHub account (optional — not required) | ✅/❌ |

**Minimum requirement**: AI tool + topic you want to learn → Just these two things.

---

## Step 1: Get the VibeLearn AI Repository (5 min)

### Option A: GitHub Clone (recommended)

```bash
git clone https://github.com/solkit70/VibeLearn-AI.git
cd VibeLearn-AI
```

### Option B: ZIP Download

1. https://github.com/solkit70/VibeLearn-AI → Click the green Code button
2. Select "Download ZIP" → Extract
3. Folder name: `VibeLearn-AI/`

### Verify Completion

The following files should be present:
```
VibeLearn-AI/
├── README.md
├── GETTING_STARTED.md
└── templates/
    ├── topic_starter.md
    ├── roadmap_prompt_template.md
    └── daily_learning_prompt.md
```

---

## Step 2: Open `VibeLearn-AI/` Folder in Your AI Tool (2 min)

**VS Code + GitHub Copilot** (most common):
1. Open `VibeLearn-AI/` folder in VS Code
2. Confirm GitHub Copilot extension is installed (search "GitHub Copilot" in Extensions)
3. Open Copilot Chat panel (`Ctrl+Alt+I`)

**VS Code + Claude Code** (Extension):
1. Open `VibeLearn-AI/` folder in VS Code
2. Activate Claude Code extension panel

**Cursor**:
1. Open `VibeLearn-AI/` folder in Cursor

**Claude Code (CLI)**:
```bash
cd VibeLearn-AI
claude
```

---

## Step 3: Say What You Want to Learn (20 min)

Say this to AI:

```
"I want to learn Python basics."
```

**That's it.** AI handles the rest:

1. Collects learning information through a few questions (goals, period, environment, etc.)
2. Automatically generates `Topics/Python-Basics/` folder structure
3. Auto-generates Roadmap → saves to `vl_roadmap/`

Once AI has finished all setup, say:

```
"Start M1 learning."
```

AI creates the first module plan and begins learning. If it needs available time or other info, AI will ask directly.

---

## 30-Minute Timeline Summary

```
00:00 ─── Step 1: Get repository (5 min)
00:05 ─── Step 2: Open folder in AI tool (2 min)
00:07 ─── Step 3: "I want to learn Python basics." (20 min)
           └── AI automatically: collects questions → creates folders → generates Roadmap
00:27 ─── "Start M1 learning." → First learning session begins! 🎉
```

---

## From the Next Day Onward

Every day, open your AI tool and from the `VibeLearn-AI/` folder:

```
"Start today's learning."
```

AI reads the Roadmap and previous WorkLog to identify where you left off, and automatically continues from there. No other input needed.

---

## Common Sticking Points & Solutions

### "AI won't create folders"
- You need an AI tool with file system access like VS Code + GitHub Copilot, Claude Code, or Cursor
- ChatGPT web can't create files directly → you need an editor-integrated AI tool

### "Where do I write the WorkLog?"
- AI creates it automatically. You don't need to write it yourself.

### "I'm not sure if my progress is on track"
- Ask AI "How far have I gotten?" and it will figure it out for you.

---

## Once You're Comfortable: Tips for Higher Quality

Starting with a short one-liner is the best approach at first.
Once you're familiar with VibeLearn AI, you can provide more detailed context for higher quality.

```
# Basic (first-time user)
"I want to learn Python basics."

# Advanced (once familiar)
"I want to learn Python basics.
Background: 2 years of JavaScript, data analysis purpose, 3 weeks available, 2 hours daily."
```

More context → AI generates more accurate Roadmap + tailored learning plan

---

## Want to Learn More?

- [What is VibeLearn AI?](../../01-System-Overview/concepts/what-is-vibelearn-ai.en.md)
- [4-Phase Workflow](../../01-System-Overview/concepts/workflow-diagram.en.md)
- [FAQ](faq.en.md)
- [GETTING_STARTED.md](../../../../GETTING_STARTED.md) — Official detailed guide

---

**Author**: Claude with VibeLearn AI
**Verified**: This guide was verified during the actual VibeLearn-AI Topic learning process
