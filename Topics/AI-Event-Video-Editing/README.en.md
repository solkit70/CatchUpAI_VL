---
title: "AI-Event-Video-Editing"
author:
  - "박창수"
  - "Claude Code"
created: "2026-10-20 10:00:00"
status: "In progress — M1 (waiting for the client's answers)"
tags:
  - ai-event-video-editing
  - video-editing
---

## About This Topic

[한국어](README.md)

> **This is an in-progress version (2026-10-20).** It covers the requirements gathered so far, how the work will proceed, and what will be delivered. It will be replaced by a final version with findings and recommendations when the topic is closed.

This topic researches ways to take event footage that runs for hours and **tell an AI, in plain words, which scenes to keep — so it edits them into a highlight of about three minutes and adds an intro and transitions**. It started from a request by an event photographer and reporter (the client) who edits by hand, mainly in Adobe Premiere Pro, with After Effects and CapCut. The goal is to research and compare methods, recommend the ones that fit the client, and write **setup and usage manuals**.

This repository is public, so the client's name, contact details, event organizers, and actual event footage are not included.

## What We Are Looking For

> A way to tell an AI "use scenes like these" about hours of event footage, so it picks only the matching parts, edits them into a short video of about three minutes, and adds an intro and transitions

The job is split into three parts. We expect **① picking scenes** to take the most time in manual editing (to be confirmed).

| Part | What the AI should do | Example |
|---|---|---|
| **① Picking scenes** | Find and cut the sections that match the instruction in long footage | "Key lines from the speeches, the award moments, and smiling participants — in three minutes" |
| **② Assembling** | Order and trim the chosen sections to fit three minutes | Trim cut lengths, cut to the music |
| **③ Decorating** | Intro, transitions, captions, logo, music | Event-name intro, lower-third captions, transitions |

## What Has Been Organized So Far (M1)

### Requirements

| Item | Summary |
|---|---|
| Input | Hours of footage from a group event (possibly several clips) |
| Instruction | Describe what you want in words |
| Output | A short video of about three minutes |
| Decoration | Opening intro; transitions, captions, logo, and music in between |
| Budget | **Paid tools are fine** if they help the work |
| Current tools | **Adobe Premiere Pro** (main) · After Effects · CapCut |

**Must have**: can upload or read long footage · pick scenes from spoken instructions (both scenes with speech and without) · revise by giving new instructions · **hand the result to Premiere for finishing** · export at deliverable quality without a watermark

**Nice to have**: Korean instructions and captions · a reusable intro template per event · a vertical (9:16) social version · a way that does not upload footage to outside servers

→ Details: [Requirements card (Korean)](01-Requirements-Map/requirements-card.md)

### A Distinction to Know First — Editing vs. Generative AI

| Type | What it does | In an event highlight |
|---|---|---|
| **Editing AI** | Finds, cuts, and joins scenes from **footage already shot** | ① picking and ② assembling — **the core** |
| **Generative AI** | Creates **new video** from text or images | Intros and background shots in ③ decorating |

The "Sidence" the client mentioned is presumably ByteDance's **Seedance**. Seedance is **generative**: it can create new shots such as an intro, but **it cannot pick and cut scenes from footage**. We are asking the client which use they had in mind.

### Methods to Research — Five Groups

| Group | What | Examples (first search, not yet verified) |
|---|---|---|
| **A. Claude · ChatGPT + connectors** | The AI operates an editor or calls a generative AI | Community connectors (MCP) that operate Premiere, Seedance connectors |
| **B. Dedicated AI video-editing services** | Long footage → instruction → highlight; some export to Premiere | VEA · Vidio.ai · OpusClip · Descript, etc. |
| **C. AI features in the client's current editors** | AI features inside Premiere and CapCut | Premiere text-based editing and scene detection, Premiere extensions |
| **D. Generative video AI** | New shots for intros and decoration | Seedance · Runway, etc. |
| **E. Code-based automatic editing** | The AI cuts, joins, and adds effects with code (for comparison) | Claude Code + FFmpeg · Remotion |

**Because the client uses Premiere, methods that connect to Premiere come first**: ① Premiere's own AI features (no extra cost) → ② services that send highlights to Premiere → ③ AI operating inside Premiere → ④ intro generation → ⑤ code-based (for comparison).

→ Details: [Methods map (Korean)](01-Requirements-Map/methods-map.md)

## Next Steps

Once the client answers the [confirmation questions (Korean)](01-Requirements-Map/client-questions.md), the work proceeds in this order. We expect **about three weeks** after the answers (5–6 hours a week).

| Step | What happens | Output of this step |
|---|---|---|
| **M1** Requirements and methods map | Organize the request, split the research scope, prepare questions | Requirements card · methods map · questions **(current step)** |
| **M2** Research by method | Research 8+ candidates from official sources (pricing, limits, Korean, Premiere connection) | Candidate cards · **comparison table** · what the "Claude · ChatGPT + plugin" approach can and cannot do |
| **M3** Choose recommendations | Pick 1–2 recommendations and an alternative for the client's conditions; plan trials | **Recommendations with reasons** · diagram of how they fit the current workflow · trial plan |
| **M4** Trial ① highlight | Test two methods with the same footage and the same instruction | Step-by-step screenshots · results table (instruction-following, time, rework, cost) |
| **M5** Trial ② intro and effects | Compare template vs. generative intros; add effects and captions by AI instruction | **Three-minute demo video** (from publishable footage) |
| **M6** Manual and delivery | Write manuals per recommendation and a summary | **Setup and usage manuals** · instruction examples · one-page summary · reference links |

## How We Can Work — Choose One of Three

We live nearby, so meeting in person is possible. The options can be combined (for example, start with B and move to C).

| Option | How | Strength | Consider |
|---|---|---|---|
| **A. Changsoo researches → delivers manuals** | Changsoo follows the steps above and delivers results and manuals | Takes the least of the client's time | Paid tools are covered "from materials only" |
| **B. Meet and work together on Changsoo's computer** | Do M2 onward together in person; paid tools are tested with the client's own account | The client learns the process and paid tools are actually checked | Scheduling · the Premiere connection is checked on the client's computer |
| **C. Install VibeLearn AI on the client's computer + guidance** | Changsoo installs the AI learning tool he uses and shows how to use it; the client researches in the direction they want, with help when stuck | Try things directly in the client's Premiere and paid accounts, and learn how to research | Requires a paid Claude subscription · installation and first guidance take time |

## What Changsoo Can and Cannot Do

**Changsoo cannot try paid services himself.** This includes trials that require a card. Every tool in the results gets one of the marks below, separating what was actually tried from what was compiled from materials.

| Mark | Meaning | In the manual |
|---|---|---|
| ✅ Tried directly | A free plan or a card-free trial that Changsoo used | Step-by-step manual with screenshots, sticking points, and free-tier limits |
| 🤝 Tried together | Paid, but checked together in person (or by screen share) while the client used their own account | Official materials + what we saw together |
| 📄 Materials only | Paid, and hard to try together (including work inside Premiere and After Effects) | Based on official docs and tutorial links, marked "not tried directly" |

- Trials use **long footage that can be made public** (recordings of Changsoo's public seminars and meetups). The client's actual event footage is used for trials only with the client's and organizer's consent, and is never published.
- Changsoo's computer has no GPU, so local AI processing is hard to try. Trials focus on cloud services.
- Pricing and features change often, so each entry records **the date it was checked** and the official pricing page.

## What You Will Receive

1. **Comparison table** — 8+ methods on the same criteria (instruction-following, scene accuracy, time, rework, Premiere connection, cost, Korean, whether footage is uploaded)
2. **1–2 recommendations and an alternative** — why each fits and how it connects to the current workflow (Premiere, After Effects, CapCut)
3. **Trial records** — step-by-step screenshots and sticking points for methods tried directly
4. **Three-minute demo video** — highlight + intro and effects, made from publishable footage
5. **Setup and usage manuals** — per recommendation: sign-up and setup → upload → instruct → revise → add effects → export → finish in Premiere
6. **Five ready-to-use instruction examples** — speeches, awards, performances, group photos, atmosphere montage
7. **One-page summary and reference links** — cost and pros/cons, official docs and tutorial videos

The manual format (document/PDF, screen recording, or a walk-through session) is up to the client.

## What Is Needed Now — Answers to the Questions

To confirm the requirements and fit the manuals to the client's setup, we are asking 18 questions. **Answering only what you know is fine.** M2 starts once the answers arrive.

- **Setup**: Windows / Mac, Adobe plan and Premiere version, paid Claude or ChatGPT use, experience installing plugins
- **Footage and finished video**: footage length, cameras, resolution, audio quality, delivery format (horizontal/vertical), a recent three-minute example, time per video and number per month
- **What you want from AI**: which part matters most (①②③), the intended use of "Sidence," intro templates and music, Korean instructions and captions
- **Cost and footage handling**: monthly budget, whether footage may be uploaded to outside servers, whether test footage can be shared
- **Manual and way of working**: manual format and deadline, option A, B, or C

→ Full questions and reasons: [Confirmation questions (Korean)](01-Requirements-Map/client-questions.md)

## Documents

| Document | Contents |
|---|---|
| [01-Requirements-Map/README.md](01-Requirements-Map/README.md) | M1 guide and what was learned (Korean) |
| [Requirements card](01-Requirements-Map/requirements-card.md) | Requirements, an example of a good three-minute video, criteria, what Changsoo can and cannot do, ways of working (Korean) |
| [Methods map](01-Requirements-Map/methods-map.md) | Editing vs. generative, five groups of candidates, research order (Korean) |
| [Confirmation questions](01-Requirements-Map/client-questions.md) | 18 questions for the client and the reasons (Korean) |
| [Learning roadmap](vl_roadmap/20261017_RoadMap_AI-Event-Video-Editing.md) | Full M1–M6 plan (Korean) |

## Progress

| Step | Status |
|---|---|
| M1 Requirements and methods map | 🔄 Outputs done · waiting for the client's answers |
| M2 Research by method | ⏳ |
| M3 Choose recommendations | ⏳ |
| M4 Trial ① highlight | ⏳ |
| M5 Trial ② intro and effects | ⏳ |
| M6 Manual and delivery | ⏳ |

This topic follows the [VibeLearn AI](https://github.com/solkit70/CatchUpAI_VL) method — set a learning plan (roadmap), and leave outputs and work logs at every step.
