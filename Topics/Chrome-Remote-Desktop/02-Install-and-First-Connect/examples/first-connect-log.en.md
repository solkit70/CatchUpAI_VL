---
title: "First Connection Test Log"
created: "2026-09-20 20:45:00"
module: M2
tags:
  - chrome-remote-desktop
  - examples
  - log
---

# First Connection Test Log — 2026-09-20

> This records **which device and network were used, how long it took, and how it felt**—not just whether it worked. It provides a comparison point for “It worked then; why not now?”

## Home computer (host)

| Item | Value |
|---|---|
| Device | Laptop (Windows 11 Home · i7-1355U · 16 GB), named `CatchUpAI_laptop` |
| Host version | 151.0.7922.13 |
| Installation time | 3:17–3:26 p.m. (about 9 minutes) |
| Account change | Re-registered with a different Google Account at 3:38 p.m. (removed and set up again; new PIN) |
| Home network | Home Wi-Fi |
| Apps open during installation | OBS 32.2.2 · Chrome · vault |

## Connection attempts

| # | Time | Device | Network | Method | Result | Time taken | Experience |
|---|---|---|---|---|---|---|---|
| 1 | 8:05 p.m. | iPad | Home Wi-Fi (VPN on) | Safari → PIN | ✅ | About 2 min | Fast |
| 2 | 8:07 p.m. | iPad | Same | Add to Home Screen → reopen as Web App | ✅ | — | Address bar disappeared, leaving more room |
| 3 | 8:1x p.m. | iPad | **Phone hotspot (LTE)** | Web App → PIN | ✅ | — | **Fast—no noticeable difference from Wi-Fi** |
| 4 | Same | iPad | Same | Type English and **Korean** in Notepad → Ctrl+S | ✅ | — | Korean input worked |

## What was confirmed

- **The connection works on an iPad with VPN enabled.** The VPN did not block remote access.
- **There was no noticeable speed difference on LTE.** This applies to a mostly static screen (documents and menus). Moving video and OBS previews will be tested in M4.
- **Korean text can be entered** using the iPad on-screen keyboard.
- What appears on the home computer during a session, and whether disconnecting locks it, are covered in M3.

## Still to test

In a follow-up test on 2026-09-23, an incorrect PIN produced an error; the correct PIN connected successfully. Turning off iPad Wi-Fi left Safari unable to load the page because it had no internet. Turning Wi-Fi back on restored access immediately. The remote session worked after entering the PIN again. See [Cannot connect?](../troubleshooting/cannot-connect.en.md).

| Item | When |
|---|---|
| Connect from Android using the app | **Untested**—no Android device available (confirmed 2026-09-23) |
| Connect from another computer’s browser | When a second computer is available (overlaps with M4) |
| Experience on a moving screen (video or OBS preview) | M4 |
| Deliberately test sleep and a different account | Planned for a later session. Incorrect PIN and iPad Wi-Fi disconnection were tested on 2026-09-23. |

→ [Connect from a phone](../guides/connect-from-phone.en.md) · [Cannot connect?](../troubleshooting/cannot-connect.en.md) · [M2 overview](../README.en.md)
