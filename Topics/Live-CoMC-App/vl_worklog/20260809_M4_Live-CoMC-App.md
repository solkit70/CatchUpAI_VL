# WorkLog - M4: Wake Word / VAD 하네스

**날짜**: 2026-08-09
**Topic**: Live-CoMC-App
**모듈**: M4 - Wake Word / VAD 하네스
**학습 시간**: M3 완료 후 같은 날 오전 이어서 진행. 실측 하네스라 사용자 라이브 녹음(Shure MV7) + 스크립트 디버깅으로 진행 (AI 보조로 코드·측정은 빠르게, 녹음 구간만 실제 소요)

---

## 🎯 오늘의 학습 목표 (실습 1·2, 실습 3·4는 다음 세션)

- [x] 개념: 오탐·에코 루프·VAD 무음 임계값 + 커스텀 호출어의 현실
- [x] 실습 1: openWakeWord 호출어 감지 — 오탐 0회 후보 확보
- [x] 실습 2: Silero VAD 발화 종료 판정
- [ ] 실습 3: 3시간 환산 오탐률 (다음 세션 — 30분 배경 녹음)
- [ ] 실습 4: 에코 루프 차단 (다음 세션)

---

## 📚 진행 내용

### 0. 환경 설치

`openwakeword`·`silero-vad`·`onnxruntime` 설치. `torch`·`sounddevice`·`pyaudio`·`ffmpeg`는 기존 설치. **torchaudio DLL 로드 실패**로 `silero_vad`/`torchaudio` import 불가 → GPU 없는 이 PC에서 torch/torchaudio 의존을 피해 **Silero VAD를 `silero_vad.onnx`로 onnxruntime 직구동**하기로 결정.

### 1. 개념 학습 — wake-vad-concepts.md

**결과**: `concepts/wake-vad-concepts.md`. 오탐(3시간 환산)·에코 루프(wake_gate 폐쇄)·VAD 무음 임계값 정리. 핵심 판단: openWakeWord는 사전학습 영어 모델만 즉시 감지, 한국어 "코엠씨"는 학습 필요 → 이번엔 **하네스·방법론을 검증**하고 오탐률로 "wake word vs 핫키"를 결정한다.

### 2. 실습 1 — openWakeWord 호출어 감지

**과정**: `wake_probe.py` 작성 → Shure MV7(device 1)로 후보 3개(hey_jarvis/alexa/hey_mycroft) 각 10회 발화 측정.

**결과**: **alexa 채택** — 10/10 감지(score 0.72–0.999), 교차 오탐 0. hey_mycroft 9/10 백업, hey_jarvis 2/10 탈락. 프레임 처리 6.07ms ≪ 80ms(실시간 여유).

**메모/인사이트**: 첫 실시간 `detect` 실행이 0회였는데, 원인은 감지 실패가 아니라 **백그라운드 stdout 버퍼링으로 라이브 피드백이 안 보여 발화 타이밍이 안 맞은 것**. `mic_check.py`(녹음→오프라인 감지)로 파이프라인이 정상(alexa=1.000)임을 격리 확인 후, `wake_probe.py`에 **record 모드(고정 창 녹음→오프라인 채점)**를 추가하니 결정론적으로 측정됐다.

### 3. 실습 2 — Silero VAD 발화 종료 판정

**과정**: `vad_probe.py`(ONNX 직구동) 작성 → 25초 record로 "3부 시작"(짧은 명령) + 5문장 질문 측정.

**결과**: "3부 시작" → 1.15s 단일 구간, 종료 정확(프레임 32ms). 긴 질문은 무음 임계값으로 분할: **800ms→7개, 2000ms→3개(질문 9.6s 병합)**. MC 짧은 명령은 800ms 적합, 긴 질문은 ~2000ms 또는 LLM단 병합이 필요하다는 설계 판단점 확보.

---

## 🐛 문제 해결 로그

### 문제 1: openWakeWord KeyError('hey_jarvis')

**증상**: `wake_probe.py` 첫 실행이 감지 프레임에서 `KeyError`로 종료.
**원인**: `Model(wakeword_models=[...])`이 전달 리스트를 **전체 경로로 in-place 변형**하는데, `predict()`는 **짧은 이름**으로 키를 반환 → 카운트 딕셔너리(변형된 전체 경로 키)와 불일치.
**해결**: 모델 생성 후 `model_names = list(oww.models.keys())`로 키를 가져와 카운트/쿨다운/요약에 사용.

### 문제 2: Silero VAD가 모든 음성에 speech 확률 ≈0

**증상**: 레벨 정상(peak 27–33%)·openWakeWord는 감지되는 오디오인데 Silero VAD가 발화 0개(모든 프레임 prob<0.5, max 0.003).
**원인**: v5 ONNX는 512샘플 프레임 앞에 **64샘플 context를 prepend해 총 576샘플**을 입력해야 하는데, 512만 넣어 에러 없이 항상 ~0을 반환.
**해결**: 공식 `OnnxWrapper` 소스 확인 → `SileroVAD` 래퍼에 context 64샘플 유지·prepend 추가. 저장 wav 재채점으로 즉시 정상(발화 검출, prob 0.5–0.97) 확인.

### 문제 3: torchaudio DLL 로드 실패

**증상**: `import silero_vad`/`torchaudio`가 `_torchaudio.pyd` 로드 오류.
**해결**: torch/torchaudio 우회, Silero VAD를 `silero_vad.onnx` + onnxruntime로 직접 구동(GPU 없는 환경에 더 안전).

---

## 📊 DoD 체크리스트

로드맵 M4의 Definition of Done:

- [x] openWakeWord로 오탐 0회 호출어 최소 1개 확보 (alexa)
- [x] Silero VAD 발화 종료 판정이 육안 판단과 500ms 이내 일치 (종료=마지막 발화 프레임, 해상도 32ms)
- [ ] 3시간 환산 오탐률 실측 및 임계치 판정 (실습 3 — 다음 세션)
- [ ] TTS 재생 중 wake 이벤트 0건 검증 (실습 4 — 다음 세션)
- [x] README 작성 완료
- [x] WorkLog 작성 완료

**완료율**: 4/6 — 실습 3·4(에코·오탐률 30분 녹음)는 다음 세션

---

## 💡 Daily Retrospective

### What went well (잘된 점)
- 실시간 감지가 안 될 때 사용자 탓으로 넘기지 않고 `mic_check.py`로 파이프라인을 격리 진단해 진짜 원인(버퍼링·타이밍, 이후 VAD context)을 찾았다
- 두 버그(키 불일치, context prepend)를 공식 소스 확인으로 근거 있게 고쳤다

### What could be improved (개선할 점)
- Silero VAD를 스모크 테스트할 때 "돌아가는지"만 보고 "실제 음성에 높은 확률이 나오는지"를 확인 안 해 한 바퀴 돌았다 — 앞으로 신호 처리 모듈은 **양성 신호(실제 음성)로 검증**해야 한다
- 로그 정리 중 `--seconds 0.1`로 vad_record.wav를 실수로 덮어써 정본 wav를 잃음(측정값은 로그로 보존). 파괴적 명령 전 확인 필요

### Insights (인사이트)
- 실측 모듈의 핵심 교훈: **백그라운드 실행은 라이브 피드백이 없으니, 고정 창 녹음→오프라인 채점이 결정론적이고 재현 가능**하다. 이 패턴을 M5(STT WER)·M6(TTS)에도 재사용한다
- alexa가 6ms로 실시간 여유가 큰 건 좋은 신호지만, 진짜 결정은 3시간 오탐률(실습 3) — 그때 한국어 학습 vs 핫키를 판단

### Tomorrow's focus (다음에 할 것)
- 실습 3: `wake_probe.py --mode falsepos --seconds 1800`로 30분 배경(타이핑·잡담·BGM) 녹음 → 3시간 환산 오탐률 → `guides/false-positive-report.md`
- 실습 4: TTS 재생 중 스피커로 호출어 재생 → wake 게이트 폐쇄로 감지 0건 검증 → `troubleshooting/echo-loop-notes.md`
- 두 실습 완료 시 M4 DoD 6/6 → M5(STT + 멀티 LLM 하네스)

---

## 📎 참조 및 산출물

**생성된 파일/폴더**:
- `04-WakeWord-VAD-Harness/concepts/wake-vad-concepts.md`: 개념
- `04-WakeWord-VAD-Harness/examples/wake_probe.py`: openWakeWord 프로브(record/detect/falsepos)
- `04-WakeWord-VAD-Harness/examples/vad_probe.py`: Silero VAD 프로브(ONNX 직구동, context prepend)
- `04-WakeWord-VAD-Harness/examples/mic_check.py`: 마이크·감지 격리 진단 도구
- `04-WakeWord-VAD-Harness/examples/probe_log.jsonl`: 실습 1 감지 23건 + 실습 2 발화 7건
- `04-WakeWord-VAD-Harness/README.md`: 모듈 개요·결과·함정 정리

**참조 자료**:
- [openWakeWord](https://github.com/dscripka/openWakeWord), [Silero VAD](https://github.com/snakers4/silero-vad)
- Silero `OnnxWrapper` 소스(context prepend 확인): `silero_vad/utils_vad.py`
- M3: `session_state.schema.json`의 `wake_gate` 필드(실습 4에서 검증)

**다음 세션 준비사항**:
- 실습 3은 30분 배경 녹음 필요(조용한 작업 환경) — `falsepos` 모드는 실시간이므로 사용자가 직접 실행하거나 record로 30분 녹음 후 오프라인 채점

---

**작성자**: solkit70
**방법론**: VibeLearn AI
