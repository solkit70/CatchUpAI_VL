---
title: "M3 Exercise 2 — Database Round Trip and `if_version` Conflict Test"
created: 2026-10-06 00:00:00
tags:
  - claude-artifacts-routines
  - m3
  - db
---

## Summary

A stale-version write was rejected, and nothing was written. In four initial calls, the Claude Code `ArtifactData` tool read the `counter/main` document, wrote with a version, and deliberately retried against an old version. The full page/session round trip then confirmed conflict handling.

## Observed sequence (2026-09-27)

| Step | Operation | Result |
|---|---|---|
| 1 | `get counter/main` | No document existed; this is reported as “No document,” not as a fatal error. |
| 2 | `set` `{value: 10}` without `if_version` | Committed; version 1. |
| 3 | `update` `{value: 11}` with `if_version: 1` | Committed; version 2. |
| 4 | `update` `{value: 999}` with stale `if_version: 1` | Rejected as `version_mismatch`; document remained at version 2. |
| 5 | `list counter` | Value remained 11; 999 was never written. |
| 6 | `list counter` at `as_level: interact` | Shared document remained visible to a Contributor under the default rules. |
| 7 | User clicked **+1** twice in the page | Page wrote two updates; versions 3 and 4. |
| 8 | Session read `counter/main` | Read value 13, `by: "page"`, version 4. The session saw the page’s writes. |
| 9 | Session wrote value 12 with its stale version 2 | Rejected; current version was 4. This reproduced a real person/AI conflict. |
| 10 | Session reread and wrote value 14 with `if_version: 4` | Committed at version 5. |

## What this shows

Document versions start at 1 and increase on every write. `if_version` lets the server check whether someone changed the document since it was read: pin the write to the known version, then reread and replan if rejected. Page-side writes do not expose this guard and use last-write-wins; two people incrementing one shared counter at once can lose an increment. Use per-person documents and aggregate them, or serialize writes with `acquire`. The `db.d.ts` update note explicitly warns: “Do NOT build monotonic counters from read-modify-update.”

The conflict error itself gives the recovery path: read the current document, replan against it, and pin the new write to that version.

## Round trip complete

The session wrote 11 and the page read it; the page then wrote 13 at version 4 and the session read it. A session write based on stale v2 failed during the real conflict, while a write based on reread v4 succeeded at v5 with value 14.

> When a person edits the page while an AI session edits the same data, `if_version` prevents the AI from overwriting the person’s change. It is the first safety mechanism to check when delegating artifact data work to AI.

[한국어 원문](db-roundtrip.md) · [M3 overview](../README_en.md)
