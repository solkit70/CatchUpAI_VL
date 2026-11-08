---
title: "Research Card — Premiere Pro MCP (Community)"
author:
  - "Codex"
created: 2026-10-24 22:52:50
source: "https://github.com/leancoderkavy/premiere-pro-mcp"
tags:
  - ai-event-video-editing
  - research-card
lang: en
---

## Summary
[한국어](premiere-mcp.md)

**Group A · checked 2026-10-24 · documents only / no installation or hands-on trial.** Among several projects with the same name, I researched `leancoderkavy/premiere-pro-mcp`. It is a community project, different from Adobe's official Assistant, and the repository description is not a verification result in the client's actual environment.

> “independent, local-first server for supported workflows”
> — [Project author's README](https://github.com/leancoderkavy/premiere-pro-mcp), checked 2026-10-24

## Features and conditions

| Criterion | What the author's material shows, and remaining conditions |
|---|---|
| Connection | A local MCP server and a Premiere CEP connection panel are installed separately. |
| Editing | Provides tools to read projects and timelines and to operate supported cuts, effects and exports. |
| Automatic judgment | Having the tools is separate from the AI picking good scenes. Evidence such as a transcript or scene descriptions is needed. |
| Adobe AI | The author classifies some Adobe AI tasks, such as starting Speech-to-Text, as user-assisted / not supported. I do not assume it calls every Premiere AI feature directly. |
| Version | The recommended local setup is Premiere, bridge and MCP client on the same PC. The README lists Premiere 2020–2026, but actual compatibility is not verified. |
| Cost | Apart from the MIT license shown in the repository, Premiere and AI client costs apply. I do not assume installing the tool is included in a subscription. |
| Limits · Korean | No fixed upload limit is given. It depends on PC performance, the client model and context, and the quality of Korean commands is unverified. |

The evidence is the [Quick Start · AI feature boundaries · Technical Details in the author's README](https://github.com/leancoderkavy/premiere-pro-mcp). I do not mix in other packages with the same name or their installation methods, and the versions listed as supported are kept as items to check on the client's PC.

## Judgment for this Topic

It has the advantage of keeping an editable timeline inside Premiere, but the burden of installation and troubleshooting is large. This is a document-based inference, and it is kept as a candidate to compare after checking what work the [official Premiere Assistant](premiere-native-ai.en.md#official-ai-assistant-public-beta) falls short on.

If the connection is tested, start with a read-only connection check on a copied project. This document is not an installation manual, and there is no hands-on evidence yet that cuts, effects or exports succeeded with this tool.
