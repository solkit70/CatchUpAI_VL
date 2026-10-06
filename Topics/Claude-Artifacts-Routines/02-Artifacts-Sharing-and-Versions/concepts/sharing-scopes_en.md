---
title: "Artifact Sharing Scopes — Page Layer and Data Layer (Docs + Test)"
created: 2026-09-13 08:05:00
tags:
  - claude-artifacts-routines
  - m2
  - concept
---

## There are three scopes; this account has two

| Scope | Who can see it | Plans | This account (Pro/Max) |
|---|---|---|---|
| Only you | Owner | All | ✅ Default observed on publish (`sharing owner`) |
| Organization (everyone at the organization / selected people) | Signed-in organization members; designated editors; **comments** | Team · Enterprise | ❌ Not in menu (observed) |
| Public link (anyone with the link) | Anyone who knows the link; no sign-in required | Only option on Pro/Max; Team/Enterprise owner must enable it | ✅ |

> “On Pro and Max plans, a public link is the only way to share an artifact.” — [official documentation](https://code.claude.com/docs/en/artifacts) `[documentation]`

## The page layer and data layer behave differently

With a public link enabled, **anyone can see the HTML**, but **only signed-in users can see data provided by runtime capabilities** (observed Sep 13 and in the platform dialog).

```text
Public link ON
├── Page (HTML and inline data) → visible anonymously; banner: “Content is user-generated and unverified”
└── db data                    → anonymous: use("db") = null; toast: “Sign in to see this artifact's data”
                                  signed-in user: can read it (dialog wording; directly tested in M3)
```

Some capabilities prevent public sharing altogether:

| Capability | Public-link behavior | Evidence |
|---|---|---|
| None / `artifact` (republish) | Allowed | Tested |
| `db` | **Page is public; data requires sign-in** | Test + dialog |
| `assets` | Not allowed — “organization-internal (never public)” | Session skill 0.2.46 `[documentation]` |
| `mcp` | Not allowed — “can't be shared to a public link on any plan” | Official documentation `[documentation]` |
| `room`, `sample`, `downloads` | Not verified (`room` assumes “same-org viewers”) | ⬜ |

## What this account’s plan does not allow

Comments, editor assignment, and organization sharing are Team/Enterprise features `[documentation]`. The initial conclusion was therefore that the “send a comment to AI and get a reply” feature could not be demonstrated on this account. **M3 corrected that conclusion:** the author did post comments and the session replied to “Send to Claude.” Whether someone outside the organization or an anonymous public-link visitor can comment remains unknown. See [the M3 lab log](../../03-Artifacts-Capabilities-Lab/guides/lab-log_en.md) and [the M5 anti-pattern](../../05-Usage-Patterns/guides/anti-patterns_en.md).

## Before sending someone a link

1. If the Share menu says “Only you,” the artifact is still private.
2. When enabling public sharing, read the dialog; it explains the data-layer conditions.
3. Open it in an **incognito window**. The owner’s browser always shows the owner’s latest/full view.
4. If it uses `db`, check whether the page’s data is blank in incognito. If so, rebuild it as a static page for anonymous viewers.

[Korean original](sharing-scopes.md) · [M2 overview](../README_en.md) · [2×2 experiment](../guides/sharing-matrix_en.md)
