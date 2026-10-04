---
title: "마감 경고 단계와 요구사항"
created: 2026-10-03 05:00:00 -07:00
tags:
  - personal-ops-board
  - deadline
---

## 마감 경고 단계와 요구사항

### 확정 요구 (EARS)

| ID | 요구 | 검증 |
|---|---|---|
| DL-01 | WHEN `due`가 오늘보다 이르면 THE SYSTEM SHALL 해당 활성 task를 기한 초과에 표시한다 | 합성 경계 회귀 |
| DL-02 | WHEN `due`가 오늘이면 THE SYSTEM SHALL 오늘 마감에 표시한다 | 합성 경계 회귀 |
| DL-03 | WHEN 활성 task가 마감 전이고 남은 날짜가 `warn_days` 이하면 THE SYSTEM SHALL 남은 날짜 D-N으로 표시한다 | 기본 D-3·사용자 D-7·D-8 경계 회귀 |
| DL-04 | WHEN `warn_days`가 없으면 THE SYSTEM SHALL 기본 3일을 적용한다 | 기본값 회귀 |
| DL-05 | WHEN 상태가 `waiting`이고 `due`가 있으면 THE SYSTEM SHALL 이를 독촉일로 동일한 경고 계산에 반영한다 | waiting 날짜 회귀 |
| DL-06 | WHEN 상태가 `done` 또는 `paused`이거나 `due`가 없으면 THE SYSTEM SHALL 기한 경고에서 제외한다 | 상태·빈 날짜 회귀 |
| DL-07 | WHEN 유효한 경고가 없으면 THE SYSTEM SHALL 명시적인 빈 상태를 표시한다 | 빈 상태 회귀 |
| DL-08 | WHEN 인덱스 또는 날짜 검증이 실패하면 THE SYSTEM SHALL 이전 warnings view를 보존하고 실패 코드로 끝난다 | 실패 보존 회귀 |
| DL-09 | WHEN 경고 view를 생성하면 THE SYSTEM SHALL task 원본과 priority board를 변경하지 않는다 | CLI 통합·원본 무변경 확인 |

### 단계 규칙

- **기한 초과**: `due < 기준일`. 매일 남아 있는 동안 `D+N`으로 표시한다.
- **오늘 마감**: `due = 기준일`. `warn_days: 0`이어도 오늘 항목으로 표시한다.
- **경고 기간**: `0 < due - 기준일 <= warn_days`. 남은 날짜 별로 D-N 그룹에 표시한다. 예를 들어 기본 `warn_days: 3`이면 D-3부터 D-1까지, 개별 `warn_days: 7`이면 D-7부터 D-1까지 포함한다. D-8은 제외된다.
- 항목별 `warn_days`를 우선하며, 필드가 없을 때 3일을 쓴다. 읽을 수 없거나 음수인 값은 실행을 중단하지 않고 기본값으로 처리한다.
- `todo`, `doing`, `waiting`만 활성 상태로 간주한다. `waiting`의 `due`는 스키마 결정 #1의 독촉일이다. `done`, `paused`, 날짜 없는 task는 제외한다.

### 알림 피로와 안전 경계

매일 파일에 경고를 표시할 뿐 외부 알림이나 task 상태 변경을 만들지 않는다. 기한 초과는 해결되거나 원본 상태가 바뀔 때까지 유지한다. 인덱스에 파싱 오류가 있거나 활성 task의 `due`가 잘못되면 불완전한 성공 화면을 만들지 않고 이전 파일을 보존한다. 실행 로그는 AI4PKM cron 실행 기록과 건수 수준의 표준 출력만 사용한다.

### 업계 방식 조사에서 얻은 설계 원칙

AI4PKM의 공식 문서는 반복 작업을 CLI cron scheduler와 설정된 cron 시각으로 실행하는 예를 제공한다. 설치된 0.1.25 CLI에서는 orchestrator daemon(`ai4pkm -o`)이 cron scheduler를 시작하는 것도 확인했다. 기존 오케스트레이터를 사용하면 별도의 scheduler 의존성을 추가하지 않고 이 볼트의 실행 로그 경로를 유지할 수 있다. 이 경고 기능은 단순한 날짜 규칙이므로 LLM 판단 대신 결정적 Python 변환으로 만들었다. ([AI4PKM Workflow Automation](https://jykim.github.io/AI4PKM/workflows.html#workflow-automation) · [Python datetime](https://docs.python.org/3/library/datetime.html))
