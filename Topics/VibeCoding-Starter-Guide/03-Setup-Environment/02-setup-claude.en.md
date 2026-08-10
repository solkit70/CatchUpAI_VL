---
title: "Sign up for Claude and install Claude Code"
created: 2026-08-10 10:50:00
author:
  - "Claude Code"
tags:
  - vibecoding
  - setup
---

> 🌐 [한국어](02-setup-claude.md) · **English**

## Sign up for Claude and install Claude Code

Now we **attach the AI** to VS Code. We do two things.

First, create a **Claude** account and start a paid subscription. Claude is an AI you can talk to in plain language and give tasks to.

Second, install **Claude Code** in VS Code. Claude Code is the tool that lets Claude **read and write the folders and files on your own computer directly.** This is the key part — unlike just chatting on a website, it actually creates and edits your files.

**Time**: 20–30 minutes
**Cost**: A paid subscription is required (explained below)

## First — the cost, honestly

To use Claude Code, you need a **paid Claude subscription.** You can't use it for free. We say this up front rather than hiding it.

| What | Details |
|---|---|
| Why it's needed | Claude Code reading and writing your files goes beyond the free tier |
| How you pay | A **subscription** billed automatically each month (like Netflix) |
| How much | Plans come in several tiers, and **the price can change.** Check the current price shown on the signup screen yourself |
| Which one at first | You can start with the **lowest tier.** Raise it later if it's not enough |
| To stop | You can cancel any time. Even after canceling, you can use the rest of that month |

> 💡 **Check first** — some people already have a paid Claude subscription. Sometimes a company or school provides an account. It's worth checking before you pay.

> ⚠️ **If you're a minor student** — do the payment with a guardian. There's a step where you enter card details.

## Step 1 — Create a Claude account

① Open a browser and go to:

```
https://claude.ai
```

② On the screen, press **Sign up**. If you already have an account, press **Log in** and skip to step 3.

③ Enter an email, or press **Continue with Google** to sign up with a Google account.

> 💡 Signing up with Google is simpler. You don't have to make a new password.

④ If you signed up by email, check the confirmation email in your inbox and enter the code.

⑤ Answer a name and a few simple questions and signup is done.

> ✅ **You'll know it worked** — a screen where you can chat with Claude opens. There's a message box in the middle. You can even try sending "Hello."

## Step 2 — Start a paid subscription

① In the Claude screen, press your name or account icon at the **bottom-left.**

② Choose **Upgrade** or **Plans**.

③ A list of plans appears. You can start with the **lowest paid tier.**

④ Enter card details and pay.

> ✅ **You'll know it worked** — after payment, your current plan name shows in the account menu. A confirmation email also arrives.

> 💡 **How much you can use** — each plan has a daily or weekly usage limit. If you use a lot, you may have to wait a bit. **This isn't a malfunction; it's normal.** After some time you can use it again.

## Step 3 — Install Claude Code in VS Code

Now come back to VS Code.

① Open VS Code.

② On the **vertical bar on the left**, press the **icon of four squares.** That's where you install extensions (add-on parts that give new features). Hovering shows "Extensions."

③ In the search box at the top, type:

```
Claude Code
```

④ **Claude Code** appears at the top of the list. Confirm the maker is **Anthropic.** There may be other extensions with similar names.

⑤ Press the **Install** button. It takes a few seconds to a minute.

> ✅ **You'll know it worked** — the Install button disappears and turns into a gear icon or "Uninstall." A Claude icon newly appears on the vertical bar on the left.

## Step 4 — Log in to Claude Code

① Press the **Claude icon** newly added to the vertical bar on the left.

② A prompt to log in appears. Press **Sign in.**

③ A browser window opens automatically with the Claude login screen. Log in with the account from step 1.

④ If a window like "Allow opening in VS Code?" appears, press **Open** (Allow).

⑤ You return to VS Code automatically.

> ✅ **You'll know it worked** — a message box appears in the Claude screen inside VS Code. The login prompt is gone.

## Step 5 — Confirm it's connected (2 min)

The surest check is to **talk to it.**

① In the Claude box inside VS Code, type this exactly and press Enter.

```
Hello. Are you working on my computer right now? Answer in one sentence.
```

② After a moment, an answer comes back.

> ✅ **If you got this far, it worked.** If the AI answered inside VS Code, both the install and the login are done right.

## If you got this far

The AI is now inside VS Code. But you haven't yet given it a **folder to work in.** The step of telling the AI "which drawer to open" remains.

→ Next: [Make and open a working folder](03-setup-workspace.en.md)

## When it doesn't work

**I search Claude Code and nothing appears**
Common. Close VS Code completely and reopen it. If it still doesn't show, check your internet connection.

**The browser won't open when I try to log in**
Common. Often an address (link) shows inside VS Code too. You can copy that address and paste it into the browser's address bar.

**I logged in but it says "a subscription is required"**
The step-2 paid subscription isn't set yet. Log in at claude.ai and check your plan. If you just paid, try again in a few minutes.

**It says something like "usage exceeded"**
Not a malfunction. Each plan has a usage limit, so heavy use means waiting a bit. After some time you can use it again.

More situations are collected in the [when-you-get-stuck document](04-troubleshooting.en.md).
