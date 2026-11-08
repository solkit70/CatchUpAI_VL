---
title: "M5 AI Direction — Applying Titles and Effects to Existing Footage"
author:
  - "Codex"
created: "2026-10-25 07:42:03"
tags:
  - ai-event-video-editing
  - effects
lang: en
---

## Direction Applied and Roles

[한국어](ai-directed-effects.md)

> Add a 5-second intro, lower section titles, and a Q&A transition card, and preserve the original speech.

The line above is the scope of this run as explained to the user. The AI wrote the [reproduction script](render_effects.py), Python/Pillow created the text and shape assets, and FFmpeg did the actual video conversion. This is not automatic scene selection in a video editing program, and it is not a generative model creating new event scenes.

## Edit Design

| Position | Applied | Sound |
|---|---|---|
| Start | 5-second title card, fade in/out | Silent |
| Start of explanation | 4-second lower section title | Original speech |
| Existing join at 62.5 s | 1.5-second Q&A card, fade | Silent |
| Start of Q&A | 4-second lower section title | Original speech |
| End | 3-second closing card, fade | Silent |

The lower titles are "핵심 설명 / PR 리뷰에 Skill 활용하기" (Key explanation / Using Skills for PR review) and "질의응답 / Skill의 범위와 구성" (Q&A / Scope and structure of Skills). They are section titles added by the editor, not captions transcribing the speech. ASR correction, translation, and syncing of speech captions were not part of this practice.

## Direction Improvements from the User Review

The user approved the transition positions, text readability, and the last card. However, the speech is in English while the on-screen titles are in Korean, so from the next request on it is better to specify `speech language`, `on-screen title language`, and `speech caption language / whether needed` separately. For example, write the output language and the caption choice separately, like "Write the on-screen titles in the same language as the English speech, and do not add full speech captions" or "Translate the English speech into Korean captions and also write the section titles in Korean." This rule is an improvement for future production directions; no captions were added to this video. → [User's original review](../../../../../Journal/2026-10-25.md#m5-효과-데모-검토-구술-원문)

The user suggested that flashier, more dynamic special effects could help a highlight. The titles and transition cards applied this time are the first step of a basic setup, and advanced effects will be reviewed in a later scope.

## 2026-10-29 Local Speech Caption Attempt

I extracted 25 seconds of the English speech in the existing demo as WAV and ran it through local Whisper. I did not upload the full source video or audio to any external service. The tiny model recognized most of the sentences as other words, so it could not be used as is. The medium model that was in the cache had better sentence flow and segmentation, but misrecognitions remained in the first phrase, in technical terms like `PR review`, and at sentence endings. Even when compared with the segments in the existing medium transcription JSON of the footage, that cannot be treated as a correct transcript, so this result is an **ASR draft**, not captions for publishing.

What this comparison showed is that a bigger model improved the context in this excerpt, but it did not remove the review work. The 25-second test SRT was kept only in a temporary folder and was not composited into the finished video. This attempt and evaluation met the roadmap item "Try and evaluate adding effects and captions by AI direction." Accurate caption production, translation, and video sync verification remain as a separate task.

## Reproduction and Limits

The source is [M4 local v1](../04-HandsOn-Highlight/method-A.en.md), and the script takes `--source` and `--output`. If the output folder already exists, it stops, and it only reads the source. It does not delete original speech segments or mix in background music or new voice; it inserts a silent card between the two segments at the 62.5-second point.

A local demo that Changsoo Park runs with code can be made, but a GUI manual that the client can edit directly without coding has not been verified yet. I do not judge it to be faster than manual work in CapCut or Premiere based only on render time.
