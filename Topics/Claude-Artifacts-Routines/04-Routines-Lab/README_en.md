# M4 — Routines · Official Documentation · Audit of Existing Routine · Second Routine

**Status:** ✅ Complete (2026-09-27): exercise 1 audited WBLP on Sep 21 as incident response; official docs; second, one-time routine succeeded; decision table completed.

M4 followed M3 in the roadmap, but on Sep 21 the only real routine (weekly AWS WBLP check) was found to have **failed silently for three consecutive weeks**, so diagnosis and recovery came first. The cause was the **cloud environment network mode (`Trusted`)**, not the routine. The recovery run sent the first alert email with four U.S. technical postings missed during the outage. It also found that the amazon.jobs API silently ignored two search parameters, and the prompt was corrected.

## Learning sequence

1. [WBLP routine audit](guides/wblp-routine-audit_en.md) — **diagnosis of three weeks of failure, environment change, prompt defect fix, results** (includes four lessons for the video)
2. [When a routine does not run](troubleshooting/routine-did-not-run_en.md) — check in order: `get` → `list_runs` → `get_run_log` → local reproduction → environment network
3. [Routines basics](concepts/routines-basics_en.md) — triggers, environment, connectors, notifications, cost, based on official docs ([clipping](../vl_materials/2026-09-27%20Routines%20공식%20문서%20클리핑.md))
4. [Second routine](guides/second-routine_en.md) — preview tomorrow’s calendar (one-time + connectors only) and its run log
5. [Local AI4PKM cron vs. cloud routine](concepts/local-vs-cloud_en.md) — decision table

## What was confirmed on Sep 21

| Finding | Details |
|---|---|
| Run history can be read inside a session | Load the `schedule` skill, then use `RemoteTrigger list_runs` and `get_run_log`; full logs are available without the claude.ai screen. |
| Environment ≠ routine | Network rules belong to the `Default` environment and can be changed only in the web UI. Path: New → `Default` chip → Cloud → Edit → **Network access**. |
| Meaning of `Trusted` | Allows package repositories (npm, PyPI, etc.) and Anthropic API only. It blocks routines that must read outside websites. |
| WebSearch is an exception | It works because it bypasses the proxy, but it is secondary information—not evidence that the target site was reached. |
| Trap with conditional notifications | If both success and failure mean “no news,” a person cannot distinguish them. Send failures via push; have a person inspect logs monthly. |
| **First scheduled run after recovery (Sep 28)** | ✅ Succeeded in 42 seconds without a person; emailed a new Frederick, MD technical job. The environment change persisted for the scheduled run. |
| Verify immediately with a manual run | Do not wait for next week after changing a setting; run `run` and inspect the log (it succeeded 113 seconds later). |

## Additional findings on Sep 27

| Finding | Details |
|---|---|
| Connectors are independent of the allowlist | Second routine used Calendar and Gmail while `Default` remained Trusted. |
| A one-time routine disables itself | `ended_reason: run_once_fired`; documentation says it also does not count toward the daily run limit. |
| Green ≠ success | Documentation explicitly says to open the run record. The three-week WBLP failure is the example. |
| Local vs. cloud | Use local when the vault is needed. This vault is not in GitHub, so the routine cannot read it. |

## Items left open as of Sep 21

- Official Routines documentation clipping in `vl_materials/` (exercises 1 and 2 were not yet complete at that point).
- Candidate for the second routine: (a) POB Deadline warning, where vault access is key and the routine environment would need a repository source; (b) BL sixth alert; (c) weekly YouTube metrics.
- Decision table comparing local (GDR 04:00 · TIU 04:30) and cloud (WBLP · second routine).

## Links

Previous: [M3 — Artifact runtime capabilities](../03-Artifacts-Capabilities-Lab/README_en.md). Roadmap: [20260913 roadmap](../vl_roadmap/20260913_RoadMap_Claude-Artifacts-Routines.md) · WorkLog: [20260921 M4a](../vl_worklog/20260921_M4a_Claude-Artifacts-Routines.md).

[Korean original](README.md)
