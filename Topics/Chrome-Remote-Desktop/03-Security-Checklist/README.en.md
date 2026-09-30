---
title: "M3 — Security Checklist"
created: 2026-09-23 05:15:04
module: M3
tags:
  - chrome-remote-desktop
  - security
  - readme
---

## M3 — Security Checklist · Close the Doors You Opened

> Understand why remote access stays available and what risks that creates; then check the account, screen, and power state in practice.

**Status**: ✅ Complete (2026-09-23 · DoD 6/6) · **Estimated study time**: 2 hours. Disconnect alone does not lock Windows. Testing confirmed that Windows Lock → Disconnect keeps the computer locked, and the Windows PIN can be entered after reconnecting. Account checks, a monthly recurring reminder, user walkthrough validation, and the module retrospective are complete.

## Learning Sequence

1. [What becomes risky when remote access is enabled](concepts/what-gets-risky.en.md) — Understand the new risks and the two keys
2. [Google Account security checks](guides/google-account-checks.en.md) — Review two-step verification, signed-in devices, recent security activity, and recovery information
3. [Windows power and lock settings](guides/windows-power-and-lock.en.md) — Keep the computer awake while protecting its screen
4. [Caution with remote support codes](guides/remote-support-caution.en.md) — Distinguish one-time support access from access to your own computer
5. [Monthly checklist](examples/monthly-checklist.en.md) — Review status without recording personal information
6. [When sign-in fails or activity looks unfamiliar](troubleshooting/locked-out-or-suspicious.en.md) — Follow a calm sequence when something looks wrong

## Current Status

| Item | Status |
|---|---|
| Chrome Remote Desktop service | ✅ Running · starts automatically |
| Sleep while plugged in | ✅ Never |
| Screen turns off while plugged in | ✅ 10 minutes |
| Sign-in required | ✅ “Every Time” shown · fingerprint sign-in works |
| Lock after remote session | ✅ Disconnect alone leaves the work screen visible. Windows Lock → Disconnect keeps it locked; Windows PIN sign-in after reconnect was verified |
| Four Google Account security items | ✅ Two-step verification enabled · user found no issue in recent activity or device list (including Mac sessions) · recovery email and phone available and verified |
| Monthly review | ✅ Checklist created · default Google Calendar reminder: first day of every month, 10:00–10:20 Seattle time, starting 2026-10-01 |

## Navigation

Previous: [M2 — Installation and First Connection](../02-Install-and-First-Connect/README.en.md)

M4 has not started yet. When away, end the session using the tested **Windows Lock → Disconnect** sequence. Do not assume Disconnect alone locks the laptop.
