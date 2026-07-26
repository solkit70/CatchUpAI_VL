---
title: Google Drive Connection Guide - Bila AI Agent
created: 2026-07-26 07:15:04
tags:
  - bila-ai-agent
  - google-drive
  - m2
---

## Purpose

This guide documents the post-fix Google Drive reconnection test for Bila AI Agent. The previous blocker was that selecting a Drive folder appeared to work in the picker, but the selected folder was not visible after leaving and re-entering GobiSpace Agents settings. The user reported on 2026-07-26 that this bug has been fixed, so the next step is controlled retesting.

Source context: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_worklog/20260705_M2_Bila-AI-Agent|M2 previous WorkLog]].

## Target Environment

| Item | Value |
|------|-------|
| Space | Changbal |
| Agent | Bila AI |
| Settings URL | `https://www.gobispace.com/spaces/changbal/settings?tab=agents` |
| Test folder | `My Drive / 2025 Vibe Coding Bootcamp` |
| Marker file | `drive-test-marker.md` |
| Expected marker code | `DRIVE-TEST-7749` |

## Reconnection Steps

1. Open GobiSpace `Changbal` space settings and go to `Settings -> Agents`.
2. In the Google Drive section, choose `My Drive / 2025 Vibe Coding Bootcamp`.
3. Confirm whether the UI now shows a persistent connected/attached state for the selected folder.
4. Leave the Agents tab, then re-enter it.
5. Confirm the folder selection remains visible after re-entry.
6. If the marker file is not already in the Drive folder, upload [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_materials/drive-test-marker|drive-test-marker]].
7. Ask Bila AI the verification question below.

## Verification Question

```text
2025 Vibe Coding Bootcamp 폴더 테스트 문서에 적힌 테스트 코드가 뭐예요?
```

Expected answer: Bila should find the Drive marker file and answer `DRIVE-TEST-7749`.

## Result Log

| Check | Result | Evidence |
|------|--------|----------|
| Folder selection persists after re-entry | Pending | |
| Bila calls Drive search tool | Pending | |
| Bila finds marker file | Pending | |
| Bila answers `DRIVE-TEST-7749` | Pending | |

## Failure Triage

If the folder persists but Bila cannot find the marker, record the exact tool call shown by Bila. The 2026-07-12 failure called `Glob "/gdrive/2025 Vibe Coding Bootcamp/**/*"` but returned zero files, so a repeated zero-file result after persistence would point to indexing, permission, or path-mapping rather than folder-save persistence.

If the folder does not persist, reopen the GOBI bug as a regression and include the steps above with today’s date.
