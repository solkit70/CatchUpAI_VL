---
title: "WorkLog — M5 판단 기준 · Topic README"
source: "[[20261004_RoadMap_AI-Agent-Apps-Compare#M5 - 판단 기준 · Topic README]]"
author:
  - "박창수"
  - "Codex"
created: "2026-10-11 07:43:08"
tags:
  - ai-agent-apps-compare
  - worklog
---

## 오늘의 학습 목표

- [x] M2·M3·M4 근거를 바탕으로 선택 기준과 흐름도 작성
- [x] 처음 예상과 실제 결과의 차이 기록
- [x] Topic 첫 화면과 모듈 학습 순서 정리

## 승인된 계획과 실행 범위

계획은 근거 검토 12분, 선택 가이드 35분, Topic README 18분, 기록·점검 7분에 버퍼 18분을 더한 90분이었다. 모델 변경 후 사용자의 M5 재진행 요청에 따라 기존 초안을 다시 검토하고 수정했다. 실제 활동별 소요 시간은 미측정이며 계획 시간을 실측값으로 사용하지 않는다.

## 진행 내용

### 근거 검토와 판단 기준

[M2 실습 판정](../02-Comparison-Table/guides/comparison-table.md#이-topic-의-실습-판정)과 [M4 판정표](../04-Real-Task-Trial/guides/trial-results.md#결과-기록표)를 대조했다. 직접 실행 근거는 Muse 두 과제이며 다른 세 서비스의 출력 품질은 확인하지 않았다. 계산 정확도와 생성문의 형식·근거 준수를 별도로 판단하고 자료 민감도·작업 영향·현재 접근·검증 방법의 네 기준을 정리했다.

### 선택 가이드와 첫 화면

[판단 흐름도](../05-Decision-Guide/guides/which-agent-when.md#판단-흐름도)에 접근 조건을 먼저 확인하는 분기를 넣고 여섯 업무 사례에 기준을 적용했다. [Topic README](../README.md#핵심-결과)에 결과와 한계, 모듈 순서를 연결했다. Codex의 직접 Muse UI 조작과 스크린샷 문서화 과정은 M6 영상 항목으로 유지했다.

## 문제 해결 로그

초안의 사례 수가 다섯으로 적혔지만 표에는 여섯 행이 있어 수정했다. M3의 시간 범위 오류와 M4의 성공한 가상 계산을 함께 기록하고, 계정별 활동 언급은 일반적인 기억 격리 한계로 바꿨다. PowerShell에서 Python으로 한글을 전달할 때 인코딩이 깨져 UTF-8로 복구한 뒤 링크와 섹션을 다시 점검했다.

## DoD 체크리스트

- [x] 근거 링크가 있는 판단 흐름도
- [x] 예상 vs 실제 표
- [x] Topic 최상위 README 초안
- [x] 모듈 README와 학습 순서
- [x] 링크 검사 및 빈 폴더 확인
- [x] WorkLog + Daily Retrospective + Module Retrospective

**완료율**: 6/6 (100%). `check_links.py`: 상대 링크 105개 정상, 깨진 링크 0개, 템플릿 예시 10개 제외, 빈 폴더 0개. M5 문서의 섹션 링크 24개와 Wiki 링크의 대상·절을 확인했다.

## Daily Retrospective

### 오늘 배운 것

계산 과제는 독립 정답으로 검증할 수 있었고 생성 과제는 형식 충족과 근거 제한이 서로 다른 평가 항목이었다. 이 차이를 선택 기준에 반영해 결과를 사용할 때 필요한 사람의 검토를 정리했다. 근거: [M4 판정표](../04-Real-Task-Trial/guides/trial-results.md#결과-기록표).

### 잘된 점과 개선할 점

실행한 서비스와 조사한 서비스를 구분하고 시간 절약 수치를 추정하지 않았다. 다음 비교에서는 반복 과제와 사람의 기준 작업·수정 시간을 기록해야 더 넓은 성능 판단이 가능하다. 사용자의 자기 평가 능력은 별도 확인하지 않았으므로 대신 체크하지 않는다.

### 다음 학습 초점

M6에서 비교 결과·실습 장면·선택 기준을 영상 슬라이드 플랜으로 옮긴다. Codex의 직접 Muse 조작과 스크린샷 문서화 과정을 포함하고 슬라이드 플랜을 검토받은 다음 제작 단계로 진행한다.

## 참조 및 산출물

- [M5 README](../05-Decision-Guide/README.md)
- [선택 기준](../05-Decision-Guide/concepts/selection-criteria.md)
- [여섯 업무 사례](../05-Decision-Guide/examples/decision-scenarios.md)
- [선택 가이드](../05-Decision-Guide/guides/which-agent-when.md)
- [모듈 회고](20261011_M5_Retrospective_AI-Agent-Apps-Compare.md)
