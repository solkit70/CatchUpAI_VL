---
title: "M2 — 방법별 리서치와 비교표"
author:
  - "Codex"
created: 2026-10-24 22:47:08
tags:
  - ai-event-video-editing
  - methods-research
---

## M2 — 방법별 리서치와 비교표

**상태**: 문서 조사 산출물 완료 — 2026-10-24, 5개 범주·9개 후보
**전체 모듈 예상 시간**: 3.5시간 (로드맵 기준; 실제 소요를 뜻하지 않음)

공식 문서와 커뮤니티 작성자 자료로 기능·비용·한도·한국어·Premiere 연계를 비교했다. 의뢰인 답변은 미확인이고 직접 체험은 0건이며, 확인하지 못한 조건을 문서에 남겼다. 사용자 자기평가는 미실시이며 추천과 실제 검증은 다음 단계다.

## 학습 순서

1. [Premiere 자체 AI](cards/premiere-native-ai.md) — 검색·전사와 공식 AI Assistant 공개 베타를 구분한다.
2. [Vidio.ai / VibeEdit](cards/vidio-vibeedit.md) — 입력 길이·크레딧·XML 누락 요소를 확인한다.
3. [OpusClip / ClipAnything](cards/opusclip-clipanything.md) — 프롬프트 클리핑·체험 제한·XML 전달을 확인한다.
4. [Premiere MCP](cards/premiere-mcp.md) — 커뮤니티 연결 도구의 역할·설치·지원 API 경계를 본다.
5. [Memories.ai VEA](cards/memories-vea.md) — 개요와 관리형 API를 구분하고 출력 길이 제약을 확인한다.
6. [Seedance](cards/seedance.md) — 생성·참조 편집과 긴 행사 편집의 차이, 기존 설명 정정을 읽는다.
7. [FFmpeg + 전사](cards/ffmpeg-transcript.md) — 장면 판단과 지정 구간 편집의 역할을 구분한다.
8. [Remotion](cards/remotion.md) — 인트로·자막·반복 템플릿과 라이선스 조건을 본다.
9. [CapCut AI](cards/capcut-ai.md) — 기존 사용 도구의 AI·무료 범위·전달 조건을 확인한다.
10. [비교표](comparison-table.md) — 5개 범주·9개 후보를 같은 기준으로 비교한다.
11. [Claude·ChatGPT 연결 방식](claude-chatgpt-plugins.md) — 클라이언트·연결·편집 도구의 역할과 검증 순서를 정리한다.
12. [리뷰 반영·전체 후보 대조](review-followup.md) — 중요 수치·화면 근거·미조사와 보류 사유를 확인한다.
13. [2026-10-24 WorkLog](../vl_worklog/20261024_M2_AI-Event-Video-Editing.md) — 조사 세션과 리뷰 반영 이력을 확인한다.

## 이번 조사에서 달라진 판단

[Premiere 공식 Assistant](cards/premiere-native-ai.md#공식-ai-assistant-공개-베타)와 [커뮤니티 MCP](cards/premiere-mcp.md#요약)는 다른 경로다. [Seedance](cards/seedance.md#기능과-기존-설명-정정)는 참조 편집도 지원하므로 「편집은 못 한다」는 기존 단정을 정정했으며, 수시간 기록 영상의 하이라이트 편집과는 여전히 구분한다.

외부 편집 서비스에서는 [XML 누락 요소](cards/vidio-vibeedit.md#premiere-연계의-한계), [무료 체험 제한](cards/opusclip-clipanything.md#가격무료-체험처리량), [출력 길이 직접 지정 불가](cards/memories-vea.md#기능과-서로-다른-문서의-경계)가 실제 도입의 확인점이다. 코드 도구는 장면 선택을 자동으로 해결하는 후보가 아니라 역할을 나누어 비교할 대상이다.

## 완료 범위와 다음 단계

M2는 후보 카드 9개·비교표·연결 방식 분석·리뷰 반영 기록을 갖췄다. [M3 조건부 추천](../03-Recommendation/recommendation.md)은 작성했지만 원본·계정·실습 결과는 아직 없으며, 확정 도입 추천이 아니다. [한 장 요약](../03-Recommendation/client-summary.md)을 상담에 활용하고 상세 검증은 카드와 리뷰 기록을 따른다.

## 이동

- 이전: [M1 요구사항과 방법 지도](../01-Requirements-Map/README.md)
- 현재: [로드맵 M2](../vl_roadmap/20261017_RoadMap_AI-Event-Video-Editing.md#m2---방법별-리서치와-비교표)
- 다음: [M3 조건부 추천안과 체험 준비](../03-Recommendation/README.md)
