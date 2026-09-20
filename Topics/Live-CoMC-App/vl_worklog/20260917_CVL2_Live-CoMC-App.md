---
title: "CVL 2 — OBS 를 맞추고 4회차를 돌려 A·B 를 판정하다"
created: 2026-09-17 17:55:00
author:
  - "Claude Code"
topic: "Live-CoMC-App"
module: "CVL"
tags:
  - vibelearn-ai
  - worklog
  - live-comc-app
  - cvl
---

## 세션 개요

| 항목 | 값 |
|---|---|
| 날짜 | 2026-09-17 (목) 16:00 준비 · 17:00~17:55 사무실에서 OBS 켜고 진행 |
| 실소요 | 약 1시간 35분 (사용자 외출 대기 약 40분 별도 · LLM 호출 7회) |
| 성격 | CVL 유지보수 2 — 4회차 무관중 리허설 · OBS 방송 프로필 · 발화 길이 상한 |
| 결과 | **4회차 사고 0건 → A GO (Live #28 부터 REVIEW 상시) · B 조건부 GO (LIVE 는 2부 CoMC 구간)** · 글자 수 상한 120 |

## 한 것

### 1. OBS 방송 프로필 — 파일로 읽고, 사용자가 화면에서 바꿨다

OBS 가 꺼진 동안 `basic/scenes/Untitled.json` · `profiles/Untitled/basic.ini` 를 읽었다. 8/31(M6b)에 넣은 **「Audio Input Capture」= CABLE Output 이 방송 씬에 이미 있었고** Simple 출력이라 송출 믹스에 실린다. 빠진 건 진행자 모니터링뿐이었다.

사무실에서 사용자가 실제 화면을 열자 전제가 하나 바뀌었다 — **진행자는 MV7 헤드폰이 아니라 Galaxy Buds2 Pro 로 듣고, 그것이 Windows 기본 재생 장치**였다. 모니터링을 Buds 로 하면 Desktop Audio(기본 장치 캡처)가 되잡아 두 번 송출된다. A안으로 갔다: Audio Input Capture 모니터링 **Enabled**(OBS 32 의 "Monitor and Output") · 모니터링 장치 **Buds** · **Desktop Audio → Realtek 스피커**(사실상 끔). 대가: 컴퓨터 소리가 송출에 안 실린다 — 영상 트는 회차엔 되돌린다.

검증(사용자 실청): Buds 에서 들림 · 믹서에서 Audio Input Capture 만 움직임 · Desktop Audio·Mic/Aux 조용 · 유튜브를 Buds 로 틀어도 OBS 무반응.

### 2. 4회차 — 질문 10건, 사고 0건

`examples/rehearsal4_driver.py` 가 데몬을 인프로세스로 띄워 `rehearsal-log-4.md` 의 질문 8개(파트 전환 2단계라 10건)를 넣었다. 오버레이 서버·재생기는 별도 프로세스. 프리플라이트 PASS 7 · WARN 2 · FAIL 0.

| # | 겨냥 | 결과 |
|---|---|---|
| 1 | 사고 8 | 확정 2개를 확정으로, "후보" 없음 ✅ |
| 2 | 사고 9 | "이번 방송에서 확정으로, 9/17 에 Topic 이 완료됐고…" ✅ |
| 3 | 사고 10 | 주간 영상 → ④ `cross_part` 거절 · 화면 비움 ✅ |
| 4a/4b | 사고 7 | 1부(미정) 전환 → ② 거절·침묵 / 2부 복귀 → 정상 답 ✅ |
| 5 | 사고 11 | `unknown` 거절 · 화면 비움 ✅ |
| 6 | B 소리 | 271자 34초 재생 → Buds ✅ · 믹서 ✅ · **패닉(MUTE)으로 77% 에서 끊김** ✅ |
| 7 | — | ③ `completion_confusion` → HITL (정책대로 · 오탐 후보) |
| 8 | 길이 | 180자 23초 끝까지 ✅ · 어미 붕괴 없음 |

LLM 완주 6회 4.0~7.3초. 소리 3조건(송출 믹스 · 모니터 · 패닉)을 **사용자가 귀와 눈으로** 확인했다.

### 3. 글자 수 상한

실측 ≈7.7자/초. 문장 수 상한 5로는 30초가 넘는다. `safety_policy.length_hardcut.max_chars` = brief 90 · **default 120** · detailed 180. ⑤ 가 문장 단위로 뒤에서 자르고 최소 1문장은 남긴다. 187자 → 119자 확인. M8 9/9 · 재현 10/10 유지.

**함정 하나** — 정책은 `data/safety_policy.json` **사본**을 읽는다. M3 원본만 고쳤더니 적용이 안 되고 drift 경고만 났다. 둘 다 고쳤다.

### 4. 작은 수정

- 데몬 `call()` — ④ 의 `return 2`(거절)를 성공으로 읽어 ⑤ 까지 흘러가던 표기 결함 (기능 영향 없음)
- 백그라운드 프로세스 정리 중 PowerShell 패턴이 **내 셸까지 죽였다** — 프로세스 이름(`python.exe`)으로 먼저 거른다

## 판정

| 갈래 | 판정 |
|---|---|
| A 화면 | ✅ **GO** — Live #28(9/20)부터 REVIEW 상시 |
| B 소리 | ✅ **조건부 GO** — 재생기 기동 · OBS 설정 유지 · 상한 120 · **LIVE 는 2부 CoMC 구간에서만** |
| C 입력 | ⏳ NO-GO 유지 |

Live28 Rundown 「방송 시작 전」에 당일 절차 6단계와 OBS 조건을 적었다.

## Insights (인사이트)

### 전제는 화면을 열어야 무너진다

파일로 읽은 OBS 구성은 정확했지만 "진행자는 MV7 로 듣는다"는 전제는 틀렸다 — Buds 였다. 파일에는 모니터링 장치가 `Default` 라고만 적혀 있었고, Default 가 무엇인지는 그날 연결된 블루투스가 정한다. **설정 파일은 구조를 말하고, 실제 값은 사람이 앉은 자리가 말한다.**

### 침묵 4건은 실패가 아니라 결과다

10건 중 4건이 침묵인데 사고는 0이다. 셋은 정확히 설계한 침묵(다른 파트 · 미정 파트 · 무의미 발화)이고, 하나는 정책이 만든 HITL 이다. M1 원칙 「근거 없으면 말하지 않는다」가 4회차에서 처음으로 **틀린 말을 막는 것과 맞는 말을 하는 것을 동시에** 해냈다.

### 소리가 나니 길이가 보였다

CVL 1 의 36초에 이어 34초·25초·23초. 화면 세 줄이 소리 30초다. 문장 수는 길이의 단위가 아니었다. 이 숫자는 재생기가 생기기 전엔 존재하지 않았다 — **부품 하나가 새 지표를 만든다.**

## Tomorrow's focus — Live #28 (9/20 일 05:00)

1. 04:30 절차 6단계 (Rundown 「방송 시작 전」) — 재생기 창이 하나 더 생겼다
2. OBS 3설정 확인 (모니터링 Enabled · Buds · Desktop Audio=Realtek). 주간 영상을 틀 거면 Desktop Audio 되돌림
3. 2부 CoMC 구간에서만 LIVE. 그 밖 REVIEW. 패닉 = Ctrl+Alt+Space
4. 방송 후 `rehearsal-log-4` 아래에 「Live #28 실전」 한 줄 + `output/debug/live28/` — 이것이 A·B 의 첫 실전
5. `completion_confusion` 이 또 나오면 ③ 규칙 좁히기 (사고 13 확정)

## 참조 및 산출물

**신규**: `10-…/examples/rehearsal4_driver.py` · `output/debug/rehearsal4/` (driver_log · session_trace · spoken_log · daemon_latency)
**수정**: `rehearsal-log-4.md`(OBS 실측 · 결과 · 판정) · `go-nogo-decision.md`(최종 판정) · `incident-classification.md`(4회차 · 사고 13 후보) · `05_verify_and_gate.py`(글자 수 컷) · `safety_policy.json` 원본+사본 · `engine_daemon.py`(반환값) · Live28 Rundown 「방송 시작 전」
**OBS (사용자)**: Audio Input Capture 모니터링 Enabled · 모니터링 장치 Galaxy Buds2 Pro · Desktop Audio Speaker(Realtek)
**모드**: REVIEW 로 복귀 · 백그라운드 프로세스 0
**비용**: LLM 7회 (gpt-5 minimal)
