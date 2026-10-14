---
title: "M4 Muse Execution and Result Decisions"
source: "Synthetic M4 task results"
author:
  - "박창수"
  - "Codex"
created: "2026-10-11 07:23:37"
tags:
  - ai-agent-apps-compare
  - muse
  - evaluation
---

# M4 Muse Execution and Result Decisions

[한국어](trial-results.md)

## Execution Conditions

- Service: Muse chat, using synthetic text inputs only
- Actual Gmail, Google Calendar, or external-app operation: None
- Dots: Not run under current access conditions
- Response wait and human review/correction times were not separately timed. Do not estimate actual measurements. Task materials were fictional text, and calendar/email connectors were not opened.

## Results Table

| Item | Task A: schedule review | Task B: description draft |
|---|---|---|
| Execution complete | Complete | Complete; one revision request |
| Muse response wait time | Not measured | Not measured |
| Tool approval request | Not observed | Not observed |
| Human review/correction time | Not measured | Not separately measured; remaining wording needs review after one specific revision request |
| Core criteria met | All met | Format, length, and structure met; strict evidence limits partly unmet |
| Observation | Correctly distinguished five-minute overlap, 90-minute elapsed span, and 95-minute item total | Both draft and revision provided the requested structure, but some promotional wording absent from the input remained in the revision |
| Decision | **Usable** | **Usable with edits** |
| Evidence | Results matched the timetable and explicitly stated that events were unchanged | “plants thrive,” “make a real difference,” and “small refuge” in the first draft exceeded the evidence. Even after revision, phrases such as “follow along at your own pace,” “try what feels manageable,” and “a small, gentle start” remained, requiring final editing. |

## Task A — Fictional Event Timetable

Muse identified a five-minute overlap between the short talk and tool demonstration at 09:35–09:40. It also distinguished the 90-minute elapsed time from first start to final end from the 95-minute sum of individual durations. It explained the five-minute difference as overlap and responded that it had not touched the schedule. All four success criteria were met.

## Task B — Fictional Broadcast Description

The first response provided a title, a description labeled by Muse as 121 words, three key points, and three hashtags. The format was correct, but it added plant-growth/space-arrangement effects and a “small refuge” for pollinators that were absent from the input.

> “the plants thrive with less fuss” — “small habits that make a real difference” — “your balcony can become a small refuge for pollinators”

We requested one revision, specifically identifying wording that exceeded the evidence. Muse returned a revision labeled as 106 words, along with the required three bullets and hashtags. However, it still included audience actions and encouragement absent from the input. Core editing therefore remains a human task, and the decision is “usable with edits.” Only fictional materials were used so no separate fact-checking or external-source verification would be needed.

## Human Review Cost

Response wait and human review/correction times were not recorded separately during execution. Since manual-work baseline time was also unmeasured, no time savings are calculated. In the next comparative exercise, record timer start/end points and correction scope first.

## Screen Record

Below is part of the screen showing the revised result for synthetic task B. Only conversation content was cropped and saved to exclude real account information.

![Muse's revised response to the fictional Maple Lab task.](../assets/muse-task-b-review.png)

## Limits of Privacy Isolation

Even with synthetic inputs and no external connectors opened, the possibility that the service consults saved memory or context needs separate checking. For strict isolation, inspect the service's memory-use indicators and settings or use a separate test environment without memories. This document does not record account-specific memory contents or states.

## Apply in the Next Run

- Independently verify answers in factual-judgment tasks.
- Score format compliance and evidence limits separately in generation tasks.
- Do not assume “use only the notes” eliminates extra rhetoric or promotional wording.
- To claim time savings, actually measure both human baseline work and review time separately.
