---
title: "Personal-Ops-Board M2 — Board 에이전트 요구와 설계안"
created: 2026-10-02 11:05:43
tags:
  - personal-ops-board
  - vibelearn-ai
  - worklog
---

## 오늘의 계획과 진행 위치

**모듈**: M2 — Board 에이전트 · **예상 학습 시간**: 4h. M0 사용자 문서 검토와 M1 DoD 6/6을 마쳤다. ① 요구 정리 → ② 업계 방식 조사 → ③ 설계 제안 후 사용자가 세 가지 설계 항목을 모두 승인했고, ④ 구현·검증 및 ⑤ 아키텍처 갱신을 완료했다. AI4PKM CLI 설치·registry 확인 후 사용자의 별도 승인으로 실제 Claude executor trigger를 한 번 실행했다.

PRD는 Board가 `views/priority-board.md`와 `Task Board.md`를 모두 쓰도록 적었지만, M3가 별도 마이그레이션·Task Board 생성 전환을 맡는다. 현재 `items/` 인덱스만으로 기존 Task Board를 다시 만들면 아직 마이그레이션하지 않은 행을 잃을 수 있다. 이 경계를 고려한 M2 제안이다.

## 업계 방식 조사

- Anthropic은 고정된 절차에 맞는 workflow가 예측 가능하고, 모델 판단의 유연성이 실제로 필요한 경우에 agent를 늘리라고 권한다. 보드의 tier 분류·정렬·요약은 규칙으로 정할 수 있으므로 출력 생성은 결정적인 Python 코드가 적합하다. [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- Kiro의 표준 Feature Spec은 요구 → 설계 → 실행 가능한 작업으로 이어지고, 요구가 명확해질 때까지 검토한 뒤 설계를 승인하는 흐름을 둔다. 현재 토픽의 WorkLog EARS + ARCHITECTURE + ADR을 이용한 변형과 맞는다. [Kiro Feature Specs](https://kiro.dev/docs/specs/feature-specs/) · [Requirements-First](https://kiro.dev/docs/specs/feature-specs/requirements-first/)
- 기존 토픽의 [ADR 007](../architecture/decisions/007-에이전트 연결은 열어 둔다.md)도 v1을 파일 공유로 시작하고 구조 변경은 별도 결정·승인을 받도록 한다.

**제안한 경계**: M2는 분류와 정렬을 Python으로 결정한다. AI4PKM/POB-Board prompt는 이 생성 단계를 호출·기록하는 얇은 진입점으로 둔다. LLM이 순서나 tier를 다시 해석하지 않는다. 자유 형식 우선순위 추천이 필요해진다면 요구를 따로 찾고 별도 출력 영역으로 검토한다.

## 오늘 정한 요구 — EARS 초안

| # | 요구 | 수용 기준 초안 |
|---|---|---|
| M2-E1 | WHEN 인덱서 캐시에 유효 task가 있으면 THE SYSTEM SHALL 각 task를 frontmatter의 tier에 해당하는 네 lane 중 한 곳에 정확히 한 번 표시한다 | 중복·누락 0, tier 1~4 각각 fixture 확인 |
| M2-E2 | WHEN tier 1 task를 표시하면 THE SYSTEM SHALL due 오름차순으로 정렬하고 동률은 priority·정규화 title·상대 경로로 결정한다 | 같은 입력을 여러 번 렌더링해 순서 동일 |
| M2-E3 | WHEN tier 2~4 task를 표시하면 THE SYSTEM SHALL P0→P3 priority 오름차순, 동률은 due 존재·due 날짜·정규화 title·상대 경로 순으로 표시한다 | 미설정 due와 동률 fixture 포함 |
| M2-E4 | WHEN task가 done이면 THE SYSTEM SHALL 활성 네 lane과 구분된 완료 영역에 표시하고 본문 `## 닫음` 여부를 닫음/완료 표시에 반영한다 | 합성 완료·닫음 본문을 각각 확인 |
| M2-E5 | WHEN 인덱스에 valid:false task 또는 warning/error가 있으면 THE SYSTEM SHALL 요약과 점검 대상을 검토 영역에 보존한다 | 원본 error/warning을 누락하지 않음 |
| M2-E6 | WHEN 보드를 생성하면 THE SYSTEM SHALL `views/priority-board.md`만 갱신하고 기존 `Task Board.md`를 변경하지 않는다 | 해시 전후 동일; Task Board 인계는 M3 승인 뒤 |
| M2-E7 | WHEN 입력 파싱·생성·저장이 실패하면 THE SYSTEM SHALL 이전 정상 보드를 보존하고 실패를 로그에 남긴다 | 실패 fixture에서 이전 결과 해시 유지 |
| M2-E8 | WHEN 같은 `index.json`을 다시 처리하면 THE SYSTEM SHALL 시간 필드 외 렌더링 결과의 내용과 순서를 동일하게 만든다 | generated_at을 제외한 본문 바이트 동일 |

사용자가 세 가지 설계 결정을 모두 승인해 이 요구를 M2 구현 계약으로 확정했다. 완료/닫음 영역, 정렬 동률 규칙, M3까지 기존 Task Board를 건드리지 않는 경계가 승인됐다.

## 승인된 설계와 구현 결과

| 부분 | 제안 | 이유 |
|---|---|---|
| 입력 | `AI/Tasks/views/index.json`의 tasks·problems | M1 파서를 재사용하고 원본을 다시 파싱하지 않음 |
| 규칙·정렬 | 비공개 `AI/Tasks/scripts/pob_board.py`의 순수 함수 | 고정 규칙을 모델 출력의 변동에서 분리 |
| 네 lane | `tier` 1~4 기준. waiting은 tier 2의 하위 묶음, paused는 tier 4에 둠 | 스키마 규칙을 자동 추정·수정하지 않음 |
| 완료 task | 활성 lane 밖에 `완료 및 닫음` 영역. 본문 `## 닫음`은 닫음, 그 외 done은 완료로 구분 | 스키마 결정 #10에 기록된 의미 유지 |
| 점검 필요 | `valid:false`와 error/warning을 별도 절에 원인 코드·파일·field별로 표시 | task를 숨기지 않고 검토 가능 |
| 출력 | `AI/Tasks/views/priority-board.md` 하나, 생성 시각·generator 표기 | 현재 M2의 검토용 view 경계 |
| Task Board | M2에서는 쓰지 않음. M3에서 기존 행과 items를 대조하고 승인받은 뒤 전환 제안 | 누락 위험과 PRD 3.1·M3 사이의 책임 충돌을 해소 |
| LLM 사용 | 순위·분류 결정에는 사용하지 않음. AI4PKM POB-Board prompt/node는 실행 진입점으로 등록 | 반복 출력 일관성·검증 가능성 |
| 실패 처리 | 새 결과를 임시 파일에 쓴 뒤 성공 시 교체. 실패면 기존 view 보존, 로그 기록 | 부분 파일이 현재 보드처럼 보이지 않게 함 |

**구현**: `AI/Tasks/scripts/pob_board.py` 결정적 renderer, 15개 M2 회귀 테스트, `_Settings_/Prompts/Personal Ops Board (POB).md`, `orchestrator.yaml`의 create/update node, 공개 합성 fixture와 M2 안내 문서를 추가했다. 생성 view는 `AI/Tasks/views/priority-board.md` 하나이며 root `Task Board.md`는 수정하지 않는다.

세 가지 승인 결정은 [ADR 010](../architecture/decisions/010-M2-보드는-비공개-view만-생성.md#결정)에 기록했다. lane과 tie-breaker 설명은 [M2 개념 안내](../02-Board-Agent/concepts/board-levels.md)에 있다.

## 검증

| 요구 | 결과 |
|---|---|
| M2-E1 | ✅ tier 1~4별 1건씩 중복 없이 배치 |
| M2-E2 | ✅ tier 1 due → priority → 정규화 title → 경로 정렬 |
| M2-E3 | ✅ tier 2~4 priority → due 존재·날짜 → 정규화 title → 경로 정렬 |
| M2-E4 | ✅ 합성 완료 1건·닫음 1건 분리, fenced code 내부 제목 무시 테스트 포함 |
| M2-E5 | ✅ invalid task와 문제 원인 코드를 별도 점검 영역에 보존 |
| M2-E6 | ✅ 합성/실제 렌더 실행 전후 root Task Board와 items 해시 동일 |
| M2-E7 | ✅ 실패 시 기존 결과 보존 테스트 통과 |
| M2-E8 | ✅ 동일 입력 반복 렌더링 결정성 테스트 통과 |

합성 fixture 6건은 `valid=6`, `error=0`으로 색인됐고 네 lane·완료·닫음 각 영역에 하나씩 출력됐다. 볼트 전체 M1+M2 회귀는 **30건 통과**했다. 실제 입력은 원본 task 69개를 다시 색인해 `valid=68`, 입력 파싱 오류 1개, warning 16개를 보존했다. 이를 바탕으로 비공개 우선순위 view를 생성했다. 원본 task와 root Task Board는 변경되지 않았다.

AI4PKM CLI 0.1.25를 공식 `jykim/AI4PKM` 저장소의 커밋 `688f7e3`에서 사용자 Python 3.13 환경에 설치했다. 사용자 Scripts 폴더를 PATH에 추가한 뒤 `ai4pkm --version`으로 실행을 확인했다. CLI는 두 POB node를 registry에 정상 로드했다. trigger 입력 약어가 대문자화되는 CLI 동작에 맞춰 노드 이름 suffix를 대문자로 정리하고, `input_type`을 `new_file`/`updated_file`로 나눴다. prompt에 필요한 registry frontmatter도 추가했다.

처음 `POB-Updated` 실행은 CLI의 약어 대소문자 조회 문제로 executor에 도달하지 않았다. 사용자가 개인 task 내용을 Claude executor로 보내는 1회 실행을 승인한 뒤 `POB-UPDATED`를 실행했다. AI4PKM log는 `Status: completed`를 기록했고 `index.json`은 11:44:47, `priority-board.md`는 11:44:52에 갱신됐다. 실행 중 `items/` 파일 변경은 0건이었고 root Task Board의 수정 시각도 그대로였다. CLI는 완료 표시의 기호를 CP1252 콘솔에 출력하다 예외를 내 프로세스 종료 코드는 1이었지만 실행 log 상태와 결과 파일로 agent 완료를 확인했다. 요청이 1회 실행에 한정되어 두 자동 trigger는 다시 `enabled: false`로 두었다.

## 사용자 수동 검토 (2026-10-02)

사용자가 실제 입력으로 생성된 `AI/Tasks/views/priority-board.md`의 분류와 정렬을 확인했고 이상 없다고 보고했다. 이후 `점검 필요` 절도 찾아 확인했으며 파싱 오류 1건과 인덱서 문제 17건을 확인했다. 인덱서 문제 합계 17건에는 파싱 오류 1건이 포함되어 있어 나머지 16건이 경고다. 경고 코드는 `project_missing` 10건과 `source_missing` 6건이다. 이 기록은 원본 task의 제목이나 세부 정보를 포함하지 않는다.

## Daily Retrospective

### What went well

사용자가 실제 출력의 분류와 정렬을 직접 확인해 이상이 없다고 확인했다. AI4PKM 1회 실행, 회귀 테스트, 보드 렌더링을 사람 검토와 연결해 검증했다.

### What could be improved

작업 로그의 진단 건수와 사용자 화면 확인 결과가 다르다. 실행 결과만 확인하지 말고, 점검 영역이 사용자에게 실제로 어떻게 보이는지도 명확히 확인해야 한다.

### Insights

결정적 출력 검증과 원본 데이터 품질 진단은 서로 다른 확인 단계다. 데이터 진단을 화면에 보존하면서, 경고가 조치 대상인지 정보성인지도 사람이 구분할 수 있어야 한다.

### Tomorrow's focus

진단 건수 차이를 해소하고 M2 DoD의 남은 검증·문서 상태를 정리한다. 이후 M3의 행별 대조 후보를 사람과 함께 판정하며, 이관이나 원본 수정은 별도 승인 전까지 하지 않는다.

---

## 다음 작업

M2 분류·정렬과 진단 표시의 사용자 검토는 통과했다. M2 DoD 중 기존 GDR·GWR 런타임 회귀는 사용자 데이터 파일을 다시 쓰는 실행 없이 검증할 방법을 확인한다. M3를 위해 비공개 `AI/Tasks/views/migration-reconciliation-preview.md`에 읽기 전용 제목 후보를 준비했다. Task Board와 `items/` 원본은 변경하지 않았고 자동 감시도 계속 비활성화 상태다. 다음에는 M3 요구·승인 설계를 확정한 뒤 행별 후보를 사람과 판정한다.
