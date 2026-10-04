---
title: "M5 합성 날짜 경계 사례"
created: 2026-10-03 05:00:00 -07:00
tags:
  - personal-ops-board
  - examples
---

## M5 합성 날짜 경계 사례

회귀 테스트는 실제 이름이나 운영 task 대신 합성 제목과 날짜를 사용한다. 기준일 `2026-10-03`에 다음 입력과 결과를 확인한다.

| 합성 입력 | 기대 결과 |
|---|---|
| due `2026-10-02`, todo | 기한 초과, D+1 |
| due `2026-10-03`, warn_days 0 | 오늘 마감, D-0 |
| due `2026-10-06`, warn_days 미지정 | 경고 기간 D-3 (기본값 3) |
| due `2026-10-10`, warn_days 7 | 경고 기간 D-7 |
| due `2026-10-11`, warn_days 7 | 경고에서 제외 (D-8 경계) |
| due `2026-10-03`, status waiting | 오늘 마감 (독촉일) |
| due 없음 또는 done/paused | 경고에서 제외 |

실행 가능한 테스트는 비공개 `AI/Tasks/scripts/test_pob_deadline.py`에 있다. fixture 입력은 메모리에서 만들기 때문에 합성 결과 파일이나 실운영 task 복사본이 공개 모듈 폴더에 생성되지 않는다.
