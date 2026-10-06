---
title: "M3 Exercise 1 — Record of Minimal Examples for Five Runtime Capabilities"
created: 2026-09-27 15:30:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m3
  - lab-log
---

## What we did

Published one minimal example for each of five runtime capabilities. Publishing was done with the `Artifact` tool in the VS Code Claude Code extension (no browser automation). Capability rules followed the types in the `artifact-capabilities` skill, runtime contract **0.2.60**. The user opened each published URL to check the screen.

## Publish results

| # | Example | Declared capability | URL | What the publish result showed |
|---|---|---|---|---|
| ① | [01-counter-db.html](../examples/01-counter-db.html) | `{db: {}}` | https://claude.ai/artifact/8p4xaEhHXB6PQyzDZfy3os | Contract 0.2.60 · readable by only you |
| ② | [02-hello-user.html](../examples/02-hello-user.html) | `{user: {scopes: ["profile"]}}` | https://claude.ai/artifact/2ofKVvCX9eW1dyoXYcPpdD | Same |
| ③ | [03-image-assets.html](../examples/03-image-assets.html) | `{assets: {}}` | https://claude.ai/artifact/EXRfAfWCLDNE89HG5jqc6s | Same · session uploaded one image → `/_blob/8bba69ce…` |
| ④ | [04-comments.html](../examples/04-comments.html) | `{comments: {composer_only: true}}` | https://claude.ai/artifact/AaVvLju4haYcDktsR9StFA | Same |
| ⑤ | [05-multi-file/](../examples/05-multi-file/index.html) (`index.html` + `app.css` + `data.json`) | None; published together through `files` parameter | https://claude.ai/artifact/J5KcHHynLoAd3MRkorftTR | No capability line—the page declares no runtime capability. |

## User screen checks

| # | What to check | My window (owner) | Other account/incognito |
|---|---|---|---|
| ① | Is **11** visible (value session wrote)? Does +1 make it 12? | ✅ At 22:28, clicked +1 twice → 13 (v4, `by: page`) → session read it. See [DB round trip](db-roundtrip_en.md). | ⏳ |
| ② | “Hello, [name]”; owner yes; edit yes | ✅ As expected (confirmed by user) | Skipped |
| ③ | Is one QR image and upload control visible? | ✅ As expected; QR uploaded by session appeared in page list. | Skipped |
| ④ | Does clicking open a comment composer for the paragraph? | ✅ At 22:24, two comments on paragraph 1 (`#c1`) attached to that paragraph. “Send to Claude” triggered an **automatic reply** from this session (auto-reply); after checking, both threads were resolved from the session. At 22:25, a comment on paragraph 2 attached not to the paragraph (`#c2`) but to its **button** (`#c2 > button`). It appears that a page button opens a composer on the passed element (the paragraph), while opening comment mode and clicking directly attaches to that element (the button). At 22:26, paragraph 3 (`#c3 > button`) also worked—all three paragraphs had comments. ⚠️ Reply language was **inconsistent**: threads 1 and 2 received Korean replies; thread 3 received English, possibly because its comment was the single English word “test.” | ⏳ |
| ⑤ | “Multiple files published successfully” · `data.json` read “yes” | ✅ As expected | Skipped |

Checks from another account were skipped at the user’s request (“Let’s do a simple test and move on”). Sharing-scope differences were recorded only from publish output and documented rules.

> All examples are currently private (“Only you”). They are expected **not to open** in a logged-out incognito window. To show them to others, the author needs to share them from the Share menu. Artifacts declaring `db`, `user`, or `assets` can only be shared within an organization (no public link). `composer_only` comments and example ⑤ with no capability can be public; check this distinction in the Share menu.

## Discovery — artifact watch limit is 10 per session

After five examples were published in a row, this session **automatically stopped watching** two existing artifacts (Booth Manager and Booth Status Board). The notification said: *“this session reached its limit of 10 artifact watches and made room to watch a newer one; it was auto-replying to comments, and that stops until its next publish.”* Publishing adds an artifact to the watch list, which has a limit of 10 per session. If a production artifact has comment auto-replies enabled, publishing many lab examples can push it out of the watch list. See [runtime troubleshooting](../troubleshooting/cdn-and-storage-gotchas_en.md).

[Korean original](lab-log.md) · [M3 overview](../README_en.md)
