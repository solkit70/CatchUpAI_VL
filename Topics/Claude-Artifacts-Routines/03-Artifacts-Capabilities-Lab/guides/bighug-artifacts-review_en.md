---
title: "M3 Exercise 3 — Booth Manager Review (No Changes Made)"
created: 2026-10-06 00:00:00
tags:
  - claude-artifacts-routines
  - m3
  - review
---

## Conclusion

No changes were made. The event had ended (Sep 26), and the booth manager had served its purpose. This review records what might change in a similar future build. The artifact was read in-session but not republished.

## Review

| Area | Existing implementation | M3 learning | If built again |
|---|---|---|---|
| Shared state | `db`, with `booths` collection and `meta/activity`; no localStorage | Database suits data shared among people | Keep it |
| Runtime version | Contract 0.2.41 at publication; lab used 0.2.60 | Consider `contract: "latest"` if republishing |
| Floor-plan images | Two maps embedded as base64 `data:image/jpeg`; page was 246 KB and included a ~100k-character line | `assets` can keep HTML small and reference `/_blob/<id>` | Store maps as assets |
| Who changed what | Activity log, but no `user` capability | `user.id()` can record the editor ID; `profiles()` can resolve names for display | Add user IDs to activity log |
| Feedback | No comments | `composer_only` comments are lightweight; a session can reply via Send to Claude | Add a per-booth comment button |
| Concurrent edits | Page uses last-write-wins | Session writes can use `if_version` | Pin session writes with `if_version` |

The booth manager had already made the most important choice correctly: shared state used `db`. The two omissions—moving images to `assets` and recording editor IDs—did not cause an operational problem during the event. This table can guide the next event tool.

[Korean review](bighug-artifacts-review.md) · [M3 overview](../README_en.md) · [Capability choices](../concepts/capability-selection-table_en.md)
