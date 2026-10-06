---
title: "Claude Artifacts and Routines — Video Slide Plan v4"
created: "2026-10-04 07:30:16"
updated: "2026-10-06 11:30:00"
author:
  - "Codex"
  - "Claude Code"
tags:
  - remotion
  - claude-artifacts-routines
  - video-plan
status: "v4-review-pending"
---

## Plan summary

This is v2, a reworking of v1 using the [Claude-version production prompt](../vl_prompts/video_production_prompt_claude.md). V1 was factually accurate, but its feature explanations followed the learning-module order, repeated caveats in narration, and used a uniform rhythm of roughly 30 seconds per scene; it was not very engaging. V2 retained the same evidence (C01–C28 plus new C29/C30) but changed the story order and how each point is shown. Decisions from the user’s 2026-10-04 review are recorded below and incorporated here.

**v3 (2026-10-06):** Two items were added at the user’s request. (1) A plan for AI-generated photorealistic stills and 10-second Gemini clips; v2 only planned real-screen captures and one AI clip for S01. The plan now places five clips and six stills (I1 deferred) into scenes. (2) New scene S20, “Now I get it every week,” about how the current job-alert email and Claude notification help, and the user’s intention to apply if a Washington State posting appears. The plan grew from 23 to 24 scenes; prior S20–S23 became S21–S24.

**v4 (2026-10-06 narration review):** The conclusion changed. Through v3, the point was “Even without knowing a feature, state the goal and AI will handle it → the person must verify.” In the review, the user said: *“You have to learn in order to explain your goal well, and also when you need to check whether you’re moving toward the goal... The person assigning the work has to learn too,”* and *“I think we still need to use AI carefully.”* (See [[Journal/2026-10-06#Artifacts · Routines 영상 나레이션 리뷰 — 일을 시키는 사람도 배워야 한다 (구술 원문)|Oct 6 original entry]].) The story now runs: **(1) AI found tools I didn’t know (S04–S06, S14) → (2) but it did not explain something essential and did not detect a failure (S08–S09, S11, S15–S19) → (3) the person assigning work must learn too and proceed carefully (S23–S24).** Changed scenes: S04, S05, S06, S08, S09, S11, S14, S15, S19, S21, S22; new S23 (“Five practices for other work”); S24 conclusion rewritten. Total: 25 scenes, about 16:16.

**Title:** undecided; the user will review and refine it. Candidates for discussion:

| # | Candidate title | Intended curiosity |
|---|---|---|
| 0 (new in v4) | I thought I only had to state the goal — the person assigning work to AI has to learn too | Directly connects to the v4 conclusion; an experience contrary to “AI does everything.” |
| 0′ (new in v4) | AI noticed what I needed first. Then it went quiet for three weeks. | Puts S14’s surprise and S15’s reversal in one line. |
| 1 | The AI automation that went quiet for three weeks — two Claude features I didn’t know by name | A “why was it quiet?” mystery plus curiosity about unknown features; connects to the Cold Open. |
| 2 | AI used features I didn’t even know existed | Reversal: the person directing it did not know the feature in advance. |
| 3 | The page AI made was blank for the person who received it | Sharing trap; chapter 2 pays off the promise. |
| 4 | What happens when you delegate to AI and don’t check? | Practical lesson; suitable for search traffic. |

**Thumbnail directions:** (1) Three overlapping real email-inbox captures, large text “Quiet for 3 weeks,” and a small red “FAILED” stamp at lower right. (2) The anonymized booth board made during a meeting, with “Built during the meeting.” Both use real screens; do not imitate UI with AI-generated imagery. Choose after the title is decided.

**Audience:** General viewers new to Claude Artifacts and Routines, interested less in feature names than in “What could I do?” and “What should I be careful about?”

**Promise:** Show what became possible with two features the user did not know by name, where the traps were, and end with one checklist for delegating work to AI.

**Estimated duration:** About 16:16, 25 scenes. Each scene was recalculated as narration characters (excluding spaces) ÷ five characters/second + three seconds of hold. At 4.5 characters/second it would be about 17 minutes. This is an estimate until TTS is measured; do not speed-compress the voice to fit. (The source plan repeated this estimate twice.)

**Language, subtitles, music:** Korean main video, **no subtitles**. Do not reserve a subtitle band at the bottom; display key phrases and labels large enough in the design. Music appears **only in the outro (S25)**, a short score synthesized directly in code; no background music in the main video. The short card-transition sound in S12 is also synthesized directly.

## Brightness and visual design

**Brightness range:** L1 bright. The skill’s original recommends L3/L4 after an L1 project on Sep 24, but the user’s [preference for bright, readable visuals](</C:/AI_study/2026/Changsoo_Vault/AI/RemotionStudio/video-style-guide.md#밝고-읽기-편한-전체-분위기>) and the prompts for this video take priority. The previous video `crd-guide-0927` also used L1 (ivory paper `#FAF8F2`, cobalt, mint), so this project stays L1 but changes the colors and motifs completely.

| Role | Color | Reason |
|---|---|---|
| Background | Cool white `#F3F5FA` | Distinguish it from the previous video’s warm ivory |
| Body text | Deep navy `#161D33` | Contrast against the bright background |
| Artifact | Violet `#5B3FD9` | Consistent marker for “page you view and edit” |
| Routine | Coral `#E0572B` | Consistent marker for “task that runs when scheduled” |
| Success | `#15803D` | Passed/saved |
| Failure/rejection | `#B4232F` plus icon | Use icon/stamp as well as color so it is not distinguished only by color from coral |
| Quiz/question | Yellow highlight `#F5B700` | Signal color only at moments when the viewer is asked a question |

**Background motif:** new “window tile drift”: faint browser-window and envelope outlines float very slowly. Do not use paper texture. For contrast, only S16 has a **dark log-window card** inside the otherwise bright design.

**Candidate new techniques** (add to the effects library only after implementation and review):

1. **Silence convergence:** three empty-inbox cards overlap and converge into one log line (connected across S01 → S15 → S16).
2. **Version gate:** an AI card holding an old number is bounced at a door; only the reread card passes (S11).
3. **Two-screen simultaneous playback:** split author and recipient views to show different results at the same moment (S07/S09).
4. **Leaking funnel:** the “Washington” and “U.S.” filter funnels have holes, so cards from other locations leak through; a fixed funnel filters them (S18).

Base output is 1920×1080, 30 fps. Do not use the same scene type three times in a row. Only S17’s evidenced **“4 jobs”** is used as a `[STAT]`. 

## AI image and video plan

> Added in v3 (2026-10-06). V2 planned real-screen captures only. Real screens prove **what happened**; AI-generated stills and clips supply **atmosphere and motion**. Insert a photorealistic still or 10-second clip among long stretches of static diagrams so the video feels visually alive.

### Division of roles

| Type | Tool/source | Use | Do not use for |
|---|---|---|---|
| 🖥️ Real screen (R1–R6) | User capture/recording | Evidence of actual events: pages, run history, email, notifications | — |
| 📸 Photorealistic still (I1–I6) | gpt-image-2 (generated by user) | Real places/objects/metaphors: desk, venue, phone, envelopes, funnel | **Imitating screen UI, email, or logs**; readable text |
| 🎬 Video clip (V1–V5) | Gemini Veo, silent 10-second clip | Chapter opening, reversal, outro—moments needing motion | Close-up human faces, text on screens, logos |

### Shared rules

- **Never generate real screens with AI.** If a phone or laptop screen appears, keep it off or show only blurred light. R4–R6 real captures supply emails and notifications.
- **People only as hands or from behind.** A face invites “who is that?” and can look like a factual depiction.
- **No text.** Remotion adds all lettering.
- **Keep brightness L1.** Stills should feel lit by cool daylight (`#F3F5FA` background range). V3 at S16 is the only dark scene and plays the same contrast role as the dark log card in v2.
- Three usage modes: (1) full-frame background (V1/V5); (2) diagram over a 30%-opacity background (V2/I4/I6); (3) small right-side card or three-second opening cut (I1/I2/I3/I5/V3/V4).
- Add clips with `<OffthreadVideo muted>`. If a scene exceeds 10 seconds, freeze on the last frame or use only part of the clip; do not slow it down (avoids a “silent failure” from slow playback).

### Placement by scene

| ID | Type | Scene | Content | Use |
|---|---|---|---|---|
| V1 | 🎬 | S01 | Early-morning desk; sunlight slowly crosses an unlit phone; coffee steam | Full-frame background; atmosphere of “three quiet weeks” |
| I1 | 📸 | Deferred | Hand taking notes on printed pages (no text) | v4 uses two real YouTube thumbnails for S04; generation not needed. Keep as backup if another scene needs a still. |
| I2 | 📸 | S06 | Empty venue with neat rows of booth tables | Small right-side card (in place of actual event photo) |
| V2 | 🎬 | S14 | Bright white data-center aisle, blinking LEDs | Routine diagram over 30%-opacity background |
| I3 | 📸 | S15 | Phone just lighting on a bedside table at night (no text) | Right-side card — “the signal arrived” |
| V3 | 🎬 | S16 | Locked mesh door in server room, blinking red status light | Three-second opening → investigation board (only dark shot) |
| I4 | 📸 | S17 | Four white envelopes on morning desk | Large “4” over blurred background |
| I5 | 📸 | S18 | Water leaking from a cracked glass funnel | Three-second opening → leaking-filter diagram |
| V4 | 🎬 | S20 | Sunrise at Mount Rainier; clouds move over evergreen forest | Final 10-second background + “If one appears in Washington → I’ll apply” |
| I6 | 📸 | S24 | Dusk desk, two hands paused before laptop | Background at 30% opacity — “verification is the human’s job” |
| V5 | 🎬 | S25 | Rainy evening window, raindrops and interior lamp | Outro background (QR cards over it) |

The five clips appear at 0:00, 8:06, 9:41, 12:36, and 15:42; stills I2–I5 break up diagram stretches at 3:24–8:06 and 10:09–12:16. Prompts are in [image prompts](image-prompts_en.md) and [video prompts](video-prompts_en.md). Each block includes aspect ratio, duration, colors, empty text-safe areas, and exclusions.

## Viewer-retention map

| Scene | Time | Question the viewer is asking | Device that pulls them forward |
|---|---|---|---|
| S01 | 0:00 | Why was there no email for three weeks? | Leave the question open and cut to a reversal |
| S02 | 0:16 | The AI made this during a meeting? | Speed-ramped real screen → title |
| S03 | 0:32 | What are the two features? What was the trap? | Promise a checklist |
| S04 | 0:59 | Can I assign work without knowing the feature? | “Something shook this belief” → that day’s original note |
| S05 | 1:46 | What are the features? What did I actually do? | “I only said what I wanted” → first example (meeting) |
| S06 | 2:24 | It worked well—what was the trap? | Preview “the first trap” at chapter end |
| S07 | 3:24 | (Quiz) Will the recipient see the same thing? | “Blank screen” reversal → why? |
| S08 | 3:48 | Why was the screen blank? | Page with storage → separate shared-page solution |
| S09 | 4:45 | Why didn’t the change show up? | “A setting AI didn’t tell me about” → preview simultaneous edits |
| S10 | 6:00 | (Quiz) What if AI changes it to 12? | Two-second pause, then answer |
| S11 | 6:25 | Is my edit safe? | Reveal answer → “the person delegating needs design knowledge” |
| S12 | 7:17 | What else did I try? | Fast montage changes rhythm |
| S13 | 7:34 | The builder was wrong too? | Return to “the quiet three weeks” |
| S14 | 8:06 | How did the routine come about? | “AI noticed the need first—why I made this video” |
| S15 | 9:02 | Then why did it go quiet? | “It was quiet even when it failed” → check the clues |
| S16 | 9:41 | Who was responsible? | Reveal cause → how it was fixed |
| S17 | 10:09 | Did the fix really work? | “Real evidence” → one more issue |
| S18 | 10:42 | What else did the routine discover? | “No results ≠ no results” → lesson |
| S19 | 11:23 | Can I delegate everything to AI? | “A person caught the failure”; QR ① → “What about now?” |
| S20 | 12:16 | Is it working now? | Actual email/notification → Washington intention → next-time checklist |
| S21 | 12:46 | What should I say before delegating? | Checklist → example sentence |
| S22 | 13:20 | What would I actually say? | “Goal and verification” → applies elsewhere? |
| S23 | 13:53 | Can I use this elsewhere? | Five principles → what did this person learn? |
| S24 | 14:50 | Was my original belief right? | “The person assigning work has to learn too” + question for viewer |
| S25 | 15:48 | Want to learn more? | QR ② held for 8 sec + end music |

Rhythm changes every 60–90 seconds: speed-ramped screen at 0:16 → original quote at 0:59 → meeting story at 2:24 → viewer quiz at 3:24 → “setting AI didn’t tell me about” at 4:45 → second quiz at 6:00 → quick montage at 7:17 → “I was wrong” at 7:34 → routine origin at 8:06 → dark-log investigation at 9:41 → number reveal at 10:09 → leaking-funnel reversal at 10:42 → actual alert and Rainier clip at 12:16 → checklist stamp at 12:46 → five principles at 13:53 → changed belief and viewer question at 14:50. AI clips (0:00, 8:06, 9:41, 12:36, 15:48) add motion between static diagrams.

V4 is about four minutes longer than v3 (about 16:16). The user judged more context necessary for viewers to follow and asked for background in S04–S09, S14, S23, and S24. To reduce static stretches in longer scenes, change the screen during the scene (two-screen playback, zooming a toggle, switching clips).

## Open questions and answers

| Open question | Raised | Answered |
|---|---|---|
| Were there really no job postings? | S01 | S15 (it failed), S16 (cause), S17 (four postings not received), S18 (filter also wrong), S20 (now it checks weekly) |
| How did AI use a feature whose name I did not know? | S03 | S04 (original note), S05 (only said what was wanted), S06 (meeting page), S14 (routine origin) |
| What was the first trap in the meeting page? | S06 | S07 · S08 |
| What if AI writes using an old number? | S10 | S11 |
| Where was verification most needed? | S13 | S14–S18 |
| One checklist? | S03 | S21 · S22 · S23 (five practices for other work) |
| Was the belief “you have to know in order to delegate” wrong after all? | S04 | S09 · S11 · S19 (what the person needed to know) → S24 (the person delegating must learn too) |

## Chapter structure

| Chapter (viewer’s question) | Scenes | Starts | Merged or removed from v1 |
|---|---|---|---|
| Cold Open + promise | S01–S03 | 0:00 | Removed v1 S01/S02 (reading an outline); moved the three-week failure from S18 to the beginning. |
| How did AI use a feature whose name I didn’t know? | S04–S06 | 0:59 | Reordered v1 S03/S05/S04; moved “how to request” (S06) to S22. |
| Will the recipient see the same link I sent? | S07–S09 | 3:24 | Compressed v1 S07/S08/S11 into S09; v1 S10 (Sep 13/Sep 27 condition difference) stays in evidence ledger only. |
| What happens if a person and AI edit the same number? | S10–S11 | 6:00 | Recast v1 S12–S14 as a quiz and answer. |
| Interlude: I was wrong | S12–S13 | 7:17 | Turned v1 S15 into a 17-second montage; kept S16 and used it to connect to next chapter. |
| How did the routine begin, what happened over three weeks, and what about now? | S14–S20 | 8:06 | Reordered v1 S17–S22 as investigation (setup → symptom → clue → fix → hidden defect → lesson). New filter story at S18; v3 adds S20 (current alerts and Washington intention). v4 makes S14 the origin/story reason and moves “quiet even when it failed” to S15. |
| So how should I ask next time? | S21–S23 | 12:46 | Merged v1 S23–S25 into a one-page checklist and S26 into one example; v4 adds S23 with five practices for other work. |
| Outro | S24–S25 | 14:50 | v1 S27/S28 and scope statement moved into outro; v4 rewrites S24 conclusion as “the person assigning work must learn too.” |

## Scene-by-scene plan

Evidence for every scene links to IDs in the [claim ledger](claim-ledger_en.md). **On-screen labels** are small fixed text that carries qualifying context without overloading narration; because there are no subtitles, labels must be at least 28 px and readable on a small screen. Visual-source legend: 🖥️ real-screen capture · 🧩 explanatory reconstruction (must be labeled) · 📸 AI photorealistic still (gpt-image-2) · 🎬 AI video (Gemini Veo, 10 seconds). I/V IDs match the AI-media table and [prompt sheets](image-prompts_en.md), [video prompts](video-prompts_en.md).

### Cold Open + promise

#### S01 — The silent inbox `[AI_VIDEO]` · 0:00 (16 sec)

**On-screen text:** “Three weeks. Zero emails.” **Visual:** 🎬 V1, 10-second clip of early-morning desk and sunlight crossing an unlit phone (full-frame background) + 🧩 three date stamps, “9/7 · 9/14 · 9/21,” appear in sequence. **Motion:** Silence convergence, step 1—three empty-inbox cards overlap. **Label:** none.

> For three weeks, not one job-alert email arrived. AI was supposed to check the postings every Monday morning. Were there really no jobs?

**Evidence:** C17 · C18. Do not say “there were no notifications at all”; the push is revealed in S15.

#### S02 — Built on the spot during a meeting `[PHOTO_BG]` · 0:16 (16 sec)

**On-screen text:** “During the meeting → used right away.” **Visual:** 🖥️ Required real screen R1—a screen recording of a page being made from a goal-only request, sped up 8× (use a public-safe equivalent). Until obtained, 🧩 reconstruction of an anonymous A/B/C booth board being drawn. **Motion:** A fast-forward timecode runs in a corner.

> But this same AI made a page right away from an idea that came up during a meeting. And we used it in that meeting.

**Evidence:** C04. Hide the event name, vendor names, and settlement information.

#### S03 — Two features whose names I didn’t know `[TITLE]` · 0:32 (27 sec)

**On-screen text:** (final title) / subtitle: “Two Claude features I didn’t know by name — Artifacts · Routines.” **Visual:** Violet “Artifact” and coral “Routine” cards appear like name tags. In the last five seconds, a “Stay to the end: one-page checklist” badge. **Label:** “Tested in Claude Code · September 2026.”

> I did not even know the names of these two features. They are Claude Artifacts and Routines. In this video, I’ll show what became possible with them and where I ran into traps. By the end, you’ll have one checklist of what to tell AI and what to verify when delegating work.

**Evidence:** C01 · C02 · C05.

### How did AI use a feature whose name I didn’t know?

#### S04 — The belief “you have to know in order to delegate” `[QUOTE]` · 0:59 (47 sec)

**On-screen text (verbatim excerpt from original):** “In this case, AI simply found and applied features I knew nothing about on its own.” — Sep 1, 2026 record. **Visual:** 🖥️ Two YouTube thumbnails made from that research appear side by side for about eight seconds: data-center video on left (`assets/yt_thumb_datacenter_ko.jpg`), caregiver video on right (`assets/yt_thumb_caregiver_ko.jpg`). They recede and blur; a note card “To give AI work → I need to know it too” is crossed out, and the original quote descends inside quotation marks. **Motion:** Thumbnails slide in tilted → handwritten strike-through (variation of existing FX-16). **Label:** “Research in Aug–Sep 2026 · public YouTube videos.”

> From late August to early September, I was looking into data-center jobs and caregiver work. I did that research with AI and made YouTube videos from the results too. Until then, I had always thought that to give AI good work, I needed to know at least something about the work myself. But during that research, something happened that shook that belief. AI found and used a feature whose name I didn’t even know. My note from that day says: “In this case, AI simply found and applied features I knew nothing about on its own.”

**Evidence:** C03 (Sep 1 Journal entry) · C38 (YouTube videos from the two topics—[data center](https://youtu.be/DotegI2Q8fw) · [caregiver](https://youtu.be/ma59E0ij1_w)). In the Oct 6 review, “But that day I wrote this” felt abrupt and disconnected; v4 builds the bridge “something shook my belief → that day’s note.” The research is past, so use past tense and show its video thumbnails to clarify what research it was.

#### S05 — I only said what I wanted `[COMPARE]` · 1:46 (38 sec)

**On-screen text:** “Artifact = a page you view and use / Routine = work that runs by itself when scheduled” → below: “What I said = what I wanted · What AI chose = the tool.” **Visual:** Violet browser-window icon left, coral clock/run icon right. A “what I want” speech bubble enters the lower strip and a “tool” card pops out. **Label:** “Claude Code capabilities · scope may differ from regular Claude chat.”

> Those two features are Artifacts and Routines. Put simply, an Artifact is a page AI makes that you can view and use. A Routine is a task AI runs by itself at a time you set. The important thing is that I did not know these features and ask AI to use them. I only said what I wanted, and AI found a tool that fit. That is where my belief—that you have to know the work to assign it—began to change.

**Evidence:** C05 · C03. In the Oct 6 review, “I didn’t choose the feature name” did not communicate clearly; v4 spells out “I didn’t know and request the feature; I only said what I wanted, so AI found a tool → my belief began to change.”

#### S06 — A page made on the spot during a meeting `[PHOTO+BULLET]` · 2:24 (60 sec)

**On-screen text:** “Volunteering at a nonprofit · event-planning meeting” → “It would help to see participating vendors’ booth layout at a glance” → shown immediately on meeting screen. Quote: “Something like that would have been unimaginable before.” — Sep 3, 2026 record. **Visual:** 🖥️ R1 finished page (anonymized) or 🧩 anonymous booth layout. A small right card shows 📸 I2 empty rows of event booths (instead of a real event photo). In the final four seconds, a link icon flies by and cracks, previewing “the first trap.” **Motion:** Booth pins appear one by one. **Label:** “No organization, event, or vendor names.”

> The first feature was Artifacts. I volunteer at a nonprofit. On September 3, that organization had an event-planning meeting. We were discussing how to arrange booths for participating vendors, and I thought it would be helpful to have a page showing the layout at a glance. Actually, I had not intended to use it in the meeting. I told Claude because I wanted to organize my own tasks. But Claude made the booth-layout page there, and I put it up on the meeting screen right away so we could look at it together. Making and using a page on the spot during a meeting would have been unimaginable before. But when I tried to send the link to the others, the first trap was waiting.

**Evidence:** C04 (Sep 3 Journal/original artifact inventory) · C33 (Oct 6 user clarification—nonprofit volunteering, vendor booths, task-organization intent) · C09. 🔒 Do not say or show the organization, event, vendor names, or settlement information.

### Will the recipient see the same thing I sent?

#### S07 — The recipient saw a blank screen `[COMPARE]` · 3:24 (24 sec)

**On-screen text:** Begin with yellow question bar “Will the recipient see the same thing?” → left “My screen” / right “Window with no sign-in.” **Visual:** Two-screen simultaneous playback (new). Left 🧩 full booth layout; right 🖥️/🧩 only a blank page with “Sign in to view this page.” **Label:** “Incognito check · 2026-09-13.”

> If you send a link, will the recipient see exactly what you see? In my case, no. My screen showed the whole booth layout, but the window where I was not signed in showed only a notice saying I needed to sign in. A page that worked so well in the meeting was blank to people outside it.

**Evidence:** C09 · C04 (incognito observation in inventory).

#### S08 — A page whose outside was public `[SVG]` · 3:48 (57 sec)

**On-screen text:** “Meeting page = page + data store” → public link: “appearance ✓ anyone” / “saved contents 🔒 signed-in users only” → solution: “editing page (store)” · “shared status board (contents in page).” **Visual:** 🧩 Split booth-layout page into two layers (appearance and saved contents). Enabling a public link opens only the appearance layer; a lock remains on the contents layer. Then split into two pages: left “Editing” (violet, storage icon), right “Shared board” (green, anyone icon). **Label:** “Experiment 2026-09-13 · may vary by account/date.”

> The reason was how the page had been built. Claude added a small data store so the booth layout could be saved whenever it changed. But with a page like that, even if you make the link public, only the page’s appearance is visible to anyone; the saved contents are visible only to people signed in to Claude. Since all the booth layout was in that store, the recipients saw an empty page. I only understood this after testing it directly with two small pages that looked the same. So I changed the approach: we kept the editing page for working together and made a separate shared status board, with no data store and its contents written directly into the page.

**Evidence:** C09 · C08 · [sharing experiment—answer to Q1](../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix_en.md#answer-to-question-1) (Booth Manager = DB page; Booth Status Board = static path). In the Oct 6 review, the “separate doors for page and data” metaphor alone was hard to follow. v4 explains in order: page with storage → only appearance is public → separate shared board. The Sep 27 record about other sharing restrictions (C10) was omitted because the cause was not established.

#### S09 — One setting AI did not tell me about `[WORKFLOW]` · 4:45 (75 sec)

**On-screen text:** Edited and resent → “It hasn’t changed yet” → share setting “Always share latest version” OFF → turn ON and it works → searched again in October: menu is gone / habit: after editing, check the recipient view in incognito. **Visual:** Two-screen playback for three seconds, “My screen: new version / Recipient: old version,” plus a message bubble “It hasn’t changed yet.” Then 🧩 reconstructed Share menu (version dropdown + toggle) zooms in, toggle off → on. Next, same menu becomes blank under label “October 2026” (dashed outline where toggle had been). No old screenshot exists and the menu cannot be found now, so use a reconstruction for the entire scene. A red “AI skipped this without explaining” question-mark sticker changes to a green “check directly” mark. In the final three seconds, a counter icon shakes to preview next chapter. **Label:** “Reconstruction for explanation · menu item ‘Always share latest version’ was present in Sep 2026 and not visible on Oct 6.”

> There was one more trap. I edited the shared page and sent it again, but the recipient wrote that it still had not changed. My screen clearly showed the new version. It turned out the artifact’s share settings had a separate option to always show recipients the latest version. If it is off, recipients keep seeing the version that was shared before. I did not know that setting existed, and Claude had not told me about it first. I only cleared up the confusion after finding and turning it on myself. But while preparing this video, I looked for it again and the menu is not visible now. These tools’ features change from time to time. Even when AI does things for you, it can skip something essential without explaining it. I now open the page in an incognito window after editing to check what the recipient sees. In the next experiment, AI and I changed the same number at the same time.

**Evidence:** C11 · C34 (Oct 6 user clarification: found and applied setting; Claude did not mention it) · C37 (Oct 6: menu no longer visible) · [old-version link investigation](../02-Artifacts-Sharing-and-Versions/troubleshooting/shared-link-shows-old-version_en.md). v4 moved the “separate editing and sharing pages” habit to S08 and made this scene about a setting AI did not mention.

### What happens when a person and AI edit the same number?

#### S10 — Quiz: what if AI changes it to 12? `[PHOTO+BULLET]` · 6:00 (25 sec)

**On-screen text:** “Value AI knows: 11 / actual value: 13” → yellow question bar “What if AI changes it to 12?” **Visual:** 🖥️ Required R2—the counter page and +1 button. Until obtained, 🧩 “Reconstruction of Sep 27 experiment record.” **Motion:** Number rises 11 → 12 → 13; AI speech bubble still says 11. Hold for two seconds after the question.

> There is a small page that counts a number. AI first saved the number 11. Then I pressed the plus button on screen twice and changed it to 13. But AI still thinks the number is 11. What would happen if AI tried to change it to 12 now?

**Evidence:** C12.

#### S11 — Answer: it gets bounced back `[SVG]` · 6:25 (52 sec)

**On-screen text:** “Only change it if the value is still what I saw” → rejected · nothing written → reread → save 14 / final: a person decides whether to include this safety feature. **Visual:** Version gate (new). AI card with “11” is bounced; red “REJECTED” stamp. It rereads “13,” and that card passes green gate to “14.” Insert a small line from R2 actual log, `nothing was written`. QR Q2 small at lower right for four seconds. **Label:** Original name `if_version` · behavior verified for session-side writes.

> The answer is: it gets bounced back. AI attached a condition when it tried to edit: only change this if the number I last saw is still there. Since I had changed it in the meantime, the update was rejected and nothing was written. AI reread the number and changed it from 13 to 14. It did not overwrite my change. This is a safety feature verified for AI-side writes. Several people pressing a button on a page at once need a separate design. What I took from the experiment is that the person delegating work needs to define the desired result clearly and understand the basic design well enough to know whether this kind of safety feature is needed.

**Evidence:** C13 · C14 · C36 (Oct 6 user insight: ability to define the goal and basic design knowledge).

### Interlude: I was wrong

#### S12 — Montage of small examples `[BULLET]` · 7:17 (17 sec)

**On-screen text:** Greeting · image · comment · multiple files. **Visual:** Four cards flip quickly, about three seconds each. 🖥️ Optional real screen (minimal examples) or 🧩 icon cards. **Motion:** Add a short synthesized transition sound each time a card flips.

> I also tried several features with small examples: greeting someone by viewer name, uploading and displaying an image, commenting on individual paragraphs, and splitting the page and data across multiple files.

**Evidence:** C15.

#### S13 — Correcting the conclusion “it doesn’t work” `[COMPARE]` · 7:34 (32 sec)

**On-screen text:** “Read docs only: ‘It can’t’” → “Tried it directly: ‘It can’” / new rule: check “can’t” with a minimal example first. **Visual:** Red correction stamp over “unavailable”; attach card “author comment → Claude reply.” Empty inbox card from S01 returns during final four seconds. **Label:** Checked from author’s account · public-link visitors not checked.

> But I was wrong about comments. I first read the documentation and concluded that comments were not available on this account. I made a small example and tried it; I could comment and send it to Claude, and get a reply. I came away with a rule: only conclude that something does not work after checking with a small example. And the place where that kind of checking mattered most was the quiet three weeks I mentioned at the beginning.

**Evidence:** C16.

### How did the routine begin, and what happened over three weeks?

#### S14 — AI noticed the need first `[WORKFLOW]` · 8:06 (56 sec)

**On-screen text:** “No Washington State postings — I’ll check again if something appears” → AI made: every Monday → check postings → email only if conditions match / below: “I didn’t even know this feature existed.” **Visual:** 🎬 V2 bright data-center aisle with blinking LEDs, at 30% opacity. Over it, conversation bubble “I’ll check when a posting appears”; coral clock appears and three boxes light in sequence: check, condition, email. **Label:** Amazon WBLP (work-based learning program) postings · routine created 2026-09-02.

> Now I’ll tell you how I came to make this video. The second feature is Routines. In early September, I was looking with AI at Amazon data-center work-based learning programs. There were no postings in Washington State, so I said we would have to look again if one appeared later. Claude heard that and created a routine on its own: check the postings every Monday morning and email me if there is a Washington State posting or a technical job in the U.S. I did not know this feature existed or even that this was possible. AI noticed what I needed and made a tool. That impressed me most, and it is why I made this video.

**Evidence:** C17 · C35 (Oct 6 user clarification: how the routine came about and why the video was made).

#### S15 — But it went quiet `[TIMELINE]` · 9:02 (39 sec)

**On-screen text:** Conditional email only → silence normally expected / 9/7 ✕ · 9/14 ✕ · 9/21 ✕ — no email / push: “Could not check.” **Visual:** First six seconds: “quiet on success / quiet on failure” two identical gray columns overlap. Then 🖥️ required R3, run-history list (hide account/session URL); until obtained, 🧩 “Reconstruction of run history.” Three small push notifications appear under timeline. Right side: 📸 I3 phone just lighting up on bedside table, no text—“the signal came, but I missed it.” **Motion:** Silence convergence, step 2—same error line highlighted across three cards.

> But from here, this is a different story. The routine only emailed when a posting matched, so it was normal to be quiet. The problem was that it was just as quiet when it failed. September 7, 14, and 21: no email three times in a row. Instead, each time the routine sent a short push notification saying it could not check. There had been a signal. Honestly, it took me three weeks to realize that the alert meant the routine was failing every week.

**Evidence:** C17 · C18.

#### S16 — Find the culprit `[SVG]` · 9:41 (28 sec)

**On-screen text:** “Did Amazon block it?” → local PC: normal ✓ / “Was the request wrong?” → request could not get out / culprit: locked door in cloud environment. **Visual:** First three seconds: 🎬 V3 server-room mesh door lock and blinking red light (beginning of 10-second clip) → a **dark log-window card** (the only dark element, for contrast) in the bright scene with one line `EGRESS_BLOCKED`. Investigation board crosses suspects off one by one. **Motion:** Silence convergence, step 3—scattered clues gather into one log line. **Label:** Network access setting “Trusted”—only allowed sites can connect.

> So I checked the clues one by one. Was Amazon blocking it? I opened the same address on my computer, and it worked. Was the request sentence wrong? The run history showed the request could not get out to the internet at all. The culprit was the cloud environment where the routine ran. Its door was locked so only allowlisted sites could get through.

**Evidence:** C19.

#### S17 — Four postings we had not received `[STAT]` · 10:09 (33 sec)

**On-screen text:** “4”—technical job postings not received during the period. Then “Sep 28 scheduled run ✓ New Maryland posting → email.” **Visual:** 📸 I4 four white envelopes blurred on a morning desk; large 4 counts up while four envelopes fly in. 🖥️ Required R4, Sep 28 alert email (hide recipient/address). Optional real screen: environment allowlist setting. **Label:** Manual run Sep 21 · first scheduled run Sep 28.

> I added the Amazon Jobs site to the environment’s allowlist and tried a manual run right away instead of waiting until the next week. All four searches succeeded, and the first alert email arrived with four technical postings we had not received in the meantime. A week later, the scheduled run found a new data-center technical job in Maryland and emailed it. The result of the next automatic run was better evidence than saying the fix had worked.

**Evidence:** C20 · C29.

#### S18 — The leaking filter `[SVG]` · 10:42 (41 sec)

**On-screen text:** Filters set to “Washington only” and “U.S. only” → actually ignored / “No results” ≠ “there really are none.” **Visual:** First three seconds: 📸 I5 close-up of water leaking from cracked glass funnel → new leaking-funnel diagram. Other-state posting cards leak from the Washington funnel; a Spain card leaks from the U.S. funnel. Then show corrected filters catching them. Insert a small line from the response showing actual conditions (`location: null`). **Label:** Routine found this during Sep 21 recovery · corrected after checking on local PC.

> But on the day I fixed it, the routine found another problem on its own. The search filters I had added for Washington State and the U.S. were being quietly ignored. Postings from other locations appeared in the Washington search, and a posting from Spain was mixed into the U.S. technical-job search. The filters had been wrong from the start, but because no results came back, I had no way to notice. I checked the conditions on my computer, found ones that worked, and changed them. No results did not necessarily mean there were really no results.

**Evidence:** C30.

#### S19 — A routine AI made does not report its own failure `[COMPARE]` · 11:23 (53 sec)

**On-screen text:** “AI made the automation” → “But I had to detect and fix the failure.” / “quiet because no result” vs “quiet because failure” → second routine: email “none” even when calendar has zero events / common rule: report failures separately + inspect run record occasionally. **Visual:** The two identical gray columns split and regain their colors. “0 calendar events” result card on right. Final ten seconds: QR ① (C3 routine failure and recovery) enlarged.

> Although AI made the routine for me, noticing that it had broken and fixing it were still my responsibility. There were things it could not yet do well enough for me to hand over everything. I also learned there are two kinds of quiet: quiet because there is no result, and quiet because it failed. So I designed the second routine the opposite way. It checks the next day’s calendar and sends an email saying there are no events even if the calendar is empty. Choose whether to notify only when needed or to report every run based on the goal. But always make failures visible through a separate channel, and open the run history yourself once in a while. I documented this whole investigation in Korean on GitHub.

**Evidence:** C21 · C22 · C28 · C36 (Oct 6 user insight: “AI still isn’t capable enough for me to entrust everything to it”).

#### S20 — Now I get it every week `[PHOTO+BULLET]` · 12:16 (30 sec)

**On-screen text:** “Now, every Monday → alert email + Claude notification” / “There were no Washington State postings this week either” / “If one appears in Washington → I’ll apply.” **Visual:** 🖥️ Required R5, Oct 5 alert email (subject “AWS WBLP Job Alert — Canton, Mississippi”; final line says no Washington posting this week) + 🖥️ R6, Claude notification from same run (phone or desktop). Cards overlap; the final ten seconds transition to 🎬 V4 Mount Rainier sunrise clip, overlaid with “If one appears in Washington → I’ll apply.” **Motion:** Yellow highlight draws across final line of email. **Label:** Scheduled run 2026-10-05 · hide application link and job number.

> Since the fix, this routine checks postings for me every Monday morning. On October 5 it found a new technical posting in Mississippi and sent an email, and a Claude notification came too. The actual email and notification are really helping with my job search now. The email ended with this sentence: “There were no Washington State postings this week either.” If a posting appears in Washington State, where I live, I plan to apply right away.

**Evidence:** C31 · C32. Do not say the user applied or is likely to be accepted. Job details (role and posting date) may appear in the email capture, but do not make it look like application advice.

### So how should I ask next time?

#### S21 — Four checks before delegating `[SVG]` · 12:46 (34 sec)

**On-screen text:** ① What is it for? ② Who will see it? ③ Where will it run? ④ How will I verify? **Visual:** One checklist stamp per line (variation of FX-18 using violet and coral). Small icons from this story beside each: ② blank page, ③ locked door, ④ incognito window/run history. **Label:** ③ reflects this environment; a cloud routine can read a connected repository.

> So what should we tell AI when we give it work next time? After this experience, I realized I should have specified these four things from the start. First, what is the work for? Second, who will see it? Will anyone need to view it without signing in? Third, where should it run? Does it need files on my computer, or are internet sources enough? Fourth, how will we verify it? Check the recipient’s view and the actual run history.

**Evidence:** C24 · C25 · C23.

#### S22 — Try saying it this way `[QUOTE]` · 13:20 (33 sec)

**On-screen text:** Three-sentence request card, tagged with purpose · audience · constraint · verification. Below: “0 feature names.” **Visual:** A chat-input card types the sentence. **Label:** Example sentence based on this experience.

> For example, I wish I had asked for the booth page this way from the beginning: “Make a page that shows the booth layout to meeting participants. People who are not signed in need to be able to view it, so separate the editing version from the sharing version. When it is done, show me how to check it from the recipient’s point of view.” Not one feature name. Let AI choose the tool; the person focuses on the goal and verification.

**Evidence:** C26 · C06.

#### S23 — Five practices that work for other tasks too `[BULLET]` · 13:53 (57 sec)

**On-screen text:** “Five practices for people delegating to AI”: ① Explain who will use the result and how, not only the result. ② Verify “can” and “cannot” with a minimal example. ③ Check important settings yourself—features change. ④ Decide first how automation will signal failure. ⑤ Learn the basic design as the person delegating. **Visual:** Five lines appear one by one; a small scene thumbnail stamps the right side (blank page · correction stamp · toggle · silent inbox · version gate). **Label:** Principles from personal experience · may apply to other tools.

> This is not only about booth pages or job alerts. I wrote down five things that can help when assigning other work to AI too. First, explain not only the output but who will use it and how. Second, even if AI says it can or cannot do something, verify with a small example. Third, AI may not tell you about an important setting, and that setting may change one day. Look through important settings yourself and revisit them occasionally. Fourth, before delegating automation, decide how it should tell you when it fails. Fifth, the person delegating also has to learn the basic design. That is how we can state the goal properly and check whether things are going well.

**Evidence:** C36 · C09 · C16 · C34 · C37 · C18 · C13. New in v4, following the Oct 6 request for “insight that others can refer to for other work, beyond explanation of this specific situation.”

### Outro

#### S24 — The person assigning work has to learn too `[TIMELINE]` · 14:50 (58 sec)

**On-screen text:** Original belief: “I only need to state the goal” → experience: I need to learn both how to state the goal and how to verify it → “The person assigning work has to learn too” / final question: “Is there anything you’ve delegated to AI and never checked?” **Visual:** Cards from earlier scenes (silent inbox, blank page, toggle, bounced card, correction stamp, leaking funnel) converge into one playbook (variation of FX-32 double-accent convergence, violet and coral). 📸 I6 dusk desk with two hands paused before laptop—“verification is human.” Yellow question bar at the end.

> When I first planned this video, I was going to say: “Now you don’t need to know the features; just explain what you want and AI will take care of it.” But after putting everything together, I realized it was a little different. The person still has to learn how to explain what they want and how to check whether the work is going well. The person assigning work has to learn too. Watching the amazing things AI can do these days can make it feel as though the world will change right away. But after using it myself, I know that world has not arrived yet. The occasional amazing feature is not everything. For now, I think we need to trust AI while checking its work carefully. Have you ever left something with AI and never checked it? Tell me in a comment.

**Evidence:** C27 · C36 (Oct 6 original user reflections: “The person assigning work has to learn too” · “We still need to use AI carefully”).

#### S25 — Sources and scope `[OUTRO]` · 15:48 (28 sec)

**On-screen text:** Full experiment record (Q0) · playbook for future work (Q5) / small footer: “September 2026 · experience checked in my environment.” **Visual:** 🎬 V5 rainy evening window with raindrops and interior lamp as background. Two **QR ②** cards side by side, held for at least eight seconds; surrounding cards settle slowly. **Music:** Short ending score synthesized in code, only in this scene (about 20 seconds), below narration and fading over final three seconds.

> This story is based on what I personally checked in my environment in September 2026. Results may differ by account and date. For detailed experiment records and a playbook for future work, use the QR codes on screen or the links in the description. Thank you for watching to the end.

**Evidence:** C28. This scene acts as the “scope card” for the whole video.

## QR destinations

The following destinations returned HTTP 200 in an unauthenticated GitHub raw GET on 2026-10-04 (checked for v1). During screen implementation, generate QR images with ECC High, test an actual scan, and recheck links immediately before rendering.

| ID | Material | Public destination | Placement |
|---|---|---|---|
| Q0 | Entire topic | [Topic overview](https://github.com/solkit70/CatchUpAI_VL/blob/main/Topics/Claude-Artifacts-Routines/README.md) | S25 (QR ②) |
| Q2 | Person/AI database round trip | [Person/AI DB round trip](https://github.com/solkit70/CatchUpAI_VL/blob/main/Topics/Claude-Artifacts-Routines/03-Artifacts-Capabilities-Lab/guides/db-roundtrip.md) | S11 (small, supporting) |
| Q3 | Routine failure and recovery | [Routine failure and recovery](https://github.com/solkit70/CatchUpAI_VL/blob/main/Topics/Claude-Artifacts-Routines/04-Routines-Lab/guides/wblp-routine-audit.md) | S19 (QR ①, end of information-dense chapter) |
| Q5 | Playbook for future work | [Playbook](https://github.com/solkit70/CatchUpAI_VL/blob/main/Topics/Claude-Artifacts-Routines/05-Usage-Patterns/guides/artifacts-routines-playbook.md) | S25 (QR ②) |
| Q1 | Sharing experiment | [Sharing experiment](https://github.com/solkit70/CatchUpAI_VL/blob/main/Topics/Claude-Artifacts-Routines/02-Artifacts-Sharing-and-Versions/guides/sharing-matrix.md) | Description only |
| Q4 | Where to run work | [Local/cloud decision](https://github.com/solkit70/CatchUpAI_VL/blob/main/Topics/Claude-Artifacts-Routines/04-Routines-Lab/concepts/local-vs-cloud.md) | Description only |

## Required real screens

The user will obtain the following six screens (R5/R6 were new in v3). These scenes lose significant impact if replaced by diagrams. See the [capture request](capture-request_en.md#required-real-screens-in-v2) for detailed requirements. Until obtained, implement a temporary screen labeled “illustrative reconstruction” and do not mark final completion.

| ID | Scene | Screen | Status |
|---|---|---|---|
| R1 | S02 · S06 | Screen recording of a page being created from a goal-only request (public-safe equivalent) | To be obtained by user |
| R2 | S10 · S11 | Counter page +1 screen and one line from rejection log | To be obtained by user |
| R3 | S15 | Routine-run list showing failures Sep 7 · 14 · 21 | To be obtained by user |
| R4 | S17 | Sep 28 job-alert email | To be obtained by user (Sep 29 inbox capture noted) |
| R5 | S20 | Oct 5 job-alert email “AWS WBLP Job Alert — Canton, Mississippi” | **New in v3** · in Gmail; receipt verified Oct 5, 10:14 CDT; user capture |
| R6 | S20 | Claude notification from same run (phone or desktop) | **New in v3** · user capture |

## v3 → v4 changes (narration review, 2026-10-06)

| Scene | Review feedback (summary) | Change |
|---|---|---|
| S04 | “But that day I wrote this” had no context. Data-center/caregiver research happened in the past and produced videos. | Bridge “something shook this belief → that day’s note,” use past tense, and show the two YouTube thumbnails made then. |
| S05 | “I did not choose a feature name” did not make sense. | Explain: “I did not know a feature and ask AI to use it; I only said what I wanted, so AI found a tool → my view began changing.” |
| S06 | The scene did not give new viewers enough background. | Explain volunteering at nonprofit → event-planning meeting → vendor booths → request made to organize own task, but page appeared on the spot and was shown in the meeting. Hide organization/event/vendor names. |
| S08 | The “separate doors” metaphor alone was hard to follow. Was it the database? Did that lead to a separate page? | Yes—page with storage → only appearance public → separate shared status board. |
| S09 | User did not know “Always share latest version” existed; Claude did not mention it. But it was absent on Oct 6, suggesting features change. | Reframe as “one setting AI didn’t tell me about”; add reversal “I don’t see the menu now”; use a reconstruction diagram; move edit/share separation to S08. |
| S10 · S11 | The person must define the goal and understand basic design. | Add that realization at end of S11. |
| S14 | Explain how the routine began and why the video was made. | “No Washington posting → I’ll check later” → AI makes routine → origin of video. |
| S15–S19 | Three-week failure is “the next story”; AI is not yet enough to delegate everything. | Open S15 with “But from here, it’s a different story”; start S19 with “Noticing and fixing the failure was still my job.” |
| S21 · S22 | Situation-specific explanation is good; add insights others can use for different work. | Refine S21/S22 to “what I should have said from the start”; add new S23 with five principles. |
| Conclusion | The person delegating must learn too and proceed carefully. | **Rewrite S24**: original belief → changed belief → question to viewer. |
| QR | Korean docs, so keep Korean QR for now. Codex is making English docs for a future English video. | No change. Make separate QR destinations to `_en.md` if an English video is produced. |

## v2 → v3 changes (2026-10-06)

| Change | Reason |
|---|---|
| Added AI image/video plan: five 10-second Gemini clips and six photorealistic stills | User request. V2 had only real captures, leaving long static diagram sections. AI media supplies atmosphere/motion; real screens remain the evidence. |
| Added S20 “Now I get it every week” (30 sec) | User request: show that the fixed routine currently helps (Oct 5 email and Claude notification) and the intention to apply if Washington has a posting. Final answer to Cold Open’s “Were there really no jobs?” |
| 23 → 24 scenes; S20–S23 → S21–S24 | Inserting S20. |
| Added required real screens R5/R6 | Show actual email and notification in S20. |

## v1 → v2 changes

| Change | Reason |
|---|---|
| 28 → 23 scenes; about 12–15 min → 11–12 min | Merged or moved repetitive scenes (v1 S06/S07/S10/S23–S25) into the evidence ledger. |
| Removed outline reading (v1 S02); moved three-week failure to Cold Open | The most compelling story did not appear until 7:38. |
| Reordered chapters from learning modules to viewer questions | Followed the [story seed](../01-Inventory-and-Questions/guides/story-seed_en.md#what-the-video-should-avoid) to avoid a feature list. |
| Reduced seven “this does not mean…” caveats to one narration caveat (S11), labels, and outro scope statement | Repeated caveats sounded uncertain. Labels, evidence ledger, and description preserve accuracy. |
| Removed `if_version`, `EGRESS_BLOCKED`, and version numbers from narration | Replaced with metaphors (“only while the number I saw is unchanged,” “the door was locked”); original terms remain in labels. |
| Added two viewer quizzes (S07/S10), confession (S13), investigation arc (S14–S18) | Change rhythm every 60–90 seconds to retain viewers. |
| Centered the real “blank when not signed in” booth-page case in chapter 2 | V1 only described experiment results and omitted the actual trap the user encountered. |
| Added “four postings not received” (C29) and “leaking filter” (C30) | Show what was at stake in the failure and how to question “no results,” within what records support. |
| Korean subtitles → no subtitles | User decision. Make screen text and labels large enough. |
| Warm white + teal/amber → cool white + violet/coral | Distinguish from previous `crd-guide-0927` video (ivory, cobalt, mint). |

## Decisions confirmed in user review (2026-10-04)

| Item | Decision |
|---|---|
| Title | User will review/refine directly; finalize S03 wording and thumbnail direction then. |
| Cold Open | Retain basic combination of three weeks of silence (S01) and meeting-time creation (S02). |
| Required real screens R1–R4 | User will obtain them. |
| Ignored-filter story | Include; new S18, evidence C30. |
| Subtitles | None. |
| Music | Short score composed directly in code only in outro S25. Also synthesize S12 transition sound. |
| AI media (Oct 6) | Five 10-second Gemini clips and six photorealistic stills; do not generate real UI, email, or logs. |
| Video conclusion (Oct 6) | “Just state the goal” → “The person assigning work has to learn too; proceed carefully.” |
| Length (Oct 6) | Expand context so viewers can follow; about 16 minutes. |
| QR (Oct 6) | Korean video keeps current Korean-document QR codes. |
| Current alerts/Washington application intention (Oct 6) | New S20; show real Oct 5 email (R5) and Claude notification (R6). |

## Self-review

| Check | Result |
|---|---|
| Does the opening make the next moment interesting? | Yes: “Three weeks, zero emails. Were there really no postings?” |
| Does a real screen/result appear within 30 seconds? | Yes: speed-ramped real screen at S02 (0:16), though it is a reconstruction until R1 arrives. |
| Are there likely drop-off sections? | Scenes lengthened in v4. Longest: S09 (75 sec), S06 (60 sec), S24 (58 sec), S08 (57 sec). S09 changes every ~15 sec (two screens → message bubble → toggle zoom → sticker); S06 has pin placement, photoreal card, cracking link; S08 splits layers then pages. If too long, first shorten “I only understood after testing it directly” in S08. |
| Does each chapter have a question → answer → connection? | Yes; S06, S09, S13, S19 pull into the next chapter. |
| Is the Cold Open question answered in the body? | Yes, S15–S18. |
| Is any scene only a feature introduction? | S12 (17 sec montage) comes closest; retain it as rhythm change and introduction to S13 confession. |
| Any unexplained technical jargon left in narration? | No. Original terms appear only in screen labels. |
| Does every claim have an evidence ID? | Yes, S01–S25 link to C01–C36. |
| Do key points remain visible without subtitles? | Each scene has one key “on-screen text” line; numbers, dates, and quotations appear on screen. |

## Next steps

Get review on plan v3. Meanwhile, the user will (1) decide the title, (2) obtain real screens R1–R6, and (3) generate I1–I6 from the [image prompts](image-prompts_en.md) and V1–V5 from the [video prompts](video-prompts_en.md), saving them to `public/claude-artifacts-routines-1004/images/` (filenames are listed in each prompt sheet). Then implement in `AI/RemotionStudio/` with video ID `claude-artifacts-routines-1004` and show the Studio preview. First build scenes without captures/media using temporary reconstructions. Create an edge-tts draft, then final Qwen3-TTS voice; get a review of each. Do not render the MP4 before final approval. Follow the [Claude-version production prompt](../vl_prompts/video_production_prompt_claude.md#12-execution-steps-and-user-review).

[Korean original](video-slide-plan.md) · [M6 overview](README_en.md) · [Claim ledger](claim-ledger_en.md)
