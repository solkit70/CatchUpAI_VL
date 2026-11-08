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

The first E trial uses only the three public files in the [synthetic test folder](../examples/trial-vault/). The actual vault mirror scope and the C (Google Drive) trial are deferred to the next session.

## Scenario Comparison

| Scenario | D · Manual transfer | E · Claude Code Remote Control (alternative) | C · Google Drive | A · Dropbox |
|---|---|---|---|---|
| S1 Put a voice memo into the Journal in the evening, word for word | Partial evidence: in M2, confirmed that the dictated sentences and the saved file are identical. Automatic entry into the Journal not tested. [M2 results](../../02-Muse-to-Vault/guides/transfer-comparison.en.md) | Not tested in M4. Existing mobile remote records do not verify the voice input → Journal flow. [Earlier Topic](../../../Claude-Code-Mobile-Remote-Execution/08-Native-Remote-Control/lab/remote-control-verification.md) | Not connected | Not connected |
| S2 Continue at home a note on an in-progress Topic left while away | Partially verified: downloaded 3 Muse Topic files, moved them to the vault, and continued the period review. The move is manual. [M3 handoff](../../vl_worklog/20261105_M3_Muse-My-Workflow.md#실습-4-결과) | Synthetic trial passed. A request sent from the phone created a new Markdown file in the home PC's test folder. The file contents and all three unchanged input hashes were verified on the PC. | Not connected | Not connected |
| S3 Search allowed vault material while away | Limited: material passed on through individual transfer · public repo links could be read. Not a search of the whole vault. [M2 results](../../02-Muse-to-Vault/guides/transfer-comparison.en.md) | Not tested in M4. Need to check search within the local work folder scope and the time to get results back. | Not connected | Not connected |
| S4 Continue away the work I was doing at home | Partially verified: after uploading the handoff packet, Muse continued the next task. Not real-time sharing of vault files. [M2 results](../../02-Muse-to-Vault/guides/transfer-comparison.en.md) | Synthetic trial passed. The home PC session read the three inputs, then received the follow-up from the phone and wrote the result in the same local session. The home PC and Claude Code were running during the test. | Not connected | Not connected |
| S5 The results of a day without the laptop arrive at the home PC automatically | Not met: download · email need a step where a person passes them on. Automatic sync not confirmed. [M2 comparison](../../02-Muse-to-Vault/guides/transfer-comparison.en.md) | Condition not met: remote work needs the home PC and local Claude Code running. It is not automatic retrieval while the laptop is off. [M8 structure](../../../Claude-Code-Mobile-Remote-Execution/08-Native-Remote-Control/concepts/native-remote-control-model.md#연결-구조) | Not connected. Unverified whether cloud results sync automatically to the local PC | Not connected. Unverified whether cloud results sync automatically to the local PC |

## Next Experiment Order

1. After the user confirms, choose the connection candidate to test. The candidates and their permission limits are in the [options map](solution-map.en.md#proposed-candidates-to-test).
2. Connect only the synthetic test folder to the chosen storage. Check the read · write · delete · share permissions and the folder scope, and stop if the permissions are more than needed.
3. Search for the synthetic events, have it explain the overlaps, then create a new result file without overwriting the original. Separately check whether that result is visible on the home PC.
4. Captures should show only synthetic file names: the connection list, the permission scope, the search results for the synthetic files, the new result file, and the result retrieved on the home PC.
5. Capture the screens for disconnecting and cleaning up the test material · result files only after getting the user's consent. File deletion is not done before separate approval.

## Status

**2026-11-08 · First E trial** — The synthetic workflow was continued from the phone (S4), and the result was verified on the home PC (S2). The file was written directly by the same local session. Its author metadata automatically included an account email, so the original result stayed local. [Trial WorkLog](../../vl_worklog/20261108_M4_Muse-My-Workflow.md#결과-검증)
