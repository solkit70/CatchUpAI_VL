---
title: "Draft Task-Type Routes for Muse and the Vault"
author:
  - Codex
created: 2026-11-08 15:38:59
tags:
  - muse-my-workflow
  - task-routing
  - draft
  - lang-en
---

## Status and Scope

[한국어](task-route-table.md)

**Direction agreed during review.** Use Muse as the primary remote workspace. First test how Muse can reproduce the vault folder tree, then compare Dropbox and Google Drive if a backup route is needed. Email is the last option for retrieving results. Determine the scope and sync method for actual vault copies after the trials.

## Routes by Task

| Task | Route or trial order | Findings and remaining checks |
|---|---|---|
| Preserve a voice memo verbatim | Save the transcript as Markdown in Muse. Use the retrieval order below at home, then review the verbatim text and bring it into the vault's `_Inbox_/` | Automatic sync to the vault and automatic filing in Journal remain unverified |
| Check email and calendar | Handle them directly in Muse using the already connected email and Google Calendar. Save only information that needs a local copy as Markdown, then add it to the vault at home | There is no need to copy all email or calendar data locally. Follow app confirmation steps for sending messages or changing events |
| Continue a Topic started away from home | Download the M2/M3 handoff package from Muse Library and continue in the local vault | In M3, three Markdown files retained their folder structure and Codex resumed the work |
| Search or edit actual vault material with AI | First, work in Muse and retrieve results from Library. Second, test a cloud folder available through a Muse connector. Verify full-vault scale and automatic sync separately | Muse ZIP import preserved nested paths. Muse then returned the whole small synthetic tree as one ZIP after editing a nested file and adding another; all four file paths and hashes were checked against the original tree or prior downloads. This verifies manual archive round-trip for a small fixture, not full-vault file/size limits or automatic synchronization. A nested synthetic vault in the Dropbox desktop sync folder also passed connector read/write, awake-PC return, and manual conflict recovery. It did not test the actual vault path. A nested folder uploaded to Drive web returned 404 for Muse search/ID lookup and root write. A separate synthetic `Computers → My PC → trial-vault` passed Muse read, write, and automatic return to the running PC |
| Retrieve a Muse result at the home PC | 1. Retrieve individual files or a synthetic whole-tree ZIP from Muse Library, review, and manually add them. 2. If automatic retrieval is needed, test bidirectional Drive or Dropbox sync. 3. Use email only if both routes are difficult | Muse individual downloads and a whole small synthetic ZIP return both succeeded. In Dropbox's synthetic sync folder, a new file created through mobile Muse while the PC was fully shut down appeared after restart at the expected path with the exact marker: 18 bytes including LF, SHA-256 `DD753DDCF1DA01EADC5E50A23CA64C7B6708C882AC38806C0E718D74F94A307D`. This verifies PC-off return only for that synthetic Dropbox folder, not the actual vault path. A new Markdown file created by Muse in the synthetic Drive `trial-vault` also synced automatically to the running PC. Dropbox Backup is one-way and cannot return Muse edits to the source |
| Automate a vault mirror | Determine what can be automated after testing folder structure preservation and retrieval of changes | Check whether new and edited files can be applied at the same relative paths and what happens when both copies are edited. Follow the mirror policy for any external copy of actual vault files |

## PC-off trial — procedure and result (November 14, 2026)

Dropbox sync to an awake PC has been verified, but the fully powered-off interval has not. Use only the already-authorized synthetic `Muse M4 Test - Synthetic` folder. Do not use actual vault files, create new shares, grant new permissions, or use Dropbox Backup.

1. While the PC is on, confirm Dropbox is current. Leave the existing trial files unchanged.
2. Fully **shut down** Windows; sleep does not count for this trial.
3. In Muse on the phone, use the existing Dropbox connection to create `pc-off-return-20261114.md` in the synthetic trial folder with the unique body marker `PC-OFF-RETURN-731`. Wait for Muse to confirm the save.
4. Start the PC. After Dropbox launches and finishes syncing, check whether the same filename, relative path, and marker appear in the local trial folder.
5. Compare the cloud file and local return by path and contents. If the file does not arrive or differs, pause further changes and record the cause.

**Result (November 14, 2026): passed.** `pc-off-return-20261114.md` appeared in the designated synthetic Dropbox folder after the PC restarted; its path, contents, and SHA-256 were verified. This only validates the synthetic Dropbox folder, not the actual vault path or Muse-native automatic sync. S5 remains partial because actual-vault routing and day-to-day operating conditions remain untested. See the [M4 WorkLog](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#pc-완전-종료-후-dropbox-결과-재확인--통과-2026-11-14).

## Stop and Roll Back

If a result is missing or its contents differ during a trial, pause the vault import and compare the result in Muse with the retrieved copy. Keep the trial copies until the cause is understood.

Use the trial findings to decide how to retry, recover, and clean up external copies in actual operation.

## Remote Work and Retrieval Order

Manage remote work files in Muse. At home, retrieve the results you need from Muse first and bring them into the vault. If that route is difficult, compare Google Drive and Dropbox as backup options. Use email if both earlier routes are difficult.

## Vault Structure and Sync Research

Meta documents file uploads and creating and editing files in the Muse workspace. M3 verified individual downloads from nested folders that Muse created, and the M2 full data export ZIP retained workspace-relative paths. The help pages checked on November 14, 2026 did not document bulk import of a local folder tree, vault-scale file count or capacity limits, or automatic change sync with a Windows vault. [Meta file help](https://www.meta.com/help/superintelligence/2074655449783957/) · [Meta data export](https://www.meta.com/help/superintelligence/2225571704857152/) · [M2 retrieval trials](../../02-Muse-to-Vault/guides/transfer-comparison.en.md)

1. **Test Muse first.** Use a synthetic vault with nested folders, same-named notes, links, and an attachment to check folder upload or ZIP import. Check whether the imported tree can be used without creating folders or specifying paths again.
2. **Check retrieval of changes.** With the home PC off, edit a note and create a new one from a phone. After startup, check whether the changes can be brought back to the same relative paths and what happens if a file was edited on both sides.
3. **Compare backup paths.** Google says an existing PC folder can sync under `Computers` with Drive for desktop. Muse read three files in the synthetic `trial-vault`, created one new Markdown file there, and Drive for desktop synced it back to the running PC. Dropbox's standard sync folder passed synthetic nested read, write, and PC return, but the actual vault path itself was not tested. See the [backup storage comparison](#backup-storage-comparison-update-november-14-2026) below for evidence and remaining tests.

## Backup Storage Comparison Update (November 14, 2026)

Meta describes connecting cloud storage and organizing files with Muse, but its public help does not specify a vault-scale limit or automatic bidirectional sync between Muse storage and a local vault. The Muse-native path can import a ZIP with nested paths and retrieve individual files, but folder-wide export remains unverified. Our same-file trial showed Muse did not automatically merge edits made on both sides, so manual review is required. [Muse file help](https://www.meta.com/help/superintelligence/2074655449783957/) · [Muse productivity overview](https://ai.meta.com/muse/productivity/)

The Dropbox connector can read and write files. In Dropbox account settings, Muse's listed permissions included editing content across Dropbox files and folders and managing file requests, sharing settings, and collaborators. The screen offered no technical restriction to one test folder. Dropbox documents Select Access, App Folder, and Full Dropbox levels, but Muse's detail panel did not label which category applied. Treat the displayed broad permission as close to whole-account access; a prompt limiting a task to one path does not narrow the account grant. No permission was changed and Muse was not disconnected. [Dropbox third-party app permissions](https://help.dropbox.com/integrations/third-party-apps)

Standard Dropbox sync reflects changes among files in the Dropbox folder, so whether the existing vault path can stay in place or must move needs more review. Dropbox Backup can back up selected computer folders, but Dropbox describes it as one-way and says backed-up copies cannot be edited on dropbox.com; it is unsuitable for returning Muse edits to the original. [Dropbox-Muse connector help](https://help.dropbox.com/integrations/connect-to-meta-muse) · [Dropbox Backup FAQ](https://help.dropbox.com/organize/dropbox-backup-faq) · [Dropbox sync status](https://help.dropbox.com/sync/check-sync-status)

An additional check of official guidance found that standard sync operates on files in the Dropbox folder, while Dropbox for Windows does not support junctions or symlinks. Dropbox Backup can select external folders, but it is one-way and its cloud backup cannot be edited. The official sources reviewed did not document a supported way to keep the current vault path and sync that folder itself through standard Dropbox sync. This means we did not find a supported procedure in the reviewed docs; it does not rule out every unverified product feature. No actual vault move or separate mirror was made. [Dropbox sync status](https://help.dropbox.com/sync/check-sync-status) · [Dropbox Backup FAQ](https://help.dropbox.com/organize/dropbox-backup-faq) · [Windows junction/symlink support](https://help.dropbox.com/sync/symlinks)

Google Drive for desktop can sync an existing local folder through `Folders from your computer → Sync with Google Drive`. Google says it appears under `Computers` and changes sync in both directions. The Drive API overview lists the `user`, `domain`, `drive`, and `allDrives` corpora, but does not describe the `Computers` view or whether Muse's connector can access it. That API documentation alone does not establish access or lack of access. Whether Muse can find, read, and edit the `Computers` path remains untested. Drive for desktop was installed on November 14, 2026, and only the synthetic `trial-vault` was selected and synced. The November 15 test covered Muse access and automatic return to the running PC. Google also documents that a computer-folder connection is tied to that device. [Google Drive for desktop help](https://support.google.com/drive/answer/10838124?hl=en) · [Drive API files and folders overview](https://developers.google.com/workspace/drive/api/guides/about-files) · [Drive streaming and mirroring](https://support.google.com/drive/answer/13401938?hl=en)

### Google Drive `Computers` prerequisite check (November 14, 2026)

Google's official instructions require opening Drive for desktop and selecting `Settings → Preferences → Folders from your computer → Sync with Google Drive` to sync a local computer folder bidirectionally under `Computers`. A folder upload through the website places content in `My Drive` and does not set up this computer-folder sync. [Google Drive for desktop help](https://support.google.com/drive/answer/10838124?hl=en)

Drive for desktop was installed on November 14, 2026. Only the synthetic `trial-vault` folder was selected and its upload completed. The official setup screen and sync-complete screen were captured for possible video reference. On November 15, Muse read three files in `Computers → My PC → trial-vault` and created one Markdown file in that folder. The returned file on the running PC matched the 76-byte payload and SHA-256 reported by Muse. PC-off return and actual vault sync remain untested. [November 15 WorkLog](../../vl_worklog/20261115_M4_Muse-My-Workflow.md#google-drive-computers-읽기와-pc-자동-회수--통과)

### Dropbox sync-folder nested synthetic vault trial (November 14, 2026)

We placed the approved synthetic tree inside the existing Dropbox test folder. Dropbox web found it and displayed the nested `Topics` and `assets` structure. Muse's Dropbox connector, restricted by instruction to that one synthetic folder, listed the files and read `Topics/Alpha/note.md`: it returned `ALPHA-731` and resolved `[Beta](../Beta/note.md)` to `Topics/Beta/note.md` and `![Sample](../../assets/sample.png)` to `assets/sample.png`. The PNG target existed in Dropbox web, although Muse's response preview showed “Image not found.” The source note was not changed.

Muse then created `Muse-M4-Connector-Probe-20261114.md` at the synthetic root (`DROPBOX-WRITE-731`, 18 bytes) and `Topics/Alpha/Muse-Result-20261114.md` (`ALPHA-WRITE-731`, 16 bytes including the trailing newline). Both appeared in the local Dropbox sync folder at the same relative paths with matching contents while the PC was awake and the Dropbox desktop app was running. This verifies Dropbox-web-to-PC return for new synthetic files at both levels, but it does not verify the original vault path or synchronization while the PC is off. Existing files were not changed, and no content was shared, moved, or deleted. See the [M4 worklog](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#dropbox-동기화-폴더의-중첩-합성-vault-시험-2026-11-14).

The UI screens for the Dropbox tree and Muse read/write result were captured in the current conversation. For any public video, recapture a clean view that excludes the unrelated side-chat titles; these captures have not yet been saved as local image assets.

**Mixed-format reading, large synthetic search/edit, and Obsidian wikilink results (November 14, 2026):** Across six non-Markdown samples, Python, JSON, and CSV were exact. PNG dimensions and shape were right, but OCR omitted the space in `SYNTH 731`; MP4 duration, resolution, and solid-color frame analysis matched. A separate one-page synthetic PDF test followed `![[assets/field-note.pdf]]`, extracted its selectable TITLE, BODY, and TABLE fields exactly, and distinguished a same-basename PDF in `Archive`. The returned ZIP had 3 files and 1,441 payload bytes; its 2,519-byte size, SHA-256 `4fb63dbb9d9fb7fe0415c5abf9d2f501a3614790704e4b593d4cb24b0c1af4d1`, and local pypdf text extraction matched Muse's report. This verifies one linked text-PDF case only; scanned/OCR PDFs, annotations, complex tables, and multipage behavior remain untested. In a separate 5,777-file synthetic Markdown tree, Muse reported searching all files and found the exact path and line for a four-token phrase that local source verification showed occurs once. Muse edited only the specified note and returned the whole tree in a ZIP; local SHA-256 comparison found no missing or extra files and exactly one changed file, with the expected 25-byte increase. Obsidian fixtures confirmed that `[[Topics/Beta/note|Beta target]]` resolved to Beta rather than its same-basename Gamma decoy, while pathless `[[note]]` with duplicate candidates was called ambiguous and left unresolved. A separate fixture resolved `[[Topics/Beta/note#Target Heading|Heading target]]` to the body under `## Target Heading` and `[[Topics/Beta/note#^block-731|Block target]]` to the paragraph carrying `^block-731`. Both fragments were found in the same Beta note, and only the specified block line was edited. The returned ZIP had three files and 242 payload bytes; its 2,016-byte size and SHA-256 `9a0b3ff8c740b831bc25131da61d95220658f7cf74fb7cdd3042768c8de246ea` matched Muse's report, and local inspection confirmed all paths and hashes. This supports basic vault-relative path/alias handling, ambiguity avoidance, and heading/block fragment targeting on tiny fixtures. Small image and one-page PDF attachment-link cases passed, and a tiny fixture backlink search found its incoming link paths; an Obsidian backlinks index and the actual vault remain unverified. Details: [M4 WorkLog — image attachment wikilink test](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-이미지-첨부-wikilink-경로판독-시험-2026-11-14) and [PDF attachment wikilink test](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-pdf-첨부-wikilink-경로텍스트-판독-시험-2026-11-14). Full-vault capacity remains unknown: the 64.614 GiB Vault is about 637 times larger than the 103.8 MiB payload and has about 9.5 times as many files. Meta says uploaded and created files are stored in System Files; the Library UI showed per-file sizes but no aggregate usage or quota. Muse ZIP return is manual and does not establish automatic local sync. Dropbox's broad grant remains unchanged. Drive for desktop is installed and the synthetic folder is synced; Muse access to `Computers` remains untested. Details: [M4 WorkLog — Obsidian wikilink test](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-위키링크-해석대상-편집경로-회수-시험-2026-11-14), [M4 WorkLog — ambiguous wikilink safety test](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-모호한-basename-wikilink-안전-처리-시험-2026-11-14), [M4 WorkLog — heading/block fragment link test](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-headingblock-fragment-링크-시험-2026-11-14), [M4 WorkLog — search, edit, and storage UI](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#muse-저장-파일-관리-표시-및-대규모-검색-편집-시험-2026-11-14), [Meta Help](https://www.meta.com/help/superintelligence/2225571704857152/).

## Muse Storage Limit Check (November 14, 2026)

The consumer Muse public pages and Library UI reviewed so far show no account-wide file or ZIP quota. The 1 GiB per-file and default 100 GiB per-team allowance in Meta Model API documentation applies to the Model API Files service; there is no evidence that it applies to the consumer Muse Library. Therefore, whether Muse can hold the 64.614 GiB actual vault remains unknown. The largest Muse-native round trip verified so far is a synthetic payload of 5,777 Markdown files and 103.8 MiB. See [M4 WorkLog — official Muse storage-limit review](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#muse-저장-용량-공식-문서-재확인-2026-11-14) and [Meta Model API file handling](https://dev.meta.ai/docs/file-handling).

## Obsidian Backlink Search Check (November 14, 2026)

In an isolated four-note fixture, Muse found two incoming wikilinks to one target note: one omitted the `.md` extension (`[[Topics/Shared/target|Target]]`) and one included it (`[[Topics/Shared/target.md|Beta target]]`). It reported the two source notes based on link target paths and distinguished them from alias/general-word matches. The returned ZIP matched locally: four Markdown files, 125 payload bytes, 2,434 bytes compressed, SHA-256 `16afcccdd65b31f9eb61687abc6938ae1cf34008291dcbcf49118ca27b3e52ac`, with expected paths and sizes. This only verifies text-based link discovery in a tiny fixture; it does not prove an Obsidian backlinks pane/index, whole-vault indexing, broken-link handling, or large-scale performance. See [M4 WorkLog — backlink search test](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-backlinks-링크-대상-탐색-시험-2026-11-14).

## Synthetic Round Trip at Actual Vault File Count (November 14, 2026)

A separate synthetic tree with 55,035 small Markdown files was created and round-tripped through Muse as a ZIP. Muse reported 825,535 payload bytes; the ZIP was 14,045,667 bytes (55,035 files plus 57 directory entries). Local inspection confirmed file count, payload size, first/last paths, unique marker location, and ZIP integrity. SHA-256 `c522fd8abf4ffb4b30ee37d9a0bc556bb681bc73c56127a483f3f7d08b95b9b0` matched Muse's report. This tests a synthetic Markdown tree at the actual vault's file count, but not its 64.614 GiB payload, real format/size distribution, consumer Muse quota, or automatic sync. See [M4 WorkLog — 55,035-file count test](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#muse-native-실제-vault-파일-수-대응-합성-시험-2026-11-14).

## Decisions After the Trials

The user decisions needed to start the synthetic vault trials are complete. Use the findings to make the following decisions when needed for actual use.

- Allowed data levels, paths, and file types when bringing over actual vault materials
- Service, destination folder, and connector permissions if a backup service is needed
- Manual or automatic import, frequency if scheduled, and copy retention period
- Retry and recovery steps and when to clean up destination copies

## Related Material

- [Scenario comparison](seamless-scenarios.en.md#scenario-comparison)
- [Mirror policy draft](mirror-policy.en.md#approval-pending)
- [Latest M4 WorkLog](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#보조-저장소-동기화-방식-리서치)
