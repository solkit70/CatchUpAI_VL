---
title: "Sharing Scope 2×2 Experiment — Static vs. DB; Owner vs. Incognito (Answer to Question 1)"
created: 2026-09-13 07:35:00
tags:
  - claude-artifacts-routines
  - m2
  - experiment
---

## Experiment

Two minimal pages with the same design were published in one session (observed 2026-09-13 at 07:30). The only difference was one capability declaration.

| Artifact | Capabilities | Publish result | Source |
|---|---|---|---|
| [Static page experiment](https://claude.ai/code/artifact/3f864d29-c5c5-4d6c-b696-37fcc798ee62) 🔓 | `{}` | Version 1 · `sharing owner` | [minimal-static.html](../examples/minimal-static.html) |
| [DB page experiment](https://claude.ai/code/artifact/a3bb593a-c879-42c2-b996-e11cc167ec1d) 🔐 | `{db: {}}`; increments `probe/hits.count` every time it opens | Version 1 · `capabilities db · sharing owner` | [minimal-db.html](../examples/minimal-db.html) |

Immediately after publishing, both said **`sharing owner` (Only you)**, matching the official documentation: “A new artifact is visible only to you.” `[documentation]`

## 2×2 results — observed cells

| | Static (`{}`) | DB (`{db: {}}`) |
|---|---|---|
| **Owner’s browser** | ✅ Opened; `window.claude` existed (only `use`), observed 07:43. | ✅ Opened; `use("db")` returned a namespace; **count 1**, observed 07:43. Session `read_db probe/hits` returned `{count:1, last:"2026-09-13T13:43:24Z"}`, version 1. **The session read what the page wrote**—half of M1 question 6. |
| **Choices in Share menu** | People with access: Owner (me). General access: **Only you / Only people with access / Anyone with the link** (“People with the link can view, but not edit”), screenshot at 07:50. | **Exactly the same menu as static.** The **“Anyone with the link”** option was present; at the menu level, `db` did not prevent public sharing. |
| **Incognito — before sharing** | Not tested; since published as `sharing owner`, sign-in was expected. | Not tested; same expectation. |
| **Incognito — after enabling public link** | Not tested; DB case was sufficient to investigate question 1. | ✅ **Page opened** with label “Content is user-generated and unverified.” But `use("db")` returned **null** (“db is not available in this view”); count showed `—`; toast at bottom said **“Sign in to see this artifact's data · Sign in”** (screenshot at 07:58). |
| **Confirmation dialog for public sharing** | — | “Anyone with this link can view this artifact, even without a Claude account or sign-in. This includes people outside your organization. **People who sign in to Claude will also be able to read its data.**” (platform wording, observed 07:57). |
| **Another account, signed in** | | ⬜ Not tested. Per the dialog, data should be visible; M3 was to check this. |

## What was known from documentation before the test

| Evidence | Information |
|---|---|
| Official documentation `[documentation]` | An artifact page using the `mcp` connector cannot be public on any plan. Public link is the only sharing method on Pro/Max. **No statement about `db`.** |
| Session skill 0.2.46 `[documentation]` | `assets` declaration: “organization-internal (never public).” `mcp`: “bars public sharing.” **No sharing-scope statement for `db`**; access levels `interact/admin/owner` imply signed-in users. |
| Sep 3 experience `[observed]` | The booth manager (`db`) was said to be impossible to share by link. |
| Sep 13 incognito test `[observed]` | Booth manager prompted for sign-in. This alone could not distinguish “sharing was not enabled” from “sharing could not be enabled.” |

## Side finding — this account’s plan

The Share menu had **no organization option**—only “Only people with access” and “Anyone with the link” (observed). This matches the official statement, “On Pro and Max plans, a public link is the only way to share,” so the account is Pro/Max `[documentation + observation]`.

- The initial conclusion was **comments are unavailable on this account**, based on documentation that only artifacts shared within an organization take comments. Thus the comment item in exercise 3 was marked “not applicable.”
  - ⚠️ **Correction from M3 (2026-09-27):** The author added comments to an example declaring `comments` with `composer_only`, and the session automatically replied to a “Send to Claude” comment. See [M3 lab log](../../03-Artifacts-Capabilities-Lab/guides/lab-log_en.md). “Unavailable” had been inferred from one documentation sentence. Whether other people—outside the organization or public-link visitors—can comment remains unknown.
- Assigning editors was also considered unavailable for the same reason.
- A6’s Sep 1 explainer statement “visitors can leave comments” was considered **incorrect for this account**. The video should omit it or qualify it by plan.

## Answer to question 1

> **Why can’t an artifact with a database be shared by link? Is it a setting or structural?**

Both descriptions were partly right. The precise answer is: **page visibility and data visibility are separate.** `[observed Sep 13 + platform dialog]`

| Layer | After enabling a public link | Evidence |
|---|---|---|
| **Page (HTML)** | Anyone can view it; no login or account required | Opened in incognito; “Content is user-generated” label |
| **Database data** | **Only a signed-in Claude user** can read it. In an anonymous view, `use("db")` returns `null`. | Dialog: “People who sign in to Claude will also be able to read its data”; incognito toast: “Sign in to see this artifact's data.” |

Therefore, a page such as the booth manager, whose content comes entirely from `db`, still looks like an **empty shell** to anonymous visitors even after enabling a public link. That is what “the link cannot be shared” meant in the Sep 3 report. There is **no setting** in the dialog to let anonymous viewers read the data—this is a structural limit. Sharing the page itself, however, is a setting and can be enabled.

**Practical choices:** (1) make the page static, as with the booth status board; (2) put the essential content in HTML and use `db` only for supplemental state; or (3) require every viewer to sign in to Claude. This became M5 pattern 1.

**Still open:** verify that a different signed-in account can actually read the data, as the dialog says. M3 planned to test with a family account.

## Exercise 3 — versions, comments, and watch: what this account could test

| Item | Result |
|---|---|
| Comments | Initially marked **not applicable**: Pro/Max has no organization sharing and documentation said comments require it. Read → reply → resolve could not be tested under that assumption. Revisit if a Team/Enterprise account becomes available; M3 later corrected the comments conclusion for the author-side test. |
| Editors | Not applicable for the same reason. |
| Watch | Maximum **5 per session** (observed). Four artifacts handled that day were rearmed on resume, plus the static test page = five; the DB test page was **not watched**. The session would not know if another session edited it, so `read` before editing matters. |
| Versions | Static and DB test pages were each Version 1. Republish creates Version 2 at the same URL; already observed on booth status board v11 (Sep 12). The Share menu screenshot did not show an “Always share latest version” toggle (perhaps because sharing was not public yet); recheck after enabling public access. ⬜ |

## Additional observations from this session

- Publish output included `sharing owner`; the session can see sharing state `[observed]`. `action: status` and `list` can also check it.
- The session’s artifact-watch limit was **five**. Publishing the DB page triggered “watch limit reached — this session already holds its maximum of 5” (observed 07:31). The session had handled six artifacts that day. This is a constraint for exercise 3’s watch test.

[Korean original](sharing-matrix.md) · [M2 overview](../README_en.md) · [Sharing scopes](../concepts/sharing-scopes_en.md)
