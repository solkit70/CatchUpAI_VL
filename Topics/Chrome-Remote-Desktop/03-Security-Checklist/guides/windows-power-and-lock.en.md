---
title: "Check Windows Power and Lock Settings"
created: 2026-09-23 05:15:04
module: M3
tags:
  - chrome-remote-desktop
  - security
  - windows
  - guide
---

## Target Settings

**Why keep these separate**: A computer waiting for a remote connection needs to stay awake, but leaving its display on can expose information to people nearby and use more electricity.

| Setting | Target while plugged in | Why |
|---|---|---|
| Turn off screen | 10 minutes | Reduce physical screen exposure when not in use |
| Sleep | Never | Keep the host awake while you are away |
| Require sign-in again | Check and configure | Require authentication after Windows locks or wakes. Turning off the display alone does not guarantee a lock |

## Values Checked on 2026-09-23

| Item | Plugged in | On battery |
|---|---:|---:|
| Screen turns off | **10 minutes ✅** | 3 minutes |
| Sleep | Never ✅ | 3 minutes |
| Chrome Remote Desktop service | Running · starts automatically | Same |

The original screen-off value while plugged in was **Never**; the user provided a screenshot after changing it to **10 minutes**. Sleep remained **Never**. On battery, the laptop sleeps after 3 minutes, so connect the power adapter when you need remote access to remain available. The sign-in requirement displayed **Every Time**, and the control was disabled because Windows Hello was in use. **Disconnect alone leaves the work screen visible, but explicitly locking Windows remotely before disconnecting kept it locked.**

## 1. Screen-Off and Sleep Settings

1. In Windows, open **Settings → System → Power & battery**.
2. Expand **Screen, sleep, & hibernate timeouts**.
3. Set **Turn my screen off when plugged in** to **10 minutes**.
4. Leave **Make my device sleep when plugged in** set to **Never**.

Microsoft’s Windows 11 guide describes changing screen and sleep timeouts separately on this page. Source: [Windows 11 power settings](https://support.microsoft.com/windows/experience/power-battery/power-settings-in-windows-11)

## 2. Require Sign-In Again

1. Open Windows **Settings → Accounts → Sign-in options**.
2. Under **Additional settings**, find **If you’ve been away, when should Windows require you to sign in again?** and check the current selection. If the wording or choices differ on your Windows version, use the screen in front of you as the reference.
3. Never include your actual Windows PIN or password in a WorkLog or screenshot.

The screen-off timer is not a Windows lock timer. Even after checking this setting, verify separately whether disconnecting from the iPad locks the laptop, using the test below.

Microsoft recommends requiring sign-in when waking from sleep. Source: [Microsoft — Secure your device](https://support.microsoft.com/security/securing-your-device)

## 3. Test Whether Windows Locks After a Remote Session

**Why test directly**: Do not assume that ending a session automatically locks Windows.

1. On the laptop, open Notepad with no personal information in it.
2. Connect from the iPad using Chrome Remote Desktop.
3. In the iPad’s remote toolbar, select **Disconnect**.
4. Look at the physical laptop screen. Is it at the sign-in screen, or is Notepad still visible?
5. Record only the result in the table. Before taking a photo, hide email, document content, and notifications.

| Check | Result |
|---|---|
| Laptop screen immediately after disconnect | **Notepad work screen remained visible** (tested 2026-09-23) |
| Could reconnect | **Yes** (tested 2026-09-23) |
| Additional action needed | **Yes** — explicitly run Windows Lock before Disconnect. The sequence below was tested |

**Practical caution**: If you disconnect and walk away, someone near this laptop may see its work screen. If you are beside it, lock it directly with **Windows key + L**. When working remotely from the iPad, use the tested **Windows Lock → Disconnect** sequence below. See [Microsoft’s Windows account access guidance](https://support.microsoft.com/en-us/accounts-billing/security/user-account-access-in-windows) for Windows lock methods.

## 4. Tested — Lock First, Then Disconnect from the iPad

**Why the first test was done beside the laptop**: We needed to know whether it would be possible to reconnect after locking it. Fingerprint sign-in works locally, but the laptop’s fingerprint sensor is not available when you are away, so remote Windows PIN sign-in was tested separately.

1. Beside the laptop, connect from the iPad and open a Notepad window with no personal information.
2. In remote Windows, select **Start menu → Power icon → Lock**. Depending on the Windows version, it may be under **Start menu → user picture/account icon → Lock**. If neither menu shows Lock, stop and inspect the screen before proceeding.
3. Confirm that the physical laptop is at the lock screen, then select Disconnect on the iPad.
4. Reconnect from the iPad. Confirm that the lock screen appears and that you can sign in remotely. Do not record or share sign-in credentials.

**Result on 2026-09-23**: Selecting Windows Lock from the iPad did not end the CRD connection. After Disconnect, the physical laptop remained locked. After reconnecting from the iPad, the user entered the **Windows PIN** and returned to the work screen. This is a separate authentication step from the CRD connection PIN; neither PIN is recorded in any document.

## Laptop Lid Caution

If closing the lid puts the computer to sleep, it will be unavailable remotely. Lid behavior varies by device, so test it first. Do not change security or thermal settings without checking their effects. This item has not yet been tested on this laptop.

Previous: [Google Account security checks](google-account-checks.en.md) · [M3 README](../README.en.md)
