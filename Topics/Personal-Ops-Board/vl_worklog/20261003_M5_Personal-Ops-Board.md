---
title: "M5 — Deadline Agent WorkLog"
created: 2026-10-03 05:00:00 -07:00
tags:
  - personal-ops-board
  - vibelearn-ai
---

## M5 — Deadline Agent

**단계**: 요구 찾기 → 업계 방식 조사 → 설계 승인 → 구현·검증 → 아키텍처 기록. 사용자는 경고 규칙과 구현 진행을 승인했다. **현재 상태**: 코드·합성 회귀·수동 CLI 생성·AI4PKM cron scheduler 시각 실행 확인 완료. 10/4 다음 날 갱신 검증은 대기 중이다.

## 오늘 정한 요구 (EARS)

| ID | 요구 | 결과 |
|---|---|---|
| DL-01 | WHEN `due`가 오늘보다 이르면 THE SYSTEM SHALL 기한 초과로 표시한다 | 통과 — 합성 overdue D+1 및 운영 입력 경고 1건 |
| DL-02 | WHEN `due`가 오늘이면 THE SYSTEM SHALL 오늘 마감으로 표시한다 | 통과 — 합성 today 사례 |
| DL-03 | WHEN 남은 날짜가 `warn_days` 이하인 활성 task면 THE SYSTEM SHALL 남은 날짜 D-N으로 표시한다 | 통과 — 기본 D-3·개별 D-7 포함, D-8 제외 |
| DL-04 | WHEN `warn_days`가 없거나 잘못됐으면 THE SYSTEM SHALL 기본 3일을 사용한다 | 통과 — 누락·잘못된 값·음수 합성 사례 |
| DL-05 | WHEN status가 `waiting`이고 due가 있으면 THE SYSTEM SHALL due를 독촉일로 취급한다 | 통과 — waiting 오늘 마감 사례 |
| DL-06 | WHEN status가 `done`·`paused` 또는 due가 없으면 THE SYSTEM SHALL 경고에서 제외한다 | 통과 — 합성 상태 제외 및 날짜 없음 |
| DL-07 | WHEN 경고가 0건이면 THE SYSTEM SHALL 명시적인 빈 상태를 표시한다 | 통과 — 합성 빈 상태 |
| DL-08 | WHEN index 또는 날짜 검증이 실패하면 THE SYSTEM SHALL 이전 view를 보존하고 실패한다 | 통과 — invalid task·잘못된 due에서 이전 출력 바이트 보존 |
| DL-09 | WHEN Deadline view를 생성하면 THE SYSTEM SHALL item 원본과 priority board를 변경하지 않는다 | 통과 — 실제 index 후 Deadline 생성 시 priority board SHA-256 불변 |

## 업계 방식과 설계

M1/M2의 결정적 Python 도구와 기존 AI4PKM runtime을 재사용했다. 공식 AI4PKM workflow 문서는 반복 workflow를 cron scheduler와 cron 설정으로 실행하는 방법을 제시한다. 날짜 판정은 Python `datetime` 날짜 차이로 처리하며, 일자 기반 due에 시각대 변환을 적용하지 않는다. LLM은 일정 등록과 실행 순서만 연결하고 조건 분기는 renderer가 수행한다. → [경고 단계](../05-Deadline-Agent/concepts/warning-levels.md) · [ADR 012](../architecture/decisions/012-M5-결정적-마감-경고.md#결정)

## 구현

- 비공개 `AI/Tasks/scripts/pob_deadline.py`: 읽기 전용 index parser, 기한 초과·오늘·D-N 분류, D-N 그룹, 빈 상태, 원자적 출력, 기준일 테스트 인자
- 비공개 `AI/Tasks/scripts/test_pob_deadline.py`: 합성 회귀 9건; 전체 POB regression과 함께 총 42건 통과
- 비공개 `AI/Tasks/views/warnings.md`: 실제 10/3 수동 생성 결과 (기한 초과 1, 오늘 0, 사전 경고 3). task 제목을 로그나 WorkLog에 복사하지 않음
- 프롬프트: `_Settings_/Prompts/Personal Ops Board Deadline (POB-Deadline).md`
- `orchestrator.yaml`: AI4PKM node `Personal Ops Board Deadline`, 활성화. 원래 05:00에서 10/3·10/4 검증을 위해 임시 05:15로 변경했다. 내일 확인 후 원래 시각으로 복구할 것
- 공개 M5 산출물: `05-Deadline-Agent/` 개념·합성 사례·실행 안내
- `ARCHITECTURE.md` v0.6 및 ADR 012, Topic README·Roadmap·daily prompt 갱신

## 검증

| 확인 | 결과 |
|---|---|
| `python -m unittest discover -s AI/Tasks/scripts -p 'test_pob_*.py' -v` | **42건 통과** (기존 33 + M5 9) |
| 운영 인덱스 재생성 | 71 task, valid 71, error 0, warning 11 |
| 운영 warnings view 생성 | 통과 — overdue 1, today 0, upcoming 3; 제목은 이 WorkLog에 기록하지 않음 |
| priority-board 보존 | 통과 — 실행 전후 SHA-256 동일 |
| `ai4pkm --debug --orchestrator-status` | 통과 — `POB-DEADLINE` loaded, 총 6개 활성 agent |
| `ai4pkm trigger POB-DEADLINE` | 통과 — 25.33초 완료, `_Settings_/Logs/2026-10-03-034950-POB-DEADLINE.log`; warnings view 갱신 완료 |
| cron 자동 실행 (10/3) | 통과 — 05:05:25 예약 시작·05:05:43 완료, 이어 05:15:56 시작·05:16:09 완료. `warnings.md` 각각 05:05:39·05:16:06 갱신 |
| 다음 날 자동 갱신 | 대기 — 10/4 방송 준비 중 05:15 재실행 및 갱신 확인 예정 |
| 링크 경로 | 통과 — M5 markdown 4개 파일, broken link 0 |

## 미완료 DoD와 다음 행동

10/3에는 절전으로 05:00 예약 시각을 지나친 뒤 05:05로 옮겨 재실행했고, 그 뒤 05:15 예약도 통과했다. 로그상 scheduler는 05:05:25와 05:15:56에 각각 실행을 시작했다. 실행 뒤 `warnings.md`가 갱신됐다. `orchestrator.yaml`은 10/4 방송 시험을 위해 05:15로 임시 설정되어 있고, 실행기를 종료했다. 내일은 절전되지 않도록 PC를 켜 두고 05:15 전에 `ai4pkm -o`를 시작한다. 로그와 `warnings.md`를 확인한 뒤 cron을 원래 05:00으로 복구한다. 다음 날 검증 전까지 M5 DoD는 완료로 표시하지 않는다.

Daily Retrospective는 오늘 구술을 저장한 [[Roundup/2026-10-03 - Daily Roundup#Interpretation|Daily Roundup 해석]]을 참조한다.
