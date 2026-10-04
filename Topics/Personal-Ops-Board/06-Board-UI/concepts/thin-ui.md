---
title: "M6 Concept — Thin UI and Markdown ownership"
created: 2026-10-03 05:41:00 -07:00
tags:
  - personal-ops-board
  - architecture
---

## Thin UI boundary

The UI reads generated state and task metadata, then asks a local service to perform a narrow operation. It does not become a second task database and does not edit generated `Task Board.md` output. The source remains the individual Markdown file; `views/index.json`, `priority-board.md`, and `warnings.md` can be regenerated from that source.

## Safe write contract

An edit carries the SHA-256 digest observed by the browser. The server compares it with the current file under a write lock and rejects stale edits, so a change made elsewhere is not silently overwritten. The write changes an allowlisted frontmatter field, updates `updated` (and `done_at` when completing), serializes YAML, and appends the original body bytes unchanged. It writes through a temporary file and atomic replacement. If view regeneration fails, the original file is restored.

New task creation and proposal approval validate required schema fields and resolve project/source wiki links against existing vault files. Tier 1 needs `due`; `waiting` requires tier 2 and `waiting_on`; `paused` requires tier 4. A proposal remains only a proposal until the user reviews that individual record and approves it.

## Local-only service

The Python HTTP server binds explicitly to `127.0.0.1`; its routes require the loopback Host, and mutations additionally require the same-origin header and a random per-process token injected into the served page. It exposes no remote listener. This follows the [Python `http.server` documentation](https://docs.python.org/3/library/http.server.html), which notes that the default bind can listen on all interfaces unless a specific address is supplied.

## Limits

This is a single-user local utility, not a multi-user service. It does not add a database, authentication account system, background watcher, or remote access. The review screen is an aid for individual human decisions; it does not auto-approve pending proposals.
