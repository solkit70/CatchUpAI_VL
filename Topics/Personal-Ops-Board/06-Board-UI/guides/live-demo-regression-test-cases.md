---
title: "M6 — Live Demo and Manual Regression Test Cases"
created: 2026-10-03 06:03:00 -07:00
tags:
  - personal-ops-board
  - regression-test
  - live-demo
---

## 목적

이 문서는 Personal Ops Board(POB)를 라이브 방송에서 소개하면서 주요 사용자 기능을 한 번씩 검증하는 진행표다. 버튼을 누르는 시연과 원본 Markdown·보드 반영을 함께 확인한다. 중요한 UI 변경 뒤에도 같은 시나리오를 반복해 기존 기능이 깨지지 않았는지 확인한다.

## 안전한 테스트 환경 시작

운영 보드는 실제 `AI/Tasks/items/` 파일을 수정할 수 있으므로 쓰기 기능 시연에는 사용하지 않는다. 합성 task만 생성하는 임시 vault를 사용한다. 이 fixture는 종료하면 임시 폴더와 그 안의 테스트 task·제안이 함께 삭제된다.

1. 볼트 루트에서 다음을 실행한다.

   ```powershell
   python AI\Tasks\scripts\pob_demo_fixture.py
   ```

2. 브라우저가 `http://127.0.0.1:8766/`을 열었는지 확인한다. 기본 포트가 사용 중이면 `--port 8767`을 붙여 실행한다.
3. 터미널에 `Synthetic fixture only:`와 임시 vault 경로가 출력되는지 확인한다. 화면에서 `Synthetic Demo` 항목을 확인한다. 이 두 신호가 없으면 쓰기 테스트를 진행하지 않는다.
4. 운영 보드 주소 `http://127.0.0.1:8765/`와 혼동하지 않는다. 방송 시연에는 `8766`의 합성 보드만 사용한다.

서버를 종료할 때는 실행한 터미널에서 `Ctrl+C`를 누른다. 정상 종료되면 스크립트가 임시 fixture 폴더를 제거한다. 다시 실행하면 처음 상태가 새로 만들어진다.

## 시나리오 개요

| ID | 기능 | 예상 확인 |
|---|---|---|
| POB-01 | 로컬 앱 시작·보드 요약 | loopback 주소, task 수, 활성 수, 승인 대기 수 표시 |
| POB-02 | 마감 경고 | overdue·today·upcoming 세 그룹과 항목 수 표시 |
| POB-03 | tier 보드·완료 이력·점검 영역 | 네 lane, 완료·닫음, 합성 정보성 점검 표시 |
| POB-04 | 빠른 입력과 필드 조건 | 링크 검증, due/waiting 입력 조건, task 생성 후 즉시 반영 |
| POB-05 | task 편집과 Markdown 원본 | 허용 필드 저장, 완료 이동, 본문 보존, 잘못된 tier 조합 거부 |
| POB-06 | 개별 proposal 승인 | 승인한 제안만 task로 생성되고 나머지는 대기 유지 |
| POB-07 | 새로고침·지속성 | fixture source를 다시 읽어 수정 결과 유지 |
| POB-08 | 종료·정리 | 서버 종료와 임시 데이터 제거 |

## 상세 테스트 케이스

### POB-01 — 로컬 앱 시작과 요약 카드

**준비**: 안전한 테스트 환경 시작 절차 완료.

**실행**: 화면 상단의 `이 컴퓨터에서만 열림` 표시, 전체 항목·활성 항목·마감 경고·승인 대기 초안 숫자를 확인한다.

**예상 결과**: 초기 상태는 전체 7개, 유효 7개, 활성 4개, 대기 제안 2개다. 활성 수에는 `todo`, `doing`, `waiting`만 들어가고 `paused`는 제외된다. 상단 주소는 `127.0.0.1:8766`이어야 한다.

### POB-02 — 마감 경고 확인

**실행**: 경고 배너 아래의 세부 그룹을 확인한다.

**예상 결과**: 기한 초과 1건, 오늘 마감 1건, 곧 마감 1건이 보인다. task 제목은 모두 `Synthetic Demo`로 시작한다. 각 항목에 날짜·D+N/D-N·상태가 표시된다.

### POB-03 — 네 tier lane, 이력, 점검 필요

**실행**: lane별 카드와 `완료와 닫음`, `점검 필요` 패널을 살펴본다.

**예상 결과**: lane은 tier 1 날짜가 정해진 일 2개, tier 2 약속·대기 1개, tier 3 프로젝트 1개, tier 4 멈춤·보류 1개다. 완료 1개와 닫음 1개는 별도 이력으로 보인다. 보류 task의 선택 필드인 프로젝트 링크를 비워 둔 합성 경고 1건이 `점검 필요`에 나타난다. 이 경고는 기한 생성과 보드 사용을 막지 않는다.

### POB-04 — 빠른 입력과 조건부 필드

1. `빠른 입력`으로 이동한다. status를 `todo`, tier를 `1`로 선택하면 마감일 입력이 나타나고 필수 표시가 되는지 확인한다. tier를 `3`으로 바꾸면 마감일 필드가 숨겨지는지 확인한다.
2. status를 `waiting`으로 선택하면 기다리는 대상 입력이 나타나고 필수 표시가 되는지 확인한다. status를 `todo`로 되돌린다.
3. 제목 `Synthetic Demo · 빠른 입력 회귀`, status `todo`, tier `3`, priority `P2`를 선택한다. 프로젝트 링크에 `[[Projects/Demo-Project]]`, 출처 링크에 `[[Sources/Demo-Source]]`를 입력한다. 본문에는 `## 맥락`과 합성 메모를 적는다.
4. 선택 사항으로 링크를 `[[Projects/Not-Found]]`로 바꾸어 저장을 시도한다. 링크 대상 오류가 나오고 task 수가 늘지 않는지 확인한 뒤 올바른 링크로 고친다.
5. `항목 만들기`를 누른다.

**예상 결과**: 필수값이 비어 있으면 브라우저가 저장을 막는다. 링크가 잘못되면 서버가 거절한다. 올바른 값으로 저장하면 성공 알림이 나오고 보드로 돌아가 새 task가 tier 3 lane에 즉시 나타난다. 전체 항목은 8개, 유효 8개, 활성 5개가 된다. 선택 필드 누락 정보성 경고는 계속 한 건이다.

### POB-05 — 상태·우선순위·tier 편집과 본문 보존

1. 카드 `Synthetic Demo · 프로젝트 작업`에서 priority를 `P1`로 바꾸고 `변경 저장`을 누른다. 저장 중 버튼이 비활성화되고 완료 알림이 뜨는지 확인한다.
2. fixture 파일 `demo-project.md`를 텍스트 편집기로 열어 frontmatter의 priority가 `P1`로 바뀌고 본문 `본문 보존 확인용 synthetic task입니다.`가 그대로 있는지 확인한다. 파일 경로는 서버 시작 터미널의 `Synthetic fixture only:` 경로 아래 `AI\Tasks\items\demo-project.md`다.
3. 같은 카드의 tier를 `1`로만 바꾸어 저장한다. due가 없는 task이므로 서버가 저장을 거절하고 tier 3에 남는지 확인한다. 새로고침해 원래 값으로 돌아온다.
4. 빠른 입력으로 만든 합성 task의 status를 `done`으로 바꾸고 저장한다.

**예상 결과**: 허용된 priority 변경만 Markdown frontmatter에 기록되고 본문은 보존된다. tier 1 필수 due가 없으면 저장이 거부된다. 완료 처리가 된 task는 활성 lane에서 빠져 완료 이력에 나타난다. 운영 task 파일은 변경되지 않는다.

### POB-06 — 제안 개별 검토와 승인

1. `승인 대기`로 이동한다. 합성 제안 두 건이 보이는지 확인한다.
2. `Synthetic Demo · 승인 제안 1`을 열어 본문을 읽는다. status `todo`, tier `3`, priority `P2`, 프로젝트 `[[Projects/Demo-Project]]`를 지정한다.
3. 제안 본문을 검토하고 `이 제안 승인`을 누른다.

**예상 결과**: 새 task 하나가 생성되고 보드에 표시된다. 제안 1은 승인됨으로 처리되고 승인 대기는 1건으로 줄어든다. 제안 2는 계속 승인 대기 상태다. 자동으로 여러 제안이 한꺼번에 승인되지 않는다.

### POB-07 — 새로고침과 지속성

**실행**: `새로고침`을 누르고 빠른 입력 task의 상태, priority 변경, 승인한 task, 남은 proposal 수를 확인한다.

**예상 결과**: 저장한 내용이 fixture Markdown에서 다시 읽혀 같은 lane·상태로 표시된다. 변경 사항이 브라우저 임시 상태에만 머물지 않는다.

### POB-08 — 정상 종료와 fixture 정리

**실행**: fixture 서버를 시작한 터미널로 돌아가 `Ctrl+C`를 누른다.

**예상 결과**: 서버가 종료되고 임시 vault 및 synthetic task·proposal 파일이 삭제된다. 다음 실행은 다시 초기값 7개 task·2개 proposal로 시작한다. 운영 보드의 항목 수와 원본 파일은 이 테스트로 바뀌지 않는다.

## 자동 회귀 검증과 수동 기록

UI를 바꾸거나 핵심 동작을 수정한 뒤에는 전체 회귀 테스트도 실행한다.

```powershell
python -m unittest discover -s AI\Tasks\scripts -p "test_pob_*.py" -v
```

이 테스트는 Markdown body 보존, stale edit 거부, 경로·필드 제한, loopback/origin/token 확인, 빠른 입력·lane 반영, proposal 개별 승인과 fixture 구성을 검증한다. 라이브 시연 뒤에는 각 POB-01~08의 통과 여부와 발견한 문제만 M6 WorkLog에 기록한다. 공개 WorkLog와 문서에는 실제 task 제목이나 사용자 데이터를 복사하지 않는다.
