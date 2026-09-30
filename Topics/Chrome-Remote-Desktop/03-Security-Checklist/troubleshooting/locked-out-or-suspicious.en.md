---
title: "When Sign-In Fails or Activity Looks Unfamiliar"
created: 2026-09-23 11:55:27
module: M3
tags:
  - chrome-remote-desktop
  - security
  - troubleshooting
---

## Identify the Symptom First

**Why**: A remote connection failure does not necessarily mean an account was compromised. Check separately whether the host is offline, the CRD PIN is wrong, Windows is locked and waiting for sign-in, or Google shows unfamiliar account activity.

| What you see | Check first | Next step |
|---|---|---|
| CRD computer is offline | Host power, internet, and sleep state | Check it near the laptop. Do not make blind power-setting changes while away |
| CRD PIN is rejected | Correct account and computer name; typing error | Retry with the correct PIN. Never write or share the actual PIN |
| Stuck at Windows lock screen | Which Windows sign-in method is available remotely | Reproduce and test beside the laptop first. Do not assume fingerprint sign-in works remotely |
| Unknown Google device or security event | Session details and your own activity | Follow [Google’s account-protection steps](https://support.google.com/accounts/answer/6294825?hl=en) |

## If You See Unfamiliar Account Activity

**Why act promptly**: Your Google Account is the first key for remote access to your own computer. Google recommends reviewing recent security events and unfamiliar devices, then following its instructions to secure the account. Source: [Google — Help secure a hacked or compromised account](https://support.google.com/accounts/answer/6294825?hl=en)

1. Open [Google Account Security](https://myaccount.google.com/security) and review recent security activity.
2. Review session details under [Your devices](https://google.com/devices). Check whether multiple entries may be sessions from one device; do not treat session count as the number of physical devices or intrusions. Source: [Google — Device-list explanation](https://support.google.com/accounts/answer/3067630?hl=en)
3. If an event was not yours, choose **No, it wasn’t me** or the unfamiliar-device flow on Google’s screen, then follow the steps to secure the account. If you cannot sign in at all, use [Google Account Recovery](https://accounts.google.com/signin/recovery).

## What Was Tested and What Remains

On 2026-09-23, the user reconnected after entering an incorrect CRD PIN and also reconnected after the iPad’s Wi-Fi recovered. Disconnect alone left the laptop’s work screen visible. **Windows Lock → Disconnect** from the iPad kept it locked; after reconnecting, the user entered the **Windows PIN** and returned to the work screen. The actual PIN was not recorded. The original error screens are summarized in the [M2 symptom checklist](../../02-Install-and-First-Connect/troubleshooting/cannot-connect.en.md#2026-09-23-additional-test--pin-and-ipad-internet).
