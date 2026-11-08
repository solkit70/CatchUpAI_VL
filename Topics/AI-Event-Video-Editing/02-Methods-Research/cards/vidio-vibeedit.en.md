---
title: "Research Card — Vidio.ai / VibeEdit"
author:
  - "Codex"
created: 2026-10-24 22:47:08
source: "https://www.vidio.ai/guide"
tags:
  - ai-event-video-editing
  - research-card
lang: en
---

## Summary
[한국어](vidio-vibeedit.md)

**Group B · official documentation checked 2026-10-24 · trial status: on 2026-10-25, in a Free account, uploaded a 5-minute copy, gave Korean instructions and output a free preview directly.** This covers VIDIO's VibeEdit, kept separate from other tools with similar names. I confirmed in the official guide the feature of selecting and revising footage by instruction, but the quality of selecting real event scenes and Korean instructions are unverified.

> “Afterwards you keep refining it by chat”
> — VIDIO, [Official guide — VibeEdit](https://www.vidio.ai/guide), checked 2026-10-24

## Features and trial scope

The [official guide](https://www.vidio.ai/guide) describes scene selection, order, target length, music, titles and chat revisions. A free account is a candidate for reviewing a watermarked preview with a short source; whether you can sign up without a card was not checked on the sign-up screen. Paid export was not run in this session.

## Pricing and input limits

I rechecked by switching monthly / yearly myself on the USD screen of the [pricing page](https://www.vidio.ai/pricing). Pro 20 is **monthly billing $10 / yearly billing $96 ($8/month equivalent), 20 credits**, and Business 400 is **monthly billing $50 / yearly billing $480 ($40/month equivalent), 400 credits**. The yearly monthly-equivalent price is not used as the monthly billing price. [Screenshot evidence](../review-followup.en.md#key-figures-rechecked)

| Item | Free | Pro | Business |
|---|---|---|---|
| Single video / total source length | 10 minutes / 10 minutes | 60 minutes / 60 minutes | 2.5 hours / 6 hours |
| Size per file | 1GB | 4GB | 8GB |
| Number of videos | 5 | 20 | 80 |
| Export | 720p · watermark | Up to 1080p | Up to 4K |

The evidence for the limits is the [VibeEdit plan table in the guide](https://www.vidio.ai/guide). A standard AI edit of a 1-hour source is listed as **108 credits**, so the amount included in Pro 20 alone is not enough. This is calculated on the input source length, not on the 3-minute length of the finished piece. Extra credit prices and the cost of repeated revisions need to be checked on the actual display before paying.

## Limits of the Premiere handoff

The guide explains that cuts, original audio, music and description markers are delivered in Final Cut Pro 7 format XML. **Captions, titles, transitions, color, speed and reframing are not recreated, and SRT is not provided either.** Relinking to the source is needed, so it must not be read as moving over all the finished effects. [Official guide — XML timeline section](https://www.vidio.ai/guide)

Free XML appears unsupported on the pricing page, but the guide says it is possible if you have credits. The difference in account and credit conditions is left **unresolved**, and free XML is not guaranteed.

## Follow-up checks

Whether a card is required at sign-up, Korean voice, instructions and captions, and the quality of the 3-minute structure are unverified. If a free trial is possible, start by checking a preview with footage under 10 minutes that can be made public, and keep Premiere XML and paid output as items to verify together with the client.

## Hands-on test follow-up record — 2026-10-25

In a Free account that the user logged into directly, a 5-minute copy was uploaded and an excerpt summary of about 148 seconds was requested in Korean. The first edit finished after using 1 free message, and the free preview file measured 126.912 seconds · 1280×720, falling short of the length target. A full decode of the free output file was normal, and a Korean revision request was actually applied, but the timeline shown in the UI shrank to 1:13 and all PR explanations were removed, so it did not meet the request. Direct listening and evaluation of manual correction remain. XML was shown as Paid plan only in the Export menu of the actual account too. → [Actual test, output and limits](../../04-HandsOn-Highlight/method-B.en.md)
