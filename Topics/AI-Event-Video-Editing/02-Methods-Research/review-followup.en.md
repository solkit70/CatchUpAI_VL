---
title: "M2 Review Follow-up — Price Re-verification and Candidate Scope"
author:
  - "Codex"
created: 2026-10-24 23:11:28
tags:
  - ai-event-video-editing
  - review
lang: en
---

## Scope of the follow-up
[한국어](review-followup.md)

Based on the Claude review the user passed on and the user's approval of the revision plan, I filled gaps in pricing, missing candidates and the reader's point of view. **The screen comparison was done by the AI. It does not replace the user's own check of the screens or a check of actual purchase conditions inside an account.** The client's answers and actual hands-on trials remain unverified.

## OpusClip plan re-verification

I compared the plan cards and the comparison table on the [official pricing page](https://www.opus.pro/pricing) in a real browser. The table columns were Free → Starter → Pro → Business, and the Premiere · Resolve export row was, in order, not included · not included · check · check. The [official FAQ](https://help.opus.pro/docs/article/import-to-adobe-premiere) also says it is Pro only. So in this check **there is no evidence to correct it to Business only, and "included in Pro" stays.** I do not generalize that the review was wrong, and I do not guess the cause of display differences at other times or in other accounts.

By switching the monthly / yearly billing toggle myself, I confirmed for Pro, 1 pack: **$29/month**, and **$174/year, $14.50/month equivalent**. Whether the free Pro trial gives all features of the paid plan, and whether XML is offered in an actual account, are separate things to verify. This result is a check of public information. No payment, login or trial was done.

| Screenshot evidence | What to read |
|---|---|
| [Monthly billing screen](assets/20261024-opus-monthly.png) | Pro $29/month, $29 billed monthly |
| [Yearly billing screen](assets/20261024-opus-yearly.png) | $14.50/month equivalent, $174 billed annually |
| [Bottom of the Pro feature card](assets/20261024-opus-pro-features.png) | Premiere · Resolve export check on the middle Pro card |

For the user's review: on the yearly billing screen, confirm that the title of the middle card is Pro, then compare it with the feature screen at the bottom of the same card. If the actual account screen differs, compare it with this record by date, region and billing cycle, and hold the adoption cost judgment until the conflict is resolved.

## Key figures rechecked

| Item | AI recheck result | Evidence / remaining conditions |
|---|---|---|
| OpusClip Pro | $29/month / $174/year ($14.50/month equivalent), 1 pack | Public screens above. Final price per account and trial features unverified |
| Vidio Pro 20 | $10/month / $96/year ($8/month equivalent), 20 credits | [Monthly billing screen](assets/20261024-vidio-monthly.png) · [yearly billing screen](assets/20261024-vidio-annual.png), USD and the selected credit value |
| Vidio Business 400 | $50/month / $480/year ($40/month equivalent), 400 credits | Same screens. Total including extra credits, reprocessing and tax is separate |
| Vidio standard AI edit | 108 credits for a 1-hour source | [Guide: Editing modes and credits](https://www.vidio.ai/guide). Based on the input source, not the 3-minute result |
| Seedance 2.5 price example | Estimated $1.156 each for 720p · 16:9 · 5 seconds with no video reference | Billing examples in the [official pricing text](https://ai.byteplus.com/ark/region:ap-southeast-1/docs/model-pricing). Not used as a monthly subscription or a quote for the whole job |

For Vidio, I checked by switching monthly / yearly on the [pricing page](https://www.vidio.ai/pricing) with USD and the default credit value selected. The [XML handoff guide](https://www.vidio.ai/guide) says captions, titles, transitions, color, speed and reframing are not recreated, so the constraint in the existing card stays.

I did not mark the numbers in this table as checked by the user directly. In consultation, first explain the conditions on the price table, and compare against the account screen right before actual adoption.

## Check of all M1 candidates

There was no record that other candidates were reviewed and excluded when the first 8 were chosen. So the missing items are stated as **not researched**, and the follow-up classification below was decided at the time of this review follow-up. "On hold" is not a product judgment that features are lacking.

| M1 candidate / method | Current status | Decision this time and reason |
|---|---|---|
| Premiere built-in AI | Research complete | [Card](cards/premiere-native-ai.en.md#summary); checking the existing tool comes first |
| Vidio / VibeEdit | Research complete | [Card](cards/vidio-vibeedit.en.md#summary) |
| OpusClip / ClipAnything | Researched, plan re-verified | [Card](cards/opusclip-clipanything.en.md#summary) |
| Premiere MCP | 1 representative repository researched | [Card](cards/premiere-mcp.en.md#summary). Does not mean all repositories with the same name were verified |
| VEA | Research complete | [Card](cards/memories-vea.en.md#summary) |
| Seedance / Claude call path | Model and connection method researched | [Card](cards/seedance.en.md#summary) · [connection document](claude-chatgpt-plugins.en.md#assessment-by-connection-method). The exact tool the client saw is unverified |
| ChatGPT connection path | Method researched | Same connection document. Not counted again as a separate video editing service |
| FFmpeg + transcript | Research complete | [Card](cards/ffmpeg-transcript.en.md#summary) |
| Remotion | Research complete | [Card](cards/remotion.en.md#summary) |
| CapCut AI | **Card added** | [Card](cards/capcut-ai.en.md#summary). A tool already in use, so check it first |
| After Effects | Not researched in detail; on hold as an M5 comparison target | If there is an intro template already in use, use that first. Not marked as having researched its AI feature support |
| Descript | Not researched; additional research conditional | Raise priority if speech-centered editing is the core need. For now, comparing candidates for building the whole event piece comes first |
| Runway · Kling · Veo | Not researched; on hold | Review when the comparison scope for generative intros is widened. Not confirmed as an alternative for selecting scenes from long events |
| Cutback / Premiere Assistant | Not researched; on hold | Add when needed after comparing with the official Assistant and the representative MCP path. Kept separate from the official Adobe product |
| AutoEdit | Not researched; on hold | Research if removing silences and filler is confirmed as the client's core problem |
| MomentCut | Not researched; on hold | Its official availability, maker and long-term support must be checked first; not included in this priority research |

There are currently **5 groups · 9** in-depth cards, and this does not mean every M1 candidate was researched in depth. Rather than adding more cards, prepare the conditional recommendation and actual hands-on trials first.

## Readers, language and naming

The main reader is a Korean-speaking video professional who is not a developer. The body text and cards stay in Korean, and the English README summarizes status and key results. English translations of all M2 documents are not made in this scope.

New guidance for the client uses 「진행자」 ("the person running the project", i.e. Changsoo Park). Past authors, spoken accounts and WorkLogs keep the original record, and expressions that existed from M1 are not described as if they were newly written in this work. Technical explanations stay in the research cards, and the consultation summary puts things in the words that are needed.

## Review follow-up results

- [x] Compared OpusClip plans and monthly / yearly prices with the source text and public screens
- [x] Rechecked conditions of key figures; saved screenshot evidence for a person to see
- [x] Added the CapCut card and recorded the status of all M1 candidates
- [x] Wrote the one-page summary for the client, the conditional recommendation, and the M3 trial plan
- [x] Applied the second review — anonymized local paths for public use; added cost examples and free / paid conditions to the one-page summary
- [ ] User's own comparison of price screens — not done
- [ ] Verifying edit results with a real account and test footage — not done
