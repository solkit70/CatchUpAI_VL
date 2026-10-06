# M3 — Artifact Runtime Capability Experiments

**Module:** M3 · **Status:** ✅ Complete (2026-09-27) · **Actual time:** about one hour (VS Code Claude Code extension session)

Published one minimal example for each runtime capability an Artifact page can declare—`db`, `user`, `assets`, `comments`, and multiple files—and observed directly what prevents an AI session and a person from overwriting one another’s changes to the same DB document. Baseline: runtime contract **0.2.60**.

## Learning sequence

1. [Capability selection table](concepts/capability-selection-table_en.md) — choose the right feature for the job (read first).
2. [01-counter-db.html](examples/01-counter-db.html) — ① DB counter.
3. [02-hello-user.html](examples/02-hello-user.html) — ② who is viewing (`user`).
4. [03-image-assets.html](examples/03-image-assets.html) — ③ image library (`assets`).
5. [04-comments.html](examples/04-comments.html) — ④ comments on each paragraph (`comments`, `composer_only`).
6. [05-multi-file/index.html](examples/05-multi-file/index.html) — ⑤ publish HTML, CSS, and JSON separately.
7. [Lab log](guides/lab-log_en.md) — five published URLs and screen-check results.
8. [DB round trip](guides/db-roundtrip_en.md) — session ↔ page DB round trip; observed `if_version` rejection (key result).
9. [BigHug Artifact review](guides/bighug-artifacts-review_en.md) — reviewed Booth Manager without modifying it.
10. [Runtime gotchas](troubleshooting/cdn-and-storage-gotchas_en.md) — ten-artifact session watch limit and common pitfalls.

## What we learned in this module

- While a person edits data on screen, `if_version` prevents the AI session from overwriting the person’s change. After the page changed v2 → v4, the session’s v2 write was rejected as `version_mismatch`; it succeeded after rereading v4.
- Page writes use last-write-wins. Do not increment a number in one document with a shared page when several people may update it.
- A session can automatically reply to a “Send to Claude” comment. Where the comment attaches depends on how the composer was opened (page button vs. comment mode).
- One session watches up to 10 Artifacts. Publishing multiple examples can displace watches on production artifacts and stop their automatic comment replies.

Previous: [M2 — Sharing and Versions](../02-Artifacts-Sharing-and-Versions/README_en.md) · Next: [M4 — Routines](../04-Routines-Lab/README_en.md)

[Korean original](README.md)
