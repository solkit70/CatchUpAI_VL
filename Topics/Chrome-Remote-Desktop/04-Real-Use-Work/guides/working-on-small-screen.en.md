---
title: "Working on a Small Screen with Chrome Remote Desktop on iPhone"
created: 2026-09-23 14:18:07
module: M4
tags:
  - chrome-remote-desktop
  - iphone
  - remote-work
---

## Before You Start

**Why check first**: To find the laptop away from home, it must be powered on and connected to the internet. Plug it into power and confirm it appears online in Chrome Remote Desktop. Lid behavior has not been tested, so do not assume closing it will keep the computer available; it may sleep.

On iPhone, you can use Safari without installing an app. Google’s [official iPhone and iPad instructions](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DiOS&hl=en-AO) include opening `remotedesktop.google.com/access` in a browser. This practice applies the web access method already used on iPad to iPhone.

## First Connection on iPhone

**Why check the account**: The laptop is registered to a particular Google Account. If you sign in with a different account, it may not appear in the list.

1. Open Safari on your iPhone and go to [remotedesktop.google.com/access](https://remotedesktop.google.com/access). If prompted, sign in with the **same Google Account** used on the iPad. Complete two-step verification yourself if requested; never send a verification code in a document or chat.
2. Under **Remote access**, select your home laptop. If it is missing, first check that you are using the same Google Account. If it appears dimmed, check that the laptop is online.
3. Enter the **Chrome Remote Desktop host PIN**. This is a different step from Google Account two-step verification and your Windows sign-in PIN.
4. If the Windows lock screen appears, unlock it with your **Windows PIN**. Do not include the PIN digits in screenshots or a WorkLog.

Google’s [remote access steps](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DiOS&hl=en-AO) say to select a computer and enter its host PIN; after connection, use the virtual trackpad to control the computer.

## Operate and Verify on the Small Screen

**Why start with a small test**: Text and buttons on the home monitor can be tiny on an iPhone, making it easy to tap the wrong item. Test typing and saving in a document with no personal information first.

1. In the default trackpad mode, swipe to move the pointer and tap once to click. Tap with two fingers for a right-click; pinch to zoom. If needed, open the session menu with the arrow at the screen edge and change the touch method under **Input controls**. Source: [Google iPhone and iPad controls](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DiOS&hl=en-AO)
2. Type a short Korean line in Notepad or a test document with no personal information, then save it. Reopen the document and confirm that the text remains.
3. Record connection time, Korean input lag, number of drops, and any difficulty reading or tapping. To compare with iPad, use the **same one-line type-and-save task**.

In Safari, choose **Add to Home Screen** from the Share menu to open the site like a web app without the address bar. This is not required for the first connection. Google also describes adding the site to the home screen after connecting in a mobile browser. Source: [Google iPhone and iPad help](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DiOS&hl=en-AO)

## When You Finish

**Why lock first**: On this laptop, Disconnect alone leaves the Windows work screen visible. In remote Windows, select **Start menu → Power icon at lower right → Lock**, then follow **confirm lock screen → Disconnect**. In current Windows 11 versions, Lock may not appear in the user account menu. If it is not in the power menu either, send **Windows key + L** from the remote keyboard. Do not select Sleep; that may prevent you from reconnecting. When you reconnect, confirm that Windows shows the lock screen and asks for the PIN. If you unlocked it to verify, lock it again before ending the practice. Source: [Microsoft Windows lock guidance](https://support.microsoft.com/en-US/accounts-billing/security/user-account-access-in-windows)

Google says a mobile remote session can be ended by closing the app or tab, or choosing Disconnect from the menu. That does not mean Windows itself has been locked. Sources: [Google ending a remote session](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DiOS&hl=en-AO) · [M3 hands-on test](../../03-Security-Checklist/guides/windows-power-and-lock.en.md#4-tested--lock-first-then-disconnect-from-the-ipad)

→ [Device and network test matrix](../examples/device-network-matrix.en.md) · [M4 WorkLog](../../vl_worklog/20260923_M4_Chrome-Remote-Desktop.md)
