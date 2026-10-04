---
title: "ADR 013 — M6 local Board UI"
created: 2026-10-03 05:41:00 -07:00
tags:
  - personal-ops-board
  - architecture-decision
---

## 결정

M6 화면은 단일 HTML 페이지와 Python 표준 라이브러리 기반 서버로 구현하고 `127.0.0.1`에만 바인딩한다. Markdown task 파일이 원본이며, 화면에서 허용한 소수 frontmatter 필드만 수정한다. 화면이 관찰한 파일 digest와 현재 파일이 다르면 거부한다. 본문은 입력 바이트 그대로 보존하고, 원자적 교체와 view 재생성 실패 시 rollback을 사용한다.

제안은 하나씩 검토하며 사용자가 명시적으로 승인한 proposal만 `items/`에 task로 만든다. UI는 task body를 편집하지 않으며 제안 승인 시에만 검토된 본문을 새 task에 담는다. 빠른 입력은 사용자의 결정에 따라 필수 분류와 실재하는 project/source 링크를 함께 입력받아 바로 `items/`에 저장한다. 링크 없는 입력은 미분류 경고를 새로 만들 수 있으므로 허용하지 않는다.

## 근거

기존 M1~M5의 파일 기반 계약과 POST-HANDOFF handoff mode를 유지하고, 별도 DB나 새 runtime을 추가하지 않으면서 시각적 관리 화면을 제공한다. `http.server`의 기본 bind 주소가 loopback 전용임을 보장하지 않으므로 주소를 명시한다. 화면 변경은 로컬 origin 및 무작위 프로세스 토큰을 검사한다. → [Python `http.server`](https://docs.python.org/3/library/http.server.html) · [Thin UI 개념](../../06-Board-UI/concepts/thin-ui.md#local-only-service)

## 결과와 제한

표준 라이브러리 서버는 설치·빌드 단계가 없고, 브라우저는 Markdown 원본을 직접 쓰지 않는다. 이는 단일 사용자·로컬 사용 범위에 한정된다. 다중 사용자 접근, 원격 접속, 자동 파일 감시 및 task DB는 추가하지 않는다. 빠른 입력은 프로젝트·출처 링크와 상태·tier·priority를 확인한 뒤에만 canonical task를 만든다.

## 검증

합성 fixture를 이용해 본문 바이트 보존, stale hash 거부, 필드 allowlist, tier validation, path traversal 거부, 개별 제안 승인, 새 task rollback, 동일 origin/session 토큰을 테스트한다. 운영 smoke check는 loopback 페이지와 state 조회만 수행하며 task 원본을 수정하지 않는다. 상세 결과는 [M6 WorkLog](../../vl_worklog/20261003_M6_Personal-Ops-Board.md#검증)에 기록한다.
