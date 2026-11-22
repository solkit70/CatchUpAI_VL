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
| S5 The results of a day without the laptop arrive at the home PC automatically | Not met: download · email need a step where a person passes them on. Automatic sync not confirmed. [M2 comparison](../../02-Muse-to-Vault/guides/transfer-comparison.en.md) | Condition not met: remote work needs the home PC and local Claude Code running. It is not automatic retrieval while the laptop is off. [M8 structure](../../../Claude-Code-Mobile-Remote-Execution/08-Native-Remote-Control/concepts/native-remote-control-model.md#연결-구조) | Not met: manually downloaded the result; automatic sync is unverified | **Partial for synthetic folder** · in addition to awake-PC sync, `pc-off-return-20261114.md` created through mobile Muse while the PC was fully shut down appeared in the designated Dropbox folder after restart. The path and `PC-OFF-RETURN-731` contents were confirmed locally. The actual vault path and normal day-long operation remain untested, so S5 overall stays partial |

## Next Experiment Order

1. The Dropbox synthetic-folder trial passed for mobile Muse file creation while the PC was fully shut down and automatic return after restart. Follow up separately on S0 sleep behavior, enforceable folder scope, and whether the 403 notification recurs during normal Muse use. Mobile file creation through the existing Dropbox connection was confirmed in this trial; the actual vault path remains untested. See the [PC-off trial WorkLog](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#pc-완전-종료-후-dropbox-결과-재확인--통과-2026-11-14).
2. Keep Google Drive folder scope, mobile access, and automatic sync as separate untested items. Do not upload more material beyond the user's approved scope.
3. Decide the whole-vault mirror policy before the next module, and review the public-marked candidate scope and internal-material exclusions.
4. Captures should show only synthetic file names. Do not enter deletion or disconnect flows before user approval.

## Status

**November 8 · E · C · A synthetic trials, and November 14 PC-off trial** — E passed S2 and S4 through Claude Code Remote Control, an alternative outside Muse. C passed reading, result creation, and manual PC retrieval in its specified synthetic Drive folder. A passed reading, result creation, post-upload search, and awake-PC sync. In the follow-up PC-off trial, a synthetic file created through mobile Muse while the PC was shut down appeared in the Dropbox folder after restart with the expected path and contents. The S0 sleep transition and any cloud change during sleep remain unverified, as does enforceable folder scope. After Dropbox was relaunched, Muse found all three source filenames and listed all four items in the named folder. After the Chrome update and restart, the 403 notification was not visible on the current Muse page, but the user reports it occurs frequently, so resolution and cause remain undetermined. The actual vault path remains untested. See the [PC-off trial WorkLog](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#pc-완전-종료-후-dropbox-결과-재확인--통과-2026-11-14) and [earlier trial WorkLog](../../vl_worklog/20261108_M4_Muse-My-Workflow.md#c-google-drive-시험).
