---
title: "AI-Agent-Apps-Compare"
source: "[[20261004_RoadMap_AI-Agent-Apps-Compare#M5 - 판단 기준 · Topic README]]"
author:
  - "박창수"
  - "Codex"
created: "2026-10-11 07:38:08"
tags:
  - ai-agent-apps-compare
  - ai-agents
---

## 이 Topic에서 한 일

[English](README.en.md)

Grok Bot, Muse, Dots, Instinct 네 에이전트의 공개 자료와 접근 조건을 비교하고, 실제 접근 가능한 Muse에서 첫 사용과 두 가지 가상 과제를 검토했다. 목표는 기능 목록만 비교하는 데서 그치지 않고, 업무 성격·위험도·검증 가능성에 따라 맡길 범위를 정하는 것이다.

## 핵심 결과

- M2에서 제품별 기능·접근·개인정보·권한 정보를 비교했다. 공식 근거와 보조 자료를 구분했고, 확인하지 못한 항목은 확정하지 않았다.
- M3에서 Muse의 답변 범위·시간 계산·출처·작업별 권한 확인 절차를 기록했다. 처음 제시된 Sources 패널이 공식 출처만으로 구성되지는 않아 Meta 원문 URL을 다시 확인했다.
- M4의 가상 일정 검토는 겹침과 시간 합계를 정확히 찾아 **쓸 만함**으로 평가했다. 형식이 제한된 설명문은 근거 밖 표현이 남아 **고치면 쓸 만함**으로 판정했다. 응답 및 사람 수정 시간은 별도 측정하지 않아 절약 시간을 계산하지 않았다.
- 직접 실행한 서비스는 Muse뿐이다. Dots·Grok Bot·Instinct는 공개 자료 조사에 한정되므로 실제 성능 순위는 만들지 않았다.

> Muse는 짧은 강연과 도구 시연이 09:35–09:40에 5분 겹친다고 찾았다. 첫 시작부터 마지막 종료까지의 경과 시간 90분과 항목별 시간 합계 95분도 구분했다.
>
> — M4 결과 문서의 관찰 기록. 한 과제에서 관찰한 결과이며, 서비스 전반을 보증하지 않는다. [M4 결과](04-Real-Task-Trial/guides/trial-results.md#과제-a--가상-행사-시간표)

## 학습 모듈

| 순서 | 모듈 | 결과 |
|---|---|---|
| 1 | [서비스 정체 확인](01-Identify-Services/README.md) | 네 서비스의 공개 정체·접근 조건·확인 필요 항목 |
| 2 | [비교표 만들기](02-Comparison-Table/README.md) | 다섯 기준 비교 및 근거 구분 |
| 3 | [Muse 첫 사용](03-Hands-On/README.md) | 실제 UI 확인, 읽기 중심 과제, 권한·출처 검증 |
| 4 | [내 일 하나 맡겨 보기](04-Real-Task-Trial/README.md) | 허구 자료로 과제 두 개 실행·평가 |
| 5 | [판단 기준 만들기](05-Decision-Guide/README.md) | 업무·위험·근거 수준별 선택 가이드 |
| 6 | [결과 영상 제작](06-Capstone-Video/video-slide-plan.md) | 슬라이드 플랜 검토 중; 영상 완성 후 링크 추가 |

## 선택 가이드

[M5 판단 흐름도](05-Decision-Guide/guides/which-agent-when.md)는 자료 민감도, 외부 행동의 위험, 현재 접근 조건, 결과를 검증할 수 있는지를 차례로 묻는다. 연결 앱 작업은 권한을 작업별로 확인하고, 읽기·초안과 외부 변경을 구분한다. 가상 입력과 외부 커넥터 미사용만으로 저장된 기억까지 격리된다고 단정할 수 없으므로, 엄격한 격리가 필요하면 기억이 없는 별도 테스트 환경을 고려한다. [M4 격리 한계](04-Real-Task-Trial/guides/trial-results.md#개인정보-격리-한계)를 참조한다.

## 범위와 한계

M4는 허구의 데이터만 사용했고 메일·일정 커넥터를 열거나 게시물을 발행하지 않았다. 시간 절약을 입증할 기준 작업 시간과 사람의 검토 시간은 측정하지 않았다. 한 서비스의 두 과제만 실행했으므로 다른 서비스나 실제 업무 결과로 일반화하지 않는다. 접근·가격·권한 정책은 바뀔 수 있으므로 실행 직전에 공식 자료와 계정 화면을 다시 확인한다.

## Capstone 영상

M6 영상에서는 **Codex가 Muse 화면을 직접 조작해 두 가지 가상 과제를 실행하고, 결과 화면을 캡처해 문서에 넣은 과정**도 소개한다. 화면 증거는 개인 일정·계정별 권한 상태를 가린 자료만 사용하며, 최종 슬라이드 플랜은 제작 전에 검토받는다.

추가로 **VS Code의 Codex에 생활 질문을 지시하자 브라우저의 Muse에 일을 맡기고 한국어 단풍 추천을 받은 경험**을 다룬다. [업무 위임 사례와 화면 기록](vl_materials/20261011_codex-muse-browser-delegation.md#관찰한-흐름)은 Senior-AI-Enablement의 시연 후보에도 연결했다.

## 주요 자료

- [M2 비교표](02-Comparison-Table/guides/comparison-table.md)
- [M3 설정 및 첫 과제](03-Hands-On/README.md)
- [M4 실행 결과](04-Real-Task-Trial/guides/trial-results.md)
- [M5 판단 흐름도](05-Decision-Guide/guides/which-agent-when.md)
- [Roadmap](vl_roadmap/20261004_RoadMap_AI-Agent-Apps-Compare.md)
- [공식 출처 목록](vl_materials/official-sources.md)
