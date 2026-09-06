---
title: "Active Shooter Response Training — 이미지 생성 프롬프트 명세서"
status: "📋 자기완결 규칙 준수 (M2 진행)"
created: 2026-09-06
---

# 이미지 생성 프롬프트 명세서: Active Shooter Response Training

본 명세서는 영상의 슬라이드에 활용할 AI 생성 이미지의 프롬프트를 정의합니다. Remotion Video Skill의 **「자기완결 프롬프트 원칙」**을 엄격히 준수하여 설계되었습니다.

---

## 🔆 이미지 가이드라인 및 공통 제약

1.  **일관된 디자인 테마**: 모든 이미지는 **L3 중간어둠(L3 Mid-Dark)** 대역을 고수합니다. 배경은 `Slate Charcoal (#161B22)` 톤을 기반으로 하며, 채도가 낮고 차분한 블루/네이비 톤 위에 강렬한 경고 색상(Crimson Red 또는 Caution Orange)이 포인트 라이트로 쓰여야 합니다.
2.  **자기완결성 (Self-Containment)**: 코드 블록 외부의 부가 설명 없이, 각 코드 블록 내의 영어 프롬프트 텍스트 한 줄만으로 AI 모델(Midjourney, DALL-E 3 등)이 완벽한 가시적 디자인을 구현할 수 있도록 7대 요소를 순서대로 포함하였습니다.
3.  **종횡비**: 모든 슬라이드용 비주얼 이미지는 **16:9 종횡비**로 명시합니다. (`--ar 16:9` 및 `aspect ratio 16:9` 포함)

---

## 📸 이미지 프롬프트 목록

### 1. Slide 03 — 뛴다 (Run)용 비주얼 이미지
*   **파일명**: `slide_03_run.png`
*   **비주얼 컨셉**: 대피로 유도선과 화살표가 있는 바닥 위로 다급히 달아나는 사람들의 발목 아래 클로즈업 샷 (긴박함과 질서정연함이 공존하는 분위기).

```text
A realistic cinematic photo of multiple people's legs and feet running urgently, low-angle ground shot, shallow depth of field, stepping on dark slate asphalt with glowing green directional evacuation arrow indicators printed on the floor, dramatic high-contrast lighting with dark shadows, L3 mid-dark desaturated blue and slate charcoal color grading, tense and high-alert atmosphere, photorealistic, sharp focus on shoes, aspect ratio 16:9, --ar 16:9 --v 6.0
```

---

### 2. Slide 05 — 싸운다 (Fight)용 비주얼 이미지
*   **파일명**: `slide_05_fight.png`
*   **비주얼 컨셉**: 어둠 속에서 최후의 수단으로 저항하기 위해 빨간 소화기의 손잡이를 굳게 쥐어잡고 있는 두 손의 익스트림 매크로 샷 (생존을 향한 비장한 의지).

```text
An extreme macro close-up cinematic photo of two strong hands gripping a red fire extinguisher tightly, preparing for last resort defense, hands are positioned in the center, dramatic high-contrast lighting with deep shadows, vivid crimson red rim light hitting the edges of the extinguisher and hands, L3 mid-dark slate grey background, intense and resolute atmosphere, photorealistic, detailed skin texture, aspect ratio 16:9, --ar 16:9 --v 6.0
```

---

### 3. Slide 07 — 경찰 대면 (Police)용 비주얼 이미지
*   **파일명**: `slide_07_police.png`
*   **비주얼 컨셉**: 건물 내부 복도의 어둠 속에서 강한 플래시라이트 조명을 비추며 전술 장비와 소총을 든 채 진입하는 SWAT 경찰 전술팀의 실루엣과, 그 앞에 무장이 없음을 보이기 위해 두 손을 높이 번쩍 들어 손가락을 펴고 있는 대피하는 시민의 양손 실루엣의 실루엣 대비 샷.

```text
A cinematic high-contrast dramatic photo of a police SWAT tactical team silhouetted in a dark slate-colored corridor, strong beams of cool white flashlight cutting through the volumetric haze, in the foreground the silhouette of a civilian's two hands raised high with fingers spread wide showing they are unarmed, L3 mid-dark slate charcoal background with teal-blue accents, urgent and intense high-alert atmosphere, extremely sharp focus on the raised hands, aspect ratio 16:9, --ar 16:9 --v 6.0
```

---

**작성 및 검증 완료**: Gemini CLI with VibeLearn AI
** master version**: 1.0
