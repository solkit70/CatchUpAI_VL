---
title: "M5 Intro — Verification Boundary Between Code Template and Generative"
author:
  - "Codex"
created: "2026-10-25 07:42:03"
tags:
  - ai-event-video-editing
  - effects
lang: en
---

## Practice Prompt

[한국어](intro-template-vs-generative.md)

I made a generative result under the same tech community event intro conditions. So it could be compared with the existing code-based title card, I did not make up a new event name or logo, and I asked for empty space in the center so a title could be added in post-editing.

> Create a 5-second widescreen 16:9 opening for a technology community event. Dark navy background, teal light trails and subtle geometric particles moving forward, clean cinematic motion, professional but warm. No people, no logos, no readable text, no music, no voiceover. Keep the center uncluttered for a title to be added later.

## Actual Run Results

| Path | Status this time | Observations and limits |
|---|---|---|
| Code-based title template | Made and rendered locally | Python placed the text and shapes, and FFmpeg assembled them into video. It is a neutral title card that does not settle a new event name or speaker name. → [Source excerpt topic](../04-HandsOn-Highlight/method-A.en.md) |
| CapCut template `INTRODUCTION 16:9` | Specs checked, failed to enter the editor | The detail page showed 16:9, 3 clips, 8 seconds, 624.61K uses. I clicked `Use this template` and the editor opened, but CapCut showed `Network error. Check your internet connection and try again.` Even after refreshing inside the editor and refreshing the whole page, the edit assets stayed in a loading state. I could not replace the template content or render it. |
| Generative intro — CapCut Seedance 2.0 Mini | Generated, MP4 downloaded, basic file check done | The output is 5.062 seconds, 1280×720, 24fps H.264 and AAC 44.1kHz stereo. Across all frames, an unrequested `Penhin` text in the center and an `Ai` mark in the top left were found, so it did not meet the no-text and empty-center request. There is an audio stream, but I did not listen to it to identify the content. |

## Limited Comparison

The generative result was actually made, but the CapCut template result was not, so the quality, time, and cost comparison of the two results (template and generative) that the roadmap requires is not yet possible. The template specs and the observations of the AI-generated result are recorded in the comparison table for reference, but template editing time, template cost, and final render quality are left as unverified. The Seedance generation screen said 60 credits would be deducted, and no separate paid trial or payment was started.

I entered only a text prompt and did not upload any user video, image, or audio. I did not run `Add text overlay`, a follow-up edit CapCut suggested, but the unintended `Penhin` text appeared in the generated result itself, so it cannot be called a clean background without a title. I confirmed that even when the on-screen generation description says it was made as requested, you still need to play and review the whole clip. This result also does not guarantee the accuracy of an event name or logo, or rights for commercial use.

## 2026-10-29 Download and Full-Frame Check

In AI Creator, when I collapsed the chat panel and selected the generated video card, a download arrow appeared over the video. I clicked it and downloaded `Video 1.mp4`. The original download is kept in a local working folder outside the public Topic. The file is 2,015,277 bytes, with a total length of 5.062 seconds, video 1280×720 at 24fps H.264, and audio AAC 44.1kHz stereo. An FFmpeg full decode check found no errors. The preview DOM showed 854×480 and about 5.125 seconds, so I do not record the preview specs as the download output specs.

Looking at one representative frame per second, there was generated text that reads as `Penhin` in the center of the middle section, and an `Ai` mark was visible in the top left. So the prompt's "No readable text" and empty-center conditions failed. The audio stream is not silent, but I did not listen to the actual content, so whether it is music or voice is unverified. This result is a draft for review before deciding whether to edit or regenerate, and no additional credits were used and no payment was made. The CapCut template still did not render, so the DoD for comparing the two results is not complete.

So the M5 DoD "Compare 2 intros (template and generative)" is not complete. Next, once the editor network problem is resolved, I will actually render the CapCut template under the same conditions and evaluate the two results side by side.

## 2026-10-29 Official Documentation

CapCut's official Intro Creator guides you to pick an intro template and add your video and branding. The template detail I viewed this time was linked from [CapCut Introduction Templates](https://www.capcut.com/template/social/introduction). The separate product page is [CapCut Intro Creator](https://www.capcut.com/create/intro-maker).

ByteDance Seed's 2026-07-31 announcement introduces the multi-reference and editing features of Seedance 2.5. This CapCut practice result was generated not with Seedance 2.5 but with **Seedance 2.0 Mini**, which was selected in the editor. → [Seedance 2.5 official announcement](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)

## Visual and Audio Materials Used

This generation did not use any external images, music, or original footage. The existing code template used the locally installed Malgun Gothic font and code-generated graphics, and the font file itself is not distributed. This is not recorded as a legal judgment that verified the usage rights of all assets, including the original footage.
