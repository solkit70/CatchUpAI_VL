# M4 — Wake Word / VAD 하네스

**상태**: 🟡 진행 중 (실습 1·2 완료, 실습 3·4 다음 세션)
**예상 학습 시간**: 7h
**Topic**: [[../topic_starter|Live-CoMC-App]]

---

## 이 모듈에서 배우는 것

파이프라인 ①Wake·②VAD 관문을 실제 마이크로 측정한다. 호출어를 안정적으로 감지하는가(오탐), 발화 종료 시점을 정확히 아는가(VAD), 그리고 TTS 에코 루프를 차단하는가. **실측 하네스 단계**의 첫 모듈이라 사용자가 직접 발화·녹음하고, 프로브 스크립트가 이를 측정한다.

## 문서 목록 (학습 순서)

1. [concepts/wake-vad-concepts.md](concepts/wake-vad-concepts.md) — 오탐·에코 루프·VAD 무음 임계값 + **커스텀 호출어의 현실**(사전학습 vs 학습)
2. [examples/wake_probe.py](examples/wake_probe.py) — openWakeWord 감지 프로브. `record`(녹음→오프라인 채점)/`detect`/`falsepos` 모드
3. [examples/vad_probe.py](examples/vad_probe.py) — Silero VAD 발화 구간 검출(ONNX 직구동, torch 우회)
4. [examples/mic_check.py](examples/mic_check.py) — 마이크 캡처+오프라인 감지 진단 도구
5. [examples/probe_log.jsonl](examples/probe_log.jsonl) — 감지·발화 측정 로그
6. guides/false-positive-report.md — 3시간 환산 오탐률 (⏳ 실습 3, 다음 세션)
7. troubleshooting/echo-loop-notes.md — 에코 루프 차단 검증 (⏳ 실습 4, 다음 세션)

## 실측 결과 (이번 세션)

**실습 1 — openWakeWord (Shure MV7, 100초 record)**

| 후보 호출어 | 감지(10회 중) | 교차 오탐 | 판정 |
|---|---|---|---|
| **alexa** | ~10/10 (0.72–0.999) | 0 | ✅ 채택 |
| hey_mycroft | 9/10 | 0 | 백업 |
| hey_jarvis | 2/10 | 0 | 탈락(재현율↓) |

- 프레임 처리 **6.07ms ≪ 80ms** → CPU만으로 실시간 여유 충분.
- 한국어 "코엠씨"는 학습 필요 — 이번엔 사전학습 모델로 **방법론 검증**. 학습 투자 여부는 실습 3 오탐률로 결정.

**실습 2 — Silero VAD (25초 record, 800ms 무음 기준)**

- "3부 시작"(짧은 명령) → 1.15s 단일 구간, 종료 정확(프레임 32ms ≪ 500ms) ✅
- 긴 다문장 발화는 무음 임계값으로 분할/병합: 800ms→7개, **2000ms→3개(긴 질문 9.6s 병합)**. MC 짧은 명령은 800ms 적합, 긴 질문은 ~2000ms 또는 LLM단 병합.

## 발견한 함정 2가지 (troubleshooting 가치)

1. **openWakeWord 키 불일치**: `Model()`이 `wakeword_models` 리스트를 전체 경로로 in-place 변형하지만, `predict()`는 짧은 이름으로 키를 반환 → 카운트 딕셔너리 KeyError. `list(oww.models.keys())`로 키를 가져와 해결.
2. **Silero VAD context prepend 누락**: v5 ONNX는 512샘플 앞에 **64샘플 context를 붙여 총 576샘플**을 입력해야 함. 512만 넣으면 에러 없이 speech 확률이 항상 ~0. 공식 OnnxWrapper대로 context 유지 추가해 해결.

**방법론 인사이트**: 백그라운드 실행 시 stdout 버퍼링으로 라이브 피드백이 안 보여 실시간 감지가 타이밍에 취약했다. **고정 창 녹음 → 오프라인 채점**(record 모드)으로 바꾸니 결정론적이고 재현 가능해졌다. `mic_check.py`(녹음+오프라인 감지)가 파이프라인 정상 여부를 격리 진단하는 데 결정적이었다.

## 핵심 결론 (다음 단계로 넘어가는 것)

- **호출어 후보 `alexa` 확정**, 실시간 처리 여유 확인. 진짜 3시간 오탐률은 실습 3에서.
- **VAD 무음 임계값은 튜닝 파라미터** — 명령용 800ms / 질문용 2000ms, 앱에서 상황별 조정 or LLM 병합.
- `session_state.wake_gate`(M3 스키마)의 런타임 차단은 실습 4(에코 루프)에서 검증.

## 검증 방법

```
cd 04-WakeWord-VAD-Harness/examples
python wake_probe.py --list-devices                       # 입력 장치 확인
python wake_probe.py --mode record --seconds 100 --device N  # 실습 1
python vad_probe.py  --mode record --seconds 25  --device N  # 실습 2
```

## 다음 모듈

⏳ 이번 모듈 잔여: 실습 3(3시간 환산 오탐률, 30분 배경 녹음) · 실습 4(에코 루프 차단) → 완료 후 M5

← 이전: [M3 - 데이터 계약과 안전 정책 스펙](../03-Data-Contracts-and-Safety/README.md)
