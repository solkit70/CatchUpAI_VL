# Remotion으로 Clearly App 소개 영상 (한국어) 제작 계획

**작성일**: 2026-02-24
**목표**: 기존 FFmpeg 기반 `clearly-intro-kr.mp4`를 Remotion으로 재제작, 모션그래픽 품질 향상

---

## 배경

기존 `clearly-intro-kr.mp4` (16:28, 38MB)는 FFmpeg 파이프라인으로 제작됨:
- Gemini JPEG 27장 + TTS MP3 27개 → 정적 슬라이드쇼
- 장면 전환: 하드컷 (전환 효과 없음)

Remotion(React 기반 영상 프레임워크)을 사용하면:
- 부드러운 크로스페이드/슬라이드 장면 전환
- 타이틀·섹션·아웃트로에 모션그래픽 적용
- 기존 오디오(MP3) 자산 완전 재사용 (추가 비용 없음)
- Remotion Skills(AI)로 애니메이션 컴포넌트 자동 생성

---

## 기존 자산 현황 (재사용 가능)

| 자산 | 위치 | 수량 | 재사용 여부 |
|------|------|------|------------|
| 한국어 MP3 오디오 | `audio-kr/slide_0.mp3` ~ `slide_26.mp3` | 27개 | ✅ 100% 재사용 |
| Gemini 슬라이드 이미지 | `slides-gemini-kr/1.jpeg` ~ `27.jpeg` | 27개 | ✅ 배경으로 재사용 |
| 실제 스크린샷 | `_files_/*.png` | 8개 | ✅ 특정 슬라이드 오버레이 |
| Remotion 프로젝트 | `Remotion-VideoCreation/my-first-video/` | 기존 | ✅ 확장 (npm install 불필요) |
| Remotion Skills 규칙 | `.agents/skills/remotion-best-practices/` | 27개 | ✅ AI 컴포넌트 생성에 사용 |

---

## 구현 전략

**기존 `my-first-video/` 프로젝트에 새 Composition 추가**
- 이유: node_modules 재설치 없이 즉시 시작, Skills 규칙 그대로 활용

### 슬라이드 구성 전략

총 27개 슬라이드를 3종 컴포넌트로 처리:

| 컴포넌트 타입 | 해당 슬라이드 | 처리 방식 |
|-------------|------------|---------|
| **TitleSlide** | 슬라이드 1 (메인 타이틀) | Remotion Skills — 모션그래픽 |
| **SectionDivider** | 5·9·13·20·25번 (섹션 구분) | Remotion Skills — 슬라이드인 |
| **ContentSlide** | 나머지 일반 슬라이드 | Gemini JPEG + 오디오 + 페이드인 |
| **OutroSlide** | 슬라이드 27 (마무리) | Remotion Skills — 구독 CTA 애니메이션 |

---

## 구현 단계

### Step 1: 오디오 길이 사전 계산
```bash
# 각 MP3 파일의 정확한 재생 시간(초) 추출
# mutagen 또는 ffprobe 활용
# → slideData.ts에 hardcode
```

### Step 2: 자산 복사
```bash
# my-first-video/public/clearly-kr/ 폴더에 복사
audio/slide_0.mp3 ~ slide_26.mp3   (27개 MP3)
slides/1.jpeg ~ 27.jpeg             (27개 JPEG)
screenshots/*.png                   (8개 PNG)
```

### Step 3: 슬라이드 데이터 설정 파일
`my-first-video/src/clearly-kr/slideData.ts`
```ts
export const FPS = 30;
export const SLIDE_DATA = [
  { id: 0, type: 'title',   durationSec: XX.X, screenshot: null },
  { id: 1, type: 'content', durationSec: XX.X, screenshot: null },
  // ...27개 전체
];
```

### Step 4: 핵심 컴포넌트 생성

| 파일 | 생성 방법 | 내용 |
|------|---------|------|
| `SlideWrapper.tsx` | 수동 작성 | 오디오 재생 + 이미지 + 페이드 전환 |
| `TitleSlide.tsx` | Remotion Skills | 그라데이션 배경 + 텍스트 스프링 애니메이션 |
| `SectionDivider.tsx` | Remotion Skills | 섹션 번호 + 제목 슬라이드인 |
| `ContentSlide.tsx` | 수동 작성 | Gemini JPEG 배경 |
| `OutroSlide.tsx` | Remotion Skills | 구독 버튼 펄스 + 링크 표시 |

### Step 5: 메인 Composition
`my-first-video/src/clearly-kr/ClearlyIntroKr.tsx`
```tsx
// 27개 Series.Sequence로 전체 영상 구성
<Series>
  {SLIDE_DATA.map((slide) => (
    <Series.Sequence durationInFrames={Math.round(slide.durationSec * FPS)}>
      <SlideWrapper {...slide} />
    </Series.Sequence>
  ))}
</Series>
```

### Step 6: Root.tsx에 Composition 등록
```tsx
<Composition id="ClearlyIntroKr" component={ClearlyIntroKr}
  durationInFrames={totalFrames} fps={30} width={1920} height={1080} />
```

### Step 7: 미리보기 & 렌더링
```bash
cd Topics/Remotion-VideoCreation/my-first-video
npx remotion studio                    # Studio에서 미리보기
npx remotion render ClearlyIntroKr \
  out/clearly-intro-kr-remotion.mp4 \
  --video-bitrate 8M
```

---

## 완성 후 파일 구조

```
my-first-video/
├── src/
│   ├── Root.tsx                              # ClearlyIntroKr 추가
│   └── clearly-kr/
│       ├── ClearlyIntroKr.tsx               # 메인 Composition
│       ├── slideData.ts                     # 슬라이드 설정 + 오디오 길이
│       ├── SlideWrapper.tsx                 # 공통 래퍼
│       ├── TitleSlide.tsx                   # 타이틀 (Skills)
│       ├── SectionDivider.tsx               # 섹션 구분 (Skills)
│       ├── ContentSlide.tsx                 # 일반 슬라이드
│       └── OutroSlide.tsx                   # 아웃트로 (Skills)
└── public/clearly-kr/
    ├── audio/slide_0.mp3 ~ slide_26.mp3     # 27개 MP3
    ├── slides/1.jpeg ~ 27.jpeg              # 27개 JPEG
    └── screenshots/                         # 8개 PNG

산출물: my-first-video/out/clearly-intro-kr-remotion.mp4
```

---

## 예상 품질 개선

| 항목 | 기존 (FFmpeg) | Remotion 버전 |
|------|-------------|--------------|
| 장면 전환 | 하드컷 | 크로스페이드 (0.5초) |
| 타이틀 슬라이드 | 정적 이미지 | 스프링 애니메이션 |
| 섹션 구분 | 정적 이미지 | 슬라이드인 + 강조 효과 |
| 아웃트로 | 정적 이미지 | 구독 버튼 펄스 애니메이션 |
| 오디오 | 동일 (TTS) | 동일 (재사용) |
| 총 길이 | 16:28 | 동일 (~16:28) |
| 해상도 | 1920×1080 | 1920×1080 |

---

## 참고 파일

| 파일 | 경로 | 용도 |
|------|------|------|
| 기존 최종 영상 통합 코드 | `my-first-video/src/VibeLearnIntro.tsx` | Series 패턴 참조 |
| 설명 장면 코드 | `my-first-video/src/ExplanationScene.tsx` | 스태거 애니메이션 참조 |
| 오디오 규칙 | `.agents/skills/.../rules/audio.md` | 오디오 싱크 패턴 |
| 타이밍 규칙 | `.agents/skills/.../rules/timing.md` | spring/interpolate 설정 |
| 한국어 스크립트 | `clearly-intro-script-kr.md` | 슬라이드 내용 참조 |
| 슬라이드 MD | `clearly-intro-script-kr - slides.md` | 섹션 구조 파악 |
