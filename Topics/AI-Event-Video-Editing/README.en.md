---
title: "AI-Event-Video-Editing"
author:
  - "박창수"
  - "Claude Code"
  - "Codex"
created: "2026-10-20 10:00:00"
updated: "2026-10-30 04:59:03"
status: "In progress — M6 delivery drafts; Topic completion pending"
tags:
  - ai-event-video-editing
  - video-editing
---

## About this Topic

[한국어](README.md)

This project investigates selecting real moments from long event footage, assembling a short highlight, and adding titles, captions and an intro. The current recommendation is conditional: check the client's existing Premiere and CapCut workflow first, then compare Vidio using a short sample approved for upload. Client software versions, subscription and delivery requirements remain unconfirmed.

## Observed results

- Local transcript-assisted FFmpeg editing produced a 147.714-second excerpt and a later 157.257-second effects demo reviewed by the user.
- Vidio Free produced a verified 126.912-second first export. Its automatic revision missed the requested duration; manual Transcript editing restored a 2:30 UI result. The user liked that preview, but its local export remains unverified.
- The user judged the summaries similarly for core content and slightly preferred the cleaner ending of the local version. This single English presentation is not evidence of general performance across events.
- CapCut Seedance 2.0 Mini produced and downloaded a 5.062-second, 1280×720 H.264 MP4; full-file decoding passed. Full-frame review found unintended generated text (“Penhin”) and an “Ai” mark, so the clip is not ready for event use. An AAC audio stream exists but was not auditioned. The template editor remains unrendered, leaving the two-intro comparison unfinished.
- A short local Whisper comparison still required transcription correction. Captions were not added to the final demo.

Evidence: [M4 comparison](04-HandsOn-Highlight/results-comparison.md), [Vidio trial](04-HandsOn-Highlight/method-B.md), [M5 intro results](05-HandsOn-Effects/intro-template-vs-generative.md).

## Read in learning order

| Module | Guide | Status |
|---|---|---|
| M1 | [Requirements and methods](01-Requirements-Map/README.md) | 6/7; client answers pending |
| M2 | [Research](02-Methods-Research/README.md) | 7/7; nine candidates across five groups |
| M3 | [Conditional recommendations](03-Recommendation/README.md) | 7/7; trial preparation complete |
| M4 | [Highlight trials](04-HandsOn-Highlight/README.md) | 5/7 |
| M5 | [Intros and effects](05-HandsOn-Effects/README.md) | 6/7 |
| M6 | [Client manuals and delivery drafts](06-Client-Manual/README.md) | 5/7; captures and walkthrough pending |

The Korean [one-page summary](06-Client-Manual/one-page-summary.md), [existing-tools manual](06-Client-Manual/manual-existing-tools.md), [Vidio manual](06-Client-Manual/manual-vidio.md), [five prompt examples](06-Client-Manual/prompt-examples.md), [eleven official references](06-Client-Manual/references.md), and [delivery message drafts](06-Client-Manual/delivery-message.md) are ready for review. Messages have not been sent. Three CapCut example captures are included; full step-by-step captures and a walkthrough in the client's environment remain pending.

## Limits and remaining work

Paid services and card-required trials were not purchased. Only the specified five-minute sample was approved for external upload. Client identities, contact details, actual footage and participant screenshots stay outside this public Topic.

Premiere XML handoff, client-version reproduction, remaining M4/M5 exercises and user self-assessment are pending. The [retrospective draft](vl_worklog/20261029_AI-Event-Video-Editing_Final_Retrospective.md) records these gaps; it does not declare Topic completion. See the [roadmap](vl_roadmap/20261017_RoadMap_AI-Event-Video-Editing.md) and [latest WorkLog](vl_worklog/20261029_M6_AI-Event-Video-Editing.md) for detailed status.
