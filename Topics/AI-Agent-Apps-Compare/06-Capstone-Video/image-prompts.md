---
title: "새 AI 에이전트 4개 비교 — 이미지 프롬프트"
video-id: agent-apps-compare-1013
created: 2026-10-14 12:30:00
tags:
  - remotion
  - ai-agent-apps-compare
  - image-prompts
---

# 이미지 프롬프트

[English](image-prompts.en.md)

> 각 프롬프트는 **블록 하나만 복사하면 그대로 쓸 수 있게** 되어 있다.
> 비율 · 해상도 · 화풍 · 밝기 · 색 · 비울 자리 · 금지 목록이 전부 블록 안에 들어 있으니 **잘라내지 말 것.**

## ⚠️ 도구 설정 (프롬프트로 안 되는 부분)

| 도구 | 비율 |
|---|---|
| ChatGPT | 프롬프트의 비율 지시를 대체로 따름 |
| Gemini | **UI 에서 비율을 직접 선택** (16:9 또는 4:5). 프롬프트로는 잘 안 먹음 |
| Copilot | 비율 선택 없음(3:2) · 오른쪽 위 워터마크 → 쓰려면 위쪽 80px 를 잘라야 함 |

## 공통 규칙 (참고용 — 블록 안에 이미 다 들어 있다)

- 밝기 대역 **L2 중간밝음**(파스텔). 하늘 파스텔 `#E6EEF6` · 연두 파스텔 `#EEF3EA` 바탕, 포인트 숲 초록 `#2F7D5B` · 호박색 `#C77712`
- 사람은 **손까지만**. 얼굴 · 화면 속 글자 · 로고 금지
- 저장: `AI/RemotionStudio/public/agent-apps-compare-1013/images/` 에 아래 파일 이름 그대로

| 파일 | 장면 | 비율 | 쓰는 방식 |
|---|---|---|---|
| `i1_key_handoff.png` | S09 맡긴다는 건, 권한을 건네는 것 | 4:5 세로 | 오른쪽 카드 |
| `i2_clock_timetable.png` | S13 처음엔 시간을 잘못 셌다 | 16:9 | 도입 3초 화면 전체 |
| `i3_single_specimen.png` | S17 그래서 몇 분 아꼈냐고요? | 16:9 | 30% 투명도 배경 |
| `i4_handoff_review.png` | S23 맡기되, 확인은 사람이 | 16:9 | 30% 투명도 배경 |
| `i5_outside_home.png` | S20 밖에서는 Muse, 집에서는 내 2nd Brain | 16:9 | 비교 카드 뒤 배경 |

## i1_key_handoff.png — S09 「맡긴다는 건, 권한을 건네는 것」 오른쪽 카드

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

## i2_clock_timetable.png — S13 「처음엔 시간을 잘못 셌다」 도입 3초

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

## i3_single_specimen.png — S17 「그래서 몇 분 아꼈냐고요?」 30% 배경

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

## i4_handoff_review.png — S23 「맡기되, 확인은 사람이」 30% 배경

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

## i5_outside_home.png — S20 「밖에서는 Muse, 집에서는 내 2nd Brain」 배경

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

## ✅ 자체 검증

- [x] 모든 블록 첫 줄이 `OUTPUT FORMAT`(비율 + 해상도 + 여백 금지)
- [x] STYLE 전문을 블록마다 반복(색 hex 포함)
- [x] LIGHTING 에 L2 문장 포함
- [x] 사람이 나오는 컷(i1 · i4 · i5)은 「손까지만」을 블록 안에 명시
- [x] 글자가 얹힐 컷은 COMPOSITION 에 비울 자리 명시
- [x] 금지 목록(얼굴 · 글자 · 로고 · 워터마크)
- [x] 블록 밖 한글 안내를 지워도 결과가 같다
