---
title: "M10 — 리허설 검증과 라이브 Demo (Capstone)"
created: 2026-09-06 00:00:00
tags:
  - live-comc-app
  - m10
  - capstone
---

**모듈**: M10 / **상태**: 진행 중 (실습 1·2·3 완료, 4·5 남음) / **예상 학습 시간**: 10h

## 요약

M1~M9 는 각자의 샘플 위에서 통과했다. M10 은 그것들을 **오늘 실제 방송 회차**에 처음 붙여 보는 자리다.
붙여 보니 **아홉 모듈이 한 번도 같이 돌아본 적이 없다는 사실**이 드러났다 — 엔진이 샘플 4회차에만 배선돼 있어
실제 회차로는 아예 기동하지 않았다.

그리고 안전 방어가 완성된 자리에서 반대편 실패가 나왔다.

> **게이트를 통과한 답이 질문에 답하지 않았다.**
> 틀린 말은 막았는데 맞는 말도 못 하고 있었다.

## 학습 순서

1. [guides/streaming-vs-safety-gate.md](guides/streaming-vs-safety-gate.md) — M9 가 남긴 선결 과제. 남은 4.5초를 스트리밍으로 줄일 것인가에 대한 결론(**채택 안 함**)과 그 근거
2. [examples/preflight_check.py](examples/preflight_check.py) — 방송 30분 전 9항목 자동 점검 (실습 1)
3. [guides/rehearsal-log-1.md](guides/rehearsal-log-1.md) — 1회차 기록. 정상 경로에서 나온 사고 6건과 지연 실측 (실습 2)
4. [guides/incident-classification.md](guides/incident-classification.md) — 사고 유형 분류와 모듈 매핑, 재현 테스트 (실습 3)
5. [guides/rehearsal-log-2.md](guides/rehearsal-log-2.md) — 2회차 기록. **막혀야 할 경로 3종**과 게이트 규칙 7·8 대조 검증
6. [examples/ending_style_probe.py](examples/ending_style_probe.py) — 문장 종결 붕괴 재현율 측정 (0/10) · 검사기 자체 검증 10/10
7. [guides/what-can-run-during-broadcast.md](guides/what-can-run-during-broadcast.md) — **방송 중 가능/불가 판정표** (기준: 오디오 출력을 건드리는가)
8. [guides/false-positive-measured.md](guides/false-positive-measured.md) — **M4 이월 과제 해소.** 3시간 실측에서 환산값이 뒤집혔다
9. [guides/rehearsal-log-3.md](guides/rehearsal-log-3.md) — **3회차 = Live #27 실전** (09-12 사용자 결정). 사전 점검 · 당일 절차 · 체크리스트 · 결과 칸 (실습 4)
10. [guides/go-nogo-decision.md](guides/go-nogo-decision.md) — **LIVE 투입 판단 3갈래**: A 화면 보조 조건부 GO · B 음성 출력 NO-GO · C 음성 입력 NO-GO
11. [../vl_worklog/20260912_Live-CoMC-App_Final_Retrospective.md](../vl_worklog/20260912_Live-CoMC-App_Final_Retrospective.md) — Topic Retrospective 초안 (실습 5)

## 핵심 결론

### 1. 스트리밍은 채택하지 않는다 — 필러가 더 빨리 소리를 낸다

M8 원칙("검증 전에는 한 글자도 내보내지 않는다")과의 충돌을 어떻게 풀지가 M9 의 숙제였다.
문장 단위 증분 게이트로 **원칙을 지키면서 스트리밍하는 설계는 성립한다**는 것을 확인했지만, 채택하지 않았다.

| 방식 | 첫 소리 |
|---|---:|
| **필러 (T_filler 1.14초)** | **≈1.20초** |
| 문장 단위 스트리밍 | ≈2.6~3.1초 |
| 파일 기반 (현재) | ≈5.03초 |

스트리밍이 당기는 것은 *끝나는 시각*이고, 체감 지연은 *시작하는 시각*의 문제다.
부수적으로 **M6 필러 설계의 `T_filler` 가 오측정(케이블 314ms) 위에 서 있던 것을 정정**했다 → 0.9초 → **1.14초**.

### 2. 프리플라이트는 실제로 사고를 막았다

첫 실행이 **FAIL 2 · WARN 4** 였고 전부 실물이었다. 특히 두 건이 이 스크립트를 만든 이유를 보여준다.

- **컨텍스트가 8/31 것이었다** — 파일은 있고 내용만 어제 것. *"있는가"* 가 아니라 *"오늘 것인가"* 를 물어서 잡혔다
- **모드가 `MUTE` 였다** — 8/31 핫키 테스트 상태 그대로. 이대로 방송했으면 앱이 한 마디도 못 하는데 **아무 오류도 안 난다**

설계 원칙은 **확인하지 못한 것을 통과로 세지 않는 것**이다. `SKIP` 을 `PASS` 와 분리하고 종료 코드도 나눈다.

### 3. 「내용 없는 발화」 — 이번 캡스톤의 진짜 수확

로드맵의 사고 4유형(근거 없는 발화/지연/오탐/장치 충돌)에 안 들어가는 실패였다.

```
질문   오늘 2부에서 진행할 실험이 뭐가 있나요?
답     …이번 주 실험 후보 전체 목록 중에서 선별된 항목들입니다.
게이트  통과 (모든 문장에 근거가 있다)
```

원인은 **두 층의 정의 불일치**였다. M8 게이트는 커버리지 화이트리스트를 *신뢰 출처*로 인정하는데,
M7 프롬프트는 *"위 근거만 사용해"* 라며 화이트리스트를 재료에서 뺐다.
질문의 답이 화이트리스트에만 있었으므로 모델은 시킨 대로 하고도 아무 말도 하지 못했다.

**수정은 두 겹이다.**

| 층 | 수정 | 성질 |
|---|---|---|
| M7 프롬프트 | 화이트리스트를 재료로 편입 + 내부 용어 누출 금지 | 확률적 — 3~7회 중 이름을 말한 비율이 흔들렸다 |
| **M8 게이트 (규칙 7 신설)** | **`content_empty` — '무엇을' 질문인데 항목을 하나도 안 말하면 자동 발화 차단** | **결정적** |

프롬프트만으로는 보장되지 않는다는 것을 실측으로 확인했기 때문에 게이트까지 갔다.
LLM 자기평가에 맡기지 않는다는 M8 원칙은 그대로 지켰다 — 규칙 기반 토큰 대조다.

## 산출물

```
10-Live-Rehearsal-Capstone/
├── README.md
├── examples/
│   └── preflight_check.py          9항목 자동 점검 (PASS/FAIL/WARN/SKIP)
└── guides/
    ├── streaming-vs-safety-gate.md 선결 과제 결론 + T_filler 정정
    ├── rehearsal-log-1.md          1회차 기록 · 사고 5건 · 지연 실측
    ├── rehearsal-log-2.md          2회차 · 막혀야 할 경로 3종 · 사고 0건
    ├── rehearsal-log-3.md          3회차 = Live #27 실전 · 사전 점검 · 당일 절차
    ├── incident-classification.md  유형 분류 6종 · 7건 매핑 · 재현 테스트
    ├── go-nogo-decision.md         LIVE 투입 판단 3갈래 · 후속 5단계
    ├── what-can-run-during-broadcast.md
    └── false-positive-measured.md  호출어 3시간 실측
```

**다른 모듈에 남긴 수정**

| 파일 | 내용 |
|---|---|
| `07-.../src/01_parse_rundown.py` | `resolve_live()` — 볼트의 실제 회차를 찾는다 · 번호 없는 H2 파트도 괄호 없이 인식 |
| `07-.../src/04_compose_answer.py` | 화이트리스트를 프롬프트 재료로 편입 · 내부 용어 누출 금지 |
| `07-.../src/05_verify_and_gate.py` | **규칙 7 `content_empty` 신설** |
| `09-.../engine_daemon.py` | `prewarm(part=...)` 하드코딩 제거 → 세션 권위값 사용 |
| `06-.../guides/wait-filler-design.md` | `T_filler` 정정(0.9 → 1.14초) · 예산표 갱신 · 「스트리밍 필요」 결론 뒤집힘 표기 |

## DoD

- [x] 프리플라이트 자동 점검 스크립트 완성 (9항목, FAIL 2건 실제 검출 → 수정 후 통과 확인)
- [x] 무관중 리허설 **2회** 완료 (실습 2) — 1회차 사고 6건 · **2회차 사고 0건**
- [x] 사고 유형 분류표 완성, 각 유형이 해당 모듈에 매핑됨 (실습 3)
- [x] 재현 테스트로 수정 확인 — 볼트 Rundown **16편 전수 파싱 이상 0건**, M8 게이트 테스트 **9/9 유지**
- [ ] 리허설 3회차 (실습 4) — **09-13 Live #27 실전으로 진행** (로드맵 원문 「동일 조건」. 「마이크 전 구간」은 존재하지 않는 경로였다 → [rehearsal-log-3](guides/rehearsal-log-3.md))
- [x] LIVE 투입 가능 여부 판단 문서화 — [go-nogo-decision.md](guides/go-nogo-decision.md) 3갈래. 3회차 후 A 확정
- [ ] Topic Retrospective (실습 5) — 초안 완료, 「실제 방송 투입 결과」절 대기

**완료율**: 5/7

## 리허설 2회차 — 막혀야 할 것이 막히는가 (사고 0건)

1회차는 정상 경로만 밟았다. 2회차는 반대를 봤다.

| 경로 | 결과 |
|---|---|
| 커버리지 미정 파트 질문 | ✅ ② 컨텍스트 단계 차단 — **LLM 근처도 안 간다** |
| 금칙 주제를 이름으로 지목 | ✅ ③ 에서 잡고 ④ 생성 거부 + 되물을 말 준비 |
| 지연 (`--repeats 5`) | 중앙값 **2,998ms** · 최선 **2,527ms** — M7 목표 2.5초 사정권 |

> 미정 파트 경로가 오늘 성립한 것은 우연이 아니다. 어제 Rundown 에서 주간 영상을
> *"이번 주 생략"* 으로 확정했기 때문에 `undefined` 파트가 실제로 생겼다.
> **M1~M9 동안 못 해본 검증을 실제 방송 편성이 만들어 줬다.**

지연은 M9(4,369ms)보다 낮지만 **회차가 달라 like-for-like 가 아니다** — 근거 풀 구성이 다르다.
그래서 "개선했다"고 적지 않는다.

→ [rehearsal-log-2.md](guides/rehearsal-log-2.md)

## 현재 판정 (09-12 갱신) — 화면 보조는 GO, 목소리는 부품이 없다

09-06 판정은 *"REVIEW 투입 가능 · LIVE 조건부"* 였고, 조건은 「사람이 마이크로 전 구간을 돈 적이 없다」였다.
09-12 방송 전날 사전 점검에서 **그 조건이 애초에 충족 불가능한 것**이었음이 드러났다.

| 발견 | 뜻 |
|---|---|
| `spoken.json` 을 읽어 재생하는 코드가 없다 (사고 6) | **LIVE 모드는 소리를 낼 부품이 없다.** REVIEW 와의 차이는 파일 이름뿐 |
| 마이크→호출어→STT→엔진 연결이 없다 | M4·M5 는 프로브 스크립트로만 존재. 「전 구간」은 리허설이 아니라 개발 |
| `--serve` 중 파트 전환이 컨텍스트를 안 만든다 (사고 7) | 파트마다 ② 재실행으로 우회 |

그래서 「LIVE 투입」을 세 갈래로 갈랐다 — [go-nogo-decision.md](guides/go-nogo-decision.md):

| 갈래 | 판정 |
|---|---|
| **A 화면 보조** (질문 입력 → 근거 있는 답 → OBS 오버레이) | **GO — 조건부.** 09-13 Live #27 을 3회차로 돌려 사고 0건이면 상시 투입 |
| **B 음성 출력** | **NO-GO** — 재생기 · 송출 트랙 검증 · 방송 없는 날 리허설, 셋 다 필요 |
| **C 음성 입력** | **NO-GO** — B 이후. 3시간 실측 오탐 1회(임계 여유 0.095) 재조정 먼저 |

> 안전 없는 음성보다 음성 없는 안전이 먼저다. M1~M10 이 만든 것은 A 이고, A 는 성립한다.

## 이전 / 다음

- 이전: [../09-Desktop-Shell-and-Overlay/README.md](../09-Desktop-Shell-and-Overlay/README.md)
- 다음: 09-13 Live #27 (3회차) → [rehearsal-log-3](guides/rehearsal-log-3.md) 결과 → go-nogo A 확정 → Retrospective 완결 (이 Topic 의 마지막 모듈)
- 그 뒤: B 음성 출력 → C 음성 입력 — go-nogo 후속표 순서대로 (새 Topic 또는 CVL 유지보수)

## CVL (Topic 완료 후)

- [guides/operator-guide.md](guides/operator-guide.md) — **진행자용 조작 가이드** (켜기 `start_comc.ps1` → 브라우저 탭 하나 · 말 시키기 · 모드 버튼/핫키 · 멈추기). CVL 3 에서 창 4개 → [콘솔 하나](../09-Desktop-Shell-and-Overlay/examples/engine/comc_console.py)
- [guides/rehearsal-log-4.md](guides/rehearsal-log-4.md) — 4회차(무관중, 소리 포함) 절차·질문 세트·결과 칸. OBS `Untitled` 프로필 현황 포함
- [examples/rehearsal4_driver.py](examples/rehearsal4_driver.py) — 4회차 질문 8개를 데몬에 넣는 드라이버 (핫키·패닉은 파일 조작)
- [examples/test_casual_lane.py](examples/test_casual_lane.py) — CVL 4 회귀: 캐주얼 의도 분류 14건(LLM 없음) + `--llm` 끝까지 4건(자리 비움 ≥30초 · 날씨 값 · 방송 질문은 방송 레인)
- [examples/test_live27_incidents.py](examples/test_live27_incidents.py) — Live #27 사고 7~11 재현 테스트 (수정 전 0/10 → 후 10/10)
