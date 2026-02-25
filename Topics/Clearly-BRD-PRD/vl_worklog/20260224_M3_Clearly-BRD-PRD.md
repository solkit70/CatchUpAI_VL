# WorkLog - M3: Clearly 앱 소개 영상 제작 (4일차 - 영어 버전)

**날짜**: 2026-02-24
**Topic**: Clearly-BRD-PRD
**모듈**: M3 - Clearly App 소개 영상 제작
**이전 세션**: [20260223_M3_Clearly-BRD-PRD.md](20260223_M3_Clearly-BRD-PRD.md)

---

## 오늘의 학습 목표

- [x] 영어 스크립트 (`clearly-intro-script-en.md`) 확인
- [x] 영어 슬라이드 MD (`clearly-intro-script-en - slides.md`) 확인
- [x] 영어 오디오 (`audio-en/`) 확인
- [x] Gemini 슬라이드 이미지 영어 전용 생성 (`slides-gemini-en/`)
- [x] `clearly-intro-en.mp4` 생성
- [x] WorkLog 작성 + GitHub 커밋

---

## 작업 컨텍스트

**3일차(2/24) 세션에서 이어지는 작업입니다.**

| 전 세션 완료 | 이번 세션 목표 |
|------------|-------------|
| 한국어 MP4 최종 완료 (`clearly-intro-kr.mp4`) | 영어 버전 MP4 제작 |
| 영어 스크립트 번역 완료 | 영어 슬라이드 이미지 생성 (영어 전용) |
| 영어 오디오 생성 완료 (`audio-en/`, 27개) | `clearly-intro-en.mp4` 합성 |

**현재 상태**: **M3 한국어 + 영어 버전 완전 완료 ✅**

---

## 진행 내용

### 1단계: 현재 상태 파악

**확인된 파일:**
- ✅ `clearly-intro-script-en.md` — 영어 나레이션 스크립트 (27슬라이드)
- ✅ `clearly-intro-script-en - slides.md` — Deckset 슬라이드 (영어)
- ✅ `audio-en/slide_0.mp3` ~ `slide_26.mp3` — 27개 MP3 완료
- ❌ `slides-gemini-en/` — 비어 있음 (이미지 미생성)
- ❌ `clearly-intro-en.mp4` — 미생성

---

### 2단계: 문제 발견 — 한국어/영어 혼재

초기 슬라이드 생성 시도에서 **슬라이드 4장에 한국어+영어 혼재** 발생.

**원인 분석**:
- `create_slides_gemini.py`의 프롬프트 마지막 줄에 하드코딩:
  ```python
  Include Korean text labels where appropriate.
  ```
- 영어 스크립트로 슬라이드를 생성해도 Gemini가 한국어를 포함시킴

**즉시 중단** → 생성된 4장 삭제 → 스크립트 수정 후 재생성

---

### 3단계: 스크립트 수정 ✅

**`create_slides_gemini.py` 수정**:
- `--language en/ko` 파라미터 추가
- `convert_slide_to_prompt()` 함수에 언어별 분기 추가:
  ```python
  if language == "en":
      lang_instruction = "Use English text labels only. All text in the image must be in English. Do not include any Korean or other non-English text."
  else:
      lang_instruction = "Include Korean text labels where appropriate."
  ```
- dry_run 경로 및 실제 생성 경로 모두 `language=args.language` 전달

**`make_video.py` 수정**:
- 각 언어 config에 `gemini_language` 키 추가:
  - `"kr"` config: `"gemini_language": "ko"`
  - `"en"` config: `"gemini_language": "en"`
- Step 2 Gemini 슬라이드 생성 시 `--language {config["gemini_language"]}` 자동 전달

> **참고**: `Topics/Claude-Skills/` 폴더는 `.gitignore`에 포함되어 있어 스크립트 변경사항은 git에 포함되지 않음.

---

### 4단계: Gemini 슬라이드 이미지 생성 ✅

```bash
cd 03-Clearly-Intro-Video
PYTHONUTF8=1 GEMINI_API_KEY="..." python make_video.py --lang en --slides-only
```

**결과**:
- Generated: **27** / Skipped: 0 / Failed: 0
- 파일: `slides-gemini-en/1.jpeg` ~ `27.jpeg`, 1920×1080
- 예상 비용: **~$1.05**
- 슬라이드 텍스트: **영어 전용** ✅

---

### 5단계: MP4 합성 ✅

```bash
PYTHONUTF8=1 python make_video.py --lang en --video-only
```

**슬라이드-오디오 매핑 (27개 전체)**:

| 슬라이드 | 오디오 | 길이 |
|---------|--------|------|
| 1.jpeg | slide_0.mp3 | 0:27 |
| 2.jpeg | slide_1.mp3 | 0:19 |
| ... | ... | ... |
| 27.jpeg | slide_26.mp3 | 0:25 |

**최종 결과**:
- 파일: `clearly-intro-en.mp4`
- 재생 시간: **13분 48초** (828초)
- 파일 크기: **27 MB**
- 해상도: 1920×1080 (Full HD)
- 오디오: alloy 보이스, gpt-4o-mini-tts

---

## DoD 체크리스트

| 항목 | 상태 |
|------|------|
| `create_slides_gemini.py` `--language` 파라미터 추가 | ✅ |
| `make_video.py` `gemini_language` 자동 전달 | ✅ |
| 영어 Gemini 슬라이드 생성 (27장, 영어 전용) | ✅ |
| `clearly-intro-en.mp4` 생성 (13:48, 27 MB) | ✅ |
| WorkLog 작성 | ✅ |
| GitHub 커밋 & 푸시 | ✅ |

**완료율**: **6/6 (100%)**

---

## Daily Retrospective

### What went well

- **영어/한국어 분리 즉각 수정**: 슬라이드 4장 생성 후 한국어 혼재를 바로 발견하고 중단 → 원인 파악 → 스크립트 수정 → 재생성. 초기에 발견해서 비용 낭비 최소화
- **`--language` 파라미터 구조**: `make_video.py`의 config에 `gemini_language` 키를 추가하여 `--lang en/kr` 만으로 전체 파이프라인이 언어별로 자동 처리됨
- **delta cache 활용**: 오디오는 이미 완료되어 있어서 슬라이드 + 비디오 단계만 실행 → 효율적

### What could be improved

- `create_slides_gemini.py` 최초 설계 시 언어 파라미터를 포함했으면 이번 수정이 불필요했음
- `Topics/Claude-Skills/` 폴더가 `.gitignore`에 포함되어 스크립트 변경사항이 git에 저장되지 않는 점은 향후 확인 필요

### 전체 인사이트

- **프롬프트 언어 설정의 중요성**: Gemini 이미지 생성 프롬프트에서 언어 지정이 없으면 기본적으로 학습 데이터의 언어 패턴에 따라 임의 선택됨. 명시적 지정 필수
- **`make_video.py` 래퍼의 가치**: `--lang en` 하나로 슬라이드 파일 자동 탐색, 오디오/슬라이드 폴더 분리, 언어별 TTS 설정까지 자동 처리 → 다음 프로젝트에서도 재사용 가능

---

## 산출물 요약

### 오늘 생성/변경된 파일

| 파일 | 상태 | 설명 |
|------|------|------|
| `clearly-intro-script-en.md` | ✅ 기존 | 영어 나레이션 스크립트 (27장) |
| `clearly-intro-script-en - slides.md` | ✅ 기존 | 영어 Deckset 슬라이드 |
| `audio-en/slide_0.mp3` ~ `slide_26.mp3` | ✅ 기존 | 영어 TTS 오디오 27개 |
| `slides-gemini-en/1.jpeg` ~ `27.jpeg` | 🆕 생성 | 영어 전용 슬라이드 이미지 27개 |
| `clearly-intro-en.mp4` | 🆕 생성 | **최종 영상, 13:48, 27 MB** |

### 최종 03-Clearly-Intro-Video 폴더 구조

```
03-Clearly-Intro-Video/
├── README.md
├── clearly-intro-script-kr.md                  ✅ (한국어 스크립트)
├── clearly-intro-script-kr - slides.md         ✅ (한국어 슬라이드)
├── clearly-intro-script-en.md                  ✅ (영어 스크립트)
├── clearly-intro-script-en - slides.md         ✅ (영어 슬라이드)
├── composite_screenshots.py                    ✅ (합성 유틸리티)
├── _files_/                                    ✅ (스크린샷 8개)
├── audio-kr/                                   ✅ (한국어 MP3 27개)
├── audio-en/                                   ✅ (영어 MP3 27개)
├── slides-gemini-kr/                           ✅ (한국어 슬라이드 JPEG 27개)
├── slides-gemini-en/                           ✅ (영어 슬라이드 JPEG 27개)
├── clearly-intro-kr.mp4                        ✅ 완성! (16:28, 37.5 MB)
└── clearly-intro-en.mp4                        ✅ 완성! (13:48, 27 MB)
```

**M3 한국어 + 영어 버전 완전 완료 🎉**

---

**작성자**: CUA_VL 학습자
**방법론**: CUA_VL (VibeLearn AI)
