---
title: "What to check when you get the plan"
created: 2026-08-10 16:50:00
author:
  - "Claude Code"
tags:
  - vibecoding
  - vibelearn-ai
  - usage
---

> 🌐 [한국어](03-roadmap-checklist.md) · **English**

## What to check when you get the plan

When you start a Topic, the AI makes you a **plan (Roadmap).** But it doesn't make it right away — it **asks first.** And it **asks again** each day when you start.

This "asking" is the key safeguard of this way of working. Let's see why, and what to look at in the plan you get.

## Why the AI doesn't run off on its own — two confirmations

### First — before making the plan

Once you've given all the Topic info, the AI doesn't write the plan yet. It **checks whether the timeframe you mentioned is reasonable and tells you.** Then it asks this.

> **User confirmation required**:
> Review the analysis above and choose one:
> 1. "Proceed as is" - use the entered timeframe
> 2. "Adjust timeframe" - change to the recommended timeframe
> 3. "Adjust scope" - keep the timeframe but adjust the learning scope
>
> — VibeLearn AI repository, `templates/roadmap_prompt_template.md` lines 132–137

Just pick one. **If you're unsure, pick "Proceed as is."** You can change it any time later.

Before getting this confirmation, the rule nails down that no plan file is made.

> **Important**: Do not create the Roadmap file before user approval.
>
> — VibeLearn AI repository, `templates/roadmap_prompt_template.md` line 20

### Second — each day when you start

After the plan exists, saying "Please start today's learning" each day makes the AI **propose today's work and ask again.** It proceeds only after you approve.

When approving you can pick one of three.

| What you can pick | For when |
|---|---|
| **Approve** ("let's start") | The plan is fine |
| **Request changes** | There's something to adjust |
| **Adjust difficulty** ("a bit easier" / "a bit deeper") | Too hard or too easy |

*— VibeLearn AI repository, `templates/daily_learning_prompt.md` lines 302–319*

### Why ask twice?

**To keep the AI from deciding on its own and running off.**

Proceed with a wrongly set plan and undoing it later is much more of a hassle. Fixing a plan takes 5 minutes; fixing something already made takes far longer.

At first this asking may feel tedious. Once you're used to it you'll mostly press "Proceed as is," but **early on it's good to build the habit of reading what the AI is about to do.**

> 💡 **When tired or short on time, just say so.** Say "I'm a bit tired today" and the AI lowers the difficulty and reduces the amount. Better than forcing progress.

## What to check in the plan

You don't need to understand the whole plan. **Skimming just this much is enough.**

### For the whole

- [ ] Roughly how many steps (M1, M2 …) and what each is
- [ ] Not very different from what I had in mind
- [ ] There's a step at the end that ties it all together

### For each step

Each step should contain nine things. The required items the repository set.

> - Basic module info (number, title, estimated time)
> - Learning objectives (3–5, measurable)
> - Key concepts (theory 20–30%)
> - Exercises (practice 70–80%)
> - Expected outputs
> - Definition of Done (DoD) checklist
> - Self-Assessment checklist
> - Time allocation
> - References
>
> — VibeLearn AI repository, `CLAUDE.md` lines 58–67

You don't need to check them all — **just these three suffice.**

- [ ] There's an **estimated time** — you can judge if it's a day-sized chunk
- [ ] There's a **DoD** (Definition of Done) as checkboxes — you can know "this is where it ends"
- [ ] Goals are written as **"I can do"** — with "I understand" there's no way to confirm

## Little theory, lots of doing

Look at the plan and you'll see practice weighted heavily. The principle the repository set.

> **Practice-first**: 70–80% practice, 20–30% theory
>
> — VibeLearn AI repository, `CLAUDE.md` line 97

**Think of it as roughly theory 3 : doing 7.** Reading alone doesn't stick.

Time includes a buffer too.

> **Respect time**: adjust scope to available time, keep a 20% buffer
>
> — VibeLearn AI repository, `CLAUDE.md` line 114

**20% of the planned time is left as slack** for the unexpected. That's why the plan doesn't keep slipping.

## If you don't like it, just say so

The plan isn't a fixed document. You can change it any time.

```
There look like too many steps. Please cut them in half.
```

```
Step 2 looks hard — please break it up smaller.
```

```
I don't think I need this part. Please remove it.
```

## The standard for saying you're done

At the end of each step there's a **DoD** (Definition of Done). Fill in all the checkboxes and that step is over.

There's also a **Self-Assessment.** What matters here is that the assessment standard is different from before.

> **"You don't need to memorize every detail. Enough understanding to instruct the AI effectively is enough."**
>
> — VibeLearn AI repository, `README.md` line 367

It doesn't ask whether you memorized. It looks at **whether you can direct the AI properly.** This is the basic attitude of this way.

## When it doesn't work

**The AI made the plan without even asking**
Happens sometimes. Just say this.

```
Please check whether the timeframe is reasonable first. Make the plan after that.
```

**The made file has `{ }` braces or odd symbols left in it**
The form didn't fill in properly. Say this.

```
There are unfilled parts left in this file. Please remake it.
```

**The plan looks too short or careless**
The AI may have made it with the form shortened. Ask it to remake it.

## Next

That's it for **starting and making a plan.** What's left is **how to keep using it well.**

The next chapter covers why this way keeps getting better, and its heart — **records.**

→ Next: **Chapter 6, How to keep using it well**
