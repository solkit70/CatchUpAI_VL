---
title: "CVL8 — 비공개 금칙 목록과 승인 화면 경고"
created: 2026-10-02 10:14:26
author:
  - "Codex"
topic: "Live-CoMC-App"
module: "CVL8"
tags:
  - vibelearn-ai
  - worklog
  - live-comc-app
  - safety
---

## 세션 개요

10/2 사용자 제공 Claude 리뷰와 구현 지시에 따라 M11에 두 가지 제한적인 보완을 추가했다. 검색 대상과 LIVE·REVIEW·MUTE·확장 레인 승인 흐름은 유지하며, 개인 기록은 근거 후보로 계속 허용한다. → [기존 M11 구현](20261001_M11_Live-CoMC-App.md#4-콘솔과-승인)

> 지금의 구조(볼트·웹·창작은 진행자 승인 뒤에만 발화)는 Human In The Loop 으로 적절하다 — 바꾸지 않는다.

이 원문은 사용자가 이번 작업에 제공한 리뷰·진행 지시에서 인용했다. 실제 고객 이름과 목록 내용은 이 기록에 옮기지 않았다.

## 🎯 오늘의 학습 목표

- [x] 로컬 비공개 금칙 목록과 색인·사용 직전·질문·최종 문장 검사를 연결한다.
- [x] 승인 대상 claim_map에 따른 개인 기록 경고·출처 목록을 콘솔에 표시한다.
- [x] 기존 90건과 합성 회귀 테스트를 실행하고 수동 사례 2개를 추가한다.
- [ ] 운영 콘솔 재시작 후 실제 대기·승인·음성·OBS를 확인한다.

## 📚 진행 내용

### 비공개 금칙 목록

[deny_terms.py](../07-CoMC-Engine-POC/src/deny_terms.py)는 비공개 JSON의 version·terms를 검증하고 NFKC·공백 정규화·대소문자 무시 부분 일치를 적용한다. 초기 목록 4개는 요청받은 항목만 비공개 `output/private/m11/deny_terms.json`에 넣었다. 공개 정책 두 사본에는 경로·동작 규칙만 기록했고 실제 목록은 Git에서 제외된다.

[evidence_lanes.py](../07-CoMC-Engine-POC/src/evidence_lanes.py)는 quote·title·path를 색인과 검색 직전에 검사하며, 금칙 질문을 볼트·웹에 보내기 전에 거절한다. [게이트](../07-CoMC-Engine-POC/src/05_verify_and_gate.py)는 모든 레인의 금칙 문장을 `m11.deny_term`으로 제거한다. trace·공개 출력·콘솔 로그에는 금칙 문자열을 남기지 않고, 목록 누락·손상은 내용 없는 경고와 빈 목록으로 처리한다.

### 승인 화면 경고

[렌더러](../07-CoMC-Engine-POC/src/06_render_output.py)는 살아남은 문장의 claim_map 출처를 별도 비공개 메타데이터로 저장한다. Journal/·AI/Roundup/ 출처가 있으면 [콘솔](../09-Desktop-Shell-and-Overlay/examples/engine/comc_console.py)의 승인 버튼 옆에 경고와 파일·섹션을 표시한다. 대기 발화 시각이 일치해야 표시하므로 이전 답의 경고가 새 답에 붙지 않는다. 경고는 output·OBS·spoken에 추가하지 않고 기존 승인도 막지 않는다.

## 자동 검증과 남은 확인

pytest 기존 90건에 신규 30건을 더해 **120건 통과**했다. 합성 용어로 정규화·조사·색인 제외·기존 색인의 새 목록 재검사·질문 거절·웹 근거 세 필드 제외·모든 레인 게이트·파일 없음/손상·로그/공개 출력 누출 방지·claim_map 경고·승인 허용·이전 대기 경고 제거를 확인했다. → [CVL8 회귀 테스트](../07-CoMC-Engine-POC/tests/test_cvl8_deny_terms.py)

실제 Chromium에서 합성 상태로 경고·출처 표시, 승인 버튼 활성 유지, 목록 개수·손상 안내, 대기 해제·비개인 출처 경고 숨김, OBS 미포함을 확인했고 JS 오류가 없었다. 실제 모델·검색·음성 API나 운영 음성 재생은 이번 CVL8 검사에서 호출하지 않았다. → [수동 F-09·F-10](../10-Live-Rehearsal-Capstone/guides/manual-regression-test-cases.md#f-m11-자동볼트웹창작과-출처)

## 📊 DoD 체크리스트

- [x] 비공개 목록 초기화와 공개 정책 동기화.
- [x] 색인·사용 직전·질문·모든 레인 최종 문장 검사.
- [x] 개인 기록 승인 경고·출처·이전 답 구분.
- [x] 합성 자동·브라우저 검사 및 76건 수동 문서 갱신.
- [ ] 운영 콘솔·목소리·OBS 확인.

## 💡 Daily Retrospective

금칙 목록은 운영자가 선택한 정보만 추가로 제한하고 개인 기록 검색 전체를 막지 않는다. 목록 누락·손상은 요청대로 빈 목록으로 진행하므로 방송 전 콘솔의 개수·경고를 확인해야 한다. 부분 일치는 정상 단어에도 걸릴 수 있어 운영자가 목록을 조정하며, 커밋·푸시는 하지 않았다.

## 변경 파일

아래 목록은 이번 CVL8에서 수정하거나 추가한 파일만 정리했다. 기존 작업의 미커밋 변경은 유지했고 staging·커밋·푸시를 하지 않았다.

| 구분 | 파일 |
|---|---|
| 금칙 목록·로그 공통 처리 | `07-CoMC-Engine-POC/src/deny_terms.py`(신규), `common.py` |
| 검색·생성·검증·출력 | 같은 src의 `evidence_lanes.py`, `03_classify_intent.py`, `04_compose_answer.py`, `05_verify_and_gate.py`, `06_render_output.py` |
| 콘솔 | `09-Desktop-Shell-and-Overlay/examples/engine/comc_console.py` |
| 공개 정책 | `07-CoMC-Engine-POC/data/safety_policy.json`, `03-Data-Contracts-and-Safety/examples/safety_policy.json` |
| 자동 테스트 | `07-CoMC-Engine-POC/tests/test_cvl8_deny_terms.py`(신규) |
| 문서 | `README.md`, `10-Live-Rehearsal-Capstone/guides/operator-guide.md`, `manual-regression-test-cases.md`, 이 WorkLog(신규) |
| 로컬 비공개 목록 | `07-CoMC-Engine-POC/output/private/m11/deny_terms.json`(신규, 초기 4개, Git 제외) |
| 볼트 작업 기록 | `AI/Tasks/Task Board.md`, `AI/Tasks/items/CoMC M11 근거 레인 확장.md` |

## 추가 수정 — 금칙 목록 캐시 (Claude Code 리뷰 뒤, 2026-10-02)

Claude Code 리뷰에서 볼트 검색이 CVL8 뒤로 크게 느려진 것을 찾았다. `deny_terms.matches()` 가 부를 때마다 금칙 목록 파일을 새로 읽어, 볼트 검색 한 번에 파일을 **49,760번** 읽고 있었다. [deny_terms.py](../07-CoMC-Engine-POC/src/deny_terms.py) 에 캐시를 넣어 파일의 수정 시각 · 크기가 바뀔 때만 다시 읽고, 정규화한 금칙어도 한 번만 만든다. 방송 중 진행자가 목록을 고치면 다음 호출에서 바로 반영되고, 파일 없음 · 깨짐 동작과 경고 1회 규칙은 그대로다.

| 볼트 검색 (실제 볼트) | 고치기 전 | 고친 뒤 |
|---|---:|---:|
| 「지난주 캐치 앱 첫 상담 이야기」 | 18.6~21.9초 | 2.8초 |
| 「지난번 화장품 회사 상담 내용」 | 6.1초 | 1.1초 |
| 「김승규 기자님 소개 고객」 | 1.4초 | 1.0초 |
| 금칙어 질문 (고객 이름 · 마진 · 단가) | 0.0초 거절 | 0.0초 거절 |

테스트 3건을 더했다(같은 파일이면 한 번만 읽음 · 고치면 반영 · 지우면 빈 목록). pytest 총 123건 통과.
