---
title: "Test Table by Seamless Scenario"
author:
  - Codex
created: 2026-11-05 07:47:00
visibility: public
tags:
  - muse-my-workflow
  - scenarios
lang: en
---

## Test Scope

[한국어](seamless-scenarios.md)

This table distinguishes earlier evidence from M4 test results. D (manual transfer) is the M2–M3 baseline. **E (Claude Code Remote Control) is an alternative outside Muse**. A phone controls the Claude Code session running on the home PC. Results for E do not count as evidence for a Muse connector or vault sync. [Official Claude Code guide](https://code.claude.com/docs/en/remote-control)

The E trial used three files from the [synthetic test folder](../examples/trial-vault/). For C, Muse read only the specified synthetic Drive test folder through the existing Google Drive connection and created a new result there. The Dropbox test also used only those three synthetic files in a private test folder and verified reading and result creation. Three reviewed `visibility: public` mirror candidates were uploaded to a separate Drive folder and were not used as C or Dropbox test inputs.

## Scenario Comparison

| Scenario | D · Manual transfer | E · Claude Code Remote Control (alternative) | C · Google Drive | A · Dropbox |
|---|---|---|---|---|
| S1 Put a voice memo into the Journal in the evening, word for word | Partial evidence: in M2, confirmed that the dictated sentences and the saved file are identical. Automatic entry into the Journal not tested. [M2 results](../../02-Muse-to-Vault/guides/transfer-comparison.en.md) | Not tested in M4. Existing mobile remote records do not verify the voice input → Journal flow. [Earlier Topic](../../../Claude-Code-Mobile-Remote-Execution/08-Native-Remote-Control/lab/remote-control-verification.md) | Connected; S1 not tested | Not connected |
| S2 Continue at home a note on an in-progress Topic left while away | Partially verified: downloaded 3 Muse Topic files, moved them to the vault, and continued the period review. The move is manual. [M3 handoff](../../vl_worklog/20261105_M3_Muse-My-Workflow.md#실습-4-결과) | Synthetic trial passed. A request sent from the phone created a new Markdown file in the home PC's test folder. The file contents and all three unchanged input hashes were verified on the PC. | Connector-level synthetic test: Muse read the three files in the specified test folder and created a result. This did not test continuation at home of a note started away. Folder-level access restrictions could not be established from the UI | Not tested · files were manually uploaded and handled in Muse on the PC browser; remote continuation of a Topic was not tested |
| S3 Search allowed vault material while away | Limited: material passed on through individual transfer · public repo links could be read. Not a search of the whole vault. [M2 results](../../02-Muse-to-Vault/guides/transfer-comparison.en.md) | Not tested in M4. Need to check search within the local work folder scope and the time to get results back. | Not tested | Partial evidence · pre-upload search returned 0; after upload, a folder-scoped search found all three sources and the folder listing showed the result file too. This did not test account-wide search or enforceable folder permissions |
| S4 Continue away the work I was doing at home | Partially verified: after uploading the handoff packet, Muse continued the next task. Not real-time sharing of vault files. [M2 results](../../02-Muse-to-Vault/guides/transfer-comparison.en.md) | Synthetic trial passed. The home PC session read the three inputs, then received the follow-up from the phone and wrote the result in the same local session. The home PC and Claude Code were running during the test. | Partial evidence: manually downloaded Muse’s result to the PC. Continuing away from work started at home was not tested. Automatic sync remains unverified | Not tested · Dropbox read and result creation were confirmed in the PC browser; phone use was not tested |
| S5 The results of a day without the laptop arrive at the home PC automatically | Not met: download · email need a step where a person passes them on. Automatic sync not confirmed. [M2 comparison](../../02-Muse-to-Vault/guides/transfer-comparison.en.md) | Condition not met: remote work needs the home PC and local Claude Code running. It is not automatic retrieval while the laptop is off. [M8 structure](../../../Claude-Code-Mobile-Remote-Execution/08-Native-Remote-Control/concepts/native-remote-control-model.md#연결-구조) | Not met: manually downloaded the result; automatic sync is unverified | Partial · after desktop setup, all four files showed Available on this device while awake. The same local states remained after a Sleep request, but S0 entry/exit was not independently verified and no cloud change was made during sleep, so the sleep effect is undetermined. After relaunching Dropbox, Muse found all three source names and listed four folder items |

## Next Experiment Order

1. Dropbox search passed after upload. Follow up separately on folder-scope enforcement, mobile access, and whether the 403 notification recurs during normal Muse use.
2. Keep Google Drive folder scope, mobile access, and automatic sync as separate untested items. Do not upload more material beyond the user's approved scope.
3. Decide the whole-vault mirror policy before the next module, and review the public-marked candidate scope and internal-material exclusions.
4. Captures should show only synthetic file names. Do not enter deletion or disconnect flows before user approval.

## Status

**2026-11-08 · E · C · A synthetic trials** — E passed S2 and S4 through Claude Code Remote Control, an alternative outside Muse. C passed reading, result creation, and manual PC retrieval in its specified synthetic Drive folder. A passed reading, result creation, and post-upload search in its private Dropbox test folder; the earlier 0-result search preceded upload. Dropbox desktop setup synced all four files locally while awake. A Sleep request was followed by the same local statuses, but the S0 transition and any cloud change during sleep were not verified, so the sleep effect remains undetermined. After Dropbox was relaunched, Muse found all three source filenames and listed all four items in the named folder; all calls succeeded. After the Chrome update and restart, the 403 notification was not visible on the current Muse page. The user reports that it occurs frequently, so resolution and cause remain undetermined. No mobile device was available to test Muse mobile access, and folder-scope enforcement remains unverified. [Trial WorkLog](../../vl_worklog/20261108_M4_Muse-My-Workflow.md#c-google-drive-시험)
