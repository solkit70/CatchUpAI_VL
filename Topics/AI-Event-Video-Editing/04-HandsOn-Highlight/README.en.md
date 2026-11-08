---
title: "M4 — First Hands-On Round of Local Talk Splitting"
author:
  - "Codex"
created: "2026-10-24 23:43:17"
tags:
  - ai-event-video-editing
  - hands-on
lang: en
---

## M4 — Talk Splitting and Highlight Hands-On

[한국어](README.md)

**Status:** Seven local talk-split drafts were made. After the user finished reviewing four boundary review clips, a 2 min 27.7 s excerpt summary cut draft of Talk B was added. This is one method that uses the existing transcripts, sample frames and FFmpeg. After that, Vidio Free produced a first edit from a 5-minute sample and a Korean instruction. The Vidio v1 file was verified at 126.912 s and 1280×720, but it fell short of the target length. The Korean revision v2 became even shorter at 1:13 shown in the UI and dropped all of the PR explanation, so it did not meet the request. The actual video and footage of people are stored locally, outside the public Topic.

## Order to Read and Run

1. [M4 comparison conclusion](results-comparison.en.md) — Read first: the differences among the four results, the user's assessment, the scope of the time measurements, and the unverified conditions.
2. [Method A and the talk segment table](method-A.en.md) — Check the reasons for the choices and the verification results of local splitting and the excerpt summary cut.
3. [Split script](split_presentations.py) — Reproduces the talk splitting without overwriting existing outputs.
4. [Summary render script](render_highlight.py) — Reproduces the local excerpt summary cut.
5. [Vidio actual test and revision record](method-B.en.md) — Read about the automatic edit, the failed automatic revision, the manual restoration, and how far the download was confirmed.
6. [Latest M4 WorkLog](../vl_worklog/20261025_M4_AI-Event-Video-Editing.md) — Check how the run went and the actual DoD status.

## Completed Scope

Seven local split drafts, four boundary review clips, a 147.714 s local summary cut, and the 126.912 s Vidio v1 file were made and verified. The user found the key selections similar but slightly preferred the local one for its ending. The Vidio automatic revision v2 did not meet the request at 1:13 shown in the UI. The later manual v3 was confirmed with 12 restored items, 2:30 shown in the UI, and Saved, and the user rated it as good.

The comparison conclusion and the assessment table are written. The original DoD is 5/7. A comparison with identical wording fixed in advance and a set of step screenshots for a full manual are not done. The v3 local file, confirmation of the A join, Korean speech, long originals, Premiere handoff and the user's self-assessment are separately unverified. The file-verified local v1 is set as the baseline for the next demo.

## Navigation

- Previous: [M3 hands-on trial plan](../03-Recommendation/test-plan.en.md)
- Current: [Roadmap M4](../vl_roadmap/20261017_RoadMap_AI-Event-Video-Editing.md#m4---체험-①--긴-영상에서-3분-하이라이트-자동-편집)
