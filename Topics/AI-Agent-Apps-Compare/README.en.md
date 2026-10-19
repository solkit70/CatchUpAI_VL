---
title: "AI-Agent-Apps-Compare"
source: "[[20261004_RoadMap_AI-Agent-Apps-Compare#M5 - 판단 기준 · Topic README]]"
author:
  - "박창수"
  - "Codex"
created: "2026-10-11 07:38:08"
tags:
  - ai-agent-apps-compare
  - ai-agents
---

## What We Did in This Topic

[한국어](README.md)

We compared public materials and access conditions for four agents — Grok Bot, Muse, Dots, and Instinct — and reviewed first use and two synthetic tasks in Muse, the service we could actually access. The goal was to go beyond feature lists and decide what to delegate based on the nature of the work, its risks, and whether the results could be verified.

## Results Video

The results of this topic were made into a video (published 2026-10-14).

- Korean (12:06) — [Korean version](https://youtu.be/BQ_TVly3TZI)
- English (12:29) — [I Never Told It To, But Codex Put Muse to Work](https://youtu.be/zi1iNN3AEBw)

The production process is documented in [M6 — Results video](06-Capstone-Video/README.en.md).

## Livestream

[Watch the livestream covering this topic](https://youtube.com/live/isjIYk2184I). The broadcast was conducted in Korean.

## Key Results

- M2 compared each product's features, access, privacy, and permissions. Official evidence was separated from secondary material, and unverified items were not treated as settled.
- M3 recorded answer scope, time calculations, sources, and per-action permission checks in Muse. The initial Sources panel did not contain only official sources, so Meta's original URLs were checked again.
- M4's fictional schedule review correctly identified overlaps and time totals and was judged **usable**. The format-constrained description retained unsupported wording and was judged **usable with edits**. Response and human correction times were not separately measured, so no time savings were calculated.
- Muse was the only service directly run. Dots, Grok Bot, and Instinct were limited to public-material research, so no actual performance ranking was created.

> Muse identified a five-minute overlap between the short talk and tool demonstration at 09:35–09:40. It also distinguished the 90-minute elapsed time from first start to final end from the 95-minute sum of individual durations.
>
> — Observation recorded in the M4 results document. This is one task observation, not a guarantee about the service overall. [M4 results](04-Real-Task-Trial/guides/trial-results.en.md#task-a--fictional-event-timetable)

## Learning Modules

| Order | Module | Result |
|---|---|---|
| 1 | [Identify the services](01-Identify-Services/README.en.md) | Public identities, access conditions, and open questions for four services |
| 2 | [Build a comparison table](02-Comparison-Table/README.en.md) | Five-criteria comparison and evidence distinctions |
| 3 | [Muse first use](03-Hands-On/README.en.md) | Actual UI checks, read-focused task, permissions/source verification |
| 4 | [Delegate a piece of my work](04-Real-Task-Trial/README.en.md) | Run and evaluate two tasks using fictional materials |
| 5 | [Build decision criteria](05-Decision-Guide/README.en.md) | Selection guide by work, risk, and evidence level |
| 6 | [Produce the results video](06-Capstone-Video/README.en.md) | 24-scene slide plan → Korean and English videos published (10/14) |

## Selection Guide

The [M5 decision flowchart](05-Decision-Guide/guides/which-agent-when.en.md) asks in turn about data sensitivity, external-action risk, current access conditions, and whether results can be verified. For connected-app work, check permissions per action and separate reading/drafting from external changes. Synthetic inputs and not using external connectors do not by themselves establish isolation from saved memory; consider a separate memory-free test environment if strict isolation is needed. See [M4 isolation limits](04-Real-Task-Trial/guides/trial-results.en.md#limits-of-privacy-isolation).

## Scope and Limitations

M4 used fictional data only and did not open email/calendar connectors or publish posts. Baseline task time and human review time needed to demonstrate time savings were not measured. Since only two tasks in one service were run, do not generalize to other services or real-work outcomes. Access, pricing, and permission policies may change; recheck official materials and account screens immediately before execution.

## Capstone Video

The M6 video also introduced **how Codex directly operated Muse's screen, ran two synthetic tasks, captured the result screens, and inserted them into documents**. Screen evidence used only materials with personal schedules and account-specific permission states masked.

It also covered **asking Codex in VS Code an everyday question, after which it delegated work to Muse in the browser and received fall foliage recommendations in Korean**. The [delegation example and screen record](vl_materials/20261011_codex-muse-browser-delegation.md#관찰한-흐름) was also linked as a demonstration candidate for Senior-AI-Enablement.

## Key Materials

- [M2 comparison table](02-Comparison-Table/guides/comparison-table.en.md)
- [M3 setup and first task](03-Hands-On/README.en.md)
- [M4 execution results](04-Real-Task-Trial/guides/trial-results.en.md)
- [M5 decision flowchart](05-Decision-Guide/guides/which-agent-when.en.md)
- [M6 results video](06-Capstone-Video/README.en.md)
- [Topic final retrospective (Korean)](vl_worklog/20261019_AI-Agent-Apps-Compare_Final_Retrospective.md)
- [Roadmap](vl_roadmap/20261004_RoadMap_AI-Agent-Apps-Compare.md)
- [Official source list](vl_materials/official-sources.md)
