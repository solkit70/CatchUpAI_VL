---
title: "Plain-Language Glossary"
created: 2026-08-10 09:55:00
author:
  - "Claude Code"
tags:
  - vibecoding
  - guide-foundation
  - glossary
---

> 🌐 [한국어](02-glossary.md) · **English**

## What this document is for

This is the **shared language standard** for the whole guide. It explains, in everyday words, the terms you can't avoid on the way from installation to your first success. Every module uses these definitions as written. If the same term is explained differently in different documents, the reader gets confused twice.

This glossary goes into the guidebook as **Appendix A**.

## The rules for using it

Explain a term **only the first time it appears**. Repeating it every time makes the text drag. Put the explanation in parentheses or a short aside.

> Example: "Install the **Extension** (an add-on part that gives a program new features) for VS Code."

**For abbreviations, spell out the full form the first time**, then use the short form afterward.

> Example: "Check the **DoD** (Definition of Done)." → after that, just "DoD"

If a term can't be explained without making the sentence too long, don't use it at all — use a **substitute expression** from the table below.

## Term definitions

### Computer basics

**Folder**
A drawer that holds files. The basic unit for organizing files on a computer. ("Directory" means the same thing, but this guide uses **folder** only.)

**Path**
The address that tells you where a folder or file lives on your computer. Something like `C:\Documents\liberation-day-talk` — the drawers written out in order.

**Terminal**
A window where you give the computer commands by typing. Instead of clicking with a mouse, you type text to tell it what to do. **This guide is written so you never need the terminal** — don't be intimidated by it.

**Install**
Putting a program onto your computer so you can use it.

### Tools

**Editor / code editor**
A program for writing and editing text and files. Think of it as a much smarter version of Notepad. The **VS Code** we use in this guide is one of these.

**VS Code**
A free editor made by Microsoft. The most widely used editor in the world. We attach an AI to it.

**Extension**
An add-on part that gives a program new features. Just like adding an app to your phone, adding an extension to VS Code gives it new abilities. **Claude Code** is also installed as an extension.

**Claude**
An AI you can talk to in plain language and give tasks to. The AI we'll use.

**Claude Code**
A tool that lets Claude **read and write the folders and files on your own computer directly**. This is the key part — unlike just chatting on a website, it actually creates and edits your files.

**AI agent**
An AI that carries out a task through several steps on its own. Instead of one question and one answer, it goes on to find, read, create, and edit files.

### Accounts and cost

**Account**
What you create to log in as "you" to a service. Usually made with an email and a password.

**Subscription**
Paying a set amount every month to keep using a service. Billed monthly, like Netflix. **To use Claude Code, you need a paid Claude subscription.**

### Downloading

**Repository**
An online space where a whole bundle of program files or materials is kept. In this guide we call it the **"VibeLearn AI folder"** or **"VibeLearn AI materials."**

**ZIP file**
A file that bundles and compresses many files into one. When you download and unzip it, the original files come out.

**Clone**
Copying a whole repository to your own computer. In this guide we say **"download"**, and only mention the word "clone" in parentheses on the optional path.

**Git / GitHub**
A service for storing program materials and managing versions. **You don't need it to follow this guide.** We show you the ZIP download path.

### Working with AI

**Prompt**
A message or request you hand to the AI. Just think of it as "a sentence asking for something."

**Markdown (.md)**
A way of formatting text with simple symbols, or a file written that way. Adding `#` makes a heading, for example. Most of the documents we make are in this format. **You don't need to memorize it** — the AI writes it for you.

**Plan mode**
A mode where the AI **plans out what it will do and how, without editing files right away**. Real work starts only after you look at the plan and approve it.

### VibeLearn AI terms

**VibeLearn AI**
A **method** for learning systematically with AI and leaving behind materials the next person can use. It's a way of working, not a program. **You don't need to memorize the method** — one sentence like "I want to learn ○○" and the AI takes it from there.

**Topic**
One subject you want to learn or make. A single unit, like "preparing a Liberation Day talk" or "making an Excel table." Each Topic gets its own folder.

**Roadmap**
The full plan the AI draws up for what order to learn that Topic in. It's divided into several steps (modules), each with its goals and tasks written out.

**Module (M1, M2 …)**
One step that makes up the roadmap. Usually sized to finish in a day or two.

**WorkLog**
A record of what you did today and where you got stuck. **It acts as the AI's memory** — with it, the AI knows what happened yesterday when you continue next time.

**Retrospective**
Briefly looking back at what went well and what didn't. The daily one takes about five minutes.

**DoD (Definition of Done)**
A list of conditions decided in advance for "this is where it ends." It's in checkbox form so you can confirm it yourself. Spelled out, it means the **standard for being able to say you're finished**. You'll keep running into the abbreviation **DoD** throughout VibeLearn AI documents, so write it out as **"DoD (Definition of Done)"** the first time, then use DoD afterward.

**Output / artifact**
The files and folders left behind from your study or work. Documents, organized notes, whatever you made — all of it counts.

## Substitute expressions — don't say this, say that

Sometimes it's better not to use a technical term at all than to explain it. Throughout the guide, **avoid the left column and use the right.**

| Don't use | Use instead |
|---|---|
| repository / repo | VibeLearn AI folder, VibeLearn AI materials |
| clone (verb) | download |
| directory | folder |
| CLI / command line | (avoid if possible) a window where you type commands |
| run / execute / launch | open, turn on |
| install (as jargon) | set up, put on your computer |
| config / configuration value | settings |
| ext / extension (as jargon) | extension (explained once) |
| commit / push | (out of scope for this guide — don't use) |
| environment variable | (out of scope for this guide — don't use) |
| install dependencies | (out of scope for this guide — don't use) |
| sidebar / activity bar | the vertical bar on the left |
| workspace | working folder |
| user / end user | you, the person using it |
| error | problem, a common thing that happens |

> **Why we avoid "error"**: To someone not used to computers, "error" reads as a signal that "I did something wrong." Most of these are common situations that happen to everyone, so we phrase them as "a common thing that happens" to lower the psychological barrier.

## When a term isn't in this glossary

If you must use a new term while writing, **add it to this glossary first** before putting it in the body. A technical term that appears in the body without being in the glossary gets caught in review (see `03-writing-checklist.en.md`).
