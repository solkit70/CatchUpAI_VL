---
title: "WorkLog - M3: VibeLearn AI on Muse (실습 4)"
author:
  - Codex
created: 2026-11-05 06:05:02
tags:
  - muse-my-workflow
  - worklog
---

## 세션 정보

> 2026-11-07 Claude Code 보강 — 앞 세션 WorkLog 와 같은 머리 정보를 맞췄다. 아래 본문(실습 4 목표 ~ 🎓)은 Codex 원문 그대로다.

**날짜**: 2026-11-05
**Topic**: Muse-My-Workflow
**모듈**: M3 - VibeLearn AI on Muse (실습 4 · 모듈 마무리)
**진행 에이전트**: Codex
**이전 WorkLog**: [20261101_M3_Muse-My-Workflow.md](20261101_M3_Muse-My-Workflow.md) — 실습 2 · 3 완료 (Claude Code)
**모듈 회고**: [20261105_M3_Retrospective.md](20261105_M3_Retrospective.md)

## 실습 4 목표

승인된 40분 계획으로 Muse가 만든 공개 Topic 파일을 집의 볼트에 가져와 기간 검토부터 이어받는다. 11/1 세션에서 M3 실습 1~3이 완료됐으며, 이번 작업은 해당 기록의 인계 지점에서 시작했다. [이전 WorkLog](20261101_M3_Muse-My-Workflow.md#다음-세션에-넘길-것)

## 실습 4 결과

Muse Library의 **System files → workspace → Topics → AI-Public-Event-Scheduling**에서 `topic_info.md`와 `vl_prompts/`의 두 파일을 개별 다운로드했다. `_Inbox_/AI-Public-Event-Scheduling/`에 원래 폴더 구조를 유지해 복사했다. 세 파일은 다운로드본과 볼트 사본의 SHA-256이 각각 일치했다.

| 파일 | 확인 결과 |
|---|---|
| `topic_info.md` | Topic 이름, 설명, 기간, 목표 세 가지, 학습 환경을 읽을 수 있었다. |
| `roadmap_prompt.md` | [2단계]와 [3단계]가 [로드맵 원본 템플릿](../../../templates/roadmap_prompt_template.md#2단계-ai에게-요청할-작업)과 줄바꿈 형식 통일 후 일치했다. |
| `daily_learning_prompt.md` | [2단계]와 [3단계]가 [일일 학습 원본 템플릿](../../../templates/daily_learning_prompt.md#2단계-ai에게-요청할-작업)과 줄바꿈 형식 통일 후 일치했다. |

**판정은 가능**이다. Codex가 가져온 파일에서 기간과 세 학습 목표를 읽고, 로드맵 프롬프트의 기간 검토 단계까지 이어갔다. 공개 행사 수집용 프롬프트 작성, 일정 충돌 판정, 캘린더에 넣기 좋은 형태로 정리하는 실습으로 범위를 잡으면 **2주 × 주 3시간(총 6시간)은 적정**하다. 기간을 확인받는 지점에서 멈췄으며 실습용 Topic의 로드맵은 생성하지 않았다.

## M3 완료 기준

- [x] 공개 저장소 지시 읽기와 대조
- [x] 순서 지키기 시험과 결과표
- [x] 기억 시험과 삭제 방법 기록
- [x] 집에서 이어받기 시험과 판정
- [x] 밖에서 준비할 일과 집에서 이어갈 일 문서화
- [x] 공개 주제 예시와 모듈 README 작성
- [x] 링크 검사 · 상대 링크 78개 정상, 깨진 링크와 빈 폴더 0개
- [x] WorkLog, 영상·교육 메모, 회고 작성

## 회고

파일을 내려받는 경로와 집에서 재개하는 지점을 모두 확인했다. 다운로드본과 사본의 동일성 확인과, 가져온 프롬프트와 템플릿의 지시 비교는 서로 다른 검증이다. 다음 모듈은 [M4 볼트 연결 해법](../vl_roadmap/20261018_RoadMap_Muse-My-Workflow.md#m4---볼트-연결-해법--집과-밖을-끊김-없이)이다.

## 🎬 영상 재료

Library에서 원본 3개를 받는 장면, 템플릿 두 절의 일치 판정, Codex가 2주 계획을 검토하고 멈춘 장면을 순서대로 보여 줄 수 있다.

## 🎓 가르칠 때

학습 기록과 실제 파일을 한 묶음으로 전달하는 연습이다. 받아 온 파일의 지시와 사용자 확인 지점을 먼저 찾으면 어느 단계부터 이어갈지 결정할 수 있다.

## 다음 세션에 넘길 것

> 2026-11-07 Claude Code 보강 — 이 세션에 없던 칸을 위 본문 · M4 WorkLog · 로드맵에서 옮겨 적었다.

1. M3 는 닫혔다(DoD 8/8). 다음은 **M4 — 볼트 연결 해법**. 시작할 때 읽을 것: [첫 조사 자료](../vl_materials/vault-connection-first-research.md) · M2 비교표(기준선) · 이 M3 판정 · M1 연결 · 이름 규칙 · 로드맵의 M4 절. (실제로 같은 날 06:39 에 Codex 가 M4 를 시작했다 → [M4 WorkLog](20261105_M4_Muse-My-Workflow.md))
2. `_Inbox_/AI-Public-Event-Scheduling/` 의 시험 Topic 은 기간 검토에서 멈춘 상태다. 실제 Topic 으로 이어 갈지는 박창수가 정한다.
3. 남은 열린 질문: 휴대폰 앱의 Import memory · 학습 끄기 스위치.
4. Muse 기억의 「VibeLearn AI 규칙」은 유지 중(박창수 결정, 11/1). Muse 메인 대화의 Roadmap 승인 질문은 답하지 않은 채 남아 있다.
5. 이전부터 남은 것: 공개 레포 push(박창수 지시 뒤) · 다운로드 폴더 시험 파일과 전체 데이터 zip 정리(박창수 결정).
