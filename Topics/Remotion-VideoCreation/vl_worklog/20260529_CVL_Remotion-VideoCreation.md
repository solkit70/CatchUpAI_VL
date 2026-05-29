# 🔄 CVL WorkLog: Remotion-VideoCreation 프로덕션 진화 동기화

**작성일**: 2026-05-29
**세션 유형**: CVL (Continuous Vibe Learning) — 첫 번째 CVL 세션
**Topic**: Remotion-VideoCreation
**관련 업데이트 기간**: 2026-02-10 ~ 2026-05-29 (약 3.5개월)
**이전 CVL**: 없음 (최초 CVL)

---

## 🔄 Continuous Vibe Learning - 업데이트 개요

### 동기화 일시
2026-05-29

### 버전 변화
- **최초 학습 시**: Remotion v4.0.x (2026-02-05 기준)
- **현재**: v4.0.456 (패치 업데이트, Breaking change 없음)
- **영향도**: 🟢 **낮음** — API 변경 없음. 패키지 업그레이드만 필요 시 수행

---

## 📋 학습 완료 이후 진화 요약 (2026-02-10 → 2026-05-29)

### 제작 완료 영상 목록 (16개 프로젝트, 한·영 포함 30+ 편)

| 날짜 | 프로젝트 | 폴더 | 언어 |
|------|---------|------|------|
| 2026-02 | VibeLearn AI 소개 | `src/` | KR |
| 2026-03 | Clearly App 소개 | `clearly-kr`, `clearly-en` | KR·EN |
| 2026-03 | VibeLearn AI 인트로 v1/v2 | `vibelearn-kr`, `vibelearn-kr-v2` | KR |
| 2026-04 | WaTech IT Forum 리포트 | `watech-report`, `watech-report-en` | KR·EN |
| 2026-04 | 역사적 노동 전환 만화 | `comic` | KR·EN |
| 2026-04 | 잔디 관리 강좌 | `lawn-care-kr`, `lawn-care-en` | KR·EN |
| 2026-04 | AI in Action Live #6 요약 | `weekly-roundup-0419` | KR |
| 2026-04 | Live #6 하이라이트 | `live6-highlight` | KR·EN |
| 2026-04 | Live #7 하이라이트 | `live7-highlight` | KR·EN |
| 2026-05-01 | AI 시대 휴먼터치 | `ai-human-touch-0501` | KR·EN |
| 2026-05-03 | Live #8 하이라이트 | `ai-action-8-0503` | KR·EN |
| 2026-05-07 | 시애틀 AI 민심 | `seattle-ai-0507` | KR·EN |
| 2026-05-10 | Live #9 (AI in Action 0510) | `ai-action-0510` | KR·EN |
| 2026-05-17 | Live #10 하이라이트 | `live10-0517` | KR·EN |
| 2026-05-19 | 모자무싸 에세이 | `mojamussa-0519` | KR·EN |
| 2026-05-24 | Live #11 하이라이트 | `live11-0524` | KR·EN |

---

## 📊 핵심 진화 패턴 (학습 산출물에 없던 새 패턴)

### 패턴 1: 슬라이드 데이터 아키텍처 🆕

초기 학습(M1~M6)에서는 컴포넌트에 Props를 직접 전달했다. 프로덕션에서는 `data.ts` 파일에 슬라이드 데이터를 분리하는 패턴이 표준화됐다.

```typescript
// data.ts 표준 패턴
export const SLIDE_DATA: SlideData[] = [
  { id: 0, type: "title", durationSec: 8, ... },
  { id: 1, type: "section", durationSec: 4, audioSrc: null },
  { id: 2, type: "photo", durationSec: 22, audioSrc: "audio/audio_02.wav", ... },
];

export const TOTAL_FRAMES = getSlideDurationSec(SLIDE_DATA) * FPS;

// 한·영 병렬: data_en.ts도 동일 구조
export const TOTAL_FRAMES_EN = ...;
```

**의의**: Root.tsx에서 `TOTAL_FRAMES`로 Composition 길이를 자동 계산 → 슬라이드 추가/삭제 시 자동 반영

### 패턴 2: TTS 오디오 파이프라인 표준화 🆕

M7(07-Rich-Media)에서 개념으로만 다뤘던 TTS 오디오가 프로덕션 표준이 됐다.

```python
# gen_audio.py 표준 패턴
AUDIO_HEAD_PAD_SEC = 0.8   # 나레이션 시작 전 여백
AUDIO_TAIL_PAD_SEC = 0.3   # 나레이션 종료 후 여백

# edge-tts (기본, 무료)
async def generate_audio(text, output_path, voice="ko-KR-SunHiNeural"):
    ...

# ffprobe로 실측 후 AUDIO_DURATIONS 딕셔너리에 기입
AUDIO_DURATIONS = {
    "audio_00_title.wav": 8.24,
    "audio_02_photo.wav": 21.6,
    ...
}
```

**의의**: 슬라이드 길이 = 오디오 길이 + 패딩 → 자동 동기화

### 패턴 3: 한·영 병렬 제작 워크플로우 🆕

모든 영상을 한국어·영어 동시 제작하는 패턴이 정착됐다.

```
src/[project]/
├── [VideoName].tsx       ← 한국어 컴포넌트
├── [VideoName]EN.tsx     ← 영어 컴포넌트 (구조 동일, 나레이션만 다름)
├── data.ts               ← 한국어 슬라이드 데이터
├── data_en.ts            ← 영어 슬라이드 데이터
├── gen_audio.py          ← 한국어 TTS
└── gen_audio_en.py       ← 영어 TTS
```

**Root.tsx 등록 패턴**:
```typescript
import { Live11Video } from "./live11-0524/Live11Video";
import { TOTAL_FRAMES as LIVE11_TOTAL_FRAMES } from "./live11-0524/data";
import { Live11VideoEN } from "./live11-0524/Live11VideoEN";
import { TOTAL_FRAMES as LIVE11_EN_TOTAL_FRAMES } from "./live11-0524/data_en";
```

### 패턴 4: 이미지 생성 통합 🆕

| 이미지 종류 | 도구 | 이유 |
|-----------|------|------|
| 썸네일, 사진형 | `gpt-image-2` (OpenAI) | 리얼리즘, 텍스트 표현력 |
| 인포그래픽, 다이어그램 | Gemini Image | Dense 정보 시각화 |
| 직접 제공 사진 | `public/[project]/assets/` | 실제 행사 사진 등 |

저장 경로: `public/[project-folder]/assets/[filename].png`

### 패턴 5: PhotoSlide with steps[] 순차 공개 🆕

```typescript
// data.ts에서 steps 배열로 순차 정보 공개
{
  type: "photo",
  steps: [
    "첫 번째 포인트",
    "두 번째 포인트",
    "세 번째 포인트"
  ],
  imageSrc: "assets/photo.png"
}
```

**의의**: 단순 bullet 대신 영상 진행에 맞춰 정보를 순차적으로 공개

### 패턴 6: Qwen3-TTS Voice Clone 도입 (실험적) 🆕

```python
# gen_audio_qwen.py — Alibaba DashScope API 활용
VC_MODEL = "qwen3-tts-vc-2026-01-22"
VC_CHANGSOO = "qwen-tts-vc-changsoo-voice-20260526021509918-daf1"
# changsoo_final.wav: 샘플 v4 + 쉼표 강화 텍스트 + atempo 1.08x
```

현재 live11-0524에 적용됨. 품질 기준: 창수 클론 4/5 도달 목표.

---

## 📊 영향도 종합 평가

| 변경사항 | 영향도 | Breaking | 조치 완료 |
|---------|--------|---------|---------|
| Remotion v4.0.456 패치 | 🟢 낮음 | ❌ | ✅ 자동 적용 |
| M7 Rich-Media 모듈 추가 | 🆕 신규 | ❌ | ✅ 07-Rich-Media 폴더 존재 |
| 슬라이드 데이터 아키텍처 | 🆕 신규 패턴 | ❌ | ✅ Topic README에 문서화 |
| TTS 오디오 파이프라인 | 🆕 신규 패턴 | ❌ | ✅ remotion-video SKILL.md에 반영 |
| 한·영 병렬 제작 | 🆕 신규 패턴 | ❌ | ✅ Topic README에 문서화 |
| gpt-image-2 이미지 기본값 | 🆕 신규 | ❌ | ✅ remotion-video SKILL.md에 반영 |
| Qwen3-TTS Voice Clone | 🆕 실험적 | ❌ | ✅ 메모 |
| Topic README.md 없음 | 📋 Gap | — | ✅ 신규 생성 |

---

## 📝 업데이트 완료 파일 목록

- [x] `vl_worklog/20260529_CVL_Remotion-VideoCreation.md` — 이 파일 (신규)
- [x] `README.md` — 토픽 레벨 README 신규 생성 (프로덕션 현황 반영)
- [x] `_Settings_/Skills/remotion-video/SKILL.md` — 이미 최신 상태 (업데이트 불필요)

---

## 🎯 오늘 배운 것 / 인사이트

- 3.5개월 만에 학습 프로젝트에서 실제 YouTube 채널 프로덕션 도구로 완전히 진화했다.
- CVL을 한 번도 하지 않았는데 코드는 계속 쌓이고 문서는 구버전에 머물러 있었다. **문서 부채(Documentation Debt)** 가 쌓이는 전형적 패턴.
- `data.ts` 아키텍처가 핵심 — 이걸 하나의 패턴으로 문서화해두면 새 영상 시작할 때마다 재발명 없이 바로 적용 가능.
- edge-tts + gpt-image-2 조합이 현재 최적 기본값으로 정착됐다.

## ✅ 잘된 점

- remotion-video SKILL.md가 이미 잘 작성되어 있어 새 영상 제작 시 가이드로 잘 활용됨
- 한·영 병렬 제작 패턴이 Root.tsx 등록 방식으로 일관성 있게 정착

## 📋 다음 할 일

- [ ] Qwen3-TTS Voice Clone 품질을 live11 수준에서 더 개선
- [ ] `@remotion/captions` Whisper 자막 실습 (07-Rich-Media에서 학습했으나 미적용)
- [ ] Live #12 영상 제작 — live12-0531 폴더 생성 예정
- [ ] Lottie 애니메이션 아이콘 적용 실험

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0 CVL
> **마지막 업데이트**: 2026-05-29
