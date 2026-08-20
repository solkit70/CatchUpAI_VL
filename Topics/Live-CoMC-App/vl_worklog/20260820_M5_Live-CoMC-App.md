---
title: "WorkLog - M5: STT + 멀티 LLM 하네스"
created: 2026-08-20 06:30:00
tags:
  - worklog
  - live-comc-app
---

## 세션 정보

**날짜**: 2026-08-20
**Topic**: Live-CoMC-App
**모듈**: M5 - STT + 멀티 LLM 하네스
**이전 세션**: [20260815_M4_Live-CoMC-App.md](20260815_M4_Live-CoMC-App.md)

## 🎯 오늘의 학습 목표

- [x] 실습 4 — 3사 API 프리플라이트
- [x] 실습 3 — LLMProvider 어댑터 (M3 설계의 코드 구현)
- [x] 실습 1 — 한국어 전사 정확도 실측
- [x] 실습 2 — STT 3단 폴백

Roadmap 순서(1→2→3→4) 대신 **사용자 참여가 필요 없는 실습 4·3을 먼저** 하고,
녹음이 필요한 실습 1·2를 뒤로 돌렸다. 8/15 WorkLog의 "Tomorrow's focus"에 적어둔 판단대로다.

## 📚 진행 내용

### 1. 실습 4 — 프리플라이트

`llm_probe.py`. 환경 변수 → `models.list()` → 모델 해석 순서로 점검하고,
사용 불가 프로바이더를 `llm_registry.runtime.json`의 `fallback_order`에서 빼는 구조로 만들었다.

처음에는 목록 조회만으로 만들었는데 **아무것도 못 잡았다**. 스모크 콜(최소 토큰 실제 호출)을
추가하고 나서야 두 가지가 드러났다. 아래 문제 해결 로그 1·2 참조.

강제 실패 테스트(`--simulate-fail claude`)에서 폴백 순서가 `claude → openai → gemini`에서
`openai → gemini`로 축소되는 것을 확인했다. 실습 4 검증 기준 충족.

### 2. 실습 3 — LLMProvider 어댑터

M3 `llm-schema-normalization.md`의 이중 검증 구조를 그대로 구현했다.

```
프로바이더 구조화 출력  =  "대략 맞게 유도"   (각 사가 받는 서브셋으로 다운그레이드)
어댑터 뒤단 재검증      =  "합격/불합격 판정"  (answer_draft.schema.json)
```

프로바이더별 스키마 처리가 실제로 달랐다.

| | 방식 | 스키마 처리 |
|---|---|---|
| Claude | strict tool use + `tool_choice` | `minimum`/`maxLength` 계열 제거 |
| OpenAI | `response_format=json_schema(strict)` | 전 필드 `required` 강제 |
| Gemini | `responseSchema` | `additionalProperties` 제거 |

**`provider`와 `created_at`을 프로바이더 스키마에서 미리 빼는 것이 선택이 아니라 필수였다.**
OpenAI strict는 전 필드 required를 요구하는데, 모델이 채울 수 없는 값(수신 시각, 자기 이름)을
required로 요구받으면 실패한다. M3 매핑 표에 "어댑터가 주입"이라고 적혀 있던 이유가 여기서 드러났다.

결과: 3사 모두 동일한 `answer_draft` 계약으로 수렴. 근거 대조(evidence_pool 문자열 확인)도 3사 통과.

문체는 뚜렷하게 갈렸다. Claude는 담백하고 짧다. OpenAI는 두 문장으로 합쳐 길다.
Gemini는 `네,` `~고요` 같은 구어체가 많고 **숫자를 "마흔두 개"로 읽는다** — TTS로 넘길 때 유리한 특성이다.
M6에서 TTS 라우팅을 할 때 이 차이가 실제로 영향을 준다.

### 3. 실습 1 — 한국어 전사 정확도

20문장(질문형 10 + 명령형 10)을 만들어 MV7으로 녹음하고 `gpt-4o-transcribe`로 전사했다.
문장 세트는 **일부러 어렵게** 구성했다 — 영어 기술 용어를 한국어 문장에 섞고, 호출어를 넣고, 숫자를 넣었다.

```
전체 WER 23.3%   CER 16.7%   평균 지연 1,160ms
```

상세는 [stt-wer-report.md](../05-STT-LLM-Harness/guides/stt-wer-report.md).

### 4. 실습 2 — STT 3단 폴백

```
정상        gpt-4o-transcribe   1,160ms
1단 실패    gpt-transcribe      1,547ms
1·2단 실패  로컬 whisper(small) 6,051ms
```

전 단계 자동 전환 확인. 로컬 폴백은 GPU가 없어 CPU 추론이라 5배 느리다 — 최후 수단인 이유가 수치로 확인됐다.

## 🐛 문제 해결 로그

### 문제 1: `models.list()`에 있다고 호출 가능한 게 아니다 ← 가장 중요

프리플라이트를 목록 조회만으로 만들었더니 3사 모두 "정상"으로 나왔다. 그런데 실제 호출은 두 곳이 실패했다.

- **Claude**: 키 유효, `models.list()` 성공, 그런데 생성 호출만 400
  `"Your credit balance is too low to access the Anthropic API"`
- **Gemini**: `gemini-2.5-pro`가 목록에는 있으나 호출하면 404
  `"no longer available to new users"`

목록 조회는 **인증만** 검증하고 모델 접근 권한은 검증하지 못한다.
최소 토큰 스모크 콜을 추가해서야 둘 다 잡혔다. 방송 중에 만났으면 늦었을 문제다.

Claude 쪽은 **Roadmap M5 주요 개념 3번("소비자 구독 ≠ API 접근권")의 실제 사례**였다.
개념으로 읽을 것을 실측으로 만난 셈이다.

### 문제 2: google-genai 클라이언트를 함수마다 만들면 죽는다

`Cannot send a request, as the client has been closed`. 목록 조회 함수가 만든 클라이언트가
GC될 때 공유 전송 계층을 닫아서, 이후 스모크 콜이 새 클라이언트를 만들어도 실패했다.
프로세스당 하나로 재사용하도록 고쳤다.

### 문제 3: Roadmap의 STT 1단계 모델이 존재하지 않는다

`gpt-live-transcribe`는 `POST /v1/audio/transcriptions`에 없다(404 "Invalid URL").
Realtime API(WebSocket) 전용이라 파일 전사로는 쓸 수 없다.

사다리를 `gpt-4o-transcribe → gpt-transcribe → 로컬 whisper`로 교정했다.
원래 모델의 한국어 정확도는 실시간 경로에서 따로 재야 한다 → **M7 과제**.

### 문제 4: API 키를 채팅에 붙여넣으면 폐기된다

진행자가 Anthropic 키를 채팅에 직접 붙여넣었고, 그 키는 이후 `AuthenticationError: API key is invalid`로 바뀌었다.
Anthropic이 유출 키를 자동 폐기한 것으로 보인다. 새 키를 환경 변수로 설정해 해결.
**키는 파일이나 채팅이 아니라 환경 변수로만 다룬다** — 이 저장소는 GitHub 공개다.

## 📊 DoD 체크리스트

- [x] 한국어 WER 실측 완료 (일반 조건)
- [~] BGM 조건 — **N/A**. 아래 Insights 참조
- [x] STT 3단 폴백이 강제 실패 테스트에서 정상 동작
- [x] LLMProvider 어댑터로 3사 모두 같은 스키마 응답 확보
- [x] 스키마 위반 시 재시도 → 폴백 로직 검증
- [x] API 키 유효성 프리플라이트 함수 동작 확인
- [x] README 작성 완료
- [x] WorkLog 작성 완료

## 💡 Daily Retrospective

### What went well (잘된 점)

- M3 설계 문서가 충분히 구체적이어서 어댑터 구현이 막히지 않았다. 3사 비교표와 매핑 규칙이
  그대로 코드가 됐다. **설계에 시간을 쓴 것이 여기서 회수됐다**
- 실습 순서를 사용자 참여 여부로 재배열한 것이 맞았다. 녹음을 기다리는 동안 어댑터를 완성했다
- WER과 CER을 함께 재기로 한 결정이 결정적이었다. 하나만 봤으면 정반대 결론을 냈다

### What could be improved (개선할 점)

- 프리플라이트를 처음에 목록 조회만으로 만든 것. "확인했다"는 착각을 주는 검증이 가장 위험하다.
  **무엇을 검증하지 못하는지**를 먼저 적었어야 했다
- 폴백 테스트(`--limit 3`)를 돌리면서 전체 결과 파일을 덮어썼다. 부분 실행 결과와
  전체 실행 결과를 같은 파일에 쓴 설계 실수다
- 모델 ID를 레지스트리에 미리 적어 넣었는데 두 개가 이미 폐지된 것이었다.
  **추측한 ID를 적고 검증하는** 순서보다 **먼저 조회하고 적는** 순서가 맞다

### Insights (인사이트)

**호출어는 전사기로 풀 수 없다.** `코엠씨` 11문장 중 정확 전사 0건이고, 매번 다르게 쓴다
(외임씨·포엠씨·QM씨·구MC…). 다른 전사기도 마찬가지였다(오엠씨·MC·우엠씨).
사전에 없는 신조어라 어떤 모델도 안정적으로 복원하지 못한다.
→ **호출어 감지는 STT 이전 단계에서 끝나야 한다.** M4에서 만든 openWakeWord 경로가
여러 대안 중 하나가 아니라 유일한 길이었다.

**오류율은 다음 단계가 무엇이냐에 따라 다르게 읽어야 한다.** `GitHub → 깃허브`,
`After Effects → 애프터이펙트`는 알아듣지 못한 게 아니라 한글로 적은 것이다.
표기를 허용하면 CER이 16.7% → 8.6%로 절반이 되고, 가장 나빠 보이던 두 문장(09·05)은
**실제로는 완벽 전사**였다. 전사문을 화면에 띄운다면 원본 기준이 맞고,
LLM에 넘긴다면 표기 허용 기준이 실질이다. 이 파이프라인은 후자다.

**BGM 조건은 이 셋업에서 의미가 없다.** 진행자가 BGM을 헤드폰으로 듣기 때문에
마이크에 들어가지 않는다. Roadmap의 요구사항은 스피커 셋업을 가정한 것이라 그대로 따르면
오히려 틀린 측정이 된다. 다만 **악조건 커버리지가 빈 것은 아니다** — 이 파이프라인에서
마이크에 실제로 섞이는 소리는 BGM이 아니라 AI 자신의 TTS 출력이고, 그건 M4에서 이미 측정했다.
소음원이 다를 뿐이다.

**병목은 STT가 아니라 LLM이다.** STT 1.2초 대 LLM 10.8~21.6초.
전체의 90% 이상이 ⑥ 단계에 있다. 지연 대책을 STT에 쓰면 헛수고다.

**진행자 제안 — 대기 필러의 안전 제약.** 응답을 기다리는 동안 미리 준비한 말을 하게 하자는
제안이 나왔다. 방향은 맞지만 **문구가 안전 설계와 충돌할 수 있다.**
파이프라인은 ⑥ LLM → ⑦ 안전 게이트 순서이고 ⑦이 차단하는 것이 정상 동작인데,
"질문에 답변 드릴게요"가 먼저 나가면 지키지 못할 약속이 된다.
시청자에게는 침묵보다 나쁘게 읽힌다.
→ **확인은 약속하되 답변은 약속하지 않는** 문구여야 한다
(`"네, 확인해 볼게요"` ○ / `"답변 드릴게요"` ×).
차단됐을 때의 후속 문구(`"그건 근거를 못 찾았습니다"`)도 함께 준비돼야 한다.
트리거 시점·중복 방지·문구 변형은 M6 오디오 라우팅에서 다룬다.
그리고 **필러는 지연을 감출 뿐 줄이지 않는다** — 지연 자체를 줄이는 실험이 따로 필요하다.

### Tomorrow's focus (다음에 할 것)

- **LLM 지연 원인 분석** — 3사 모두 기본 추론이 켜진 상태로 보인다. effort를 낮추거나
  더 빠른 모델 티어로 내렸을 때 얼마나 줄어드는지 측정. M7 전제가 여기 달렸다
- **M6 진입** — 멀티 TTS 하네스 + 오디오 라우팅. 대기 필러 설계를 여기서 확정
- M4 이월(여전히 미완): 과거 라이브 3시간 오디오 오프라인 채점 → 환산이 아닌 실측 오탐률
- 호출어 재검토 — 사전에 있는 단어로 바꾸면 전사는 되지만 오탐이 는다.
  M4 오탐률 측정을 다시 해야 판단 가능

## 📎 참조 및 산출물

**생성된 파일**

- `05-STT-LLM-Harness/README.md` — 모듈 학습 순서와 발견 6건
- `05-STT-LLM-Harness/guides/stt-wer-report.md` — **핵심 산출물**. 전사 정확도 실측 리포트
- `05-STT-LLM-Harness/guides/utterance-script.md` — 20문장 세트와 녹음 방법
- `05-STT-LLM-Harness/guides/llm_registry.json` — 3사 프로바이더 설정
- `05-STT-LLM-Harness/examples/utterances.py` — 정답 데이터 + 정규화
- `05-STT-LLM-Harness/examples/record_utterances.py` — 고정 창 녹음기
- `05-STT-LLM-Harness/examples/stt_probe.py` — 전사 + WER/CER + 3단 폴백
- `05-STT-LLM-Harness/examples/llm_probe.py` — 프리플라이트 (스모크 콜 포함)
- `05-STT-LLM-Harness/examples/llm_compare.py` — 3사 비교 + 폴백 데모
- `05-STT-LLM-Harness/examples/llm_providers/` — 어댑터 4종 (base + 3사)

**측정 로그**

- `examples/probe_log.jsonl` — `llm_preflight` / `llm_compare` / `llm_fallback` / `stt_wer` 이벤트
- `examples/stt_result_clean.json` — 문장별 WER·CER·지연
- `examples/utterances/clean/` — 녹음 원본 20 wav + manifest (3.8MB, git 미포함)

**다음 세션 준비사항**

- 지연 측정을 하려면 같은 프롬프트로 effort 수준별 스윕이 필요하다. `llm_compare.py`에
  `--effort` 옵션을 붙이면 된다
- M6는 TTS 출력이 스피커로 나가므로 **M4 에코 게이트를 켠 상태**에서 시작해야 한다

---

**작성자**: solkit70
**방법론**: VibeLearn AI
