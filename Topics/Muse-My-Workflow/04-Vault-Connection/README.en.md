# M4 — Vault Connection Options — Home and Away, Seamless

[한국어](README.md)

**Status**: 🔄 In progress 7/8 (started 2026-11-05 · Codex) — E synthetic S2 · S4, C synthetic Drive read · result creation · manual PC retrieval, and the separate upload of 3 approved public candidates verified. Dropbox connection and action-level Allow settings were checked; three synthetic files were uploaded to a private test folder and Muse read them by folder path and created a result. A search before upload returned 0 results; after upload, a folder-scoped repeat found all three files. The whole-vault mirror policy remains undecided.
**Estimated study time**: 3 hours

## Progress

In Lab 1, I checked the official documentation and Muse screens. In Lab 2, I ran the draft mirror rules and a real-vault preview. I reviewed the internal preview report and, after user approval, uploaded its 3 public candidates to a separate Drive folder. This was not blanket approval to mirror the whole vault. E · Claude Code Remote Control, an alternative outside Muse, passed synthetic S2 · S4. C · Google Drive was verified for reading and writing in the specified synthetic folder and manually downloading the result to the PC. On 2026-11-08, all Dropbox action permissions displayed Allow (download and write were Custom Allow). After the user approved the device-access prompt, I uploaded 3 synthetic files to the private `Muse M4 Test - Synthetic` folder. The filename search before upload returned 0 results. After upload, a folder-scoped repeat found all three files; reading by folder path and creating `m4-dropbox-result.md` also succeeded. Dropbox showed all four files and the result content. Automatic PC retrieval was verified while awake: after Dropbox desktop setup, all four files showed Available on this device. The same local statuses remained after a Sleep request, but S0 entry/exit and a cloud change during sleep were not verified, so the sleep effect is undetermined. After Dropbox relaunch, Muse again found all three source names and listed four folder items. Mobile access and folder-scope restriction remain untested.

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
- **There is no sync feature.** A connector is a connection that looks in when needed. So "the work I did away arrives at the home PC by itself" (S5) is not yet met by any candidate.
- **A mirror copy holding only public-marked files works safely.** In the real vault preview: 3 candidates to include · 55,975 excluded · 0 copied — internal markers 112 · `visibility: internal` 58 were all left out.
- **What I could not check** — The pre-upload search returned 0 results; a folder-scoped search after upload found all three files. Technical enforcement of folder-only access, mobile access, and Sleep effect is undetermined: the same files remained local after the request, but the S0 transition and a cloud change during sleep were not verified. Awake-state automatic PC retrieval was verified after desktop setup: all four files showed Available on this device. A 403 notification seen earlier was not tied to a failed Dropbox operation. After the Chrome update and restart, it was not visible on the current Muse page; the user reports seeing it frequently, so resolution and cause remain undetermined. Google Drive folder scope and automatic sync remain unverified.

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
