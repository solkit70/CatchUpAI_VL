---
title: "Tehaleh-Community-Video Final Retrospective"
created: 2026-06-22 13:57:10
completed: 2026-06-22
status: completed
tags:
  - tehaleh-community-video
  - final-retrospective
  - vibelearn-ai
  - remotion
  - youtube
---

# Topic Final Retrospective — Tehaleh-Community-Video

## 완료 요약

`Tehaleh-Community-Video`는 Tehaleh 지역 리서치부터 슬라이드 플랜, Remotion 구현, 한국어·영어 Qwen3-TTS 나레이션, MP4 렌더링과 YouTube 배포까지 전 과정을 완료했다. 한국어 영상은 https://youtu.be/Cucvcz9bVPU, 영어 영상은 https://youtu.be/YygPvJbKPvU에 공개했으며, 창발 Product Group의 `The AI Powered Creator` 발표에서 AI 콘텐츠 제작 과정을 설명하는 실증 사례로 인계했다.

> “이 영상은 제가 실제로 살고 있는 동네를 소개한 것입니다. 레이니어 산이 보이는 이 동네에서, AI를 이용해서 이렇게 뚝딱 영상을 만들어봤습니다.”

이 문장은 최종 영상의 메시지이면서 Topic의 완료 기준을 요약한다. 단순히 AI가 만든 화면을 보여주는 데 그치지 않고, 실제 거주 경험과 직접 촬영한 사진을 리서치·코드·음성·배포 과정에 연결했다는 점이 핵심 성과다. 제작 과정의 근거는 [[20260621_M1-M4_Tehaleh-Community-Video#📚 진행 내용|M1~M4 WorkLog]]와 [[20260621_RoadMap_Tehaleh-Community-Video#📊 학습 진행 상황 추적|Roadmap 진행 현황]]에 기록되어 있다.

## 전체 학습 여정 통계

| 항목 | 결과 |
|------|------|
| 학습 모듈 | M1 리서치, M2 슬라이드·이미지, M3 Remotion, M4 TTS·렌더·배포 |
| 슬라이드 | 한국어·영어 각 15장 |
| TTS | Edge-TTS 초벌 후 Qwen3-TTS 한국어·영어 최종 음성 |
| 로컬 렌더 | 한국어 4:51.8, 영어 4:14.3 |
| 영상 사양 | 1920×1080, 30fps |
| 배포 | YouTube 한국어·영어 2개 공개 |
| 배포 자료 | 제목, Description, Chapter, Tags, 썸네일 프롬프트 |
| 발표 인계 | `The-AI-Powered-Creator` 데모 자산 및 슬라이드에 연결 |

초기 계획은 약 90~150초 분량의 짧은 데모였지만, 커뮤니티 시설·교통·주택 가격·재택근무·은퇴 생활과 직접 촬영한 레이니어 산 이야기가 추가되면서 정보형 영상으로 범위가 확장됐다. 길이 목표는 달성하지 못한 항목으로 숨기지 않고, 전달 품질을 우선한 승인된 Scope Change로 처리했다.

## 모듈별 통합 회고

### M1 — 리서치

Tehaleh의 위치, 규모, 공원과 트레일, 교통, 주택 가격, IT 종사자와 은퇴자 관점을 하나의 자료로 구조화했다. Homes.com 매물 정보에 2026년 6월 21일 기준일을 명시하고, 교통 시간은 상황에 따라 달라질 수 있다는 조건을 영상과 Description에 함께 남긴 것이 정확성을 높였다. 근거 자료와 결과는 [[20260621_M1-M4_Tehaleh-Community-Video#M1: Tehaleh 리서치 (이전 세션 → 계속)|M1 WorkLog]]에 정리되어 있다.

### M2 — 슬라이드와 이미지

15장 구조를 통해 지역 소개, 커뮤니티 시설, 주택, 재택근무와 은퇴 생활을 순차적으로 설명했다. Post & Pour에서 직접 촬영한 다섯 장의 사진을 시퀀스로 구성하면서 생성 이미지 중심의 영상보다 개인 경험이 분명한 결과가 됐다. 이후 배경을 어두운 테크 스타일에서 밝은 PNW 자연 색상으로 바꾼 결정은 콘텐츠의 정서와 시각 디자인을 일치시킨 중요한 개선이었다.

### M3 — Remotion 구현

데이터와 렌더 컴포넌트를 분리하고, 슬라이드별 오디오 길이를 기반으로 프레임을 계산하는 구조를 구현했다. 이미지 전환, 슬라이드 시작 전 오디오 여백, 나레이션 종료 후 Hold 구간을 조정하면서 정적인 프레젠테이션을 실제 영상 흐름으로 발전시켰다. Trail 컴포넌트 타입 오류를 spring 기반 애니메이션으로 대체한 경험은 외부 API 버전보다 단순하고 검증 가능한 구현을 우선해야 한다는 교훈을 남겼다.

### M4 — 음성, 렌더링과 배포

Edge-TTS로 구조와 타이밍을 먼저 검증한 뒤 Qwen3-TTS로 한국어·영어 최종 음성을 만들었다. `485K`, `2 Gbps` 같은 발음 문제는 음성용 스크립트 표기를 별도로 조정해 해결했으며, 한국어와 영어 렌더를 1920×1080, 30fps로 검증했다. 최종 편집 후 Chapter 타임코드를 다시 측정하고, 제목·Description·Tags·썸네일 프롬프트와 공개 URL까지 기록해 제작이 Distribution으로 이어지도록 했다.

## VibeLearn AI 방법론 평가

Roadmap은 리서치에서 영상 배포까지 작업 순서를 빠르게 정하는 데 효과적이었고, WorkLog는 여러 AI 도구와 세션 사이에서 결정 근거를 유지하는 Context 역할을 했다. 특히 사실 수정, 발음 보정, 배경 변경과 이미지 시퀀스 확장처럼 반복적인 요구가 생겼을 때 기존 기록이 있어 전체 구조를 잃지 않고 수정할 수 있었다.

반면 예상 영상 길이와 M4 시간은 실제보다 크게 낮게 산정됐다. 나레이션 단어 수, 다국어 제작, 사용자 검토 횟수, 썸네일과 YouTube 메타데이터 같은 배포 작업이 Roadmap에 충분히 반영되지 않았기 때문이다. 다음 영상 Roadmap에서는 `리서치 → 스크립트 → TTS 초벌 → 시각 QA → 최종 TTS → 렌더 → 편집 → 배포`를 별도 단계로 나누고, 언어별 산출물을 처음부터 DoD에 포함해야 한다.

## Self-Assessment

### 개념 이해

- [x] 슬라이드 데이터, 오디오 파일과 Remotion Composition의 관계를 설명할 수 있다.
- [x] 오디오 실측 길이로 `durationInFrames`와 전체 렌더 길이가 결정되는 과정을 설명할 수 있다.
- [x] Edge-TTS 초벌과 Qwen3-TTS 최종 음성을 분리하는 이유를 설명할 수 있다.

### 실무 활용

- [x] 리서치 문서를 15장 영상 구조로 변환하고 한국어·영어 버전을 제작할 수 있다.
- [x] 직접 촬영 이미지와 생성 이미지를 목적에 맞게 조합할 수 있다.
- [x] 제목, Description, Chapter, Tags와 썸네일을 포함해 YouTube 배포까지 완료할 수 있다.

### 문제 해결

- [x] TypeScript 컴포넌트 오류를 대체 구현으로 해결할 수 있다.
- [x] TTS의 숫자·단위 발음을 음성용 표기로 보정할 수 있다.
- [x] 슬라이드와 오디오 사이의 시작·종료 여백 및 편집 후 Chapter 변화를 조정할 수 있다.

## 산출물 품질 평가

완성본은 해상도, 음성, 이미지 전환과 정보 구조 측면에서 창발 발표 데모로 사용할 수 있는 수준에 도달했다. 실제 촬영 사진과 거주 경험이 일반적인 지역 홍보 영상과 차별화되고, 한국어와 영어 두 버전이 있어 발표 이후에도 독립 콘텐츠로 재사용할 수 있다.

한계도 분명하다. 주택 가격과 매물 수는 특정 날짜의 조회 결과이므로 시간이 지나면 갱신이 필요하고, 자동차 이동 시간은 교통 상황에 따라 크게 달라진다. 또한 Remotion 프로젝트 전체가 대용량 의존성과 미디어 때문에 Git에서 제외되어 있어 GitHub 문서만으로 영상을 완전히 재현할 수 없으며, 장기 재현성이 필요하면 소스 코드와 필수 자산만 분리한 별도 저장 전략이 필요하다.

## 방법론 개선 및 다음 적용

1. 나레이션은 작성 단계에서 언어별 예상 발화 시간을 계산하고 목표 길이를 초과하면 TTS 전에 축약한다.
2. 숫자, 단위, 영문 고유명사는 음성용 발음 사전을 먼저 만든다.
3. 데이터성 주장에는 수집 날짜와 출처를 슬라이드 데이터 단계부터 필수 필드로 둔다.
4. 다국어 영상은 번역, TTS, Chapter와 배포 메타데이터를 언어별 DoD로 관리한다.
5. YouTube 제목·Description·Tags·썸네일과 공개 URL을 제작의 부가 작업이 아닌 Distribution 모듈로 계획한다.

다음 적용 대상은 [[20260621_M4-M6_The-AI-Powered-Creator#발표 구조 v2.0 최종 확정|The-AI-Powered-Creator 발표]]이다. 발표에서는 완성 영상뿐 아니라 Roadmap, 리서치, Remotion, TTS와 Distribution 기록을 함께 보여주어 “기록이 AI의 Context가 된다”는 메시지를 실제 사례로 설명한다.

## 완료 판정

이 Topic은 2026년 6월 22일 기준으로 M1~M4의 맞춤형 DoD, 한국어·영어 렌더링, YouTube 배포, Self-Assessment와 Final Retrospective를 완료했다. VibeLearn AI의 일반 기준인 “최소 5개 산출물 폴더”는 4모듈 단기 Capstone의 구조와 맞지 않아 인위적인 빈 폴더를 만들지 않고 예외 처리했으며, 실제 산출물 수와 외부 Remotion 프로젝트를 근거로 완료를 승인한다.

모듈별 Retrospective는 모든 모듈이 하루 집중 세션과 연속 후속 편집으로 진행된 특성을 반영해 이 문서의 M1~M4 통합 회고로 대체했다. Topic 상태는 `completed`이며, 이후 작업은 영상 제작이 아니라 상위 발표 Topic에서의 재생 테스트와 발표 활용이다.

## 근거 문서

- [[20260621_RoadMap_Tehaleh-Community-Video#🎯 성공 기준|Topic Roadmap 완료 기준]]
- [[20260621_M1-M4_Tehaleh-Community-Video#YouTube 업로드 메타데이터|YouTube 업로드 메타데이터]]
- [[20260621_M4-M6_The-AI-Powered-Creator#다음 세션 작업 (D-5 → D-3)|발표 Topic 인계 상태]]
- [한국어 YouTube 영상](https://youtu.be/Cucvcz9bVPU)
- [영어 YouTube 영상](https://youtu.be/YygPvJbKPvU)
