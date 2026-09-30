---
title: "Connect to Your Home Computer from an iPhone with Chrome Remote Desktop"
created: "2026-09-27 00:00:00"
author:
  - "Codex"
module: M2
status: "Mobile-data connection, input, save, lock, and reconnect tested"
tags:
  - chrome-remote-desktop
  - guides
  - iphone
  - mobile
---

# Connect to Your Home Computer from an iPhone with Chrome Remote Desktop

**Time:** About 10 minutes · **You need:** An iPhone, the same Google Account set up on the home computer, and the Chrome Remote Desktop PIN. This guide is specific to iPhone and includes results from an actual iPhone test.

## Current test status

During a live session on 2026-09-27, Safari was set up on the iPhone and the web app was added to the Home Screen. After the session, Wi-Fi was turned off and the phone connected over mobile data. The user entered and saved a line of Korean text in Notepad, entered English text, checked and unlocked the Windows lock screen, disconnected, and reconnected. The saved text was still there. Connection time was estimated at about two seconds, and no disconnections were reported. This was not a timed measurement.

## First, know this

The Chrome Remote Desktop app may not appear in the iPhone App Store. Google’s current instructions say to open `remotedesktop.google.com/access` in a browser if the app is unavailable. Adding it to the Home Screen from Safari hides the address bar and gives the remote screen more room.

## 1. Open the remote screen in Safari

1. Open **Safari**. Use Safari, not Chrome.
2. Enter `remotedesktop.google.com/access` in the address bar.
3. Sign in using the **same Google Account** that is set up on the home laptop.
4. Find `CatchUpAI_laptop` in the list. It should say **Online** below its name.

If the computer does not appear, do not assume installation failed. First check that you are signed in to the same Google Account. Then check the home laptop’s power, internet connection, and sleep status.

## 2. Connect with your PIN

1. Tap `CatchUpAI_laptop`.
2. Enter the Chrome Remote Desktop PIN and tap the arrow.
3. If **“Remember my PIN on this device”** appears, select it **only if this is your personal iPhone and it has a lock screen**. Do not select it on a shared or unlocked device.

Do not put your PIN in a broadcast, chat, screenshot, or work log. When the screen opens, first check that you see the actual desktop of your home laptop.

## 3. Add it to the Home Screen

1. Tap Safari’s Share button: `□↑`.
2. Scroll down in the menu and tap **Add to Home Screen**.
3. Check the suggested name and tap **Add**.
4. After that, open it from the **Remote Desktop** icon on your Home Screen.

The Share menu may show recent contacts’ names and photos. When capturing the screen for a broadcast or document, hide those details, along with account email addresses, PINs, and device names.

## 4. Run a first test over iPhone LTE

1. Turn **Wi-Fi off** on the iPhone. Only LTE or 5G should remain, to simulate being away from home.
2. Connect again using the **Remote Desktop** icon on the Home Screen.
3. On the home computer, open Notepad, type one line in Korean, and save it.
4. Record how long connection takes, typing delay, and the number of disconnections.

On a small screen, the default trackpad mode can make precise clicks easier. You can also try Windows touch input mode from the session menu. For a first test, stick with one familiar mode and first finish typing and saving a short note.

### A Windows permission prompt appeared during the test

The user reported that Windows displayed **“Do you want allow this app to make changes to your device?”** during the first input. They selected **Yes**, after which both Korean and English typing worked. The [test photo](../images/005_iPhone_test_Windows_UAC_Command_Processor.jpg) shows the requesting program as `Windows Command Processor` and the verified publisher as `Microsoft Windows`. The photo was taken at 2:39 p.m., around the time RustDesk was installed and registered as a service on this laptop, so the prompt may have come from that installation. **Do not describe it as a prompt that appears every time you type through CRD.** The parent process was not verified, so the cause remains an estimate. If the prompt appears again, check the program and publisher, then decide whether it belongs to an action you just started.

## 5. End the session safely

1. In remote Windows, select **Start menu → power icon at lower right → Lock**. In recent Windows 11 versions, Lock may not appear in the user-account menu. If you cannot find it in the power menu, send **Windows key + L** using the remote keyboard. Do **not** choose **Sleep** or **Sign out**. See [Microsoft’s Windows lock instructions](https://support.microsoft.com/en-US/accounts-billing/security/user-account-access-in-windows).
2. Check that the Windows lock screen appears on the iPhone.
3. Then select **Disconnect** from the session menu.
4. If possible, connect again and check whether Windows asks you to sign in.

Testing for this topic showed that **Disconnect alone does not lock Windows**. Lock first to protect the physical screen of the home laptop.

## If something goes wrong

- **The device list is empty:** The most likely cause is that you are signed in to a different Google Account.
- **The computer looks dark or says Offline:** Check power, internet, and sleep status on the home laptop.
- **You do not remember the PIN:** Do not guess repeatedly. Check Chrome Remote Desktop settings on the home computer.

→ [Full phone and tablet guide](connect-from-phone.en.md) · [Troubleshooting](../troubleshooting/cannot-connect.en.md) · [M3 security guide](../../03-Security-Checklist/guides/windows-power-and-lock.en.md)

## Source

- [Google Chrome Help—Use Chrome Remote Desktop on your iPhone or iPad](https://support.google.com/chrome/answer/1649523?hl=en&co=GENIE.Platform%3DiOS)—browser access when the app is unavailable, PIN entry, Home Screen shortcut, input modes, and ending a session
