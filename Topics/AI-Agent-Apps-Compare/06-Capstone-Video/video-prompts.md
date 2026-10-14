---
title: "새 AI 에이전트 4개 비교 — Gemini 동영상 프롬프트"
video-id: agent-apps-compare-1013
created: 2026-10-14 12:30:00
tags:
  - remotion
  - ai-agent-apps-compare
  - video-prompts
  - gemini-veo
---

# 동영상 클립 프롬프트 (Gemini · Veo)

[English](video-prompts.en.md)

> 각 프롬프트는 **블록 하나만 복사하면 그대로 쓸 수 있게** 되어 있다.
> 비율 · 길이 · 무엇이 움직이는지 · 카메라 고정 · 밝기 · 색 · 금지 목록이 전부 블록 안에 있다.

## ⚠️ 도구 설정

| 항목 | 설정 |
|---|---|
| 도구 | Gemini 앱 또는 Google AI Studio 의 Veo (API 로 만들지 않는다) |
| 비율 | **UI 에서 16:9 직접 선택** |
| 길이 | Gemini 앱 기본 8초. 블록에도 8초로 적었다. 장면이 더 길면 Remotion 에서 마지막 프레임에 멈춘다(느리게 늘리지 않는다) |
| 소리 | 생성된 소리가 있어도 **무음으로** 넣는다 — 내레이션이 따로 있다 |

## 공통 규칙 (참고용 — 블록 안에 이미 다 들어 있다)

- 밝기 대역 **L2 중간밝음**(파스텔). 하늘 파스텔 `#E6EEF6` · 연두 파스텔 `#EEF3EA` · 숲 초록 `#2F7D5B` · 호박색 `#C77712`
- **카메라 고정**, 화면 안의 것만 움직인다. **사람은 넣지 않는다**(손도 뺐다 — 거부 대응)
- 저장: `AI/RemotionStudio/public/agent-apps-compare-1013/images/` 에 아래 파일 이름 그대로

| 파일 | 장면 | 쓰는 방식 |
|---|---|---|
| `v1_task_tray.mp4` | S04 답하는 AI, 일하는 AI | 화면 전체 배경 + 왼쪽 글 쪽 밝은 그라데이션 |
| `v2_four_doors.mp4` | S08 잠긴 문 셋, 열린 문 하나 | 화면 전체 배경 → 위에 「1 / 4」 |
| `v3_fall_maples.mp4` | S18 오프닝의 그 장면, 처음부터 | 도입 3초 화면 전체 → 라이브 클립으로 |
| `v4_four_checks.mp4` | S21 맡기기 전 네 가지 질문 | 도입 4초 → 판단 흐름도 |

## ⚠️ Gemini 거부 대응 (2026-10-14)

처음 쓴 긴 프롬프트(FORMAT · CAMERA · STYLE · DO NOT INCLUDE 같은 항목형, 색 hex 코드, 「얼굴 · 머리 · 몸 금지」 같은 신체 부위 금지 목록)를 Gemini 가 v1 에서 **「I can't generate that video」로 거부**했다. 정확한 이유는 알려 주지 않는다. 그래서 네 프롬프트를 모두 **짧은 자연어 문단**으로 다시 썼다.

- 항목 제목 · 대문자 경고 · hex 코드를 뺐다. 색은 말로 쓴다(soft pastel blue 등)
- **신체 부위를 나열하는 금지 문장을 뺐다.** 사람이 꼭 필요 없는 장면은 아예 사람 없이 물건만 움직이게 바꿨다(v1 · v4)
- 필수 조건(16:9 · 8초 · 카메라 고정 · 무엇이 움직이나 · 글자 없음 · 글자 얹을 빈자리 · 밝기)은 문장 안에 남겼다 — 블록 하나만 복사해도 되는 원칙은 그대로다
- 그래도 거부되면 블록 아래 「더 짧은 안」을 쓴다

## v1_task_tray.mp4 — S04 「답하는 AI, 일하는 AI」 배경

```
A calm, bright, photorealistic 8-second video in 16:9 widescreen. The camera stays completely still the whole time.

A light oak desk in a sunny, modern home office with a soft pastel blue wall. On the right side of the desk, a blank white paper card slides gently into a shallow white tray, and then the tray glides slowly away toward the back of the desk, as if the task has been handed off. Nothing else moves.

The left half of the frame is a plain, empty pastel wall and desk, leaving space for text. Soft natural daylight from the right, light and airy pastel blue and sage green tones, a few small forest green accents. No people, no writing on the card, no text, no logos.
```

**더 짧은 안**

```
Photorealistic 8-second 16:9 video, static camera. On a bright light oak desk against a pastel blue wall, a blank white card slides into a white tray, and the tray slowly glides away to the back of the desk. Left half of the frame stays empty. Soft daylight, airy pastel tones, no people, no text.
```

## v2_four_doors.mp4 — S08 「잠긴 문 셋, 열린 문 하나」 배경

```
A calm, bright, photorealistic 8-second video in 16:9 widescreen. The camera stays completely still, centered and symmetrical.

A short, minimal hallway with soft pastel blue walls and a pale sage green floor. Four identical light gray doors stand side by side on the far wall. Three of them stay closed. Only the second door from the right slowly swings open, and warm golden daylight spills out across the floor. Nothing else moves.

The wall above the doors is plain and empty, leaving space for a large number. Soft, even daylight, hopeful mood. No people, no signs, no numbers or writing on the doors, no text, no logos.
```

**더 짧은 안**

```
Photorealistic 8-second 16:9 video, static centered camera. A bright pastel hallway with four identical gray doors. Three stay closed; the second door from the right slowly opens and warm daylight spills out. Plain wall above the doors. No people, no text.
```

## v3_fall_maples.mp4 — S18 도입 「단풍」

```
A calm, photorealistic 8-second nature video in 16:9 widescreen. The camera stays completely still on a tripod.

A quiet forest walking path in Washington State in autumn, lined with maple trees in warm amber, red-orange and gold, with a few tall evergreen fir trees behind them. The path is covered with fallen leaves. A light breeze moves the branches slightly and a few red and amber leaves drift slowly down onto the path.

Bright, soft overcast daylight, clearly lit and peaceful. The lower left part of the path is calm and uncluttered. No people, no animals, no signs, no text.
```

**더 짧은 안**

```
Photorealistic 8-second 16:9 video, static camera. A Pacific Northwest forest path in autumn with red and amber maple trees and evergreen firs; a few leaves drift down in a light breeze. Bright overcast daylight. No people, no text.
```

## v4_four_checks.mp4 — S21 도입 「맡기기 전 네 가지 질문」

```
A bright, photorealistic 8-second video in 16:9 widescreen, filmed from directly above. The camera stays completely still.

A clean sheet of off-white paper lies on a light oak desk. On the left side of the paper is a vertical column of four empty square checkboxes with blank space beside them. One by one, from top to bottom, a neat forest green check mark appears in each box, as if drawn by an invisible pen. Nothing else moves.

The right side of the frame is plain empty desk, leaving space for text. Soft daylight from the upper left, airy pastel blue and sage green tones. No people, no words or numbers on the paper, no text, no logos.
```

**더 짧은 안**

```
Photorealistic 8-second 16:9 top-down video, static camera. A sheet of paper on a light oak desk with four empty checkboxes in a column; a green check mark appears in each box one by one. Right side of the frame stays empty. Soft daylight, pastel tones, no people, no text.
```

## ✅ 자체 검증

- [x] 블록마다 16:9 · 8초 · 실사 · 카메라 고정을 문장 안에 명시 (해상도 · fps 는 Gemini 가 정하므로 뺐다)
- [x] 「무엇이 움직이나」를 문장으로 명시하고 나머지는 「Nothing else moves」
- [x] 색은 hex 대신 말로 (Gemini 거부 대응), 밝기는 「bright · airy · soft daylight」로
- [x] 글자가 얹힐 빈자리 명시
- [x] 「No people, no text」 한 줄로 끝냄 — 신체 부위 금지 목록은 넣지 않음
