---
title: "Active Shooter Response Training — AI 이미지 생성 프롬프트 명세서"
status: "📋 설계 완료 (M2 완료 - v2.1 개정판)"
created: 2026-09-08
note: "Remotion 비디오 제작을 위한 자기완결형(Self-contained) 이미지 생성 명세서입니다."
---

# AI 이미지 생성 프롬프트 명세서: Active Shooter Response

본 문서는 **VibeLearn AI 자기완결 프롬프트 원칙**에 맞춰, 비율, 조명, 구도, 그리고 밝기 가이드가 각 프롬프트 내에 완벽하게 기재된 영어 프롬프트 명세서입니다.

---

## 🎨 밝기 대역 정의 (Brightness Scale)

*   `L1`: 매우 밝음 (화이트 도면지 스키마, 테크니컬 스케치)
*   `L2`: 밝음/보통 (실내 자연광, 일상적인 사무실/로비 풍경)
*   `L3`: 어두움 (Slate Charcoal `#1a1f2c` 테마, 진지하고 현대적인 인포그래픽)
*   `L4`: 아주 어두움 (야간, 완전 소등 대피실, 침묵 은신처)

---

## 🖼️ 슬라이드별 이미지 프롬프트 리스트

### Slide 01: 오프닝 타이틀 (Opening Title Backdrop)
*   **밝기 대역**: `L3` (어두움)
*   **비주얼 컨셉**: 미 국토안보부(DHS) 재난대응 브리핑 느낌의 신뢰도 높은 추상 테크니컬 디자인.
*   **영어 프롬프트**:
    > Cinematic modern abstract background, dark slate charcoal (#1a1f2c) color scheme, soft neon-blue and gold light accents, flowing elegant lines and high-tech geometric structures, clean professional educational theme, 3D render, subtle depth of field, 16:9 aspect ratio, ultra-high resolution, photorealistic, no text, no human --ar 16:9

---

### Slide 05: 물리적 방어선: 문 단속 (Physical Security Steel Door)
*   **밝기 대역**: `L3` (어두움)
*   **비주얼 컨셉**: 안일한 불감증을 차단하는 튼튼하고 잠글 수 있는 보안 출입문 레이아웃.
*   **영어 프롬프트**:
    > Close-up shot of a heavily reinforced industrial steel security door, set in a solid matte-grey concrete wall, locked tight, modern minimalist design, dramatic side-lighting casting sharp shadows, minimal high-tech digital keypad glowing softly in blue on the wall side, dark moody atmospheric look, 16:9 aspect ratio, photorealistic, high contrast, no text, no human --ar 16:9

---

### Slide 06: 제1원칙: 뛴다 (Run - The Bright Exit)
*   **밝기 대역**: `L2` (밝음/보통)
*   **비주얼 컨셉**: 짐을 버리고 단호하게 달려가는 목적지인 안전하고 환하게 트인 비상구 방향.
*   **영어 프롬프트**:
    > Symmetric perspective of a modern architectural corridor leading to a bright, safe exit illuminated by warm morning sunlight, minimalist clean white walls, high concrete ceiling, subtle green emergency exit sign glowing softly above the glass doors, feeling of safety and ultimate hope, cinematic warm lighting, 16:9 aspect ratio, depth of field, photorealistic, no text, no human --ar 16:9

---

### Slide 07: 제2원칙: 숨는다 (Hide - Barricaded Shelter)
*   **밝기 대역**: `L4` (아주 어두움)
*   **비주얼 컨셉**: 소리가 완벽히 음소거되고 물리적 바리케이드가 튼튼하게 구축된 실내 은신 공간.
*   **영어 프롬프트**:
    > Dimly lit safe room interior, dark blue and deep charcoal palette, windowless concrete wall, heavy wooden desks and solid steel filing cabinets barricaded tightly against a locked metal door, quiet and secure atmosphere, soft moonlight filtering in, no people, safe shelter, cinematic moody lighting, 16:9 aspect ratio, photorealistic, no text --ar 16:9

---

### Slide 08: 제3원칙: 맞서 싸운다 (Fight - Aggressive Resolution)
*   **밝기 대역**: `L3` (어두움)
*   **비주얼 컨셉**: 맨손이 아닌 주변 집기를 적극 무기화하여 공격적으로 대항하겠다는 결연한 의지의 시각화.
*   **영어 프롬프트**:
    > Powerful energetic abstract background with intense deep-red and golden-yellow color splashes, dramatic diagonal light beams cutting through dark smoke, high-contrast, representing ultimate resolve, courageous action, and extreme determination, sharp graphic edges, professional vector poster style, 16:9 aspect ratio, no text --ar 16:9

---

## ⚠️ 프롬프트 적용 시 금지사항 (Negative Prompts)

- **텍스트 금지 (No Text)**: 모든 프롬프트에 `no text`, `no letters`, `no typos`를 의무 적용하여 AI가 생성하는 무작위 문자열 깨짐을 원천 차단합니다.
- **상대적 지칭 금지**: "Slide 01과 같은 테마" 혹은 "위와 동일" 등의 지칭을 일절 사용하지 않으며, 각각의 프롬프트는 완전히 자기완결적으로 독립 복사하여 사용할 수 있게 설계되었습니다.
