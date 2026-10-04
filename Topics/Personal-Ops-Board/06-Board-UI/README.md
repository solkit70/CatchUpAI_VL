---
title: "M6 — Board UI"
created: 2026-10-03 05:41:00 -07:00
tags:
  - personal-ops-board
  - vibelearn-ai
---

## M6 — Board UI

M6 adds a local visual interface over the existing Markdown task ledger. The browser is a view and controlled editor; `AI/Tasks/items/` remains the task source of truth, and the generated index and boards remain rebuildable outputs. The implementation uses one HTML file and Python's standard-library HTTP server bound to `127.0.0.1`.

## Current capabilities

- View active tasks in four tier lanes, completion history, due warnings, indexer diagnostics, and pending proposals.
- Change only `status`, `priority`, and `tier` on an existing task. The service checks the file hash, validates lane requirements, rewrites frontmatter atomically, preserves body bytes, then regenerates the views.
- Review and approve one inbox proposal at a time. Approval creates one task and marks only that proposal approved.
- Create a task with its classification and existing project/source links, then regenerate the board immediately.
- Reject requests with an unexpected Host or mutation Origin/session token. Request paths are omitted from server logs because task filenames may be private.

## Run and test

Follow [the local server guide](guides/run-server.md). To rehearse all user features safely with disposable synthetic data, use the [live demo and manual regression test cases](guides/live-demo-regression-test-cases.md). For the data boundary, see [the thin UI concept](concepts/thin-ui.md); for common launch and display issues, see [troubleshooting](troubleshooting/README.md).

## Validation

The private service regression suite lives at `AI/Tasks/scripts/test_pob_app.py`. It uses temporary synthetic fixtures and runs with the existing POB suite:

```powershell
python -m unittest discover -s AI\Tasks\scripts -p "test_pob_*.py" -v
```

Current implementation verification is recorded in the [M6 WorkLog](../vl_worklog/20261003_M6_Personal-Ops-Board.md). Live visual inspection uses the private board's current task data locally; examples and this module documentation contain synthetic data only.
