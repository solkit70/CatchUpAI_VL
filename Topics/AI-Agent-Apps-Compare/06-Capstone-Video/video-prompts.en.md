---
title: "Comparing Four New AI Agents — Gemini Video Prompts"
video-id: agent-apps-compare-1013
created: 2026-10-14 12:30:00
tags:
  - remotion
  - ai-agent-apps-compare
  - video-prompts
  - gemini-veo
---

# Video Clip Prompts (Gemini / Veo)

[한국어](video-prompts.md)

> Each prompt is **ready to use by copying a single block**.
> Aspect ratio, duration, what moves, fixed camera, brightness, colors, and exclusions are all inside the block.

## ⚠️ Tool Settings

| Item | Setting |
|---|---|
| Tool | Veo in the Gemini app or Google AI Studio (do not generate via API) |
| Aspect ratio | **Select 16:9 directly in the UI** |
| Duration | Gemini app defaults to 8 seconds; blocks also specify 8 seconds. If a scene is longer, freeze the final frame in Remotion (do not slow it down) |
| Sound | Insert **muted** even if sound is generated — narration is separate |

## Shared Rules (Reference Only — Already Included in Every Block)

- Brightness band **L2 moderately bright** (pastel). Pastel sky blue `#E6EEF6`, pale green `#EEF3EA`, forest green `#2F7D5B`, amber `#C77712`.
- **Fixed camera**; only objects within the frame move. **No people** (hands also removed in response to refusals).
- Save in `AI/RemotionStudio/public/agent-apps-compare-1013/images/` using the exact filenames below.

| File | Scene | Usage |
|---|---|---|
| `v1_task_tray.mp4` | S04 AI That Answers, AI That Works | Full-screen background + light gradient behind left-side text |
| `v2_four_doors.mp4` | S08 Three Locked Doors, One Open Door | Full-screen background → “1 / 4” overlaid |
| `v3_fall_maples.mp4` | S18 That Opening Scene, from the Beginning | First 3 seconds full screen → live clip |
| `v4_four_checks.mp4` | S21 Four Questions Before Delegating | First 4 seconds → decision flowchart |

## ⚠️ Responding to Gemini Refusals (2026-10-14)

Gemini **refused v1 with “I can't generate that video”** when given the original long prompt (sections such as FORMAT, CAMERA, STYLE, DO NOT INCLUDE; color hex codes; body-part exclusion lists such as “no faces, heads, bodies”). It does not explain the precise reason. All four prompts were therefore rewritten as **short natural-language paragraphs**.

- Removed section titles, uppercase warnings, and hex codes. Colors are described in words (e.g., soft pastel blue).
- **Removed exclusion sentences listing body parts.** Scenes not requiring people were changed to show only moving objects, with no people at all (v1, v4).
- Kept essential conditions (16:9, 8 seconds, fixed camera, what moves, no text, empty space for overlays, brightness) inside sentences — the single-copyable-block principle remains.
- If still refused, use the “shorter alternative” below the block.

## v1_task_tray.mp4 — S04 “AI That Answers, AI That Works,” Background

```
A calm, bright, photorealistic 8-second video in 16:9 widescreen. The camera stays completely still the whole time.

A light oak desk in a sunny, modern home office with a soft pastel blue wall. On the right side of the desk, a blank white paper card slides gently into a shallow white tray, and then the tray glides slowly away toward the back of the desk, as if the task has been handed off. Nothing else moves.

The left half of the frame is a plain, empty pastel wall and desk, leaving space for text. Soft natural daylight from the right, light and airy pastel blue and sage green tones, a few small forest green accents. No people, no writing on the card, no text, no logos.
```

**Shorter alternative**

```
Photorealistic 8-second 16:9 video, static camera. On a bright light oak desk against a pastel blue wall, a blank white card slides into a white tray, and the tray slowly glides away to the back of the desk. Left half of the frame stays empty. Soft daylight, airy pastel tones, no people, no text.
```

## v2_four_doors.mp4 — S08 “Three Locked Doors, One Open Door,” Background

```
A calm, bright, photorealistic 8-second video in 16:9 widescreen. The camera stays completely still, centered and symmetrical.

A short, minimal hallway with soft pastel blue walls and a pale sage green floor. Four identical light gray doors stand side by side on the far wall. Three of them stay closed. Only the second door from the right slowly swings open, and warm golden daylight spills out across the floor. Nothing else moves.

The wall above the doors is plain and empty, leaving space for a large number. Soft, even daylight, hopeful mood. No people, no signs, no numbers or writing on the doors, no text, no logos.
```

**Shorter alternative**

```
Photorealistic 8-second 16:9 video, static centered camera. A bright pastel hallway with four identical gray doors. Three stay closed; the second door from the right slowly opens and warm daylight spills out. Plain wall above the doors. No people, no text.
```

## v3_fall_maples.mp4 — S18 Opening “Fall Foliage”

```
A calm, photorealistic 8-second nature video in 16:9 widescreen. The camera stays completely still on a tripod.

A quiet forest walking path in Washington State in autumn, lined with maple trees in warm amber, red-orange and gold, with a few tall evergreen fir trees behind them. The path is covered with fallen leaves. A light breeze moves the branches slightly and a few red and amber leaves drift slowly down onto the path.

Bright, soft overcast daylight, clearly lit and peaceful. The lower left part of the path is calm and uncluttered. No people, no animals, no signs, no text.
```

**Shorter alternative**

```
Photorealistic 8-second 16:9 video, static camera. A Pacific Northwest forest path in autumn with red and amber maple trees and evergreen firs; a few leaves drift down in a light breeze. Bright overcast daylight. No people, no text.
```

## v4_four_checks.mp4 — S21 Opening “Four Questions Before Delegating”

```
A bright, photorealistic 8-second video in 16:9 widescreen, filmed from directly above. The camera stays completely still.

A clean sheet of off-white paper lies on a light oak desk. On the left side of the paper is a vertical column of four empty square checkboxes with blank space beside them. One by one, from top to bottom, a neat forest green check mark appears in each box, as if drawn by an invisible pen. Nothing else moves.

The right side of the frame is plain empty desk, leaving space for text. Soft daylight from the upper left, airy pastel blue and sage green tones. No people, no words or numbers on the paper, no text, no logos.
```

**Shorter alternative**

```
Photorealistic 8-second 16:9 top-down video, static camera. A sheet of paper on a light oak desk with four empty checkboxes in a column; a green check mark appears in each box one by one. Right side of the frame stays empty. Soft daylight, pastel tones, no people, no text.
```

## ✅ Self-Check

- [x] Every block specifies 16:9, 8 seconds, photorealistic, and fixed camera within sentences (resolution/fps omitted because Gemini determines them)
- [x] Sentences specify what moves; everything else is covered by “Nothing else moves”
- [x] Colors described in words instead of hex codes (in response to Gemini refusals); brightness expressed as “bright, airy, soft daylight”
- [x] Empty space for text overlays specified
- [x] Ends with the single line “No people, no text” — no body-part exclusion lists
