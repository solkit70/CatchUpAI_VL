---
title: "Routines Basics — Triggers, Environment, Notifications, and Cost"
created: 2026-10-06 00:00:00
tags:
  - claude-artifacts-routines
  - m4
  - concepts
---

## In one sentence

A routine is a Claude Code session running in the cloud while your PC is off. Its reach is determined by the selected repository, the environment’s network policy, and connected services. Source: the [official documentation clipping](../../vl_materials/2026-09-27%20Routines%20공식%20문서%20클리핑.md), dated 2026-09-27 (research preview).

## How it works

| Area | Behavior | Example from this vault |
|---|---|---|
| Trigger | Recurring or one-time schedule, API, or GitHub event. Recurring schedules have a one-hour minimum interval and may start a few minutes late; the docs suggest a time such as :07. A one-time run turns itself off (`Ran`). | WBLP: Monday 15:00 UTC / 08:00 PDT; started around 15:07. |
| Repository | A fresh GitHub clone is used for each run; changes go to a `claude/` branch. | WBLP has no repo. The local vault is not in GitHub, so the routine cannot read it; public CatchUpAI_VL could be selected. |
| Environment network | `Default` is **Trusted**: allowlisted package repositories and cloud APIs; other hosts return `403 host_not_allowed`. | This caused three weeks of WBLP failures; adding amazon.jobs to the allowlist fixed it. |
| Connectors | Only Claude.ai-connected connectors (Gmail, Google Calendar, Claude Docs). They use Anthropic servers and do not depend on the network allowlist. By default all are included and writes need no further prompt, so retain only what is needed. Local `claude mcp add` servers are unavailable. | WBLP connected only Gmail. |
| Notifications and observation | Each run creates a session record. Green means no infrastructure error, not that the task succeeded; inspect `list_runs` and `get_run_log`. | WBLP had three “normal” runs that actually failed. |
| Cost and limits | Uses subscription capacity like interactive sessions and has a daily account run limit. One-time runs do not count toward the daily limit. | Weekly WBLP use was modest. |

The scheduled prompt is treated as a saved instruction and carried out as written. API-provided `text` is wrapped as untrusted data and must be explicitly processed by the prompt. Actions such as sending email or committing run under the user’s identity.

If something works locally but not in the cloud, check the environment’s network policy first. See [troubleshooting](../troubleshooting/routine-did-not-run_en.md).

[한국어 원문](routines-basics.md) · [M4 overview](../README_en.md)
