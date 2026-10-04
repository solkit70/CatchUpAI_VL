---
title: "M6 Guide — Run the local board UI"
created: 2026-10-03 05:41:00 -07:00
tags:
  - personal-ops-board
  - guide
---

## Start

From the vault root in PowerShell, run:

```powershell
python AI\Tasks\app\serve.py --open-browser
```

The app opens at `http://127.0.0.1:8765/`. It listens only on this computer. Keep the terminal open while using the app; press `Ctrl+C` there to stop it. If that port is already occupied, choose another port:

```powershell
python AI\Tasks\app\serve.py --port 8766 --open-browser
```

## Use the board

The board view shows task lanes, due warnings, completed/closed history, and indexer diagnostics. Change status, priority, or tier on a card, then select **변경 저장**. If the Markdown file changed since the page loaded, refresh and review the latest values before trying again. The server blocks a change that would violate required tier fields.

Use **승인 대기** to inspect a single proposal and approve it only after choosing its status, tier, priority, project link, and body. Use **빠른 입력** for a fully classified task with existing project and source links. The UI regenerates the private index and views after a successful change.

The app's write boundary and ownership model are described in [Thin UI and Markdown ownership](../concepts/thin-ui.md).
