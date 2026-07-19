---
title: "20260719 M5 Build with AI WorkLog"
created: 2026-07-19 07:16:00
tags:
  - vibelearn-ai
  - worklog
  - build-with-ai
---

# WorkLog - M5: Capstone Video Production Package

**날짜**: 2026-07-19
**Topic**: Build-with-AI
**모듈**: M5 - Capstone Video Production Package
**학습 시간**: 1시간 내외
**방법론**: VibeLearn AI

## 오늘의 학습 목표

- [x] M1-M4 핵심 산출물 통합
- [x] 최종 추천 영상 angle 명시
- [x] 최종 제목 후보와 target viewer 정리
- [x] 영상 structure와 asset list 정리
- [x] 사용자 review request를 3개 이하로 작성
- [x] 후속 영상으로 넘길 내용 분리
- [x] 다음 제작 작업 목록 작성

## 진행 내용

### 1. Production Package 폴더 생성

`05-Production-Package/` 폴더가 아직 없어서 새로 만들었다. 로드맵 기준 M5 산출물은 `README.md`와 `production-package.md`이므로 두 파일을 작성했다.

### 2. M1-M4 산출물 통합

M1의 Source Map과 쉬운 12부 요약, M2의 통합 소개형 angle, M3의 video brief, M4의 slide plan을 하나의 제작 착수 패키지로 통합했다. 이 패키지는 단순 요약이 아니라 실제 다음 작업으로 넘어가기 위한 기준 문서다.

### 3. 최종 제작 방향 정리

첫 영상은 송재희님의 Build with AI 12부작을 비개발자·시니어 도메인 전문가에게 쉽게 소개하는 통합 소개형 영상으로 확정했다. 사용자의 경험은 중심 주제가 아니라, 각 Part를 이해시키는 보조 사례로 배치한다.

### 4. Review Request 작성

사용자가 승인할 결정 사항을 3개로 제한했다.

1. 영상 제목 방향
2. 영상 범위
3. 사례 사용 방식

승인 후 즉시 할 작업도 캡처, 도식 제작, 표 제작, 전체 스크립트 초안 작성으로 정리했다.

## 문제 해결 로그

### 문제: M1-M4 산출물이 많아 제작자가 바로 보기 어려움

**증상**: Source Map, Angle, Brief, Slide Plan이 각각 유용하지만, 실제 제작 착수 단계에서는 흩어져 있어 판단 비용이 컸다.

**원인**: VibeLearn AI 모듈별 산출물이 단계별 학습에는 좋지만, 제작 전환에는 핵심 결정만 압축한 package가 필요하다.

**해결**: `production-package.md`에 최종 추천, 제목 후보, target viewer, promise, scene structure, opening script, explanation blocks, asset list, attribution notes, scope boundary, review request, immediate next work를 통합했다.

## DoD 체크리스트

Roadmap M5 Definition of Done:

- [x] M1-M4 핵심 산출물이 통합되었다.
- [x] 최종 추천 영상 angle이 명시되었다.
- [x] 사용자가 승인할 결정 사항이 3개 이하로 정리되었다.
- [x] 후속 영상으로 넘길 내용이 분리되었다.
- [x] 다음 작업 목록이 작성되었다.
- [x] Module Retrospective 또는 WorkLog 업데이트가 완료되었다.

**완료율**: 6/6 (100%)

## Daily Retrospective

### What went well

- Build with AI 첫 영상의 제작 방향이 산출물 수준에서 명확해졌다.
- 사용자의 핵심 목적, 즉 송재희님의 Build with AI를 소개하고 사용자의 해석과 경험으로 쉽게 돕는 방향을 최종 패키지에 반영했다.
- 다음 제작 작업이 캡처, 도식, 표, 스크립트 작성으로 명확히 분리되었다.

### What could be improved

- 실제 영상 제작 전에는 Build with AI 공식 화면 캡처와 PDF 표지/목차 사용 여부를 확인해야 한다.
- 12부 전체를 다룰 경우 영상 길이가 12분을 넘을 수 있으므로, 실제 스크립트 작성 단계에서 압축이 필요하다.

### Insights

- 이 Topic의 최종 산출물은 "영상 스크립트"가 아니라 "영상 제작 착수 패키지"다.
- 첫 영상의 균형은 Build with AI 소개 70%, 사용자 해석/경험 30% 정도가 적합하다.
- 후속 영상으로 Part별 심화, 실제 바이브 코딩, Bila AI Agent 구현을 분리하면 첫 영상의 초점이 유지된다.

### Tomorrow's focus

- 사용자 review request 3개에 대한 결정을 받는다.
- 승인 후 실제 영상 제작 단계로 넘어간다.
- 다음 작업은 공식 화면 캡처, 도식 제작, Part별 한 줄 표 제작, 전체 스크립트 초안 작성이다.

## 사용자 피드백 반영 - 영상 범위 수정

### 피드백 요약

사용자는 각 Part별 심화 해설을 후속 영상으로 넘기지 않고, 이번 영상 안에서 Build with AI 12부 전체를 다 담고 싶다고 결정했다. 방식은 원문을 길게 설명하는 것이 아니라, 각 Part를 쉽게 설명하고, 사용자의 의견과 실제 예시를 붙여 해당 Part의 이해를 돕는 구조다.

### 수정 내용

- `production-package.md`의 영상 범위를 수정했다.
- 기존의 "12부작 전체를 쉬운 큰 그림으로 소개하고 각 Part 심화는 후속 영상으로 넘김" 문구를 제거했다.
- 이번 영상에서 12개 Part를 모두 다루되, 각 Part를 `원문 핵심 / 쉬운 설명 / 사용자 의견·예시` 구조로 설명하는 규칙을 추가했다.
- 영상 길이는 기존 8-12분보다 넓혀 12-14분까지 허용하는 방향으로 조정했다.
- 후속 영상 후보에서는 "Build with AI 각 Part별 심화 해설"을 제거하고, 실제 튜토리얼/도구 비교/구현 상세만 남겼다.

## 영상 제작 스킬 Handoff 검토

### 검토 결과

사용자는 이 Topic 학습은 여기서 마치고, 나중에 별도 영상 제작 스킬로 이 Topic 산출물을 참조해 영상을 만들 계획이라고 밝혔다. 관련 스킬을 확인한 결과, 이 Topic은 `markdown-video`보다 `remotion-video` 스킬에 더 적합하다.

`remotion-video` 스킬은 슬라이드 플랜 리뷰, 이미지 프롬프트, Remotion 컴포지션, edge-tts 초벌, Qwen3-TTS 최종 음성, 최종 렌더링의 승인 게이트를 가지고 있다. Build with AI 영상은 12부 해설, 동적 도식, 출처 화면, TTS 리뷰가 필요하므로 이 흐름이 잘 맞는다.

### 보강 내용

- `05-Production-Package/remotion-video-handoff.md`를 추가했다.
- `05-Production-Package/README.md`에 handoff 문서를 Learning Order에 추가했다.
- `production-package.md`에 Video Skill Handoff 섹션을 추가했다.
- 나중에 사용할 handoff prompt draft, video-id 후보, 필요한 입력 문서, slide plan 요구사항, 이미지/캡처 요구사항, TTS notes, 승인 게이트를 정리했다.

## 참조 및 산출물

**생성된 파일**:
- `05-Production-Package/README.md`
- `05-Production-Package/production-package.md`
- `vl_worklog/20260719_M5_Build-with-AI.md`

**업데이트된 파일**:
- `vl_roadmap/20260705_RoadMap_Build-with-AI.md`: M5 완료, Topic 산출물 패키지 완료 상태 반영
- `vl_prompts/daily_learning_prompt.md`: Topic 완료 후 사용자 리뷰 단계로 갱신

**참조 자료**:
- `01-Source-Map/source-materials.md`
- `01-Source-Map/easy-12-part-summary.md`
- `01-Source-Map/build-with-ai-source-map.md`
- `02-Video-Angle/first-video-angle.md`
- `03-Video-Starter/video-brief.md`
- `04-Slide-Plan/slide-plan.md`
- `vl_roadmap/20260705_RoadMap_Build-with-AI.md`

**작성자**: Codex
**방법론**: VibeLearn AI
