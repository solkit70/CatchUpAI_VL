---
title: "When a Routine Does Not Run — Troubleshooting Sequence"
created: 2026-10-06 00:00:00
tags:
  - claude-artifacts-routines
  - m4
  - troubleshooting
---

## First distinguish three symptoms

| Symptom | Meaning | Where to check |
|---|---|---|
| No run exists | Trigger did not fire: routine disabled, schedule issue, or missing environment | Routine configuration via `get`: `enabled`, `next_run_at`, `environment_id` |
| Run exists but failed | Session started and failed inside | `list_runs` → `get_run_log` |
| Run succeeded but no result | Conditional notification stayed quiet, or a filter was ignored and returned no results | Final log summary and the actual search parameters in the response |

With the `schedule` skill, `RemoteTrigger` can inspect all three from a session without opening claude.ai.

## Check in this order

1. `get`: confirm `enabled: true`, a future `next_run_at`, and inspect `last_run.status`.
2. `list_runs`: find recent executions. No run means a pre-trigger issue (paused, environment, or repository access); there is no log to inspect.
3. `get_run_log`: inspect `tool_result ERROR`, `connect_rejected`, `EGRESS_BLOCKED`, organization policy messages, `InputValidationError`, and the final `result:` summary.
4. Reproduce the same request locally. If `curl` to the failed URL returns 200 locally, suspect the cloud environment rather than the remote server.
5. Check environment network mode in claude.ai/code → New → `Default` chip → Cloud → edit environment → **Network access**. `Trusted` allows package repositories and Anthropic APIs; add the needed domain or use Full for external-site routines.
6. After fixing, run manually and inspect the log instead of waiting a week.

## Common confusions

- WebSearch can work while WebFetch and `curl` fail because it uses a separate search API; its results are secondary evidence, not proof the routine reached the target site.
- Cloud environment settings are under the New session environment chip, not Settings → Claude Code (which manages CLI/desktop connections).
- `RemoteTrigger update` can change `environment_id` but cannot change the environment’s network rules; edit those in the web UI.
- “Zero results” does not prove a filter worked. Inspect the actual conditions returned (for example `job_posting_search_request.filterFacets` from amazon.jobs). An empty value can mean the API ignored the parameter.

See the [WBLP audit](../guides/wblp-routine-audit_en.md) for the Sep 7–21 `EGRESS_BLOCKED` failures, network recovery, and ignored search parameters.

[한국어 원문](routine-did-not-run.md) · [M4 overview](../README_en.md)
