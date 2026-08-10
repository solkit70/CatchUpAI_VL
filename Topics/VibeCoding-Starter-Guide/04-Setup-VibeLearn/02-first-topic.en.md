---
title: "Start your first Topic"
created: 2026-08-10 12:10:00
author:
  - "Claude Code"
tags:
  - vibecoding
  - vibelearn-ai
---

> 🌐 [한국어](02-first-topic.md) · **English**

## Start your first Topic

Now the most surprising part. **One sentence starts it.**

You don't need to study VibeLearn AI. You don't have to memorize the method's name, the folder structure, or the rules. **Say what you want to do, and the AI handles the rest.**

**Time**: 15–20 minutes
**What you need**: the `VibeLearn-AI` folder you opened earlier

## Step 1 — Say one sentence

Press the **Claude icon** on the vertical bar on the left, and type **what you want to do** in the box.

The form is this.

```
I want to learn ○○.
```

That really is all. Below are examples. **Pick the one that applies to you and type it as is.**

**If you're a student**

```
I want to prepare a Liberation Day talk.
```

**If you have something to make**

```
I want to learn to make a web page that presents my experience.
```

**If you want to use it at work**

```
I want to learn how to organize our group's event materials.
```

> 💡 **If the word "learn" feels off** — it doesn't have to be school study. Making, organizing, looking into something — all count. Saying "I want to try ○○" works too; the AI understands.

## Step 2 — Answer the AI's questions

The AI asks a few things. Don't overthink it — answer as best you know. If you don't know, saying "I'm not sure" is fine — the AI asks again with examples.

Usually it asks things like this.

| What the AI asks | How to answer |
|---|---|
| What you want to make or know | As specifically as possible. Not "slides" but "slides for a 5-minute talk at a Liberation Day ceremony" |
| Roughly how long it'll take | As best you know. "3 days," "a week," "I'm not sure" all fine |
| What computer you use | Windows / Mac |
| Whether you know anything in advance | If not, "nothing" is fine |

> 💡 **An easier way** — if answering is tedious, ask like this.
>
> ```
> Please ask me one at a time in multiple-choice form.
> ```
>
> Then the AI gives options for you to pick.

> ✅ **When you get this far** — the AI summarizes your answers and confirms whether to proceed with this.

## Step 3 — Watch the folder get made

When the AI says it'll make folders, **Allow.** After a moment, this appears in the left list.

```
Topics/
└── the-name-i-chose/
    ├── topic_info.md      ← a summary of what I'm trying to do
    ├── vl_prompts/        ← prompts the AI will use
    ├── vl_roadmap/        ← the full plan appears here
    ├── vl_worklog/        ← daily records pile up here
    └── vl_materials/      ← where reference materials go
```

**Folders with `vl_` in front** are VibeLearn AI's workspace. You don't have to manage them directly.

> ✅ **You'll know it worked** — inside the `Topics` folder there's a folder named after your subject.

## Step 4 — Get the plan (Roadmap)

Next the AI makes the **full plan.** This is called the **Roadmap.** It's a table dividing what to do in what order, step by step.

Here **something important happens.** The AI doesn't make the plan right away — it **asks first.**

> "I looked at whether the timeframe you mentioned fits this subject. What would you like?"
> 1. Proceed as is
> 2. Adjust the timeframe
> 3. Adjust the scope

Just pick one. **If you're unsure, pick "Proceed as is."** You can change it any time later.

When you approve, the plan file is made.

> ✅ **You'll know it worked** — inside the `vl_roadmap` folder there's a file named something like `20260810_RoadMap_...md`. Open it and you'll see steps split into M1, M2, M3…

## Step 5 — Skim the plan (5 min)

Open the plan and read through it. You don't need to understand all of it. **Just checking these three is enough.**

**One, how many steps (M1, M2 …) there are and what each is.** As long as it's not very different from what you had in mind.

**Two, whether each step has an "estimated time."** See if it's a day-sized chunk.

**Three, whether there's a list called "Definition of Done."** That means the **completion criteria** — a checkbox of "this is where it ends" decided in advance. With it, you don't fall into the "I don't know when this is done" state. From now we shorten it to **DoD.**

If something's off, just say so.

```
Step 2 looks too hard. Please break it up more simply.
```

## The whole flow — from now it cycles like this

VibeLearn AI is a structure where three steps repeat. You've just finished steps 1 and 2.

| Step | When | What |
|---|---|---|
| **① Start Topic** | Once at first | "I want to learn ○○" → folders made |
| **② Make the plan** | Once at first | The AI writes a step-by-step plan → **you approve** |
| **③ Study daily** | Repeat each time | Plan today's work → **you approve** → proceed → record |

When you continue next time, say this.

```
Please start today's learning.
```

Then the AI reads the plan and the past records, and tells you **how far you've come and what to do today.** Here too it asks once more before proceeding.

> 💡 **Why it asks twice** — once when making the plan, once each day when starting. It's a device so the AI doesn't decide on its own and run off. Once you're used to it you'll just press "Proceed as is," but at first it's good to build the habit of **reading what the AI is about to do.**

## If you got this far

Your first Topic has started and you have the plan in hand. Now all that's left is to actually **make something.**

→ Next: [First success — a result in 5 minutes](03-first-win.en.md)

## When it doesn't work

**The AI just answers instead of doing it the VibeLearn AI way**
The `VibeLearn-AI` folder is likely not open. Check that `VIBELEARN-AI` shows at the top-left of VS Code. If it still doesn't work, say this.

```
Read the CLAUDE.md in this folder and proceed that way.
```

**The made file has `{ }` braces or odd symbols left in it**
Common. The form didn't fill in properly. Just say this.

```
There are unfilled parts left in this file. Please remake it.
```

**The plan looks too long and hard**
Just say so. "It looks like too much. Please reduce the steps" and it redraws.

**I don't know what to answer to the questions**
Say "I'm not sure. Please give me an example" and the AI asks again with options. Answering "I don't know" is no problem at all.
