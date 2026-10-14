---
title: "Comparing Four New AI Agents — Image Prompts"
video-id: agent-apps-compare-1013
created: 2026-10-14 12:30:00
tags:
  - remotion
  - ai-agent-apps-compare
  - image-prompts
---

# Image Prompts

[한국어](image-prompts.md)

> Each prompt is **ready to use by copying a single block**.
> Aspect ratio, resolution, style, brightness, colors, empty space, and exclusions are all inside the block. **Do not trim it.**

## ⚠️ Tool Settings (Not Controlled by Prompts)

| Tool | Aspect ratio |
|---|---|
| ChatGPT | Generally follows the aspect ratio specified in the prompt |
| Gemini | **Select the aspect ratio directly in the UI** (16:9 or 4:5). Prompt instructions often do not work |
| Copilot | No aspect-ratio selection (3:2); watermark at upper right → crop the top 80px to use it |

## Shared Rules (Reference Only — Already Included in Every Block)

- Brightness band **L2 moderately bright** (pastel). Pastel sky blue `#E6EEF6` and pale green `#EEF3EA` backgrounds; forest green `#2F7D5B` and amber `#C77712` accents.
- Show **hands only** for people. No faces, on-screen text, or logos.
- Save in `AI/RemotionStudio/public/agent-apps-compare-1013/images/` using the exact filenames below.

| File | Scene | Aspect ratio | Usage |
|---|---|---|---|
| `i1_key_handoff.png` | S09 Delegation Means Handing Over Authority | 4:5 portrait | Right-hand card |
| `i2_clock_timetable.png` | S13 It Miscounted the Time at First | 16:9 | Full screen for first 3 seconds |
| `i3_single_specimen.png` | S17 So How Many Minutes Did I Save? | 16:9 | Background at 30% opacity |
| `i4_handoff_review.png` | S23 Delegate, but Let a Person Verify | 16:9 | Background at 30% opacity |
| `i5_outside_home.png` | S20 Muse Outside, My 2nd Brain at Home | 16:9 | Background behind comparison cards |

## i1_key_handoff.png — S09 “Delegation Means Handing Over Authority,” Right-Hand Card

```
OUTPUT FORMAT — 4:5 vertical portrait, 1080x1350 or larger.
Compose for 4:5. Do not output square or landscape. No letterboxing, no borders,
no frame, no white margin — the image must fill the entire canvas edge to edge.

STYLE — Photorealistic cinematic still photograph, shallow depth of field, soft
natural textures. Calm, trustworthy mood. Color palette: soft sky-blue pastel
(#E6EEF6) and pale sage green (#EEF3EA) in the background, warm light oak wood,
a small polished brass object as the single warm accent. Subtle film grain,
gentle contrast, nothing harsh or dramatic.

LIGHTING — Warm daylight fills the room. Mid-tone overall, clearly lit —
brighter than a typical interior photograph. Single-direction soft window light
from the left. Shadows are soft and short.

SCENE — Close-up over a light oak desk: one person's hand gently places a small
old-fashioned brass key into another person's open palm. Only hands and wrists
are visible, with plain light-colored sleeves (one pale blue, one off-white).
The handoff is careful and deliberate, as if trusting someone with something
important. Background is a softly blurred bright room with a window.

COMPOSITION — The two hands and the key sit in the lower-middle third of the
frame. Keep the top third calm and softly blurred (plain pastel background) so a
small label can be placed there later. Key in sharp focus.

ABSOLUTELY NO faces, no heads, no full bodies. NO text, letters, numbers,
logos, watermarks, signatures or labels anywhere in the image. No jewelry
brand marks. No dark or moody lighting.
```

## i2_clock_timetable.png — S13 “It Miscounted the Time at First,” First 3 Seconds

```
OUTPUT FORMAT — 16:9 widescreen landscape, 1920x1080 or larger.
Compose for 16:9. Do not output square or 3:2. No letterboxing, no borders,
no frame, no white margin — the artwork must fill the entire canvas edge to edge.

STYLE — Photorealistic cinematic still photograph, clean and minimal, soft
natural textures. Color palette: soft sky-blue pastel wall (#E6EEF6), pale sage
green accents (#EEF3EA), white paper, a thin forest-green clock rim (#2F7D5B).
Gentle contrast, subtle film grain.

LIGHTING — Warm daylight fills the room. Mid-tone overall, clearly lit —
brighter than a typical interior photograph. Soft light from the left, faint
soft shadow of the clock on the wall.

SCENE — A simple round wall clock hangs on a pale blue wall. The clock face has
NO numerals and no markings except twelve tiny plain tick marks; the hands point
to roughly 9:40. Below it, on a light wooden desk in the foreground, lies a
blank paper sheet printed with an empty grid of horizontal rows and colored
blocks (like a day planner), but every cell is empty — no writing at all.

COMPOSITION — Clock in the upper-right area, paper grid in the lower-right.
Keep the left 40% of the frame plain pastel wall with nothing in it, so text
can be placed there later.

CRITICAL — NO TEXT: Do not render any text anywhere in the image. No numbers on
the clock, no times, no names, no labels, no letters, no legend, no watermarks,
no signature. All labels will be added separately in post-production.
No people, no hands.
```

## i3_single_specimen.png — S17 “So How Many Minutes Did I Save?”, 30% Background

```
OUTPUT FORMAT — 16:9 widescreen landscape, 1920x1080 or larger.
Compose for 16:9. Do not output square or 3:2. No letterboxing, no borders,
no frame, no white margin — the artwork must fill the entire canvas edge to edge.

STYLE — Photorealistic minimal still life, quiet and honest mood, museum-like
calm. Color palette: soft sky-blue pastel (#E6EEF6) wall, pale sage green
(#EEF3EA) shelf, clear glass with a faint forest-green (#2F7D5B) tint.
Very clean, lots of empty space, subtle film grain.

LIGHTING — Warm daylight fills the room. Mid-tone overall, clearly lit —
brighter than a typical interior photograph. Soft even light from the left.

SCENE — A long, simple wooden wall shelf, almost entirely empty. Exactly ONE
small clear glass specimen jar with a cork lid sits on the shelf, holding a
single small green leaf. The rest of the shelf is bare. The feeling: one small
sample, nothing more.

COMPOSITION — The jar sits slightly left of center on the shelf at mid-height.
Large calm empty space above and to the right. The image will be shown at 30%
opacity behind large text, so keep it simple, soft and low in detail.

CRITICAL — NO TEXT: Do not render any text anywhere in the image. No labels on
the jar, no letters, no numbers, no logos, no watermarks, no signature.
No people, no hands.
```

## i4_handoff_review.png — S23 “Delegate, but Let a Person Verify,” 30% Background

```
OUTPUT FORMAT — 16:9 widescreen landscape, 1920x1080 or larger.
Compose for 16:9. Do not output square or 3:2. No letterboxing, no borders,
no frame, no white margin — the artwork must fill the entire canvas edge to edge.

STYLE — Photorealistic cinematic still photograph, warm and reassuring, soft
natural textures. Color palette: soft sky-blue pastel (#E6EEF6) and pale sage
green (#EEF3EA) background, a sleek white robotic arm with soft gray joints, a
manila folder, a wooden rubber stamp with a forest-green (#2F7D5B) handle, and
a warm amber (#C77712) accent on the stamp pad. Subtle film grain.

LIGHTING — Warm daylight fills the room. Mid-tone overall, clearly lit —
brighter than a typical interior photograph. Soft light from the left.

SCENE — On a light oak desk, a person's hand passes a closed manila folder to a
small, friendly white desktop robotic arm, which gently grips it. On the right
side of the desk, the person's other hand rests on a wooden rubber stamp next to
an ink pad, ready to approve — the human keeps the final say. Only hands and
forearms are visible, plain light sleeves.

COMPOSITION — Folder handoff in the left-center, stamp in the lower-right.
Keep the center and upper area calm and slightly blurred: this image will be
shown at 30% opacity behind one large line of text in the middle.

ABSOLUTELY NO faces, no heads, no full bodies. CRITICAL — NO TEXT: no writing
on the folder, no letters on the stamp, no numbers, no logos, no brand marks on
the robot, no watermarks, no signature. Do not make the robot humanoid or scary.
```

## i5_outside_home.png — S20 “Muse Outside, My 2nd Brain at Home,” Background

```
OUTPUT FORMAT — 16:9 widescreen landscape, 1920x1080 or larger.
Compose for 16:9. Do not output square or 3:2. No letterboxing, no borders,
no frame, no white margin — the artwork must fill the entire canvas edge to edge.

STYLE — Photorealistic cinematic photograph made of two halves joined by a soft
vertical gradient (not a hard line), telling one story: away from home, then
back home. Color palette: soft sky-blue pastel (#E6EEF6), pale sage green
(#EEF3EA), autumn leaves in warm amber (#C77712) and red-orange, a forest-green
(#2F7D5B) accent. Subtle film grain, gentle contrast.

LIGHTING — Warm daylight fills the room. Mid-tone overall, clearly lit —
brighter than a typical interior photograph. Left half: bright overcast autumn
daylight outdoors. Right half: warm late-afternoon light through a window
indoors. Both halves are similarly bright.

SCENE — LEFT HALF: outdoors on a park path in the Pacific Northwest in autumn,
maple trees with red and amber leaves, a person's hand holding a smartphone
(screen turned slightly away so nothing on it is readable, only a soft glow).
RIGHT HALF: a calm home desk by a window, an open laptop (screen shows only a
soft blank glow, nothing readable), a cup of tea, and a small stack of
notebooks — a quiet place where everything is kept. No person visible on the
right, or only a hand resting near the laptop.

COMPOSITION — Keep the upper 30% of both halves fairly plain (sky and wall) so
two short labels can be placed above each half later. The middle blend zone
should be soft and uncluttered.

ABSOLUTELY NO faces, no heads, no full bodies. CRITICAL — NO TEXT: nothing
readable on the phone or laptop screens, no app icons, no logos, no letters,
no numbers, no watermarks, no signature.
```

## ✅ Self-Check

- [x] Every block starts with `OUTPUT FORMAT` (aspect ratio, resolution, no margins)
- [x] Full STYLE repeated in every block (including color hex codes)
- [x] LIGHTING includes the L2 sentence
- [x] Shots with people (i1, i4, i5) explicitly specify “hands only” within the block
- [x] COMPOSITION specifies empty space for shots with text overlays
- [x] Exclusions (faces, text, logos, watermarks)
- [x] Removing the Korean guidance outside the blocks does not change the result
