---
title: "Download VibeLearn AI"
created: 2026-08-10 11:50:00
author:
  - "Claude Code"
tags:
  - vibecoding
  - vibelearn-ai
  - setup
---

> 🌐 [한국어](01-get-vibelearn.md) · **English**

## Download VibeLearn AI

You have all the tools. Now we get **VibeLearn AI.**

VibeLearn AI is not a program. It's a **method for learning systematically with AI and leaving behind materials the next person can use.** What you actually get is a bundle of instruction files (one folder), and the AI reads those instructions to guide you.

**Time**: 10 minutes
**Cost**: Free
**No installer** — you're just downloading a folder

> 💡 **If you prefer video over text** — you can first watch a video that introduces what VibeLearn AI is.
> 👉 [VibeLearn AI intro video](https://youtu.be/KAcTebGpU5M)

## What you can relax about

Look up the install instructions for this project and you may meet hard words. Let's settle them first.

| Do you need this? | Answer |
|---|---|
| Installing a program | ❌ No. Get one folder and you're done |
| A Git / GitHub account | ❌ Not needed (we show the ZIP path) |
| Python, Node.js, etc. | ❌ Not needed |
| Typing commands | ❌ You don't have to |
| Studying this method | ❌ **Not needed.** One line — "I want to learn ○○" — and the AI takes it from there |

> Look up this project's install instructions online and you'll see things like `pip install`, `install hook`, `set API key`. **Those are for the people who build and maintain this method, not for the person learning.** If you're curious, they're collected in [A little deeper](04-appendix-advanced.en.md).

## Step 1 — Get it (just one of these)

### Method A — Get it as a ZIP (recommended, simplest)

You don't need to know Git, and no account is required.

① Go to this address in your browser.

```
https://github.com/solkit70/VibeLearn-AI
```

② Press the **green Code button** near the top-right of the screen.

③ In the list that drops down, press **Download ZIP** at the bottom.

④ The file downloads. Its name looks like `VibeLearn-AI-main.zip`.

⑤ **Double-click the downloaded file to unzip it.**

- Windows: right-click the file and choose **Extract All.**
- Mac: double-clicking unzips it automatically.

⑥ If the unzipped folder is named `VibeLearn-AI-main`, **rename it to `VibeLearn-AI`** (just remove the trailing `-main`).

⑦ Put that folder **next to the working folder you made earlier.** Inside your Documents folder is good.

> ✅ **You'll know it worked** — inside your Documents folder there's a folder named `VibeLearn-AI`, and inside it you see things like `README.md` and `templates`.

### Method B — Get it with Git (only if you already use Git)

If you don't know what Git is, **use Method A.** The result is the same.

```
git clone https://github.com/solkit70/VibeLearn-AI.git
```

## Step 2 — Open it in VS Code

① Open VS Code.

② In the top menu, choose **File → Open Folder...**

③ Choose the **`VibeLearn-AI` folder** you just got and open it.

④ If a window asks "Do you trust the authors of the files in this folder?" press **Yes, I trust the authors.**

> ✅ **You'll know it worked** — the name `VIBELEARN-AI` shows at the top-left of VS Code, and a list of files and folders appears below it.

## Step 3 — Look around the folder (3 min)

Seeing many files may feel overwhelming. **You only need to know two things.** You won't need to open the rest.

| What | What it does | Do I open it? |
|---|---|---|
| `CLAUDE.md` | **The instructions given to the AI.** The AI reads this and guides you | ❌ No need to open it |
| the `templates` folder | Forms the AI uses when making a plan | ❌ No need to open it |
| `README.md` | The full explanation of this method (a long read) | 🔸 Only if curious |
| `GETTING_STARTED.md` | Quick-start guide (a long read) | 🔸 Only if curious |
| the `Topics` folder | **Appears here once you start studying.** It's not there yet | ✅ Later this becomes your workspace |

The most important is **`CLAUDE.md`.** This file tells the AI "help this person in this way." You don't need to read it — **the AI reads it.**

> 💡 **Why do I have to download a folder?**
> Because the AI needs to be able to read these instructions. If you only tell the AI "help me the VibeLearn AI way" in words, the AI doesn't know exactly what that is. Download the folder and keep it open, and the AI reads it directly and follows it.

## Step 4 — Confirm the AI read the instructions (2 min)

① Press the **Claude icon** on the vertical bar on the left.

② Type this exactly in the box and press Enter.

```
Read the CLAUDE.md in the currently open folder,
and tell me in three sentences what kind of method VibeLearn AI is.
```

③ If the AI asks whether it may read the file, press **Allow.**

④ The AI gives an answer explaining VibeLearn AI.

> ✅ **If you got this far, it worked.** The AI has read the instructions and is ready to help you that way.

## If you got this far

Getting it is done. To sum up:

| Folder | What |
|---|---|
| `my-ai-work` | The practice folder you made earlier (not used now) |
| `VibeLearn-AI` | **The folder currently open. From now, you study here** |

Now it's time to **start your first Topic.** You'll be surprised — one sentence does it.

→ Next: [Start your first Topic](02-first-topic.en.md)

## When it doesn't work

**I don't see the green Code button**
If the screen is narrow the button moves. Widen the browser window, or scroll up a little.

**I unzipped it and there's another folder inside the folder**
Common. Sometimes there's `VibeLearn-AI-main` inside `VibeLearn-AI-main`. The **side where `README.md` is directly visible** is the real folder. Pull that inner one out and use it.

**The AI says "I can't find CLAUDE.md"**
You likely opened the wrong folder. Check that `VIBELEARN-AI` shows at the top-left of VS Code and that `CLAUDE.md` is below it.

**I forgot to rename the folder**
It's fine. It works with the name `VibeLearn-AI-main` too. You can rename it later.

More situations are collected in the [when-you-get-stuck document](../03-Setup-Environment/04-troubleshooting.en.md).
