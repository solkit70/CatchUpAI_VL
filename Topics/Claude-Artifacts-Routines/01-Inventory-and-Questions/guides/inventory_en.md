---
title: "Inventory of Existing Work — Six Artifacts and One Routine (Observed 2026-09-13)"
created: 2026-09-13 06:25:00
tags:
  - claude-artifacts-routines
  - m1
  - inventory
---

## First discovery — seven items, not four

The case index counted **three artifacts and one routine**. Running the `Artifact` tool with `action: list` returned **six artifacts** (observed 2026-09-13 at 06:22). The three missing artifacts had all been created between Sep 1 and Sep 8. Two were pages explaining these very features, made for the Datacenter and Caregiver capstone videos. Their URLs had not been recorded anywhere in the vault’s Task Board or Journal.

> There were real artifacts that had never been recorded in the vault. The gallery was the original; the vault was its shadow. This is the first assumption this topic needed to reverse.

## Six artifacts

| # | Artifact | Created · last edited | Purpose and capabilities | Incognito result | Still in use? |
|---|---|---|---|---|---|
| A1 | [Booth Manager](https://claude.ai/code/artifact/991fb41f-5007-4f15-9c3b-429ab0e33b2a) 🗺️ | Sep 3 · **Sep 10** | BigHug booth-layout editor. Uses **`db`**; pin dragging, seat swaps, and activity log are stored in the database (observed `write_db` use on Sep 3 and 12). | 🔒 “Sign in to view this page” (Sep 13 incognito test) | ✅ Through the Sep 26 event |
| A2 | [Booth Status Board](https://claude.ai/code/artifact/aa2d46bf-d01c-4864-96c2-9257c7bd3e0e) 📋 | Sep 3 · **Sep 10** (v11) | Static snapshot, no `db`. On Sep 12 the HTML was directly edited to move booths, merge pins, and mark the restroom. | ✅ Opened with latest edits (Sep 12: Tous les Jours at booth 1, booths 3/4 OPEN, restroom). ⚠️ Banner still said “Last synced 09-10 15:20,” not updated with the Sep 12 edits. | ✅ Shared with the team |
| A3 | [Could We Become Caregivers?](https://claude.ai/code/artifact/1fca682e-195a-4934-b593-84e4af2e5dc4) 🏡 | Sep 8 | One-page result of caregiver research—the page behind “I only sent my wife a link” (page content dated Sep 1). Capabilities not yet checked. | ✅ Opened; Updated Sep 7, 2026; Korean/English toggle (Sep 13 test). | Shared with family |
| A4 | [Builders Lounge Event Entry Guide](https://claude.ai/code/artifact/e9c029bd-e072-45a9-9618-a47881af3676) 🚪 | Sep 7 (version 3) | Guide reused in newsletter, Slack, and Gobi announcements. Incognito test on Sep 7 confirmed v3 was served. | ✅ Opened, latest version (rechecked Sep 13). | ✅ Through the sixth meetup |
| A5 | [What Runs When I’m Away](https://claude.ai/code/artifact/01289ae4-44b5-461f-8c44-b1d75f9d9ef9) 🔁 | Sep 2 | Routines explainer: WBLP example, eight-week timeline, “the key is what it does not do,” and limitations (no local-computer access, one-hour minimum, connected services only, deletion only on the web). Private according to list output. | 🔒 Sign-in required; matched the private state from list. | Video reference |
| A6 | [A Webpage from the Terminal](https://claude.ai/code/artifact/f69047c1-e380-478e-b169-15f0e48b512f) 🔗 | Sep 1 | Artifacts explainer: sharing-scope table (private by default / anyone with link), versions, comments, “it is not limited to static pages”; source was in a note. Private. | 🔒 Sign-in required (Sep 13). | Video reference |

**How capabilities were checked:** `Artifact read` returns the HTML; calls to `window.claude.*` reveal database/user use. A1 and A2 were confirmed through direct edits in the Sep 12 session. A3 was checked in M2.

**Incognito check (Sep 13; user opened six tabs in Chrome Incognito):** all six predictions matched. A1 (with `db`) and A5/A6 (private) displayed “Sign in to view this page”; the other three opened. This was the first direct observation behind M2 question 1. A page using `db` required sign-in in this state; M2 investigated whether that was structural or a sharing setting.

An additional issue: A2’s top banner said “Read-only snapshot · Last synced 2026-09-10 (Thu) 15:20.” The contents were changed on Sep 12 without updating the banner. A static snapshot’s “as of” label must be updated manually; this became a candidate for the M5 anti-pattern list.

The session’s `curl` could not reach the external network (HTTP 000), so it could not simulate unauthenticated access. The user opened the pages directly in an incognito window.

## One routine

| # | Routine | Created | Configuration | Run history | Still in use? |
|---|---|---|---|---|---|
| R1 | [AWS WBLP weekly check](https://claude.ai/code/routines/trig_01LKgvHWt4ZfJbTqJgn5KvVT) | Sep 1 | Mondays at 08:00 PT; four `amazon.jobs` search JSON endpoints; email only when Washington postings or U.S. technical, data-center operations, or fiber roles appear (Task Board, Sep 1). | ⬜ **Unverified** — a Sep 8 run should exist. User to check at claude.ai/code/routines (M4 exercise 1). | ✅ |

## Claims already made by A5 and A6 — M2/M4 verification list

The two explainer pages were written on Sep 1–2 from experience and knowledge available at the time, without checking official documentation. Each statement below needs evidence from documentation or a direct test.

| Claim in source page | Source | Module | Evidence at inventory time |
|---|---|---|---|
| “It is not public as soon as you create it. At first only you can see it; you must enable sharing in the Share menu.” | A6 | M2 | Sep 1 experience; matches `private` in list output |
| “Anyone with the link” can view; “it does not appear in search.” | A6 | M2 | Inference |
| “The URL stays the same when you edit; a new version is created at that URL”; “you can choose which version to share.” | A6 | M2 exercise 3 | Partially observed with v3 on Sep 7 |
| “A page remembers what visitors enter, with different limits for each account.” | A6 | M2/M3 | Inference; this is the original database-sharing question |
| “Send a visitor’s comment to AI and it can reply or edit in place.” | A6 | M2 exercise 3 | Tool description only; not tested |
| “It cannot access my computer; it is a separate session running in the cloud.” | A5 | M4 | Sep 2 experience; candidate M4 exercise (a) was whether a Deadline routine requiring vault files could work |
| “Minimum interval is one hour”; “connected services only”; “delete only on web, pause/edit in conversation.” | A5 | M4 | Sep 2 experience |
| “Results arrive by email and a dedicated page, with a record for each run.” | A5 | M4 exercise 1 | Sep 2 experience; verify against run history |

[Korean original](inventory.md) · [M1 overview](../README_en.md)
