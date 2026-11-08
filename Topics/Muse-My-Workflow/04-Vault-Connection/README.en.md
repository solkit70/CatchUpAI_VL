# M4 — Vault Connection Options — Home and Away, Seamless

[한국어](README.md)

**Status**: 🔄 In progress 3/8 (started 2026-11-05 · Codex) — Lab 1 checklist · Lab 2 preview done, Lab 3 being prepared (synthetic test folder · scenario comparison table). **Lab 3 starts once Changsoo Park reviews the preview report and chooses the candidates to test (D / E / C Drive / A)**
**Estimated study time**: 3 hours

## Progress

In Lab 1, I checked the official documentation and the Muse screens. In Lab 2, I ran the mirror copy rules draft and previews of a synthetic vault and the real vault. To prepare for Lab 3, I made a synthetic public test folder and a scenario comparison table. The real report is internal material, kept inside the vault, and is waiting for review. Choosing and connecting an external storage candidate, and copying, have not been done yet.

## 📚 Learning Order

1. [Two connection models](concepts/connection-models.en.md) — cloud-agent model · remote-console model, connection, not sync, mirror copy and inbox, three things to check before connecting.
2. [Options map](guides/solution-map.en.md) — 8 candidates, limits and costs, scope of the next test.
3. [Mirror policy draft](guides/mirror-policy.en.md) — include · exclude rules and approval boundaries.
4. [Scenario comparison table](guides/seamless-scenarios.en.md) — existing evidence for D · E, the unverified scope of C · A, the next test and the screens to capture.
5. [Synthetic test folder](examples/trial-vault/) — 3 synthetic Markdown files marked public.
6. [Preview script](scripts/build_mirror.py) — by default it only reports; a real copy needs an explicit `--apply`.
7. [Example config](scripts/mirror_config.example.yaml) — a YAML-compatible config in JSON syntax that targets only the synthetic test folder.
8. [Synthetic preview report](examples/mirror-report-sample.md) — 1 public file as a candidate to include; 4 personal · internal · unclassified · non-Markdown files excluded.
9. [M4 WorkLog](../vl_worklog/20261105_M4_Muse-My-Workflow.md) — observations from Labs 1 · 2 and the next points to check.

## What I Have Found So Far

- **All 8 candidates** are organized with official documentation and Muse screens, along with the check date (11/5). In the Muse connector list, I checked GitHub · Dropbox · Google Drive directly (not connected).
- **There is no sync feature.** A connector is a connection that looks in when needed. So "the work I did away arrives at the home PC by itself" (S5) is not yet met by any candidate.
- **A mirror copy holding only public-marked files works safely.** In the real vault preview: 3 candidates to include · 55,975 excluded · 0 copied — internal markers 112 · `visibility: internal` 58 were all left out.
- **What I could not check** — whether a connector can be narrowed to one folder · one repo; whether the training off switch, which is not in web Data controls, is somewhere else; a Windows release of Muse desktop.
- The screen capture of the Lab 2 preview is on hold because of a problem with the Windows capture tool.

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

## Navigation

- Previous · [M3 — VibeLearn AI on Muse](../03-VibeLearn-on-Muse/README.en.md)
- Next · M5 — One week of real use and a usage guide ([roadmap](../vl_roadmap/20261018_RoadMap_Muse-My-Workflow.md#m5---1주일-실제-사용과-사용-가이드)) — starts with the combination chosen in M4
