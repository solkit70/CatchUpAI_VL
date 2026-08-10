---
title: "Appendix D — A little deeper (you don't have to do this)"
created: 2026-08-10 12:35:00
author:
  - "Claude Code"
tags:
  - vibecoding
  - vibelearn-ai
  - appendix
---

> 🌐 [한국어](04-appendix-advanced.md) · **English**

## Appendix D — A little deeper

**You don't have to read this.** Following just the main text is enough to use VibeLearn AI without any trouble.

This document is for two kinds of people. One is someone who got **anxious meeting hard words** while looking up install instructions online. The other is someone who wants to **modify this method themselves or share it with others.**

## Why it was pulled out of the main text

The official instructions in the VibeLearn AI repository include things like this.

```
powershell -ExecutionPolicy Bypass -File scripts/install-hooks.ps1
pip install -r requirements.txt
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

Seeing this the first time makes you think "do I have to do all this?" and gives up. **But the learner needs none of it.**

This is for **the people who fix and maintain this method itself.** It's for keeping other files in sync when the instructions (`CLAUDE.md`) are edited, and for auto-translating the English version. The official guide itself says:

> "If you're just downloading and using the template files, you can skip this."

What you need to do is only up to **getting the folder, opening it, and saying what you want to learn.**

## What each thing is (only if curious)

| The word you see | What it is | Does the learner need it? |
|---|---|---|
| `install-hooks.ps1` | Installs a device that auto-runs checks/cleanup when you save a file | ❌ Not needed |
| `pip install -r requirements.txt` | Installs Python parts used for auto-translation | ❌ Not needed |
| `ANTHROPIC_API_KEY` | A key used to run auto-translation | ❌ Not needed |
| `Git`, `clone` | Tools for fetching a repository and managing change history | 🔸 Not needed (ZIP works) |
| `Node.js`, `npm` | Tools for running a different kind of program | ❌ **Not used at all in this project** |

## If you want to use a different AI tool

This guide is written around **VS Code + Claude Code.** If you already use a different tool, that works too. VibeLearn AI isn't tied to a specific AI.

Inside the folder there's a per-tool instruction file, and **the contents are all the same.**

| Your tool | The file it reads |
|---|---|
| Claude Code | `CLAUDE.md` |
| Codex | `AGENTS.md` |
| Gemini CLI | `GEMINI.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |

They're **the same content copied under different names.** Switch tools and it proceeds the same way.

> ⚠️ That said, **just chatting on a website** (claude.ai, ChatGPT web) doesn't work well. It can't read and write files directly, so you have to copy-paste every time. The official guide too says it "causes time waste from copy-pasting."

## One convenience feature (optional)

If you use Claude Code, you can turn on a helper that automates making folders and finding files a bit more. **It all works the same without it.**

If you'd like, ask the AI like this.

```
Please register the claude-skill in extras.
```

## If you want to share what you made

As your study results pile up, they help others too. There are several ways to share.

**The simplest** is to zip your subject folder inside `Topics` and send it whole. The recipient opens it in VS Code and can see it as is.

**Putting it on GitHub** is another way, but you'll need to learn an account and how to use it separately. No rush.

## If you're curious about the method itself

The VibeLearn AI repository has the full explanation. But **it's substantial and has many developer examples.** No need to read it in a hurry.

- Repository: https://github.com/solkit70/VibeLearn-AI
- Intro video: [VibeLearn AI intro](https://youtu.be/KAcTebGpU5M)

This method is open so you can **use and modify it freely as long as you credit the source.**

## Once more

**You don't have to do any of what's here.** Following just the main text (chapters 3 and 4) is enough to use VibeLearn AI.

← Back: [First success — a result in 5 minutes](03-first-win.en.md)
