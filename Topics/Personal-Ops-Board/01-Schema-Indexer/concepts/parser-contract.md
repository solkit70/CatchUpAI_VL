---
title: "읽기 전용 파서 계약"
created: 2026-10-02 10:43:41
tags:
  - personal-ops-board
  - vibelearn-ai
---

## 읽기 전용 파서 계약

M1은 원본을 읽어 캐시를 만드는 단계다. 입력의 오류를 보여 주되 값을 추정해서 고치지 않고, 파싱 실패도 결과에 보존한다. → [M1 요구와 검증](../../vl_worklog/20261002_M1_Personal-Ops-Board.md#오늘-정한-요구--ears)

1. `items/*.md`만 읽고 `_schema.md`와 하위 폴더는 제외한다.
2. 필수 필드는 `type`, `title`, `status`, `tier`, `priority`, `created`, `updated`다. status·tier·priority의 허용값과 done_at을 검사한다.
3. tier는 일방향 검증이다. tier 1의 due, waiting의 tier 2·waiting_on, paused의 tier 4를 검사한다. paused의 waiting_on은 재개 조건으로 보존한다.
4. project/source의 위키링크는 볼트 루트·AI 생략 경로·이름을 해석한다. 0개는 unresolved, 여러 개는 ambiguous이며 섹션 제목 존재는 검사하지 않는다.
5. 모든 입력이 tasks에 남는다. 파싱 실패는 valid:false와 frontmatter_parse_error로 남긴다.

| 심각도 | 의미 | 예 |
|---|---|---|
| error | valid:false | YAML 실패·필수 누락·허용값 오류·done_at 누락 |
| warning | 경고만, 원본 무변경 | tier 불일치·권장 필드 누락·링크 오류 |
| info | 향후 보드 기본값 안내 | next_action이 없으면 title 사용 안내 |

현재 인덱서는 next_action을 실제로 채워 넣지 않고 안내만 남긴다. 본문·파일명으로 상태나 due를 추정하지 않으며 type은 필수 존재만 확인하고 task 외 타입 제한은 별도 구현하지 않았다.

## 스키마 결정 반영표

원본 사양은 비공개 볼트 `AI/Tasks/items/_schema.md`의 결정 로그다. 이전 계획은 9건 기준이었지만 10/2 현재 10건이며, 아래는 실제 이름·할 일 내용을 제거한 공개용 대응표다. 입력 운영 규칙까지 파서 기능으로 오인하지 않도록 구분한다.

| # | 결정 요지 | M1 대응·검증 | 이후 범위 |
|---|---|---|---|
| 1 | tier 2에도 due 허용 | due가 있다고 tier 1로 바꾸지 않음, 합성 검사 | Deadline의 독촉일 표시 |
| 2 | priority 문자열 표기 | P0~P3 판정, 따옴표 있는 YAML 합성 파싱 | 입력 작성 규칙 유지 |
| 3 | project는 기존 파일 | 존재·중복 링크 검사, 새 문서 자동 생성 없음 | 생성·변경은 사람 판단 |
| 4 | 단계적으로 원본 투입 | 현재 존재하는 전체 파일만 읽음, 임의 task 생성 없음 | M3 마이그레이션 |
| 5 | 프로젝트 투입 시기 유보 | items 밖 보드 행을 자동 수집하지 않음 | M2·M3 승인 |
| 6 | 확인 후 파일명 변경 | 메타데이터를 기준으로 읽고 현재 file 경로 보존, 이름 변경 합성 검사 | 이름 변경은 사람·화면 |
| 7 | due 변경 시 파일명 변경 | 파일명 날짜로 due를 덮어쓰지 않음, 합성 검사 | 운영 규칙 유지 |
| 8 | waiting일 때만 waiting_on 필수, paused 우선 | tier 2의 빈 값·paused 재개 조건 허용, 합성 검사 | 자동 tier 추정 없음 |
| 9 | 상시 작업 doing·tier 3·due 비움 | 상태 유지·due 경고 없음, 합성 검사 | 본문 트리거 표시 M2 검토 |
| 10 | 취소도 done·done_at·본문 사유 | done과 done_at 허용, 원본 본문 보존 | 완료/취소 구분 표시 M2 요구 찾기 |

## JSON과 성능

JSON은 generated_at·generated_by·items_dir·tasks·problems를 가진 재생성 가능한 캐시다. 날짜는 JSON 문자열로 저장하며 valid:false 항목도 지우지 않는다. 경로는 직접 확인하고 이름 색인은 필요한 순간 한 번 만들며, 현재 입력의 전체 실행 목표는 5초다. → [성능 결정](../../architecture/decisions/009-링크는%20직접%20확인하고%20색인은%20지연%20생성.md#결정)
