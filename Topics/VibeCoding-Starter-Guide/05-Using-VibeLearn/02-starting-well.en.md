---
title: "How to start well"
created: 2026-08-10 16:35:00
author:
  - "Claude Code"
tags:
  - vibecoding
  - vibelearn-ai
  - usage
---

> 🌐 [한국어](02-starting-well.md) · **English**

## How to start well

Earlier we said **one sentence — "I want to learn ○○" — starts it.** That's true.

But **how you write that one sentence** changes what follows quite a bit. It's not hard, so let's look at just three things.

## One — specify the goal first

The most common mistake is **starting vaguely.**

```
I want to study AI.
```

Say it this way and the AI answers vaguely too. It doesn't know what, why, or how far you're trying to go.

Instead, try this.

```
I want to make materials for a 5-minute talk at a Liberation Day ceremony.
At a level even a middle schooler understands,
I want to introduce one independence activist.
I need to finish by next Friday.
```

**What / for whom / how far / by when.** You don't need all four. Writing just what you know makes it much better.

> 💡 **It's fine if you can't decide it all at once.** The AI asks back. If answering is hard, say "Please ask me in multiple-choice form" and it gives options.

## Two — make the name specific

The Topic name becomes the folder name. Once several pile up you find them by name, so it's good to be specific from the start.

Examples the repository gives:

| Good | Avoid |
|---|---|
| `Docker-Fundamentals` (tech-level) | `Docker` (too broad) |
| `React-Hooks` (tech-specific topic) | `docker advanced` (uses a space) |
| `ML-Basics` (abbrev-level) | |

*— VibeLearn AI repository, `templates/workflow_guide.md` lines 294–303*

Since developer examples may feel unfamiliar, converted to our side:

| Good | Avoid |
|---|---|
| `Liberation-Day-Talk-Prep` | `talk` (don't know what talk) |
| `Excel-PivotTable-Basics` | `excel` (too wide) |
| `Event-Materials-Cleanup-2026` | `organizing` (spaces, vague) |

**There are only two rules.** Make it recognizable what it's about, and use a hyphen (`-`) instead of a space.

## Three — write goals as "I can do"

This is the part with the biggest effect. Write goals in a **confirmable** form and you can later judge "am I done?" yourself.

| Good | Avoid |
|---|---|
| "I can write a Dockerfile and make a custom image" | "I understand Docker" (unverifiable) |
| "I can connect 3+ services with docker-compose.yml" | "I become a Docker expert" (unmeasurable) |

*— VibeLearn AI repository, `templates/workflow_guide.md` lines 305–313*

Converted to our side:

| Good | Avoid |
|---|---|
| "I can finish a 5-minute talk script and read it aloud" | "I get to know Liberation Day well" |
| "I can organize event materials into one folder and make a list" | "I get good at organizing" |
| "I can make a journal screen for the elderly and actually open it" | "I get to know how to make an app" |

**Turning "I understand" into "I can do"** is the trick.

## The Do / Don't the repository organized

The things to keep and to avoid when starting are collected in the repository. Copied as-is.

**Recommended**

> - **Be specific**: "learn a framework" → "build a RESTful API with FastAPI"
> - **Make it verifiable**: "understand" → "can implement directly"
> - **Be realistic**: don't set the timeframe too tight
> - **Include references**: name links or docs that help learning

**Avoid**

> - Too broad a Topic (e.g. "all of programming")
> - Vague goals (e.g. "get good," "learn a lot")
> - Unrealistic timeframe (e.g. "become an expert in a week")
> - Starting with no references
>
> — VibeLearn AI repository, `templates/topic_starter.md` lines 253–266

## How do I set the timeframe?

**If you don't know, say you don't know.** The AI checks whether it fits and tells you. That process is covered in the next document.

The rough feel is this.

| This kind of thing | Roughly |
|---|---|
| Making one simple thing | 3–7 days |
| Something of some size | 2–4 weeks |
| A big project | 1–3 months |

It's best not to set it too tight. **Set it in a rush and you'll fail to keep it daily and give up.**

## If you have reference materials, share them from the start

If you already have materials, telling the AI from the start is much better.

```
I have reference materials. I'll put them in the vl_materials folder.
```

Put files in the folder and the AI reads them. Web addresses work too.

**Giving materials only you have** is especially effective. Ask using only information anyone can find and you get answers like everyone else's; give your own materials and you get answers that fit you. This is covered again in chapter 6.

## To sum up — just these three at the start

**One. Write what you know of what / for whom / how far / by when.**
**Two. Make the name recognizable**, hyphen instead of space.
**Three. Write goals as "I can do,"** not "I understand."

You don't have to keep all three. **Keeping even one beats just starting.**

## Next

Once you start, the AI makes you a plan. But before that, it **asks once.** Let's see why it asks, and what to check when you get the plan.

→ Next: [What to check when you get the plan](03-roadmap-checklist.en.md)
