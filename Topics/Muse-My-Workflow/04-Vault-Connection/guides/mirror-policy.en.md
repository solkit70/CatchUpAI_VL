---
title: "M4 Mirror Copy Include · Exclude Rules Draft"
author:
  - Codex
created: 2026-11-05 07:13:00
tags:
  - muse-my-workflow
  - mirror-policy
lang: en
---

## Purpose and Boundaries

[한국어](mirror-policy.md)

These rules are a draft for keeping the original vault safe and exporting only selected Markdown material to a separate mirror copy. The current default setting is preview. This document and the example config do not copy real vault material or connect to Muse · cloud storage.

## Include Rules

- Only files in the source root set by the user, and in the explicit include paths inside it, are treated as candidates.
- Only files with the `.md` extension and within the set size limit are treated as candidates.
- By default, only files whose YAML `visibility` value is `public` are included. `personal` files are excluded until approval and a config change.
- Files are copied to a separate destination, keeping their relative path from the source.

## Always Exclude

- Files with `visibility: internal`, or with a `🔒 내부 자료` mark in the body
- Files with no classification marker or that cannot be read, `personal` material, and paths the user did not put on the allow list
- Files under path components excluded in the config, formats other than Markdown, files over the size limit, and symbolic links
- The destination folder is not placed inside the source root. If a file with the same path already exists at the destination, it is not overwritten.

## Run Steps

1. The preview reports the candidates and the reasons for exclusion, using only relative paths. Source files are not changed.
2. A person reviews the report. If a file with an internal marker is among the candidates to include, or there is a classification that cannot be explained, the run stops.
3. Copy with `--apply` only after the user approves the mirror copy scope, the destination, and the data levels to include. A new storage connection · upload is checked separately from this approval.
4. After the run, check the include · exclude counts and the destination files, and do not overwrite results onto the mirror copy.

## Items Waiting for Approval

This draft is not a final policy. The real source path · include paths · destination · allowed data levels have not been decided. The synthetic test currently planned includes only `public` material. The real vault preview and the real copy come after a later review and separate approval.

## Links

- [Options map](solution-map.en.md#proposed-candidates-to-test)
- [Lab 2 WorkLog](../../vl_worklog/20261105_M4_Muse-My-Workflow.md#실습-2-초안)
