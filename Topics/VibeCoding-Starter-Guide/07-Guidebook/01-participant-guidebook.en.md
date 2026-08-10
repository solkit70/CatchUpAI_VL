---
title: "Vibe Coding First Steps — Participant Guidebook"
created: 2026-08-10 18:40:00
author:
  - "Catch Up AI"
tags:
  - vibecoding
  - vibelearn-ai
  - guidebook
---

> 🌐 [한국어](01-participant-guidebook.md) · **English**

## Welcome

**It's fine if you don't know how to code. It's fine if you're not used to computers.**

This guide was made to set up an environment for working with AI on your own computer and take you all the way to actually making one thing.

A teacher in their 60s in Utah, USA started this way too. We helped set up their computer, and **within just a few days they made — themselves — an app that records their life story, organizes it into text, and turns it into a book.** Not because of special talent, but because the experience they'd built up in one field was already enough raw material.

This guide was made by **Catch Up AI** (https://catchupai.net/).

## Chapter 1 — What you'll be able to do with this guide

Follow through to the end and this is where you'll be.

| What | Result |
|---|---|
| An AI work environment on your computer | VS Code + Claude Code |
| The AI reads and writes your files | Not a conversation, but **stays as files** |
| A systematic way to proceed | VibeLearn AI |
| **One result from your own hand** | First success |

**Time**: 40 min – 1 hour to install, 30 minutes more to first success
**Cost**: a paid Claude subscription (details in chapter 3)

We seat three people together.

- **Students** — prepare talks or assignments with AI
- **Experienced people** — make what you want to make with your experience and knowledge
- **Civic-group workers** — organize scattered work materials and plan events

What you're doing differs, but **the tool and the method are the same.**

## Chapter 2 — What is vibe coding

### In one sentence

**You describe what you want in plain language, and the AI handles the details.** You decide what to make and whether it's right.

### It used to be

Making something on a computer took two things: **knowing what to make** (the person who worked a field for years knows best) and **the skill to make it** (years to learn). The problem was these two rarely landed in one person.

### Now it is

The second has shrunk. Say this and the AI makes it:

```
I want to make a health journal for the elderly folks in my neighborhood.
The text should be large, with only a few buttons.
```

**The first part — knowing what to make — is still the human's job.** And that's the part you already have.

### So does the AI do everything?

No. **The AI is not a magic wand.** Bolt on features without a plan and you end up in a state that's hard to fix. "First set a plan and build from step 1" is much better.

You don't need to become a developer, but you do need enough to **steer the AI.** That's the part this guide teaches.

### It's not only coding

The tool we'll install **reads and writes the folders and files on your computer directly.** So anything with files works — research, writing, organizing files, meeting notes, talk prep, learning, making.

### It's different from chatting with AI on a website

| | Chatting on a website | The way we'll install |
|---|---|---|
| Output | Text in a chat window | **Files in my folder** |
| When you close the window | Gone | **Still there** |
| To continue | Explain from scratch | **The AI reads the past files** |
| When it piles up | Nothing piles up | **It becomes your material** |

### AI is a coworker, not a tool

| Same situation | Used like a search box | Handed off like a coworker |
|---|---|---|
| Talk prep | "What is Liberation Day?" | "I'm preparing a 5-minute talk for middle schoolers — what should I decide first?" |
| Scattered files | "How do I organize well?" | "Look at the files in this folder and split them into decided and undecided." |
| Something to make | "How do I make an app?" | "I want to make an app like this. Set a plan first." |
| Work is done | (closes the window) | "Record what I did today." |

**What, why, how far.** Telling it these three is the core. Just explain like you would to the coworker next to you.

### Why is starting hard?

The stretch AI made fast is just one — picture a 100-mile highway where **only 5 miles were widened to 10 lanes.** But **the on-ramp into that stretch is still narrow.** This guide was made to walk that on-ramp together. **You only have to cross it once.**

> 💡 To see more: [Build with AI, made easy (for seniors)](https://youtu.be/bfpj7aetzhk) · [AI for civic-group workers](https://youtu.be/3wgTpWA55cY)
>
> **To watch it actually being done**: [I told it out loud and the AI made everything — a real AI meeting on Liberation Day ceremony planning with a civic group](https://youtu.be/3wgTpWA55cY) (36 min)
> A video capturing a whole online meeting with a civic-group person, **handling real work with AI right on the spot.** You can see exactly how the method in this guide is used in practice.
>
> Chapter in depth: [Chapter 2 detail](../02-What-Is-Vibe-Coding/README.en.md)

## Chapter 3 — Getting ready

### First — does your computer work?

| Your computer | Works? |
|---|---|
| Windows laptop/desktop | ✅ |
| MacBook / iMac (macOS) | ✅ |
| **Chromebook** | ❌ **Not with this method** |
| iPad / tablet / phone | ❌ |

> ⚠️ **If you use a Chromebook**, tell your facilitator in advance. We'll prepare a different computer or a separate method.

### The cost first

To use Claude Code you need a **paid Claude subscription.** Not free. We say it up front.

| Item | Details |
|---|---|
| How you pay | A subscription billed automatically each month (like Netflix) |
| How much | Several tiers, and **the price changes.** Check the current price on the signup screen |
| At first | You can start with the **lowest tier** |
| To stop | Cancel any time |

> 💡 **You may already be subscribed.** Sometimes a company or school provides an account — check before you pay.
> ⚠️ **If you're a minor student**, do the payment with a guardian.

### 3-1. Install VS Code (10–15 min, free)

VS Code is a free program for writing and editing text and files. **You don't need to learn VS Code itself.**

1. Type `https://code.visualstudio.com` in the browser
2. Press the **blue Download button** in the middle (the site picks the right one for your computer)
3. **Windows**: double-click the file → "Yes" → agree → Next → **Install**
   **Mac**: double-click the file → drag the icon **into the Applications folder** → double-click to open → "Open"

> ✅ **Success check** — a dark-colored window opens with a vertical bar of icons on the left.

For now you only need **two places**: the **vertical bar on the left** (where you install extensions) and the **wide area in the middle** (where file contents show).

### 3-2. Sign up for Claude + paid subscription (15–20 min)

1. Go to `https://claude.ai`
2. Press **Sign up**. **Continue with Google** is simplest
3. After signup, **your name/account icon at the bottom-left** → **Upgrade** or **Plans**
4. Pick the **lowest paid tier** and pay

> ✅ **Success check** — your current plan name shows in the account menu. A confirmation email arrives.
> 💡 If later it says "usage exceeded," **it's not a malfunction.** It's a plan limit; after some time it works again.

### 3-3. Install and log in to Claude Code (10 min)

Claude Code lets Claude **read and write your files directly.** This is the key part.

1. Open VS Code
2. On the **vertical bar on the left**, press the **icon of four squares** (extensions)
3. Type `Claude Code` in the search box
4. Confirm the maker is **Anthropic** and press **Install**
5. Press the new **Claude icon** on the left bar → **Sign in** → log in in the browser → **Allow**

> ✅ **Success check** — a message box appears in the Claude screen inside VS Code.

### 3-4. Make and open a working folder (10 min)

The AI reads and writes files **only in the folder you open.** It's also a safeguard.

1. Make a folder named `my-ai-work` inside your **Documents** folder
2. In VS Code, **File → Open Folder...** → select that folder
3. If a "trust the authors?" window appears, press **Yes, I trust the authors**

> ✅ **Success check** — `MY-AI-WORK` shows at the top-left of VS Code. Empty inside is normal.

### 3-5. Confirm it really works (3 min)

Type this exactly in the Claude box.

```
Make a file called hello.md in this folder,
and write one line inside: "My first step working with AI."
```

If the AI asks permission, press **Allow.** After a moment, `hello.md` appears in the left list.

> ✅ **If you got this far, the prep is done.** The AI actually made a file on your computer.
>
> 💡 **The AI asking permission is a safeguard** — so nothing changes without you knowing. Read what it's about to do, then allow it.

> Stuck? → [When you get stuck](../03-Setup-Environment/04-troubleshooting.en.md) (18 situations)

## Chapter 4 — Install VibeLearn AI and take your first step

### 4-1. Download (10 min, free)

VibeLearn AI is not a program but **a method for learning systematically with AI.** What you get is a bundle of instruction files (one folder).

**You can relax about**: program install ❌ · Git ❌ · Python ❌ · typing commands ❌ · **studying this method ❌**

1. Go to `https://github.com/solkit70/VibeLearn-AI`
2. **Green Code button** at the top-right → **Download ZIP**
3. Unzip → in the folder name `VibeLearn-AI-main`, remove the trailing `-main`
4. Put the folder inside your **Documents** folder
5. In VS Code, **File → Open Folder...** and open the `VibeLearn-AI` folder

> ✅ **Success check** — `VIBELEARN-AI` shows at the top-left, with `README.md`, `templates`, etc. below.

There are many files, but **you don't have to open any of them.** `CLAUDE.md` is the instructions given to the AI, and **the AI reads it.**

> 💡 If you prefer video over text: [VibeLearn AI intro video](https://youtu.be/KAcTebGpU5M)

### 4-2. Start your first Topic — one sentence does it

Type **what you want to do** in the Claude box.

```
I want to prepare a Liberation Day talk.
```
```
I want to learn to make a web page that presents my experience.
```
```
I want to learn how to organize our group's event materials.
```

The AI asks a few things. **Answer as best you know; if you don't know, "I'm not sure" is fine.**

> 💡 If answering is tedious, say **"Please ask me in multiple-choice form"** and it gives options.

Next the AI makes a **plan (Roadmap).** But before making it, it **asks first.**

> 1. Proceed as is / 2. Adjust timeframe / 3. Adjust scope

**It's a safeguard, not a malfunction.** If unsure, pick **"Proceed as is."**

### 4-3. First success — one result in 5 minutes

Pick **just one** of the three.

```
Please make a one-page web page introducing me.
My name is [your name], and I want to present [your interest].
```
```
Please organize today's to-dos. [three to-dos]
In order of importance, with time estimates, as a table.
```
```
Please organize what I should know about [a topic], simply, and save it as a file.
```

**If you don't like it, just say so.** "The colors are too dark, make them lighter." **Saying "please fix it" is the normal way to use this.**

> Detail: [Chapter 4 detail](../04-Setup-VibeLearn/README.en.md) · [A little deeper (appendix)](../04-Setup-VibeLearn/04-appendix-advanced.en.md)

## Chapter 5 — How to use it well

Even with the tools, **if your way of using them stays the same, nothing changes.**

### What's different from chatbot use

| | Used like a chatbot | The VibeLearn AI way |
|---|---|---|
| Yesterday's work | The AI doesn't know | **Reads records and continues** |
| When it ends | Unknown | Set in advance with a **DoD** (Definition of Done) |
| Output | Text in a chat window | **Stays as files** |
| Switch tools | From scratch | **Continues as is** |

**Chatbot-style isn't bad.** For something answered once and done, just ask. But for **work built up over many sittings**, make a Topic.

### Three ways to start well

**One — specify the goal and tell it.** What / for whom / how far / by when. Just what you know helps a lot.

**Two — make the name recognizable.** `Liberation-Day-Talk-Prep` (O) / `talk` (X). Hyphen instead of space.

**Three — write goals as "I can do."** "I get to know Liberation Day well" (X) → **"I can finish a 5-minute talk script and read it aloud"** (O)

### Three things to check in the plan

- [ ] There's an **estimated time**
- [ ] There's a **DoD** (completion criteria) as checkboxes
- [ ] Goals are written as **"I can do"**

If you don't like it, just say "there are too many steps, cut them in half."

### Why it asks twice

Once before making the plan, once each day when starting. **To keep the AI from deciding on its own and running off.** Fixing a plan takes 5 minutes; fixing something already made takes far longer.

> Detail: [Chapter 5 detail](../05-Using-VibeLearn/README.en.md)

## Chapter 6 — How to keep using it well

### Records are the AI's fuel

The AI forgets once a conversation ends. Yet working with VibeLearn AI, the AI knows yesterday. **Not because its memory is good, but because it reads the records you left yesterday.**

**You don't have to write it yourself.** When you finish the day, one line does it.

```
I got this far today. Please record it.
```

**Especially leave what got stuck.** Get stuck at the same spot next time and the AI tells you last time's fix.

### This actually happened

**It continues even after a four-day break.** Stopped on July 19, reopened on the 23rd, and didn't flounder over where to continue, because there was a record.

**It keeps getting faster.** The same task went 4.5 hours first → 4 hours second → 2–3 hours estimated next.

**The first time takes longest.** That's good news.

### Why "your own records"

Ask using only information anyone can search and you get an **answer like everyone else's.** But give your records and it's different.

> **Records make AI stronger. Your records make an AI that's yours.**

> 💡 [Records make AI stronger | Live #13 Summary](https://youtu.be/BJPB_YMWUcE)

### The retrospective is five minutes

The daily one is just a single **5–10 minute** one. What went well / what fell short / what I learned / tomorrow's focus. **"Tomorrow's focus" becomes the first line the AI reads tomorrow.**

### Four principles for working with AI

1. **Set a goal, tell it, then start** — what, why, how far
2. **Make it plan before making anything**
3. **Leave records** — especially what got stuck
4. **Ask when you don't know** — "why did you do it this way?"

### What not to do

Perfectionism (trying to memorize it all) · reading only without doing · starting with no plan · several Topics at once · skipping retrospectives · using only web chat

### Honestly — what didn't go well

**Time estimates are often off.** Generally generous, but multi-language and deployment work took longer than planned instead.

**The tool-use itself is the barrier.** An actual record says — *"there may be a barrier of having to first learn how to use AI agent tools. Supporting material would help adoption."* **The very guide you're reading is that supporting material.**

**Cost can run out faster than expected.** Hitting the limit isn't a malfunction. Record what you did and take a break.

**The retrospective gets dropped first.** Don't try to do it perfectly. **Even a 5-minute daily retrospective** is enough.

### How to read the numbers

**Take them as encouragement, not a promise.** The people in the records were already used to the tool. A first-timer takes longer. **That's normal.**

> Detail: [Chapter 6 detail](../06-Records-And-Habits/README.en.md)

## Chapter 7 — Next steps

You've come this far.

**You have the tools.** VS Code, Claude, Claude Code, VibeLearn AI.
**You know the method too.** Set a goal, plan first, leave records, ask.
**One thing remains.** Actually starting something.

### When you continue next time

Open the `VibeLearn-AI` folder in VS Code and say:

```
Please start today's learning.
```

The AI reads the plan and past records and tells you **how far you've come and what to do today.**

### When it's hard to go alone

**Don't wrestle with it alone for long.** Installation is a threshold you cross once, usually finished with 5 minutes of help.

When asking for help, sharing three things makes it much faster.

1. Which step you're stuck at
2. What the screen says (a photo/screenshot is best)
3. What computer (Windows / Mac / Chromebook)

### Learn more

**Catch Up AI** — https://catchupai.net/
A place to share how to use AI in real work, with cases. Program info and contact are here too.

**The first time takes longest. And you've already passed that first time.**

## Appendices

| Appendix | Contents |
|---|---|
| A | [Plain-language glossary](../01-Guide-Foundation/02-glossary.en.md) — 21 terms + words to avoid |
| B | [When you get stuck](../03-Setup-Environment/04-troubleshooting.en.md) — 18 situations |
| C | Frequently asked questions — reuses the existing FAQ |
| D | [A little deeper](../04-Setup-VibeLearn/04-appendix-advanced.en.md) — things you don't have to do, other AI tools |
