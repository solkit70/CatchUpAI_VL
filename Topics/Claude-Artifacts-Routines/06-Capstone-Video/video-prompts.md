---
title: "Claude Artifacts · Routines — Gemini 10초 동영상 프롬프트 (V1~V5)"
created: "2026-10-06 09:45:00"
author:
  - "Claude Code"
tags:
  - remotion
  - video-prompts
  - gemini-veo
  - claude-artifacts-routines
status: "ready-for-generation"
---

## 사용법

[슬라이드 플랜 v3](video-slide-plan.md#ai-이미지동영상-계획)의 10초 동영상 5편이다. **코드블록 하나만 복사해 Gemini(Veo)에 붙이면 된다** — 비율 · 길이 · 무엇이 움직이는지 · 카메라 고정 · 색 · 글자 자리 · 금지 목록이 모두 블록 안에 있다. 생성한 파일은 아래 이름으로 `AI/RemotionStudio/public/claude-artifacts-routines-1004/images/`에 둔다.

| ID  | 장면  | 시점    | 파일 이름                         | 쓰는 방식               |
| --- | --- | ----- | ----------------------------- | ------------------- |
| V1  | S01 | 0:00  | `v1_s01_morning_desk.mp4`     | 화면 전체 배경            |
| V2  | S14 | 8:06  | `v2_s14_datacenter_aisle.mp4` | 30% 투명도 배경 위 도식     |
| V3  | S16 | 9:41  | `v3_s16_locked_cage.mp4`      | 도입 3초 컷 (유일한 어두운 컷) |
| V4  | S20 | 12:36 | `v4_s20_rainier_sunrise.mp4`  | 마지막 10초 배경          |
| V5  | S25 | 15:48 | `v5_s25_rainy_window.mp4`     | 아웃트로 배경 (QR 뒤)      |

공통 원칙: 카메라는 고정하고 화면 안의 것만 움직인다. 사람 · 글자 · 로고는 넣지 않는다. 화면이 나오면 꺼져 있거나 흐린 빛만 보인다. Remotion에서는 `<OffthreadVideo muted>`로 넣고, 장면이 10초보다 길면 클립을 늦추지 않고 마지막 프레임에서 멈춘다.

## V1 — 조용한 아침 책상 (S01)

```
Silent 10-second video clip, 16:9 landscape aspect ratio, 1920x1080 resolution, 24fps. Live-action photorealistic look (not animation), cinematic and calm.

SCENE: An early Monday morning at a home desk. A smartphone lies face-up on the desk with its screen OFF (black glass, no content). Beside it, a white mug of coffee with gentle steam rising. A closed laptop at the back edge. The feeling: waiting for a message that never arrives.

MOTION (this is all that moves): a soft beam of sunlight from a window on the LEFT slowly slides across the desk surface from left to right over the 10 seconds; steam rises and curls from the mug; tiny dust particles drift in the light beam. Nothing else moves. The phone never lights up.

CAMERA: Completely static, locked off. No pan, no zoom, no push-in, no tilt.

LIGHT: Cool, quiet dawn light from the LEFT, growing very slightly brighter over the clip. Bright overall, not dark.

COLOR PALETTE: cool off-white desk and wall close to #F3F5FA, shadows toward deep navy #161D33, mug with a small coral #E0572B stripe.

COMPOSITION FOR TEXT OVERLAY: phone and mug in the LOWER-RIGHT third; the CENTER and LEFT of the frame stay calm and uncluttered — large text and three date-stamp cards will be placed there.

CRITICAL — NO TEXT: no text, letters, numbers, clocks, logos, or watermarks anywhere. The phone screen stays black the entire time.

DO NOT INCLUDE: people, hands, faces, lit screens, notifications, brand logos, music, sound.
```

## V2 — 밝은 데이터센터 통로 (S14)

```
Silent 10-second video clip, 16:9 landscape aspect ratio, 1920x1080 resolution, 24fps. Live-action photorealistic look (not animation).

SCENE: A modern, very clean and bright data center aisle. Tall white server racks line both sides, stretching toward the back in one-point perspective. White floor tiles, white ceiling with linear lights. Calm, orderly, high-tech.

MOTION (this is all that moves): small status LEDs on the racks blink softly in cool blue and green at different rhythms; a very faint haze of cool air drifts slowly across the floor. Nothing else moves.

CAMERA: Completely static, locked off, centered in the aisle at eye level. No pan, no zoom, no push-in, no dolly.

LIGHT: Bright, even, cool white overhead lighting; soft reflections on the floor. Bright overall (this clip sits behind diagrams at 30% opacity).

COLOR PALETTE: whites and very light grays close to #F3F5FA, rack details in deep navy #161D33, LED accents in cool blue, one tiny coral #E0572B status light near the center.

COMPOSITION FOR TEXT OVERLAY: symmetrical; the central aisle area stays clean and low-detail because a workflow diagram will sit in the center.

CRITICAL — NO TEXT: no labels on racks, no signs, no rack numbers, no letters, no numbers, no logos, no watermarks anywhere.

DO NOT INCLUDE: people, workers, faces, brand logos, company names, screens with content, dark or moody lighting, sound.
```

## V3 — 잠긴 철망 문과 빨간 상태등 (S16)

```
Silent 10-second video clip, 16:9 landscape aspect ratio, 1920x1080 resolution, 24fps. Live-action photorealistic look (not animation).

SCENE: Close-up of a locked metal mesh cage door inside a server room. A heavy padlock and a small electronic access panel are on the door. Behind the mesh, out of focus, rows of server racks. The idea: "the door was locked — requests could not get out".

MOTION (this is all that moves): a small red status light on the access panel blinks slowly on and off; behind the mesh, out-of-focus server LEDs twinkle faintly. The door and padlock stay perfectly still.

CAMERA: Completely static, locked off. No pan, no zoom, no push-in.

LIGHT: Dim but readable server-room light, cool blue ambient from the LEFT; the red light is the only warm accent. Darker than the rest of the video, but shadow detail must remain visible.

COLOR PALETTE: deep navy #161D33 dominant, cool steel grays, mesh highlights close to #F3F5FA, red-coral status light #E0572B.

COMPOSITION FOR TEXT OVERLAY: padlock and access panel slightly RIGHT of center; the LEFT third is plain dark mesh with low detail — a short line of text may appear there.

CRITICAL — NO TEXT: the access panel shows NO characters, NO numbers, NO icons. No signs, no letters, no logos, no watermarks anywhere.

DO NOT INCLUDE: people, hands, faces, brand logos, warning signs with text, sparks, alarms, sound.
```

## V4 — 레이니어산 일출 (S20)

```
Silent 10-second video clip, 16:9 landscape aspect ratio, 1920x1080 resolution, 24fps. Live-action photorealistic look (not animation), cinematic nature footage.

SCENE: Mount Rainier in Washington State at sunrise, its snow-covered peak glowing softly, seen across a wide valley of dense evergreen forest (Douglas fir and cedar). Gentle layers of morning mist sit between the forested ridges. A hopeful, quiet "home" feeling.

MOTION (this is all that moves): low clouds and mist drift slowly from left to right across the forest; the sunrise light on the mountain peak warms gradually from pale pink to soft gold over the 10 seconds. The mountain and trees stay still.

CAMERA: Completely static, locked off. No pan, no zoom, no push-in, no drone movement.

LIGHT: Early sunrise from the RIGHT side, soft and clear; the sky bright and pale, not dark.

COLOR PALETTE: pale sky close to #F3F5FA, forest shadows toward deep navy-green #161D33, peak glow with a gentle coral #E0572B warmth, a faint violet #5B3FD9 tint in the upper sky.

COMPOSITION FOR TEXT OVERLAY: mountain peak in the RIGHT half; the UPPER-LEFT sky area is clean and low-detail — a line of large text will be placed there.

CRITICAL — NO TEXT: no text, letters, numbers, signs, logos, or watermarks anywhere.

DO NOT INCLUDE: people, hikers, buildings, roads, cars, power lines, aircraft, birds in the foreground, sound.
```

## V5 — 비 오는 저녁 창가 (S25)

```
Silent 10-second video clip, 16:9 landscape aspect ratio, 1920x1080 resolution, 24fps. Live-action photorealistic look (not animation), calm and cozy.

SCENE: A window on a rainy Pacific Northwest evening, seen from inside a home. Raindrops run down the glass. Outside, softly blurred evergreen trees under a blue dusk sky. Inside, at the lower edge of the frame, the warm glow of a small desk lamp reflects faintly on the glass.

MOTION (this is all that moves): raindrops slide slowly down the window and new droplets land; the trees outside sway very slightly. Nothing else moves.

CAMERA: Completely static, locked off. No pan, no zoom, no push-in, no focus pull.

LIGHT: Cool blue dusk light from outside, one small warm lamp glow at the LOWER-RIGHT inside. Calm and moderately bright, not dark (QR codes will sit on top).

COLOR PALETTE: window glass and sky in soft cool tones close to #F3F5FA, dusk shadows toward deep navy #161D33, lamp glow with a gentle coral #E0572B warmth.

COMPOSITION FOR TEXT OVERLAY: the CENTER of the frame is soft, low-contrast blurred rain on glass — two large QR codes and short text will be placed side by side in the center. Keep strong detail only near the edges.

CRITICAL — NO TEXT: no text, letters, numbers, logos, or watermarks anywhere; no writing in the condensation on the glass.

DO NOT INCLUDE: people, silhouettes, faces, hands, screens, brand logos, lightning, sound.
```


English companion: [video-prompts_en](video-prompts_en.md)
