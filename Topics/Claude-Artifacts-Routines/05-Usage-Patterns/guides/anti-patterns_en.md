---
title: "Artifacts and Routines Anti-Patterns — Only What We Experienced"
created: 2026-09-27 16:45:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m5
  - anti-patterns
---

## Rule

**Record only what we actually experienced.** Include a date and source for each item. When a new incident happens, add one row at the bottom and include the corresponding [pattern-card](patterns_en.md) number if one exists.

## List

| # | Date | What we did (what not to do) | What happened | Do this instead | Pattern | Source |
|---|---|---|---|---|---|---|
| 1 | Sep 7 | After editing a page, checked only **my own screen** before sharing | Other people saw an old version (shared version was pinned) | Set shared version to Latest and check in incognito | 6 | [M2 troubleshooting](../../02-Artifacts-Sharing-and-Versions/troubleshooting/shared-link-shows-old-version_en.md) |
| 2 | Sep 13 | Sent a link to a **DB-backed page** to someone who would not sign in | “Sign in to view this page”—even if public, data is available only to signed-in users | Make a separate static snapshot for sharing | 1 | [M1 inventory](../../01-Inventory-and-Questions/guides/inventory_en.md) · [M2 sharing matrix](../../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix_en.md) |
| 3 | Sep 13 | **Did not record the Artifact URL in the vault** when it was created | Three of seven real artifacts were nowhere in the vault, including two pages explaining these features | Record the URL in the Task Board/Roundup on the day it is created | — | [M1 inventory](../../01-Inventory-and-Questions/guides/inventory_en.md) |
| 4 | Sep 12 | Edited the static snapshot contents but left the **“last synced” label unchanged** | Contents were edited Sep 12, but banner still said “09-10 15:20” | Update the date label whenever the snapshot is updated | 1 | [M1 inventory, A2](../../01-Inventory-and-Questions/guides/inventory_en.md#six-artifacts) |
| 5 | Sep 7–21 | Gave a conditional-notification routine **weak failure reporting** (one short push) | Three weeks of failures looked just like “no postings.” The routine had already written the cause in Sep 14 log. | Route failure through another channel such as email; have a person inspect the log monthly | 3 | [WBLP routine audit](../../04-Routines-Lab/guides/wblp-routine-audit_en.md) |
| 6 | Sep 21 | Put external API parameters (`loc_query=`, `country[]=`) in a prompt **without verifying them** | amazon.jobs silently ignored both; two queries returned the same result | Check locally whether each parameter applies (`filterFacets`) | 5 | [WBLP routine audit](../../04-Routines-Lab/guides/wblp-routine-audit_en.md) |
| 7 | Sep 21 | **Guessed** where the environment settings were and gave that as the path | The user went to the wrong place twice (three captures, 12 minutes) | If unsure, check documentation or ask for a capture first | 5 | [M4a WorkLog](../../vl_worklog/20260921_M4a_Claude-Artifacts-Routines.md) |
| 8 | Sep 27 | Published lab examples in the same session watching production artifacts | Session watch limit was 10; Booth Manager/Status Board watches and comment auto-replies were displaced | Publish lab examples in a separate session | — | [M3 troubleshooting](../../03-Artifacts-Capabilities-Lab/troubleshooting/cdn-and-storage-gotchas_en.md) |
| 9 | Sep 3 (reviewed Sep 27) | Embedded floor-plan images **as base64 in the HTML** | Page was 246 KB; one line was about 100,000 characters, making edits/review cumbersome | Upload images as assets and reference `/_blob/<id>` | — | [Booth Manager review](../../03-Artifacts-Capabilities-Lab/guides/bighug-artifacts-review_en.md) |
| 10 | Sep 13 (corrected Sep 27) | Read one sentence in documentation and closed a feature as **“unavailable on this account”** (comments) | Sep 27 test showed comments and Send to Claude worked; the record contained a wrong conclusion for two weeks | Test a minimal example before concluding “unavailable” | — | [M2 sharing-matrix correction](../../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix_en.md) · [M3 lab log](../../03-Artifacts-Capabilities-Lab/guides/lab-log_en.md) |

## Near misses (documentation only)

| What could be done | Risk | Evidence |
|---|---|---|
| Several people use page-side “read, add 1, write” at the same time | An increment can be lost (last write wins) | `[documentation]` `db.d.ts`; simultaneous clicks were not tested. |
| Include every connector by default in a Routine | Included connectors can make writes without asking again | `[documentation]` Routines. The second routine retained only Calendar and Gmail. |

[Korean original](anti-patterns.md) · [M5 overview](../README_en.md)
