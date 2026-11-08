---
title: "M3 Trial Plan — Comparing with the Same Source and Instructions"
author:
  - "Codex"
created: 2026-10-24 23:13:03
tags:
  - ai-event-video-editing
  - test-plan
lang: en
---

## Purpose and Current Status
[한국어](test-plan.md)

Using the continuous talk footage the user specified, we compare finding talk boundaries and the actual editing time. We chose the source set and the first 5-minute test section, checked them against the existing English transcript · sample frames, and generated [7 local splitting drafts](../04-HandsOn-Highlight/method-A.en.md). On 2026-10-25, the user allowed uploading only the specified 5-minute sample to Vidio or OpusClip. After that, that copy was uploaded to Vidio Free, and a first edit and a revision request were run with Korean instructions. The v1 file was measured at 126.912 seconds · 1280×720, and the revised v2 was 1:13 in the UI, short of the target. Signing up for new services · uploading the full source · listening review of the full source were not done. A short 74 seconds of audio around two boundaries was additionally checked with a cached local Whisper medium. M3 is 6/7 because access to the two trial methods is unverified, and it is not fully complete.

## Test Preparation Status

| Item | Status · decision criteria |
|---|---|
| Video | 5 files of the 2026-09-08 GitHub event footage specified by the user. Source set from the list below chosen; first test section chosen as IMG_5252.MP4 25:00–30:00 |
| Allowed scope | User approval on 2026-10-25: only a 5-minute copy of IMG_5252.MP4 25:00–30:00 may be uploaded to Vidio or OpusClip. The full source · other videos are not allowed |
| Short test clip | IMG_5252.MP4 25:00–30:00. Includes 27:32, a candidate for the talk → questions transition. Kept separate from a speaker-change test |
| Long source verification | After the short test, expand to the 5 files totaling about 2 hours 1 minute. Check recording order · duplicates · gaps, then split by talk |
| Work baseline | Manual editing baseline time or recent work records unverified. If none, edit the same section manually to compare |
| Accounts · apps | Premiere · CapCut versions · access to paid features unverified; Vidio · OpusClip free sign-up · features unverified |
| Evaluator · schedule | Changsoo Park does the first pass, the client confirms result preference. Actual schedule not decided |

The user explained that several talks at one event were filmed continuously and that the start · end of each talk is not clear. They specified this video for re-editing each talk or for the original goal of a 1–3 minute summary. Only the specified 5-minute copy was allowed for outside service tests, and upload of the rest of the source is unverified. Follow the [second method's preparation and access record](../04-HandsOn-Highlight/method-B.en.md). Public documents do not record absolute paths that include the user name.

## Specified Source and Priority Practice

Below are the results of a local ffprobe query on 2026-10-24. The file name order is a list for checking only, not confirmed as the actual recording order · talk order. All files have audio and a 1280×720 video stream, and the screen orientation has not been checked yet.

| File | Length (rounded) | Size (decimal GB) |
|---|---|---|
| IMG_5249.MP4 | 5 min 20 sec | 0.144 |
| IMG_5250.MP4 | 22 min 47 sec | 0.610 |
| IMG_5251.MP4 | 22 sec | 0.010 |
| IMG_5252.MP4 | 37 min 03 sec | 0.993 |
| IMG_5253.MP4 | 55 min 38 sec | 1.492 |

Total 7,269.29 seconds (about 2 hours 1 minute 9 seconds), 3.249GB. The event information in the accompanying info.txt is used only as supporting material for checking the talk order, and we do not assume it matches the actual footage.

1. **Talk section table first:** Check the start and end of each file and transition candidates, and find each talk's start and end by looking at introductions · speaker changes · slides · applause together. Do not confirm a talk change from silence or a screen change alone.
2. **Split by talk:** In the section table, record the source file name · start/end within the file · evidence for the speaker/topic · confidence · items needing checks. If one talk spans several files, group them as linked candidates and mark duplicates · gaps. If the name is unknown, use Talk A/B, and also record whether Q&A is included.
3. **Summary comes later:** After reviewing the section table, make a 1–3 minute summary of one talk or the whole event. Keep the full video of each talk and the summary as separate deliverables.

The first deliverable puts a reviewable talk section table ahead of a playable final video. The source is preserved, split files are output separately, and the local output location is decided before actual video production.

## Tentative Test Paths

| Path | What to check first | Conditions to proceed · results to keep separate |
|---|---|---|
| A. Premiere / CapCut | Check access to search · highlights · captions in the environment already in use | Changsoo Park does not try paid features himself. Evaluate only when we can look together on the client's screen |
| B. Vidio preview | Source of 10 minutes or less, check free features without a card | Stop if card registration · payment is required. Record free preview and XML · final output separately |
| C. OpusClip alternative | Check testing without a card and the needed aspect ratio · instruction features | Substitute when B does not fit or a clip comparison is needed. Do not guess the free scope |

This table is a tentative list before checking accounts · source. Start the M4 comparison after deciding two paths that are actually accessible for free, and if conditions do not fit, adjust the plan without a new payment.

## Instruction for Splitting Talks

> This is source footage where several talks were filmed continuously. First, find candidates for the start and end of each talk and present them in a table with the source file name and the time within the file. Do not assume that one file is one talk. Mark cases where a talk continues across files or where recording is missing. Write the evidence based on introductions, what is said, and changes in speaker and slides, and leave unclear boundaries and speaker names as unverified. Do not arbitrarily delete key remarks or Q&A.

In the splitting evaluation, record gaps · duplicates · cuts in the middle of a sentence · Q&A linkage · time to fix boundaries, and the boundaries confirmed by a person. Distinguish candidates set from the transcript alone from boundaries confirmed by picture · audio, and record the test as unsupported for tools without a splitting feature.

## Common Instruction for Summaries

The text below is a **draft for testing**, not the client's final delivery requirement. Check that the remarks · scenes actually exist in the source, and change any missing items the same way for all tools.

> Using only scenes actually filmed in this event footage, make a landscape 16:9 highlight of 1–3 minutes. Include key remarks, the event atmosphere, awards or the main program, and the closing. Reduce long silences and repeated scenes, and do not change the meaning of key remarks. Do not generate new event scenes. Tell me about any tasks you do not support.

Enter the Korean instruction first, and if it is not supported, run an English translation with the same meaning separately. Do not count results from the translated path as a Korean-instruction success. For tools that only provide search, split the same request into search terms · selection steps, and record the automatic processing steps and the person's operating time separately.

The revision test is unified into one request: "Shorten the speech parts and lengthen the main program scenes." Finishing is left out at first so scene selection can be compared, and then evaluated separately under the same logo · event name · music conditions.

## Evaluation Sheet and Success Criteria

Below are comparison criteria proposed by Changsoo Park, not experiment results. Once the source and the client's delivery example are checked, adjust the criteria and apply them equally to all paths.

| Evaluation item | Value to record | Proposed criterion |
|---|---|---|
| Following instructions | Requested parts that were met and those that were missing | Check that it does not leave out required scenes that actually exist |
| Length · aspect ratio | Length in seconds · ratio | Before comparing, set the same target length within 60–180 seconds, and record against ±5 seconds · 16:9 and the manual work to adjust |
| Scene accuracy | Source file · section · reason for selection | A person checks the fit of speech scenes and scenes without speech separately |
| Remarks · captions | Edits that changed the meaning · name errors · number of fixes | Meaning distortion does not pass before it is fixed |
| Time | Preparation · upload · waiting for processing · revision · finishing time | Compare active working time and total elapsed time separately |
| Revisability | First result and result after revision · number of extra instructions | Check whether it reflects the same revision request |
| Premiere handoff | Which of cuts · music · captions · transitions are kept/missing | Include the time to rebuild what is missing |
| Cost · output | Usage · payment terms · quality · watermark | Record the values actually shown. Do not judge it deliverable from the free preview alone |

## Intro Comparison — M5 Preparation

The baseline is the time to swap the event name · date · logo in existing After Effects · CapCut templates. If a repeated template is needed, compare with a 5–10 second Remotion intro, and test generative intros separately when the purpose · cost · labeling terms are decided. This work is not actual production included in writing this plan.

## Records and Stop Criteria

In actual tests, record the source · version · plan · instruction · usage · result files so they can be reproduced. Videos whose client information or permission to use is not confirmed are not saved in the public Topic folder. If outside upload is not allowed or a paid feature is required, put that path on hold and record that point as a result.
