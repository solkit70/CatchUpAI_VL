---
title: "M5 — 로컬 인트로·타이틀·효과 실습"
author:
  - "Codex"
created: "2026-10-25 07:42:03"
tags:
  - ai-event-video-editing
  - effects
---

## M5 실습 범위

사용자가 M5 진행을 요청해 로컬 기준 영상에 코드 기반 타이틀·효과를 적용하는 실습을 시작했다. 원래 로드맵 예상은 3시간이며 실제 학습 시간으로 집계하지 않는다. 로컬 Whisper 발언 자막은 짧게 시험했으나 오인식이 남아 최종 영상에는 넣지 않았다. CapCut Seedance 2.0 Mini로 5초 인트로를 생성했지만 템플릿 편집기는 네트워크 오류로 로딩되지 않아 두 인트로를 비교하지 못했다. Premiere 연계도 미완료이며, 실제 영상은 공개 Topic 밖 로컬 작업 폴더에 보관한다.

## 학습 순서

1. [인트로 방식 비교](intro-template-vs-generative.md) — 코드 템플릿·Seedance 생성 결과·CapCut 템플릿 오류를 확인한다.
2. [AI 지시 효과 적용](ai-directed-effects.md) — 인트로·하단 제목·Q&A 카드와 원본 보존 기준을 확인한다.
3. [재현 스크립트](render_effects.py) — 원본과 새로운 출력 폴더를 지정해 데모를 만든다.
4. [데모 조립과 검증](demo-assembly.md) — 타임라인·출력 실측·검증 결과·검토 항목을 확인한다.
5. [최신 M5 WorkLog](../vl_worklog/20261029_M5_AI-Event-Video-Editing.md) — 자막 시험·Seedance 생성·템플릿 편집기 오류·현재 DoD를 확인한다.

## 이동

- 이전: [M4 비교 결론](../04-HandsOn-Highlight/results-comparison.md)
- 현재: [로드맵 M5](../vl_roadmap/20261017_RoadMap_AI-Event-Video-Editing.md#m5---체험-②--인트로--효과--premiere--capcut-연계)
- 다음: [M6 매뉴얼과 전달 패키지](../06-Client-Manual/README.md)
