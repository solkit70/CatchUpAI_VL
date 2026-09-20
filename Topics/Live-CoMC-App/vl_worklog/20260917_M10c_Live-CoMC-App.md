---
title: "M10c — 3회차 결과를 적고 Topic 을 닫다 · 4회차는 CVL 로"
created: 2026-09-17 10:40:00
author:
  - "Claude Code"
topic: "Live-CoMC-App"
module: "M10"
tags:
  - vibelearn-ai
  - worklog
  - live-comc-app
---

## 세션 개요

| 항목 | 값 |
|---|---|
| 날짜 | 2026-09-17 (목) 10:05 ~ 10:40 — Live #27 나흘 뒤, Live #28 사흘 전 |
| 실소요 | 약 35분 (사용자 응답 대기 약 5분 포함 · LLM 호출 0회) |
| 모듈 | **M10 — 리허설 검증과 라이브 Demo (Capstone)** 잔여 2건 → **완료** |
| 범위 | 3회차(Live #27) 결과 기록 · 사고 8~11 분류 · A 판정 · Retrospective 완결 · Topic README · 링크 점검 |
| 결과 | **M10 DoD 7/7 · Topic 완료.** A 판정은 「무관중 4회차 뒤 확정」(사용자). B 갈래·사고 수정·4회차는 **이 Topic 의 CVL 유지보수**로 |

사용자 요청: *"이 작업을 이어서 진행하고 싶습니다. VibeLearn AI 를 사용해서 계속 진행 해 주세요."*
세션 시작 시 남은 것은 M10 DoD 2건(3회차 결과 · Retrospective)이었는데, 둘 다 **9/13 방송 결과가 Topic 안에 적히지 않아** 열려 있었다. 결과 자체는 Rundown·Daily Roundup·`output/debug/live27/` 에 있었다.

## 사용자 결정 3건 (세션 초반)

1. **진행자 소감** — 원문은 [[Journal/2026-09-17#Live #27 CoMC 앱 3회차 소감 · 4회차 재리허설 결정 (구술 원문)|Journal 9/17]]. 요지: *"멘트가 나왔다는 것에 만족. 퀄리티는 Rundown 등 사전 대본을 더 잘 만들면서 다듬을 것. 빨리 음성으로 듣고 싶다. 기능상 OK, 내용상 사전 작업 보완 필요."*
2. **A 판정** — ⓒ **무관중 4회차 재리허설 뒤 결정.** 목요일이고 방송까지 3일 → 재리허설 후 Live #28 에서 제대로.
3. **B 갈래** — **이 Topic 안에서 CVL 유지보수.**

## 한 것

### 1. 3회차 결과 기록 — `rehearsal-log-3.md` 「결과」표

트레이스(`session_trace.jsonl` 9/13 행 72건)로 Daily Roundup 수치를 대조했다: `03_classify_intent` 10회(answer_question 4 · summarize_part 4 · unknown 2), LLM 완주 8회 **4,400~7,260ms**(중앙값 ≈5.7s). Daily 의 「시도 9 · 통과 6 · 침묵 3」과 일치한다(unknown 2 중 1은 재시도 셈). 프리플라이트 PASS 7 · WARN 2 · FAIL 0.

### 2. 사고 8~11 — 분류표에 유형 · 원인 모듈 · 대책

| # | 사고 | 유형 | 원인 모듈 |
|---|---|---|---|
| 8 | 확정 커버리지를 「후보」로 말함 (3/3 재현) | 내용 없는 발화 | M2·M8 — 커버리지 줄 > 후보 표 우선순위가 컨텍스트에 없음 |
| 9 | 상태 질문에 항목만 읊음 | 내용 없는 발화 | M7·M8 — 사고 3과 같은 뿌리 |
| 10 | 2부에서 주간 영상을 묻자 2부 항목 오귀속 | **근거 없는 발화** (이 Topic 첫 발생) | M7 — ④ 가 파트 밖 근거 사용 · M8 게이트가 `part_id` 미검사 |
| 11 | `unknown` 거절 시 옛 초안 재렌더 | 운영 위험 | M9 — ⑥ 이 거절 시 오버레이를 안 비움 |

유형 집계: 근거 없는 발화 1 · 내용 없는 발화 3 · 오탐 2 · 구조 3 · 운영 위험 2 · 지연 0 · 장치 충돌 0 = **11건**. 「4회차 전 수정 목록」 6항목을 분류표 끝에 달았다.

### 3. A 판정 → go-nogo 「3회차 결과 반영」표

판정 규칙(「사고 있음 → 원인 기록 + 재리허설 여부 결정」) 그대로: **원인 기록 완료 · 무관중 4회차(09-18~19) 뒤 확정.** 4회차 사고 0건이면 Live #28 부터 REVIEW 상시. B 는 4회차에서 `spoken_player.py` 로 같이 시도하되 판정은 분리.

### 4. Retrospective 완결

「실제 방송 투입 결과」 5칸 + 해석 한 단락. 해석: **사고 4건 중 3건의 뿌리는 코드가 아니라 입력 문서** — Rundown 이 확정/후보·현재 상태·파트 소속을 앱이 읽을 만큼 적지 않았다. 진행자 소감 "사전 작업에서 보완"과 같은 자리. 학습 목표 6 · 성공 기준 표 · 여정 통계(14세션)도 맞췄다.

### 5. Topic 닫기 — 로드맵 · README · 링크 점검

- 로드맵 진행표 M10 **✅ 100% (7/7)** · 성공 기준 4/6 체크(DoD 100% 와 Self-Assessment 는 Retrospective 판정 그대로 — M6·M9 잔여는 B 갈래)
- **Topic 최상위 `README.md` 신규** — 무엇을 알아냈나 6 · 모듈 10 링크 · 실전 결과 · 틀렸던 판단 4 · 다음(CVL)
- `check_links.py`: **상대 링크 295 정상 · 깨짐 0.** 빈 폴더 3 → `10-…/troubleshooting` 삭제, `vl_materials`·`examples/audio/_preflight` 는 README 에 생략 사유 (재료가 비공개 Rundown · 오디오는 gitignore)

## 안 한 것 — 일부러

- **코드 수정 0.** 사고 8~11 수정은 4회차 세션(9/18~19)에서 수정 → 재현 테스트(수정 전 실패 / 후 통과 대조, M8 원칙) → 리허설 순서로. 오늘 문서만 닫고 코드를 건드리면 「고쳤다」는 주장에 대조가 없다
- `spoken_player.py` — 같은 이유. 4회차 세션의 첫 항목
- `missing_section` 5/6 원인 — 4회차 준비에서 이번 주 Rundown(Live28)을 먹여 보며 같이 본다

## Insights (인사이트)

### 결과가 있는데 적히지 않은 상태는 「미완」과 같다

9/13 방송 결과는 Rundown·Daily·트레이스 세 곳에 있었지만 Topic 문서 네 곳(rehearsal-log · go-nogo · Retrospective · 로드맵)은 나흘 동안 빈칸이었다. M10b 의 "Tomorrow's focus" 1~3번이 정확히 이것이었고, 방송 다음 날 BL5 발표 준비가 밀고 들어왔다.
> 프로젝트형 Topic 의 마지막 모듈은 「방송 직후 30분」을 캘린더에 박아야 닫힌다. Rundown 의 「방송 후 기록」 규칙이 Topic 에도 필요하다 — 개선 제안 6 후보.

### 진행자 소감이 사고 분류를 바꿨다

코드만 보면 사고 8~11 은 ②④⑤⑥ 의 결함이다. 소감 *"사전 작업에서 보완"* 을 놓고 다시 보니 8·9·10 은 **Rundown 이 신호를 약하게 준 것**이 먼저였다. 그래서 수정 목록에 코드와 함께 **rundown-writer 스킬(문서 규칙)** 을 넣었다. M1 원칙 「Rundown 에 적힌 것만」이 지켜졌기 때문에 Rundown 의 품질이 그대로 앱의 품질이 된다 — 이게 이 Topic 의 마지막 인사이트다.

### 「닫는다」와 「끝났다」는 다르다

M10 DoD 는 7/7 이지만 A 판정은 보류이고 B·C 는 NO-GO 다. 그래도 닫는 게 맞다 — 로드맵이 M10 에 요구한 것은 「근거 있는 판단」이었고 판단은 끝났다. 이후는 로드맵 밖 일이므로 CVL 로 가는 것이 방법론에 맞다 ([[project_vibelearn_cvl_pattern]] 패턴).

## DoD 체크리스트 (M10) — 최종

- [x] 프리플라이트 자동 점검 스크립트 — 9항목 · Live26·27
- [x] 무관중 리허설 2회 (1회차 사고 5 → 2회차 0)
- [x] 사고 유형 분류표 — 6유형 · **11건**
- [x] 재현 테스트 — 16편 전수 이상 0 · 게이트 9/9
- [x] 리허설 3회차 — **09-13 Live #27 실전**, 결과 기록 09-17 (시도 9 · 통과 6 · 침묵 3 · 사고 4)
- [x] LIVE 투입 판단 문서화 — 3갈래. A 「4회차 뒤 확정」 · B/C NO-GO
- [x] Topic Retrospective — 완결 (실제 투입 결과 + 진행자 소감 원문)

**완료율**: 7/7 (100%) — **Topic 완료 (2026-09-17)**

## Tomorrow's focus — CVL 세션 1 (09-18~19, 방송 없는 날)

순서는 [go-nogo 후속표](../10-Live-Rehearsal-Capstone/guides/go-nogo-decision.md) + [4회차 전 수정 목록](../10-Live-Rehearsal-Capstone/guides/incident-classification.md):

1. **사고 8~11 · 7 코드 수정** — ② `confirmed/candidate` 태깅 · ④ 상태 질문 규칙 + 현재 파트 근거 제한 · ⑤ `cross_part` 검사 · ⑥ 거절 시 오버레이 clear · 데몬 파트 전환 시 ② 내부 재실행. 각각 **수정 전 실패 / 후 통과** 대조 + 16편 회귀
2. **`spoken_player.py`** (약 60줄) — `spoken.json` 폴링 → M6 provider(edge-tts) 합성 → 지정 출력 장치 재생 → 파일 소비. 헤드폰으로 먼저
3. **OBS 방송 프로필 송출 트랙** — AI 출력 장치가 송출에 들어가는지 · 개별 뮤트 (M6b 미완 DoD)
4. **무관중 4회차 30분** — Live28 Rundown 으로, 이번엔 소리 포함. 결과 → `rehearsal-log-4.md` → A 확정 · Live #28 투입 여부
5. rundown-writer 스킬에 「확정/후보 · 현재 상태 · 파트 소속」 규칙 추가 (문서 쪽 수정)

WorkLog 파일명은 `20260918_CVL1_Live-CoMC-App.md` (Topic 완료 후 유지보수 세션 표기).

## 참조 및 산출물

**신규**: `README.md`(Topic 최상위) · 이 WorkLog · Journal 9/17 구술 원문
**수정**: `10-…/guides/rehearsal-log-3.md`(결과) · `incident-classification.md`(8~11 · 정리 · 수정 목록) · `go-nogo-decision.md`(3회차 반영) · `vl_worklog/20260912_…_Final_Retrospective.md`(완결) · `vl_roadmap/…`(M10 ✅ · 성공 기준)
**삭제**: `10-Live-Rehearsal-Capstone/troubleshooting/`(빈 폴더)
**비용**: LLM 호출 0
