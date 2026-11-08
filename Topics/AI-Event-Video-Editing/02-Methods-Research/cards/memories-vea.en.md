---
title: "Research Card — Memories.ai VEA / Edit Video"
author:
  - "Codex"
created: 2026-10-24 22:52:50
source: "https://docs.memories.ai/visual-agents/video-editing-agent"
tags:
  - ai-event-video-editing
  - research-card
lang: en
---

## Summary
[한국어](memories-vea.md)

**Group B · checked 2026-10-24 · documents only / no account or paid API trial.** The VEA overview and the managed Edit Video API are kept separate. The overview says it understands long videos and builds highlights, but an exact 3-minute length and Premiere handoff have not been verified on one path.

> “it cannot be manually specified.”
> — [Output length guidance in the Edit Video API](https://docs.memories.ai/visual-agents/video-edit), checked 2026-10-24

## Features and the boundaries between different docs

The [VEA overview](https://docs.memories.ai/visual-agents/video-editing-agent) describes indexing, prompt-based highlight scripts, clip assembly, music, captions, MP4 and Final Cut Pro XML. The example uses a local service address, so I do not conclude from this overview alone that a finished web editor is ready to use.

The [Edit Video API](https://docs.memories.ai/visual-agents/video-edit) takes several uploaded assets, landscape or portrait output, and instructions of up to 500 characters, and recommends English. **The output length is decided by the AI and cannot be set manually**, and a webhook setup is needed to receive the asynchronous result. The response example is an MP4 asset, and whether the overview's XML feature is offered the same way in this API is unverified.

## Cost, limits, Korean

| Item | Result checked |
|---|---|
| Editing fee | $0.15/minute shown in the API documentation and the [pricing page](https://memories.ai/pricing) |
| Total cost | Indexing, storage, transcription and editing are separate items. Which length the per-minute editing fee applies to, and the overall total, are unverified |
| Free trial | Free allowance of the editing API and whether a card is needed are unverified |
| Input limits | Could not determine maximum video length or file size per account from these two editing documents |
| Korean | English recommended. States that other instruction languages are not guaranteed; Korean transcription and caption quality unverified |
| Data | Cloud API path using asset upload and asynchronous processing |

## Judgment for this Topic

The editing goal is close, but exact length, XML handoff and developer setup need further checking. Based on the documents, it is a comparison candidate that needs developer help, and I do not conclude that a web manual the client can follow right away can be provided.

Follow-up checks are: the relationship between the API and the full VEA pipeline, the format in which XML opens in Premiere, how to build 3 minutes, and total cost and file limits. I do not calculate the total cost for several hours of source from the price figure alone.
