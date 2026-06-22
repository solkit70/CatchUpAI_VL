# Tehaleh-Community-Video 학습 로드맵

**생성일**: 2026-06-21
**방법론**: VibeLearn AI
**버전**: 1.0

---

## 📊 학습 기간 적정성 분석

**사용자 입력 기간**: 1일 (집중 세션, ~6-8시간)
**Topic 복잡도**: 중간~복잡 (다중 기술 통합: 리서치 + 영상 기획 + Remotion 코딩 + TTS 오디오)
**권장 기간**: 2-3일 (일반적), 1일 (사전 지식 충분한 경우)

**분석 결과**:
- ⚠️ **빠듯하지만 달성 가능**: 1일 집중 세션은 일반적으로 빠듯하나, Remotion·edge-tts 사전 경험이 있고 기존 프롬프트 파일이 잘 준비되어 있어 핵심 산출물 완성 가능.

**조치 제안**: 계획대로 1일 집중 세션으로 진행. M3(Remotion 개발)에서 시간이 부족하면 AI 코드 생성 최대 활용.

---

## 📚 학습 개요

### Topic 소개

Tehaleh 지역 소개 영상을 AI(Remotion)로 제작하는 전 과정 학습 및 실습. 창발 발표(2026-06-26) 오프닝 데모로 "AI로 이렇게 뚝딱 만들 수 있습니다"를 실증하는 실제 사례. 대상 시청자는 시애틀/벨뷰 IT 종사자 및 은퇴 예정자.

### 학습 목표

- [ ] Tehaleh 리서치 자료를 수집·구조화하여 tehaleh-research.md를 완성할 수 있다
- [ ] 영상 슬라이드 플랜(15-18장)을 video-slide-plan.md로 작성할 수 있다
- [ ] gpt-image-2 이미지 프롬프트를 image-prompts.md로 작성할 수 있다
- [ ] Remotion 컴포넌트(TehalehIntro0619)를 AI 도움으로 개발할 수 있다
- [ ] edge-tts로 한국어 나레이션 오디오를 생성할 수 있다
- [ ] MP4 영상(1920×1080)을 최종 렌더링할 수 있다

### 예상 학습 기간

1일 집중 세션 (~6-8시간, 버퍼 포함 ~9시간)

### 학습 환경

- OS: Windows 11
- 도구: Remotion, edge-tts (ko-KR-SunHiNeural), gpt-image-2, Node.js 18+, Python 3 (gen_audio.py)
- 사전 지식: Remotion 기초, edge-tts 사용법

---

## 🗺️ 전체 로드맵 구조

| 모듈  | 모듈명                | 난이도 | 예상 시간 | 산출물 폴더          |
| --- | ------------------ | --- | ----- | --------------- |
| M1  | Tehaleh 리서치        | ⭐   | ~2h   | 01-Research/    |
| M2  | 슬라이드 플랜            | ⭐⭐  | ~1h   | 02-SlidePlan/   |
| M3  | Remotion 개발        | ⭐⭐⭐ | ~3h   | 03-RemotionDev/ |
| M4  | 오디오·렌더링 (Capstone) | ⭐⭐  | ~1.5h | 04-AudioRender/ |

**총 예상 시간**: ~7.5시간 (버퍼 20% 포함 → ~9h)

---

## 📖 모듈별 상세 계획

---

### M1 - Tehaleh 리서치

**난이도**: ⭐
**예상 시간**: ~2시간
**산출물 폴더**: `01-Research/`

#### 학습 목표

- [ ] Tehaleh 위치, 규모, 개발사 등 기본 정보를 정확하게 수집할 수 있다
- [ ] IT 종사자·은퇴자 관점에서 Tehaleh의 장점을 구조화하여 설명할 수 있다
- [ ] 한인/아시안 커뮤니티 접근성 정보를 포함한 tehaleh-research.md를 완성할 수 있다

#### 주요 개념

1. **리서치 구조화**: 정보를 6개 카테고리(기본 정보, 위치, 커뮤니티 특성, IT 관점, 은퇴자 관점, 한인 커뮤니티)로 분류
2. **1인칭 거주자 시점**: 공식 정보 + 실제 거주 경험을 구분하여 신뢰도 향상
3. **대상 청중 맞춤화**: 시애틀/벨뷰 IT 종사자와 은퇴 예정자의 관심사에 맞게 정보 선별

#### 실습 과제

**실습 1: 기본 정보 웹 검색** ⭐
- **목적**: Tehaleh 공식 정보를 수집하여 리서치 기반 구축
- **단계**:
  1. "Tehaleh community Bonney Lake WA" 검색
  2. "Tehaleh Washington state homes for sale 2026" 검색
  3. "Tehaleh amenities The Post commute Seattle" 검색
  4. 수집 정보를 기본 정보·위치 섹션에 정리
- **예상 시간**: 40분
- **검증**: tehaleh-research.md의 기본 정보·위치 섹션이 완성되면 성공

**실습 2: 대상 청중별 분석 정리** ⭐⭐
- **목적**: IT 종사자·은퇴자·한인 커뮤니티 관점으로 정보를 재구성
- **단계**:
  1. "Tehaleh commute Seattle Bellevue remote work" 검색
  2. "living in Tehaleh review cost of living Seattle" 검색
  3. "H-Mart Korean community Pierce County" 검색
  4. 각 대상 그룹별 섹션에 정리
  5. 거주자 실제 경험 코멘트 추가 (1인칭)
- **예상 시간**: 50분
- **검증**: IT 관점·은퇴자 관점·한인 커뮤니티 섹션이 각 3개 이상 포인트로 채워지면 성공

#### 산출물

```
01-Research/
├── README.md
└── (tehaleh-research.md는 vl_materials/에 저장)

vl_materials/
└── tehaleh-research.md   ← 실제 리서치 결과
```

> **저장 위치 주의**: tehaleh-research.md는 `vl_materials/` 폴더에 저장 (tehaleh-video-prompt.md 지시에 따름)

```
tehaleh-research.md 구조:
# Tehaleh 리서치 노트
## 기본 정보
## 위치 및 접근성
## 커뮤니티 특성
## IT 종사자 관점
## 은퇴자 관점
## 한인/아시안 커뮤니티
## 출처 목록
```

#### Definition of Done

- [ ] tehaleh-research.md 6개 섹션 모두 작성 완료
- [ ] 기본 정보: 위치, 규모, 개발사, 공식 사이트 포함
- [ ] 위치 섹션: Seattle·Bellevue·SeaTac 거리/시간 포함
- [ ] IT 관점·은퇴자 관점 각 3개 이상 포인트
- [ ] 출처 목록에 URL 3개 이상
- [ ] WorkLog(20260621_M1_Tehaleh-Community-Video.md) 작성 완료

#### Self-Assessment

**개념 이해**:
- [ ] Tehaleh의 위치를 Seattle/Bellevue 대비 시간·거리로 설명할 수 있다
- [ ] IT 종사자에게 좋은 이유 3가지를 즉시 말할 수 있다

**실무 활용**:
- [ ] 리서치 결과를 영상 슬라이드 구성에 바로 연결할 수 있다
- [ ] AI에게 추가 정보 검색을 효과적으로 요청할 수 있다

**문제 해결**:
- [ ] 정보가 부족할 때 대체 검색어를 생성할 수 있다

#### 예상 시간 배분

- 기본 정보 검색: 40분 (33%)
- 대상 청중별 분석: 50분 (42%)
- 문서화 및 정리: 20분 (17%)
- 버퍼: 10분 (8%)
- **합계**: ~2시간

#### 참조 자료

- tehaleh-video-prompt.md의 Phase 1 섹션: 수집 항목·검색어 목록
- Tehaleh 공식 사이트: https://tehaleh.com (검색 후 접근)

---

### M2 - 슬라이드 플랜 작성

**난이도**: ⭐⭐
**예상 시간**: ~1시간
**산출물 폴더**: `02-SlidePlan/`

#### 학습 목표

- [ ] Tehaleh 소개 영상의 15-18장 슬라이드 구성을 video-slide-plan.md로 작성할 수 있다
- [ ] 각 슬라이드에 타입·내용·나레이션·시각 자료·시간을 명시할 수 있다
- [ ] gpt-image-2용 이미지 프롬프트를 image-prompts.md로 작성할 수 있다

#### 주요 개념

1. **슬라이드 타입**: `[TITLE]`, `[SECTION]`, `[BULLET]`, `[STAT]`, `[QUOTE]`, `[OUTRO]` — 각 타입별 Remotion 컴포넌트가 다름
2. **영상 흐름**: 타이틀 → 위치 → 커뮤니티 → IT 관점 → 은퇴자 관점 → 거주자 시점 → 아웃트로
3. **나레이션 원칙**: 한국어 구어체, 슬라이드당 1-3문장, 길이 제한 없음 (내용 중심)

#### 실습 과제

**실습 1: video-slide-plan.md 작성** ⭐⭐
- **목적**: M3 Remotion 개발의 데이터 원천(data.ts)이 될 슬라이드 플랜 완성
- **단계**:
  1. tehaleh-video-prompt.md의 Phase 2 슬라이드 구성표를 기반으로 시작
  2. M1 리서치 결과를 각 슬라이드 내용에 반영
  3. 각 슬라이드에 한국어 나레이션 스크립트 작성
  4. `public/tehaleh-intro-0619/video-slide-plan.md`로 저장
- **예상 시간**: 35분
- **검증**: 15-18장 슬라이드, 각 슬라이드에 type·content·narration·duration 필드 완성

**실습 2: image-prompts.md 작성** ⭐⭐
- **목적**: gpt-image-2로 생성할 AI 이미지 프롬프트 준비
- **단계**:
  1. 슬라이드 중 AI 이미지가 필요한 슬라이드 식별 (S2, S5, S8, S11)
  2. PNW 자연·커뮤니티 분위기의 영어 프롬프트 작성
  3. "no text" 규칙 적용
  4. `public/tehaleh-intro-0619/image-prompts.md`로 저장
- **예상 시간**: 20분
- **검증**: AI 이미지 필요 슬라이드별 영어 프롬프트 완성, 거주자 사진 사용 슬라이드 명시

#### 산출물

```
02-SlidePlan/
└── README.md

public/tehaleh-intro-0619/      ← Remotion 프로젝트 public 폴더
├── video-slide-plan.md         ← 슬라이드 플랜 (메인 산출물)
├── image-prompts.md            ← AI 이미지 프롬프트
└── images/
    └── mt-rainier-personal.jpg ← 사용자 직접 촬영 (사전 준비)
```

**video-slide-plan.md 형식**:
```markdown
# Tehaleh Intro 슬라이드 플랜

## Video ID: tehaleh-intro-0619
## Total Duration: ~120s

| # | Type | Content | Narration | Visual | Duration |
|---|------|---------|-----------|--------|----------|
| S0 | [TITLE] | ... | "나레이션 텍스트" | mt-rainier-personal.jpg | 6s |
...
```

#### Definition of Done

- [ ] video-slide-plan.md: 15장 이상 슬라이드, 각 슬라이드 5개 필드 완성
- [ ] S0(타이틀)과 S마지막(아웃트로)에 거주자 직접 촬영 사진 지정
- [ ] 모든 슬라이드에 한국어 나레이션 스크립트 작성
- [ ] image-prompts.md: AI 이미지 필요 슬라이드별 영어 프롬프트 완성
- [ ] 총 예상 영상 시간 ~90-150초 범위
- [ ] WorkLog 업데이트 완료

#### Self-Assessment

**개념 이해**:
- [ ] 슬라이드 타입(TITLE, SECTION, BULLET 등)의 차이를 설명할 수 있다
- [ ] video-slide-plan.md가 Remotion data.ts의 원천임을 설명할 수 있다

**실무 활용**:
- [ ] AI에게 나레이션 스크립트 개선을 효과적으로 요청할 수 있다
- [ ] gpt-image-2 프롬프트의 "no text" 규칙이 왜 필요한지 설명할 수 있다

#### 예상 시간 배분

- video-slide-plan.md 작성: 35분 (58%)
- image-prompts.md 작성: 20분 (33%)
- 검토 및 문서화: 5분 (9%)
- **합계**: ~1시간

#### 참조 자료

- tehaleh-video-prompt.md Phase 2: 슬라이드 구성표 (S0-S14)
- Phase 2.4: 나레이션 스크립트 작성 지침
- Phase 3.3: 이미지 프롬프트 예시

---

### M3 - Remotion 컴포넌트 개발

**난이도**: ⭐⭐⭐
**예상 시간**: ~3시간
**산출물 폴더**: `03-RemotionDev/`

#### 학습 목표

- [ ] video-slide-plan.md를 기반으로 data.ts 슬라이드 데이터를 작성할 수 있다
- [ ] TehalehIntro0619.tsx 메인 컴포넌트를 AI 도움으로 개발할 수 있다
- [ ] 각 슬라이드 타입별 컴포넌트(TitleSlide, BulletSlide 등)를 구현할 수 있다
- [ ] ANIMATED_DARK 배경 스타일을 적용할 수 있다

#### 주요 개념

1. **Composition 구조**: Remotion에서 `<Composition>`은 VideoID·너비·높이·fps·durationInFrames를 등록하는 단위. Root.tsx에서 등록 필요
2. **슬라이드 타입 컴포넌트**: 각 `[TYPE]`마다 별도 .tsx 파일 — TitleSlide, SectionSlide, BulletSlide, StatSlide, QuoteSlide, OutroSlide
3. **ANIMATED_DARK 배경**: 기존 Remotion-VideoCreation 프로젝트에서 재사용 가능한 배경 스타일
4. **data.ts 패턴**: 슬라이드 데이터를 타입 안전하게 정의하는 TypeScript 파일 — AI에게 video-slide-plan.md를 주면 자동 생성 가능

#### 실습 과제

**실습 1: data.ts 및 컴포넌트 구조 생성** ⭐⭐
- **목적**: video-slide-plan.md를 TypeScript 데이터로 변환
- **단계**:
  1. 기존 Remotion 프로젝트 구조 확인: `Ingest/CatchUpAI_VL/Topics/Remotion-VideoCreation/my-first-video/src/`
  2. `src/tehaleh-intro-0619/` 폴더 생성
  3. AI에게 video-slide-plan.md를 주고 data.ts 생성 요청
  4. 슬라이드 타입별 TypeScript 인터페이스 정의 확인
- **예상 시간**: 45분
- **검증**: data.ts가 생성되고 `npx tsc --noEmit`에서 타입 에러 없음

**실습 2: 슬라이드 컴포넌트 개발** ⭐⭐⭐
- **목적**: 각 슬라이드 타입을 React 컴포넌트로 구현
- **단계**:
  1. AI에게 `slides/TitleSlide.tsx` 생성 요청 (ANIMATED_DARK 배경 포함)
  2. `slides/SectionSlide.tsx`, `slides/BulletSlide.tsx` 생성
  3. `slides/StatSlide.tsx`, `slides/QuoteSlide.tsx`, `slides/OutroSlide.tsx` 생성
  4. `TehalehIntro0619.tsx` 메인 컴포넌트 생성 (data.ts 슬라이드 배열을 순회)
  5. `Root.tsx`에 Composition 등록
- **예상 시간**: 90분
- **검증**: `npx remotion preview` 실행 시 브라우저에서 슬라이드 미리보기 성공

**실습 3: 이미지 통합 및 미리보기 검증** ⭐⭐
- **목적**: 거주자 직접 촬영 사진과 AI 생성 이미지를 컴포넌트에 통합
- **단계**:
  1. `public/tehaleh-intro-0619/images/` 폴더에 이미지 파일 확인
  2. staticFile() 또는 img src로 이미지 참조 방법 확인
  3. TitleSlide와 OutroSlide에 mt-rainier-personal.jpg 적용
  4. 전체 슬라이드 미리보기 검토
- **예상 시간**: 30분
- **검증**: Remotion 미리보기에서 거주자 촬영 사진이 S0·S14에 표시됨

#### 산출물

```
src/tehaleh-intro-0619/
├── data.ts               ← 슬라이드 데이터 (TypeScript)
├── TehalehIntro0619.tsx  ← 메인 컴포넌트
└── slides/
    ├── TitleSlide.tsx
    ├── SectionSlide.tsx
    ├── BulletSlide.tsx
    ├── StatSlide.tsx
    ├── QuoteSlide.tsx
    └── OutroSlide.tsx

03-RemotionDev/
└── README.md
```

#### Definition of Done

- [ ] data.ts 생성 완료 (모든 슬라이드 데이터 포함)
- [ ] 6개 슬라이드 컴포넌트 모두 구현
- [ ] TehalehIntro0619.tsx 메인 컴포넌트 완성
- [ ] Root.tsx에 Composition 등록 완료
- [ ] `npx remotion preview`에서 에러 없이 미리보기 성공
- [ ] 거주자 사진(mt-rainier-personal.jpg)이 S0·S14에 표시됨
- [ ] WorkLog 업데이트 완료

#### Self-Assessment

**개념 이해**:
- [ ] Remotion Composition과 Sequence의 차이를 설명할 수 있다
- [ ] ANIMATED_DARK 배경 스타일이 어떻게 적용되는지 설명할 수 있다

**실무 활용**:
- [ ] AI에게 컴포넌트 수정을 효과적으로 요청할 수 있다 ("S5 슬라이드에서 이미지가 너무 크다" 등)
- [ ] 타입 에러 발생 시 AI에게 정확한 에러 메시지를 전달하여 해결 요청 가능

**문제 해결**:
- [ ] Remotion 미리보기 에러 발생 시 브라우저 콘솔 확인 방법을 안다

#### 예상 시간 배분

- data.ts 생성: 45분 (25%)
- 슬라이드 컴포넌트 개발: 90분 (50%)
- 이미지 통합 및 미리보기: 30분 (17%)
- 버퍼: 15분 (8%)
- **합계**: ~3시간

#### 참조 자료

- 기존 Remotion 프로젝트: `Ingest/CatchUpAI_VL/Topics/Remotion-VideoCreation/my-first-video/`
- tehaleh-video-prompt.md Phase 3.4: 컴포넌트 구조
- tehaleh-video-prompt.md Phase 3.2: 기술 사양 (Composition ID, 배경 스타일, 해상도)

---

### M4 - 오디오 생성·최종 렌더링 (Capstone)

**난이도**: ⭐⭐
**예상 시간**: ~1.5시간
**산출물 폴더**: `04-AudioRender/`

#### 학습 목표

- [ ] edge-tts(ko-KR-SunHiNeural)로 슬라이드별 한국어 나레이션 오디오를 생성할 수 있다
- [ ] 오디오 파일을 Remotion 컴포넌트에 통합할 수 있다
- [ ] `npx remotion render`로 최종 MP4 영상을 렌더링할 수 있다

#### 주요 개념

1. **gen_audio.py**: video-slide-plan.md의 나레이션 텍스트를 읽어 슬라이드별 .mp3/.wav 파일 생성
2. **오디오 동기화**: 각 슬라이드의 오디오 길이에 맞게 durationInFrames 조정 (또는 오디오 길이에 맞게 슬라이드 시간 조정)
3. **렌더링 명령어**: `npx remotion render Root TehalehIntro0619 out/tehaleh-intro-0619.mp4`

#### 실습 과제

**실습 1: edge-tts 오디오 생성** ⭐⭐
- **목적**: video-slide-plan.md의 나레이션을 한국어 TTS로 변환
- **단계**:
  1. 기존 gen_audio.py 스크립트 위치 확인
  2. video-slide-plan.md의 narration 필드를 gen_audio.py에 입력
  3. `python gen_audio.py --plan public/tehaleh-intro-0619/video-slide-plan.md` 실행
  4. 생성된 .mp3 파일을 `public/tehaleh-intro-0619/audio/` 폴더에 저장
  5. 오디오 파일 재생하여 품질 확인
- **예상 시간**: 30분
- **검증**: 슬라이드 수만큼 .mp3 파일 생성 완료, 재생 시 자연스러운 한국어 TTS 확인

**실습 2: 오디오 통합 및 최종 렌더링** ⭐⭐
- **목적**: 오디오가 포함된 최종 MP4 영상 생성
- **단계**:
  1. TehalehIntro0619.tsx에 Audio 컴포넌트로 슬라이드별 오디오 통합
  2. 오디오 길이에 맞게 각 슬라이드 durationInFrames 조정
  3. `npx remotion preview`에서 오디오·영상 동기화 확인
  4. `npx remotion render Root TehalehIntro0619 out/tehaleh-intro-0619.mp4` 실행
  5. 렌더링된 MP4 재생하여 최종 품질 확인
- **예상 시간**: 45분
- **검증**: `out/tehaleh-intro-0619.mp4` 파일 생성, 1920×1080, 음성+영상 동기화 정상

#### 산출물

```
public/tehaleh-intro-0619/
├── video-slide-plan.md
├── image-prompts.md
├── images/
│   ├── mt-rainier-personal.jpg
│   └── (AI 생성 이미지들)
└── audio/
    ├── s00-title.mp3
    ├── s01-section.mp3
    └── (슬라이드별 오디오)

out/
└── tehaleh-intro-0619.mp4   ← 최종 산출물 🎬

04-AudioRender/
└── README.md
```

#### Definition of Done

- [ ] 슬라이드별 한국어 TTS 오디오(.mp3) 생성 완료
- [ ] 오디오가 Remotion 컴포넌트에 통합됨
- [ ] `out/tehaleh-intro-0619.mp4` 파일 생성 완료
- [ ] 영상 해상도 1920×1080 확인
- [ ] 총 영상 길이 ~90-150초 범위
- [ ] 음성·영상 동기화 정상
- [ ] Topic Retrospective 작성 완료

#### Self-Assessment

**개념 이해**:
- [ ] edge-tts gen_audio.py 스크립트의 입력/출력 구조를 설명할 수 있다
- [ ] Remotion render 명령어의 파라미터(Root, CompositionID, 출력경로)를 설명할 수 있다

**실무 활용**:
- [ ] 다음 Remotion 영상 프로젝트에서 동일 워크플로우를 독립적으로 실행할 수 있다
- [ ] 오디오 품질이 낮을 때 TTS 설정 조정 방법을 안다 (Qwen3-TTS 교체 등)

**문제 해결**:
- [ ] 렌더링 실패 시 에러 메시지로 원인을 파악할 수 있다

#### 예상 시간 배분

- TTS 오디오 생성: 30분 (33%)
- 오디오 통합 및 렌더링: 45분 (50%)
- 최종 검토 및 Retrospective: 15분 (17%)
- **합계**: ~1.5시간

#### 참조 자료

- gen_audio.py: 기존 Remotion-VideoCreation 프로젝트 내 위치
- tehaleh-video-prompt.md Phase 3.5: 제작 단계 (3d-3f)
- edge-tts 공식: `ko-KR-SunHiNeural` voice 설정

---

## 📝 WorkLog 작성 가이드

각 학습 세션마다 WorkLog를 작성하여 진행 상황을 추적합니다.

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_Tehaleh-Community-Video.md`
- 예: `vl_worklog/20260621_M1_Tehaleh-Community-Video.md`

**WorkLog 필수 섹션**:
1. 오늘의 학습 목표 (체크리스트)
2. 진행 내용 (실습별 상세 기록)
3. 문제 해결 로그
4. DoD 체크리스트 (모듈 완료 기준)
5. Daily Retrospective
6. 참조 및 산출물

---

## 🔍 Retrospective 가이드

### Daily Retrospective (매일, 5-10분)
WorkLog 내에 작성:
- What went well?
- What could be improved?
- Insights
- Tomorrow's focus

### Module Retrospective (모듈 완료 시, 15-20분)
`vl_worklog/YYYYMMDD_MX_Retrospective.md`:
- 계획 대비 실제 비교
- 핵심 학습 내용
- 발생한 문제와 해결
- Roadmap 정확도 평가
- 다음 모듈 준비사항

### Topic Retrospective (전체 완료 시, 30-60분)
`vl_worklog/20260621_Tehaleh-Community-Video_Final_Retrospective.md`:
- 전체 학습 여정 통계
- VibeLearn AI 방법론 효과성 평가
- 산출물 품질 평가 (MP4 영상 발표 적합성)
- 향후 학습 개선 사항

---

## 📂 전체 폴더 구조

```
Topics/Tehaleh-Community-Video/
├── topic_starter.md
├── vl_prompts/
│   ├── roadmap_prompt.md
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── 20260621_RoadMap_Tehaleh-Community-Video.md
├── vl_worklog/
│   ├── 20260621_M1_Tehaleh-Community-Video.md
│   ├── 20260621_M2_Tehaleh-Community-Video.md
│   ├── 20260621_M3_Tehaleh-Community-Video.md
│   └── 20260621_M4_Tehaleh-Community-Video.md
├── vl_materials/
│   └── tehaleh-research.md
├── 01-Research/
│   └── README.md
├── 02-SlidePlan/
│   └── README.md
├── 03-RemotionDev/
│   └── README.md
└── 04-AudioRender/
    └── README.md

Remotion 프로젝트 (별도 위치):
Ingest/CatchUpAI_VL/Topics/Remotion-VideoCreation/my-first-video/
├── src/
│   └── tehaleh-intro-0619/
│       ├── data.ts
│       ├── TehalehIntro0619.tsx
│       └── slides/
│           ├── TitleSlide.tsx
│           ├── SectionSlide.tsx
│           ├── BulletSlide.tsx
│           ├── StatSlide.tsx
│           ├── QuoteSlide.tsx
│           └── OutroSlide.tsx
├── public/
│   └── tehaleh-intro-0619/
│       ├── video-slide-plan.md
│       ├── image-prompts.md
│       ├── images/
│       └── audio/
└── out/
    └── tehaleh-intro-0619.mp4
```

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | 2026-06-21 | 2026-06-21 | ✅ | 100% | tehaleh-research.md 완성 |
| M2 | 2026-06-21 | 2026-06-21 | ✅ | 100% | video-slide-plan.md + image-prompts.md 완성 |
| M3 | 2026-06-21 | 2026-06-21 | ✅ | 100% | data.ts + TehalehIntro0619.tsx + Root.tsx 완성 |
| M4 | 2026-06-21 | | 🔄 | 43% | edge-tts 15개 완료, MP4 렌더링 Qwen3-TTS 승인 후 |

**범례**:
- ⏳ 대기
- 🔄 진행 중
- ✅ 완료

---

## 🎯 성공 기준

전체 Topic 완료 기준:
- [ ] 4개 모듈 모두 완료 (DoD 100%)
- [ ] tehaleh-research.md (vl_materials/) 완성
- [ ] video-slide-plan.md 완성 (15장 이상)
- [ ] TehalehIntro0619 Remotion 컴포넌트 완성
- [ ] `out/tehaleh-intro-0619.mp4` 최종 렌더링 완료
- [ ] Topic Retrospective 작성 완료
- [ ] 창발 발표(2026-06-26) 데모로 활용 가능한 품질

---

**생성자**: Claude with VibeLearn AI
**Roadmap 버전**: 1.0
**방법론 버전**: VibeLearn AI 2.0
