---
title: "Choosing an Artifact Capability"
created: 2026-10-06 00:00:00
tags:
  - claude-artifacts-routines
  - m3
  - concepts
---

## The short rule

Choose based on **who needs to see the data**. Use browser storage for something only you need to remember; use `artifact` when the page itself is the record; use `db` when multiple people and Claude need shared read/write access. This reflects runtime contract 0.2.60; ✅ marks capabilities tested on 2026-09-27.

## Selection table

| Need | Capability | Who can see it? | Test |
|---|---|---|---|
| Remember the last tab or collapsed section | Browser storage (`localStorage`) | Only that person in that browser; not other people or Claude | — |
| A poll or checklist where the page itself is the record | `artifact` (page republishes a new version) | Everyone who opens the page | — |
| Shared live data that people and Claude can read/write | `db` | Authorized people in the organization and Claude sessions | ✅ Counter and round-trip test |
| Private per-person notes or votes | `db` at `data/users/<id>/` plus `user` | That person only; even the author cannot see another user's data | — |
| Identify the viewer or check edit permissions | `user` | — | ✅ Example 2 |
| Images, PDFs, or floor plans | `assets` | People who can access the artifact (within the organization) | ✅ Session upload and page display |
| Collect feedback on sections and send it to Claude | `comments` (`composer_only` is the lightest option) | The claude.ai interface displays the comment list | ✅ Three sections; automatic Send to Claude reply |
| Keep CSS, JS, and data in separate files | Publish them together with the `files` parameter (not a capability) | Same as the page | ✅ Example 5 |
| Cursors or signals among current viewers | `room` (not persisted) | People currently viewing | — |
| Ask Claude from the page | `sample` (viewer consent and usage) | — | — |

## Sharing limits

`db`, `assets`, and `user` prevent public-link sharing and are organization-only. `comments` with only `composer_only` can be public. Pages without capabilities can be shared publicly.

## Ten-second design exercise

For “make a status board during the meeting,” where several people edit it and Claude summarizes it afterward, use **`db`**. Add **`user`** if the editor identity matters, and pin session writes with **`if_version`**.

[한국어 원문](capability-selection-table.md) · [M3 overview](../README_en.md)
