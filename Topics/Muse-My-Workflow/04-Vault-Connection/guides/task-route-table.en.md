---
title: "Draft Task-Type Routes for Muse and the Vault"
author:
  - Codex
created: 2026-11-08 15:38:59
tags:
  - muse-my-workflow
  - task-routing
  - draft
  - lang-en
---

## Status and Scope

[한국어](task-route-table.md)

**Draft — operating routes and mirror policy are not approved or finalized.** This table separates paths supported by M2–M4 evidence from untested paths. It does not activate a new connection, whole-vault copy, automation, file move, or deletion. Dropbox/Drive synthetic tests were limited to the designated synthetic files. E · Claude Code Remote Control is an **alternative outside Muse**, not a Muse feature.

## Routes by Task

| Task | Route with current evidence | Limits and status |
|---|---|---|
| Preserve a voice memo verbatim | Use Muse voice input, then download the individual result or email it to yourself; manually add it to `_Inbox_/` at home | Automatic reflection in Journal is untested. Review the verbatim text before filing |
| Check email and calendar | Use Muse's existing connection for that service | Do not copy to the vault automatically. Follow app confirmation steps for sending or changing events |
| Continue a Topic started away from home | Manually hand off the M2/M3 package and continue in the local vault | This is not whole-vault sync. E, remote control, is an alternative outside Muse and requires the home PC and local Claude Code session |
| Search or edit actual vault material with AI | Use a local tool on the home PC under the vault's rules | Whole-vault Muse access is not approved or configured. Current Dropbox/Drive synthetic tests did not use actual vault content |
| Retrieve a Muse result at the home PC | Download the individual file or email it to yourself; Dropbox desktop sync was observed for synthetic test files while the PC was awake | Dropbox sleep effect, mobile path, and sync of actual work material are unverified. Drive auto-sync is unverified |
| Automate a vault mirror | No operating route is configured. A review-only preview is available | Source root, include/exclude paths, data levels, destination, and schedule are undecided. Do not send internal material outside the vault. `--apply` was not run |

## Stop and Roll Back

No scheduled copy or automatic mirror is configured. If a future approved copy has a problem, stop new runs and review the output and destination against the original vault. Do not delete or overwrite source files as a rollback method. Reruns or scope changes require a new preview and approval.

This table does not authorize cleanup of existing external copies or disconnecting Dropbox/Drive. First present the exact targets and impact, then obtain user confirmation. No deletion, disconnection, or copy was performed while writing this draft.

## Recommendation — Draft Pending Approval

The temporary combination best supported by current evidence is **no automatic vault mirror**. When using Muse away from home, manually hand off only the needed result file; use a local tool for work that requires actual vault rules. Remote work while the home PC is running can use E · Claude Code Remote Control, an alternative outside Muse.

Dropbox and Drive worked with synthetic files, but testing did not establish that connector access is restricted to a single folder. Do not treat those successful calls as approval to connect the real vault. This temporary combination also does not mean an operating route has been activated.

## Decisions Pending

- Whether to approve the temporary combination (no automatic mirror), plus allowed data levels and explicit include paths from the real vault
- Storage destination, access scope, retention period, and whether to schedule automation
- Need and scope for mobile, sleep, and folder-boundary tests
- Preview and rollback steps before any approved run

## Related Material

- [Scenario comparison](seamless-scenarios.en.md#scenario-comparison)
- [Mirror policy draft](mirror-policy.en.md#approval-pending)
- [M4 WorkLog](../../vl_worklog/20261108_M4_Muse-My-Workflow.md#next-session-handoff)
