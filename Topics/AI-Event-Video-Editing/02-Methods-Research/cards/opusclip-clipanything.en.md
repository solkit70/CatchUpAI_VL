---
title: "Research Card — OpusClip / ClipAnything"
author:
  - "Codex"
created: 2026-10-24 22:47:08
source: "https://www.opus.pro/clipanything"
tags:
  - ai-event-video-editing
  - research-card
lang: en
---

## Summary
[한국어](opusclip-clipanything.md)

**Group B · official documentation checked 2026-10-24 · trial status: documents only / no hands-on trial.** A candidate that finds segments by prompt and passes them to Premiere. The quality of combining several scenes into one 3-minute event story has not been verified yet.

> “Just type your prompt.”
> — OpusClip, [ClipAnything](https://www.opus.pro/clipanything), checked 2026-10-24

## Features and Korean

[ClipAnything](https://www.opus.pro/clipanything) describes using visual, audio and emotion cues, and says videos with little or no speech are also covered. I confirmed automatic clip generation and natural-language segment instructions, but the ability to accurately pick out a specific person at a real event has not been tried yet. The vendor's promotional accuracy and performance figures are not used as verification scores.

The [supported languages help](https://help.opus.pro/docs/article/video-languages-supported) marks **Korean as beta**. This is guidance on processing Korean video, and it is not evidence that Korean prompts perform equally well.

## Pricing, free trial, processing volume

**Screen re-verification after the review (2026-10-24)**: I compared the plan cards and the 4-column comparison table on the public pricing page in a real browser. Premiere · Resolve export is shown **checked for Pro and Business** and not included for Free and Starter, so "included in Pro" stays. I also confirmed the prices below by switching monthly / yearly. [Screenshots and verification record](../review-followup.en.md#opusclip-plan-re-verification)

| Plan | Official display | Main conditions |
|---|---|---|
| Free | $0 · 60 credits/month | Watermark, editing limits, cannot export after 3 days |
| Starter | Monthly billing $15 · 150 credits/month | Watermark removed. Premiere XML not included |
| Pro | Monthly billing $29 / yearly billing $174 ($14.50/month equivalent) · 300 credits/month | Premiere · Resolve export, several aspect ratios including 16:9 |

Pricing and plan evidence: [official pricing page](https://www.opus.pro/pricing). The [credits help](https://help.opus.pro/docs/article/how-are-credits-consumed) says 1 credit per minute of source, so 3 hours of source is 180 credits. Even if the final result is 3 minutes, the source processing volume is separate.

The [official homepage](https://www.opus.pro/) describes a 7-day trial for new users with 90 minutes of processing, and the pricing page has a "no card required" line. However, according to [features not included in the free trial](https://help.opus.pro/docs/article/features-not-included-free-trial), trial results also have a watermark, and intros, transitions, music and so on are limited. I do not treat the free Pro trial as equal to all features of paid Pro. I did not create an account or start a trial.

## Premiere handoff and length caveats

The [Premiere import FAQ](https://help.opus.pro/docs/article/import-to-adobe-premiere) describes Pro-only delivery of XML, source and SRT. Animated captions are overlays, so they are different from a caption track where the text can be changed freely. To edit them, use the path of importing the SRT separately.

The same FAQ says **XML export has a maximum of 1.5 hours, a recommended maximum for stability**. From the wording alone it is not clear whether this length means the whole source or the exported result, so it is left as unverified. The earlier search figure of "supports 10 hours of source" is not applied as is to this XML condition, and for long event videos, splitting and the target length for XML need to be checked.

## Follow-up checks

1. In a trial without a card, check separately whether ClipAnything, 16:9 and XML are actually offered.
2. Look at selection results for scenes without speech, such as awards, performances and group photos.
3. Record the amount of manual work to build several clips into one piece, Korean caption errors, and XML import results.

This candidate assumes cloud upload, so whether the client's footage may be uploaded stays unverified. No footage was uploaded in this research.
