---
title: "Full Guide Outline + Module Mapping"
created: 2026-08-10 09:40:00
author:
  - "Claude Code"
tags:
  - vibecoding
  - guide-foundation
---

> 🌐 [한국어](01-outline.md) · **English**

## What this document is for

We fix the outline of the final deliverable — the **participant guidebook** — first. Deciding in advance which chapter each of M2–M7 fills prevents overlap and gaps, and lets each module be written knowing "where the piece I'm writing sits in the whole."

## The order the reader reads in

The guide is not a tool manual; it's **one path a person follows from start to finish.** So the outline is arranged not by feature order but by the reader's emotional order. First we ease the "am I allowed to do this?" feeling (chapters 0–1), then get them to understand "what this is" (chapter 2), then get their hands moving (chapters 3–4), and only then teach "how to use it well" (chapters 5–6).

Installation is placed in chapter 3, not chapter 2, for exactly this reason. If you start installing without knowing what you're installing or why, a reason to give up appears the moment you get stuck.

## Full outline

| Ch | Title | Filled by | Rough length |
|---|---|---|---|
| 0 | Welcome | M7 (at integration) | 1 page |
| 1 | What you'll be able to do with this guide | M7 | 1 page |
| 2 | What is vibe coding | **M2** | 3–4 pages |
| 3 | Getting ready — what to install | **M3** | 5–6 pages |
| 4 | Install VibeLearn AI and take your first step | **M4** | 4–5 pages |
| 5 | How to use it well | **M5** | 4–5 pages |
| 6 | How to keep using it well | **M6** | 4–5 pages |
| 7 | Next steps | M7 | 1 page |
| Appendix A | Plain-language glossary | **M1** | 2 pages |
| Appendix B | When you get stuck (common things) | **M3** | 2 pages |
| Appendix C | Frequently asked questions | M7 (reuse existing FAQ) | 2 pages |
| Appendix D | A little deeper (optional) | **M4** | 1 page |

### Chapter details

**Chapter 0 — Welcome**
Opens with "It's fine if you don't know how to code. It's fine if you're not used to computers." Here we state that this guide was made by **Catch Up AI** (https://catchupai.net/). We add the Utah teacher's story in two or three sentences to signal "someone like me did this."

**Chapter 1 — What you'll be able to do with this guide**
Shows, with a picture, what you'll walk away with if you follow through to the end. One paragraph per reader tier — a student for talk preparation, a senior/experienced person for what they want to build with their knowledge, a civic-group worker for organizing work materials. States the time honestly (about an hour to install, thirty minutes more to first success).

**Chapter 2 — What is vibe coding** *(M2)*
The meaning of vibe coding, that **it's not only coding** (file organizing, research, learning, project management), what changes when you treat AI as a **coworker** rather than a tool, and why setup is the barrier (the highway analogy). Here we attach links to the Build with AI video and the civic-group video.

**Chapter 3 — Getting ready** *(M3)*
Install VS Code → sign up for paid Claude → install and log in to the Claude Code extension → make a working folder. Every step gets a "you'll see this screen when it works" checkpoint. We mark where Windows and macOS diverge, and state that Chromebooks can't use this path.

**Chapter 4 — Install VibeLearn AI and take your first step** *(M4)*
Starts by pointing to the VibeLearn AI intro video → download (ZIP recommended / clone) → look around the folder → **start your first Topic with one sentence, "I want to learn ○○"** → confirm first success. Contributor-only setup is moved out of the body into Appendix D.

**Chapter 5 — How to use it well** *(M5)*
How to break away from the ask-and-answer chatbot habit. Why chatbot Q&A doesn't stick (memory, completion, outputs, portability), naming your Topic and goals well, why the two approval gates are reassurance, and what to check when you get the roadmap.

**Chapter 6 — How to keep using it well** *(M6)*
That records are the AI's fuel, how to do retrospectives without pressure, how to make the AI plan first, what not to do, and stories from people who went ahead (encouragement + reality). We attach records-related video links here.

**Chapter 7 — Next steps**
Guides both the path to keep going alone and the path to get help. Here we introduce **Catch Up AI** (https://catchupai.net/) again, with community links and how to reach out.

## Where the per-tier motivation paragraphs go

Since three tiers read the same guide together, each tier needs at least one passage where they feel "this is about me." But we don't split the document by tier — splitting triples maintenance and loses the benefit of learning from each other's cases.

| Location | Student | Senior / experienced | Civic-group worker |
|---|---|---|---|
| Ch 1 (what you'll do) | Prepare a talk/assignment with AI | Turn your experience into an app | Organize work materials & event prep |
| Ch 2 (not only coding) | Research and slide prep | The first version of what you want to make | Organizing minutes & event materials |
| Ch 4 (first Topic example) | "I want to prepare a Liberation Day talk" | "I want to learn to make the app I have in mind" | "I want to learn to organize our group's materials" |
| Ch 6 (someone who went ahead) | — | The teacher's story | The civic-group video case |

## Where Catch Up AI is introduced (fixed)

Two places only. Repeating it reads like promotion and erodes trust.

| Location | How |
|---|---|
| **Top of ch 0** | "This guide was made by Catch Up AI (https://catchupai.net/)" — one line naming who made it |
| **Ch 7 next steps** | As "learn more" and a contact point. Here the link comes with one sentence on what you can find there |

The facilitator manual also lists it once as a participant contact point (separate from the guidebook body).

## Module → chapter reverse map (for writing reference)

| Module | Fills chapter | Output files |
|---|---|---|
| M1 | Appendix A + the language standard for all chapters | `01-outline.en.md`, `02-glossary.en.md`, `03-writing-checklist.en.md` |
| M2 | Ch 2 | `01-what-is-vibe-coding.en.md`, `02-beyond-coding.en.md`, `03-ai-as-partner.en.md` |
| M3 | Ch 3 + Appendix B | `01-setup-vscode.en.md`, `02-setup-claude.en.md`, `03-setup-workspace.en.md`, `04-troubleshooting.en.md` |
| M4 | Ch 4 + Appendix D | `01-get-vibelearn.en.md`, `02-first-topic.en.md`, `03-first-win.en.md`, `04-appendix-advanced.en.md` |
| M5 | Ch 5 | `01-why-not-chatbot.en.md`, `02-starting-well.en.md`, `03-roadmap-checklist.en.md` |
| M6 | Ch 6 | `01-records-as-fuel.en.md`, `02-working-with-ai.en.md`, `03-real-stories.en.md` |
| M7 | Ch 0·1·7 + Appendix C + full integration | `01-participant-guidebook.en.md`, `02-facilitator-manual.en.md` |

## Decisions on record

**Target length is about 30 pages.** Beyond that, the target reader won't finish it. If a chapter runs well past the length in the table above, we move material into an appendix.

**Videos get links inline in the body**, not gathered into a list — they only matter if the reader can watch at the moment they read that passage. Links come only from `vl_materials/video-references.md`.

**There is no setup-process video yet** (confirmed 2026-08-10, to be produced later). Chapters 3 and 4 are written to stand on their own, and we don't pre-insert phrases like "you can also watch a video."
