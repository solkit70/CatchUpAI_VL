---
title: "Artifacts and Routines Usage Patterns — What to Do in These Situations"
created: 2026-09-27 16:40:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m5
  - patterns
---

## How to read these cards

Only directly observed results are stated as patterns. Evidence labels mean: `[observed date]` = directly tried and checked in this topic; `[docs]` = official documentation; `[inference]` = not yet verified (a candidate, not a pattern). Every card links to an artifact or record.

## 1. If the goal is sharing, start with a static page

| | |
|---|---|
| **Situation** | A person who is not signed in (someone outside the team, family, event attendees) needs to view the page from one link. |
| **Do** | Build and share a **static page without `db`**. Keep the editing/data tool separate, and publish a snapshot from it for sharing. |
| **Avoid** | Sending a database-backed editing tool as the public link. Someone who is not signed in will see “Sign in” or an empty shell. |
| **Examples** | Booth Manager (`db`, for editing) and Booth Status Board (static, for sharing) were split into two pages. See [M1 inventory](../../01-Inventory-and-Questions/guides/inventory_en.md). |
| **Evidence** | `[observed 9/13]` Six incognito checks: three `db`/private pages prompted sign-in; three others opened. `[observed 9/13]` M2 2×2 test: [sharing matrix](../../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix_en.md). `[observed 9/27]` `db`, `user`, and `assets` declarations could not use public links. |

## 2. Use `if_version` when an AI session edits Artifact data

| | |
|---|---|
| **Situation** | A Claude session reads and edits a database that people are using in the page (status updates, bulk edits). |
| **Do** | Include the `version` received when reading as `if_version` on the write. If rejected, reread and replan. |
| **Avoid** | Overwriting without a version. Also avoid making a shared incrementing number with page-side “read, add 1, write”; page writes use last-write-wins. |
| **Example** | [DB counter](https://claude.ai/artifact/8p4xaEhHXB6PQyzDZfy3os) and [round-trip record](../../03-Artifacts-Capabilities-Lab/guides/db-roundtrip_en.md). |
| **Evidence** | `[observed 9/27]` After a person changed v2 → v4 on screen, the session’s v2 write was rejected with `version_mismatch`; retry with v4 succeeded. `[docs]` `db.d.ts` says, “Do NOT build monotonic counters from read-modify-update.” |

## 3. Choose conditional or always-on notifications based on the purpose

| | |
|---|---|
| **Situation** | A routine checks something and sends email. |
| **Do** | If it runs often and usually finds nothing, make the result email conditional to avoid notification fatigue—but explicitly send failures through another channel (push or failure email). If it runs rarely or execution itself must be visible, always send a report. |
| **Avoid** | Making only the success email conditional and leaving failure handling empty; success and failure both become “no news.” |
| **Examples** | [Weekly WBLP check](https://claude.ai/code/routines/trig_01LKgvHWt4ZfJbTqJgn5KvVT) (conditional) and [tomorrow’s calendar preview](https://claude.ai/code/routines/trig_01TyCwrfL1H3vsmdkmcDS8xk) (always reports). |
| **Evidence** | `[observed 9/21]` Three weeks of WBLP failures were indistinguishable from “no jobs”: [audit](../../04-Routines-Lab/guides/wblp-routine-audit_en.md). `[observed 9/27]` The second routine emailed even with zero events, making execution immediately visible: [second routine](../../04-Routines-Lab/guides/second-routine_en.md). |

## 4. Use local for vault work and cloud for external-only work

| | |
|---|---|
| **Situation** | Someone asks for “X every day/week.” |
| **Do** | Use **local AI4PKM cron** when reading or writing vault files; use a **cloud routine** when it only needs external web, email, or calendar and should run while the PC is off. Split the task if it needs both. |
| **Avoid** | Putting work that needs vault files into a cloud routine; it clones only the selected GitHub repository. |
| **Examples** | GDR and TIU are local; WBLP and calendar preview are cloud. See [decision table](../../04-Routines-Lab/concepts/local-vs-cloud_en.md). |
| **Evidence** | `[docs]` “Each repository is cloned at the start of a run.” `[observed 9/27]` A routine without a repository logged “No sources configured.” |

## 5. If a cloud routine cannot reach an external site, check environment networking first

| | |
|---|---|
| **Situation** | A check that works on the local PC fails in a routine. |
| **Do** | (1) Open logs with `list_runs` and `get_run_log`; (2) reproduce the same request on the PC; (3) inspect environment **Network access** (`Default` = Trusted = allowlist only). Gmail and Calendar connectors are independent of the allowlist. |
| **Avoid** | Editing the prompt before opening logs, or trusting a green run status as success. |
| **Example** | WBLP recovery; see [routine troubleshooting](../../04-Routines-Lab/troubleshooting/routine-did-not-run_en.md). |
| **Evidence** | `[observed 9/21]` `connect_rejected (organization policy)` while local `curl` returned HTTP 200; routine succeeded 113 seconds after adding the domain. `[docs]` “A green status … does not mean the task in your prompt succeeded.” `[observed 9/27]` Connector-only routine worked under unchanged Trusted mode. |

## 6. Set shared links to the latest version and verify in incognito

| | |
|---|---|
| **Situation** | A shared page has been edited. |
| **Do** | Set the Share menu’s shared version to **Latest**, then verify in an **incognito window**. The author’s browser always shows the latest version and is not proof of what viewers see. |
| **Avoid** | Looking only at your own screen after editing and declaring the update visible. |
| **Example** | [Builders Lounge event entry guide](https://claude.ai/artifact/Vs9GEkCtEXsyRdT5kvyF7s)—after publishing v4 on Sep 25, the user changed the shared version to Latest. |
| **Evidence** | `[observed 9/7]` Another person saw an old version: [reanalysis](../../02-Artifacts-Sharing-and-Versions/troubleshooting/shared-link-shows-old-version_en.md). `[observed 9/25]` Latest was selected in the Share menu, answering the question left open in M2. |

## Candidates — not yet established patterns

| Candidate | Why it is not established yet |
|---|---|
| Build something during a meeting and use it in that same meeting | The record says the Booth Manager was built during the Sep 3 meeting ([M1 inventory](../../01-Inventory-and-Questions/guides/inventory_en.md)), but there is no comparative observation that it worked better as a result. `[inference]` |
| Give the goal and constraints, and let AI choose the tool names | One example from Sep 1; no counterexample was sought. `[inference]` |

[Korean original](patterns.md) · [M5 overview](../README_en.md)
