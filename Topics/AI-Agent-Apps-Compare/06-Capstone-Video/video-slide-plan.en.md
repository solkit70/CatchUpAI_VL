---
title: "Comparing Four New AI Agents — Video Slide Plan v2"
created: "2026-10-13 10:30:00"
updated: "2026-10-14 11:30:00"
author:
  - "박창수"
  - "Claude Code"
tags:
  - remotion
  - ai-agent-apps-compare
  - video-plan
status: "📋 Awaiting review"
video-id: "agent-apps-compare-1013"
---

# Video Slide Plan: Comparing Four New AI Agents

[한국어](video-slide-plan.md)

## Changes in v2 (2026-10-14)

Reflects the direction agreed after transcribing and reviewing two clips edited from the livestream by Changsoo Park (`1014_Codex_Muse-1`, 37 seconds; `1014_Codex_Muse-2`, 1 minute 43 seconds). The clip review is in the vault at `AI/RemotionStudio/public/agent-apps-compare-1013/live-clips-review.md`.

1. **Two real live reactions as the opening hook** — clip 1 through “It entered that itself?” and clip 2 through “This seems to have tremendous potential.” Use **the original voices** with subtitles (S01).
2. **Show all of clip 1 (37 seconds) in S14** as the reveal, “It Turned Out AI Entered It.”
3. **Replay clip 2 from the beginning through “This is a new experience” (33 seconds) in S18**. Promise the rest of the scene cut short in the opening (S02), then resolve it here — a retention device.
4. **Briefly use clip 2's answer/source scene (about 13 seconds) at the start of S19**. The screen showing sources leads directly into “Can we trust it as is?”
5. **New scene S20, “Muse Outside, My 2nd Brain at Home”** — turns the discussion in the latter half of clip 2 (Changsoo Park's Oct 14 explanation) into slides. Thus 23 scenes became 24; former S20–S23 became S21–S24.
6. **Voices**: Use multiple Qwen3 voices, and **include a clone of Changsoo Park's voice in this episode** (Changsoo Park, Oct 14). First-person experiences use his voice; explanations/quizzes use the presenter voice. This connects naturally to his real voice in the live clips.
7. **Name display**: Use **“Catch Up AI,” not Changsoo Park's name**, in on-screen text, narration, and subtitles (Changsoo Park, Oct 14). Write “캐치업 에이아이” in the TTS script. Names remaining in this plan's production notes do not appear on screen.
8. **Promise for the future**: At present, Muse has only been installed and its basic features tried. Add a promise in the outro (S24) to keep sharing new learning from continued use (Changsoo Park, Oct 14).

## Planning Overview

Combine M1–M5 results into one video. Evidence comes only from this topic's documents, listed under “Evidence” for each scene. Production follows the Remotion skill (`_Settings_/Skills/remotion-video/SKILL.md`), vault video style guide (`AI/RemotionStudio/video-style-guide.md`), and Codex scene lessons (`codex-design-lessons.md`).

**Target audience**: General viewers who have heard of AI agents but never used one. They wonder, “Which new one should I use? What can I delegate?”

**Video promise**: Explain what the four new agents are, show what worked and did not when delegating to the one actually tested, and leave viewers with **“four questions before delegating.”**

**What to disclose honestly** (say it in the video): Four were compared, but **only Muse was directly used**. There were two tasks with synthetic data, and elapsed time was not measured. Therefore, do not rank services or claim quantified time savings.

**Title candidates** (user makes the final decision):

| # | Candidate title | Intended curiosity |
|---|---|---|
| 1 | AI Put Another AI to Work — Four New AI Agents: What Should We Delegate? | Connects directly to the opening |
| 2 | Of Four New AI Agents, I Could Use Only One | “Why only one?” |
| 3 | Four Questions to Ask Before Delegating to an AI Agent | Practical lesson; search discovery |
| 4 | From AI That Answers to AI That Works — Grok Bot, Muse, Dots, Instinct | Search discovery through service names |

**Estimated length**: About 15 minutes, 24 scenes. Estimated as narration character count per scene (excluding spaces) ÷ five characters per second + three-second pause + actual live-clip duration. These estimates precede measured TTS output.

**Language/subtitles/music**: Korean main video. No subtitles during narration; make key phrases and labels sufficiently large (at least 28px). **Korean subtitles only where live clips play with original sound (S01, S14, S18, start of S19)** — spontaneous live speech is hard to follow by sound alone (subtitle text in the “Live Clips” table below). Display Muse task B's English sentences alongside Korean meanings. Music is a short piece synthesized directly in code **only in the outro (S24)**, with none in the main video.

**Voices**: edge-tts draft → replace with Qwen3-TTS after approval. Use **two voices** in the final Qwen3 stage (Changsoo Park's Oct 14 decision).

| Voice | Assigned scenes | Reason |
|---|---|---|
| **Changsoo Park's voice (clone)** — Qwen3 clone | First-person experience/judgment: S03, S08, S10, S11, S12, S13, S14, S16, S17, S18, S19, S20, S21, S23, S24 | Testimony of “when I tried it,” continuous with the real voice in live clips |
| **Presenter voice** (Qwen3 preset; `ko-KR-SunHiNeural` for edge-tts draft) | Introduction, explanation, quizzes: S02, S04, S06, S07, S09, S15, S22 | Introduces the Catch Up AI livestream (S02) and handles objective explanations, creating rhythm through voice changes |
| (Original live audio) | Clip portions of S01, S14, S18, S19 | Real reactions unchanged |

In the edge-tts draft, temporarily use a male voice (`ko-KR-InJoonNeural`) for Changsoo Park's scenes to preview only the rhythm of voice changes.

## Brightness and Screen Design

**Brightness band**: **L2 moderately bright** (pastel). Both preceding videos, `crd-guide-0927` and `claude-artifacts-routines-1004`, were L1. This follows rule ① (different band from the previous two) while honoring the user's preference for bright, readable screens. Avoid L3/L4 because the style guide reserves dark colors for night, danger, and warning scenes.

| Role | Color | Reason |
|---|---|---|
| Background | `#E6EEF6` pastel sky blue → `#EEF3EA` pale green gradient | Distinguishes it from the previous video's cool white/ivory |
| Body text | `#14213D` dark navy | Contrast against a bright background |
| Muse (directly used) | `#2F7D5B` forest green | Consistent marking of hands-on experience |
| Research only (Grok Bot, Dots, Instinct) | `#7A8699` gray blue + dashed border | Distinguishes untested services by both color and line style |
| Success | `#1F8A4C` + ✓ icon | |
| Human editing needed | `#C77712` amber + pencil icon | “Usable with edits,” rather than “failure” |
| Caution/risk | `#B4232F` + warning icon | Instinct agency clause, etc. |
| Quiz | `#F2C230` yellow highlight band | Only when asking viewers a question |

**Background motif**: Very faint task-card outlines (to-do cards/check boxes) drifting slowly. Avoid static screens in every scene.

**New technique candidates** (record in `effects-library.md` after implementation/review):

1. **Four locked doors, one open door** — four service cards stand like doors; locks descend on three (S08).
2. **Baton handoff** — a task card flies from a VS Code window into a browser window (S14, S18, S20).
3. **The reverse of highlighting — red underline grading** — red wavy underlines appear only under unsupported phrases in task B's English sentences (S16).
4. **Dual practice/research marking** — badges saying “Directly used” / “Materials only” accompany every service mention (throughout).

Default output: 1920×1080, 30fps. Arrange so the same scene type does not appear three or more times consecutively.

## Visual Asset Plan

> Video style rule: **Do not generate images or short videos via API.** Prepare prompt documents for the user to generate them directly. Use real screens for practice scenes.

### Types and Roles

| Type | Who creates it | Used for | Not used for |
|---|---|---|---|
| 🔴 Live clips (C1, C2) | **Two files Changsoo Park edited from the livestream** | Actual scenes of Codex operating Muse in the browser and reactions at that moment | — |
| 🖥️ Actual screenshots (R1–R9) | Already in the topic | Muse settings, source panel, task results | — |
| 📸 AI images (I1–I5) | Generated by the user from prompts | Metaphor/mood: key, clock, specimen, stamp, outside/home | **Imitation screen UI**, readable text, human faces |
| 🎬 Gemini videos (V1–V4) | Generated by the user in Gemini (Veo), 8 seconds, muted | After opening, reveal, foliage, conclusion | Human faces, on-screen text, logos |

### Live Clips — Selected Segments (Direction Confirmed 2026-10-14)

Originals: `C:\Users\dougg\Videos\Youtube\2026\AI_in_Action\20261009_NewTopics\1014_Codex_Muse-1.mp4` (37.0 seconds), `…-2.mp4` (1 minute 43.1 seconds), 1920×1080. During production, copy into `AI/RemotionStudio/public/agent-apps-compare-1013/clips/` and trim with `<OffthreadVideo>` `startFrom` / `endAt` (do not trim originals). Segments were chosen using word-level timestamps.

| ID | Original/segment | Scene | Sound | Visible content |
|---|---|---|---|---|
| **C1-H** | Clip 1, **0:00.8–0:11.6** | S01 hook ① | Original + subtitles | First 3 seconds contain a transition; replace with a **zoomed freeze of the Codex answer (frame at 4 seconds)** — highlight “I performed this process by operating the Muse screen.” Then the Muse screen |
| **C2-H** | Clip 2, **0:00.0–0:19.7** (cut before the next “I”) | S01 hook ② | Original + subtitles | “ChatGPT” started debugging this browser banner, someone else's cursor, foliage question entering itself in Muse |
| **C1-F** | Clip 1, **0:00.8–0:37.0** (full) | S14 | Original + subtitles | Codex answer → Muse task B result |
| **C2-A** | Clip 2, **0:00.0–0:33.0** | S18 | Original + subtitles | Question entry → send → Muse “Finding spots” → Codex in VS Code |
| **C2-B** | Clip 2, **0:52.0–1:05.2** (audio from 0:54.1) | S19 opening | Original + subtitles | Muse's Korean answer (five places) → **Sources panel** |
| (C2-C) | Clip 2, 1:13–1:25 | S20 (optional) | **Muted** | Saving Muse's answer to the vault in VS Code — small card only; blur path |

Do not use audio from clip 2 at 0:33–0:52 (“This experience is also a very good experience … impressive”). The same sentence already appears in S19's on-screen quotation (2026-10-11 original).

**Subtitle text** (corrected transcription of live audio; parentheses supplement the screen)

| ID | Subtitles |
|---|---|
| C1-H | “I performed this process by operating the Muse screen.” (Reading Codex's answer) → It entered that into Muse itself? → It entered something I didn't enter? |
| C2-H | There is a cursor right now. It isn't mine. → The cursor moved over here. It looks like ChatGPT is using this screen. → I'm not using it. Codex is using it. → This is such an amazing experience. Codex AI is operating Muse right now. → This seems to have tremendous potential. |
| C1-F (after C1-H) | So Codex has this feature. I definitely didn't type this. → It entered it, then even made screenshots of what it entered and created a document. → This is very convenient! Excellent. → I installed OpenAI here. I think this is possible because I installed the ChatGPT plugin. (Speculation during broadcast) → In that case, I also installed Claude, so Claude can operate it too. (Speculation during broadcast) → I could ask AI to operate Muse instead of operating it myself. |
| C2-A (after C2-H) | I didn't enter this. → I asked Codex — not from this browser, but from VS Code — → to operate Muse and recommend places to see fall foliage, → and (Codex) is carrying that out here. → This is great. A new experience. |
| C2-B | The answer has arrived too. This is wonderful. → Codex asks and (Muse) answers, → and it also shows where the information came from. |

**Mask**: Muse conversation URL (`muse.ai/thread/…`) in address bar, browser tabs, bookmarks bar, extension icon names, small broadcast window at lower left, VS Code file paths and vault document names. In the upper banner, retain only ““ChatGPT” started debugging this browser” and blur the rest — that phrase is evidence of AI operating the browser.

### Actual Screenshots — Already Available

| ID | File | Scene |
|---|---|---|
| R1 | `03-Hands-On/assets/muse-screenshots/data-controls.png` | S11 |
| R2 | `03-Hands-On/assets/muse-screenshots/permission-defaults.png` | S11 |
| R3 | `03-Hands-On/assets/muse-screenshots/gmail-permissions.png` | S11 |
| R4 | `03-Hands-On/assets/muse-screenshots/calendar-write-permissions.png` | S11 |
| R5 | `03-Hands-On/assets/muse-screenshots/source-panel.png` | S12 |
| R6 | `04-Real-Task-Trial/assets/muse-task-b-review.png` | S16 |
| R7 | `04-Real-Task-Trial/assets/muse-fall-foliage-result.png` | S19 (zoom after C2-B) |
| R8 | `03-Hands-On/assets/muse-screenshots/direct-network-protocols.png` | (Reserve) |
| R9 | `03-Hands-On/assets/muse-screenshots/calendar-permissions.png` | (Reserve) |

Fit screenshot slots to image aspect ratios and create cropped versions of only the needed regions (codex-design-lessons §6). Add “Actual screen” badges.

### AI Image / Gemini Video Placement

| ID | Type | Scene | Content | Usage |
|---|---|---|---|---|
| V1 | 🎬 | S04 | A hand places a task card (no text) in a desk tray; tray glides away — “delegate” | Full-screen background + light gradient behind left-side text |
| V2 | 🎬 | S08 | Four doors in a bright hallway; three stay closed, one slowly opens and admits light | Full-screen background → “1 / 4” overlaid |
| I1 | 📸 | S09 | One hand gives another a small brass key over a desk (no faces) | Right-hand card — “handing over authority” |
| I2 | 📸 | S13 | Numberless wall clock and blank paper timetable | First 3 seconds → reconstructed diagram |
| I3 | 📸 | S17 | A single glass specimen jar on an empty shelf | Background at 30% opacity — “small sample” |
| V3 | 🎬 | S18 | Puget Sound maple forest; red leaves fall in the wind | First 3 seconds full screen → clip C2-A |
| I4 | 📸 | S23 | Hand gives folder to small robotic arm; a human holds an approval stamp beside it (no text) | Background at 30% opacity — “delegate, human verifies” |
| I5 | 📸 | S20 | Left: hand holding phone in autumn park; right: laptop on home desk by window — smoothly connected in one image | Behind comparison cards (①); blurred during flowchart |
| V4 | 🎬 | S21 | Pen checks four empty boxes on paper one after another (no text) | First 4 seconds → decision flowchart |

Four Gemini videos (within the skill's recommended 2–5), each the Gemini app's default eight seconds. Videos and photographic images break up sequences of static diagrams (S05–S10, S20–S22). If a scene exceeds ten seconds, hold the final frame instead of slowing the clip (avoids the “silent failure” of slow playback). Prompts were written in [image-prompts.md](image-prompts.en.md) (I1–I5) and [video-prompts.md](video-prompts.en.md) (V1–V4) so **only one block needs copying** (including ratio, resolution, brightness, color hex codes, empty space, exclusions), on Oct 14. Put generated files in `AI/RemotionStudio/public/agent-apps-compare-1013/images/` with the exact filenames in the prompt documents.

### GitHub QR

- URL: `https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/AI-Agent-Apps-Compare` — **confirmed accessible 2026-10-13**
- **QR ①** — S10, after the service comparison (the section densest with numbers/conditions)
- **QR ②** — S24 outro; hold at least eight seconds
- Error correction H; large enough. Same link in description. Narration states that repository documents are in Korean.

## Viewer Retention Map

| Scene | Time | Viewer's question | Pull into the next scene |
|---|---|---|---|
| S01 | 0:00 | AI says “I operated it”? The cursor moves by itself? | Two real reactions → three-line “What this video covers” at the end |
| S02 | 0:32 | What exactly was that? | Promise “the full story from the beginning midway through” → four AIs like this |
| S03 | 0:57 | What will I get from this? | Four questions; only one accessible; preview working outside and bringing results home |
| S04 | 1:29 | How is it different from a chatbot? | Answers vs work → what are the four? |
| S06 | 1:57 | What is each of the four? | Four cards → can anyone use them? |
| S07 | 2:52 | (Quiz) How many can I try right away? | Three-second pause → answer |
| S08 | 3:22 | Why only one? | Three locked doors → delegation risks? |
| S09 | 3:46 | How far does it act on my behalf? | Agency clause → this is complicated |
| S10 | 4:31 | Must I remember all this? | QR ① → hands-on story |
| S11 | 4:54 | What was the first screen like? | Real meaning of “I'll ask” → are sources trustworthy? |
| S12 | 5:44 | Can I trust an answer with source links? | Third-party source reveal → calculations? |
| S13 | 6:24 | Did it calculate time correctly? | Wrong at first → asked again |
| S14 | 6:59 | What about my work? What was “I operated it”? | **Full opening clip ①** — AI entered it → two results |
| S15 | 7:54 | (Quiz) 90 minutes or 95? | Answer → usable |
| S16 | 8:34 | Did it write well too? | Red underlines → usable with edits |
| S17 | 9:21 | So how many minutes did it save? | Honest “not measured” → everyday work? |
| S18 | 10:01 | What was that opening cursor scene after all? | **Opening clip ② from the start** — foliage question |
| S19 | 10:51 | Is the answer trustworthy? | Actual source panel → “unverified” label → where does the result stay? |
| S20 | 11:36 | Can I use it outside without a laptop? | Muse outside, my 2nd Brain at home → how to choose? |
| S21 | 12:31 | What should guide my choice? | Check four questions |
| S22 | 13:21 | Were initial assumptions right? | Expectations vs reality |
| S23 | 14:06 | So can I delegate or not? | One-sentence conclusion → to learn more |
| S24 | 14:36 | Where are the details? | QR ②; next story (Instinct invitation) |

The flow changes every 60–90 seconds: 0:00 two real reactions → 0:32 timeline → 1:29 video metaphor → 2:52 quiz → 3:22 door-opening video → 4:31 QR → 4:54 actual screen → 6:59 **full opening clip ①** → 7:54 quiz → 8:34 red underlines → 10:01 foliage video + **full opening clip ②** → 10:51 actual source panel → 11:36 outside/home flowchart → 12:31 check-box video → 14:06 conclusion.

**Open loops**: Deliberately cut both opening scenes midway. In S02, promise “the rest from the beginning midway through the video”; resolve ① in S14 (seven minutes) and ② in S18 (ten minutes). A device to reduce mid-video drop-off.

## Chapter Structure

| Chapter | Scenes | Start |
|---|---|---|
| Cold Open + Promise | S01–S03 | 0:00 |
| What Is an Agent? What Are the Four? | S04–S06 | 1:29 |
| Who Can Try Them, and What Needs Care? | S07–S10 | 2:52 |
| Trying Muse Directly | S11–S13 | 4:54 |
| Delegating a Piece of My Work | S14–S17 | 6:59 |
| Everyday Questions — Foliage Recommendations and Bringing Results to My Computer | S18–S20 | 10:01 |
| How Should We Choose? | S21–S23 | 12:31 |
| Outro | S24 | 14:36 |

## Scene-by-Scene Plan

**Scene types**: Add two types for this video to the skill legend (`[TITLE]` `[SECTION]` `[BULLET]` `[WORKFLOW]` `[COMPARE]` `[STAT]` `[TIMELINE]` `[QUOTE]` `[PHOTO_BG]` `[PHOTO+BULLET]` `[AI_IMAGE]` `[AI_VIDEO]` `[OUTRO]`): `[VIDEO]` for full-screen actual recorded clips (livestream edits), and `[QR]` for repository guidance. Quiz scenes overlay a yellow quiz band on the corresponding type (`[COMPARE]`, `[STAT]`).

Visual markers: 🔴 live clip; 🖥️ actual screenshot; 🧩 explanatory reconstruction (label required); 📸 AI image; 🎬 Gemini video. Narration is written for the TTS script (“10월” is written “시월”). 🎙 beside scene titles indicates voice — **Park** = Changsoo Park clone; **Host** = presenter; **Original** = live clip.

### Cold Open + Promise

#### S01 — Two Real Reactions `[VIDEO]` · 0:00 (32 seconds) · 🎙 Original

**Screen**: 🔴 **C1-H** (11 seconds) → quick cut (small “Same day, another scene” label) → 🔴 **C2-H** (20 seconds). Full-screen clips with bottom subtitles. During the first three seconds of clip ①, zoom into the Codex answer and highlight “I performed this process by operating the Muse screen.” In clip ②, add no extra markers so attention follows the self-moving cursor — do not emphasize the upper ““ChatGPT” started debugging this browser” banner, which appears often regardless of Muse (Changsoo Park, Oct 14). Go directly from the final frame to S02 (Changsoo Park, Oct 14 — no three-line preview). **Badge**: Actual screen · AI in Action livestream.

**Narration**: None — only Changsoo Park's real reaction (original audio) and subtitles. See C1-H/C2-H in the “Live Clips” table above for subtitle text.

**Evidence**: [Codex → Muse delegation record](../vl_materials/20261011_codex-muse-browser-delegation.md#관찰한-흐름). Clip ① follows Codex's execution of M4 synthetic task B on Muse's screen.

#### S02 — Four in Two Months `[TIMELINE]` · 0:32 (25 seconds) · 🎙 Host

**Screen**: For the first five seconds, S01's final frame shrinks into a small card at upper left with “We'll replay it → 7 min / 10 min.” Then a horizontal timeline: Aug 11 Grok Bot (xAI), August Instinct (stealth report), Sep 8 Muse (Meta), Sep 29 Dots (OpenAI). Nodes light in sequence; a question mark appears over all four at the end. **Screen label**: Launch dates · 2026 · Some secondary sources.

> What you just saw really happened during a Catch Up AI livestream. I'll replay both scenes from the beginning midway through this video. In just two months, four of these AI agents appeared — AI that takes on work, rather than only answering. So what makes each one different, and what does it take to use them?

**Evidence**: [Service cards](../01-Identify-Services/guides/service-cards.en.md#at-a-glance). Label the Grok Bot launch date and Instinct timing as secondary-source information.

#### S03 — This Video's Promise `[TITLE]` · 0:57 (32 seconds) · 🎙 Park

**Screen**: Title (final choice) / subtitle: Grok Bot · Muse · Dots · Instinct. Four name cards instead of logos. Last six seconds: three badges — “Watch to the end: Four questions before delegating,” “Directly used: One,” “Delegate outside, bring it home.”

> I compared these four using official materials and delegated some of my work to the one I could actually try. Let me say up front: only one of the four was immediately available to me. I'll show exactly why, and what worked and didn't when I used it. I'll also show a way to delegate work to AI while out without a laptop and bring it to my computer at home, along with four questions to ask myself before delegating to an AI agent.

**Evidence**: [Topic README](../README.en.md#key-results).

### What Is an Agent? What Are the Four?

#### S04 — AI That Answers, AI That Works `[COMPARE]` · 1:29 (24 seconds) · 🎙 Host

**Screen**: 🎬 V1 background (task card placed in tray, which glides away). Left: “Chatbot: Gives answers”; right: “Agent: Completes work — browser, files, apps.” On the right card, sequentially add “Continues after the app closes” and “Asks for approval when needed.”

> A chatbot answers questions. An agent goes a step further, using browsers or apps directly to complete work. It continues after the app closes, and when user approval is needed, it asks whether it may proceed, much like seeking sign-off.

**Evidence**: [Agent vs chatbot](../01-Identify-Services/concepts/agent-vs-chatbot.en.md) · [Verified Muse announcement claims](../03-Hands-On/guides/first-task-results.en.md#claims-checked).

#### S05 — Section: What Are the Four? `[SECTION]` · 1:53 (4 seconds)

**Screen**: Section title “What Are the Four?” No narration.

#### S06 — Four Cards `[BULLET]` · 1:57 (55 seconds) · 🎙 Host

**Screen**: Four cards unfold one at a time. Each shows company, one-line description, and where to use it. Only Muse is green; others use gray-blue dashed borders (“Materials only” badge). Light only the card currently being narrated.

| Card | One line | Where to use |
|---|---|---|
| Grok Bot · xAI | A named “AI teammate” with a role works on a dedicated cloud computer | Desktop app, mobile |
| Muse · Meta | A personal assistant handling email, bookings, and forms through conversation | iPhone, Android, web |
| Dots · OpenAI | An “always-on” agent in ChatGPT that keeps working between conversations | ChatGPT desktop, web |
| Instinct · Spear Street Technology | A personal assistant assigned work by text and phone | Text, phone |

> Grok Bot is an “AI teammate” made by xAI. Give it a name and role, and it works across apps on a dedicated cloud computer. Muse is Meta's personal assistant: ask conversationally and it handles email, bookings, and forms. Dots is OpenAI's “always-on” agent inside ChatGPT. Instinct is a personal assistant you assign work to by text and phone rather than an app.

**Evidence**: [Service cards 1–4](../01-Identify-Services/guides/service-cards.en.md). Dots/Instinct descriptions rely substantially on secondary sources; attach “Materials only” badges.

### Who Can Try Them, and What Needs Care?

#### S07 — Quiz: How Many Can I Try Right Away? `[COMPARE]` · 2:52 (30 seconds) · 🎙 Host

**Screen**: Yellow “Quiz” highlight band. Below four cards, “Free? Right now?” cells start empty, pause three seconds, then fill one by one. Grok Bot: paid subscription; Muse: free tier; Dots: ChatGPT Pro or above (my Plus account ✗); Instinct: awaiting invitation.

> Here's a question. How many of these four could I try right now without paying for anything new? ... Grok Bot needs a paid subscription. Dots requires ChatGPT Pro or above, so I couldn't use it with Plus. Instinct requires an invitation, and I'm still on the waitlist. Muse was the only one I could try immediately for free.

**Evidence**: [Practice decisions](../02-Comparison-Table/guides/comparison-table.en.md#practice-decisions-for-this-topic).

#### S08 — Three Locked Doors, One Open Door `[STAT]` · 3:22 (24 seconds) · 🎙 Park

**Screen**: 🎬 V2 background (four doors, one opens). Four locked doors, one open (new technique) → large “1 / 4.” Small text below: “The other three compared through official materials only.”

> So here's how this comparison works. I tried Muse directly and compared the other three through official materials only. I won't evaluate services I haven't used as though I had.

**Evidence**: [Evidence level by service](../05-Decision-Guide/guides/which-agent-when.en.md#evidence-level-by-service).

#### S09 — Delegation Means Handing Over Authority `[PHOTO+BULLET]` · 3:46 (45 seconds) · 🎙 Host

**Screen**: 📸 I1 right-hand card (hands passing key). Left, four approval methods appear sequentially: Grok Bot — draft approval before sending; Muse — allow/ask per action; Dots — user defines scope of independent action (secondary); Instinct — **agent under its terms** (red warning icon). **Screen label**: Official docs/terms / Dots uses secondary sources.

> Delegating work to an agent can also mean handing over permission to touch your email or calendar. That is why services differ in when they ask a person. In particular, Instinct's terms designate it as your agent, so commitments made on your behalf may bind you. That's a reason to read the terms before delegating.

**Evidence**: [Comparison ④ Privacy/approval](../02-Comparison-Table/guides/comparison-table.en.md#at-a-glance) · [Approval boundaries and privacy](../02-Comparison-Table/concepts/approval-and-privacy.en.md) · [Instinct terms verification](../vl_materials/official-sources.md#instinct-spear-street-technology).

#### S10 — You Don't Have to Remember Everything · QR ① `[QR]` · 4:31 (23 seconds) · 🎙 Park

**Screen**: Left, blurred comparison-table thumbnail (4 × 5); right, large QR + short URL + “Comparison, official sources, practice records (Korean).”

> You don't need to remember all the pricing, regional, and privacy conditions. I've organized the comparison and official sources for all four services into Korean documents and published them on GitHub. Use the QR code on screen. Pricing and conditions change often, though, so check the official screens again immediately before using them.

**Evidence**: [Comparison table](../02-Comparison-Table/guides/comparison-table.en.md) · [Official source list](../vl_materials/official-sources.md).

### Trying Muse Directly

#### S11 — What “Ask for Some Actions” Really Means `[PHOTO+BULLET]` · 4:54 (50 seconds) · 🎙 Park

**Screen**: 🖥️ R1 → R2 → R3 · R4 sequentially inside cards (account-specific values already masked). Text on the right (keep menu names in English — Changsoo Park, Oct 14): “Data controls → Help improve our AI models” → “Default: Ask for some actions — asks only before important actions; select Always ask to ask every time” → “Gmail · Calendar — separate Read / Write and delete permissions.” Narration also reads menu names in English. **Badge**: Actual screen · 2026-10-11 · Personal settings masked.

> The first thing I looked at after opening Muse was Settings. Under Data controls, there was a separate Help improve our AI models option for choosing whether my conversations could be used for AI training. The default on the Permissions screen was Ask for some actions. This means it asks only before sharing my information or changing something important, and does the rest without asking. To make it ask before every action, you need to select Always ask separately. Gmail and Calendar separate Read permissions from Write and delete permissions by action, so you need to check each one.

**Evidence**: [Concepts observed in settings](../03-Hands-On/guides/first-task-results.en.md#concepts-observed-in-settings) · [Muse first web use](../03-Hands-On/guides/setup-muse.en.md).

#### S12 — Can We Trust an Answer with Source Links? `[PHOTO_BG]` · 5:44 (40 seconds) · 🎙 Park

**Screen**: 🖥️ R5 Sources panel slowly zooms with a Ken Burns effect → “Third-party material” labels attach to domains → “Ask again for official materials” → two cards enter: Meta announcement and help.

> I asked Muse to research Muse itself. Its answer had a Sources list, but the sources initially shown were mainly news outlets and summary sites. Only after I asked again for official materials did it bring back Meta's announcement and help pages. Having source links and having trustworthy sources are different things.

**Evidence**: [Public-material research and source verification](../03-Hands-On/guides/first-task-results.en.md#public-material-research-and-source-verification).

#### S13 — It Miscounted the Time at First `[WORKFLOW]` · 6:24 (35 seconds) · 🎙 Park

**Screen**: 📸 I2 first three seconds (numberless clock and blank timetable) → 🧩 three-stage explanatory reconstruction: ① Request “Summarize today's schedule” → ② Counts already elapsed time as free (✗) → ③ Ask again “From now onward, Seattle time” → corrected (✓). **Badge**: Explanatory reconstruction — real schedule values are not disclosed.

> Next I asked for a summary of my schedule. The first answer counted time that had already passed as free time. When I asked again, “From now onward, in Seattle time,” it corrected the result. Even if the first answer looks plausible, calculations involving dates and time zones need another check.

**Evidence**: [First task: read-focused schedule summary](../03-Hands-On/guides/first-task-results.en.md#first-task-read-focused-schedule-summary).

### Delegating a Piece of My Work

#### S14 — It Turned Out AI Entered It `[VIDEO]` · 6:59 (55 seconds) · 🎙 Park + Original

**Screen**: Two task cards first (10 seconds): A “Review event timetable,” B “Broadcast notes → video description”; below, “All fictional materials · No email/calendar connections.” Then 🔴 **C1-F** (about 36 seconds, original audio + subtitles), full screen. Brief “That opening scene” label at the opening cutoff (“It entered that?”). At clip end, baton handoff — task card flies from VS Code window into browser window (nine seconds, closing narration). Label the clip's “ChatGPT plugin” and “Claude too” portions “Speculation during broadcast” beside subtitles. **Badge**: Actual screen · Livestream.

> (Before clip) This time I assigned two tasks resembling my real work. To keep personal information out, I made all the materials fictional. But while looking at the results, something surprised me.
>
> (After clip) A task I thought I'd typed myself had actually been entered into Muse by Codex directly operating the browser. It had even captured and organized the results. So how well did Muse do?

**Evidence**: [Task cards](../04-Real-Task-Trial/examples/task-cards.en.md) · [Topic README — Capstone video](../README.en.md#capstone-video). “Possible through the ChatGPT plugin” was live speculation; do not assert it in narration.

#### S15 — Quiz: 90 Minutes or 95? `[STAT]` · 7:54 (40 seconds) · 🎙 Host

**Screen**: Yellow “Quiz” band. Draw five fictional timetable rows (09:00–10:30) as bars. Mark the five-minute overlap at 09:35–09:40 between “Short talk 09:10–09:40” and “Tool demo 09:35–10:00” in red. Question “Total time?”; pause three seconds → count up “90 minutes start to finish,” “95-minute item total,” “Five-minute difference = overlap.” Finish with a green “Usable” stamp.

> Two items overlap in this timetable. So is the event's total duration 90 minutes or 95? ... Both are right. It's 90 minutes from first start to final end, and 95 when you add the item durations; that five-minute difference is the overlap. Muse distinguished all three correctly and left the schedule untouched. I judged this task “usable.”

**Evidence**: [Task A — fictional event timetable](../04-Real-Task-Trial/guides/trial-results.en.md#task-a--fictional-event-timetable). Use the timetable exactly as in the task card. “Tool demo” starts at 09:35.

#### S16 — The Format Was Right, But… `[COMPARE]` · 8:34 (47 seconds) · 🎙 Park

**Screen**: 🖥️ R6 card (Muse's revised answer). Left, “Format ✓”: title, 100–140 words, three bullets, three hashtags. Right, “Evidence ✗”: red wavy underlines (new) under original English phrases + Korean meanings — “the plants thrive with less fuss” (plants grow well with less care), “your balcony can become a small refuge for pollinators” (a small refuge for bees), and, even after revision, “a small, gentle start.” Finish with amber “Usable with edits” stamp.

> The second task was writing. Title, length, bullets, hashtags — the format was all correct. But it added things absent from my notes: claims such as “plants thrive” and “the balcony becomes a refuge for bees,” effects not in the material I supplied. Even after one revision request, similar wording remained. So this task is “usable with edits.” Delegate the draft, but a person must do the final editing.

**Evidence**: [Task B — fictional broadcast description](../04-Real-Task-Trial/guides/trial-results.en.md#task-b--fictional-broadcast-description). Use only original phrases recorded in the results document.

#### S17 — So How Many Minutes Did I Save? `[QUOTE]` · 9:21 (40 seconds) · 🎙 Park

**Screen**: 📸 I3 background at 30% (single specimen jar on shelf). Large central text “I didn't measure it” → three lines below: one service, two synthetic tasks, no timing → “So I won't claim rankings or time savings.”

> You might ask how much time I saved. Honestly, I didn't measure it. I didn't separately record how long I waited for Muse or how long I spent editing. With one service and two synthetic tasks, I won't use these results to rank services or claim time savings. Next experiment, I'll turn on the timer first.

**Evidence**: [Human review cost](../04-Real-Task-Trial/guides/trial-results.en.md#human-review-cost) · [Scope and limitations](../README.en.md#scope-and-limitations).

### Everyday Questions — Fall Foliage Recommendations in Korean

#### S18 — That Opening Scene, from the Beginning `[VIDEO]` · 10:01 (50 seconds) · 🎙 Park + Original

**Screen**: 🎬 V3 first three seconds (Puget Sound foliage forest) → one narration sentence (six seconds) → 🔴 **C2-A** (33 seconds, original + subtitles), full screen. “That opening scene” label at the opening cutoff (“This seems to have tremendous potential”). After the clip, baton-handoff animation from VS Code to browser during eight-second closing narration.

> (Before clip) Here's that scene from the opening, this time from the beginning. This was the day I asked where to see fall foliage.
>
> (After clip) All I did was ask Codex in Visual Studio Code in one sentence. Codex operated the browser screen just as a person would and entered the question into Muse.

**Evidence**: [Request and result](../vl_materials/20261011_codex-muse-browser-delegation.md#요청과-결과) — “An example of operating the browser UI, rather than implementing a separate API integration.”

#### S19 — Can We Trust the Answer as Is? `[VIDEO]` + `[BULLET]` · 10:51 (45 seconds) · 🎙 Original + Park

**Screen**: 🔴 **C2-B** (13 seconds, original + subtitles) — Muse's Korean answer → Sources panel opens. Then enlarge 🖥️ R7, circle ⚠️ “Current observed conditions unverified” → three lines: “Sources are visible — still check directly,” “Foliage conditions, weather, closures — mark unverified,” “Ask and receive answers in Korean — works.” Below, one original livestream quotation styled as a quote (attribution: “Catch Up AI livestream”).

> (After clip) Muse answered in Korean with five places, driving times, and walking difficulty, and showed where the information came from in Sources. A good point was that it marked places whose foliage conditions it hadn't checked as “unverified.” Still, as you saw earlier, visible sources don't mean you can trust everything; check weather and road closures yourself before going.

**On-screen quotation (original, translated here)**: “What impressed me was asking Codex in VS Code to do a task, then seeing Codex go to the browser and assign work to Muse.” — Catch Up AI livestream (2026-10-11)

**Evidence**: [Request and result](../vl_materials/20261011_codex-muse-browser-delegation.md#요청과-결과) · [Public-material research and source verification](../03-Hands-On/guides/first-task-results.en.md#public-material-research-and-source-verification) (connects to S12). Use the exact original quotation in the delegation record. The senior-training demonstration discussion was removed to make room for S20.

#### S20 — Muse Outside, My 2nd Brain at Home `[WORKFLOW]` + `[COMPARE]` · 11:36 (55 seconds) · 🎙 Park

**Screen**: Two parts.
① **Comparison with remote control** (15 seconds) — 📸 I5 background (outside left, home right); left card: “Remote access: leave home computer on and operate it from outside” (method recently investigated); right card: “Delegate to Muse outside, bring results home.” Right card comes forward.
② **Three-step flowchart** (40 seconds) — 🧩 explanatory reconstruction: ① **Outside** — assign work to Muse on the phone (research, organization, drafting) → ② **Results accumulate in Muse** (my computer can be off) → ③ **At home** — turn on computer and ask Codex, “Save Muse's results in my vault” → **Keep them as documents in my computer's 2nd Brain (vault)**. Beside ③, show 🔴 C2-C as a small card for four seconds (muted, path blurred) — the actual saving of the foliage answer to the vault. End with small label “Tried once · Not automatic synchronization.”

> After this scene, I had Codex save Muse's answer as a document in my computer's notes folder. That made me think. Until recently, I'd been looking into remotely controlling my home computer while away. With this approach, I might not need to. When my laptop isn't with me, I can assign work to Muse on my phone, then bring that work to my computer when I return home and turn it on. That way, work done in spare moments outside gradually accumulates in my second brain on my computer. I've only tried it once, and the transfer isn't automatic, but I think it's a path worth trying.

**Evidence**: [Delegation record — related records](../vl_materials/20261011_codex-muse-browser-delegation.md#관련-기록) (foliage answer saved as an everyday-reference document in the vault) · clip 2, 1:08–1:43 (live speech) · Changsoo Park's 2026-10-14 explanation (verbatim in personal journal) · remote-access comparison: [Chrome-Remote-Desktop topic](../../Chrome-Remote-Desktop/README.md). Always say both “not automatic synchronization” and “tried once” — Codex read Muse's result in the browser and saved it.

### How Should We Choose?

#### S21 — Four Questions Before Delegating `[WORKFLOW]` · 12:31 (50 seconds) · 🎙 Park

**Screen**: 🎬 V4 first four seconds (pen checks four empty boxes) → four decision stages appear sequentially: ① Can I use it now? (plan, region, invitation) ② Does it need personal/customer data? → minimize or make fictional ③ Does it send or change anything externally? → draft only if hard to reverse ④ Can I verify results? → if not, limit to drafts/questions. Light only the narrated stage.

> So I decided to ask four questions before delegating to an agent. First, can I really use this service now? Second, does it need personal data? If so, can I reduce it or replace it with fictional material? Third, does it do something externally, like sending email or changing a schedule? If it's hard to reverse, I delegate only the draft. Fourth, can I check whether the result is right? If I can't, I accept it only as a draft, not a conclusion.

**Evidence**: [Four checks before choosing](../05-Decision-Guide/concepts/selection-criteria.en.md#four-checks-before-choosing) · [Decision flowchart](../05-Decision-Guide/guides/which-agent-when.en.md#decision-flowchart).

#### S22 — Initial Expectations and Reality `[COMPARE]` · 13:21 (45 seconds) · 🎙 Host

**Screen**: Three-row table, spotlight cycling by row — “It'll calculate schedules well” → first answer wrong; accurate after asking again / “It'll follow the notes” → format right; unsupported wording remained / “Comparing four on the same tasks will make choosing easy” → only one could actually be used.

> Initial expectations differed from reality. I assumed time calculations would be easy, but it needed a clear reference. I thought the writing would follow instructions, but it added things that weren't there. And I thought comparing four side by side would make choosing easy, but only one was available to try.

**Evidence**: [Initial expectations and practice results](../05-Decision-Guide/guides/which-agent-when.en.md#initial-expectations-and-practice-results).

#### S23 — Delegate, but Let a Person Verify `[AI_IMAGE]` · 14:06 (30 seconds) · 🎙 Park

**Screen**: 📸 I4 background at 30% (hand gives folder to robotic arm; person keeps approval stamp). Highlight central sentence “Delegate, but let a person verify.” Small question below: “What would you like to delegate?”

> AI agents certainly do work. But for now, deciding the scope and checking the results remain human responsibilities. What would you like to delegate to an agent? Let me know in the comments.

**Evidence**: [M5 selection guide summary](../README.en.md#selection-guide).

### Outro

#### S24 — Details on GitHub · QR ② `[OUTRO]` · 14:36 (38 seconds; QR held at least 8 seconds) · 🎙 Park

**Screen**: Large QR + URL + “Comparison, official sources, practice records, decision flowchart (Korean).” Two small lines below: “Continuing to share what I learn using Muse” / “Follow-up practice when Instinct invitation arrives.” Ending music synthesized in code.

> All the comparison tables, official sources, practice records, and decision flowchart shown today are publicly available on GitHub in Korean. Use the QR code on screen or the link in the description. In fact, I've only installed Muse and tried its basic features so far. I'll keep using it and share what I learn along the way. When an Instinct invitation arrives, I'll return with a story of trying that directly too.

**Evidence**: [Topic README](../README.en.md).

## YouTube Description Draft

```
I compared four new AI agents (Grok Bot, Muse, Dots, Instinct) using official materials, then assigned two synthetic tasks and an everyday question to Muse, the one I could actually use. This also includes livestream scenes of Codex in VS Code directly operating Muse in the browser, and a way to bring work assigned to Muse while outside back to my computer at home.

📂 Comparison, official sources, practice records, decision flowchart (Korean)
https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/AI-Agent-Apps-Compare

※ I've only installed Muse and tried its basic features so far; I'll keep sharing what I learn through continued use. Muse is the only service directly tested, and tasks used synthetic data. Pricing and access may change; check official screens before use. (As of October 2026)
```

## Decisions Before Finalization

| # | Question | Default/status |
|---|---|---|
| 1 | Title | Candidate 1 (“AI Put Another AI to Work” — best match for opening reactions) |
| 2 | Live clips | ✅ Confirmed Oct 14 — C1-H/C2-H (hooks), C1-F (S14), C2-A (S18), C2-B (S19). Word-level segment boundaries; adjust only 0.5 seconds at either end in preview |
| 3 | Changsoo Park voice clone | ✅ Use, Oct 14 — 15 first-person scenes, alongside presenter voice |
| 4 | Instinct waitlist status | Say “waiting” |
| 5 | Approximately 15 minutes | To shorten, consider merging S12/S22 |
| 6 | Presenter voice for S02's “Catch Up AI livestream” introduction? | Default — presenter introduces; Changsoo Park voice from S03 |

## Next Steps After Approval

1. ✅ Write `image-prompts.md` (I1–I5) and `video-prompts.md` (V1–V4), Oct 14.
2. User generates images/Gemini videos → `AI/RemotionStudio/public/agent-apps-compare-1013/images/`. Copy the two live-clip files into `clips/` (set segments in Remotion).
3. Build Remotion scenes (codex-design-lessons checklist/contact sheet) → Studio review.
4. edge-tts draft (check two-voice rhythm) → approval → Qwen3-TTS (presenter preset + Changsoo Park clone) → approval → align clip subtitles → render.
5. Link video in Topic README, Final Retrospective, `check_links.py`.
