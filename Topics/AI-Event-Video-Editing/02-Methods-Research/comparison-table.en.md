---
title: "M2 Comparison Table — 5 Groups · 9 Candidates"
author:
  - "Codex"
created: 2026-10-24 22:47:08
tags:
  - ai-event-video-editing
  - comparison
lang: en
---

## Summary and scope
[한국어](comparison-table.md)

**2026-10-24 document research · 5 groups · 9 candidates · 0 hands-on trials · client's answers unverified.** After the review I added CapCut and re-verified the key prices against the source text and screenshots. Read this together with the [status of all candidates and the verification record](review-followup.en.md#check-of-all-m1-candidates). Claims of support are kept separate from actual quality, and values I could not confirm from public material are left as unverified. The judgments below are not a final recommendation or hands-on scores.

## Feature comparison

| Group · candidate | Selecting scenes | Assembling | Finishing | Handoff to Premiere | Key constraints |
|---|---|---|---|---|---|
| C · [Premiere built-in AI](cards/premiere-native-ai.en.md#summary) | Visual and script search, beta Assistant assembly | Text-based editing (released) / beta first cut | General editing features | Editable sequence | Version and Assistant access; an exact 3-minute result not verified |
| C · [CapCut AI](cards/capcut-ai.en.md#summary) | Automatic highlights; instruction quality not verified | Clip generation, general editing | Auto captions, etc. | Video output; timeline handoff unverified | Check free AI scope by platform, region and plan, and a landscape 3-minute structure |
| B · [Vidio.ai / VibeEdit](cards/vidio-vibeedit.en.md#summary) | Prompt-based selection | Target length, order, chat revisions | Music, titles, etc. | XML, relinking to source | Not all finishing (captions, transitions, etc.) carries over in XML |
| B · [OpusClip / ClipAnything](cards/opusclip-clipanything.en.md#summary) | Clipping based on visual, audio and emotion cues | Clip generation; building one event piece not verified | Captions, reframing, etc. | Pro XML · SRT | Free trial limits effects; XML length guidance needs checking |
| A · [Premiere MCP](cards/premiere-mcp.en.md#summary) | Needs transcript and scene evidence for the AI to use | Operates supported Premiere actions | Within the range of supported tools | Inside Premiere | Community tool; installation, API support and compatibility not verified |
| B · [Memories.ai VEA](cards/memories-vea.en.md#summary) | Overview: long-video understanding, highlights | Overview: assembly; managed API cannot set length directly | Overview: music, captions | FCP XML in overview; same support in API unverified | Do not confuse the VEA overview, the managed API and a finished web tool |
| D · [Seedance](cards/seedance.en.md#summary) | Selecting segments from hours-long footage unverified | Short video generation, reference editing | Candidate for intro and supporting shots | Output video; XML unverified | Keep generation / reference editing separate from cut editing of recorded footage |
| E · [FFmpeg + transcript](cards/ffmpeg-transcript.en.md#summary) | Separate judgment from transcript and scene notes | Control of specified segments and length | Filters, separate code setup | Video, individual clips; XML needs separate implementation | Scenes without speech cannot be selected from the transcript alone |
| E · [Remotion](cards/remotion.en.md#summary) | Needs separate analysis | Code- and frame-based assembly | Repeated intro, captions, logo | Rendered video; code effects separate | Coding burden; organization / collaboration license conditions |

The link in each row goes to the summary section of the original research card. For detailed evidence, follow the official links in the card body. A is connection methods, B is editing services and systems, C is existing programs, D is generation / reference editing, E is code-based methods. One tool can play several roles, but I counted it under its main group for comparison.

## Cost, free trial, input limits

| Candidate | Cost conditions confirmed | What to check for long source files and free trials |
|---|---|---|
| Premiere | Transcription included in subscription; Assistant uses beta-only credits | Local PC performance, version, beta access, scope of cloud features |
| CapCut | Free basic editing and paid plans. Final price in the account unverified | Check AI allowance, length and export conditions by region, app and feature |
| Vidio | Pro 20: $10/month / $96/year ($8/month equivalent). Business 400: $50/month / $480/year ($40/month equivalent) | Free: 10 minutes total, 1GB. Pro: 60 minutes total, 4GB. Standard AI edit of a 1-hour source: 108 credits |
| OpusClip | Starter $15/month; Pro with XML $29/month / $174/year | Free 60 credits/month; trial has feature limits. Source processing volume and XML length conditions are separate |
| Premiere MCP | Repository shows MIT; Premiere and AI costs separate | PC, client and supported features matter more than a fixed upload amount. Keep free installation separate from free real-world use |
| VEA | Managed Edit Video API shows $0.15/minute | Total including indexing and storage, the length that is billed, maximum file limit and free allowance unverified |
| Seedance | BytePlus example: estimated $1.156 for 720p · 16:9 · 5 seconds with no reference video | Varies by tokens, resolution and reference. Max 30 seconds per generation; free allowance and input limits unverified |
| FFmpeg + transcript | FFmpeg itself is open source; AI and transcription costs separate | Local resources, limits and Korean quality of the chosen API. Keep server API and local transcription conditions separate |
| Remotion | Free License for individuals and companies of 3 people or fewer; collaboration and size conditions separate | Creators $25/month per seat / Automators minimum $100/month. Which form applies needs checking |

Amounts are in USD and are not quotes that include tax, extra services or retry costs. The billing units differ by source, so I do not rank by price. Detailed sources and caveats: [Vidio pricing section](cards/vidio-vibeedit.en.md#pricing-and-input-limits), [OpusClip pricing section](cards/opusclip-clipanything.en.md#pricing-free-trial-processing-volume), [VEA cost section](cards/memories-vea.en.md#cost-limits-korean), [Seedance pricing section](cards/seedance.en.md#pricing-output-handoff), [Remotion license section](cards/remotion.en.md#cost-and-license).

## Korean, data, real verification

| Candidate | Scope of Korean support confirmed | Data path / hands-on record |
|---|---|---|
| Premiere | Transcription supported / visual search English / Assistant optimized for English | Search is local, part of Assistant is cloud / documents only |
| Vidio | Scope for instructions, voice and captions unverified | Upload / documents only |
| OpusClip | Korean video language in beta; Korean instructions not verified | Upload / documents only |
| Premiere MCP | Client understanding and Korean task results are separate | Bridge is local; what is sent to the AI depends on settings / documents only |
| VEA | Managed API recommends English and does not guarantee other languages | Upload, webhook / documents only |
| Seedance | Accuracy of instructions, voice and on-screen text not verified | Sent to the service or API used / documents only |
| CapCut | Quality of instructions and Korean captions not verified | Web uploads; desktop AI processing also needs checking / documents only |
| FFmpeg + transcript | Depends on the chosen transcriber, model and font | Can be local; data is sent when combined with cloud / not tried in this Topic |
| Remotion | Korean fonts, line breaks and actual rendering not verified | Local or the chosen render environment / not tried in this Topic |

Supporting Korean captions does not mean accuracy in Korean scene-selection instructions. Whether the user's source files may be uploaded, which account to use, and whether to look at paid tools too are still unverified. Narrow the conditions after receiving answers to the [M1 questions](../01-Requirements-Map/client-questions.en.md).

## One-line judgment by group

- **A Connection tools**: There is a path to operate Premiere, but the supported API and the evidence for scene selection decide the quality of the work. → [Connection method analysis](claude-chatgpt-plugins.en.md#what-works-and-what-has-no-evidence-yet)
- **B Editing systems**: Vidio, OpusClip and VEA each have parts close to the need, but differ in length, language, effect handoff and total cost. → [Feature comparison](#feature-comparison)
- **C Existing programs**: There is reason to compare the search, transcription and official Assistant beta of Premiere, which the client already uses, first. The client's access conditions are not yet known. → [Premiere card](cards/premiere-native-ai.en.md#follow-up-checks)
- **D Generation / reference editing**: A candidate for intros and supporting shots, kept separate from the feature of selecting real scenes from hours of source footage. → [Seedance correction](cards/seedance.en.md#features-and-correction-of-the-earlier-description)
- **E Code methods**: Possibly an advantage for reproducible length and repeatable templates, but ease of use and maintenance are to be checked by hands-on trial. → [FFmpeg judgment](cards/ffmpeg-transcript.en.md#judgment-for-this-topic) · [Remotion judgment](cards/remotion.en.md#judgment-for-this-topic)

## Conditions to check in M3

The [M3 conditional recommendation](../03-Recommendation/recommendation.en.md) is: check existing Premiere and CapCut → compare Vidio, with OpusClip as an alternative → existing intro template. Final adoption is not decided, and accounts, footage and schedule are kept as not yet decided in the [trial plan](../03-Recommendation/test-plan.en.md).

| Unverified item | Effect on the choice |
|---|---|
| OS, Premiere version, plan, beta access | Whether built-in AI and MCP can be used |
| Source length, cameras, image quality | Input limits, processing cost, XML splitting |
| Delivery aspect ratio, examples of a good finished piece | Whether short-form clips or an event montage is needed |
| Budget, permission for external upload | Whether paid and cloud candidates apply |
| Way of working, willingness to install | Scope of the client using it directly, trying it together, or receiving materials |
