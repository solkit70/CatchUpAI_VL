---
title: "M4 Second Method — Vidio Actual Test and Comparison Record"
author:
  - "Codex"
created: "2026-10-25 05:49:13"
tags:
  - ai-event-video-editing
  - hands-on
lang: en
---

## Current Results

[한국어](method-B.md)

The user gave positive feedback on the local summary cut draft and asked to go to the next step. When the scope of the external service test was then confirmed, the user answered **“Only allow uploading the 5-minute test video.”** The allowed scope is limited to uploading a test copy of IMG_5252.MP4 25:00–30:00 to Vidio or OpusClip. It does not extend to the full original, other videos, payment or card registration.

After the earlier failure of the browser-control connection, the user logged in directly. Once the connection was restored, the agent uploaded the allowed 5-minute copy and sent the common Korean instruction. The account screen showed Free, and the file showed All requirements met. Free messages went from 10 before sending to 9 after, and the first edit was completed. The preview was about 2 min 06 s, short of the target length. After the free export, the user told us the download location, so the file was kept and verified. Its actual length is 126.912 s, 1280×720, and it decoded fully without problems. No final judgment on quality or cost ranking has been made yet.

## Common Test Input and Instructions

The test input was prepared as the local `talk-B-sample-25m-30m.mp4`. Its actual length is 300.0327 s and 31,502,623 bytes, and it is a 1280×720 H.264/AAC copy. 00:00 in the sample corresponds to 25:00 in the original, and all comparison times are converted on this basis. Neither the full original nor the summary cut made earlier is used as input to an external service.

> From this 5-minute presentation video, pick the key explanation of using a Skill for PR review and the related question and answer about what scope to build a Skill for, and make them into one summary video. Horizontal 16:9, target length 2 minutes 28 seconds, with ±5 seconds allowed. Keep the relationship between the question and answer and the meaning of the statements, and keep the original time order. Do not create scenes or statements that are not in the original. For this test, do not add an intro, music, transitions or subtitles. Tell me about any requirement you cannot perform. (original prompt in Korean)

This instruction is **wording fixed this time for the comparison hands-on**. The existing local summary cut chose its segments from an earlier, broader request, so it is not yet the result of running the literally same prompt twice. For a strict same-condition comparison, the local selection should also be reviewed again with this wording, and the times of the existing cuts should not be given to the external service as the correct answer. If Korean is not supported, the English wording below is recorded as a separate attempt.

> From this five-minute presentation, select the key explanation of using a Skill for PR reviews and the related question and answer about how narrowly to scope a Skill. Assemble one 16:9 summary, targeting 2 minutes 28 seconds with a tolerance of 5 seconds. Preserve the question-answer relationship, the meaning of the statements, and chronological order. Use only the original footage and speech. Do not add an intro, music, transitions, or captions for this test. Tell me which requirements you cannot perform.

The revision test is standardized as “Shorten the explanation of using it for PR review, and lengthen the question and answer about the scope of a Skill. Keep the total length in the same target range.” The result of the new revision request, the automatic processing time and the human operation time are recorded separately.

## Sample Creation Verification

The full decode check was fine, and the original's size and modification time were kept. Creating and checking the sample took 279.974 s. This does not include reading the original, documentation, or time waiting for browser access. The video and the manifest of commands and measurements were saved locally outside the public Topic in `AI/VideoEditing/20260908-GitHub/comparison/`.

## Rechecking Access Conditions

On 2026-10-25, the [Vidio official pricing page](https://www.vidio.ai/pricing) was checked again for the free Basic plan's VibeEdit, watermark, 1 GB file limit and 10-minute input limit. The [Vidio guide](https://www.vidio.ai/guide) describes a path of editing by instruction and revising by chat. This paragraph is a record of checking public documentation. In the actual test below, Free account access and the free preview export menu were confirmed, but receiving a local output file was not verified here.

The [OpusClip official pricing page](https://www.opus.pro/pricing) mentions a free trial without a card, and a watermark and editing limits on the free plan. So it is kept as an alternative if Vidio cannot be accessed, but whether a trial account supports Korean instructions, a horizontal aspect ratio and assembling into one video must each be checked. It is not recorded as having used a new account, payment or a paid plan.

## Browser Access Attempts

| Path | Observed result | Step that could not be run |
|---|---|---|
| in-app browser | `createBrowserTab` timed out, and the recovery `getState` also timed out | Viewing the page, checking whether login is needed |
| Windows Computer Use | `list_apps` timed out. Retrying, and retrying after resetting the JavaScript session, gave the same error | Choosing the browser window, operating the page, uploading the file |

The table above records the earlier failure. At that time it failed before the control connection, so it was not concluded to be an outage of the site itself or a sign-up block. Later, after the user logged in and the connection was restored, the work resumed with the actual test below.

## Actual Account Access and First Run

The user logged in directly, and the work went on while checking the screen. The actual entry path was **Dashboard → New project under Create → VibeEdit**; VibeEdit was not directly in the left Create submenu. In VibeEdit's Media composer → Add files → Choose Files, the allowed 5-minute copy was selected. Add files first opens an upload panel, so waiting for the operating-system file picker right from that button caused a timeout. Choosing Choose Files in the panel worked normally.

The uploaded file was confirmed as 1 A-roll in Main visuals, 05:00.0, All requirements met. The upload panel showed the Free account's 1 GB limit and, at that time, 3 free processing projects for today. Closing the panel with the X in Media Composer kept the 1 input video, and the common Korean instruction above was entered as is and sent. The free message count changed 10→9, and the screen showed Analyzing your request / Processing 35%. This is an observation that the Korean request was received, not a verification of how accurately the result understood Korean.

Vidio repeated, in Korean, the requirements of 148 s ±5 s, 16:9, keeping the original order, and excluding intro/music/transitions/subtitles, and directed us to run Run task. In Show the plan, we confirmed 1 source, best moments of about 148 s, shooting order, original sound and 16:9, and then ran Run task. Processing went 0%→60%→72%, and it is not judged as meeting the requirements until the result video is verified. Vidio replied that sentences might not be cut at exactly the same points.

No new account was created, and no card registration, payment, YouTube connection or external media search was done. The source of this section is observation of the actual account screen on 2026-10-25, and the final result is updated after processing finished.

## First Result — Length and Selected Content

Run task finished processing, and the first result was opened in Preview. The timeline was shown as 5 groups, about **2 min 06 s**. This is shorter than the target of 148±5 s, so it fails the length criterion. This is shown in the UI. The ffprobe measurement of the later downloaded file is 126.912 s, which is 16.088 s shorter than the allowed lower limit of 143 s.

The Transcript showed 19 of 53 items selected for the video. We confirmed that the explanation of a Skill for PR review and the question and answer about the scope of building a Skill were selected. However, at the end of the selected speech, the start of the next question on a different topic was also included. Also, some humor and definition segments were left out, so context checking and revision are needed. This is an observation from reading the selected transcript and status buttons, and it does not replace an assessment by direct listening.

The Export menu had Free preview export — Low resolution with watermark, and the note stated a 720p limit. Premium export and Download XML (Premiere Pro) were separate, and XML was shown as Paid plan only. Only the free preview was run. The export progress rose to 89%, and then the Export button became active again. The save location was not received from a download event, so the first result was exported for free again, but waiting for the same event timed out. On the retry, progress of 21% was seen, and then repeated runs were stopped. While trying to detect the download event, the browser-control connection timed out again, so at that time the local save could not be confirmed. Later the user pointed to the actual downloaded file, confirming the save succeeded, so this is not judged as a failure of the service to create output or a download failure. Paid output and XML were not run.

## Download Check and Revision Request Test

The user told us where the actual downloaded file was, and the first result was kept separately as `vidio-talk-B-v1.mp4`. It is 41,182,201 bytes, and the full decode check found no errors. The container length is 126.912 s, video 126.860067 s and audio 126.912 s. The video is 1280×720 H.264 and the audio is 48 kHz stereo AAC. Four sample frames at the start, middle and end were also checked. Direct listening and verification of the meaning of the statements were not completed.

The following Korean wording was sent, adding the first result's measurements and the problems found to the common revision request. Unlike simply running the common wording, this is classed as **a combined revision test that asked at once for length correction, a change in Q&A share, and removal of the incomplete next question**. Since the amount of related Q&A in the original is limited, we also watch whether the requirements can be met together and whether it says so when they cannot.

> Shorten the explanation of using it for PR review, and lengthen the question and answer about the scope of a Skill. Keep the total length in the same target range. The first result was actually 126.912 s, short of the requested 148 s ±5 s. Please fit the revision within 143–153 s. The start of the separate open source/security question placed at the end is cut off without an answer, so please exclude it. Keep the related questions and answers so the sentences are complete, and keep the original order. Keep 16:9 and the original sound, and do not add an intro, music, transitions or subtitles. If you cannot meet these conditions together, tell me what is not possible.

The user said they had done a Usage Reset, but this was not interpreted as to its target or as a reset of Vidio usage. Before the revision, the actual Vidio screen showed 9 free messages. After keeping the first result, the revision request was sent in the chat input of the same project. The follow-up reply explained that it had shortened the PR explanation and added Q&A to match the length, but the actual applied result was different, as below.

## Revision Result — Mismatch Between the Explanation and the Actual Timeline

Sending the revision request reduced free messages 9→8. Vidio explained in Korean that it had removed the PR explanation, added Q&A, removed the incomplete next question and adjusted to 143–153 s, and offered an Apply changes button. After applying, the timeline in Preview showed **1 min 13 s**, 2 groups. This is a value shown in the UI, not one measured from a downloaded revision file.

The Transcript selection fell from 19/53 to 12/53. All 6 PR review explanation items and the 1 next-question start from the first result were removed, and the 12 related Q&A items were kept. Items left out earlier, such as the RACI question and definition, were still shown as Add to video, so no clips were confirmed as actually added. So in this observation, instead of keeping the PR explanation short, it was removed entirely, and the absolute amount of Q&A did not increase. The length match and clip additions claimed in the explanation are kept separate from the actual state.

| Result | Length | How checked | Observation |
|---|---|---|---|
| Local baseline | 147.714 s | Measured from the file, full decode | Meets target length, positive user feedback |
| Vidio v1 | 126.912 s | Measured from the downloaded file, full decode | Related explanation and Q&A selected, part of the next question included, short of length |
| Vidio revision v2 | about 73 s | Service UI, selected transcript | PR explanation all removed, 12 Q&A items kept, nothing added, short of length |
| Vidio manual v3 | 2:30 shown in the UI | 12 added, Saved shown | Explanation and Q&A context restored, next question excluded. User preview assessment good. Local output verification not done |

Whether the conditions of the combined revision request were possible together, given the amount in the original, needs a separate review. However, Vidio explaining that it had met the goal instead of saying which conditions were impossible, and then actually showing 1:13, is a directly observed mismatch. This one sample is not generalized to the service's overall performance. In this work, meeting the requirements could not be judged from the natural-language reply alone.

At that time the revision was kept so the failed state could be checked, and Undo was not pressed. Later, while keeping the failure screen, the work went on to manual correction v3 below. The first result file was kept separately locally. The revision screen was saved outside the public Topic as `vidio-revision-v2.png`. This automatic revision step and the later manual correction are kept separate. The actual video and footage of people are not attached to public documents.

## User Comparison Viewing Results — 2026-10-25

The user watched both the local summary cut and Vidio v1, and assessed them as similar in that both picked the key parts of the lecture and Q&A. The difference showed at the ending. The user pointed out that in Vidio v1, after the related Q&A ends, a bit of a second Q&A appears, so it does not end cleanly. For that reason, **for this sample the user slightly preferred the local summary cut**. → [[Journal/2026-10-25#AI 행사 영상 편집 비교 평가 (구술 원문)|Original of the user's comparison assessment]]

This assessment is evidence that **the completeness of statements and Q&A and the ending cut**, rather than a large difference in key content selection, affected the preference. The strength of the preference is not expanded into a strong ranking or a numeric score. It is not treated as having verified meaning distortion in every sentence, subtitles or audio sync. Vidio revision v2 was not part of this user comparison.

## Manual Correction v3 — Restoring 12 Items from Transcript

The user opened the Transcript tab and asked the agent to operate it directly. Starting from the 12 selected items of automatic revision v2, Add to video was clicked 12 times to restore 9 PR review explanation items and 3 Q&A items for the RACI question and definition. The start times within the sample are below; add 25 minutes for the original time.

| Restored items | Start times within the sample |
|---|---|
| 9 PR explanation and connecting-context items | 0:21, 0:30, 0:34, 0:45, 0:48, 0:53, 0:57, 1:01, 1:11 |
| 3 RACI question and definition items | 3:37, 3:41, 3:46 |

0:45 and 0:57 were marked No speech by the service, but they were included because they are part of the continuous stretch that restores the original flow of the explanation. This label was not treated as the correct answer for whether there is speech, and the detailed audio boundaries will be checked by later listening. The unrelated next question (after 4:20) was not added.

The selection changed 12/53→24/53, and the length shown in the UI changed 1:13→1:45→2:16→**2:30**. The Timeline showed two groups, **explanation 0:00–1:02 + Q&A 1:02–2:30**, and Saved was confirmed. 150 s shown in the UI falls within the target range of 143–153 s, but measurement of an output file and a check for natural cuts are separate.

From the first addition to the last took **48.216 s**. This is the elapsed time of 12 UI operations that the agent made through a browser API. It excludes prior reading, selection decisions, later playback checks, documentation and export. So it is not used as a measure of a person's manual editing time or a typical user's skill. Only per-sentence Add to video was used, with no dragging or code rendering, and the remaining AI chat messages stayed at 8.

The automatic revision failure (v2) is kept in screens and records, and the current project was saved in the manual correction v3 state. The result of the manual correction is not counted as an AI automatic revision success. The screen, selection log and time were saved as vidio-manual-v3.png and vidio-manual-v3.json in the local comparison folder. A free 720p watermarked export was run once, and after the progress display ended, Export became active again. However, no new vidio-output file was found in Downloads, so it is not treated as a successful local file save. The same export was not repeated, and the current project's Saved and 2:30-in-UI state was kept. The actual file length and listening verification are follow-up items.

## User Review of Manual Correction v3 and Interpreting the Download

The user assessed the manual correction as “I think the video editing came out well.” So the user's preview review of v3 is recorded as done, but this is not extended to detailed technical checks, receiving the local file, or the full Topic self-assessment. → [[Journal/2026-10-25#Vidio 수동 보정본 검토와 다운로드 추정 (구술 원문)|Original of the user's assessment of the manual correction]]

The user guessed that the download problem might be a free plan limit. The attached screen separates Free preview export (low resolution, watermark), Premium export (high resolution) and XML (Paid plan only), and a separate warning says preview streaming is slow. This warning alone cannot be read as meaning downloads are blocked. Also, the earlier v1 free output file was actually downloaded, kept and verified. So the current conclusion is **v3 local save unverified, cause undetermined**, and it is not recorded that all downloads on the free plan are impossible.

## Comparison Table — Only Items With Results

| Item | A: transcript reading + FFmpeg | B: external AI editing service |
|---|---|---|
| Status | Local excerpt summary cut draft made, positive user feedback | First file measured, user comparison viewing, automatic revision failed, manual correction 2:30 in UI |
| Input scope | Two segments within original 25:00–30:00 | One upload of the same 5-minute test copy |
| Length | 147.714 s | Measured 126.912 s — short of target |
| Resolution | 1280×720 | Measured 1280×720, H.264/AAC stereo |
| Segment selection | AI read the existing ASR and set the segments | 19 of 53 transcript items selected, part of the next question included |
| Question-answer preservation | Slightly preferred after user comparison viewing for ending completeness. No score measured | User comparison viewing: key selection similar, but the ending is less clean because of part of the next Q&A |
| Processing time | Render and decode check 65.542 s. Selection and review time excluded | Not measured |
| Revision by extra instruction | Not re-run in this session | Combined revision request run, 1 free message used. 1:13 in UI, PR explanation all removed, short of target |
| Cost and watermark | No new payment or watermark in this run | Free shown, 1 free message used, free output noted as 720p with watermark. User's downloaded file verified |
| Premiere handoff | Unverified | XML shown as Paid plan only on the actual account screen. Import unverified |

This table is a first-round record comparing local measurements with Vidio UI observations. The user comparison viewing is done. The user's preview assessment of the corrected version was confirmed as good, but a strict re-check running the identical prompt again was not done. A file check of the corrected version remains, so this is not judged as a finished performance comparison table. The two hands-on paths from M3 are confirmed as the local method and Vidio Free, and the overall M4 DoD stays incomplete.

## Order to Resume

1. User comparison viewing done: key selection was similar, and the user slightly preferred the local summary cut for its clean ending. The ending cut is assessed on this basis.
2. The user's review of manual correction v3 was confirmed as good. Whether the local file was saved and the cause of the download problem remain separately unverified. The 12 additions and 48.216 s are a record of the agent's UI operations and are not counted as human working time.
3. One test on the same sample is kept separate from the tool's full features, and the conditional recommendation and manual will be updated. Paid output, XML, Korean speech and long originals are separately unverified.

→ **Local baseline result**: [Method A — Talk B summary cut draft](method-A.en.md#2026-10-25-talk-b-summary-cut-draft)
