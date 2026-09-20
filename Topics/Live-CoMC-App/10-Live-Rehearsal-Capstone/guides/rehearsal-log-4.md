---
title: "리허설 4회차 — 무관중 · 사고 8~11 수정본 · 처음으로 소리 포함 (CVL 2)"
created: 2026-09-17 16:10:00
tags:
  - live-comc-app
  - cvl
  - rehearsal
---

## 왜 4회차인가

3회차(Live #27 실전)는 사고 4건이었다. 판정 규칙 「사고 있음 → 원인 기록 + 재리허설」 그대로, **사용자 결정(9/17): 무관중 4회차 뒤 A 판정 확정.** CVL 1(9/17)에서 사고 7~11 을 고쳤고(`test_live27_incidents.py` 0/10 → 10/10) `spoken_player.py` 로 소리 경로가 생겼다. 4회차는 그 둘을 **한 번에, 실제 방송 구성(OBS `Untitled` 프로필)에서** 돌린다.

**판정은 둘로 나눈다** — go-nogo 의 A(화면)와 B(소리)는 부품이 다르다.
- **A**: 사고 0건이면 Live #28(9/20)부터 REVIEW 상시 투입 확정
- **B**: 소리가 송출 믹스에 실리고, 진행자 헤드폰에서 들리고, 소스 뮤트로 AI 만 끊기면 LIVE 모드 사용 가능. A 가 실패해도 B 는 별도로 판정한다

## OBS — 파일에서 확인한 것 (9/17, OBS 꺼진 상태)

| 항목 | 현재 (Untitled = 방송 프로필/씬) | 판정 |
|---|---|---|
| 출력 모드 | Simple — 스트림은 모든 오디오 소스의 단일 믹스 | ✅ AI 음성이 송출에 실린다 (트랙 배정 불필요) |
| Mic/Aux | MOTIV Mix Virtual Output (진행자 마이크) | ✅ |
| Desktop Audio | Windows 기본 재생 장치 = Speaker (Realtek) | ✅ CABLE 과 무관 → 이중 포착 없음 (8/31 실측과 같은 구조) |
| **AI 음성** | 소스 「Audio Input Capture」 = `CABLE Output` · 전 트랙 · 뮤트 아님 | ✅ 8/31 에 넣은 것. 880Hz 테스트로 **소스 뮤트 = AI 만 차단** 이미 확인 |
| AI 음성 모니터링 | `monitoring_type = 0` (끔) · 프로필 모니터링 장치 = Default | ⚠️ **진행자가 AI 목소리를 못 듣는다** — 4회차 전에 바꾼다 |
| 오버레이 | Browser Source 「Co-MC 오버레이」 `http://127.0.0.1:8777/` (씬에 2개 항목) | ✅ · 중복 항목은 하나 숨겨도 됨 |

### ✅ 9/17 저녁 — OBS 에서 실제로 바꾼 것 (사용자 · OBS 32.2.2)

실측으로 전제가 하나 바뀌었다: **진행자는 MV7 헤드폰이 아니라 Galaxy Buds2 Pro(블루투스)로 듣고, 그것이 Windows 기본 재생 장치**다. 그래서 「모니터링 = 기본 장치」로 두면 Desktop Audio 가 모니터 소리를 되잡아 AI 목소리가 두 번 송출된다. 선택은 A안:

| 설정 | 값 |
|---|---|
| Advanced Audio Properties → Audio Input Capture → Audio Monitoring | **Monitoring Enabled** (OBS 32 에서 "Monitor and Output" 의 새 이름) |
| Settings → Audio → Desktop Audio | **Speaker (Realtek(R) Audio)** — 사실상 끔. ⚠️ 컴퓨터 소리(유튜브 재생 등)는 송출되지 않는다. 영상을 트는 회차엔 그때만 Galaxy Buds2 Pro 로 되돌린다 |
| Settings → Audio → Advanced → Monitoring Device | **Headphones (Galaxy Buds2 Pro)** |
| Mic/Auxiliary Audio | MOTIV Mix Virtual Output (변경 없음) |

검증: `spoken_player.py --device "CABLE Input" --text …` 14.5초 → **Buds 에서 들림 ✅ · 믹서 「Audio Input Capture」만 움직임 ✅** (사용자 확인). 유튜브를 Buds 로 틀었을 때 OBS 미터 무반응 = Desktop Audio 분리 확인.

### (참고) 원래 계획했던 절차

1. 오디오 믹서 → 「Audio Input Capture」 톱니 → **오디오 모니터링 → 모니터링 및 출력(Monitor and Output)**. 이름도 「AI 음성 (CABLE Output)」으로 바꿔 두면 방송 중에 헷갈리지 않는다
2. 설정 → 오디오 → 고급 → **모니터링 장치 = Headphones (Shure MV7)**. ⚠️ Default(=Realtek 스피커)로 두면 Desktop Audio 가 모니터 소리를 다시 잡아 **AI 목소리가 두 번 송출**된다

확인: `spoken_player.py --device "CABLE Input" --text "모니터 테스트"` → 헤드폰에서 들리고, OBS 믹서에서 「Audio Input Capture」 미터만 움직이고 Desktop Audio 는 조용해야 한다.

## 절차 — 방송 없는 날, 30분

```
# 0. 인코딩 (PowerShell)
$env:PYTHONUTF8 = "1"

# 1. Rundown = Live28 (2부 커버리지 2건 확정 · 1부·주간 영상 미정) — 그대로 쓴다

# 2. 파싱·컨텍스트   (07-CoMC-Engine-POC/src)
python 01_parse_rundown.py --live 28
python 02_resolve_context.py --live 28 --part 2

# 3. 오버레이 서버   (09-…/examples/engine) — 창 1
python overlay_server.py

# 4. 재생기          — 창 2   ⭐ 처음 들어가는 창
python spoken_player.py --device "CABLE Input"
#    폴링 중 · 모드 표시 확인. 헤드폰에서 들으려면 OBS 모니터링(위) 이 켜져 있어야 한다

# 5. 엔진 대기       — 창 3
python engine_daemon.py --live 28 --serve
#    파트 전환은 이제 데몬이 감지한다 (사고 7 수정) — ② 를 손으로 돌리지 않는다

# 6. 프리플라이트    (10-…/examples)
python preflight_check.py --rundown "…/2026-09-13 - Live28 Weekly Rundown.md" --probe-live
#    FAIL 0 이 아니면 시작하지 않는다

# 7. 모드 — REVIEW 로 시작. 질문 1~3 을 화면으로 본 뒤 LIVE 로 올려 4~6 을 소리로.
python 06_render_output.py --live 28 --set-mode LIVE --reason "4회차 소리 구간"
```

### 질문 세트 (사고 8~11 을 하나씩 겨냥)

| # | 질문 | 겨냥 | 기대 |
|---|---|---|---|
| 1 | 오늘 2부에서 뭘 다루나요 | 사고 8 | 확정 항목 2개를 **확정으로** 말한다. "후보" 라는 말이 없다 |
| 2 | CoMC 앱은 어디까지 왔나요 | 사고 9 | 상태 어휘가 있는 한 문장 (완료·진행 중·확정…) |
| 3 | 주간 영상은 뭐예요 | 사고 10 | **침묵** + 화면이 비어 있다 (`cross_part`) |
| 4 | (핫키로 1부 → 2부 전환 뒤) 2부 첫 항목이 뭐죠 | 사고 7 | 데몬 로그에 `part_switch` · 1부 컨텍스트로 답하지 않는다 |
| 5 | 음 그러니까 저기 (무의미) | 사고 11 | `unknown` 거절 + **화면이 비어 있다** (옛 초안 없음) |
| 6 | (LIVE) 오늘 2부 첫 번째 실험은 뭔가요 | B | 헤드폰에서 들린다 · OBS 「Audio Input Capture」 미터 움직임 · 재생 길이 기록 |
| 7 | (LIVE, 재생 중 Ctrl+Alt+Space) | B 패닉 | 즉시 끊김 · mode=MUTE · `spoken_log` 에 `aborted: true` |
| 8 | (LIVE) 아무 질문 한 번 더 | 사고 4·길이 | 어미 붕괴 없음 · **발화 길이(초) 기록** — CVL 1 실측 3문장 36초 |

## 관찰 체크리스트

- [ ] 프리플라이트 FAIL 0
- [ ] 질문 1~5 화면 결과 — 사고 8·9·10·11·7 각각 재발 여부
- [ ] 질문 6 — 소리가 헤드폰·OBS 미터 둘 다에 나타나는가 (둘 중 하나만이면 라우팅 문제)
- [ ] 질문 7 — 패닉 스톱 → `spoken_log.jsonl` `aborted` · 오버레이 유지 여부
- [ ] 질문 8 — 재생 초 · 문장 수 · 글자 수 → 길이 상한 결정 재료
- [ ] OBS 녹화 켜 두기 → 녹화본에서 AI 목소리·진행자 목소리 둘 다 들리는지 (송출 믹스 최종 확인)
- [ ] 방송 후 `daemon_latency.json` · `session_trace.jsonl` · `spoken_log.jsonl` → `output/debug/rehearsal4/`

## 결과 — 리허설 후 채운다

| 항목 | 값 |
|---|---|
| 진행 시각 | 2026-09-17(목) 17:16~17:40 PDT — 무관중, OBS `Untitled` 프로필 켜 둠, 사용자가 Buds·믹서 관찰. 프리플라이트 PASS 7 · WARN 2 · FAIL 0. 드라이버 `examples/rehearsal4_driver.py` (핫키·패닉은 파일 조작으로 대신) |
| 발화 시도 / 통과 / 침묵 | **10 / 6 / 4** — 침묵 4는 전부 **의도된 침묵**: ③ 주간 영상(`cross_part`) · ④a 1부 미정(② 거절) · ⑤ 무의미 발화(`unknown`) · ⑦ `completion_confusion` 모호성(HITL). LLM 완주 6회 **4,026~7,329ms** |
| 사고 (A) | **0건.** 사고 8(확정을 후보로) · 9(상태 어휘) · 10(파트 오귀속) · 11(옛 초안 잔존) · 7(파트 전환) 모두 **재발 없음** — 질문 1~5 가 각각 기대 결과. 관찰 1건: 질문 7 「CoMC 앱은 무엇을 하나요」에 ③ 이 `completion_confusion` 을 달아 HITL 로 멈춤 — 정책대로지만 오탐일 수 있다(아래) |
| 소리 (B) — 송출 믹스 · 헤드폰 · 패닉 | ✅ **셋 다.** 질문 6·8·재실행: Buds 에서 들림(사용자) · OBS 믹서 「Audio Input Capture」만 움직이고 Desktop Audio·Mic/Aux 조용(사용자) · 재생 중 MUTE → **끊김**(질문 6 이 77% 에서 abort, `spoken_log` `aborted: true`, 사용자가 "중간에 뚝 끊겼다" 확인) |
| 발화 길이 (초 · 글자) | 271자 = 34.2s · 189자 = 25.3s · 180자 = 23.3s → **≈7.7자/초.** 문장 수 상한(5)만으로는 30초를 넘는다 → `safety_policy.length_hardcut.max_chars` 추가 (brief 90 · **default 120** · detailed 180), 문장 단위 뒤에서 자름. 재검증: 187자 → 119자 (2/3 문장) |
| A 판정 → Live #28 상시 투입 | ✅ **GO — 사고 0건.** Live #28(9/20)부터 REVIEW 모드 상시 투입 |
| B 판정 → LIVE 모드 사용 | ✅ **GO — 조건부.** ① 방송 전 `spoken_player.py --device "CABLE Input"` 기동 ② OBS 모니터링(Buds)·Desktop Audio(Realtek) 설정 유지 ③ 글자 수 상한 120 ④ 패닉 = 모드 전환(핫키 Ctrl+Alt+Space 또는 `--set-mode MUTE`) — 재생기가 22ms~ 안에 끊는다. **Live #28 에서 LIVE 는 2부 CoMC 구간에서만 켠다** (그 밖은 REVIEW) |

### 관찰 — `completion_confusion` 오탐 가능성 (사고 13 후보)

질문 「오늘 2부에서 CoMC 앱은 무엇을 하나요?」에 ③ 이 `completion_confusion`(완료된 항목을 진행 예정으로 묻는 것) 플래그를 달았고 정책(`block_generation`)대로 ④ 가 멈췄다. 근거 풀의 확정 항목 상태에 "9/17 Topic 완료" 가 있어서다. 그러나 이 항목은 **완료된 Topic 을 방송에서 실사용하는 것**이라 "무엇을 하나요" 는 정당한 질문이다. 유형은 **오탐**(말해도 되는 것을 못 말함). 방송에 틀린 말은 안 나가므로 A 판정에는 영향 없음. Live #28 에서 같은 일이 나면 ③ 규칙을 좁힌다 — 지금은 고치지 않는다(실물 1건).

### 그 밖에 알게 된 것

- **모드가 LIVE 를 벗어나면 어떤 이유든 재생이 끊긴다** — 패닉(MUTE)뿐 아니라 REVIEW 로 내려도. 재실행에서 드라이버가 끝나며 REVIEW 로 내려 85% 에서 끊겼다. 의도된 성질이지만, 방송 중 **REVIEW 로 내리는 것 = 말하던 것을 끊는 것**임을 진행자가 알아야 한다
- 데몬 `call()` 이 ④ 의 `return 2`(거절)를 성공으로 읽어 ⑤ 까지 흘러가 「⑤ 실패」로 기록됐다 — 기능 영향 없음, 표기만. 반환값을 보도록 고침
- 정책 파일은 `data/safety_policy.json` **사본**을 읽는다 — M3 원본만 고치면 적용되지 않고 drift 경고만 난다. 둘 다 고쳤다

## 참조

- [rehearsal-log-3.md](rehearsal-log-3.md) — 3회차 실전 · [incident-classification.md](incident-classification.md) — 사고 1~12 · [go-nogo-decision.md](go-nogo-decision.md)
- `../examples/test_live27_incidents.py` — 사고 7~11 재현 테스트 (LLM 0회)
- `../../06-TTS-Audio-Routing-Harness/guides/audio-routing-setup.md` — 8/31 소스 뮤트 실측
