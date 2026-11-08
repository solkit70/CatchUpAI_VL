---
title: "Research Card — Seedance: Separating Generation / Reference Editing from Event Highlights"
author:
  - "Codex"
created: 2026-10-24 22:52:50
source: "https://seed.bytedance.com/en/seedance2_5"
tags:
  - ai-event-video-editing
  - research-card
lang: en
---

## Summary
[한국어](seedance.md)

**Group D · checked 2026-10-24 · documents only / no direct generation or paid API trial.** This research is based on Seedance 2.5 as confirmed on the official page this time. Whether the "시덴스" (Seedance) the client mentioned means this model, version or service is still unverified.

> “Smarter Reference and Editing Capabilites”
> — [ByteDance Seedance official page](https://seed.bytedance.com/en/seedance2_5), spelling as in the original, checked 2026-10-24

## Features and correction of the earlier description

The official page describes generating up to 30 seconds at a time and editing based on a reference video. So the flat statement written in M1, **"it is generative, so it cannot edit recorded footage," is corrected.** However, an event editing feature that searches hours of footage, picks real scenes and assembles them into 3 minutes was not confirmed in this material. [Official model description](https://seed.bytedance.com/en/seedance2_5)

In this Topic it is classified as a candidate for intros, short supporting shots and reference editing. Cut editing that selects and keeps real event footage is kept separate from making generated or altered scenes, and I do not recommend it as a replacement for automatic editing of long videos.

## Pricing, output, handoff

| Item | Result checked in official documentation |
|---|---|
| Price example | Estimated $1.156 each for a 16:9 · 720p · 5-second generation with no video reference. Not a monthly subscription price |
| Billing | Token-based. Varies with resolution, source reference video, generation length and so on |
| Length | Max 30 seconds per generation on the ByteDance model page |
| Free trial | Free allowance in the client's region and account, and whether a card is needed, unverified |
| Korean | Accuracy of instructions, voice and on-screen text not verified |
| Premiere | A path of importing the video file is expected, but timeline XML and handoff of editable effects are unverified |

Price evidence: [Seedance 2.5 example in the BytePlus official pricing documentation](https://ai.byteplus.com/ark/region:ap-southeast-1/docs/model-pricing). API cost is different from an external service subscription, and the actual cost only comes out when repeated generations and discarded attempts are taken into account. Input file limits, commercial use and content-specific conditions are checked separately on the service that will be used.

**Rechecked after the review (2026-10-24)**: I compared the $1.156 example again against the "Input without video," "720p," "16:9," "5 seconds" row in the official pricing text. The user's own check and verification against an actual API bill have not been done yet. [Key figures verification record](../review-followup.en.md#key-figures-rechecked)

## Follow-up checks

After confirming the exact name and address of the tool the client saw, research that service's conditions. If an intro is needed, compare it with putting the event name, date and logo in through [a template such as Remotion](remotion.en.md#judgment-for-this-topic), and do not assume that text inside a generated video will come out accurately.
