---
title: "Connect from a Browser on Another Computer"
created: "2026-09-20 20:40:00"
module: M2
status: "Pending test on a second computer"
tags:
  - chrome-remote-desktop
  - guides
  - browser
---

# Connect from a Browser on Another Computer

**Time:** 5 minutes · **You need:** Another computer (such as a laptop or office PC), Chrome or Firefox, the same Google Account, and your PIN

> Unlike phones and tablets, **there is nothing to install**. A browser is enough.
> You can connect from an office computer, library computer, or someone else’s laptop—but **take extra care** (see below).

## Steps

1. Open **Chrome** (or Firefox) on that computer.
2. Go to `remotedesktop.google.com/access`.
3. Sign in to the **same Google Account** that is set up on the home computer.
4. Select **Remote Access**, click your computer in the list, and enter your **PIN**.
5. The home computer appears inside the browser tab.

## How this differs from a phone

| | Phone or tablet | Computer browser |
|---|---|---|
| Mouse | Simulated with your finger | Use a **regular mouse** |
| Keyboard | On-screen keyboard or Bluetooth | Use a **regular keyboard** |
| Screen | Small; zooming and panning may be needed | The full-screen button makes it **nearly match the home screen** |
| Shortcuts | Some available | Send special keys such as **Ctrl+Alt+Del** from the side panel |
| Files | Not available | **Upload and download files** from the side panel |
| Clipboard | Limited | Copy and paste can sync in both directions (toggle in the side panel) |

> Select the **small arrow (‹)** at the right edge to open the side panel. Full screen, special keys, file transfer, and screen-size controls are there.

## ⚠️ If you use someone else’s computer

The browser can keep your sign-in active. If you use an office or public computer:

1. **Disconnect** the remote session.
2. **Never** select “Remember my PIN.”
3. **Sign out** of your Google Account (account icon → Sign out).
4. If possible, start in a **private/incognito window**. Closing that window ends its session.

> This connects to the M3 checks for device lists and sign-in history. After using someone else’s computer, check **Google Account → Security → Your devices** and remove it if it remains listed.

## Test record

| Item | Value |
|---|---|
| Computer tested | ⬜ Not yet—this home computer is a laptop, so a second computer is needed |
| Browser | ⬜ |
| Connection | ⬜ |
| Full screen | ⬜ |
| Clipboard sync | ⬜ |
| Test in private window | ⬜ |

> 📌 **Why has this not been tested yet?** The computer registered as the “home computer” is a laptop named `CatchUpAI_laptop`. I confirmed that it appears in another browser on the same computer, but that is not a true remote connection. I will fill this in when I can use a second computer at an office or gathering; this overlaps with M4 (working away from home).

## Next

→ [Cannot connect?](../troubleshooting/cannot-connect.en.md) · [M2 overview](../README.en.md)

## Source

- [Chrome Remote Desktop Help](https://support.google.com/chrome/answer/1649523?hl=en)—browser connection steps
