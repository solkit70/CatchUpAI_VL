---
title: "Eight Runtime Capabilities on This Account (contract 0.2.46)"
created: 2026-10-06 00:00:00
tags:
  - claude-artifacts-routines
  - m2
  - concept
---

This is what `Skill: artifact-capabilities` served to this account on 2026-09-13. Capabilities can vary by account and date. The source clipping is in `vl_materials`.

| # | Capability | What it does | When to use it | Public sharing |
|---|---|---|---|---|
| 1 | `artifact` (formerly `self`) | Page republishes itself as a new version, keeping state in HTML | Polls, checklists, or boards where the page itself is the record | Possible |
| 2 | `db` | Server-side JSON documents shared among viewers; `data/users/<id>/` is private per user; sessions can use `read_db/write_db` | Data outside the page, data Claude will read later, or multiple editors | Page only; data requires sign-in |
| 3 | `assets` | Upload images, PDFs, fonts, CSS/JS (20 MiB) | Large images instead of data URIs | Not allowed; organization internal |
| 4 | `downloads` | Lets viewers download files made by the page, with a confirmation dialog | CSV export | Not confirmed |
| 5 | `mcp` | Calls tools through the viewer’s own connectors, with viewer consent | Live-data dashboards | Not allowed |
| 6 | `room` | Ephemeral realtime events/presence among current viewers; nothing is stored | Cursors, reactions, “view together” | Not confirmed; same-organization premise |
| 7 | `sample` | Page asks Claude a question; viewer consents and incurs usage | AI features inside a page | Not confirmed |
| 8 | `permissions` (built in) | No declaration required; checks or requests multiple permissions | Bundled permission requests | — |

**Review point for the booth manager (M3):** Its edits live in a database. If “the page is the record,” `artifact` republish may fit better and can be publicly shared. If several people edit and Claude must read the shared state, `db` is the better match; the current use is closer to the latter.

[한국어 원문](capabilities-roster.md) · [M2 overview](../README_en.md) · [M3 capability selection](../../03-Artifacts-Capabilities-Lab/concepts/capability-selection-table_en.md)
