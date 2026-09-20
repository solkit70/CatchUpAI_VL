# Live-CoMC-App — 라이브 방송 보조 MC 앱

> **Rundown 에 적힌 것만 근거로 말하는 방송 보조 MC.** 매주 일요일 05:00 PST 「AI in Action Live」에서 진행자 옆에 붙어, 그 주 Rundown 에 있는 내용만 화면(오버레이)과 — 다음 단계로 — 목소리로 답하는 앱을 VibeLearn AI 방법론으로 만든 프로젝트형 Topic 이다.

| | |
|---|---|
| 기간 | 2026-08-02 로드맵 → 2026-09-17 완료 (6주 반 · 14세션) |
| 상태 | ✅ **M1~M10 완료** · Retrospective 완결 · **CVL 1~4 (9/17)**: 사고 7~11 수정 · `spoken_player.py` · 무관중 4회차 사고 0 → **A GO · B 조건부 GO** · 진행자 UI = [브라우저 탭 하나](09-Desktop-Shell-and-Overlay/examples/engine/comc_console.py) · **코엠씨 캐주얼 레인** (주간 맥락·날씨·시청자 인사·영어) · 15개 언어 시그니처 끝인사 |
| 실전 투입 | Live #26(09-06, 리허설 1회차) · **Live #27(09-13, 3회차 실전 — REVIEW 모드)** |
| 한 줄 결과 | 「근거 없으면 말하지 않는다」를 지키는 엔진과 그것을 방송 화면에 띄우는 경로는 완성됐다. 목소리로 내는 경로(B)와 목소리로 묻는 경로(C)는 부품이 각각 검증된 채 아직 이어지지 않았다 |

## 무엇을 알아냈나

- **안전의 반대편은 무용함이다.** M1~M9 가 「틀린 말을 막는 것」을 완성하자, 캡스톤에서 **맞는 말도 못 하는 상태**(「내용 없는 발화」)가 드러났다. 로드맵의 사고 4유형에 없던 유형 2개(내용 없는 발화 · 운영 위험)를 추가했다 → [사고 유형 분류](10-Live-Rehearsal-Capstone/guides/incident-classification.md)
- **모듈별 통과의 합은 통합의 통과가 아니다.** 아홉 모듈이 각자 DoD 를 채웠지만 한 번도 같이 돈 적이 없었다 — `--live` 가 샘플에 고정(M7), `spoken.json` 을 읽는 코드가 없음(M9), 파트 전환이 컨텍스트를 안 만듦(M9). 셋 다 캡스톤에서 나왔다.
- **Rundown 의 품질이 곧 앱의 품질이다.** Live #27 사고 4건 중 3건의 뿌리는 코드가 아니라 입력 문서(확정/후보 구분 · 현재 상태 줄 · 파트 소속)였다. 진행자 소감: *"기능상으로는 OK, 내용상으로는 사전 작업에서 보완해야 할 점들이 많다."*
- **무료가 가장 빨랐다.** TTS 4사 첫 청크 실측에서 edge-tts 588ms 가 1위 — 로드맵의 「유료→무료 강등」 전제가 뒤집혔다 (M6).
- **호출어는 전사기로 풀 수 없다.** 신조어 호출어 전사 0/11 → 감지는 STT 이전에 끝나야 한다 (M5).
- **"느리다"의 원인은 계산이 아니라 연결이었다.** `OpenAI()` 를 매번 새로 만든 3초, 파이썬 기동 비용 — 상주 데몬으로 9,084 → 4,369ms (M9).

## 모듈 (학습 순서)

| # | 모듈 | 핵심 산출물 |
|---|---|---|
| 1 | [Concept and Rundown Contract](01-Concept-and-Rundown-Contract/README.md) | 커버리지 3상태(defined / undefined / conditional) · 금칙 섹션 규칙 · [문서 지도](01-Concept-and-Rundown-Contract/concepts/document-map.md) |
| 2 | [Architecture and Boundary](02-Architecture-and-Boundary/README.md) | [앱 경계 하드 게이트](02-Architecture-and-Boundary/guides/app-boundary.md) · 9단계 파이프라인 · 기술 선택 |
| 3 | [Data Contracts and Safety](03-Data-Contracts-and-Safety/README.md) | JSON 스키마 7종 + [`validate.py`](03-Data-Contracts-and-Safety/examples/validate.py) · `safety_policy.json` · [claim–evidence 모델](03-Data-Contracts-and-Safety/concepts/claim-evidence-model.md) |
| 4 | [WakeWord / VAD Harness](04-WakeWord-VAD-Harness/README.md) | openWakeWord · Silero VAD 하네스 · [오탐 리포트](04-WakeWord-VAD-Harness/guides/false-positive-report.md)(3시간 실측 1회) · [에코 루프 노트](04-WakeWord-VAD-Harness/troubleshooting/echo-loop-notes.md) |
| 5 | [STT / LLM Harness](05-STT-LLM-Harness/README.md) | STT 3사 CER 8.6% · [LLM 지연 스윕](05-STT-LLM-Harness/guides/llm-latency-sweep.md)(추론 토큰이 원인) · 어댑터 레지스트리 |
| 6 | [TTS / Audio Routing Harness](06-TTS-Audio-Routing-Harness/README.md) | [TTS 4사 비교](06-TTS-Audio-Routing-Harness/guides/tts-comparison.md) · [오디오 라우팅](06-TTS-Audio-Routing-Harness/guides/audio-routing-setup.md) · [운영 모드](06-TTS-Audio-Routing-Harness/guides/operating-modes.md) · 대기 필러 |
| 7 | [CoMC Engine POC](07-CoMC-Engine-POC/README.md) | 파일 기반 6단계 엔진 [`src/`](07-CoMC-Engine-POC/src/) (①파싱 → ②컨텍스트 → ③의도 → ④작성 → ⑤검증·게이트 → ⑥렌더) · [지연 리포트](07-CoMC-Engine-POC/guides/latency-report.md) |
| 8 | [Safety Gate Scenarios](08-Safety-Gate-Scenarios/README.md) | [검증 규칙 1~8](08-Safety-Gate-Scenarios/guides/verification-rules.md) · 시나리오 6종 · 결정적 테스트 9 · 파서 결함 5종(볼트 Rundown 16편 전수) · LIVE/REVIEW/MUTE |
| 9 | [Desktop Shell and Overlay](09-Desktop-Shell-and-Overlay/README.md) | [상주 데몬](09-Desktop-Shell-and-Overlay/examples/engine/engine_daemon.py) · [OBS 오버레이 서버](09-Desktop-Shell-and-Overlay/examples/engine/overlay_server.py) · 핫키 15개 · [패닉 스톱 112ms](09-Desktop-Shell-and-Overlay/guides/panic-stop-benchmark.md) |
| 10 | [Live Rehearsal Capstone](10-Live-Rehearsal-Capstone/README.md) | [프리플라이트 9항목](10-Live-Rehearsal-Capstone/examples/preflight_check.py) · 리허설 [1](10-Live-Rehearsal-Capstone/guides/rehearsal-log-1.md)·[2](10-Live-Rehearsal-Capstone/guides/rehearsal-log-2.md)·[3](10-Live-Rehearsal-Capstone/guides/rehearsal-log-3.md)회차 · [사고 분류 11건](10-Live-Rehearsal-Capstone/guides/incident-classification.md) · [**go / no-go 3갈래 판정**](10-Live-Rehearsal-Capstone/guides/go-nogo-decision.md) · [방송 중 허용 작업](10-Live-Rehearsal-Capstone/guides/what-can-run-during-broadcast.md) |

## 실전 결과 — Live #27 (2026-09-13)

REVIEW 모드(진행자 타이핑 → OBS 오버레이). 프리플라이트 PASS 7 · WARN 2 · FAIL 0. **시도 9 · 통과 6 · 침묵 3 · 사고 4건 · 방송 중 코드 수정 0 · 소리로 나간 오류 0.** LLM 완주 8회 4.4~7.3초.
사고 4건(확정/후보 혼동 · 내용 없는 발화 · 파트 오귀속 · 거절 시 옛 초안 재렌더)은 전부 화면에서 멈췄다 → [rehearsal-log-3](10-Live-Rehearsal-Capstone/guides/rehearsal-log-3.md) 「결과」.

**판정** (4회차 09-17 뒤 최종) — A 화면 보조: **GO, Live #28 부터 REVIEW 상시** · B 음성 출력: **조건부 GO** (재생기 · OBS 설정 · 글자 수 120 · LIVE 는 CoMC 구간만) · C 음성 입력: NO-GO → [go-nogo-decision](10-Live-Rehearsal-Capstone/guides/go-nogo-decision.md) · [rehearsal-log-4](10-Live-Rehearsal-Capstone/guides/rehearsal-log-4.md) · **[진행자 조작 가이드](10-Live-Rehearsal-Capstone/guides/operator-guide.md)**

## 틀렸던 판단 · 확인 못한 것

- **3회차 조건을 로드맵보다 높게 적어 놓고 일주일을 미뤘다** — WorkLog 가 「마이크 전 구간」을 요구했는데 로드맵 원문은 「동일 조건」이었다. 없는 요구사항에 일정을 뺏겼다 (M10b).
- **「M9 셸의 몫」이라는 주석이 6주 동안 아무도 안 읽은 계약이었다** — 위임은 받는 쪽 DoD 에 적혀야 계약이다.
- **실소요 시간을 안 적었다** — 계획 90h 대비 실제를 비교할 숫자가 없다 (14세션 중 4개만 기록). 방법론 개선 제안 1.
- ElevenLabs 미검증(키 없음) · Electron 셸 미착수 · 송출 트랙 뮤트 미검증 · 실제 방송 3시간 오디오 오탐 실측 1회뿐 — 전부 B·C 갈래로 이월.

## 다음 (CVL 유지보수)

✅ CVL 1·2 (09-17) 로 ①②③ 완료 — [사고 7~11 수정](10-Live-Rehearsal-Capstone/guides/incident-classification.md) · [`spoken_player.py`](09-Desktop-Shell-and-Overlay/examples/engine/spoken_player.py) · [4회차](10-Live-Rehearsal-Capstone/guides/rehearsal-log-4.md). CVL 3 (09-17 밤) 로 창 4개 → [콘솔 하나](09-Desktop-Shell-and-Overlay/examples/engine/comc_console.py) + [조작 가이드](10-Live-Rehearsal-Capstone/guides/operator-guide.md). CVL 4 (09-17 밤) 로 두 번째 근거 풀 [캐주얼 브리프](07-CoMC-Engine-POC/src/02b_build_casual_brief.py) — 날씨·이번 주 한 일·인사이트·자리 비움 진행(≈50초)·시청자 언급·영어 답변 ([게이트 규칙 차이](08-Safety-Gate-Scenarios/guides/verification-rules.md)). 다음은 **Live #28(09-20) 실전** — A·B 의 첫 방송 — 그 뒤 C(음성 입력).

## 기록

- 로드맵: [`vl_roadmap/20260802_RoadMap_Live-CoMC-App.md`](vl_roadmap/20260802_RoadMap_Live-CoMC-App.md)
- WorkLog 14편 + Retrospective: [`vl_worklog/`](vl_worklog/) — 특히 [Final Retrospective](vl_worklog/20260912_Live-CoMC-App_Final_Retrospective.md)(방법론 평가 · 인사이트 6 · 개선 제안 5)
- Topic 시작: [`topic_starter.md`](topic_starter.md)
- WorkLog 5편이 더 붙었다 (09-17 M10c · CVL 1~4) — 하루의 이야기는 [`vl_materials/2026-09-17 CoMC 하루 개발 기록 — 발표·영상용.md`](vl_materials/2026-09-17%20CoMC%20하루%20개발%20기록%20—%20발표·영상용.md) (발표 3막 · 데모 시나리오 · 숫자 한 장)
- `vl_materials/` 의 다른 재료는 볼트의 실제 Rundown 16편(`AI/Roundup/*Weekly Rundown.md`, 비공개)이라 레포에 두지 않았다. `06-…/examples/audio/` 는 실측 오디오라 gitignore.
