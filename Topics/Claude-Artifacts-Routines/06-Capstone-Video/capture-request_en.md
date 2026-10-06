---
title: "Claude Artifacts and Routines — Video Capture and Source-Material Request v2"
created: "2026-10-04 07:30:16"
author:
  - "Codex"
tags:
  - remotion
  - capture-request
  - claude-artifacts-routines
status: "review-pending"
---

## Materials currently available

PNG/JPG/JPEG files were searched for across the topic, but no saved screen captures were found. Lab HTML, run records, and public documents exist, and records mention seeing captures in the past, but the original file location is unknown. The request distinguishes screens that can be captured now from past experiments whose conditions may have changed.

The planning review will use the list below to choose which items to show as actual screens. A capture request does not authorize changing account sharing settings, resending email, running a routine, or resetting the counter. Do not recreate an old state and present it as a current screen. If a historical capture cannot be found, use a diagram reconstructed from the record and label it as a reconstruction.

## Required real screens in v2

The [slide plan](video-slide-plan_en.md#required-real-screens) marks these six screens as **required** (R5 and R6 were added in v3). They directly show the video’s promises (“I described the goal and it was built” and “a quiet failure”). Replacing them with diagrams would significantly weaken those scenes. A02, A03, A05, and A07 are optional and can use record-based reconstructions.

| ID | v2 scene | What/how to capture | What must be visible | What to hide | Temporary screen until obtained |
|---|---|---|---|---|---|
| R1 (extends A01) | S02 · S06 | Screen-record 1–3 minutes of a public-safe equivalent page being built from a goal-only request. The video will speed it up 8×. Example: “Make a page showing the layout of anonymous booths A, B, and C.” | Request → generation → finished booth-layout board | Account, tabs, private links. Do not include actual event or vendor names or settlement details at all. | 🧩 Reconstructed booth board being drawn |
| R2 (A04) | S10 · S11 | Counter page from Sep 27 and one line from the rejection log. If the original capture is unavailable, capture the **current screen**, label it “current,” and do not reset or rewrite the counter. | Number, +1 button, one line: `nothing was written` | Session ID, full URL, unrelated console output | 🧩 “Reconstruction of the Sep 27 experiment record” |
| R3 (A06) | S15 | Existing routine-run list showing failures on Sep 7, 14, and 21. Do not run it. | Dates and failure state | Account, session address, token | 🧩 “Reconstruction of run history” |
| R4 (A08) | S17 | Sep 28 job-alert email (confirmed in inbox Sep 29) | Subject, received date, result sentence mentioning Frederick, Maryland | Recipient/sender, email addresses, other inbox items | 🧩 Result card (do not imitate email UI) |
| R5 (new in v3) | S20 | Oct 5 alert email “AWS WBLP Job Alert — Canton, Mississippi” (in Gmail inbox) | Subject, received date, first line about a new WBLP technical posting, final line “There were no Washington State postings this week either.” | Recipient, sender address, application link, job number, other inbox items | 🧩 Result card (do not imitate email UI) |
| R6 (new in v3) | S20 | Claude notification from the same Oct 5 run (phone lock screen or desktop notification) | That a notification arrived, time, routine name | Account, session address, notifications from other apps | 🧩 Reconstructed notification card (label “illustrative reconstruction”) |

Optional addition: if available, insert a three-second view of the environment’s **Network access** allowlist (A07) before S17.

## Full v1 screen list

| ID | Scene | Screen/capture needed and timing | What must be visible | What to hide | Can it be replaced? |
|---|---|---|---|---|---|
| A01 | S01 · S04 · S07 · S08 | Open a result page that can be public. First choice: Builders Lounge event entry page; booth editing tool only after confirming material boundaries. | Page result and some structure. Enlarge the important area instead of showing the whole screen small. | Account, browser tabs, private links, vendor names and settlement details | If no public-safe material is available, use an anonymous booth A/B/C diagram labeled “illustrative reconstruction.” |
| A02 | S11 | Current Share menu’s selected shared version and what appears in a no-login window. Observe only; do not change settings. | Actual shared version and what a recipient can access | People list, emails, profiles, other tabs | Can use a version card reconstructed from the Sep 25 record. Omit current click-path instructions. |
| A03 | S09 · S10 | If Sep 13 original capture exists, show the public page and data sign-in notice together. | Date, HTML opens, data notice | Account, email, unrelated records | If original unavailable, use a diagram based on the experiment record. Do not imply that a successful rerun is the old result. |
| A04 | S12–S14 | Original Sep 27 counter page and conflict/retry logs. If only the current page is available, label it as current. | Value, version, `version_mismatch`, `nothing was written`, minimum line showing successful result | Session ID, account, full URL, unrelated console output | Can be replaced completely with record-based motion. Do not reset current state. |
| A05 | S15 · S16 | Relevant areas from viewer greeting, image, comments, and multi-file examples. For comments, show a comment posted by the author and the reply. | Successful result of one capability; evidence of Send to Claude behavior | Real user names, private image content, unrelated comments | Can use minimal example source or a diagram of observed results. Do not extrapolate to outside viewers. |
| A06 | S18–S20 | Run-history list and Sep 21 manual recovery/Sep 28 scheduled-run logs. Do not execute a run for capture. | Dates, failure/success, blocked domain, checked result. Distinguish conditional email from push. | Account, token, session URL, email recipients, full search results | Reconstruct dates and minimal log lines from records; label “reconstruction of run history.” |
| A07 | S19 · S24 | Environment edit screen’s Network access and relevant site access. Show only where to verify it; no need to show all account settings. | Role of site-access settings | Environment variables, API keys, connected-service usernames | Can use a diagram of the execution environment, but omit exact click instructions. |
| A08 | S20 · S21 | Relevant parts of the Sep 28 job email and Sep 27 “no events” email | Received date and result sentence; personal calendar content is not needed | Recipients, sender, email addresses, other inbox items, meeting links | Can use a result card based on the original result. Do not style it to look like a real email capture. |

## Optional material and capture method

Use photos from the meeting only after confirming they are public-safe for S04. The same experience can be conveyed with the user’s original words and a layout diagram if there is no photo. Do not move internal event-document names, amounts, or original images outside the vault in order to find a photo.

Capture at original resolution as PNG if possible, then crop the required areas separately for each scene. Mask personally identifying information before copying the original into the production folder. Put only public-safe assets in `06-Capstone-Video/assets/`; when an asset is obtained, record its path, capture date, and whether it is current or reconstructed in this document. Do not create an empty assets folder while no assets exist.

## AI visual candidates

AI media was formally planned in v3 (2026-10-06): five 10-second Gemini video clips (V1–V5) and six photorealistic still images (I1–I6). Placement is in [AI image/video plan](video-slide-plan_en.md#ai-image-and-video-plan); prompts are in [image prompts](image-prompts_en.md) and [video prompts](video-prompts_en.md). Real UI, logs, emails, and notifications must still be captured or explicitly reconstructed; generated images must not stand in for them.

## Material checklist

- [ ] R1 screen recording (v2 S02 · S06)
- [ ] R2 counter page and log (v2 S10 · S11)
- [ ] R3 routine run history (v2 S15)
- [ ] R4 Sep 28 alert email (v2 S17)
- [ ] R5 Oct 5 alert email (v3 S20)
- [ ] R6 Oct 5 Claude notification (v3 S20)
- [ ] Generate AI stills I1–I6 and clips V1–V5
- [ ] Check for real names, emails, tokens, and internal material; place only public-safe assets
- [ ] Label each capture as a current screen or a reconstruction of the record

Current status: **request list complete; materials not yet obtained**. Missing materials do not block the full plan. When the [slide plan](video-slide-plan_en.md) is approved, confirm the exact set of required real screens at the same time.

[Korean original](capture-request.md) · [M6 overview](README_en.md)
