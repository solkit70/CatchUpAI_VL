---
title: "WorkLog - M6: 멀티 TTS 하네스 + 오디오 라우팅"
created: 2026-08-23 05:11:00
tags:
  - worklog
  - live-comc-app
---

## 세션 정보

**날짜**: 2026-08-23
**Topic**: Live-CoMC-App
**모듈**: M6 - 멀티 TTS 하네스 + 오디오 라우팅
**이전 세션**: [20260820_M5_Live-CoMC-App.md](20260820_M5_Live-CoMC-App.md)
**학습 시간**: 05:11 - 05:47 (36분)

> 계획은 6시간이었다. 36분에 끝난 이유는 측정 대기를 전부 병렬로 돌렸기 때문이다 —
> LLM 스윕(24회 호출)과 TTS 실측(45회 합성)이 백그라운드로 도는 동안
> 어댑터 작성과 필러 설계를 진행했다. 실제 API 대기 시간이 세션 시간의 대부분이었다.

## 🎯 오늘의 학습 목표

- [x] **M5 이월** — LLM 지연 원인 분석 (effort 스윕)
- [x] 실습 1 — TTSProvider 어댑터 + 프리플라이트
- [x] 실습 2 — 지연·비용 실측표, 기본값 결정
- [x] 실습 4 — 비용 서킷 브레이커
- [x] 실습 5(추가) — 대기 필러 문구 설계
- [~] 실습 3 — VoiceMeeter/VB-CABLE 라우팅 → **설계만. 구성은 이월**

### 오늘의 제약 — 라이브 방송 중

진행자가 방송 중이라 두 가지를 계획에서 뺐다.

1. **VoiceMeeter/VB-CABLE 설치** — 둘 다 미설치이고 설치 시 재부팅이 필요하다.
   방송 중 재부팅은 불가. 실습 3의 구성 작업을 다음 세션으로 미루고,
   대신 [설계와 절차 문서](../06-TTS-Audio-Routing-Harness/guides/audio-routing-setup.md)를
   완비해 두었다 — 다음 세션에 그대로 따라 하면 된다
2. **오디오 재생 검증** — TTS 결과를 스피커로 들으면 방송 오디오에 섞이고
   M4 에코 게이트 측정 조건까지 오염된다. 그래서 이 세션의 코드는 **오디오를 재생하지 않는다.**
   파일로만 쓰고 길이·바이트·지연으로 검증했다. 주관 청취 평가는 방송 종료 후로 분리

제약이 오히려 도움이 된 면도 있다. 재생이 막히니 **측정 가능한 것만으로 판단하는**
설계를 하게 됐고, 그 결과 첫 청크와 완료 시간을 분리해 재게 됐다 — 아래 인사이트 3번 참조.

## 📚 진행 내용

### 1. M5 이월 — LLM 지연 원인 분석

**순서**: 1번째. 이후 작업의 전제라 가장 먼저.

M5에서 LLM 지연이 10.8~21.6초였고 STT는 1.2초였다. M7 전제가 여기 달려 있어 먼저 처리했다.
가설은 "3사 모두 추론이 켜진 채로 호출되고 있다"였고, 맞았다.

상세: [llm-latency-sweep.md](../05-STT-LLM-Harness/guides/llm-latency-sweep.md)

| | 기본값 | 튜닝 후 | 추론 토큰 |
|---|---|---|---|
| openai | 15.2s | **2.6s** (`reasoning_effort=minimal`) | 1440 → 0 |
| gemini | 11.1s | **4.1s** (`thinking_level=low`) | 1141 → 없음 |
| claude | 7.2s | 7.0s (반응 없음) | 보고 안 함 |

**지연은 추론 토큰이었다.** 줄어든 1400여 토큰은 사용자에게 도달하지 않는 사고 과정이고,
실제 발화문 길이는 거의 그대로다.

품질 확인을 따로 했다. 계약 통과 여부만 보면 **형식** 판정에 그치므로, 발화문을 직접
나란히 찍었다([llm_effort_quality.py](../05-STT-LLM-Harness/examples/llm_effort_quality.py)).
근거 2건을 양쪽 다 썼고 누락이 없다. 오히려 minimal 쪽이 문장을 짧게 끊어
**한 호흡에 읽을 수 있는 길이**로 만들었다 — TTS 로 넘길 때 유리하다.

TTFT(첫 토큰 지연)는 재지 않기로 했다. ⑦ 게이트가 JSON 전체를 받아 근거 대조까지
끝내야 발화가 허용되므로, 첫 토큰이 빨라도 그 시점에 할 수 있는 일이 없다.
계획에는 재겠다고 적었다가 스크립트를 쓰기 전에 뺐다.

### 2. 실습 1 — TTSProvider 어댑터 + 프리플라이트

**순서**: 2번째. LLM 스윕이 백그라운드로 도는 동안 시작.

M5 LLMProvider 와 같은 구조로 4종 어댑터를 만들고, 프리플라이트를
**실제 합성 1회**로 구성했다(M5 문제 1의 교훈 — 키 확인만으로는 못 잡는다).

```
edge         OK  (edge-tts/ko-KR-SunHiNeural)  첫청크 620ms · 완료 1,587ms
openai       OK  (gpt-4o-mini-tts/nova)        첫청크 2,401ms · 완료 2,512ms
qwen         OK  (qwen3-tts-flash/Cherry)      첫청크 2,321ms · 완료 2,322ms
elevenlabs   제외 (키 없음 — 어댑터만 작성, 미검증)
```

LLM 과 달리 TTS 에서는 **첫 청크 지연이 실질 지표**다. ⑧ 단계에 들어온 텍스트는
이미 ⑦ 게이트를 통과했으므로 오디오가 도착하는 즉시 재생할 수 있다.
같은 "첫 조각 지연"이 어느 단계냐에 따라 의미가 정반대다.

### 3. 실습 2 — 실측표와 기본값 결정

**순서**: 3번째.

문장 3종(plain/mixed/long) × 3사 × 5회 = 45회 합성.
상세: [tts-comparison.md](../06-TTS-Audio-Routing-Harness/guides/tts-comparison.md)

**결정: 기본 프로바이더 = edge-tts** (`ko-KR-SunHiNeural`).
첫 청크 588ms(최악 628ms), 무료, 출력이 결정적, 여성 음성으로 진행자와 구분.
2순위 openai(1,548ms), 3순위 qwen(2,827ms·조기 시작 불가).

### 4. 실습 4 — 비용 서킷 브레이커

**순서**: 4번째. 설계는 실습 2 측정 대기 중 병행.

세션 누적 **호출 수·문자 수·비용** 셋 중 하나라도 상한을 넘으면 무료로 강등한다.
강등은 세션이 끝날 때까지 되돌리지 않는다.

실제 합성으로 검증: 호출 상한 4회에서 `openai → edge` 강등 확인.

### 5. 실습 5(추가) — 대기 필러 설계

**순서**: TTS 실측 5회 반복이 백그라운드로 도는 동안 병행.

M5에서 "M6 오디오 라우팅에서 다룬다"고 넘긴 항목.
설계: [wait-filler-design.md](../06-TTS-Audio-Routing-Harness/guides/wait-filler-design.md)

지연이 17초에서 4.5초로 줄면서 **요구 자체가 바뀌었다.** 17초를 메우려면 필러가
사실상 하나의 발화가 되어야 했고, 그러면 내용이 필요하고, 내용이 있으면 근거가 필요해
M1 원칙과 충돌한다. 4.5초는 내용 없는 한 마디로 덮인다.

## 🐛 문제 해결 로그

### 문제 1: anthropic 0.75.0 은 `output_config` 를 모른다

`Messages.create() got an unexpected keyword argument 'output_config'`.
설치된 SDK 가 구버전이라 effort 를 명시 인자로 받지 못한다.

SDK 1.x 로 올리면 `httpx2` 전환 등 파괴적 변경이 딸려 오고 M5 하네스가 도는 중이라
방송일에 건드릴 일이 아니다. `extra_body={"output_config": {...}}` 로 우회했다.

**우회가 실제로 먹었는지 따로 확인했다.** 없는 값(`nonsense-level`)을 보내니
서버가 400 과 함께 유효 목록을 돌려줬다 — 요청이 도달해 검증까지 받고 있다는 뜻이다.
"보냈으니 됐겠지"로 넘어가면 M5 문제 1(목록 조회만으로 만든 프리플라이트)의 반복이 된다.

### 문제 2: thinking 을 끄는 길은 막아 두는 게 맞았다

지연을 줄이는 가장 직관적인 수단은 thinking 을 끄는 것이다. 쓰지 않았다.
Opus 5 에서 thinking 을 끄면 도구 호출이 `tool_use` 블록 대신 **본문 텍스트로 새는**
실패 모드가 있고, Claude 어댑터는 strict tool use 기반이라 정확히 여기 걸린다.
그 경우 호출은 200 으로 성공하고 도구는 실행되지 않으며 오류도 나지 않는다 —
방송 중이라면 원인 모를 침묵으로 나타났을 것이다.

결과적으로 Claude 는 effort 에 거의 반응하지 않았지만, 위험한 길을 피한 판단은 유효했다.

### 문제 3: 비용 표가 "미확인"으로 나왔다 — 오래된 런타임 파일

실측표를 처음 돌렸을 때 openai 비용이 "미확인"으로 나왔다. 가격을 확인해 레지스트리에
넣은 뒤였는데도 그랬다. **`voice_registry.runtime.json` 이 가격 갱신 전에 생성된 상태**였다.

프리플라이트가 만드는 런타임 파일은 원본 레지스트리의 스냅샷이다. 원본을 고치면
프리플라이트를 다시 돌려야 반영된다. M5 에서 같은 구조를 만들 때는 모델 ID만 담았으므로
드러나지 않았던 함정이다. → 재생성 후 정상.

### 문제 4: 1순위가 무료면 서킷 브레이커가 동작하지 않는다

호출 상한 데모를 실제 합성으로 돌렸는데 강등이 일어나지 않았다.
원인은 버그가 아니라 **설계상의 사실**이었다 — 기본값이 `edge` 이고 강등 목적지도 `edge` 라,
내려갈 곳이 없어 차단기가 즉시 반환한다.

**기본값 선택(실습 2)과 비용 차단(실습 4)은 따로 정할 수 없는 한 쌍이다.**
데모가 이 상태를 감지해 명시적으로 알리고 유료 1순위로 바꾸도록 고쳤다.
조용히 넘어가면 "차단기가 있다"는 착각만 남는다.

### 문제 5: Qwen 이 스트리밍을 못 한다고 단정할 뻔했다

첫 청크와 완료가 1~2ms 차이로 붙어 있어 "Qwen 은 조기 재생이 안 된다"고 어댑터 주석에 적었다.
가격을 찾다가 DashScope 가 **WebSocket 스트리밍 경로를 따로 제공**하고 Flash 는
첫 패킷 300ms 수준이라는 것을 알게 됐다.

내가 쓴 HTTP 경로(`stream=False`, URL 반환)의 한계였지 Qwen 의 한계가 아니었다.
주석과 레지스트리를 고쳤다. **하나의 경로로 잰 결과를 프로바이더 전체의 성질로 일반화한 것**이
실수의 형태다 — M5 문제 3(`gpt-live-transcribe` 가 Realtime 전용)과 같은 종류다.

## 📊 DoD 체크리스트

로드맵 M6의 Definition of Done:

- [~] 4종 TTS 모두 동일 문장 합성 성공 — **3/4**. ElevenLabs 는 키 없음(미검증)
- [x] 지연·비용·품질 실측표 완성 및 기본값 결정 — 주관 청취 평가만 방송 후로 분리
- [ ] VoiceMeeter+VB-CABLE 라우팅 구성, OBS 트랙 개별 뮤트 검증 — **이월** (설계·절차는 완비)
- [x] 비용 서킷 브레이커 강등 동작 확인
- [x] README 작성 완료
- [x] WorkLog 작성 완료

**완료율**: 4/6 완료 + 1건 부분(3/4) + 1건 이월

## 💡 Daily Retrospective

### What went well (잘된 점)

- **이월 과제를 먼저 처리한 순서가 맞았다.** LLM 지연 결과가 대기 필러 설계 요구를
  바꿔 놓았다. 필러부터 만들었다면 17초를 메우는 물건을 설계했을 것이고,
  그건 내용이 있어야 하고 내용이 있으면 근거가 필요해 M1 원칙과 충돌했을 것이다.
  **지연을 줄인 것이 필러를 안전하게 만들었다**
- **백그라운드 실행으로 대기 시간을 없앴다.** LLM 스윕(24회 호출)과 TTS 실측(45회 합성)이
  도는 동안 어댑터 작성과 필러 설계를 했다. M5에서 "사용자 참여 여부로 실습 순서를
  재배열"한 것과 같은 종류의 판단이다
- **첫 청크와 완료를 나눠 잰 것이 결정적이었다.** 완료 시간만 봤으면 edge 를 탈락시켰을 것이다
  (mixed 완료 1,122~3,598ms). 첫 청크는 522~628ms 로 촘촘하다
- 라이브 방송 제약이 오히려 설계를 다듬었다. 재생이 막히니 측정 가능한 지표만으로
  판단하는 구조를 만들게 됐다

### What could be improved (개선할 점)

- **런타임 파일 재생성을 잊었다**(문제 3). 원본을 고쳤으면 파생 파일도 다시 만들어야 하는데,
  그 의존 관계를 코드가 알려주지 않는다. `voice_registry.json` 이 `runtime.json` 보다
  새로우면 프리플라이트를 다시 돌리라고 경고하게 하는 편이 낫다
- **하나의 경로로 잰 결과를 프로바이더의 성질로 일반화했다**(문제 5). 가격을 찾다가
  우연히 발견했을 뿐, 안 찾았으면 그대로 남았을 오류다. "내가 쓴 경로가 유일한 경로인가"를
  주석에 적기 전에 물었어야 했다
- 계획에 TTFT 측정을 적었다가 스크립트 작성 직전에 뺐다. 계획을 세울 때
  **⑦ 게이트가 전체 JSON을 요구한다는 사실을 이미 알고 있었다** — 계획 단계에서 걸렀어야 했다
- edge 의 8초 outlier 를 처음 만났을 때 n=2 였다. 반복을 5회로 올리고서야 그것이
  희귀 사건임을 알았다. **처음부터 5회로 시작했으면** 한 번 덜 돌렸다

### Insights (인사이트)

**같은 지표가 단계에 따라 정반대 의미를 갖는다.** LLM 단계의 첫 토큰 지연은 무의미하다 —
⑦ 게이트가 JSON 전체를 받아 근거 대조까지 끝내야 발화가 허용되므로 부분 응답으로 할 수 있는
일이 없다. TTS 단계의 첫 청크 지연은 실질 지표다 — 이미 게이트를 통과한 텍스트라
오디오가 도착하는 즉시 재생할 수 있다. **"첫 조각을 빨리 받자"는 일반 최적화 지침이
어디에 적용되는지는 파이프라인의 검증 지점이 결정한다.**

**무료가 가장 빨랐고, 그것이 로드맵의 전제를 뒤집었다.** 실습 4는 "유료 기본값 → 비용 초과 →
무료 강등"을 가정했는데, 실측에서 edge-tts 가 첫 청크 588ms 로 openai(1,548ms)의 38%였다.
필요한 것은 강등이 아니라 **가용성 승격**(edge 실패·지연 → openai)이다.
설계 문서에 적힌 전제도 실측 앞에서는 가설일 뿐이다.

**"검증했다"의 범위를 좁게 적어야 한다.** 세 번 반복해서 같은 실수를 피했다 —
extra_body 우회가 서버에 도달하는지 400 테스트로 확인했고(문제 1), 프리플라이트를
실제 합성으로 만들었고, ElevenLabs 를 "어댑터 작성했으나 미검증"으로 명시했다.
반대로 한 번 실패했다(문제 5) — Qwen 을 "스트리밍 불가"로 단정했다.
차이는 **무엇을 검증하지 못했는지 먼저 적었느냐**에 있었다.

**비용을 셀 수 없는 프로바이더가 실제로 존재한다.** qwen 은 공식 단가가 확인되지 않았고,
openai `gpt-4o-mini-tts` 는 텍스트+오디오 토큰 이중 요금인데 음성 엔드포인트가
오디오 토큰 수를 돌려주지 않는다. 비용만 보는 차단기는 그런 프로바이더에서 0 에 가깝게
집계되어 **폭주해도 걸리지 않는다.** 호출 수와 문자 수는 단가와 무관하게 항상 셀 수 있다.
"셀 수 없는 것으로 만든 안전장치는 안전장치가 아니다."

**결정적 출력과 생성적 출력의 차이가 타이밍 설계에 걸린다.** edge 는 같은 문장을 매번
정확히 같은 길이(4.944초)로 읽는다. openai 는 4.608~5.400초로 매번 다르다.
발화 종료 시각을 예측해 다음 동작을 예약하는 설계는 결정적 프로바이더에서만 가능하다.
M7에서 발화 큐를 만들 때 이 차이가 드러날 것이다.

### Tomorrow's focus (다음에 할 것)

- **실습 3 — 오디오 라우팅 구성** (방송 없는 시간에). VoiceMeeter Banana + VB-CABLE 설치 →
  재부팅 → [절차 문서](../06-TTS-Audio-Routing-Harness/guides/audio-routing-setup.md) 대로.
  검증 기준은 "트랙 2 를 뮤트해도 트랙 1 이 살아 있는가"
- **라우팅 후 재측정** — 경로가 바뀌면 M4 에코 게이트 오탐률, M5 WER, M6 첫 청크 지연이
  모두 유효하지 않다. 특히 첫 청크는 파일 기준으로 쟀으므로 가상 케이블 버퍼 지연을 더해야
  실제 발화 시각이 된다 → 필러 트리거 시각(`T_filler`)이 여기 달렸다
- **주관 청취 평가** — `06-TTS-Audio-Routing-Harness/examples/audio/compare/` 45개 파일
- **M7 진입** — Co-MC 엔진 POC. 진입 전에 `llm_registry.json` 의 `fallback_order` 를
  `openai → gemini → claude` 로 바꾸고 프로바이더별 기본 effort 를 등재할 것
- M4 이월(여전히 미완): 과거 라이브 3시간 오디오 오프라인 채점 → 실측 오탐률

## 📎 참조 및 산출물

**생성된 파일 — M6**

- `06-TTS-Audio-Routing-Harness/README.md` — 모듈 학습 순서와 발견 9건
- `06-TTS-Audio-Routing-Harness/guides/tts-comparison.md` — **핵심 산출물**. 4종 실측 비교
- `06-TTS-Audio-Routing-Harness/guides/wait-filler-design.md` — 대기 필러 설계 (로드맵 외 추가)
- `06-TTS-Audio-Routing-Harness/guides/audio-routing-setup.md` — 라우팅 설계·절차 (구성은 이월)
- `06-TTS-Audio-Routing-Harness/examples/voice_registry.json` — 4종 설정 + 클론 보이스 회피 정책
- `06-TTS-Audio-Routing-Harness/examples/tts_probe.py` — 프리플라이트 (실제 합성 검증)
- `06-TTS-Audio-Routing-Harness/examples/tts_compare.py` — 실측표 생성
- `06-TTS-Audio-Routing-Harness/examples/circuit_breaker.py` — 서킷 브레이커
- `06-TTS-Audio-Routing-Harness/examples/tts_providers/` — 어댑터 5종 (base + 4사)

**생성·수정된 파일 — M5 (이월 과제)**

- `05-STT-LLM-Harness/guides/llm-latency-sweep.md` — 지연 원인 분석 리포트
- `05-STT-LLM-Harness/examples/llm_latency_sweep.py` — effort 스윕
- `05-STT-LLM-Harness/examples/llm_effort_quality.py` — 발화문 품질 비교
- `05-STT-LLM-Harness/examples/llm_providers/` — 3사 어댑터에 effort 제어·추론 토큰 계측 추가

**측정 로그**

- `05-STT-LLM-Harness/examples/latency_sweep.json` — 3사 × effort × 2회
- `06-TTS-Audio-Routing-Harness/examples/tts_comparison.json` — 3사 × 문장 3종 × 5회
- `06-TTS-Audio-Routing-Harness/examples/tts_log.jsonl` — `tts_preflight` / `tts_compare` /
  `tts_circuit_break` / `tts_circuit_demo` 이벤트
- `06-TTS-Audio-Routing-Harness/examples/audio/compare/` — 합성 오디오 45개 (청취 평가 대기)

**다음 세션 준비사항**

- VoiceMeeter Banana 와 VB-CABLE 설치 (재부팅 필요) — **방송 일정이 없는 시간에**
- 설치 확인: `python -c "import sounddevice as sd; [print(d['name']) for d in sd.query_devices()]"`
- ElevenLabs 키를 발급했다면 환경 변수 설정 후 `python tts_probe.py` 한 번

---

**작성자**: solkit70
**방법론**: VibeLearn AI
