---
title: "When you get stuck (common things)"
created: 2026-08-10 11:20:00
author:
  - "Claude Code"
tags:
  - vibecoding
  - setup
  - troubleshooting
---

> 🌐 [한국어](04-troubleshooting.md) · **English**

## When you get stuck

While installing, you'll definitely snag somewhere at least once. **This isn't because you did something wrong.** Situations differ from computer to computer, so it happens to everyone. Even when we help side by side, the situations below come up almost every time.

The things here aren't malfunctions — they're **"common things that happen."** Go through them one by one and most clear up within a few minutes.

## First, try these three

Whatever you're stuck on, trying these three first solves more than half of it.

**One, close VS Code completely and reopen it.** Not closing the window — quitting the program and running it again. Right after installing, this alone often fixes it.

**Two, check your internet connection.** Just open any website in your browser.

**Three, wait a bit and try again.** Servers get busy sometimes. Try pressing again in 2–3 minutes.

## While installing

### I can't find the downloaded file

In the browser press `Ctrl + J` (Mac: `Command + J`) to see your downloads. The one at the top is the file you just got.

### The install window doesn't appear and nothing happens

It's often hidden behind another window. Look for a **flashing icon** on the taskbar at the bottom and click it. On a Mac, check for a bouncing icon in the Dock at the bottom.

### On a Mac it won't open, saying "unidentified developer"

This is a check Apple does once for a program it hasn't seen. **Right-click the icon → Open** and it opens. You only need to do this the first time.

### It says "administrator privileges required"

Common on company or school computers, where you don't have permission to install programs. You'll need to **use a personal computer, or ask the administrator to install it.** This is a part we can't solve for you, so it needs checking in advance.

## When signing up / paying for Claude

### The signup confirmation email doesn't arrive

**Check your spam (junk) folder.** It's usually in there. If it's still missing after 5 minutes, press resend on the signup screen.

### I paid but it still shows as free

Payment can take a few minutes to reflect. After a moment, try **logging out and back in** at claude.ai.

### My card is declined

It may be a card with overseas payments blocked. Check that **overseas payments are allowed** in your card's app or with customer service. Trying a different card is another option.

## When installing / logging in to Claude Code

### I search Claude Code and nothing appears

Close VS Code completely and reopen it. If it still doesn't show, check your internet connection. Also check you typed `Claude Code` exactly, space and all.

### Several similar names appear and I don't know which to pick

Pick the one whose maker is **Anthropic.** The maker's name is written small under the extension name.

### The browser won't open when I try to log in

Often an address (link) shows inside VS Code too. Copy that address and paste it into the browser's address bar — it works the same.

### I logged in in the browser but it doesn't return to VS Code

Check whether the browser has a button or window like "Open in VS Code." If so, press **Allow.** If it still doesn't work, close and reopen VS Code and log in once more.

### It says "a subscription is required"

The paid subscription isn't reflected yet. Check your plan at claude.ai. If you just paid, try again in a few minutes.

### It says "usage exceeded"

**Not a malfunction.** Each plan has a set amount you can use within a time window. Heavy use means waiting a bit. After some time you can use it again.

When this happens, take a break. If you record what you did today (WorkLog), it's easy to continue next time.

## When opening a folder and working

### I clicked Open Folder but can't find my folder

In the address part at the top of the window, find **Documents** first and go in — it's inside there. If you don't remember where you made it, you can search for the folder name (`my-ai-work`).

### The AI says "no folder is open"

The folder isn't open. The test is whether the **folder name shows at the top-left** of VS Code. If not, redo File → Open Folder.

### The AI says it made a file but I don't see it in the list

Press the **Refresh icon** (a circular arrow) at the top of the left list. If it still doesn't show, closing and reopening VS Code brings it up.

### The AI keeps asking for permission. It's annoying — can I turn it off?

**Asking is normal and safe.** It's the step where the AI gets confirmation before editing your files. Once you're used to it, you'll see at a glance what it's about to do, and allow it then.

At first, that asking step is actually **a chance to learn what the AI is doing.**

### I deleted a file by mistake, or something changed oddly

Don't panic. Just tell the AI.

```
Please undo what you just changed.
```

You can also undo in VS Code with `Ctrl + Z` (Mac: `Command + Z`).

## When it still doesn't work

If you're stuck even after all this, **don't wrestle with it alone for long.** Installation is a threshold you cross once, and it's usually something that finishes with 5 minutes of help.

When you ask for help, sharing these three makes it much faster.

1. **Which step you're stuck at** (e.g. "the Claude Code login step")
2. **What the screen says** — a photo or screenshot is best
3. **What kind of computer** (Windows / Mac / Chromebook)

You can find the contact point at **Catch Up AI** (https://catchupai.net/).

## Good to know in advance

**Chromebooks don't work with this method.** As mentioned at the top of chapter 3, VS Code can't be installed this way on a Chromebook. Check in advance before the session.

**Company/school computers may block installation.** Using a personal computer is more comfortable.

**You need the internet.** The AI uses the internet every time it makes an answer. If the connection is unstable, answers may be slow or cut off.
