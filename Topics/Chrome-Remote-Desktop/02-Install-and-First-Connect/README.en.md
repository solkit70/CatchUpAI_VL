---
title: "M2 — Installation and First Connection"
created: "2026-09-20 20:50:00"
module: M2
tags:
  - chrome-remote-desktop
  - readme
---

# M2 — Installation and First Connection · Host and Remote Device

> **Set up the computer you will leave on, then connect to it from the device you will use while away.**
> This module records an installation and connection tested on 2026-09-20; all screenshots are from that day.

## Read in this order

| Order | Document | What you will do | Time |
|---|---|---|---|
| 1 | [Install on Windows](guides/install-host-windows.en.md) | Install on the home computer, name it, and set a PIN | 10–15 min |
| 2 | [Connect from iPhone](guides/connect-from-iphone.en.md) | **iPhone-specific:** connect in Safari, test mobile data, and end safely | 10 min |
| 3 | [Connect from a phone or tablet](guides/connect-from-phone.en.md) | Shared guide for phones and tablets, including iPad and Android | 15–20 min |
| 4 | [Connect from another computer](guides/connect-from-laptop.en.md) | Use a browser on another computer and learn precautions for shared computers | 5 min |
| Reference | [Cannot connect?](troubleshooting/cannot-connect.en.md) | Troubleshoot by symptom | When stuck |
| Record | [First connection log](examples/first-connect-log.en.md) | Measured device, network, time, and experience | — |

## What I ran into—and what beginners may run into too

1. **The Windows user name (often a real name) may already be filled in as the device name.** If you simply select Next, that name is registered.
2. **The same computer may appear twice** under “Remote devices” and “This device.” They are not two computers.
3. **The app may not appear in the iPad App Store.** The iOS app was discontinued in September 2025; use Safari and add the web app to the Home Screen.
4. **Names and photos from Contacts may appear in the iOS Share menu.** Hide them before using a screenshot in a document or video.
5. The six-digit minimum for the PIN appears **on the setup screen, not in the Help page**.
6. **A Windows permission prompt appeared during an iPhone test.** The screenshot showed `Windows Command Processor` and publisher `Microsoft Windows`. RustDesk was also being installed at that time, so the cause was not confirmed to be CRD input.
7. **The Lock command may not appear in the account menu in recent Windows 11 versions.** Look under the power icon in the Start menu.

## Facts tested (2026-09-20)

| | |
|---|---|
| Host | Windows 11 Home laptop · version 151.0.7922.13 · `chromoting` service starts automatically |
| Connection | iPad (Safari web app)—home Wi-Fi ✅ · **phone hotspot over LTE ✅** · VPN enabled ✅ |
| Input | English ✅ · **Korean ✅** · Ctrl+S save ✅ |
| Experience | Fast on a mostly static screen |

In a follow-up iPhone test on 2026-09-27, I turned off Wi-Fi and connected over mobile data. Korean and English text entry, saving a line in Notepad, locking and unlocking Windows, disconnecting, and reconnecting all worked. The connection time was estimated at about two seconds; no drops were reported. This was not a timed measurement. See the [iPhone guide](guides/connect-from-iphone.en.md) for instructions.

## Untested areas and next checks

- **The Android app method is untested.** No Android device was available, so it was excluded from the required hands-on work. There is no need to borrow or buy an Android device.
- Connecting from another computer’s browser is an optional extension for when a second computer is available.
- In “Practice 3—make it fail on purpose,” an incorrect PIN and a disconnected iPad Wi-Fi connection were tested on 2026-09-23. Results are in [Cannot connect?](troubleshooting/cannot-connect.en.md). The user plans to test sleep and a different account later.

## Screenshots (`images/`)

| File | Contents | Redaction |
|---|---|---|
| `01_remotedesktop_access.png` | First view of the access page | — |
| `02_remotedesktop_addToChrome.png` | Add the extension | — |
| `03_remotedesktop_acceptNinstall.png` | Accept and install | — |
| `04_remotedesktop_name_masked.png` | Enter a device name (default value hidden) | ✅ Real name |
| `05_remotedesktop_pin.png` | Set a PIN (shown as dots) | Not needed |
| `06_remotedesktop_device3.png` | Device list showing Online | — |
| `001_iPad_access.PNG` | iPad device list and Home Screen instructions | — |
| `002_iPad_pin.PNG` | Enter PIN on iPad | Not needed |
| `003_iPad_addToHomeScreen_masked.png` | Share menu | ✅ Contacts |
| `004_iPad_addToHomeScreen2_masked.png` | Add to Home Screen · Open as Web App | ✅ Contacts |
| [iPhone test photo](images/005_iPhone_test_Windows_UAC_Command_Processor.jpg) | Windows UAC prompt on the laptop during an iPhone test; shows `Windows Command Processor` / `Microsoft Windows` | ✅ Location EXIF removed; check screen reflections and surroundings before video use |

> Do not use the originals `04_remotedesktop_name.png`, `06_remotedesktop_device.png`, or `003/004`: they show a real name or contacts.

The original `005` photo was left in Downloads. Its copy in this folder has location EXIF removed. Do not describe the UAC prompt as “a window that always appears when typing from an iPhone.” The prompt may have been caused by the installer because its timestamp coincides with RustDesk installation, but the parent process was not confirmed.

## Next module

→ `03-Security-Checklist/`—Close the doors opened for convenience (two-step verification, sleep settings, locking before disconnecting, and access history)

← [M1 — Concepts and selection](../01-Concepts-and-Choice/README.en.md) · [Roadmap](../vl_roadmap/20260920_RoadMap_Chrome-Remote-Desktop.md) · [M2 work log](../vl_worklog/20260920_M2_Chrome-Remote-Desktop.md)
