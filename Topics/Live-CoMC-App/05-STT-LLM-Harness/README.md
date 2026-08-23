# M5 — STT + 멀티 LLM 하네스

**상태**: 실습 1~4 완료 · DoD 7/8 (1건 N/A) · 이월 해소됨(2026-08-23)
**예상 학습 시간**: 8h
**난이도**: ⭐⭐⭐

방송 파이프라인의 ⑤ STT 와 ⑥ LLM 응답 단계를 실물로 만들고 측정하는 모듈이다.
M3에서 설계만 해둔 3사 스키마 정규화를 코드로 옮기고, 한국어 전사 정확도를
공개 수치가 아니라 **이 마이크·이 목소리·이 문장으로** 직접 잰다.

---

## 학습 순서

### 1. 개념

1. [../03-Data-Contracts-and-Safety/guides/llm-schema-normalization.md](../03-Data-Contracts-and-Safety/guides/llm-schema-normalization.md)
   — M3 설계 문서. 이 모듈의 구현은 전부 여기서 출발한다. **먼저 읽을 것**

### 2. 실습 자료

2. [guides/utterance-script.md](guides/utterance-script.md)
   — WER 측정용 20문장(질문형 10 + 명령형 10)과 녹음 방법. 왜 일부러 어렵게 만들었는지 포함
3. [guides/llm_registry.json](guides/llm_registry.json)
   — 3사 프로바이더 설정. 모델 ID를 코드에 하드코딩하지 않기 위한 장치

### 3. 코드

4. [examples/utterances.py](examples/utterances.py)
   — 20문장 정답 데이터와 WER 비교용 정규화 함수
5. [examples/record_utterances.py](examples/record_utterances.py)
   — 고정 창 녹음기. M4의 장치 이름 해석과 스트림 1회 오픈 규약을 그대로 따른다
6. [examples/stt_probe.py](examples/stt_probe.py)
   — 전사 + WER/CER 계산 + 3단 폴백 (실습 1·2)
7. [examples/llm_probe.py](examples/llm_probe.py)
   — 3사 프리플라이트. 키·인증·**실제 호출 가능 여부**까지 확인 (실습 4)
8. [examples/llm_providers/](examples/llm_providers/)
   — LLMProvider 어댑터 계층 (실습 3)
   - [base.py](examples/llm_providers/base.py) — 공통 인터페이스, 스키마 다운그레이드, 재검증
   - [claude_provider.py](examples/llm_providers/claude_provider.py) — strict tool use
   - [openai_provider.py](examples/llm_providers/openai_provider.py) — json_schema strict
   - [gemini_provider.py](examples/llm_providers/gemini_provider.py) — responseSchema
9. [examples/llm_compare.py](examples/llm_compare.py)
   — 3사 동일 입력 비교 + 재시도·폴백 검증 (실습 3)

### 4. 결과

10. [guides/stt-wer-report.md](guides/stt-wer-report.md)
    — 한국어 전사 정확도 실측 리포트. **이 모듈의 핵심 산출물**
11. [guides/llm-latency-sweep.md](guides/llm-latency-sweep.md)
    — LLM 지연 원인 분석. 2026-08-23 M6 세션에서 이월 과제로 처리했다.
    지연은 추론 토큰이었고, effort 를 낮추면 15.2초 → 2.6초로 줄면서도 품질은 유지된다

---

## 실행 순서

```bash
cd examples

# 실습 4 — 프리플라이트 (가장 먼저. 나머지의 전제 조건)
python llm_probe.py
python llm_probe.py --simulate-fail claude     # 강제 실패 시 폴백 축소 확인

# 실습 3 — 3사 어댑터
python llm_compare.py
python llm_compare.py --fallback-demo

# 실습 1 — 녹음 후 전사 정확도
python record_utterances.py --list-devices
python record_utterances.py --device "MV7" --condition clean
python stt_probe.py --condition clean

# 실습 2 — STT 3단 폴백
python stt_probe.py --condition clean --force-fail t4o
python stt_probe.py --condition clean --force-fail t4o,batch

# 이월 과제 — 지연 원인 분석 (2026-08-23 추가)
python llm_latency_sweep.py --repeats 2
python llm_effort_quality.py --provider openai --levels minimal,low
```

---

## 이 모듈에서 확인된 것

| # | 발견 | 영향 |
|---|---|---|
| 1 | **호출어 `코엠씨` 전사 0/11** | 전사문에서 호출어를 찾는 방식은 불가. M4 openWakeWord 경로가 유일한 길 |
| 2 | **CER 16.7% → 8.6%** (표기 허용 기준) | 영어 용어의 한글 표기를 오류로 세면 실패를 과장한다 |
| 3 | **`gpt-live-transcribe` 는 파일 전사 불가** | Realtime 전용(404). Roadmap 1단계 모델을 교체 |
| 4 | **`models.list()` ≠ 호출 가능** | 프리플라이트에 스모크 콜 필수 |
| 5 | **LLM 지연 10.8~21.6초** | STT(1.2초)가 아니라 ⑥이 병목. → **해소됨**: 원인은 추론 토큰이며 effort 를 낮추면 2.6초. [llm-latency-sweep.md](guides/llm-latency-sweep.md) |
| 6 | **google-genai 클라이언트 재생성 시 사망** | 프로세스당 1개로 재사용해야 함 |

상세는 [guides/stt-wer-report.md](guides/stt-wer-report.md) 와
[../vl_worklog/20260820_M5_Live-CoMC-App.md](../vl_worklog/20260820_M5_Live-CoMC-App.md) 참조.

---

## Definition of Done

- [x] 한국어 WER 실측 완료 (일반 조건)
- [~] BGM 조건 — **N/A**. BGM을 헤드폰으로 듣는 셋업이라 마이크에 들어가지 않는다.
      악조건 검증은 M4 에코 게이트 측정이 대신한다 ([리포트 1절](guides/stt-wer-report.md))
- [x] STT 3단 폴백이 강제 실패 테스트에서 정상 동작
- [x] LLMProvider 어댑터로 3사 모두 같은 스키마 응답 확보
- [x] 스키마 위반 시 재시도 → 폴백 로직 검증
- [x] API 키 유효성 프리플라이트 함수 동작 확인
- [x] README 작성 완료
- [x] WorkLog 작성 완료

---

← 이전: [M4 Wake Word / VAD 하네스](../04-WakeWord-VAD-Harness/README.md)
→ 다음: M6 멀티 TTS 하네스 + 오디오 라우팅 (`06-TTS-Audio-Routing-Harness/`)
