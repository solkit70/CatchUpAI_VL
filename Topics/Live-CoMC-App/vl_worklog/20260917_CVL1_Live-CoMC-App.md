---
title: "CVL 1 — 사고 7~11 을 고치고, 처음으로 소리가 났다"
created: 2026-09-17 15:20:00
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
| 날짜 | 2026-09-17 (목) 10:45 ~ 15:20 — Topic 완료(M10c) 직후 이어서 |
| 실소요 | 약 1시간 40분 (사용자 대기 없음 · LLM 호출 2회 — 실전 검증 1 · 수정 전 대조 중 1) |
| 성격 | **CVL 유지보수 1** — Topic 은 완료, 로드맵 밖 작업. "변한 것"은 외부 레포가 아니라 **실전 방송이 되돌려 준 요구사항** |
| 범위 | 사고 7·8·9·10·11 코드 수정(수정 전/후 대조) → `spoken_player.py` → end-to-end 소리 → 문서·스킬 |
| 결과 | 재현 테스트 **0/10 → 10/10** · M8 게이트 9/9 · 18회차 파싱 회귀 이상 0 · **헤드폰·루프백·abort·⑥→재생 전부 확인** |

사용자: *"지금 시간이 있으니까요 지금 CVL 세션을 시작해 주세요."* + CVL 의 뜻 질문 → Continuous Vibe Learning. 이 볼트에서는 Retrospective 로 닫힌 Topic 에 붙는 유지보수 세션.

## 한 것

### 1. 수정 전 상태를 먼저 재현했다

Live28 Rundown 을 ① → ② 로 먹이니 2부 근거 풀이 **4건: 「후보」·「지난 회차의 교훈」·불릿 2** — 확정 항목 2개와 그 상태는 하나도 없었다. 사고 8·9 가 왜 났는지 코드를 읽기 전에 파일이 말해 줬다.

### 2. 코드 수정 — 5건, 파일 계약은 유지

| 사고 | 어디 | 무엇 |
|---|---|---|
| 8 확정/후보 | ② `part_body_quotes` · `build` | 근거 풀 첫 줄에 `[확정] 이번 방송 커버리지 — {항목}` · 커버리지 항목과 같은 표 행을 `[확정 항목 현재 상태] 이름 — 상태` 로 인용 · `### 후보` 소절은 제목·불릿 모두 제외. ④ 프롬프트에 「[확정]은 확정, 후보는 확정 아님」 |
| 9 상태 질문 | ④ `is_status_question` · ⑤ 규칙 7-b | 상태 키워드(`어디까지·상태·진행·현황·됐나…`) → ④ 는 상태 값을 한 문장으로 말하라 지시, ⑤ 는 남은 문장에 상태 어휘가 없으면 `content_empty` |
| 10 다른 파트 | ② `other_parts`(이름만) · ④ `other_part_mentioned` · ⑤ 규칙 9 | `N부` 번호 불일치 또는 다른 파트 제목 어휘 전부 포함 → ④ 는 LLM 전 거절, ⑤ 는 전부 `cross_part` 드롭. **판정 함수는 하나** — ⑤ 가 ④ 의 함수를 import 한다 |
| 11 옛 초안 | `common.clear_overlay` · ④ `refuse` · ⑥ `nothing_to_say` | 거절·침묵이면 `overlay.json` 을 `text=""` 로 갱신 (서버는 빈 text 면 화면을 숨긴다). "파일을 안 쓴다"는 규칙이 옛 화면을 남기고 있었다 |
| 7 파트 전환 | 데몬 `utter()` | 발화 전에 `session_state.current_part_id` 를 읽어 `context_part` 와 다르면 ② 재실행. 대상 파트가 undefined 면 ② 가 (옳게) 거절 → 침묵 |

스키마 2건: `broadcast_context.other_parts` 추가(enum 은 `rundown_index` 의 3분류 `defined·directive·undefined` 와 맞춤 — 처음에 `conditional` 로 잘못 넣어 Live21·23 이 계약 위반으로 죽었다) · `verdict.dropped_sentences.reason` 에 `cross_part` **와 `style_broken`** — 후자는 09-06 규칙 8 을 넣을 때 빠진 **잠복 결함**이었다(사고 12).

### 3. 대조 — 고치기 전에 실패하고 후에 통과하는가

`10-Live-Rehearsal-Capstone/examples/test_live27_incidents.py` (LLM 0회, 결정적):

| | 수정 전 (`git stash`) | 수정 후 |
|---|---|---|
| 재현 테스트 10항목 | **0/10** | **10/10** |
| M8 `test_gate_rules.py` | — | 9/9 |
| 볼트 Rundown 18회차 ① 파싱 | — | 파트·항목 수 M8 기록과 전부 일치 · 이상 0 · ② 도 전 회차 생성 |

실전 1회(LLM): "오늘 2부에서 CoMC 앱은 어디까지 왔나요?" → *"…완성본 음성 출력 실사용으로 진행하고요, 이번 방송 확정 항목입니다. 현재 상태는 9/17에 Topic을 완료했고…"* — 게이트 3/3 통과. **사고 8·9 가 실물에서 사라졌다.**

### 4. `spoken_player.py` — 6주 비어 있던 자리

`09-Desktop-Shell-and-Overlay/examples/engine/spoken_player.py` (230줄). 폴링 → `mode.json` 재확인 → M6 `tts_providers.build`(edge, 레지스트리 그대로) → `sounddevice` 재생 → 소비(삭제) → `spoken_log.jsonl`. 재생 중 모드가 LIVE 를 벗어나면 **abort**. 실패는 전부 침묵 쪽.

| 검증 | 결과 |
|---|---|
| 헤드폰(Shure MV7) `--text` | ✅ 합성 2,428ms · 오디오 7.7s 재생 |
| VB-CABLE 루프백 (CABLE Input 재생 · CABLE Output 캡처) | ✅ 1,449 블록 중 **696 블록 소리 감지** · peak 0.63 — 소리가 실제로 흘렀다 |
| 재생 중 `mode.json` → MUTE | ✅ 전환 뒤 **22ms** 에 abort, 진행률 30% 에서 멈춤 |
| ⑥ LIVE → `spoken.json` → 재생기 `--once` | ✅ 소비 후 파일 삭제 · 로그 1건. 합성 2,766ms · **재생 36초** |

**첫 시도의 abort 테스트가 "실패"한 이유** — 모드를 1.2초 뒤에 내렸는데 합성이 1.5초 걸려서, 재생이 시작되기 전에 이미 MUTE 였다(29ms 에 abort). 계측기가 틀린 것이지 재생기가 틀린 게 아니었다. 4초로 다시 재서 확인.

### 5. 문서 · 스킬

- `verification-rules.md` 규칙 7-b · 9 절 · `incident-classification.md` 수정 목록 ✅ 6/6 + 「CVL 1 에서 새로 본 것」 · `go-nogo-decision.md` 후속표 1번 ✅ · M9 README
- **`rundown-writer` 스킬** — 「CoMC 앱이 읽는 방식에 맞추기」 표(확정 vs 후보 · 현재 상태 열 · 파트 소속) + 체크리스트 1줄. 진행자 소감 "사전 작업에서 보완"이 여기로 갔다

## 안 한 것 — 내일

- **OBS 방송 프로필 송출 트랙** — `CABLE Input` 이 OBS 오디오 소스로 들어가고 개별 뮤트되는지. OBS 화면이 필요해 사용자와 함께
- **무관중 4회차** — 사고 수정본 + 소리. `rehearsal-log-4.md` → A 확정 → Live #28 투입 여부
- 발화 길이 상한(글자 수) — 36초 실측을 보고 4회차에서 정한다

## Insights (인사이트)

### 사고의 뿌리는 근거 풀이 「무엇을 안 보여 주는가」였다

코드 다섯 군데를 고쳤지만, 가장 큰 변화는 ② 한 줄 — 확정 커버리지를 근거로 넣은 것이다. M1 원칙 「근거에 없으면 말하지 않는다」가 정확히 지켜졌기 때문에, 근거 풀에 확정이 없으면 앱은 확정을 말할 수 없었다. **안전장치가 완벽할수록 입력이 곧 출력이다.** 진행자 소감 "사전 작업에서 보완"은 이 구조를 정확히 짚었고, 그래서 수정의 절반은 Rundown 작성 규칙(rundown-writer 스킬)으로 갔다.

### 판정 함수는 하나여야 한다

사고 9·10 검사를 ④(생성 전 거절)와 ⑤(게이트)에 둘 다 넣었다. ⑤ 가 ④ 의 함수를 import 하게 한 것은 게으름이 아니라 M8 회고 — *"같은 대상에 대한 정의가 두 층에서 다르다"* 가 사고 3 의 원인이었다. 두 벌이면 반드시 어긋난다.

### 계측기를 먼저 의심한다

abort 테스트 첫 결과(29ms·진행률 0.3%)는 "즉시 끊긴다"로 읽을 수도 있었다. 합성 시간을 생각하면 재생 전에 이미 끊긴 것이었다. M4b 의 *"무음인데 peak 92%"* 와 같은 종류 — **너무 좋은 결과는 계측 오류를 먼저 본다.**

### 36초

세 문장이 소리로 36초다. 화면에서는 세 줄이라 짧아 보였다. **소리가 나기 전까지 길이는 보이지 않는다** — B 갈래를 미룬 6주 동안 이 숫자를 몰랐다.

## Tomorrow's focus — CVL 2 (09-18~19)

1. OBS 방송 프로필: `CABLE Input` → 오디오 소스 · 송출 트랙 포함 · 개별 뮤트 (사용자와 화면 보며)
2. 무관중 4회차 30분 — Live28 Rundown · REVIEW 로 시작해 LIVE 로 올려 소리까지 · 사고 0 목표 · 발화 길이 실측
3. `rehearsal-log-4.md` → go-nogo A 확정 · Live28 Rundown 「방송 시작 전」 체크 갱신 (재생기 기동 절차 추가)
4. 길이 상한 결정 → `safety_policy.length_hardcut` 에 글자 수

## 참조 및 산출물

**신규**: `09-…/examples/engine/spoken_player.py` · `10-…/examples/test_live27_incidents.py` · `output/spoken_log.jsonl` · `output/debug/audio/spoken_*.mp3`
**수정**: `07-…/src/{common,02,04,05,06}.py` · `09-…/engine/engine_daemon.py` · `03-…/schemas/{broadcast_context,verdict}.schema.json` · `verification-rules.md` · `incident-classification.md` · `go-nogo-decision.md` · M9 README · `_Settings_/Skills/rundown-writer/SKILL.md`
**모드**: 세션 끝에 `mode.json` = REVIEW 로 되돌림
**비용**: LLM 2회 (gpt-5 minimal)
