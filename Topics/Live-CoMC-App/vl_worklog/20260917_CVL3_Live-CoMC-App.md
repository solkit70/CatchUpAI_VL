---
title: "CVL 3 — 창 4개를 브라우저 탭 하나로"
created: 2026-09-17 20:20:00
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
| 날짜 | 2026-09-17 (목) 18:30~20:20 |
| 실소요 | 약 1시간 50분 (사용자 실사용 연습 40분 · 콘솔 구현·검증 70분 · LLM 호출 6회) |
| 성격 | CVL 유지보수 3 — 진행자 UX. 사용자 요청 「창 4개는 복잡하다, 가장 간단하게 하나의 UI 로」 |
| 결과 | **`comc_console.py` — 프로세스 하나 + 브라우저 탭 하나** (`http://127.0.0.1:8778/`). 승인 재생 · LIVE 재생 · 패닉 abort · 파트 · 프리플라이트 전부 탭에서 동작 확인. 사고 17 (WASAPI 콜백은 COM 스레드) 수정 |

## 한 것

### 1. 사용자가 직접 켜 보자 막힌 자리 (CVL 2 판, 창 4개)

`start_comc.ps1` 을 사용자가 처음 돌렸다. BOM 없는 .ps1 파싱 오류 → BOM 저장. 창 4개가 뜬 뒤 「여기서 어떻게 해야 하나요?」 — 어느 창에 질문을 치는지, 핫키가 살아 있는지, 결과가 어디 뜨는지가 화면에 없었다. 그 상태로 사고 14(드라이버가 남긴 스키마 밖 필드로 핫키 종료) · 15(OBS 소스 Refresh) · 16(「설명해 주세요」 unknown)이 나왔고, 마지막으로 패닉 뒤 Ctrl+Alt+R 을 눌러 REVIEW 가 되니 소리가 안 나는 것을 앱이 틀린 것으로 읽었다. 기능은 다 있었는데 **조작 면이 없어서** 있는 기능을 못 썼다.

### 2. `comc_console.py` — 합치되, 검증된 코드는 그대로

네 모듈(`overlay_server` · `spoken_player` · `hotkeys` · `engine_daemon.Engine`)을 프로세스 하나에 **스레드**로 넣고, 콘솔 HTTP(8778)를 더했다. 새 로직은 콘솔뿐이다. Electron 도 프레임워크도 없이 표준 라이브러리 `ThreadingHTTPServer` + 인라인 HTML/JS 300줄 — 1초 폴링 `GET /api/state` 로 모드 배지 · 파트 · 오버레이 미리보기 · 결과 목록 · 로그를 그리고, 버튼은 `POST /api/{ask,part,mode,panic,approve,preflight}`. 「대기 발화 승인 → 소리」 버튼은 REVIEW 에서 답이 대기 중일 때만 보인다. 파트 버튼은 Rundown 의 파트 제목·커버리지 상태(확정/지시/미정)를 같이 보여 준다.

### 3. 합치니 나온 사고 — 17 · 그리고 stdout

| 문제 | 실측 | 수정 |
|---|---|---|
| 승인 발화가 `PortAudioError: Error starting stream: Unanticipated host error (WdmSyncIoctl … GLE=0x490)` 로 침묵 | 단독 프로세스(main 스레드)에서는 정상. 새 스레드에서 블로킹 write 는 되고 **콜백 스트림만** 죽음. 스레드에서 `CoInitializeEx` 를 부르면 됨 | `spoken_player._com_init()` — 스레드마다 한 번 COM 초기화. 사고 17 |
| 재생기 로그에 `player  hotkey part_set 1` 같은 남의 줄이 섞임 | `contextlib.redirect_stdout` 은 sys.stdout 을 **프로세스 전체**에서 바꾼다. 재생기가 합성하는 3초 동안 다른 스레드의 print 가 재생기 버퍼로 갔다 | 스레드별 stdout 라우터 `_Router` — sys.stdout 을 한 번만 바꾸고 스레드마다 자기 버퍼를 켠다 |

수정 후 콘솔에서 끝까지: REVIEW 질문 → 승인 → 10.7초 완주 재생 · LIVE 질문 → 재생 3.9초 시점 패닉 → `⛔ 중단 mode=MUTE` · 파트 1↔2 · REVIEW 복귀 · 프리플라이트 PASS 7 WARN 2. 화면은 headless Edge 스크린샷으로 확인.

### 4. 문서·런처

`start_comc.ps1` 은 파싱·1부 컨텍스트·REVIEW 뒤 콘솔을 띄우는 것으로 바뀌었다 (창 4개 판 폐기). [operator-guide](../10-Live-Rehearsal-Capstone/guides/operator-guide.md) 를 콘솔 기준으로 다시 썼고, 「왜 창 하나로 바꿨나」와 「패닉 뒤엔 REVIEW 가 아니라 LIVE」를 넣었다. M9·M10 README · Live28 Rundown 「방송 시작 전」 · incident-classification 사고 17.

## Insights (인사이트)

### 기능이 있는 것과 쓸 수 있는 것은 다르다

CVL 2 까지 만든 것은 전부 동작했다. 4회차 사고 0. 그런데 사용자가 앉자 첫 질문이 「여기서 어떻게 해야 하나요?」였다. 드라이버가 돌린 리허설은 조작 면을 시험하지 않는다 — 드라이버는 어느 창에 칠지 헷갈리지 않는다. **사람이 앉아야 나오는 사고 종류가 있고**(14·15·16, 그리고 R/L 혼동), 그것은 코드 테스트로는 영원히 안 나온다.

### 합치면 합친 만큼 새 사고가 생긴다

창 4개 = 프로세스 4개일 때는 COM 도 stdout 도 각자 것이었다. 하나로 합치자 둘 다 공유 자원이 됐고, 그날로 사고 17 과 로그 섞임이 나왔다. 단순화는 공짜가 아니다 — 대신 **사고가 나는 자리가 한 곳**이라 잡기도 한 곳에서 잡는다.

### 「가장 간단하게」의 답은 브라우저였다

Windows 앱(tkinter/Electron)이 아니라 로컬 HTTP + HTML 이 가장 짧았다. 이유는 이미 오버레이가 HTTP 였고(OBS Browser Source), 상태가 전부 파일이라 폴링 한 줄로 화면이 되기 때문이다. M9 에서 Electron 셸을 미룬 결정이 여기서 이자를 냈다.

## Tomorrow's focus — Live #28 (9/20 일 05:00)

1. 04:30 `start_comc.ps1 -Live 28` → 탭에서 「지금 점검」 FAIL 0 → 그다음 OBS (순서!)
2. 2부 CoMC 구간에서만 LIVE 버튼. 패닉 뒤 다시 소리는 **LIVE**
3. 사용자 재테스트 (「테스트는 다음에」) — 콘솔 탭으로 질문 1건 · 승인 1건 · 패닉 1건이면 충분
4. 방송 후 `rehearsal-log-4` 아래 「Live #28 실전」 + `output/debug/live28/`
5. 콘솔 「결과」는 프로세스와 함께 사라진다 — 남길 게 있으면 끄기 전에 (다음 CVL 후보: 결과를 `output/debug/` 에 자동 저장)

## 참조 및 산출물

**신규**: [`09-…/examples/engine/comc_console.py`](../09-Desktop-Shell-and-Overlay/examples/engine/comc_console.py)
**수정**: `spoken_player.py`(`_com_init`) · `start_comc.ps1`(콘솔 런처) · `operator-guide.md`(전면) · `incident-classification.md`(사고 17) · M9·M10 README · Live28 Rundown · Topic README
**모드**: REVIEW · `spoken_pending.json` 없음 · 백그라운드 프로세스 0
**비용**: LLM 6회 (gpt-5 minimal)
