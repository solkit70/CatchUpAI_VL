---
title: "active-shooter-response M4 학습 일지 및 회고"
type: worklog
project: active-shooter-response
date: 2026-09-13
created: "2026-09-13 16:30:00"
tags:
  - active-shooter
  - worklog
  - retro
  - M4
---

# VibeLearn AI 학습 일지 - Module M4

본 학습 일지는 **VibeLearn AI 방법론 v2.0**을 준수하여 작성되었으며, 나레이션 오디오 파일 합성 및 재생 정밀 계측, 타임라인 동기화를 진행한 과정과 결과를 영구 기록합니다.

---

## 1. 오늘 학습 목표 (Checklist)

- [x] 슬라이드 기획안(`video-slide-plan.md`)에서 나레이션을 파싱해 `narrations.json` 백업 생성 완료
- [x] edge-tts 라이브러리를 사용해 고화질 한국어 남성 성우 음성(InJoonNeural) 파일 12종 개별 합성 완료
- [x] ffprobe를 이용한 각 mp3 파일 재생 길이의 밀리초 단위 정밀 측정 완료
- [x] 정밀 딜레이 보정 공식(HEAD_PAD 0.1s + TAIL_PAD 0.12s)을 타임라인 연산에 대입 완료
- [x] 실측 durations 값을 Remotion `data.ts` 및 슬라이드 연출 제어 코드에 100% 싱크 완료
- [x] SectionSlide(Slide 03) 컴포넌트에 오디오 재생 장치(`<SlideAudio />`)를 연동하여 완성도 극대화 완료
- [x] `04-TTS-Audio/` 산출물 폴더 및 교과서 품질의 `README.md` 작성 완료

---

## 2. 진행 내용 (상세 학습 및 실습)

### 실습 1: 나레이션 자동 추출 및 edge-tts 음성 합성
*   **나레이션 파싱 스크립트 작성**: `02-Remotion-Setup/video-slide-plan.md` 파일 구조에서 각 슬라이드(Slide 01~12) 블록과 그 안에 작성된 bullet 나레이션(blockquote `>`)을 정규표현식으로 정교히 매핑해 파싱하는 `gen_audio_edge.py` 스크립트를 구현했습니다.
*   **발음 및 기호 보정**: 영어 알파벳 약어(FEMA, CRASE, EAP 등)나 마크다운 강조 표시 기호가 읽힐 때 어색해지는 것을 사전 방지하기 위해 `PRONUNCIATION` 보정 사전 및 `STRIP_MARKS` 정제 알고리즘을 소스에 주입했습니다.
*   **음성 합성**: Microsoft Edge Neural TTS 기반의 `ko-KR-InJoonNeural` 보이스에 속도 배율 `+4%`를 조율하여 진중하고 선명한 공익안전 안내 나레이션 mp3 파일들을 `AI/RemotionStudio/public/active-shooter-0908/audio/`에 성공적으로 추출 완료했습니다.

### 실습 2: ffprobe 실측 계측 및 타임라인 싱크 매핑
*   **시간 정밀 추출**: `ffprobe -show_entries format=duration` 명령어 결과값을 파이썬의 subprocess 객체로 스트리밍하여 각 슬라이드의 정확한 재생 길이를 소수점 3자리(밀리초) 단위로 확보해 `durations.json`에 영구 백업했습니다.
*   **타임라인 보정**: 실측된 12개 값들을 `data.ts`의 `AUDIO_DURATIONS` 객체에 한 치의 오차도 없이 일치시켜 주입했습니다.
*   **SectionSlide 오디오 바인딩**: 슬라이드 3번(생존 대응 3원칙 Section)에 기획된 나레이션을 재생할 수 있도록 `<SlideAudio />` 컴포넌트를 이식해 12개 슬라이드 전체의 청각적 공백이 사라졌습니다.

---

## 3. 문제 해결 로그 (Troubleshooting)

### 이슈 1: 마크다운 인덴트 블릿 기호로 인한 나레이션 파싱 누락
*   **원인**: 기존의 타 토픽용 파싱 소스는 줄 시작 지점의 마크다운 강조 기호(`**나레이션**`)만을 탐색했으나, 본 토픽은 가독성을 위해 불릿 기호 인덴트(`*   **나레이션**:`)가 가미되어 있어 파싱이 전혀 되지 않는 누락이 예상되었습니다.
*   **해결책**: 스크립트의 파싱 정규표현식을 `\*\s+\*\*나레이션\*\*:\s*\n((?:\s*>\s*.*\n)+)` 형태로 인덴트 유연 매칭 구조로 특화 개선하여 12개 슬라이드 전체 문장을 누락 없이 단 한 번에 성공적으로 추출했습니다.

---

## 4. Definition of Done (DoD) 체크리스트

- [x] 12개 슬라이드 전체의 나레이션 오디오 파일이 누락 없이 고품질로 가동 완료됨.
- [x] `ffprobe` 오디오 계측을 통해 프레임 수 싱크가 맞아떨어지는 `durations.json` 구축 완료.
- [x] 오디오 헤드/테일 패딩 수식이 `data.ts` 연산식에 정합하게 바인딩되어 첫마디가 유연하게 시작함.
- [x] `04-TTS-Audio/` 하위에 Python 스크립트, 문구 JSON, 계측 JSON 및 표준 README.md 탑재 완료.

---

## 5. Retrospective (회고)

### What went well?
*   수동으로 오디오를 하나하나 생성하고 초단위를 손수 체크하는 번거로움 없이, 단 한 번의 파이썬 스크립트 실행만으로 12개 대본 파싱 ➔ 음성 합성 ➔ durations 계측 ➔ JSON 백업 및 실시간 Remotion public 파일 저장을 정밀 자동화 완료했습니다.
*   Slide 03의 나레이션 역시 풍부하게 합성되어 SectionSlide 비주얼 연출과 함께 흘러나오도록 보강하여 영상의 전체 몰입도와 연출 정합도가 배가되었습니다.

### What could be improved?
*   Qwen3-TTS 등의 로컬 모델 연계 시에는 파이썬 가상환경에 추가 연산 라이브러리 및 모델 가중치가 소요될 것입니다. edge-tts는 API 제약 없이 매우 빠른 RTF(Real-time Factor)를 보여주므로 프로토타입 단계에서의 음성 합성 최적 수단임을 재확인했습니다.

### Insights
*   **"코드와 기획은 단일 원본(Single Source of Truth)을 추종해야 한다."** 자막 문구나 오디오 대본을 수정할 때 여러 데이터 파일을 개별 수정하면 정합성이 무너집니다. `video-slide-plan.md`라는 기획서 단 하나만을 고치고 `gen_audio_edge.py`를 원클릭 실행해 모든 소스 및 에셋을 전면 자동 재생성·갱신하는 워크플로우가 얼마나 안전하고 우아한지 온전히 깨달았습니다.

### Tomorrow's focus (다음 학습 목표)
*   **모듈 M5(최종 고화질 MP4 렌더링 및 배포 패키지 마감) 진입**:
    *   `05-Final-Delivery/` 폴더를 개설하고, Remotion CLI 빌드 커맨드를 통해 FHD(1080p) MP4 최종 무결점 영상 렌더링을 완수합니다.
    *   시민단체가 즉시 YouTube, Slack, Gobi, LinkedIn 등 다양한 소셜 플랫폼에 안전 링크와 교육 수강 안내를 배포할 수 있도록 구조화된 SNS 홍보 및 안내 글(`promo_text.md`)을 작성합니다.
    *   전체 학습 대장정을 돌아보고 소회를 기리는 Topic Final Retrospective를 기고하여 토픽을 명예롭게 졸업합니다.

---

## 6. 참조 및 산출물 경로

*   **나레이션 자동화 스크립트**: `04-TTS-Audio/gen_audio_edge.py`
*   **정제 완료 나레이션 원본**: `04-TTS-Audio/narrations.json`
*   **ffprobe 실측 durations 데이터**: `04-TTS-Audio/durations.json`
*   **모듈 안내 가이드**: `04-TTS-Audio/README.md`
*   **생성된 실물 음성 에셋 폴더**: `AI/RemotionStudio/public/active-shooter-0908/audio/`
