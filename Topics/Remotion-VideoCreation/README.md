# Remotion-VideoCreation — Topic 인덱스

> **Topic**: Remotion-VideoCreation
> **방법론**: VibeLearn AI v2.0
> **최초 완료일**: 2026-02-10 (M1~M6)
> **CVL 업데이트**: 2026-05-29 (프로덕션 진화 동기화)
> **상태**: 완료 → 실제 프로덕션 도구로 운용 중

---

## 이 Topic에 대하여

React 기반 영상 제작 프레임워크 **Remotion**을 학습하고, 실제 YouTube 채널 `@catchupai`의 모든 영상을 이 파이프라인으로 제작 중입니다.

학습(M1~M6) 완료 후 3.5개월 동안 **16개 프로젝트(30+ 영상 편)**를 제작하면서 실질적인 프로덕션 파이프라인으로 진화했습니다.

---

## 모듈 목록

| 모듈 | 제목 | 상태 | 링크 |
|------|------|------|------|
| M1 | 환경 설정 & Remotion 프로젝트 시작 | ✅ 완료 | [01-Setup/README.md](01-Setup/README.md) |
| M2 | Core 기초 (interpolate, spring, Sequence) | ✅ 완료 | [02-Core-Basics/README.md](02-Core-Basics/README.md) |
| M3 | 모션그래픽 컴포넌트 패턴 | ✅ 완료 | [03-Motion-Graphics/README.md](03-Motion-Graphics/README.md) |
| M4 | Remotion Skills (AI 기반 영상 생성) | ✅ 완료 | [04-Skills/README.md](04-Skills/README.md) |
| M5 | 렌더링 & YouTube 최적화 | ✅ 완료 | [05-Rendering/README.md](05-Rendering/README.md) |
| M6 | Capstone — 실전 YouTube 영상 제작 | ✅ 완료 | [06-YouTube-Project/README.md](06-YouTube-Project/README.md) |
| M7 | Rich Media (TTS 오디오·자막·Lottie) | ✅ 완료 | [07-Rich-Media/README.md](07-Rich-Media/README.md) |

---

## 프로젝트 구조

```
Remotion-VideoCreation/
├── my-first-video/         ← Remotion 프로젝트 루트 (실제 제작 공간)
│   ├── src/
│   │   ├── Root.tsx        ← 전체 Composition 등록
│   │   ├── [project]/      ← 영상별 폴더
│   │   │   ├── [Video].tsx      ← 한국어 컴포넌트
│   │   │   ├── [Video]EN.tsx    ← 영어 컴포넌트
│   │   │   ├── data.ts          ← 한국어 슬라이드 데이터
│   │   │   ├── data_en.ts       ← 영어 슬라이드 데이터
│   │   │   ├── gen_audio.py     ← 한국어 TTS (edge-tts)
│   │   │   └── gen_audio_en.py  ← 영어 TTS
│   │   └── ...
│   └── public/
│       └── [project]/assets/   ← 사진, 생성 이미지
├── 01-Setup/ ~ 07-Rich-Media/  ← 학습 모듈 산출물
├── vl_worklog/                 ← 학습 일지 & CVL 기록
├── vl_roadmap/                 ← 원 학습 로드맵
└── topic_info.md               ← Topic 기본 정보
```

---

## 핵심 프로덕션 패턴

### 슬라이드 데이터 아키텍처

모든 영상은 `data.ts`에 슬라이드 데이터를 분리하고, `TOTAL_FRAMES`를 자동 계산합니다.

```typescript
// data.ts
export const SLIDE_DATA: SlideData[] = [
  { id: 0, type: "title", durationSec: 8, audioSrc: "audio/audio_00.wav" },
  { id: 1, type: "section", durationSec: 4, audioSrc: null },
  { id: 2, type: "photo", durationSec: 22, audioSrc: "audio/audio_02.wav",
    steps: ["포인트 1", "포인트 2", "포인트 3"] },
];
export const TOTAL_FRAMES = getSlideDurationSec(SLIDE_DATA) * FPS;
```

### TTS 오디오 파이프라인

```
gen_audio.py 실행
  → edge-tts로 WAV 생성 (AUDIO_HEAD_PAD 0.8s + 나레이션 + AUDIO_TAIL_PAD 0.3s)
  → ffprobe로 실제 길이 측정
  → AUDIO_DURATIONS 딕셔너리에 기입
  → data.ts의 durationSec에 반영
```

**기본 TTS**: `ko-KR-SunHiNeural` (한국어) / `en-US-JennyNeural` (영어) — edge-tts (무료)
**실험적**: Qwen3-TTS Voice Clone (`changsoo_final.wav`) — Live #11부터 적용

### 한·영 병렬 제작

```typescript
// Root.tsx 등록 패턴
import { LiveXVideo } from "./live-MMDD/LiveXVideo";
import { TOTAL_FRAMES } from "./live-MMDD/data";
import { LiveXVideoEN } from "./live-MMDD/LiveXVideoEN";
import { TOTAL_FRAMES as EN_TOTAL_FRAMES } from "./live-MMDD/data_en";
```

### 이미지 생성 기본값

| 종류 | 도구 | 저장 경로 |
|------|------|----------|
| 썸네일·사진형·텍스트 포함 | `gpt-image-2` (OpenAI) | `public/[project]/assets/` |
| 인포그래픽·다이어그램 | Gemini Image Skill | `public/[project]/assets/` |
| 실제 촬영 사진 | 직접 제공 | `public/[project]/assets/` |

---

## 영상 제작 워크플로우 (전체)

자세한 내용은 `_Settings_/Skills/remotion-video/SKILL.md` 참조.

```
1. [입력] 방송 트랜스크립트 / 클리핑 / 아이디어
2. [Phase 1] video-slide-plan.md 작성 → 사용자 리뷰
3. [Phase 1.5] AI 이미지 생성 (필요 슬라이드)
4. [Phase 2] data.ts + 컴포넌트 구현 → npm run dev 미리보기
5. [Phase 3] gen_audio.py 실행 → ffprobe 길이 측정 → durationSec 업데이트
6. [Phase 4] npx remotion render [CompositionId] out/[filename].mp4
```

---

## 제작 완료 영상 목록

| 날짜 | 영상 | 폴더 | 유튜브 |
|------|------|------|--------|
| 2026-03 | Clearly App 소개 | `clearly-kr/en` | — |
| 2026-04 | WaTech IT Forum 리포트 | `watech-report` | — |
| 2026-04 | 역사적 노동 전환 만화 | `comic` | — |
| 2026-04 | 잔디 관리 강좌 | `lawn-care-kr/en` | — |
| 2026-04 | Live #6 하이라이트 | `live6-highlight` | — |
| 2026-04 | Live #7 하이라이트 | `live7-highlight` | — |
| 2026-05-01 | AI 시대 휴먼터치 | `ai-human-touch-0501` | — |
| 2026-05-03 | Live #8 하이라이트 | `ai-action-8-0503` | — |
| 2026-05-07 | 시애틀 AI 민심 | `seattle-ai-0507` | — |
| 2026-05-10 | Live #9 하이라이트 | `ai-action-0510` | — |
| 2026-05-17 | Live #10 하이라이트 | `live10-0517` | [KR](https://youtu.be/k8iksu8C6uI) · [EN](https://youtu.be/qTNVc_PIWQw) |
| 2026-05-19 | 모자무싸 에세이 | `mojamussa-0519` | [KR](https://youtu.be/ApWkZu0RcWE) |
| 2026-05-24 | Live #11 하이라이트 | `live11-0524` | [KR](https://youtu.be/ApWkZu0RcWE) · [EN](https://youtu.be/VL-S43gnhe0) |

---

## CVL WorkLog

- [vl_worklog/20260529_CVL_Remotion-VideoCreation.md](vl_worklog/20260529_CVL_Remotion-VideoCreation.md) — 프로덕션 진화 동기화 (최초 CVL)
- [vl_worklog/20260210_Remotion-VideoCreation_Final_Retrospective.md](vl_worklog/20260210_Remotion-VideoCreation_Final_Retrospective.md) — 최초 학습 완료 회고

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
