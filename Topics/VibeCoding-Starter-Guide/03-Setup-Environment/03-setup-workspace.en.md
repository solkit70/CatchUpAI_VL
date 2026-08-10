---
title: "Make and open a working folder"
created: 2026-08-10 11:05:00
author:
  - "Claude Code"
tags:
  - vibecoding
  - setup
---

> 🌐 [한국어](03-setup-workspace.md) · **English**

## Make and open a working folder

The AI is now inside VS Code. Now it's time to tell it **which drawer to work in.**

The AI doesn't rummage through any folder it likes. It **reads and writes files only in the folder you open for it.** So deciding on a working folder is also a safeguard.

**Time**: 5–10 minutes
**Cost**: Free

## Where to make it

Anywhere easy to find is fine. We recommend one of these.

| Computer | Recommended location |
|---|---|
| Windows | Inside the `Documents` folder (`C:\Users\yourname\Documents`) |
| Mac (macOS) | Inside the `Documents` folder |

> ⚠️ **It's best to avoid the Desktop.** As files pile up the screen gets cluttered, and it's easy to delete something by mistake.

> ⚠️ **Name the folder in English** is recommended. Korean names usually work too, but occasionally a tool has trouble. E.g. `my-ai-work`, `vibe-study`

## Step 1 — Make the folder

### If you use Windows

① Open **File Explorer** (the yellow folder icon) on the taskbar.

② Click **Documents** in the left list.

③ Right-click in an empty spot.

④ Choose **New → Folder.**

⑤ Type the folder name `my-ai-work` and press Enter.

### If you use a Mac (macOS)

① Open **Finder** (the blue face icon) at the bottom of the screen.

② Click **Documents** in the left list.

③ Right-click (or two-finger click) in an empty spot.

④ Choose **New Folder.**

⑤ Type the folder name `my-ai-work` and press Enter.

> ✅ **You'll know it worked** — an empty folder named `my-ai-work` shows inside your Documents folder.

## Step 2 — Open that folder in VS Code

① Open VS Code.

② In the top menu, choose **File → Open Folder...**

③ Find the `my-ai-work` folder you just made and **click once to select it.** You don't need to go inside it.

④ Press the **Select Folder** (Open) button at the bottom-right.

⑤ A window may ask "Do you trust the authors of the files in this folder?" Since you made it yourself, press **Yes, I trust the authors.**

> ✅ **You'll know it worked** — the folder name `MY-AI-WORK` shows at the top-left of VS Code. Below it is still empty. Having no files at all is normal.

## Step 3 — Let the AI see the folder (2 min)

Now check that the AI sees this folder.

① Press the **Claude icon** on the vertical bar on the left.

② Type this exactly in the box and press Enter.

```
What's the name of the folder currently open? Also tell me how many files are inside it.
```

③ If the AI names the `my-ai-work` folder and answers that there are no files, it's connected right.

> ✅ **If you got this far, it worked.** The AI can now see your folder.

## Step 4 — Try making your first file (3 min)

While we're at it, let's check that the AI **can also make a file.** This is the decisive difference from web chat.

① Type this in the Claude box.

```
Make a file called hello.md in this folder,
and write one line inside it: "My first step working with AI."
```

② The AI may **ask for permission** to make the file. Press **Allow** (Yes).

③ After a moment, `hello.md` newly appears in the left list of VS Code.

④ Click it to open, and the sentence you asked for is written there.

> ✅ **If you got this far, all the prep is done.** The AI actually made a file on your computer. From now, you only need to decide "what to make."

> 💡 **Why it asks for permission** — the AI usually asks first before making or editing a file. It's a safeguard so nothing changes without you knowing. Don't be scared — read what it's trying to do, then allow it.

## If you got this far — prep complete

Here's what you've done so far.

| Step | What you did |
|---|---|
| ① | Installed VS Code — a program for handling files |
| ② | Signed up for Claude and paid — the right to use the AI |
| ③ | Installed and logged in to Claude Code — attached the AI to VS Code |
| ④ | Made and opened a working folder — set the AI's workspace |
| ⑤ | Confirmed making a file — verified it actually works |

**Now you have all the tools.** Next comes what to do with them, and how — installing VibeLearn AI to proceed systematically.

→ Next: [Install VibeLearn AI and take your first step](../04-Setup-VibeLearn/README.en.md)

## When it doesn't work

**I clicked Open Folder but can't find my folder**
Common. In the address part at the top of the window, find **Documents** first and go in — it's inside there.

**The AI says "no folder is open"**
The folder isn't open. Redo step 2. The test is whether the folder name shows at the top-left of VS Code.

**The AI says it made a file but I don't see it in the left list**
Common. Press the **Refresh** icon (a circular arrow) at the top of the left list, or close and reopen VS Code.

More situations are collected in the [when-you-get-stuck document](04-troubleshooting.en.md).
