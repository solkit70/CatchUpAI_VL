---
title: "A Shared Link Shows an Old Version (Sep 7) — Reanalysis"
created: 2026-10-06 00:00:00
tags:
  - claude-artifacts-routines
  - m2
  - troubleshooting
---

## Symptom (Sep 7, Builders Lounge event entry page)

The owner’s browser showed the latest version, but a link sent to someone else showed an older one. The original note guessed that this was a “pin” behavior.

## What the documentation says

> “Each publish becomes a version, and from the Share control in the page header you can choose which version viewers see.”

The documentation screenshot shows an **“Always share latest version”** toggle and a **“Sharing version 2”** selector. A shared link can therefore be pinned to a particular version while the owner sees the latest version.

## Reanalysis and checks

The sidebar pin feature is unrelated. The Sep 7 symptom was likely caused by the shared version being fixed to an older version (toggle off); checking in an incognito window and aligning to v3 was the action taken that day. On Sep 13, the toggle was not visible in this account’s Share menu before public sharing was enabled. Whether that depended on the sharing state or plan was not confirmed.

## Oct 6, 2026 — the menu is gone

User check: during the September work, **a version dropdown appeared each time the page was edited, and the “Always share latest version” toggle was there.** The user found that toggle on their own and turned it on, which resolved the “the other person still sees the old version” confusion. **As of Oct 6, that menu can no longer be found.** Whether the feature was removed, moved or renamed, or its default behavior changed has not been confirmed.

> “Features change like this all the time. That’s exactly why a person needs to check.” — the user, Oct 6, 2026

**Lesson:** menus and default behavior in tools like this change without notice. Read documents, videos, and this guide **together with the date they were checked**, and recheck on the current screen. Of the checks below, only step 3 (incognito verification) is unaffected.

## Checks

1. Check the version number in the Share menu.
2. Enable “Always share latest version” if it is available (not visible in the menu as of Oct 6, 2026 — see above).
3. Verify in an incognito window; the owner’s browser is not evidence of the viewer’s version. **This check works even when the menu changes.**

[한국어 원문](shared-link-shows-old-version.md) · [M2 overview](../README_en.md)
