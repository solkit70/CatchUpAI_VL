---
title: "M5 — 사용 패턴 가이드 · 정리하다가 M2 결론 하나가 틀린 것을 찾았다"
created: 2026-09-27 17:05:00
author:
  - "Claude Code"
topic: "Claude-Artifacts-Routines"
module: "M5"
tags:
  - vibelearn-ai
  - worklog
  - claude-artifacts-routines
---

## 세션 개요

| 항목 | 값 |
|---|---|
| 날짜 | 2026-09-27 (일) — M4 직후, 사용자 「M5 를 진행 해 주세요」 |
| 실소요 | 약 25분 (예상 1.5h) — M1~M4 기록이 이미 `[실측]` 표기로 정리돼 있어 모으기만 하면 됐다 |
| 직전(M4b) 개선할 점 | 「요일은 cron 에서 바로 옮겨 적는다」 → 플레이북 루틴 항목은 cron·로그 값을 그대로 옮겼다 |
| 결과 | 패턴 6장 · 안티패턴 10개 · 플레이북 1편 · **M2 결론 정정 1건** |

## 오늘의 학습 목표

- [x] 패턴 카드 5장 이상 (실물 링크 + 근거) — 6장 + 후보 2
- [x] 안티패턴 목록 (날짜 · 출처) — 10개 + 문서로만 확인 2
- [x] 플레이북 1편 조립 — 결정 흐름(mermaid) · 체크리스트 · 실물 8개
- [ ] 「다른 사람이 이 문서만 보고 따라 할 수 있는가」 — 사용자 판단

## 진행 내용

1. **근거 모으기** — M1 상태표 · M2 sharing-matrix · M2 troubleshooting · M3 lab-log · db-roundtrip · M4 audit · second-routine 을 다시 읽고 `[실측]` 만 골랐다
2. **패턴 6장** — ① 공유는 정적부터 ② 세션 쓰기는 `if_version` ③ 알림은 조건부/항상을 목적으로 ④ 볼트면 로컬 ⑤ 외부에 못 닿으면 환경 네트워크부터 ⑥ 공유 버전 Latest + 시크릿 창. 「회의 중 즉석 제작」 · 「AI 가 도구를 고르게」는 비교 실측이 없어 **후보로 내림**
3. **안티패턴 10개** — 9/3~9/27 에 겪은 것만
4. **플레이북** — 세 질문 흐름 → Artifact 체크리스트 8 · Routine 체크리스트 8 · 실물 8

## 문제 해결 로그

| 발견 | 처리 |
|---|---|
| **M2(9/13) 「이 계정에서 댓글 불가」 ↔ M3(9/27) 댓글 · Send to Claude 작동** | M2 기록은 지우지 않고 정정 줄을 붙였다 → `02-.../guides/sharing-matrix.md`. 안티패턴 10 「문서 한 문장으로 불가라고 닫기」 추가. 다른 사람(조직 밖 · 공개 링크 방문자)의 댓글 가능 여부는 여전히 미확인 |
| M2 의 「공유 버전 Latest 토글이 안 보인다」 미해결 질문 | 9/25 사용자가 BL 입장 안내 Version 4 를 Latest 로 바꾼 실측으로 답 → 패턴 6 |
| DoD 「플레이북 예시 링크가 전부 시크릿 창에서 열린다」 | 실습 예제 5개 · 루틴 2개는 **비공개**라 시크릿 창에서는 안 열리는 것이 정상. 플레이북 실물 표에 공개 범위를 명시해 대신했다 — 사용자 판단 「간단하게」에 맞춰 공개 전환은 하지 않음 |

## DoD 체크리스트 (M5)

- [x] 패턴 5장 이상 · 안티패턴 목록 · 플레이북 1편
- [~] 🔴 실물 링크 — 전부 실제 실물(URL 확인됨). 시크릿 창 열림은 공개 1건만 해당, 나머지는 비공개라 범위 표기로 대신
- [x] README · 링크 검사
- [x] WorkLog · Daily Retrospective · 직전 개선점

## Daily Retrospective

- **잘된 점**: 모듈마다 `[실측]`/`[문서]`/`[추론]` 을 붙여 둔 덕에 패턴 고르기가 기계적이었다. 추론뿐인 후보 둘을 패턴에서 뺐다
- **개선할 점**: M2 에서 「불가」를 문서로만 닫았고 2주 동안 그대로였다 — 부정 결론일수록 최소 예제로 확인한다
- **인사이트**: 정리 모듈(M5)이 **검증 모듈** 역할도 한다. 흩어진 기록을 한 곳에 모으자 서로 어긋나는 결론이 드러났다 — VibeLearn AI 에서 Capstone 전에 「모아 보기」 모듈을 두는 이유
- **다음**: M6 Remotion 영상 — 플레이북이 대본 뼈대. 영상에 「댓글 불가 → 가능」 정정 장면을 넣을지 사용자에게 묻는다

## 참조 및 산출물

- 신규: [README](../05-Usage-Patterns/README.md) · [playbook](../05-Usage-Patterns/guides/artifacts-routines-playbook.md) · [patterns](../05-Usage-Patterns/guides/patterns.md) · [anti-patterns](../05-Usage-Patterns/guides/anti-patterns.md)
- 수정: [M2 sharing-matrix](../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix.md) (정정 줄) · 로드맵 진행표
