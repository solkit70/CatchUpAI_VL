---
title: "M3 — Artifact Runtime Gotchas"
created: 2026-10-06 00:00:00
tags:
  - claude-artifacts-routines
  - m3
  - troubleshooting
---

## Directly observed (2026-09-27)

| Symptom | Cause | Response |
|---|---|---|
| Comment auto-replies stopped on an artifact after several examples were published | One session watches at most **10 artifacts**. New examples displaced older watched items such as the booth manager and status board. | Publish lab examples in a separate session from the one watching production artifacts. If displaced, re-add with `ArtifactComments` `watch` when needed. |
| Session database write was rejected with `version_mismatch` | The page or another session changed the document after it was read. | Expected protection: reread and write against the new version. See [the round-trip test](../guides/db-roundtrip_en.md). |
| Writing several Korean HTML files with a long Git Bash heredoc failed with `unexpected EOF while looking for matching '` | Quote parsing broke in the long heredoc sequence (twice that day). | Write each file separately with a file-writing tool. |

## Checked in runtime contract 0.2.60

| Gotcha | Rule |
|---|---|
| External scripts and fonts | Scripts are allowed only from listed sources such as cdnjs, jsDelivr, and unpkg; stylesheets only from Google Fonts. Other requests are blocked silently. |
| `localStorage` | Stored only in the viewer’s browser; unavailable to other people, devices, or Claude. It may be empty or throw in an incognito session. Use it for convenience such as remembering a tab. |
| Artifacts declaring `db`, `assets`, or `user` | Organization-only sharing; no public link. `comments` with only `composer_only` can be public. |
| Direct access such as `window.claude.db` | Not available. Always use `await claude.use("db")` and hide the feature if the result is `null`. |
| Page-side counter increment | Last write wins; simultaneous increments can lose an update. |
| `alert()`, `confirm()`, and `prompt()` | They do not display normally (`confirm` returns false and `prompt` returns null). Build confirmation UI inside the page. |

[한국어 원문](cdn-and-storage-gotchas.md) · [M3 overview](../README_en.md)
