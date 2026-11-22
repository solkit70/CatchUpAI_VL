# M4 — Vault Connection Options — Home and Away, Seamless

[한국어](README.md)

**Status**: 🔄 In progress 7/8 (started 2026-11-05 · Codex) — E synthetic S2 · S4, C synthetic Drive read · result creation · manual PC retrieval, and separate upload of 3 approved public candidates verified. Dropbox synthetic nested-vault read/write, awake-PC return, and manual conflict recovery passed. Muse-native import and whole-tree ZIP return also passed for a small synthetic tree: all 4 paths and hashes were checked, including an edited file and a new file. This does not establish whole-vault limits or automatic sync. The whole-vault mirror policy remains undecided.
**Estimated study time**: 3 hours

On November 14, 2026, Muse returned a 5,777-file, 103.8 MiB synthetic Markdown ZIP with paths preserved through a unique-phrase search and single-file edit. Obsidian fixtures confirmed that Muse followed a path-qualified link to the Beta note rather than a same-basename Gamma note, and treated pathless `[[note]]` with two candidates as ambiguous. A separate fixture showed that `#Target Heading` and `#^block-731` resolve to different fragments in the same note; Muse edited only the specified block paragraph. Tiny attachment fixtures verified an image link with PNG pixel reading and a PDF embed that extracted selectable text from the explicitly linked one-page PDF and distinguished a same-basename decoy. Local inspection confirmed returned ZIP paths and hashes. These cases verify basic path/alias handling, ambiguity recognition, fragment targeting, and two attachment types on small fixtures; a separate tiny fixture found backlink paths by scanning wikilinks, but complex PDFs, an Obsidian backlinks pane/index, and the actual vault remain unverified. Muse's Library → System Files exposes uploaded and created files, but neither the UI nor public help showed an aggregate quota. The actual vault is about 637 times larger than the synthetic payload, so full-vault capacity remains unproven. Six mixed non-Markdown files also returned with identical paths and bytes. Content reading was exact for Python, JSON, and CSV; Muse recognized the PNG dimensions and shape but omitted a space in OCR. MP4 metadata and decoded solid-color frame matched the fixture. Drive for desktop is installed, and sync of only the synthetic `trial-vault` completed; Muse access to `Computers` and return of Muse-created files remain untested. Dropbox standard sync passed for a synthetic folder but not the actual vault path. Dropbox Backup is one-way and cannot return Muse edits to the source. See the [task route table](guides/task-route-table.en.md#backup-storage-comparison-update-november-14-2026) and [November 14 WorkLog](../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-pdf-첨부-wikilink-경로텍스트-판독-시험-2026-11-14) for evidence.

An additional synthetic fixture found two incoming Obsidian wikilinks to a target note, one with the `.md` extension omitted and one explicit. This is link discovery by scanning a tiny fixture; it does not establish an Obsidian backlinks pane/index or whole-vault indexing. No public quota was found for the consumer Muse Library. Meta Model API storage limits belong to a separate product and were not applied to Muse. See the [backlink WorkLog](../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-backlinks-링크-대상-탐색-시험-2026-11-14) and [storage-limit review](../vl_worklog/20261114_M4_Muse-My-Workflow.md#muse-저장-용량-공식-문서-재확인-2026-11-14).

An additional synthetic Markdown tree matching the actual vault's 55,035-file count was ZIP round-tripped through Muse. Local inspection confirmed count, payload, paths, marker, and ZIP integrity. This addresses file count only: its payload was 825,535 bytes, so it does not establish capacity for the 64.614 GiB vault or its real format/size distribution. See the [file-count WorkLog](../vl_worklog/20261114_M4_Muse-My-Workflow.md#muse-native-실제-vault-파일-수-대응-합성-시험-2026-11-14) and [task route table](guides/task-route-table.en.md#synthetic-round-trip-at-actual-vault-file-count-november-14-2026).

On November 14, 2026, `pc-off-return-20261114.md`, created through mobile Muse while the PC was fully shut down in the synthetic Dropbox test folder, appeared in the local Dropbox folder after restart. The relative path, `PC-OFF-RETURN-731` contents, 18-byte size, and SHA-256 were verified. Mobile creation and automatic return after PC shutdown are confirmed for this synthetic folder. The actual vault path, S0 sleep behavior, and enforceable folder-only connector scope remain unverified. See the [trial WorkLog](../vl_worklog/20261114_M4_Muse-My-Workflow.md#pc-완전-종료-후-dropbox-결과-재확인--통과-2026-11-14).

## Progress

In Lab 1, I checked the official documentation and Muse screens. In Lab 2, I ran the draft mirror rules and a real-vault preview. I reviewed the internal preview report and, after user approval, uploaded its 3 public candidates to a separate Drive folder. This was not blanket approval to mirror the whole vault. E · Claude Code Remote Control, an alternative outside Muse, passed synthetic S2 · S4. C · Google Drive was verified for reading and writing in the specified synthetic folder and manually downloading the result to the PC. On 2026-11-08, all Dropbox action permissions displayed Allow (download and write were Custom Allow). After the user approved the device-access prompt, I uploaded 3 synthetic files to the private `Muse M4 Test - Synthetic` folder. The folder-scoped search, path-specific read, result creation, and return to the awake PC were verified. On November 14, a new synthetic file created through mobile Muse while the PC was fully shut down appeared in the Dropbox folder after restart. Mobile creation and return after PC shutdown passed for this synthetic folder. S0 sleep behavior and enforceable folder-only permissions remain unverified; the actual vault path was not tested.

## 📚 Learning Order

1. [Two connection models](concepts/connection-models.en.md) — cloud-agent model · remote-console model, connection, not sync, mirror copy and inbox, three things to check before connecting.
2. [Options map](guides/solution-map.en.md) — 8 candidates, limits and costs, scope of the next test.
3. [Mirror policy draft](guides/mirror-policy.en.md) — include · exclude rules and approval boundaries.
4. [Scenario comparison table](guides/seamless-scenarios.en.md) — evidence from D · E · C · A, unverified scope, next tests, and screens to capture.
5. [Synthetic test folder](examples/trial-vault/) — 3 synthetic Markdown files marked public.
6. [Preview script](scripts/build_mirror.py) — by default it only reports; a real copy needs an explicit `--apply`.
7. [Example config](scripts/mirror_config.example.yaml) — a YAML-compatible config in JSON syntax that targets only the synthetic test folder.
8. [Synthetic preview report](examples/mirror-report-sample.md) — 1 public file as a candidate to include; 4 personal · internal · unclassified · non-Markdown files excluded.
9. [Draft task-type route table](guides/task-route-table.en.md) — evidenced workflows, pending approval boundaries, and stop/rollback rules.
10. [M4 WorkLog](../vl_worklog/20261108_M4_Muse-My-Workflow.md) — observations from Labs 1 · 2 and the next points to check.

## What I Have Found So Far

- **All 8 candidates** are organized with official documentation and Muse screens, along with check dates. I also tested Dropbox read and write in a synthetic folder.
- **Manual Muse-native whole-tree return passed for the small synthetic fixture.** Muse returned an archive containing the edited and new files while preserving all four paths and hashes. This is a manual Library transfer, not automatic sync to the local vault. Full-vault size/file-count limits and the complete workflow with the PC off remain untested, so automatic S5 arrival is not demonstrated.
- **A mirror copy holding only public-marked files works safely.** In the real vault preview: 3 candidates to include · 55,975 excluded · 0 copied — internal markers 112 · `visibility: internal` 58 were all left out.
- **What I could not check** — Dropbox sync at the actual vault path, technical enforcement of folder-only access, and changes made during Windows S0 sleep remain unverified. The PC-off automatic return passed in the synthetic folder only and does not prove the full S5 scenario for the actual vault. The earlier 403 notification was not tied to a failed Dropbox operation. It was not visible after the Chrome update and restart, but the user reports seeing it repeatedly, so resolution and cause remain unknown. For Google Drive, Muse's ability to find and edit a `Computers` sync path and the automatic return of new changes to the PC remain untested. It is also unknown whether standard Dropbox sync can preserve the existing vault location without moving it.

## How to Reproduce Lab 2

The command below makes five synthetic Markdown files in a temporary folder and runs only a preview. The temporary folder is cleaned up automatically after the run, and no real vault material is read or copied.

```powershell
python Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow/04-Vault-Connection/scripts/build_mirror.py --demo --report Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow/04-Vault-Connection/examples/mirror-report-sample.md
```

To preview the three fixed files again, use the example config. Do not add the real copy option.

```powershell
python Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow/04-Vault-Connection/scripts/build_mirror.py --config Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow/04-Vault-Connection/scripts/mirror_config.example.yaml --report Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow/vl_worklog/trial-vault-preview-internal.md
```

When targeting real paths, the user must first review the source, destination, and include paths in the config file. The default run is a preview, and `--apply` is not added before the policy and the report are approved. `--apply` is not run without separate approval.

## Screens for the Video

- [Muse business connectors](assets/muse-business-connectors.jpg) — the list showing GitHub and Dropbox.
- [Muse Data controls](assets/muse-data-controls.jpg) — the memory import, data download, and reset menus.
- [Dropbox permissions (2026-11-08)](assets/20261108-muse-dropbox-permissions.jpg) — connected account and per-action Allow states. Check for account identifiers before using it in video.
- [Dropbox device-access prompt (2026-11-08)](assets/20261108-dropbox-permission-prompt-1.jpg) — private test folder and file-upload permission prompt.
- [Dropbox upload completed](assets/20261108-dropbox-upload-success.jpg) · [Four files in the test folder](assets/20261108-dropbox-four-files.jpg).
- [Muse analysis result](assets/20261108-muse-dropbox-analysis-result.jpg) · [Dropbox result content, top](assets/20261108-dropbox-result-content-top.jpg) · [bottom](assets/20261108-dropbox-result-content-bottom.jpg).
- [Dropbox result-file verification](assets/20261108-dropbox-result-verified.jpg).

## Navigation

- Previous · [M3 — VibeLearn AI on Muse](../03-VibeLearn-on-Muse/README.en.md)
- Next · M5 — One week of real use and a usage guide ([roadmap](../vl_roadmap/20261018_RoadMap_Muse-My-Workflow.md#m5---1주일-실제-사용과-사용-가이드)) — starts with the combination chosen in M4
