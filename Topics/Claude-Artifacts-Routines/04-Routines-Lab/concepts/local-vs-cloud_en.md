---
title: "Local AI4PKM Cron vs. Cloud Routines — Decision Guide"
created: 2026-10-06 00:00:00
tags:
  - claude-artifacts-routines
  - m4
  - concepts
---

## The 30-second rule

Use **local** automation if the task must read or write vault files. Use a **cloud routine** when it needs external web, email, or calendar access while the PC may be off. This vault is not in GitHub, so cloud routines cannot read it directly; they clone only the selected GitHub repository. If both are needed, the cloud task can email its result and a local task can move it into the vault.

## Comparison

| Dimension | Local AI4PKM cron (`orchestrator.yaml`) | Cloud routine |
|---|---|---|
| Read/write vault | Direct access | No, except files in selected GitHub repo (including public CatchUpAI_VL) |
| Runs while PC is off | No | Yes |
| External web | Uses PC network | Limited by environment allowlist (`Default` = Trusted) |
| Email/calendar | Depends on local MCP setup | Claude.ai connectors, independent of network allowlist |
| Cost | Local agent run costs | Subscription usage and daily run limit; one-time runs are excluded |
| Failure records | `_Settings_/Logs/` | Session run record via `list_runs` and `get_run_log`; green does not guarantee task success |
| Minimum interval | No fixed limit | One hour |

## Existing jobs

| Job | Where | Why |
|---|---|---|
| GDR Daily Roundup, 04:00 | Local | Reads the day’s vault files and writes Roundup and Task Board updates. |
| TIU Topic Index Update, 04:30 | Local | Edits the vault’s topic index. |
| WBLP weekly AWS job search, Monday 08:00 | Cloud | Needs external-site search and conditional email, not the vault; should run with the PC off. |
| Second routine (lab) | Cloud | See [second routine](../guides/second-routine_en.md). |
| Personal Ops Board Deadline agent | Local | Reads `items/` and writes `views/warnings.md`; POB belongs on a local AI4PKM node. |

All four POB agents (Board, Deadline, Intake, Discovery) read and write the vault, so they should run locally. If a morning deadline alert is required while the PC is off, consider splitting only email delivery into a cloud task, without exposing `warnings.md`; record the design in the POB decisions.

[한국어 원문](local-vs-cloud.md) · [M4 overview](../README_en.md)
