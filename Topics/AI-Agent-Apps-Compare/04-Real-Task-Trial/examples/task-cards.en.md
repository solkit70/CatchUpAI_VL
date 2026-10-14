---
title: "M4 Synthetic Task Cards"
source: "M4 synthetic task design; no external source"
author:
  - "박창수"
  - "Codex"
created: "2026-10-11 07:18:43"
tags:
  - ai-agent-apps-compare
  - synthetic-data
---

# M4 Synthetic Task Cards

[한국어](task-cards.md)

The names, dates, events, and notes below are fictional data created for practice. They are not real user, customer, event, or broadcast information. Enter both tasks as text in Muse chat; do not open or change events, email, or posts in external apps.

## Task A — Review a Fictional Event Schedule

**Goal**: Identify conflicts and total duration in a timetable and report findings to the organizer.

**Synthetic input**:

| Item | Start | End |
|---|---:|---:|
| Welcome and orientation | 09:00 | 09:10 |
| Short talk | 09:10 | 09:40 |
| Tool demonstration | 09:35 | 10:00 |
| Q&A | 10:00 | 10:20 |
| Break | 10:20 | 10:30 |

**Muse request**:

> Review only the fictional event timetable below. Separately summarize overlapping items and their overlap duration, total elapsed time from the first item to the last, and the sum of individual item durations. Do not modify or create events. Do not infer facts absent from the input.

[Paste the table above]

**Expected result**: Identify a five-minute overlap at 09:35–09:40, distinguish the 90-minute elapsed span from the 95-minute sum of individual durations. Do not automatically apply a revised schedule.

**Success criteria**:
- [x] Correctly identify both overlapping items and the five-minute conflict interval
- [x] Distinguish 90 minutes elapsed from the 95-minute item total
- [x] Do not invent information not provided (checked in the fictional timetable analysis response)
- [x] Provide analysis only, without changing events

## Task B — Write a Video Description from Fictional Broadcast Notes

**Goal**: Turn unstructured broadcast notes into a reviewable draft video description.

**Synthetic input**:

- Fictional channel: Maple Lab
- Fictional episode: A Small Balcony Garden to Help Pollinators
- Key notes: beginner pot plan, choose locally suitable flowers, shallow water dish, avoid pesticides
- Tone: friendly, without exaggeration
- Audience: people starting a balcony garden for the first time

**Muse request**:

> Write a draft video description using only the fictional notes below. Include one title, a 100–140-word description, three key-point bullets, and three hashtags. Do not add numbers, effects, or expert quotations absent from the notes. Do not create external links or publish anything.

[Paste the fictional notes above]

**Expected result**: Follow the specified format and length, cover all four key notes, and add no unsupported ecological effects or numbers.

**Success criteria**:
- [x] Include a title, 100–140-word description, three bullets, and three hashtags
- [x] Reflect all four fictional notes
- [ ] Add no numbers, effects, quotations, or links absent from the notes
- [x] Draft only; do not publish
