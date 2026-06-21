# Tehaleh 소개 영상 제작 프롬프트

**목적**: 창발 발표 오프닝 데모 영상 — "AI로 이렇게 뚝딱 만들 수 있습니다"를 보여주는 실제 사례
**영상 길이**: 2~3분
**대상 시청자**: 시애틀/벨뷰 지역 IT 종사자 및 은퇴 예정자
**주제**: Tehaleh 커뮤니티 — 시애틀·벨뷰 IT 종사자와 은퇴자에게 어떤 곳인가

---

## 작업 개요

이 프롬프트는 3단계로 구성됩니다:

1. **Phase 1 — 리서치**: Tehaleh에 대한 정보를 수집하고 구조화
2. **Phase 2 — 슬라이드 플랜**: 영상 구성을 video-slide-plan.md로 작성
3. **Phase 3 — Remotion 영상 제작**: 슬라이드 플랜을 바탕으로 영상 제작

각 Phase가 완료될 때마다 사용자의 승인을 받고 다음 단계로 진행합니다.

---

## 핵심 비주얼 자산 — Mt. Rainier View

**Tehaleh의 가장 큰 매력**: Mt. Rainier가 정면으로 보이는 뷰. 커뮤니티 도로 끝에서 Mt. Rainier가 정면으로 펼쳐지는 장면은 Tehaleh의 상징적인 이미지.

### 사용 가능한 사진

**① 거주자 직접 촬영 (우선 사용)**
- 파일: 사용자가 직접 촬영한 Mt. Rainier 뷰 사진
- 저장 경로: `public/tehaleh-intro-0619/images/mt-rainier-personal.jpg`
- 특징: 커뮤니티 도로에서 정면으로 촬영, 도로 양옆 소나무 + 정상의 설산 구도
- **사용 시**: 타이틀 슬라이드 또는 아웃트로에 우선 배치

**② 공개 사진 (보조 사용)**
- Tehaleh 공식 웹사이트 (tehaleh.com) 이미지 갤러리
- Newland Communities 공식 홍보 이미지
- Google Maps / Bing Maps 스트리트뷰 캡처
- Flickr/Unsplash에서 "Tehaleh Washington" 또는 "Bonney Lake Mt Rainier view" 검색
- **주의**: 저작권 확인 필요 — CC 라이선스 또는 공식 홍보용 이미지 우선

### 영상 내 Mt. Rainier 활용 계획

| 슬라이드 | 활용 방식 |
|---------|---------|
| S0 타이틀 | 거주자 직접 촬영 사진 배경 (full bleed) |
| S14 아웃트로 | 동일 사진 또는 황금빛 석양 버전 |
| S4 커뮤니티 섹션 | Mt. Rainier 뷰 언급 — "창문 밖으로 보이는 레이니어" |

### 사진 파일 준비 지침

Phase 3 시작 전 사용자가 아래 경로에 사진을 저장:
```
public/tehaleh-intro-0619/images/
├── mt-rainier-personal.jpg   ← 거주자 직접 촬영
└── (추가 공개 사진들)
```

---

## Phase 1: Tehaleh 리서치

### 1.1 리서치 목표

아래 항목들을 웹 검색으로 수집하세요. 단, 사용자가 직접 Tehaleh 거주자이므로 **개인 경험과 공식 정보를 구분**해서 정리합니다.

**수집 항목**:

**① 기본 정보**
- Tehaleh 위치 (시, 카운티, 우편번호)
- 개발사 및 개발 시작 연도
- 전체 규모 (세대수, 면적)
- 공식 웹사이트

**② 위치 및 접근성**
- Seattle 도심까지 거리/시간 (차, 대중교통)
- Bellevue까지 거리/시간
- Tacoma까지 거리/시간
- 가장 가까운 공항 (SeaTac)까지 거리/시간
- 인근 쇼핑/편의시설

**③ 커뮤니티 특성**
- 주거 유형 (단독주택, 타운홈 등)
- 주택 가격대 (현재 시세)
- 편의시설 (The Post, 수영장, 트레일, 공원, 피트니스 등)
- 학교 구역
- 커뮤니티 이벤트/활동

**④ IT 종사자에게 좋은 이유**
- 재택근무 환경 (인터넷 인프라, 조용한 환경)
- 자연환경 (등산, 하이킹, 자전거)
- Seattle/Bellevue 출퇴근 가능성
- tech 커뮤니티 presence
- 주택 가성비 (시애틀 대비)

**⑤ 은퇴자에게 좋은 이유**
- 조용하고 안전한 환경
- 액티브 시니어를 위한 활동
- 의료 시설 접근성
- 시애틀 대비 생활비
- 자연 속 라이프스타일

**⑥ 한인/아시안 커뮤니티**
- 인근 한인 상권 (H마트, 한인 식당 등)
- 아시안 커뮤니티 비율
- 한인 교회/커뮤니티 센터 접근성

### 1.2 리서치 실행 지침

```
검색어 예시:
- "Tehaleh community Bonney Lake WA"
- "Tehaleh Washington state homes for sale 2026"
- "Tehaleh amenities The Post"
- "Tehaleh commute Seattle Bellevue"
- "living in Tehaleh review"
- "Tehaleh vs Seattle cost of living"
- "Newland Communities Tehaleh"
```

### 1.3 리서치 산출물

수집한 정보를 아래 경로에 저장:
```
Ingest/CatchUpAI_VL/Topics/The-AI-Powered-Creator/vl_materials/tehaleh-research.md
```

**파일 구조**:
```markdown
# Tehaleh 리서치 노트

## 기본 정보
## 위치 및 접근성
## 커뮤니티 특성
## IT 종사자 관점
## 은퇴자 관점
## 한인/아시안 커뮤니티
## 출처 목록
```

> **Phase 1 완료 후**: 사용자에게 리서치 결과를 보여주고, 추가·수정 사항을 받은 뒤 Phase 2로 진행합니다.

---

## Phase 2: 영상 슬라이드 플랜 작성

### 2.1 영상 구성 방향

**영상 콘셉트**:
> "시애틀/벨뷰에서 45분, 자연 속 커뮤니티 Tehaleh — IT 종사자와 은퇴자의 새로운 선택"

**영상 흐름**:
```
[타이틀] Tehaleh가 뭔가요?
    ↓
[위치] 시애틀에서 얼마나 걸리나요?
    ↓
[커뮤니티] 어떤 곳인가요?
    ↓
[IT 종사자] 재택근무자에게 왜 좋은가요?
    ↓
[은퇴자] 은퇴 후 살기 좋은 이유는?
    ↓
[실제 거주자 시점] "저도 여기 삽니다"
    ↓
[마무리] 한 줄 정리
```

### 2.2 슬라이드 구성 (예상 15~18장, ~150초)

아래를 바탕으로 `video-slide-plan.md`를 작성하세요:

| # | 슬라이드 타입 | 내용 | 시각 자료 | 시간 |
|---|-------------|------|---------|------|
| 0 | `[TITLE]` | "Tehaleh — 시애틀에서 45분, 자연 속 삶" | **거주자 직접 촬영 Mt. Rainier 뷰 사진** (full bleed 배경) | 6초 |
| 1 | `[SECTION]` | "Tehaleh가 뭔가요?" | — | 4초 |
| 2 | `[BULLET]` | 위치, 규모, 개발사 기본 정보 | 지도 이미지 또는 위치 인포그래픽 | 8초 |
| 3 | `[STAT]` | Seattle 45분 · Bellevue 40분 · SeaTac 30분 | 거리 인포그래픽 | 7초 |
| 4 | `[SECTION]` | "어떤 커뮤니티인가요?" | — | 4초 |
| 5 | `[BULLET]` | The Post (카페·피트니스·수영장), 20마일 트레일 | AI 이미지: 커뮤니티 센터 | 8초 |
| 6 | `[BULLET]` | 주택 유형·가격대 (시애틀 대비 비교) | 가격 비교 인포그래픽 | 8초 |
| 7 | `[SECTION]` | "IT 종사자에게 왜 좋은가요?" | — | 4초 |
| 8 | `[BULLET]` | 재택근무 환경 · 고속 인터넷 · 조용한 자연 | AI 이미지: 홈오피스 + 자연 | 8초 |
| 9 | `[BULLET]` | 시애틀 출퇴근 가능 · 주택 가성비 | — | 7초 |
| 10 | `[SECTION]` | "은퇴 후 살기 좋은 이유는?" | — | 4초 |
| 11 | `[BULLET]` | 안전하고 조용한 환경 · 액티브 라이프 · 자연 | AI 이미지: 트레일 하이킹 | 8초 |
| 12 | `[BULLET]` | 인근 한인 마트·식당 · 의료 시설 접근 | — | 7초 |
| 13 | `[QUOTE]` | "저도 여기 삽니다 — 이 영상은 제가 사는 곳을 AI로 소개한 것입니다" | 거주자 시점 | 8초 |
| 14 | `[OUTRO]` | "Tehaleh — 시애틀/벨뷰 IT인의 새로운 선택" | **거주자 직접 촬영 Mt. Rainier 뷰 사진** (재사용, 황금빛 오버레이) | 8초 |

**총 예상 시간**: ~107초 (~1분 47초) → 나레이션 추가 시 ~2분 30초 내외

### 2.3 슬라이드 플랜 저장 경로

```
Remotion 프로젝트: Ingest/CatchUpAI_VL/Topics/Remotion-VideoCreation/my-first-video/
Video ID: tehaleh-intro-0619
```

저장 경로:
```
public/tehaleh-intro-0619/video-slide-plan.md
```

### 2.4 나레이션 스크립트 작성 지침

- **언어**: 한국어 (자연스러운 구어체)
- **톤**: 친근하되 정보 전달이 명확한 스타일
- **길이**: 슬라이드당 1~3문장, 총 2~3분 분량
- **특이사항**: S13(실제 거주자 시점)은 1인칭으로 작성

> **Phase 2 완료 후**: 슬라이드 플랜을 사용자에게 보여주고 확인을 받은 뒤 Phase 3으로 진행합니다.

---

## Phase 3: Remotion 영상 제작

### 3.1 Remotion 스킬 호출

Phase 3 시작 전 반드시 Skill tool로 `remotion-video` 스킬을 호출하세요:
```
Skill("remotion-video")
```

### 3.2 기술 사양

| 항목 | 설정 |
|------|------|
| **Video ID** | `tehaleh-intro-0619` |
| **Composition ID** | `TehalehIntro0619` |
| **배경 스타일** | `ANIMATED_DARK` (프리미엄 테크 분위기 — 자연과 기술의 조화) |
| **이미지** | `gpt-image-2` (AI 생성 이미지) — image-prompts.md 작성 후 사용자 제공 |
| **TTS Phase 1** | `edge-tts` → `ko-KR-SunHiNeural` |
| **TTS Phase 2** | 사용자 리뷰 후 Qwen3-TTS 교체 여부 결정 |
| **해상도** | 1920×1080 |

### 3.3 이미지 프롬프트 작성

슬라이드별 AI 이미지 프롬프트를 아래 경로에 작성:
```
public/tehaleh-intro-0619/image-prompts.md
```

**이미지 스타일 가이드**:
- 사실적이고 아름다운 PNW(Pacific Northwest) 자연 풍경
- 커뮤니티 생활 느낌 (현대적 주택, 트레일, 커뮤니티 센터)
- `no text` 규칙 적용 — 이미지에 글자 없음
- 밝고 따뜻한 색감 (낮 시간대, 맑은 날씨 선호)

**슬라이드별 이미지 프롬프트 예시**:
```
S0 (타이틀): ← 거주자 직접 촬영 사진 사용 (AI 생성 불필요)
S2 (위치 정보): "Simple clean map graphic of Pacific Northwest showing Seattle, Bellevue, and Bonney Lake area with distance markers, minimal style, no text"
S5 (커뮤니티): "Modern community center building surrounded by tall pine trees, people walking on paths, Pacific Northwest architecture, warm afternoon light, no text"
S8 (IT 재택): "Person working on laptop in a bright home office with large windows overlooking pine forest and snow-capped mountain, modern interior, no text"
S11 (은퇴 트레일): "Senior couple hiking on a scenic forest trail, Pacific Northwest, golden light filtering through tall pine trees, no text"
S13 (거주자 시점): ← 거주자 직접 촬영 Mt. Rainier 뷰 사진 사용 (AI 생성 불필요)
S14 (아웃트로): ← 거주자 직접 촬영 사진에 황금빛 오버레이 적용 (AI 생성 불필요)
```

**AI 이미지 생성 시 Mt. Rainier 표현 참고 프롬프트**:
```
"Straight road leading toward massive snow-capped Mount Rainier, pine trees lining both sides of the road, residential neighborhood visible, clear blue sky, Pacific Northwest, photorealistic, no text"
```
→ 거주자 실제 사진이 있으므로 S0/S13/S14는 실제 사진 우선 사용

### 3.4 Remotion 컴포넌트 구조

```
src/tehaleh-intro-0619/
  ├── data.ts               ← 슬라이드 데이터
  ├── TehalehIntro0619.tsx  ← 메인 컴포넌트
  └── slides/
      ├── TitleSlide.tsx
      ├── SectionSlide.tsx
      ├── BulletSlide.tsx
      ├── StatSlide.tsx
      ├── QuoteSlide.tsx
      └── OutroSlide.tsx
```

### 3.5 제작 단계

```
Phase 3a: video-slide-plan.md 최종 확인
Phase 3b: image-prompts.md 작성 → 사용자가 gpt-image-2로 이미지 생성
Phase 3c: Remotion 컴포넌트 개발
Phase 3d: edge-tts 오디오 생성 (gen_audio.py)
Phase 3e: 사용자 리뷰 → Qwen3-TTS 교체 여부 결정
Phase 3f: MP4 렌더링
```

---

## 실행 시작 방법

이 프롬프트를 새 세션에서 실행할 때:

1. **이 파일을 AI에게 제공**
2. AI가 Phase 1 리서치를 웹 검색으로 시작
3. 각 Phase 완료 시 결과 확인 후 "계속" 또는 수정 요청
4. Phase 3는 `remotion-video` 스킬을 먼저 호출한 후 진행

**주요 입력 정보** (세션 시작 시 AI에게 제공):
- 실제 거주 경험: Tehaleh 거주 중 (발표자 직접 거주)
- 발표 목적: 창발 발표 오프닝 데모 ("AI로 뚝딱 만들기" 증명)
- 주요 언어: 한국어
- 영상 길이 목표: 2~3분

---

## 녹화 가이드

이 작업 과정을 스크린 녹화할 때 포함할 장면:

| 장면 | 내용 | 발표 포인트 |
|------|------|-----------|
| ① 프롬프트 입력 | AI에게 이 프롬프트를 주는 순간 | "시작은 프롬프트 하나" |
| ② 리서치 진행 | AI가 웹 검색하며 정보 수집 | "AI가 조사한다" |
| ③ 슬라이드 플랜 | video-slide-plan.md가 만들어지는 과정 | "AI가 기획한다" |
| ④ 컴포넌트 생성 | Remotion 코드가 작성되는 화면 | "AI가 코딩한다" |
| ⑤ 렌더링 | MP4가 완성되는 순간 | "완성!" |

**편집 방향**: 전체 과정을 2~3분으로 압축. 각 단계 사이 빠른 전환. 최종 영상(Tehaleh 소개) 재생으로 마무리.

---

*발표 오프닝 데모용 — 창발 Product Group 2026-06-26*
*VibeLearn AI + Remotion 통합 워크플로우*
