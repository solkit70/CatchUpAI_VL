# Live-CoMC-App — 라이브 방송 보조 MC 앱

> **근거의 종류를 밝히고 말하는 AI 공동 MC.** 매주 일요일 Seattle 현지 05:00 「AI in Action Live」에서 Rundown을 우선 확인하고, 지난 볼트 기록·공개 웹 검색·명시적으로 요청한 가상 이야기를 구분해 답한다. M1~M10의 방송 진행 계약에 M11 근거 확장을 연결한 프로젝트형 Topic이다.

| | |
|---|---|
| 기간 | 2026-08-02 시작 → 2026-09-17 M1~M10 마감 → 2026-10-01 M11 근거 확장 |
| 상태 | M1~M10 · CVL1~4 완료. M11 구현·자동 및 실제 LLM 검증 완료, 진행자 콘솔·라이브 확인 대기 |
| 실전 투입 | Live #26·#27 화면 리허설 → Live #28(9/20) 음성 첫 실전 → Live #29(9/27) 두 번째 음성 방송 |
| 한 줄 결과 | 화면·음성 공동 MC에 Rundown·볼트·웹·창작을 연결했다. 새 답변 경로는 출처를 표시하고 승인 뒤 발화한다. 음성 입력(C)은 아직 별도 검증 대상 |

## M11 — 답변 근거 확장 (2026-10-01)

CVL8은 비공개 금칙 목록으로 검색 근거·질문·최종 발화를 검사하며, Journal·Roundup 출처의 승인 대기 답에는 콘솔 경고와 파일·섹션을 표시한다. 개인 기록 검색과 기존 승인 흐름은 유지한다. → [CVL8 기록](vl_worklog/20261002_CVL8_Live-CoMC-App.md#📚-진행-내용)

Rundown → 비공개 로컬 볼트 색인 → Tavily 공개 웹 검색의 자동 선택과 수동 선택을 구현했다. 창작은 명시적으로 요청할 때만 허용하며, 볼트·웹·창작 답변은 LIVE 모드에서도 승인 대기로 보내고 진행자가 확인한 뒤 발화한다. 현재 파트 권위값, 미편성 내용 제외, 숫자·고유명사·인용 검증을 유지한다.

콘솔을 재시작하면 질문란 아래 **답변 근거** 선택 칸과 **볼트 색인 갱신** 버튼이 보인다. 결과에는 경로 배지와 출처 파일의 섹션 또는 URL이 나오며, 새 기록을 반영하려면 색인을 갱신한다. 구현은 [evidence_lanes.py](07-CoMC-Engine-POC/src/evidence_lanes.py), 검증은 [M11 테스트](07-CoMC-Engine-POC/tests/test_evidence_lanes.py)와 [개발 WorkLog](vl_worklog/20261001_M11_Live-CoMC-App.md)에 있다.

색인·질문별 근거·Tavily 설정은 Git에서 제외되는 `07-CoMC-Engine-POC/output/private/m11/`에만 둔다. 내부 자료와 민감한 개인 일은 검색에서 제외하며, 구현·자동 및 실제 LLM 검증 뒤 진행자의 콘솔·음성 확인과 다음 라이브 검증이 남아 있다. 개발 순서는 M11 → 시청자 이름·참여 기록 → Persona이며, 기존 CVL5 사고 손질은 뒤로 미룬다.

## 시청자 이름 기억과 참여 기록 (CVL6 · 2026-10-01)

콘솔의 「시청자 · 이번 회차 참여 기록」에서 표시 이름을 한 번 등록한 뒤 선택해서 인사한다. 쉼표로 여러 명을 추가하고 방송 날짜를 확인·수정할 수 있으며, 회차별 명단은 재시작 후에도 유지된다. 이전 회차 참여 횟수와 다시 온 분 표시, 전체 참여자의 처음·마지막 회차, 이름 수정·삭제·음성용 읽는 법을 지원한다. 인사 대상이 많으면 최대 네 명씩 묶어 하나씩 진행한다.

✓ 인사 완료는 실제 재생이 정상 종료된 뒤에만 표시한다. 명단은 `output/private/viewers/roster.json`, 이름이 포함되는 런타임 파일과 오디오는 `output/private/runtime/`에 저장한다. 자동·브라우저·실제 LLM 검증을 마쳤고 실제 출력 장치와 다음 라이브 확인은 남아 있다. → [운영 가이드](10-Live-Rehearsal-Capstone/guides/operator-guide.md#시청자-명단과-참여-기록-cvl6--2026-10-01) · [CVL6 WorkLog](vl_worklog/20261001_CVL6_Live-CoMC-App.md). 다음 개발은 Persona 선택이다.

## Persona 선택 (CVL7 · 2026-10-01)

콘솔의 「AI 코엠씨 · Persona」에서 기본 말투와 하늘(고등학생), 다온(아나운서 지망 대학생), 서연(프로 아나운서), 지우(친구)를 선택한다. 다음 질문부터 말투와 음성 설정이 바뀌며 선택은 재시작 후에도 유지된다. 답변 생성 중 바꿔도 기존 초안·승인 대기 음성은 생성 당시 캐릭터를 유지하고 콘솔 결과와 자막에 그 이름을 표시한다. → [정의 JSON](07-CoMC-Engine-POC/data/personas.json) · [운영 가이드](10-Live-Rehearsal-Capstone/guides/operator-guide.md#persona-선택-cvl7--2026-10-01)

캐릭터는 AI 공동 진행자의 가상 설정이다. 친구가 진행자의 과거 이야기를 할 때는 실제 볼트 기록만 사용하며, 기존 사실·인용·길이·민감 정보 제외 검사는 유지하고 실존 인물 행세와 공동 경험 주장 검사를 추가했다. 선택·답변 생성·재생 완료와 회차별 반응 메모는 `output/private/personas/state.json`에 남긴다. 구현·자동·브라우저·실제 LLM 비교·한국어와 영어 합성을 검증했으며, 자연스러움과 목소리 적합성은 진행자의 실제 청취 확인이 남아 있다. → [CVL7 WorkLog](vl_worklog/20261001_CVL7_Live-CoMC-App.md)

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

✅ CVL 1·2 (09-17) 로 ①②③ 완료 — [사고 7~11 수정](10-Live-Rehearsal-Capstone/guides/incident-classification.md) · [`spoken_player.py`](09-Desktop-Shell-and-Overlay/examples/engine/spoken_player.py) · [4회차](10-Live-Rehearsal-Capstone/guides/rehearsal-log-4.md). CVL 3 (09-17 밤) 로 창 4개 → [콘솔 하나](09-Desktop-Shell-and-Overlay/examples/engine/comc_console.py) + [조작 가이드](10-Live-Rehearsal-Capstone/guides/operator-guide.md). CVL 4 (09-17 밤) 로 두 번째 근거 풀 [캐주얼 브리프](07-CoMC-Engine-POC/src/02b_build_casual_brief.py) — 날씨·이번 주 한 일·인사이트·자리 비움 진행(≈50초)·시청자 언급·영어 답변 ([게이트 규칙 차이](08-Safety-Gate-Scenarios/guides/verification-rules.md)). Live #28(09-20)과 Live #29(09-27) 음성 실전을 거쳤다. 현재 개발은 M11 근거 확장 → 시청자 참여 기록 → Persona 순이며 C(음성 입력)는 별도 후속 대상이다.

## 기록

- 로드맵: [`vl_roadmap/20260802_RoadMap_Live-CoMC-App.md`](vl_roadmap/20260802_RoadMap_Live-CoMC-App.md)
- WorkLog 14편 + Retrospective: [`vl_worklog/`](vl_worklog/) — 특히 [Final Retrospective](vl_worklog/20260912_Live-CoMC-App_Final_Retrospective.md)(방법론 평가 · 인사이트 6 · 개선 제안 5)
- Topic 시작: [`topic_starter.md`](topic_starter.md)
- WorkLog 5편이 더 붙었다 (09-17 M10c · CVL 1~4) — 하루의 이야기는 [`vl_materials/2026-09-17 CoMC 하루 개발 기록 — 발표·영상용.md`](vl_materials/2026-09-17%20CoMC%20하루%20개발%20기록%20—%20발표·영상용.md) (발표 3막 · 데모 시나리오 · 숫자 한 장)
- 참고 영상: [`vl_materials/2026-09-29 참고 영상 — AI 와 함께 진행하는 라이브 방송 (hu-po).md`](vl_materials/2026-09-29%20참고%20영상%20—%20AI%20와%20함께%20진행하는%20라이브%20방송%20(hu-po).md) — 음성 AI 를 공동 진행자로 둔 1시간 51분 라이브. 진행 위치 착각 · 엉뚱한 모델과 대화 · 채움 말 · 추측 금지 등 CoMC 에 참고할 8가지
- `vl_materials/` 의 다른 재료는 볼트의 실제 Rundown 16편(`AI/Roundup/*Weekly Rundown.md`, 비공개)이라 레포에 두지 않았다. `06-…/examples/audio/` 는 실측 오디오라 gitignore.
