# WorkLog - M4: Remotion으로 Clearly 앱 소개 영상 제작

**날짜**: 2026-02-25
**Topic**: Clearly-BRD-PRD
**모듈**: M4 - Remotion 영상 제작 (한국어)
**이전 세션**: [20260224_M3_Clearly-BRD-PRD.md](20260224_M3_Clearly-BRD-PRD.md)
**계획 문서**: [remotion-kr-plan.md](../03-Clearly-Intro-Video/remotion-kr-plan.md)

---

## 오늘의 학습 목표

- [x] Step 1: 27개 MP3 오디오 길이 계산 → `slideData.ts`
- [x] Step 2: 자산 복사 (`public/clearly-kr/`)
- [x] Step 3: 슬라이드 설정 파일 생성 (`slideData.ts`)
- [x] Step 4: 핵심 컴포넌트 생성 (`ClearlySlide.tsx`)
- [x] Step 5: 메인 Composition 생성 (`ClearlyIntroKr.tsx`)
- [x] Step 6: `Root.tsx`에 Composition 등록
- [x] Step 7: 최종 MP4 렌더링 완료 (KR + EN)

---

## 작업 컨텍스트

**기존 FFmpeg 영상**: `clearly-intro-kr.mp4` (16:28, 38MB) — 정적 슬라이드쇼

**Remotion으로 개선하는 점**:
- 하드컷 → 크로스페이드 장면 전환
- 타이틀·섹션·아웃트로 모션그래픽
- 기존 오디오(27개 MP3) 100% 재사용

**Remotion 프로젝트**: `Topics/Remotion-VideoCreation/my-first-video/` (기존 확장)

---

## 진행 내용

<!-- 작업하면서 아래에 채워 넣음 -->

### Step 1: 오디오 길이 계산 ✅

`ffprobe`로 27개 MP3 정확한 길이 측정:

| 슬라이드 | 오디오 파일 | 길이(초) |
|---------|-----------|---------|
| 1 | slide_0.mp3 | 35.352 |
| 2 | slide_1.mp3 | 22.104 |
| 3 | slide_2.mp3 | 29.856 |
| 4 | slide_3.mp3 | 26.208 |
| 5 | slide_4.mp3 | 30.408 |
| 6 | slide_5.mp3 | 39.912 |
| 7 | slide_6.mp3 | 39.552 |
| 8 | slide_7.mp3 | 37.752 |
| 9 | slide_8.mp3 | 52.200 |
| 10 | slide_9.mp3 | 33.312 |
| 11 | slide_10.mp3 | 37.848 |
| 12 | slide_11.mp3 | 33.120 |
| 13 | slide_12.mp3 | 37.056 |
| 14 | slide_13.mp3 | 40.512 |
| 15 | slide_14.mp3 | 36.168 |
| 16 | slide_15.mp3 | 57.768 |
| 17 | slide_16.mp3 | 41.016 |
| 18 | slide_17.mp3 | 34.560 |
| 19 | slide_18.mp3 | 43.656 |
| 20 | slide_19.mp3 | 44.952 |
| 21 | slide_20.mp3 | 31.848 |
| 22 | slide_21.mp3 | 27.264 |
| 23 | slide_22.mp3 | 37.152 |
| 24 | slide_23.mp3 | 35.616 |
| 25 | slide_24.mp3 | 38.712 |
| 26 | slide_25.mp3 | 32.712 |
| 27 | slide_26.mp3 | 31.968 |

**총 길이**: 988.584초 = 29,658 프레임 (30fps)

---

### Step 2: 자산 복사 ✅

`my-first-video/public/clearly-kr/` 폴더에 복사:
- `audio/`: 27개 MP3 (slide_0.mp3 ~ slide_26.mp3)
- `slides/`: 27개 JPEG (1.jpeg ~ 27.jpeg, Gemini 생성)
- `screenshots/`: 8개 PNG (앱 실제 스크린샷)

---

### Step 3: `slideData.ts` 생성 ✅

`my-first-video/src/clearly-kr/slideData.ts` 생성:
- `FPS = 30`, `FADE_FRAMES = 15` (0.5초 페이드)
- `SlideConfig` 타입 정의 (audioIndex, slideNum, type, durationSec, screenshot)
- 27개 슬라이드 설정 + `TOTAL_FRAMES = 29658`

슬라이드 타입 분류:
- `title` (1개): slide 1
- `content-screenshot` (8개): slides 4, 9, 13, 14, 17, 18, 19, 24
- `outro` (1개): slide 27
- `content` (17개): 나머지

---

### Step 4 & 5: Remotion 컴포넌트 생성 ✅

**`ClearlySlide.tsx`**:
- Gemini JPEG를 배경 이미지로 표시
- `content-screenshot` 타입: 반투명 오버레이 위에 실제 PNG 스크린샷 표시
- `Audio` 컴포넌트로 MP3 재생
- 시작 페이드인 + 끝 페이드아웃 (interpolate로 처리, 첫/마지막 슬라이드 예외)

**`ClearlyIntroKr.tsx`**:
- `Series` + `Series.Sequence`로 27개 슬라이드 순차 재생
- `durationInFrames = Math.round(durationSec * FPS)` 정확한 오디오 길이 매핑

---

### Step 6: Root.tsx 등록 ✅

```tsx
<Composition
  id="ClearlyIntroKr"
  component={ClearlyIntroKr}
  durationInFrames={TOTAL_FRAMES}  // 29658
  fps={30}
  width={1920}
  height={1080}
/>
```

---

### Step 7: MP4 렌더링 ✅

**한국어 (ClearlyIntroKr)**:
```bash
cd my-first-video
npx remotion render ClearlyIntroKr out/clearly-intro-kr-remotion.mp4 --video-bitrate=8M
```
- 파일: `out/clearly-intro-kr-remotion.mp4`
- 재생 시간: **16분 28초** (988.6초)
- 파일 크기: **213 MB**
- 해상도: 1920×1080 (Full HD)
- 렌더링: 29,657 프레임 완료

**영어 (ClearlyIntroEn)**:
```bash
npx remotion render ClearlyIntroEn out/clearly-intro-en-remotion.mp4 --video-bitrate=8M
```
- 파일: `out/clearly-intro-en-remotion.mp4`
- 재생 시간: **13분 48초** (828.3초)
- 파일 크기: **202 MB**
- 해상도: 1920×1080 (Full HD)
- 렌더링: 24,849 프레임 완료

---

## DoD 체크리스트

| 항목 | 상태 |
|------|------|
| EN 자산 복사 (`public/clearly-en/`) | ✅ |
| `src/clearly-kr/slideData.ts` | ✅ |
| `src/clearly-kr/ClearlySlide.tsx` | ✅ |
| `src/clearly-kr/ClearlyIntroKr.tsx` | ✅ |
| `src/clearly-en/slideData.ts` | ✅ |
| `src/clearly-en/ClearlySlide.tsx` | ✅ |
| `src/clearly-en/ClearlyIntroEn.tsx` | ✅ |
| `Root.tsx` 등록 (KR + EN) | ✅ |
| `out/clearly-intro-kr-remotion.mp4` 렌더링 | ✅ |
| `out/clearly-intro-en-remotion.mp4` 렌더링 | ✅ |
| WorkLog 작성 | ✅ |
| GitHub 커밋 & 푸시 | ✅ |

---

## Daily Retrospective

### What went well

- **자산 재사용 100%**: 기존 27개 MP3, 27개 Gemini JPEG, 8개 스크린샷 PNG를 모두 재사용 — 추가 API 비용 없음
- **KR/EN 공통 구조**: `slideData.ts` + `ClearlySlide.tsx` + `ClearlyIntroKr/En.tsx` 패턴이 두 언어 모두 동일하게 적용 → EN 버전 추가 시간이 크게 단축
- **Series 패턴의 정확성**: `durationInFrames = Math.round(durationSec * FPS)`로 각 슬라이드가 오디오 길이에 정확히 맞춰짐

### What could be improved

- **렌더링 속도**: 29,657 프레임에 약 25분 소요. 프레임별 복잡도가 낮은 슬라이드쇼 형식임에도 Remotion은 모든 프레임을 렌더링함
- **파일 크기**: 213 MB (KR) — FFmpeg 버전 38 MB 대비 크게 증가. `--video-bitrate`를 낮추면 크기 조정 가능

### 전체 인사이트

- **Remotion 슬라이드쇼 패턴**: `staticFile()` + `Audio` + `Img` + `interpolate()` 조합으로 오디오 싱크 슬라이드쇼를 React 컴포넌트로 표현 가능
- **페이드 전환**: 이전 슬라이드의 fadeOut과 다음 슬라이드의 fadeIn이 `Series.Sequence` 경계에서 자연스럽게 교차됨
- **공용 폴더 구조**: `public/clearly-kr/` + `public/clearly-en/` 분리로 두 언어가 독립적으로 관리됨

---

## 산출물 요약

### 생성된 파일

| 파일 | 설명 |
|------|------|
| `src/clearly-kr/slideData.ts` | KR 27개 슬라이드 설정 |
| `src/clearly-kr/ClearlySlide.tsx` | KR 슬라이드 컴포넌트 |
| `src/clearly-kr/ClearlyIntroKr.tsx` | KR 메인 Composition |
| `src/clearly-en/slideData.ts` | EN 27개 슬라이드 설정 |
| `src/clearly-en/ClearlySlide.tsx` | EN 슬라이드 컴포넌트 |
| `src/clearly-en/ClearlyIntroEn.tsx` | EN 메인 Composition |
| `public/clearly-kr/` | KR 자산 (audio 27 + slides 27 + screenshots 8) |
| `public/clearly-en/` | EN 자산 (audio 27 + slides 27 + screenshots 8) |
| `out/clearly-intro-kr-remotion.mp4` | **KR 최종 영상 (16:28, 213 MB)** |
| `out/clearly-intro-en-remotion.mp4` | **EN 최종 영상 (13:48, 202 MB)** |

---

**작성자**: CUA_VL 학습자
**방법론**: CUA_VL (VibeLearn AI)

