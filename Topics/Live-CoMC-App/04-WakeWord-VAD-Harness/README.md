# M4 — Wake Word / VAD 하네스

**상태**: ✅ 완료 (실습 1~4)
**예상 학습 시간**: 7h
**Topic**: [[../topic_starter|Live-CoMC-App]]

---

## 이 모듈에서 배우는 것

파이프라인 ①Wake·②VAD 관문을 실제 마이크로 측정한다. 호출어를 안정적으로 감지하는가(오탐), 발화 종료 시점을 정확히 아는가(VAD), 그리고 TTS 에코 루프를 차단하는가. **실측 하네스 단계**의 첫 모듈이라 사용자가 직접 발화·녹음하고, 프로브 스크립트가 이를 측정한다.

## 문서 목록 (학습 순서)

1. [concepts/wake-vad-concepts.md](concepts/wake-vad-concepts.md) — 오탐·에코 루프·VAD 무음 임계값 + **커스텀 호출어의 현실**(사전학습 vs 학습)
2. [examples/wake_probe.py](examples/wake_probe.py) — openWakeWord 감지 프로브. `record`(녹음→오프라인 채점)/`detect`/`falsepos` 모드
3. [examples/vad_probe.py](examples/vad_probe.py) — Silero VAD 발화 구간 검출(ONNX 직구동, torch 우회)
4. [examples/echo_probe.py](examples/echo_probe.py) — 에코 루프 차단(`wake_gate`) 검증 프로브. `echo`/`reopen`/`level` 모드
5. [examples/mic_check.py](examples/mic_check.py) — 마이크 캡처+오프라인 감지 진단 도구
6. [examples/probe_log.jsonl](examples/probe_log.jsonl) — 감지·발화·에코 측정 로그
7. [guides/false-positive-report.md](guides/false-positive-report.md) — **3시간 환산 오탐률과 판정** (실습 3)
8. [troubleshooting/echo-loop-notes.md](troubleshooting/echo-loop-notes.md) — **에코 루프 차단 검증 + 하네스 함정 4건** (실습 4)

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

**실습 3 — 3시간 환산 오탐률 (30분 record)** → 상세: [guides/false-positive-report.md](guides/false-positive-report.md)

| 지표 | 값 |
|---|---|
| 30분 감지 / 3시간 환산 | **0회 / 0회** ⚠️ **환산값 — 실측과 다름** |
| **3시간 실측 (2026-09-06 추가)** | **`alexa` 1회** · `hey_jarvis` 0회 · `hey_mycroft` 0회 → [리포트](../10-Live-Rehearsal-Capstone/guides/false-positive-measured.md) |
| 최대 점수 | **0.1953** (임계값 0.5의 39%) |
| p99.9 / 중앙값 | 0.0007 / 0.00000 |
| 측정 환경 활동량 | 프레임 31.7%가 RMS>1000 (무음 아님) |

0회가 "운"이 아님을 두 가지로 확인했다 — 환경이 무음이 아니었고(활동 31.7%), 30분 전체에서 **0.2를 넘은 프레임이 하나도 없었다**(임계값까지 2.6배 여유).

**실습 4 — 에코 루프 차단** → 상세: [troubleshooting/echo-loop-notes.md](troubleshooting/echo-loop-notes.md)

| 조건 | 재생 구간 감지 | 억제 |
|---|---:|---:|
| `--gate off` (기준선) | **5건** | 0 |
| `--gate on` | **0건** ✅ | **5건** |

재생 종료 + hangover 200ms 이후 14.18s·17.46s에서 감지가 재개되어 게이트 재개방도 확인(DoD "500ms 이내" 충족). M3 계약 `session_state.wake_gate`의 첫 실측 검증이다.

**한계**: MV7이 지향성 다이나믹 마이크라 스피커 소리를 3.7%로만 받아 **음향 에코 경로 자체는 이 볼륨에서 재현되지 않았다.** 양성 신호는 TTS 재생 중 사용자가 직접 호출어를 발화해 주입했다. 게이트 정책은 검증됐지만 음향 재현은 낮 시간대 보완 측정이 필요하다. 한편 이 낮은 수음률은 **물리적 2차 방어선**이라는 부수 발견이기도 하다.

## 발견한 함정 (troubleshooting 가치)

**1차 세션 (실습 1·2)**

1. **openWakeWord 키 불일치**: `Model()`이 `wakeword_models` 리스트를 전체 경로로 in-place 변형하지만, `predict()`는 짧은 이름으로 키를 반환 → 카운트 딕셔너리 KeyError. `list(oww.models.keys())`로 키를 가져와 해결.
2. **Silero VAD context prepend 누락**: v5 ONNX는 512샘플 앞에 **64샘플 context를 붙여 총 576샘플**을 입력해야 함. 512만 넣으면 에러 없이 speech 확률이 항상 ~0. 공식 OnnxWrapper대로 context 유지 추가해 해결.

**2차 세션 (실습 3·4)** — 상세: [troubleshooting/echo-loop-notes.md](troubleshooting/echo-loop-notes.md)

3. **`sd.rec()` + `sd.play()` 충돌**: 두 편의 함수가 모듈 레벨 스트림을 공유해 재생이 녹음을 중단시킨다. 에러 없이 녹음본이 "재생 시작 클릭 한 번 + 무음"이 되고 peak는 92%로 찍혀 정상처럼 보인다. → 입력은 명시적 `InputStream(callback=)`으로 분리.
4. **입력 스트림 `read()` 지연 ~7초**: 실시간 루프로 채점하면 이벤트 시각이 통째로 밀린다. → 고정 창 녹음 → 오프라인 채점.
5. **출력 장치 오픈 지연 4~9초**: `sd.play()` 호출과 실제 소리 사이 간격이 크고 가변적이라 시각 기반 정렬이 불가능. → **1kHz 비프 마커**를 앞에 붙여 정렬.
6. **장치 인덱스 불안정** ← 가장 위험: 한 세션에서 MV7이 `1→22→3→1`로 바뀜. 번호 하드코딩은 조용히 다른 마이크로 측정된다. → 이름으로 검색하고 16kHz 지원까지 확인하는 `resolve_device()`를 `echo_probe.py`·`wake_probe.py`에 도입.

**방법론 인사이트**: 백그라운드 실행 시 stdout 버퍼링으로 라이브 피드백이 안 보여 실시간 감지가 타이밍에 취약했다. **고정 창 녹음 → 오프라인 채점**(record 모드)으로 바꾸니 결정론적이고 재현 가능해졌다. 2차 세션의 함정 3·4도 결국 같은 처방으로 해결됐다 — **실시간성이 필요 없는 측정은 항상 녹음 후 채점**이 옳다. `mic_check.py`(녹음+오프라인 감지)가 파이프라인 정상 여부를 격리 진단하는 데 결정적이었다.

**측정 설계 인사이트**: 차단을 검증할 때는 **끈 상태(기준선)를 반드시 함께 잰다.** 게이트를 켜고 0건이 나오는 것만으로는 아무것도 증명되지 않는다 — 신호가 애초에 안 닿아도 0건이기 때문이다. `echo_probe.py`는 `--gate off`에서 0건이면 실험 무효라고 경고하며, 이 경고 덕분에 초반 무효 측정 4회를 "차단 성공"으로 오기록하지 않았다.

## 핵심 결론 (다음 단계로 넘어가는 것)

- **wake word 방식은 기술적으로 성립한다** — 오탐 여유 2.6배, 실시간 여유 12배(6.39ms / 80ms). 한국어 커스텀 호출어 학습에 투자할 근거가 확보됐다. 핫키 전용 전환은 보류.
- **`alexa`는 측정용이지 실사용 호출어가 아니다** — AI 방송에서 자연 발화될 수 있어, 원 목표인 "코엠씨"가 조건에 더 맞는다. 이번에 검증된 것은 단어가 아니라 **openWakeWord 방식의 오탐 특성과 하네스**다.
- **VAD 무음 임계값은 튜닝 파라미터** — 명령용 800ms / 질문용 2000ms, 앱에서 상황별 조정 or LLM 병합.
- **`session_state.wake_gate`(M3 스키마) 런타임 차단 검증 완료** — M7 Co-MC 엔진에서 TTS 재생 파이프라인에 실제로 연결한다.

## 검증 방법

장치 인덱스가 불안정하므로 **번호 대신 이름**으로 지정한다.

```powershell
cd 04-WakeWord-VAD-Harness/examples
python wake_probe.py --list-devices                                    # 장치 확인
python wake_probe.py --mode record --seconds 100  --device "MV7"       # 실습 1
python vad_probe.py  --mode record --seconds 25   --device N           # 실습 2
python wake_probe.py --mode record --seconds 1800 --device "MV7" --models alexa   # 실습 3
python echo_probe.py --make-tts                                        # 실습 4 준비
python echo_probe.py --mode echo --gate off --device "MV7" --output-device "Speaker (Realtek"
python echo_probe.py --mode echo --gate on  --device "MV7" --output-device "Speaker (Realtek"
```

## 다음 모듈

M4 완료 → **M5 - STT + 멀티 LLM 하네스**

이월 과제 (M4 보완, M5와 병행 가능):
- [x] ~~과거 라이브 방송 3시간 오디오를 오프라인 채점해 **환산이 아닌 실측 오탐률** 확보~~
  → ✅ **2026-09-06 해소. 그리고 환산값이 틀렸다.**
  `AIInAction_20260724_full.mp4` **183.7분 실측** 결과 `alexa` **1회 오탐**(score 0.595 · 2시간 13분 지점).
  `hey_jarvis`·`hey_mycroft` 는 0회. **30분 창에서 0회였다고 3시간에 0회인 것이 아니었다** —
  아래 「3시간 환산 오탐률」 표의 *"0회 / 0회"* 는 **환산값이며 실측과 다르다.**
  대책 후보: ①`hey_jarvis` 단일 모델(실측 0회) ②임계값 0.6. 감지율 재측정이 선행돼야 한다.
  → 전문: [3시간 실측 리포트](../10-Live-Rehearsal-Capstone/guides/false-positive-measured.md)
  → 도구: `python wake_probe.py --mode file --audio "<파일>"` (2026-09-06 추가, 마이크 불필요)
- 낮 시간대 방송 볼륨으로 **음향 에코 경로** 보완 측정
- MOTIV Mix 라우팅 활성화 후 디지털 루프백 회귀 테스트

← 이전: [M3 - 데이터 계약과 안전 정책 스펙](../03-Data-Contracts-and-Safety/README.md)

## 호스트 API 선택 규칙 (2026-08-31 추가)

Windows 는 **같은 물리 장치를 MME · DirectSound · WASAPI · WDM-KS 로 중복 열거**한다.
이름만 맞춰 첫 매칭을 집으면 대개 **MME** 가 걸리는데, 지연이 가장 크다.

| 상황 | 규칙 |
|---|---|
| **지연이 중요한 경로** | **WASAPI 를 명시 선택한다.** 없으면 그때 폴백 |
| 단순 존재 확인 | 아무거나 무방 |

실측 근거 — 같은 VB-CABLE 을 방식만 바꿔 재생 지연을 재면:

| 경로 | 지연 |
|---|---:|
| MME + `sd.play` | **314ms** (M6 최초 실측) |
| WASAPI + `sd.play` | 124ms |
| WASAPI + 저지연 스트림 | **63ms** |

> 이 규칙이 없어서 M6 의 케이블 지연이 **5배 과대 측정**됐다.
> → [정정 실측](../09-Desktop-Shell-and-Overlay/guides/panic-stop-benchmark.md)
