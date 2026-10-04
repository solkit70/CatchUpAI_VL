---
title: "M6 Troubleshooting — Board UI"
created: 2026-10-03 05:41:00 -07:00
tags:
  - personal-ops-board
  - troubleshooting
---

## The page does not open

Confirm the server process is still running in the terminal and use the exact loopback URL it printed. If the default port is busy, restart with another port such as `--port 8766`, then open that port's URL.

## Save is rejected

Read the message and refresh the page. A stale-file message means the Markdown source changed after the board was loaded; the app intentionally refuses to overwrite it. A tier validation message means the requested status/tier needs a due date or waiting target that the limited card editor does not change. Edit the full Markdown item or use a compatible status/tier combination.

## A proposal is missing

The inbox shows only well-formed `proposal-*.md` records with `type: proposal` and `status: pending_review`. Malformed or already processed proposals are not shown as pending. Check the source file and indexer diagnostics before changing its frontmatter.

## Views did not update

The app regenerates index, board, and warning views after a source write. If that step fails, the service restores the original task file and reports a save error. Check that the existing Python environment can run the POB scripts and that the relevant vault folders are writable; then refresh the UI.
