---
title: "리허설 3회차 — Live #27 실전을 3회차로 (사전 점검 · 당일 절차 · 결과)"
created: 2026-09-12 23:40:00
tags:
  - live-comc-app
  - m10
  - rehearsal
---

## 결정 — 조건이 바뀌었다

로드맵 실습 4는 *"동일 조건으로 3회차 리허설 → 사고 0건이면 LIVE 투입 판단"* 이다. M10 WorkLog 는 이것을
*"사람이 마이크→호출어→STT→답변→오디오 출력 전 구간을 30분 돈다"* 로 올려 적었고,
[what-can-run-during-broadcast.md](what-can-run-during-broadcast.md) 는 그래서 *"3회차는 방송 중에 못 한다"* 고 결론냈다.

**2026-09-12 사용자 결정: 내일 Live #27(09-13 05:00 PST) 방송을 3회차로 삼는다.** 무관중이 아니라 실전이다.

이 결정이 성립하려면 두 가지를 먼저 인정해야 한다.

| 전제 | 사실 |
|---|---|
| 마이크 전 구간을 돌 수 있는가 | **아니다.** 호출어(M4)·STT(M5)·재생(M6)은 각자 프로브 스크립트로만 존재한다. 엔진(`engine_daemon.py`)은 `--text` 와 `--serve`(stdin) 만 받는다. 이어 붙이는 것은 개발이지 리허설이 아니다 |
| LIVE 모드로 소리가 나가는가 | **아니다 — 오늘 밤 확인.** `06_render_output.py` 는 LIVE 에서 `spoken.json` 을 쓰고 *"합성·재생은 M9 셸의 몫"* 이라 적어 두었는데, **`spoken.json` 을 읽어 재생하는 코드가 어디에도 없다.** M9 의 미완 항목(Electron 셸)이 바로 그 자리다 |

그러므로 내일 3회차는 **로드맵 원문 조건**(1·2회차와 동일: 텍스트 입력 → 파이프라인 → 게이트 → 화면)으로 진행하되,
**입력을 진행자가 실시간으로 넣고, 출력을 OBS 오버레이로 시청자가 본다**는 점이 1·2회차와 다르다.
모드는 **REVIEW** 다. 소리가 나갈 부품이 없으므로 LIVE 로 올려도 달라지는 것은 파일 이름뿐이다.

> 이렇게 하면 실습 4의 「동일 조건」은 충족하고, 「마이크 전 구간」은 후속 과제로 넘어간다. 그것을 이 문서와
> [go-nogo-decision.md](go-nogo-decision.md) 에 그대로 적는다. **판정을 올리려고 조건을 낮춘 것이 아니라, 조건이 애초에 로드맵보다 높게 적혀 있었다.**

## 사전 점검 (09-12 23:33, 방송 전날 밤)

### 프리플라이트 9항목 — Live27 Rundown 기준

`python preflight_check.py --rundown "AI/Roundup/2026-09-06 - Live27 Weekly Rundown.md" --date 2026-09-13`

| # | 항목 | 결과 | 의미 |
|---|---|---|---|
| 1 | STT·LLM·TTS probe | ⬜ 키 존재만 | `--probe-live` 안 씀 (비용). 내일 아침 1회 |
| 2 | 오디오 장치 | ✅ 입력 30 · 출력 36 · WASAPI 6 | |
| 3 | Rundown 최종본·파싱 | ✅ 파트 3 · 이상 0 | `is_final=True` |
| 4 | 커버리지 미정 파트 | ⚠️ 주간 영상 1/3 | 의도된 상태 — 그 파트에서 앱은 침묵한다(M1) |
| 5 | part_timeline | ⚠️ 샘플 사용 | Rundown 의 파트 시간이 전부 「미정」이라 만들 값이 없다. `suggested_part_id` 에만 영향, 권위값 아님 |
| 6 | 컨텍스트 사전 빌드 | ❌ 09-06 것 | **예상된 FAIL** — 날짜 검사라 오늘 밤 빌드해도 내일 아침엔 다시 FAIL. 아침 루틴에 넣는다 |
| 7 | 오버레이 서버 | ❌ 응답 없음 | 서버를 안 띄웠으니 당연. 아침 루틴 |
| 8 | 패닉 스톱 | ✅ open→abort | |
| 9 | 운영 모드 | ✅ REVIEW | 09-06 이후 그대로. 내일도 REVIEW |

**FAIL 2건은 둘 다 「아직 안 켰다」이고, WARN 2건은 둘 다 Rundown 의 실제 상태다.** 코드 결함은 없다.

### 파이프라인 — 처음으로 Live27 을 먹였다

| 단계 | 명령 | 결과 |
|---|---|---|
| ① 파싱 | `01_parse_rundown.py --live 27` | 파트 3개 · 커버리지 항목 4개 · 금칙 0 · 조건부 0 |
| ② 컨텍스트 | `02_resolve_context.py --live 27 --part 2` | `broadcast_context.27.json`. 근거 6건 중 **5건 `missing_section`** (Weekly Progress · Claude Code 주간 · Live26 Rundown · Task Board), 캔버스 1건 skip. Rundown 만 `final` |
| ③~⑥ 발화 1건 | `engine_daemon.py --live 27 --repeats 1 --text "오늘 2부에서 CoMC 앱은 어디까지 왔나요?"` | 게이트 **pass** · 4/4 문장 유지 · 위반 0 · REVIEW 라 `spoken_pending.json` 으로 보류 |

답변 원문:

> 오늘은 AI로 라이브 방송 보조 MC 앱 만들기 마무리까지 진행 상황을 정리해 드리겠습니다. 그리고 이어서 Claude Artifacts & Routines 배우기를 준비해 두었습니다. 또한 AI로 Seattle AI Week 참가 준비하기도 함께 안내드릴 예정입니다. 나머지 실험 항목들은 후보로, 주중 진행에 따라 승격될 수 있습니다.

지연 **6,210ms** (④ LLM 6,191). 1회 표본이라 결론은 안 내지만 2회차 2,998ms(Live26) · M9 4,369ms(Live21) 보다 느리다.
`⚠️ 캐시 미작동` 표시는 `--repeats 1` 이라 두 번째 호출이 없어서 나온 것이고 결함이 아니다.

### 오늘 밤 발견 3건

1. **`spoken.json` 소비자 부재** — 위 「결정」표 참조. M10 09-06 인사이트 *"아홉 모듈이 한 번도 같이 돌아본 적이 없었다"* 와 같은 종류다. 이번엔 출력 끝단이었다. 사고 유형: **구조**(연결 없음) → [incident-classification.md](incident-classification.md) 에 6번으로 추가.
2. **근거 5/6 `missing_section`** — 2부 컨텍스트가 사실상 Rundown 한 장으로만 만들어졌다. 게이트는 통과했지만(Rundown 인용만으로 답이 됐다), 질문이 「지난주 뭐 했나」쪽으로 가면 근거가 얇다. 원인은 이번 주 문서들의 섹션 이름이 컨텍스트 해석기가 찾는 이름과 다른 것으로 보인다 — **방송 후 확인**. 방송 전에 고칠 일은 아니다.
3. **파트 전환이 컨텍스트를 갱신하지 않는다** — `--serve` 는 ①②(파싱·컨텍스트)를 기동 시 한 번만 한다. 핫키로 `current_part_id` 를 바꿔도 ④ 가 읽는 `broadcast_context.27.json` 은 옛 파트 것이다. 내일은 파트마다 다른 창에서 ② 를 다시 돌리는 것으로 운영한다. 사고 유형: **구조** → 7번.

부수: `engine_daemon.py` 를 콘솔이 아닌 파이프로 실행하면 `cp1252` 인코딩 오류로 죽는다. `PYTHONUTF8=1` 로 우회. 사용자 터미널에서는 안 나던 것이라 내일 영향 없음. 8/30 `prompt.txt` 는 오늘도 `output/` 에 남아 있다(사고 5) — 어떤 코드도 더 이상 쓰지 않는 파일이니 아침에 `output/debug/` 로 옮긴다.

## 당일 절차 — 04:30 PST 부터 (30분 전)

전부 [what-can-run-during-broadcast.md](what-can-run-during-broadcast.md) 의 ✅ 열이다. 소리를 내는 단계가 없다.

```
# 0. 인코딩 (PowerShell)
$env:PYTHONUTF8 = "1"

# 1. Rundown 최종 — 주간 영상 커버리지 확정 또는 「이번 주 없음」 (사람)
#    바꿨으면 ①② 를 다시 돈다. 안 바꿨어도 ② 는 오늘 날짜로 다시 만든다 (프리플라이트 6번)

# 2. 파싱·컨텍스트   (07-CoMC-Engine-POC/src)
python 01_parse_rundown.py --live 27
python 02_resolve_context.py --live 27 --part 1        # 1부로 시작한다

# 3. 오버레이 서버   (09-Desktop-Shell-and-Overlay/examples/engine)  — 창 하나
python overlay_server.py
#    OBS Browser Source → http://127.0.0.1:8777/state   (CoMC-Test 프로필이 아니라 방송 프로필에 있는지 확인)

# 4. 엔진 대기       — 창 둘
python engine_daemon.py --live 27 --serve
#    한 줄 = 발화 하나. ⚠️ 파트 바꿀 때는 **다른 창에서 ② 를 다시 돈다**:
#      python 02_resolve_context.py --live 27 --part 2
#    데몬은 ①② 를 기동 때 한 번만 하고, ④ 는 broadcast_context.27.json 을 매 발화마다 파일에서 읽는다.
#    핫키(Ctrl+Alt+N)는 권위값만 바꾸고 컨텍스트는 다시 만들지 않는다 — 발견 3

# 5. 프리플라이트    (10-Live-Rehearsal-Capstone/examples)
python preflight_check.py --rundown "…/2026-09-06 - Live27 Weekly Rundown.md" --probe-live
#    기대: 6·7 이 ✅ 로 바뀌고, 1 이 ✅. 4·5 는 WARN 그대로. FAIL 이 하나라도 있으면 그 상태로 시작하지 않는다.

# 6. 모드 확인 — REVIEW (mode.json). LIVE 로 올리지 않는다 (올려도 소리 부품이 없다)
```

방송 중 **2부 ①「CoMC 앱 마무리」** 구간에서 진행자가 실제 질문을 3~5개 넣는다. 최소 세트:

| # | 질문 (예) | 보는 것 |
|---|---|---|
| 1 | 오늘 1부에서 뭘 다루나요 | 정상 경로 — 인용이 커버리지 ① 인가 |
| 2 | 지난주 Live26 에서 안 한 게 뭐죠 | 근거 얇은 질문 — 부재 주장을 하는가, 침묵하는가 |
| 3 | 주간 영상은 뭐예요 | 미정 파트 — **침묵해야 한다** (2회차 경로 1) |
| 4 | (파트를 2부로 바꾸고) CoMC 앱은 어디까지 왔나요 | 파트 전환 후 컨텍스트 |
| 5 | 아무 질문이나 한 번 더 | 어미 붕괴(사고 4) 재발 여부 |

## 관찰 체크리스트 — 진행자 또는 방송 후 기록에서

| 항목 | 확인 |
|---|---|
| 프리플라이트 최종 결과 (PASS/WARN/FAIL 수) | |
| 발화 시도 수 / 게이트 통과 수 / 침묵 수 | |
| 오버레이가 OBS 화면에 실제로 보였는가 (시청자 화면 기준) | |
| 가장 느린 발화 지연 (`daemon_latency.json`) | |
| 사고 (있으면 유형: 구조 · 오탐 · 내용 없는 발화 · 운영 위험) | |
| 진행자가 앱 때문에 진행을 멈춘 순간이 있었는가 | |
| 방송 중 손댄 코드·설정 (있으면 안 되지만, 있었다면) | |

## 결과 — 방송 후 채운다

_(09-13 방송 종료 후 기록. 비어 있으면 3회차는 아직 안 끝난 것이다.)_

| 항목 | 값 |
|---|---|
| 진행 시각 | 2026-09-13(일) 04:30 프리플라이트 → 05:00~08:00 PST Live #27 전 구간. 모드 **REVIEW** (진행자 타이핑 → 오버레이). 프리플라이트 PASS 7 · WARN 2 · FAIL 0 (LLM 실호출 4.8초) |
| 발화 시도 / 통과 / 침묵 | **9 / 6 / 3** — 트레이스: `03_classify_intent` 10회(answer_question 4 · summarize_part 4 · unknown 2), LLM 완주 8회 **4,400~7,260ms** (중앙값 ≈5,700ms). 파트 전환 3회는 `02_resolve_context.py` 재실행으로 우회(사고 7) |
| 사고 건수 | **4건** (사고 8~11, [incident-classification.md](incident-classification.md)) — ⑧ 1부 확정 커버리지를 「후보」표 문구와 혼동(3/3 재현) ⑨ 「CoMC 어디까지 왔나」에 항목만 읊고 답 없음 ⑩ 2부에서 주간 영상을 묻자 2부 항목을 "이번 주 영상"으로 오귀속 ⑪ 의도 `unknown` 거절 시 옛 초안이 재렌더. **방송 중 코드 수정 0 · 소리로 나간 오류 0** (전부 화면에서 멈춤) |
| 판정 | 판정 규칙 「사고 있음 → 원인 기록 + 재리허설 여부 결정」 → **원인 기록 완료(9/17) · 무관중 4회차 재리허설 뒤 A 확정** (사용자 결정 9/17). 4회차는 9/18~19, Live #28(9/20) 전. 진행자 소감(원문): *"기능상으로는 OK, 내용상으로는 사전 작업에서 보완해야 할 점들이 많이 있는 것 같다"* |

> 9/17 기록. 산출물: `07-CoMC-Engine-POC/output/debug/live27/` (`daemon_latency.json` · `session_trace.jsonl`). 상세 서사: [[Roundup/2026-09-13 - Daily Roundup#1. Live 27 — CoMC 앱 3회차 실전|Daily 9/13]]

## 판정 규칙

로드맵 실습 4 그대로: **사고 0건 → LIVE 투입 판단**(단, 여기서 LIVE 는 「REVIEW 모드로 방송에 상시 투입」을 뜻한다 — 이유는 go-nogo 문서),
**사고 있음 → 원인 기록 + 재리허설 여부 결정.** 음성 출력 경로는 어느 쪽이든 판정 대상 밖이다 — 부품이 없는 것은 사고가 아니라 범위다.

## 참조

- [rehearsal-log-1.md](rehearsal-log-1.md) · [rehearsal-log-2.md](rehearsal-log-2.md) — 1·2회차 (명령줄 단발 발화)
- [incident-classification.md](incident-classification.md) — 사고 유형 4종 + 7건
- [what-can-run-during-broadcast.md](what-can-run-during-broadcast.md) — 방송 중 허용 작업 판정표
- [go-nogo-decision.md](go-nogo-decision.md) — LIVE 투입 판단
- `AI/Roundup/2026-09-06 - Live27 Weekly Rundown.md` — 내일 Rundown
