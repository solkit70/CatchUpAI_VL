---
title: "M4 Local Talk Splitting — Segment Table and Review Edits"
author:
  - "Codex"
created: "2026-10-24 23:43:17"
tags:
  - ai-event-video-editing
  - hands-on
lang: en
---

## First-Round Results of Local Talk Splitting

[한국어](method-A.md)

**Status:** The AI compared the existing transcripts with sample frames and made seven review files with local FFmpeg. This is separate from testing an external AI service, hands-on work by the user, a full listening check, or final delivery verification. The boundaries chosen this time are not the output of an automatic speaker-separation model. They are editing judgments based on the AI's reading of the transcript content and comparison with the frames.

The user allowed the original footage, in which several talks at one event were filmed back to back, to be re-edited per talk or summarized into 1 to 3 minutes. The first round of talk splitting focused on dividing the segments. On 2026-10-25, after the user finished reviewing the four review clips, an excerpt summary cut on a specific theme from Talk B was added. The originals, the actual video and footage of people are kept locally, outside the public Topic. Only the file names and times needed to reproduce the work are recorded here.

## Input and How It Was Checked

There are 5 MP4 files, 7,269.29 s in total. The English transcripts and timing data in the existing `transcripts_medium/*.json` in the same folder were reused. No new transcription API or external upload was used. For the extra boundary check, the local Whisper medium model that was already installed and cached was used. This work did not verify the model or the full creation process of the transcripts. The date metadata did not match the order of the file names, so it was not used to settle the filming time or gaps between files.

Self-introductions, talk endings and switches to questions were read in the existing transcripts. Sample frames at the start and end of each file and every few minutes were checked. The opening frames of each file support the order Talk A → B → C. However, gaps or overlaps between files and the audio continuity remain unverified until a full listen. A segment where a different presenter answers during questions was not assumed to be a new, separate talk.

## Talk Segment Table

Times are within each original file, and the end time is exclusive. End times with decimals are ffprobe durations and do not mark the exact last syllable of the talk. A/B/C are used instead of the presenters' real names.

| Output | Original | Start → End | Division and basis for judgment | Remaining check |
|---|---|---|---|---|
| 01-opening-draft.mp4 | IMG_5249.MP4 | 00:00.000 → 05:19.927 | A's greeting and event guidance, then a switch to the main talk slides | Whether the audio continues into the main talk, and any overlap |
| 02-talk-A-draft.mp4 | IMG_5250.MP4 | 00:00.000 → 22:46.933 | Same presenter, main talk slides, including demo and questions | Join with the previous file, position of the short follow-up answer |
| 03-answer-unplaced-draft.mp4 | IMG_5251.MP4 | 00:00.000 → 00:21.842 | A short answer by a person who appears to be A; the question was not recorded | Question content and exact join position unverified. Kept separately |
| 04-talk-B-draft.mp4 | IMG_5252.MP4 | 00:00.000 → 27:32.000 | B's self-introduction and talk. Transcript at 27:32: “Okay, I'm open to questions.” | Error between ASR time and the actual speech boundary |
| 05-talk-B-QA-draft.mp4 | IMG_5252.MP4 | 27:32.000 → 37:02.930 | Taking questions, several questions and answers, and the presenter leaving at the end | Another person joining mid-answer is kept as the same Q&A |
| 06-workshop-C-draft.mp4 | IMG_5253.MP4 | 00:00.000 → 37:59.000 | C's self-introduction, hands-on and extra demo. Includes questions in the middle | There are questions before the full Q&A, so this is not a pure lecture segment |
| 07-open-QA-and-close-draft.mp4 | IMG_5253.MP4 | 37:59.000 → 55:37.662 | After transcript 37:59 “Yeah, go for it.”, a discussion starting with a tool-comparison question, then the closing | The switch around 37:59 is an editing choice. The actual audio boundary needs checking |

Around 27:32 and 37:59, the slides stayed on screen without a major scene change. So scene-change detection alone cannot be said to have found these two boundaries; the spoken content was needed. The order of the short answer was not forced, and no unrecorded introduction or question was invented.

## Generation and Verification

The [reproduction script](split_presentations.py) uses only the paths given by `--source` and `--output`. It requires an output folder separate from the source folder and stops if an output with the same name already exists. It only stream-copies video and audio, so there is no quality loss from re-encoding. However, because of keyframes and audio packets, the review cuts may keep some extra margin at the boundaries.

The durations of the seven actual outputs are, in order, 319.935 s, 1366.933 s, 21.844 s, 1652.072 s, 570.932 s, 2279.077 s and 1058.663 s. The largest difference from the planned length is about 0.077 s. This does not replace checking that cuts are exact in content or that audio is in sync. Decoding the first and last 2 seconds of each file gave no errors and no FFmpeg warnings. The size and modification time of the 5 originals were the same before and after the work.

Running the script and decoding the boundaries took 46.913 s in total. This does not include transcript reading, frame checking or documentation. The cost and creation time of the existing transcripts are unverified. This work had no new payment, upload or watermark. The input segments, output lengths, run time and decode results were recorded in a local `cut-manifest.json`. Human editing time, a manual baseline time, and ranking against other tools were not measured.

## Checking Boundaries by Re-transcribing Short Segments

The 34 seconds of audio from 27:18 to 27:52 in the B original were re-transcribed with local Whisper medium. There is a closing remark and an invitation for questions around 27:32, and the first question starts at about 27:35.28. This confirmed again that the review cut at 27:32 is a candidate that includes the front of the speech switch. Re-running ASR is not the same as a person listening directly, and it does not guarantee the accuracy of the whole original.

The 40 seconds from 37:40 to 38:20 in the C original were also re-transcribed with the same local model. The closing remark ends at about 37:58.28, “Yeah, go for it.” is at 37:59.66, and the first comparison question starts at about 38:00.58, so the current cut at 37:59 falls between them. The extra checks, including re-transcribing both segments and loading the model, took 238.6 s in total, separate from the 46.913 s of video generation.

This original is in English, so it is not used as hands-on evidence for Korean speech or Korean instruction support.

## 2026-10-25 Boundary Waveform Check and Listening Prep

The user approved the boundary check plan, so the audio of the existing split files was compared with the original. For each of the two boundaries, 20 seconds of the original around the boundary were decoded to 16 kHz mono PCM. The last 2 seconds of the earlier split file and the first 2 seconds of the later split file were aligned by normalized cross-correlation. This check finds where the same audio sits in the original. It does not replace checking the meaning of speech, video sync, or a person's listening check.

| Boundary | Original position of the end of the earlier split's audio | Original position of the start of the later split's audio | Estimated overlap | Waveform correlation (earlier/later) |
|---|---|---|---|---|
| B 27:32 | 1652.009375 s | 1652.000000 s | about 9 ms | 0.99855 / 1.00000 |
| C 37:59 | 2279.017375 s | 2279.000000 s | about 17 ms | 0.99799 / 1.00000 |

At the audio boundaries checked, a short overlap rather than a gap was estimated. This fits the packet margin of stream-copy drafts, but it does not verify video frame continuity or integrity at other positions. Both cut candidates were kept, and the existing 7 files were not remade or overwritten.

The join candidate for Talk A runs from the end of the event guidance into a mid-talk remark, as in the original text below. So it cannot be judged that the recording connects without a break just because it is the same person and slides, and the amount of missing recording was not estimated.

> “and get to anything. All right.” — existing IMG_5249 transcript 05:17–05:20
>
> “copilot app. How many have tried to get a copilot app so far?” — part of existing IMG_5250 transcript 00:00–00:17

The existing transcript of the 22-second answer contains a comparison answer, “they are the same,” but not what question it compares. No evidence to identify that question was found at the end of the existing IMG_5250 either, so the extra answer is still kept separately. This is a judgment from reading the transcript, not something confirmed by direct listening.

Four short review clips were made for a person to play and check. The times within each original file are recorded in the table below. The actual video, the absolute paths of the originals and the run manifest are not put in the public Topic; they stay in a local work folder in the vault.

| Local review file | Original | Start | Requested length | Purpose of the check |
|---|---|---|---|---|
| review-A-opening-tail.mp4 | IMG_5249.MP4 | 05:04.927 | 15 s | Check the end of the guidance remarks |
| review-A-main-head.mp4 | IMG_5250.MP4 | 00:00 | 20 s | Check the start of the main talk and whether it can be joined |
| review-B-transition.mp4 | IMG_5252.MP4 | 27:18 | 34 s | Check the cut candidate at playback 00:14 |
| review-C-transition.mp4 | IMG_5253.MP4 | 37:40 | 40 s | Check the cut candidate at playback 00:19 |

The review clips are copies re-encoded to 640 pixels wide, H.264/AAC, for listening and viewing checks. All four decoded fully with no errors, and generation plus the waveform check took 32.96 s in total. This time is not a full check of the originals, and not time saved compared with manual editing. → [Run record for this session](../vl_worklog/20261025_M4_AI-Event-Video-Editing.md#진행-내용)

## 2026-10-25 Talk B Summary Cut Draft

The user said all four review clips had been reviewed and asked to continue. Reflecting that the review was done, the work moved on to the next hands-on step while keeping the existing split drafts. No specific revision comments on individual cuts or a firm judgment on the A join were given, so none are assumed.

Within the first 5-minute sample, a 147.7 s excerpt summary cut was built in the order **explanation of a Skill for PR review → question and answer about the scope of a Skill**. The AI read the existing transcript to pick the segments. Low-volume stretches found near the cuts with FFmpeg `silencedetect` (-32 dB, minimum 0.12 s) were used as supporting evidence. Low volume was not treated as the correct answer for where speech ends, and the final meaning and listening checks are left for later.

| Order | IMG_5252.MP4 original segment | Requested length | Position in output | Reason for selection |
|---|---|---|---|---|
| 1 | 25:21.500–26:24.000 | 62.5 s | 00:00–01:02.500 | Explanation and examples of using a Skill for PR review |
| 2 | 27:52.000–29:17.200 | 85.2 s | 01:02.500–02:27.700 | Question and answer about whether to build a Skill broadly or per purpose |

This is not a summary that represents the whole talk or the whole event. It is **an excerpt draft explaining one theme from the selected 5-minute sample**. The two segments keep the original order, and nothing was cut from the middle of the speech within each segment. Award, performance or atmosphere scenes that are not in this original were not added. No subtitles were added in this version, so that ASR errors in technical terms would not be fixed into captions.

The [summary render script](render_highlight.py) decodes those two segments directly from the original with FFmpeg and joins them with a hard cut. It does not reuse the packet margin of the existing split files. It re-encoded to 1280×720, about 29.97 fps, H.264/AAC stereo MP4. It only allows a new output name and checks that the original's size and modification time are unchanged. No intro, transitions or music were added in this scene-selection test.

The actual output `talk-B-skills-highlight-v1.mp4` is **147.714 s, 23,042,176 bytes**. It decoded fully with no errors and no FFmpeg warnings, and the original's size and modification time were the same. Four sample frames at the start, around the join, and at the end confirmed the video orientation and that the original frame was kept. Output and checks took 65.542 s. This does not include transcript reading, segment selection, documentation, or a person's review time.

The actual video, sample frames, run commands and the manifest of measurements are kept in a local work folder. This result is **one local path: the AI's transcript reading + Python + FFmpeg**. It does not verify automatic selection, Korean instruction support or Premiere handoff of an external AI editing service. → [Summary production record in this WorkLog](../vl_worklog/20261025_M4_AI-Event-Video-Editing.md#4-사용자-리뷰-완료와-요약-제작-재개)

## First Comparison Segment and Next Steps

The first common test source is set as **IMG_5252.MP4 25:00–30:00 (5 minutes)**. It includes the 27:32 candidate where the talk moves to questions, so it suits a test of finding talk boundaries. This time is not fixed as the correct answer. A boundary that a person corrects by checking the audio will be used as the comparison baseline later.

The user reported that the four review clips were reviewed. Next, the joins, the question and answer, and the audio cuts of the new 2 min 27.7 s excerpt summary cut will be reviewed, and the access conditions for the second method to test with the same sample will be checked. The A join and the answer placement, which have no evidence, stay unverified. A comparison of two free services, Premiere import and final delivery quality checks have not been done yet.

## References

- [Hands-on trial plan — Designated source and priority hands-on](../03-Recommendation/test-plan.en.md)
- [M4 run record](../vl_worklog/20261024_M4_AI-Event-Video-Editing.md)
