# M6 — 멀티 TTS 하네스 + 오디오 라우팅

**상태**: 실습 1·2·4 완료 · 실습 3 대부분 완료(트랙 뮤트 검증 1건 미완) · DoD 5.5/6
**예상 학습 시간**: 7h
**난이도**: ⭐⭐⭐

방송 파이프라인의 ⑧ TTS·오디오 출력 단계를 실물로 만들고 측정하는 모듈이다.
M5의 LLMProvider 와 같은 구조로 TTS 어댑터 계층을 세우고, 어느 프로바이더를
기본값으로 쓸지 **취향이 아니라 실측으로** 정한다.

이 세션에는 M5 이월 과제였던 **LLM 지연 원인 분석**도 함께 처리했다.
결과가 이 모듈의 설계에 직접 영향을 줬다 —
[llm-latency-sweep.md](../05-STT-LLM-Harness/guides/llm-latency-sweep.md) 참조.

---

## 학습 순서

### 1. 전제

1. [../05-STT-LLM-Harness/guides/llm-latency-sweep.md](../05-STT-LLM-Harness/guides/llm-latency-sweep.md)
   — LLM 지연을 15.2초에서 2.6초로 내린 측정. **대기 필러 설계의 전제이므로 먼저 읽을 것**

### 2. 코드

2. [examples/voice_registry.json](examples/voice_registry.json)
   — 4종 프로바이더 설정. 모델·보이스 ID를 코드에 박지 않기 위한 장치. 클론 보이스 회피 원칙도 여기 있다
3. [examples/tts_providers/base.py](examples/tts_providers/base.py)
   — 공통 인터페이스. 첫 청크와 완료를 나눠 재는 이유가 문서화돼 있다
4. [examples/tts_providers/edge_provider.py](examples/tts_providers/edge_provider.py)
   — 무료·최속. async 스트림을 큐로 넘겨 도착 시각을 보존한다
5. [examples/tts_providers/openai_provider.py](examples/tts_providers/openai_provider.py)
   — `with_streaming_response` 로 진짜 스트리밍 경로를 쓴다
6. [examples/tts_providers/qwen_provider.py](examples/tts_providers/qwen_provider.py)
   — RemotionStudio 검증 형태. URL 반환이라 조기 재생 불가 (경로의 한계, Qwen 의 한계 아님)
7. [examples/tts_providers/elevenlabs_provider.py](examples/tts_providers/elevenlabs_provider.py)
   — ⚠️ **미검증**. 키가 없어 실제 호출로 확인하지 못했다
8. [examples/tts_probe.py](examples/tts_probe.py)
   — 프리플라이트. 키 확인이 아니라 **실제 합성 1회**로 판정 (실습 1)
9. [examples/tts_compare.py](examples/tts_compare.py)
   — 문장 3종 × 프로바이더 × N회 실측 (실습 2)
10. [examples/circuit_breaker.py](examples/circuit_breaker.py)
    — 비용·호출·문자 상한 초과 시 무료 프로바이더로 강등 (실습 4)

### 3. 결과와 설계

11. [guides/tts-comparison.md](guides/tts-comparison.md)
    — **이 모듈의 핵심 산출물**. 4종 실측 비교와 기본값 결정 근거
12. [guides/wait-filler-design.md](guides/wait-filler-design.md)
    — 대기 필러 설계. M5에서 넘어온 과제 (로드맵 외 추가)
13. [guides/audio-routing-setup.md](guides/audio-routing-setup.md)
    — VoiceMeeter+VB-CABLE 라우팅 설계와 절차. **설계만, 구성은 이월**

---

## 실행 순서

```bash
cd examples

# 실습 1 — 프리플라이트 (나머지의 전제 조건)
python tts_probe.py
python tts_probe.py --keep          # 프리플라이트 오디오를 남긴다

# 실습 2 — 실측표
python tts_compare.py --repeats 5

# 실습 4 — 서킷 브레이커
python circuit_breaker.py --demo --by cost --dry-run
python circuit_breaker.py --demo --by calls --repeats 1
python circuit_breaker.py --demo --by chars
```

⚠️ 이 모듈의 코드는 **오디오를 재생하지 않는다.** 파일로만 쓴다.
라이브 방송 중에 돌리면 스피커 출력이 방송에 섞이고, M4 에코 게이트 측정 조건까지 오염된다.
청취는 `audio/` 의 파일을 따로 열어서 한다.

---

## 이 모듈에서 확인된 것

| # | 발견 | 영향 |
|---|---|---|
| 1 | **지연은 추론 토큰이었다** — openai 추론 1440→0tok 일 때 15.2s→2.6s | M7 목표 지연 달성 가능. 첫 발화까지 17s → 4.5s |
| 2 | **낮은 effort 에서 품질이 떨어지지 않았다** — 오히려 문장이 짧아져 TTS 에 유리 | 기본 effort 를 minimal 로 둘 근거 |
| 3 | **무료(edge)가 가장 빠르다** — 첫 청크 588ms, 2위의 38% | 로드맵의 "유료 기본 → 무료 강등" 전제가 뒤집힌다 |
| 4 | **edge 는 21회 중 1회 8.07초로 튄다** | SLA 없음. 감시와 승격 로직이 필요 |
| 5 | **openai 는 같은 문장을 매번 다르게 읽는다** (길이 4.6~5.4s) | 발화 종료 시각 예측 불가 → 타이밍 설계 제약 |
| 6 | **완료 시간은 첫 청크보다 3배 이상 불안정** | 둘을 뭉쳐 재면 edge 를 잘못 탈락시킨다 |
| 7 | **비용만 보는 서킷 브레이커는 조용히 과소 추정한다** | 단가 미확인·이중 요금 프로바이더 존재 → 호출·문자 상한 병행 |
| 8 | **1순위가 무료면 서킷 브레이커는 동작할 수 없다** | 기본값 선택과 비용 차단은 따로 정할 수 없는 한 쌍 |
| 9 | `anthropic` 0.75.0 은 `output_config` 를 모른다 | `extra_body` 우회. SDK 1.x 업그레이드는 백로그 |

상세는 [guides/tts-comparison.md](guides/tts-comparison.md) 와
[../vl_worklog/20260823_M6_Live-CoMC-App.md](../vl_worklog/20260823_M6_Live-CoMC-App.md) 참조.

---

## Definition of Done

- [~] 4종 TTS 모두 동일 문장 합성 성공 — **3/4**. ElevenLabs 는 키가 없어 미검증.
      어댑터는 작성했고 프리플라이트가 자동 제외한다
- [x] 지연·비용·품질 실측표 완성 및 기본값 결정 — [tts-comparison.md](guides/tts-comparison.md).
      단, **주관 청취 평가는 방송 종료 후로 분리** (재생이 방송에 섞이므로)
- [~] VoiceMeeter+VB-CABLE 라우팅 구성, OBS 트랙 개별 뮤트 검증 — **거의 완료**.
      **VoiceMeeter 는 실측으로 불필요 판명**(마이크 WASAPI 공유 모드 동시 열기 성립).
      VB-CABLE 설치·통과 검증·재생 지연 실측(**케이블 314ms**)·OBS 격리 구성까지 완료.
      **트랙 2 개별 뮤트 검증 1건만 미완** → [audio-routing-setup.md](guides/audio-routing-setup.md)
- [x] **운용 모드 2종 정리** (로드맵 외 추가) — [operating-modes.md](guides/operating-modes.md).
      평상시 미팅 녹화 세팅과 AI 공동진행 방송 세팅을 체크리스트로 분리
- [x] 비용 서킷 브레이커 강등 동작 확인 — 실제 합성으로 openai → edge 강등 검증
- [x] README 작성 완료
- [x] WorkLog 작성 완료

---

## Self-Assessment

**개념 이해 — 클론 보이스를 기본값으로 쓰지 않는 이유**

시청자가 사람의 발화와 AI 의 발화를 구분할 수 없게 되기 때문이다. 이 파이프라인은
⑦ 안전 게이트가 근거 없는 발화를 차단하는 구조인데, 차단이 제대로 동작하려면
"AI 가 말했다"는 사실 자체가 청자에게 전달돼야 한다. 목소리가 같으면 AI 의 실수가
진행자의 실수로 귀속되고, 반대로 진행자의 말이 AI 의 말로 오해된다.
M1 "커버리지 없으면 침묵" 원칙과 같은 뿌리다 — **AI 발화는 AI 발화로 들려야 한다.**
목소리 성별을 진행자와 다르게 둔 것은 이 구분을 만드는 가장 값싼 신호다.

**실무 활용 — 방송 중 비용이 치솟으면 앱이 어떻게 반응하는가**

세션 누적 호출 수·문자 수·비용을 세다가 셋 중 하나라도 상한을 넘으면
무료 프로바이더로 강등하고, 강등은 세션이 끝날 때까지 되돌리지 않는다.
자동 복귀를 넣으면 상한 근처에서 오르내리며 비용이 계속 새고 목소리가 왔다 갔다 한다.

비용 하나만 세지 않는 이유는 **비용을 정확히 셀 수 없는 프로바이더가 실제로 있기 때문**이다.
qwen 은 공식 단가가 확인되지 않았고, openai 는 텍스트+오디오 토큰 이중 요금인데
음성 엔드포인트가 오디오 토큰 수를 돌려주지 않는다. 비용만 보는 차단기는
그런 프로바이더에서 0 에 가깝게 집계되어 **폭주해도 걸리지 않는다.**
호출 수와 문자 수는 단가와 무관하게 항상 셀 수 있다.

다만 이번 실측으로 **방향이 뒤집혔다.** 가장 빠른 프로바이더가 이미 무료라서,
실제로 필요한 것은 비용 강등이 아니라 가용성 승격이다(edge 실패·지연 → openai).
승격 로직은 M7 통합에서 붙인다.

---

← 이전: [M5 STT + 멀티 LLM 하네스](../05-STT-LLM-Harness/README.md)
→ 다음: M7 Co-MC 엔진 POC (`07-CoMC-Engine-POC/`)
