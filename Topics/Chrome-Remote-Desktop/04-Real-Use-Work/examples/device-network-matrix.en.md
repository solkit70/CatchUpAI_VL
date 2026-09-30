---
title: "Chrome Remote Desktop Device and Network Test Matrix"
created: 2026-09-23 14:13:42
module: M4
tags:
  - chrome-remote-desktop
  - remote-work
  - comparison
---

## Comparison Criteria

**Why put these results together**: To distinguish how a task performs on an external Wi-Fi network or phone hotspot compared with home Wi-Fi. The [M2 first-connection test](../../02-Install-and-First-Connect/examples/first-connect-log.en.md) remains the baseline. M4 sessions used different dates and task scopes, so they are not a rigorous speed comparison.

| Date and context | Device | Connection | Connection time | Korean input and lag | Drops | Work checked |
|---|---|---|---|---|---|---|
| 9/20 M2 · home | iPad | Home Wi-Fi (+VPN) | About 2 minutes, first connection | Korean input succeeded · fast | Not recorded | Connected and opened web app |
| 9/20 M2 · home | iPad | Phone hotspot (LTE) | Not recorded | Korean input and save succeeded · fast on a static screen | Not recorded | Typed and saved in Notepad |
| 9/23 M4 · Starbucks away from home | iPad | Venue Wi-Fi | Estimated under 10 seconds | No major Korean input lag noticed | 0 | Edited document and verified content; test folder; checked OBS and Task Manager |
| 9/27 M4 · first iPhone test | iPhone | Mobile data (Wi-Fi off) | Estimated about 2 seconds | Korean and English input succeeded · lag not recorded | 0 reported | Typed and saved a Notepad line and verified it remained; Windows lock, unlock, Disconnect, and reconnect succeeded |

## Current Assessment and Next Measurement

The iPad and Starbucks Wi-Fi combination handled about 20 minutes of document editing and status checks without reported inconvenience. On 9/27, mobile data on iPhone also supported input, saving, content persistence, safe exit, and reconnection; connection time was estimated at about 2 seconds, with no reported drops. Neither connection time was measured with a timer, and the sessions differed in whether they were first connections and in task scope. They cannot establish which network is faster. A fair comparison requires repeating the **same task** away from home and timing the connection with a real timer.

The roadmap calls for tests across three devices and two connection types, but no Android device is available and availability of a second computer has not been confirmed. Do not invent results for unavailable combinations; adjust completion criteria after confirming which devices and connections the user has.

→ [External work session log](real-session-log.en.md) · [M4 WorkLog](../../vl_worklog/20260923_M4_Chrome-Remote-Desktop.md)
