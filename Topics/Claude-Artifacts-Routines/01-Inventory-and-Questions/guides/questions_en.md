---
title: "Nine Questions This Topic Needs to Answer — Module, Evidence Type, and Priority"
created: 2026-09-13 06:35:00
tags:
  - claude-artifacts-routines
  - m1
  - questions
---

## Rule

Questions came **only from things that actually happened**: what the case index said was learned or missing, gaps in the inventory, and categorical claims made on explanatory pages A5/A6. Each question is assigned a module and an evidence requirement (`documentation` = quote official documentation; `experiment` = reproduce it in this vault). Once answered, add a one-line answer and link in the Answer column.

## Questions

| # | Question | Why (observed experience) | Owner | Evidence | Answer |
|---|---|---|---|---|---|
| **1** | **Why can’t an artifact with `db` (Booth Manager) be shared with someone else by link? Can a setting fix it, or is it structural?** | BigHug Sep 3—the exact question in the original request | M2 | Documentation → if absent, 2×2 experiment | ✅ **The page can be public; DB data is visible only to signed-in users.** Anonymous visitor sees an empty shell → structural. [Sharing matrix](../../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix_en.md) |
| 2 | Exactly how many sharing scopes are there—only you / link / organization / sign-in required—and what are the conditions for each? | A6 listed only two | M2 | Documentation | ✅ Three: private, organization (Team/Enterprise), public link. This account has no organization option. |
| 3 | What caused “shared link shows an old version” (Sep 7)—pinned shared version, cache, or owner view? | Happened with A4 | M2 exercise 3 | Experiment | See [reanalysis](../../02-Artifacts-Sharing-and-Versions/troubleshooting/shared-link-shows-old-version_en.md). |
| 4 | What is the right procedure when publishing is rejected because another session edited the artifact (Sep 12 Booth Status Board)? When is `force` safe? | Sep 12 session | M2 | Tool documentation + experiment | — |
| 5 | What do comment → AI reply → resolve look like in practice? What does the viewer need (for example, sign-in)? | A6 claim, not tested at inventory time | M2 exercise 3 | Experiment | Initially recorded as ⛔ comments unavailable on this Pro/Max account—organization sharing only. **Corrected in M3:** author-side comment and Send to Claude reply worked; public/outside-user behavior remains untested. |
| 6 | Can the session read a DB value changed on screen, then write a value the page reads? Does `if_version` block concurrent edits? | Booth Manager used this structure, but round trip had never been verified | M3 | Experiment | ✅ Stale session write was rejected with `version_mismatch`; reread version succeeded. See [DB round trip](../../03-Artifacts-Capabilities-Lab/guides/db-roundtrip_en.md). |
| 7 | Should images such as booth-layout captures have used `assets` instead of data URIs? What are the actual 16 MB and CDN allowlist constraints? | Image handling while editing board on Sep 12 | M3 | Documentation + experiment | See [runtime gotchas](../../03-Artifacts-Capabilities-Lab/troubleshooting/cdn-and-storage-gotchas_en.md). |
| 8 | Can a Routine really not read local vault files? If so, can Personal Ops Board Deadline warnings run only with local AI4PKM cron? | A5 says “cannot access my computer”; directly affects POB design | M4 | Documentation + experiment (second routine) | Cloud routine clones the chosen GitHub repo, not the local vault. See [local vs. cloud](../../04-Routines-Lab/concepts/local-vs-cloud_en.md). |
| 9 | Did the WBLP routine actually run on Sep 8? Did “email only when conditions match” work? Where can run history be viewed? | Run history had not been checked | M4 exercise 1 | Direct observation | Three consecutive `EGRESS_BLOCKED` failures were found. See [WBLP audit](../../04-Routines-Lab/guides/wblp-routine-audit_en.md). |

## Priority

1 → 8 → 6 → 2 → 9 → 3 → 4 → 5 → 7. **Question 1 was explicitly requested in the original case**; **question 8 could change another topic’s design (Personal Ops Board, Sep 27)**. They became the first M2 and M4 exercises.

## What was excluded

- Open-ended questions such as “What can you make with Artifacts?” were not based on an experience. M5 patterns answer them naturally from observed results.
- Cost had not come up as a problem. Add it if it appears in the M4 documentation clipping.

[Korean original](questions.md) · [M1 overview](../README_en.md)
