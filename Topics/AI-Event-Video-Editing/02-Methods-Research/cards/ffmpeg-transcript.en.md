---
title: "Research Card — FFmpeg + Transcript + AI Edit Plan"
author:
  - "Codex"
created: 2026-10-24 22:52:50
source: "https://ffmpeg.org/ffmpeg.html"
tags:
  - ai-event-video-editing
  - research-card
lang: en
---

## Summary
[한국어](ffmpeg-transcript.md)

**Group E · checked 2026-10-24 · documents only / not practiced in this Topic.** This is a combination where an edit plan is made from the transcript and scene notes, and then FFmpeg cuts the segments into a video. The M1 record of past experience with it is not turned into a successful hands-on result for this Topic.

## Roles and limits

| Step | What it does | What to check |
|---|---|---|
| Transcript | Turns speech into text with timestamps | Award moments, performances and facial expressions without speech cannot be found from the transcript alone |
| AI edit plan | Decides which segment of which source to use, in what order | Without watching the video or scene notes, it may guess at the actual scenes |
| FFmpeg | Cuts, joins and encodes specified segments | It is not itself an editing agent that judges natural-language meaning |

The [FFmpeg documentation](https://ffmpeg.org/ffmpeg.html) explains `-ss` seeking and time and length control, and the [official FAQ](https://ffmpeg.org/faq.html) describes the concat methods. Stream copy and re-encoding have different conditions for cut accuracy and compatibility, so a one-line command alone does not guarantee a frame-accurate result.

## Cost, language, input, Premiere

FFmpeg itself is open source, and the [official license explanation](https://ffmpeg.org/legal.html) has LGPL/GPL conditions by build. Uploading the source is not required for local cut editing, but if transcription and AI judgment are handed to the cloud, there is separate cost and data transfer. Instead of a fixed service upload limit, storage space, codecs and processing time need checking.

As a transcription example, [OpenAI File transcription](https://developers.openai.com/api/docs/guides/speech-to-text) describes a 25MB API upload limit and splitting of large files. The API's `whisper-1` is listed as a model scheduled to be retired, so a new manual is not tied to that model. I do not read this API guidance as a limit or retirement of the local open-source Whisper. The transcription model, Korean quality and total cost are chosen and verified separately.

A flow can be designed to import the output video, individual clips and caption files into Premiere, but **this combination by itself does not automatically provide an editable Premiere XML.** Timeline handoff is a separate item to implement and verify.

## Judgment for this Topic

It is useful as a comparison baseline that reproduces specified segments and length, but extra tools are needed for the client to use it repeatedly without code. This is a document-based judgment, and it will be verified in M4 when actual cost and the amount of touch-up are compared with the same source, instructions and segment records.
