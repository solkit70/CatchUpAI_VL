---
title: "M6 — Board UI WorkLog"
created: 2026-10-03 05:41:00 -07:00
tags:
  - personal-ops-board
  - vibelearn-ai
---

## M6 — Board UI

**단계**: 요구·스키마 재확인 → 로컬 화면 설계 → 사용자 승인 → 구현·합성 검증 → 실제 입력 read-only smoke → 아키텍처·모듈 기록. M6 UI 구현 진행 중이다. 빠른 입력은 사용자의 결정에 따라 project/source 링크와 필수 분류를 받아 `items/`에 바로 저장한다. M5의 다음 날 scheduler 확인과 별도로 진행한다.

## 요구와 설계 기준

로드맵 M6 DoD의 보드·경고 표시, 세 frontmatter 필드 편집과 본문 보존, 빠른 입력, 개별 inbox 승인, loopback 전용 서버를 구현 범위로 사용했다. 앱은 Markdown task 파일을 원본으로 유지하고 index·Board·warning은 갱신 가능한 view로 취급한다. 사용자 승인 없이 기존 task를 수정하지 않았다.

## 구현

- 비공개 `AI/Tasks/app/index.html`, `serve.py`: 네 tier lane, due warning, 완료/닫음, index 문제, proposal inbox, task 편집·작성 화면.
- 업데이트 허용 필드는 `status`, `priority`, `tier`로 제한한다. SHA-256 stale check, lock, 원자적 저장, body-byte 보존, tier 필수 조건 확인, view 재생성 실패 시 rollback을 사용한다.
- proposal은 개별 검토·승인만 허용하고 승인 시 source와 승인된 본문을 새 task에 기록한다.
- 서버는 `127.0.0.1`에 바인딩한다. Host/origin/session token을 확인하고 path가 포함된 요청 로그는 남기지 않는다.
- `test_pob_app.py`는 실제 task가 아닌 temporary synthetic fixture만 사용한다.
- 공개 M6 module 안내, thin UI 개념, 실행·문제 해결 안내, ADR 013을 작성했다. 예시에는 합성 내용만 사용했다.
- 라이브 시연 중 운영 task를 수정하지 않도록 `pob_demo_fixture.py`를 추가했다. 임시 볼트에 tier별 task·마감 경고·이력·정보성 점검 경고·승인 대기 제안을 채우고 종료 시 자동 제거한다. 진행 순서는 [라이브 시연 회귀 테스트](../06-Board-UI/guides/live-demo-regression-test-cases.md)에 기록했다.
- fixture 기대값 대조 중 활성 항목 통계가 `paused`를 포함하던 UI 집계 오류를 찾아 `todo/doing/waiting`만 세도록 수정했다.
- POB-01~08을 브라우저에서 합성 fixture로 직접 실행했다. 빠른 입력 후 `event.currentTarget`이 비동기 처리 뒤 null이 되어 성공 저장 후 화면 갱신이 중단되는 UI 오류를 발견해, form element를 await 전에 보관하도록 수정했다. 수정 후 task 생성·편집·tier 거부·완료 이동·proposal 단건 승인·새로고침 지속성과 종료 정리를 확인했다.

## 검증

| 확인 | 결과 |
|---|---|
| `python -m unittest discover -s AI\\Tasks\\scripts -p "test_pob_*.py" -v` | **56건 통과** (기존 42 + M6 14) |
| Python 구문 컴파일 | `serve.py`, fixture 실행기, M6 테스트 모듈 통과 |
| loopback HTTP 페이지 | 200, title 확인; warning detail container 존재 |
| 실제 `/api/state` read-only 조회 | 71 task, valid 71, invalid 0; 네 lane 표시. 조회에서 task 원본 수정 없음 |
| HTTP fixture end-to-end | 합성 task 생성→lane 반영→priority 수정 후 본문 보존→proposal 개별 승인·새 task 반영 통과; 임시 폴더는 테스트 종료 후 정리 |
| 브라우저 접근성 점검 | localhost 화면에서 lane·마감 경고·승인 대기·점검 필요·빠른 입력 폼 렌더링 확인 |
| 라이브 시연 fixture | POB-01~08 브라우저 수동 시나리오 합성 fixture에서 통과; 종료 후 fixture 서버 중단·임시 데이터 제거 확인 |
| 링크 확인 | 통과 — M6 module 4 Markdown files, broken links 0 |

## 남은 일

라이브 시연 전 [POB-01~08](../06-Board-UI/guides/live-demo-regression-test-cases.md)을 fixture UI로 직접 따라 하고 M6 Retrospective를 마친 뒤 DoD를 다시 판정한다. 운영 task를 생성·편집하지 않는다.

근거: [M6 로드맵](../vl_roadmap/20260927_RoadMap_Personal-Ops-Board.md#-m6--화면) · [M6 ADR 013](../architecture/decisions/013-M6-로컬-Board-UI.md#결정) · [M6 모듈 안내](../06-Board-UI/README.md)
