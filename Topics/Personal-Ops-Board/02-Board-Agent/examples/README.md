---
title: "M2 합성 입력과 기대 결과"
created: 2026-10-02 11:32:31
tags:
  - personal-ops-board
  - examples
---

## M2 합성 입력과 기대 결과

`fixtures/`에는 실제 할 일이나 사람 이름이 없는 공개 합성 task 여섯 개가 있다. 입력 폴더를 인덱싱하고 Board renderer에 넘기면 tier 1 날짜, tier 2 대기, tier 3 프로젝트, tier 4 보류, 완료, 닫음을 각각 확인할 수 있다.

| 합성 항목 | 기대 영역 | 확인할 점 |
|---|---|---|
| 합성 날짜 확인 | Tier 1 | due 표시 |
| 합성 대기 확인 | Tier 2 | 상태가 대기로 남음 |
| 합성 프로젝트 확인 | Tier 3 | 프로젝트 lane |
| 합성 보류 확인 | Tier 4 | 멈춤 상태 보존 |
| 합성 완료 확인 | 완료 | `## 닫음`이 없으므로 완료 |
| 합성 닫음 확인 | 닫음 | 실제 `## 닫음` heading 감지 |

실행 명령은 [수동 실행 안내](../guides/run-board.md)를 따른다. 이 예제의 결과 파일을 공개 저장소에 추가하지 않는다. renderer는 비공개 `AI/Tasks/views/`에만 출력한다.
