---
title: "Claude Artifacts and Routines — Photorealistic Image Prompts (I1–I6)"
created: "2026-10-06 09:40:00"
author:
  - "Claude Code"
tags:
  - remotion
  - image-prompts
  - claude-artifacts-routines
status: "ready-for-generation"
---

## How to use

These are six photorealistic image prompts from the [slide plan v3](video-slide-plan_en.md). Copy one code block into gpt-image-2; aspect ratio, colors, lighting, text-safe area, and exclusions are specified inside each prompt. Save generated files to `AI/RemotionStudio/public/claude-artifacts-routines-1004/images/` with the names below.

| ID | Scene | Filename | Use |
|---|---|---|---|
| I1 | (deferred) | `i1_s04_hands_notes.png` | v4 replaces S04 with an actual YouTube thumbnail; generation is optional (backup). |
| I2 | S06 | `i2_s06_empty_booths.png` | Small card on the right |
| I3 | S15 | `i3_s15_phone_glow.png` | Card on the right |
| I4 | S17 | `i4_s17_four_envelopes.png` | Number “4” over blurred background |
| I5 | S18 | `i5_s18_cracked_funnel.png` | Three-second opening cut |
| I6 | S24 | `i6_s24_hands_laptop_dusk.png` | Background at 30% opacity |

Common rules: do not depict actual screen UI (screens stay off or show only blurred light); show people only from the hands down; include no text—Remotion adds all text.

## I1 — Hands Taking Notes (S04)

```text
Photorealistic cinematic photograph, landscape 3:2, 1536x1024 resolution. The final video frame is 16:9 (1920x1080): keep all important content inside the central horizontal band, nothing important in the top and bottom 8%.

SCENE: Over-the-shoulder close view of a person's two hands at a light wooden desk, one hand writing with a pen on a printed sheet of paper, a few other printed sheets loosely stacked beside it, a closed notebook and a mug. The person is researching new career options at home. Only hands and forearms are visible.

LIGHT: Soft natural daylight from a window on the LEFT, cool morning tone, gentle shadows falling to the right.

COLOR PALETTE: cool off-white paper and walls close to #F3F5FA, deep shadow tones toward #161D33, one small accent object (the pen) in coral #E0572B. Overall bright, airy, low contrast.

COMPOSITION FOR TEXT OVERLAY: hands and papers on the LEFT 45% of the frame; the RIGHT 55% is a calm, softly out-of-focus desk surface and wall with no objects — a quotation card will be placed there. Shallow depth of field.

CRITICAL — NO TEXT: The papers must look printed but contain NO readable text — only faint, blurred gray line shapes. No names, no labels, no letters, no numbers, no logos, no watermarks, no signature anywhere in the image.

DO NOT INCLUDE: faces, heads, full bodies, computer screens, phones with visible content, brand logos, company names, hard dark shadows.
```

## I2 — Empty Event Booths (S06)

```text
Photorealistic cinematic photograph, landscape 3:2, 1536x1024 resolution. The final use is a small card inside a 16:9 (1920x1080) video frame: keep the subject centered with comfortable margins.

SCENE: A large, empty convention hall during setup, seen from a slightly raised angle. Neat rows of identical empty exhibition booth tables with plain white tablecloths, simple pipe-and-drape dividers, a few folding chairs pushed in. Clean carpeted aisle running toward the back. No people. The mood is "a booth layout being planned".

LIGHT: Even, bright overhead hall lighting plus soft daylight from large windows on the LEFT; cool neutral tone.

COLOR PALETTE: cool whites and light grays close to #F3F5FA, drapes in muted navy #161D33, one subtle accent of violet #5B3FD9 on a single table runner. Bright and orderly.

COMPOSITION: centered one-point perspective down the main aisle, symmetrical rows on both sides, plenty of breathing room around the edges.

CRITICAL — NO TEXT: No signs, no banners with writing, no booth numbers, no letters, no numbers, no logos, no watermarks anywhere in the image.

DO NOT INCLUDE: people, faces, crowds, brand logos, company names, promotional posters, screens showing content, any identifiable real event.
```

## I3 — Phone Glowing at Night (S15)

```text
Photorealistic cinematic photograph, landscape 3:2, 1536x1024 resolution. The final use is a card inside a 16:9 (1920x1080) video frame: keep the subject centered.

SCENE: A smartphone lying face-up on a bedside nightstand at night, its screen has just lit up with a soft glow as if a notification arrived. The screen shows only a blurred, featureless bright gradient — no interface, no icons. Nearby: a small lamp switched off, a glass of water. Nobody is looking at it. The feeling: "a signal arrived, but no one noticed".

LIGHT: The phone screen is the main light source, casting a soft cool glow upward; faint blue night light from a window on the LEFT. Not pitch black — keep shadow detail visible.

COLOR PALETTE: night tones in deep navy #161D33, screen glow in cool white close to #F3F5FA with a faint coral #E0572B tint at the edge of the glow.

COMPOSITION: phone slightly right of center, nightstand surface filling the lower third, softly blurred background.

CRITICAL — NO TEXT: The phone screen must show NO text, NO icons, NO app interface, NO time, NO numbers — only a smooth blurred glow. No letters, no logos, no watermarks anywhere in the image.

DO NOT INCLUDE: people, hands, faces, readable screen content, brand logos, clock displays with numbers.
```

## I4 — Four Envelopes on a Morning Desk (S17)

```text
Photorealistic cinematic photograph, landscape 3:2, 1536x1024 resolution. The final video frame is 16:9 (1920x1080): keep important content inside the central horizontal band.

SCENE: Exactly four plain white paper envelopes resting on a clean light-colored desk in the morning, slightly fanned and overlapping near the LOWER-RIGHT corner of the frame. A coffee cup at the far right edge. The rest of the desk is empty and clean.

LIGHT: Bright soft morning daylight from the LEFT, long gentle shadows of the envelopes falling to the right.

COLOR PALETTE: bright cool whites close to #F3F5FA, soft gray shadows, deep accents toward #161D33 only in the darkest shadow, a thin coral #E0572B stripe on one envelope's edge.

COMPOSITION FOR TEXT OVERLAY: the CENTER and LEFT 60% of the frame must be calm, empty desk surface — a very large number will be placed in the center. Envelopes stay in the lower-right area only.

CRITICAL — NO TEXT: Envelopes are completely blank — no addresses, no stamps with text, no postmarks, no logos. No letters, no numbers, no watermarks anywhere in the image.

DO NOT INCLUDE: people, hands, phones, laptops, screens, brand logos, more or fewer than four envelopes.
```

## I5 — Cracked Glass Funnel (S18)

```text
Photorealistic macro photograph, landscape 3:2, 1536x1024 resolution. The final video frame is 16:9 (1920x1080): keep the subject centered inside the central horizontal band.

SCENE: A clear glass laboratory funnel held upright in a simple stand, filled with water. A visible crack runs down the side of the funnel and water droplets are leaking out through the crack, while a thin stream also flows out of the spout. Droplets are frozen mid-air below the crack. The idea: "the filter has a hole".

LIGHT: Bright, clean studio light from the LEFT, crisp highlights on the glass and droplets, soft shadow to the right on a white surface.

COLOR PALETTE: bright white background close to #F3F5FA, glass edges with subtle navy reflections #161D33, the leaking droplets catching a faint coral #E0572B rim light.

COMPOSITION: funnel centered, crack facing the camera, generous white space on all sides.

CRITICAL — NO TEXT: No labels, no measurement markings, no letters, no numbers, no logos, no watermarks anywhere in the image.

DO NOT INCLUDE: people, hands, colored liquids, kitchen clutter, brand logos, dark backgrounds.
```

## I6 — Hands Paused Above a Laptop at Dusk (S24)

```text
Photorealistic cinematic photograph, landscape 3:2, 1536x1024 resolution. The final video frame is 16:9 (1920x1080): keep important content inside the central horizontal band; this image will sit behind text cards at about 30% opacity.

SCENE: A person's two hands resting still on a desk in front of an open laptop at dusk, fingers paused just above the keyboard as if double-checking something before pressing enter. The laptop screen shows only a soft, blurred light — no interface. A notebook and pen lie beside the laptop. Only hands and forearms are visible.

LIGHT: Fading daylight from a window on the LEFT mixed with the cool glow of the laptop screen; calm, reflective mood, not dark.

COLOR PALETTE: soft cool whites close to #F3F5FA, dusk shadows toward #161D33, a small violet #5B3FD9 accent (notebook cover) and a small coral #E0572B accent (pen).

COMPOSITION FOR TEXT OVERLAY: hands and laptop in the LOWER-RIGHT half; the UPPER-LEFT area is calm, low-detail wall and window light — cards will be placed over the center and left.

CRITICAL — NO TEXT: The laptop screen shows NO text, NO interface, NO icons — only blurred light. No letters, no numbers, no logos (including on the laptop lid), no watermarks anywhere in the image.

DO NOT INCLUDE: faces, heads, readable screen content, brand logos, coffee shop crowds, harsh dark shadows.
```

[Korean original](image-prompts.md) · [Slide plan](video-slide-plan_en.md)
