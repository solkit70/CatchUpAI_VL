---
title: "시민단체를 위한 총기난사 대응 및 공인 교육 수강 가이드 — 이미지 프롬프트 명세서 (v3.0)"
video-id: "active-shooter-0908"
created: 2026-09-13
---

# AI 이미지 생성 프롬프트 명세서

본 명세서는 **VibeLearn AI 자기완결형 프롬프트 원칙**을 엄격히 준수하여, 사용자가 각 코드 블록을 **단 한 번에 복사해서 미드저니, Dall-E 3, 또는 Gemini Image Skill에 붙여넣기만 하면** 즉각 고화질 에셋을 얻을 수 있도록 상세 규격을 내부화했습니다.

*   **배경 테마 및 밝기 대역**: L1 밝음 (Blueprint / Drawing Paper, #F7F9FC 배경색 기반)  
*   **화풍 컨셉**: 플랫하고 현대적인 산뜻한 테크니컬 일러스트레이션 및 다이어그램 스타일  

---

## 🖼️ 슬라이드별 이미지 프롬프트

### 1. `slide_02_context.png` — [Slide 02 삽입형 인포그래픽, 16:9]
*   **역할**: 시애틀센터 축제 현장 참사의 복합 충격(락다운, 수송 중단, 사회 불안)을 상징하는 연결형 재난 임팩트 다이어그램.
*   **권장 비율**: 16:9 와이드 삽입형 (`--ar 16:9` / 1792x1024)
*   **복사용 프롬프트**:
```text
Professional clean flat technical infographic diagram illustrating the cascading crisis of an urban active shooter incident, showing nodes connected by dashed blue lines representing "SOCIETAL CRISIS", "LOCKDOWN", and "TRANSPORTATION HALT". High-contrast, clean modern graphic vector style, soft off-white drawing paper background (#F7F9FC), bright sky-blue and warning-rose accents, minimal flat design, extremely sharp details, professional vector illustration, 16:9 aspect ratio, no realistic human faces, no gibberish text --ar 16:9
```

---

### 2. `slide_08_boundaries.png` — [Slide 08 역할 경계 다이어그램, 16:9]
*   **역할**: 무장 경비/경찰(공식 대응 영역)과 자원봉사자(대피/연락 및 대처 영역)의 엄격한 역할 한계선과 협업 구조를 시각화한 역할 경계 맵.
*   **권장 비율**: 16:9 와이드 삽입형 (`--ar 16:9` / 1792x1024)
*   **복사용 프롬프트**:
```text
A professional flat infographic diagram showing a clear vertical sky-blue dashed line representing a "ROLE BOUNDARY". On the left side is a security shield icon labeled with the word "OFFICIAL" in clean dark slate font. On the right side is a megaphone and high-visibility vest icon labeled with the word "VOLUNTEER" in bright caution-orange font. Minimalist technical vector style, soft light blue-gray background (#F7F9FC), clean flat design, high contrast, professional organization chart, 16:9 aspect ratio, no messy details, no gibberish letters --ar 16:9
```

---

### 3. `slide_12_qr.png` — [Slide 12 QR 코드 수록 글래스 카드, 1:1]
*   **역할**: 아웃트로에서 가이드북 다운로드용 QR코드가 삽입될 고급 골드/오렌지 빛 글로우 테두리의 글래스모피즘 카드 배경.
*   **권장 비율**: 1:1 정밀 카드형 (`--ar 1:1` / 1024x1024)
*   **복사용 프롬프트**:
```text
A high-fidelity minimalist vector illustration of a blank translucent frosted-glass square card floating in center, with a pulsing warm-golden and cautious orange neon glowing border emitting subtle light waves. Inside the glass card is an abstract high-tech square placeholder pattern representing a QR code. Soft off-white drawing paper background (#F7F9FC) with a faint micro dot grid pattern. Clean flat design, premium vector style, high-contrast, centered composition, aspect ratio 1:1, no letters, no typos --ar 1:1
```
