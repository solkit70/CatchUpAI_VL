---
title: Phase 1 Final Q&A Test - Bila AI Agent
created: 2026-07-26 07:15:04
tags:
  - bila-ai-agent
  - qa-test
  - m2
---

## Test Purpose

This sheet records the final Phase 1 validation after GitHub and Google Drive are connected. Passing means Bila can answer at least 7 of 10 realistic Builders Lounge questions with appropriate evidence and without guessing.

Source context: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_worklog/20260705_M2_Bila-AI-Agent|M2 previous WorkLog]].

## Scoring Rubric

| Score | Meaning |
|------:|---------|
| 3 | Accurate, source-aware, and directly useful. |
| 2 | Mostly correct but missing source detail or some useful context. |
| 1 | Partially relevant but weak, vague, or not source-grounded. |
| 0 | Incorrect, fabricated, or unable to answer when source data exists. |

Pass condition: at least 7 questions score 2 or 3, and no answer fabricates a source.

## Test Questions

| # | Question | Expected Source Path | Result | Score | Notes |
|---:|----------|----------------------|--------|------:|-------|
| 1 | 2025 Vibe Coding Bootcamp 폴더 테스트 문서에 적힌 테스트 코드가 뭐예요? | Google Drive marker file | Pending | | Expected exact code: `DRIVE-TEST-7749` |
| 2 | 김성수님 HebronGuide가 뭔가요? | GitHub `ideas/` file | Pending | | Should cite GitHub file path if available. |
| 3 | Nate Cho님의 Job Search Co-pilot은 어떤 제품인가요? | GitHub `ideas/` file and README link | Pending | | Regression check for README-linked retrieval. |
| 4 | Builders Lounge 멤버는 누가 있나요? | GitHub README or member list | Pending | | Should avoid overclaiming if list is partial. |
| 5 | BL 다음 모임은 언제인가요? | Space posts or Drive meeting notes | Pending | | Should use dated source, not guess. |
| 6 | 지난 모임에서 결정된 사항은 무엇인가요? | Drive meeting notes | Pending | | Drive retrieval test. |
| 7 | BL에 새로 가입하려면 어떻게 해야 하나요? | Space posts or project plan | Pending | | Should distinguish confirmed process from unknowns. |
| 8 | BL에서 진행 중인 프로젝트에는 어떤 것들이 있나요? | GitHub `ideas/`, Space posts | Pending | | Should summarize with examples. |
| 9 | 발표 영상이나 자료 링크가 있나요? | GitHub, Drive, or Space posts | Pending | | Should provide links only if found. |
| 10 | Bila AI는 지금 무엇을 도와줄 수 있나요? | System prompt + connected data scope | Pending | | Should state Phase 1 scope clearly. |

## Summary

| Metric | Value |
|--------|-------|
| Questions tested | 0 / 10 |
| Score >= 2 | 0 |
| Fabrication count | 0 |
| Pass / Fail | Pending |

## Observations

- Pending post-fix Drive reconnection.
- Pending final Q&A run.
