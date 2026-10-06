---
title: "M4 Exercise 2 — Second Routine: Preview Tomorrow’s Calendar (One Time)"
created: 2026-09-27 15:40:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m4
  - routine
---

## Why this routine

The first routine (WBLP) used **recurrence + external website checking**. To avoid repeating those conditions, the second test used **one-time + connectors only**. This tested each side of two decision axes once: network allowlist vs. connector, and recurring vs. one-time. It did not need the vault, so cloud was appropriate; see the [decision table](../concepts/local-vs-cloud_en.md). User approval: “Yes, I approve. Please proceed.” (2026-09-27).

## Configuration

| Item | Value |
|---|---|
| Routine | Preview tomorrow’s calendar (one time) · `trig_01TyCwrfL1H3vsmdkmcDS8xk` · https://claude.ai/code/routines/trig_01TyCwrfL1H3vsmdkmcDS8xk |
| Created with | VS Code Claude Code extension session · `schedule` skill → `RemoteTrigger create` |
| Trigger | `run_once_at: 2026-09-27T23:07:00Z` (16:07 PDT); chose :07 instead of the hour per official-doc recommendation |
| Repository | None |
| Environment | `Default` (Trusted), unchanged. The test checked the documentation claim that connectors do not depend on the allowlist. |
| Connectors | Google Calendar (read) · Gmail (send). Claude Docs was removed because documentation said all connectors are included by default and can write without asking; retain only what is needed. |
| Tools | Read · Write (no Bash or WebFetch) |
| Model | `claude-sonnet-5` |
| Prompt essentials | Read the Sep 28 (Monday) schedule and email one line per event in Korean; do not copy descriptions, attendee email addresses, or meeting links. If the calendar cannot be read, email the **failure too**, preventing the “silent failure” found in WBLP. |

## Run result — ✅ success (session `cse_017Jz54UXyMTvroETg979pEP`)

| Time (UTC) | Log |
|---|---|
| 23:07:00 | Scheduled time |
| **23:08:11** | Actual start, 1 minute 11 seconds late (even though scheduled at :07) |
| 23:08:13 | Sandbox: “No sources configured,” “No setup script configured”—routine ran without a repository |
| 23:08:20 | Loaded connector tools with `ToolSearch` (`mcp__Google-Calendar__*` · `mcp__Gmail__*`) |
| 23:08:23–32 | `list_calendars` → four calendars; `list_events` on each for Sep 28, 00:00–23:59 PDT → zero events |
| 23:08:37 | `send_message` → emailed: “There are no events on the calendar for Mon 9/28.” |
| 23:08:42 | `result: success` · 9 turns · **25 seconds** |
| Confirmation | User: “The tomorrow calendar preview email arrived.” Receipt verified in inbox. |

After the run, `get` returned `enabled: false` and `ended_reason: "run_once_fired"`; the one-time routine turned itself off (`Ran` in web UI). A date one day later still appeared under `next_run_at`, but because `enabled: false` it would not run; this was treated as display residue.

## What we learned

- **Connectors worked while `Default` stayed Trusted.** Unlike WBLP, no network allowlist change was needed (directly confirmed the docs’ “Connectors … don’t need allowlist changes” claim).
- The routine did not need calendar names in the prompt: it called `list_calendars` first and read each. Saying “all calendars” was sufficient.
- By requiring an email even when the result was zero, **successful execution was immediately visible in the inbox**. This is the opposite design from WBLP’s “email only when conditions match”; choose based on the purpose of the notification.
- Even when scheduled at :07, it started about a minute late; it is not suitable for work needing minute-level precision.

[Korean original](second-routine.md) · [M4 overview](../README_en.md) · [Local/cloud decision](../concepts/local-vs-cloud_en.md)
