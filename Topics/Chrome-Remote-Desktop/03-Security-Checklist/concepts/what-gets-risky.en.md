---
title: "What Becomes Risky When Remote Access Is Enabled"
created: 2026-09-23 05:15:04
module: M3
tags:
  - chrome-remote-desktop
  - security
  - concepts
---

## First, Know This: There Are Two Keys

Access to your own computer through Chrome Remote Desktop uses two keys: your **Google Account** and the **host PIN**. The Google Account is the first door, so protect it with two-step verification instead of relying on a password alone. Avoid easy-to-guess host PINs such as birthdays or phone numbers. Google Account two-step verification and the Chrome Remote Desktop host PIN are separate steps; the host PIN is not a Google sign-in verification method.

> “Using a second step to sign in … makes your Google Account much more secure.”

Source: [Google Account Help — Protect your personal information with 2-Step Verification](https://support.google.com/accounts/answer/10956730?hl=en)

## Risk 1 — If the Account Is Compromised, the First Door Is Open

**Why check this first**: An unfamiliar device signed in to your Google Account could put more than Chrome Remote Desktop at risk. Review two-step verification, signed-in devices, recent security activity, and recovery information together.

A single device may appear as multiple sessions. Do not remove an entry based on its name alone; check the device type, browser, time, and approximate location to decide whether it was yours. Source: [See devices with account access](https://support.google.com/accounts/answer/3067630?hl=en)

Google Account device and security-activity pages help review account security. Their existence does not prove that every individual Chrome Remote Desktop connection is recorded there.

## Risk 2 — Disconnecting May Leave Your Computer Screen Visible

**Why check**: Ending a remote session and locking Windows are different actions. If the laptop remains unlocked after you disconnect, someone nearby could see open documents or apps.

Test it instead of guessing. In a test on 2026-09-23, the Notepad screen remained visible on the laptop immediately after Disconnect from the iPad, and reconnecting worked. See the [M3 WorkLog lock test](../../vl_worklog/20260923_M3_Chrome-Remote-Desktop.md#activity-4--lock-test-immediately-after-ipad-disconnect).

## Risk 3 — Keeping the Host Available Does Not Require Leaving the Screen On

**Why separate these settings**: A sleeping computer may be unavailable remotely, but its display does not need to stay on. When plugged in, use separate settings such as **Never sleep** and **turn off the screen after 10 minutes**.

Verify screen-off and Windows lock separately. When stepping away, use a manual lock method described in [Microsoft’s device security guidance](https://support.microsoft.com/en-us/security/securing-your-device). On this laptop, Windows Lock followed by Disconnect kept it locked; after reconnecting, Windows PIN sign-in was verified in the [test](../../vl_worklog/20260923_M3_Chrome-Remote-Desktop.md#activity-5--lock-windows-from-ipad-end-session-and-reconnect).

On battery, a short sleep timeout helps conserve power. As of 2026-09-23, this laptop turns its screen off after 3 minutes and sleeps after 3 minutes on battery. Connect the power adapter when you need the host to remain available remotely.

## Three Takeaways

- Your Google Account is the first key; the host PIN is the second.
- Ending a session does not shut down or automatically lock the computer.
- Keep the computer awake for remote access without leaving its display on.

Next: [Google Account security checks](../guides/google-account-checks.en.md)
