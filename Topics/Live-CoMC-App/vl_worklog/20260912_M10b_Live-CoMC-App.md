---
title: "M10b — 방송 전날 밤 · 3회차를 실전으로 옮기고, 소리 나는 부품이 없다는 것을 알았다"
created: 2026-09-12 23:20:00
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
| 날짜 | 2026-09-12 (토) 23:20 ~ 00:15 — Live #27 **약 5시간 전** |
| 실소요 | 약 55분 (사용자 대기 없음 · LLM 호출 1회) |
| 모듈 | **M10 — 리허설 검증과 라이브 Demo (Capstone)** 잔여 3건 |
| 범위 | 남은 작업 파악 → 3회차 조건 재정의 → Live27 사전 점검 → 판단 문서 · Retrospective 초안 |
| 결과 | **사용자 결정: Live #27 을 3회차로.** 사전 점검에서 **구조 사고 2건 추가 발견**(6·7). go/no-go 3갈래 판정. Retrospective 초안 |

사용자 요청은 *"내일 라이브 방송을 하는데요. 하기 전에 이 Topic 을 마저 진행하고 싶습니다."* 였다.
남은 것은 M10 3건(3회차 · LIVE 판단 · Retrospective)과 M6·M9 꼬리 각 1건이었고, 3회차는 사용자 30분이 필요해 선택지를 드렸다.
**오늘 밤이 아니라 내일 방송을 3회차로** 하기로 하셨다.

## 한 것

### 1. 3회차의 조건을 로드맵 원문으로 되돌렸다

WorkLog 09-06 은 3회차를 *"사람이 마이크→호출어→STT→답변→오디오 전 구간"* 으로 적었다. 로드맵 실습 4 원문은 *"동일 조건으로 3회차"* 다.
코드를 보니 마이크 전 구간은 **존재하지 않는 경로**였다 — 엔진은 `--text`/`--serve` 만 받고, M4·M5·M6 은 프로브 스크립트로만 있다.
그래서 내일 3회차는 로드맵 원문 조건(텍스트 입력 → 화면)에 「진행자가 실시간으로 넣고 시청자가 오버레이로 본다」를 더한 것으로 정의했다.
→ [rehearsal-log-3.md](../10-Live-Rehearsal-Capstone/guides/rehearsal-log-3.md) 「결정」

### 2. Live27 Rundown 으로 프리플라이트 · 파이프라인 사전 점검

| 점검 | 결과 |
|---|---|
| 프리플라이트 9항목 | PASS 4 · WARN 2 · FAIL 2 · SKIP 1. FAIL 은 「컨텍스트 오늘 것 아님」「오버레이 서버 안 켜짐」 — 둘 다 아침 루틴. 코드 결함 0 |
| ① 파싱 `--live 27` | 파트 3 · 항목 4 · 이상 0 |
| ② 컨텍스트 `--part 2` | 생성됨. 근거 6건 중 5건 `missing_section` — Rundown 만 살아 있다 |
| ③~⑥ 발화 1건 | 게이트 pass · 4/4 문장 · REVIEW 보류. **6,210ms** (1회 표본) |

### 3. 발견 — 사고 6 · 7

**사고 6 — `spoken.json` 을 읽는 코드가 없다.** `06_render_output.py` 는 LIVE 에서 `spoken.json` 을 쓰고 "합성·재생은 M9 셸의 몫"이라 주석해 두었다.
M9 는 Electron 셸을 "급하지 않음"으로 내렸고, 그 자리가 비어 있다. `grep -rn spoken.json` 결과: 쓰는 곳 1, 지우는 곳 1(시나리오 러너), **읽는 곳 0.**
→ **LIVE 모드는 지금 소리를 내지 못한다.** REVIEW 와의 차이는 파일 이름뿐이다.

**사고 7 — `--serve` 중 파트 전환이 컨텍스트를 안 만든다.** 데몬은 ①② 를 기동 시 한 번만 돌리고, ④ 는 `broadcast_context.{live}.json` 을 매번 파일에서 읽는다.
핫키는 `current_part_id` 만 바꾼다. 내일은 파트마다 다른 창에서 ② 를 재실행하는 것으로 우회한다.

둘 다 유형 **구조**다. 09-06 의 사고 1(`--live` 샘플 고정)과 같은 종류 — **각 모듈이 자기 DoD 는 채웠는데 옆 모듈과 이어진 적이 없었다.**

### 4. LIVE 투입 판단을 3갈래로 문서화

「LIVE 투입」을 A 화면 보조 / B 음성 출력 / C 음성 입력으로 갈랐다. 실물이 있는 것은 A 뿐이다.
**A GO(3회차 사고 0건 조건) · B NO-GO(부품 부재) · C NO-GO(B 이후).** 근거는 모듈별 실측 14건.
→ [go-nogo-decision.md](../10-Live-Rehearsal-Capstone/guides/go-nogo-decision.md)

### 5. Topic Retrospective 초안

여정 통계 · 목표 6개 점검 · 방법론 평가(잘 된 것 4 · 안 된 것 4) · 인사이트 6 · **개선 제안 5**. 「실제 방송 투입 결과」절은 비워 두었다.
→ [20260912_Live-CoMC-App_Final_Retrospective.md](20260912_Live-CoMC-App_Final_Retrospective.md)

### 6. 안 한 것 — 일부러

- **`spoken_player.py` 를 오늘 밤 만들지 않았다.** 60줄이면 되지만, 방송 5시간 전에 새 오디오 부품을 넣고 송출 트랙 검증 없이 켜는 것은 M6c 교훈(*"검증은 실제로 쓰는 환경에서 한 번은"*) 위반이다. go-nogo 후속표 1번으로 남김
- `playback_latency.py` WASAPI 명시 · 지연 like-for-like 재측정 — B 갈래 일이라 같이 이월
- 사고 5 대책(`output/debug/{회차}/`) — 코드는 이미 `prompt.txt` 를 안 쓴다. 남은 것은 옛 파일 이동뿐이라 아침 루틴에 넣음
- M6 트랙 2 뮤트 검증 — 소리 낼 부품이 없으니 내일은 무의미. B 와 함께

## Insights (인사이트)

### 판정을 올리려고 조건을 낮춘 것이 아니다

3회차 조건을 「마이크 전 구간」에서 「동일 조건」으로 되돌리면서 계속 스스로 물었다 — *이건 DoD 를 채우려고 기준을 낮추는 건가?*
로드맵 원문을 다시 읽으니 아니었다. **높은 조건은 WorkLog 가 추가한 것이고, 로드맵은 처음부터 「동일 조건」이었다.**
그런데 그 높은 조건이 「방송 중에 못 한다」는 결론을 낳았고, 그 결론이 3회차를 일주일 미뤘다.
> 문서에 적힌 조건이 어디서 왔는지 — 로드맵인지, 그날의 야심인지 — 를 확인하지 않으면 없는 요구사항에 일정을 뺏긴다.

### 「M9 셸의 몫」이라는 주석이 6주 동안 아무도 안 읽은 계약이었다

M7 이 `audio_path: null` 을 쓰면서 재생을 M9 에 위임했고, M9 는 Electron 을 뒤로 미루면서 그 위임을 받지 않았다.
둘 다 자기 문서 안에서는 옳았다. **위임은 받는 쪽 DoD 에 적혀야 계약이다.** 주는 쪽 주석은 계약이 아니다.
Retrospective 개선 제안 3(「실물 1건 통합 기동」 DoD 필수)이 여기서 나왔다.

### 09-06 과 같은 밤, 같은 발견

09-06: *"아홉 모듈이 한 번도 같이 돌아본 적이 없었다"* — 입력 끝(`--live`). 09-12: 출력 끝(`spoken.json`).
캡스톤이 두 번 연속 「연결 부재」를 찾았다. 셋째가 있다면 파트 전환(사고 7)이고 오늘 같이 나왔다.
**캡스톤의 역할은 새 기능이 아니라 이음새 확인이다.** 로드맵이 M10 에 10h 를 준 것은 적정했고, 그 시간은 코드가 아니라 이런 발견에 쓰였다.

## DoD 체크리스트 (M10)

- [x] 프리플라이트 자동 점검 스크립트 완성 — 9항목 · Live26·27 두 회차 실행
- [x] 무관중 리허설 2회 완료 (1회차 사고 5건 — 분류표 기준. 09-06 WorkLog 의 「6건」은 프리플라이트 FAIL 을 포함한 셈이다 · 2회차 0건)
- [x] 사고 유형 분류표 완성 — 6유형 · **7건** 매핑
- [x] 재현 테스트 — 16편 전수 이상 0건 · 게이트 9/9
- [ ] 리허설 3회차 — **09-13 Live #27 실전** (로드맵 원문 「동일 조건」. 절차·체크리스트 준비 완료, 결과 칸 비움)
- [x] LIVE 투입 가능 여부 판단 문서화 — **3갈래 판정 완료** (A 조건부 GO · B/C NO-GO). 3회차 후 A 확정
- [ ] Topic Retrospective — **초안 완료**, 「실제 방송 투입 결과」절 대기

**완료율**: 5/7 (71%) — 남은 2건은 둘 다 09-13 방송 결과 하나에 걸려 있다

## Tomorrow's focus (09-13 방송 후)

1. [rehearsal-log-3.md](../10-Live-Rehearsal-Capstone/guides/rehearsal-log-3.md) 「결과」표 채우기 — 발화 시도/통과/침묵 · 사고 · `daemon_latency.json`
2. go-nogo A 갈래 확정 → Live #28 상시 투입 여부
3. Retrospective 「실제 방송 투입 결과」 + 진행자 소감 원문 → Topic 완료 · 로드맵 진행표 M10 ✅
4. 근거 5/6 `missing_section` 원인 확인 (이번 주 문서 섹션명 vs 해석기)
5. 개선 제안 1~4 를 `workflow_guide.md` · `daily_learning_prompt.md` · `roadmap_prompt_template.md` 에 반영할지 사용자와 결정

## 참조 및 산출물

**신규**

- `10-Live-Rehearsal-Capstone/guides/rehearsal-log-3.md` — 결정 · 사전 점검 · 당일 절차 · 체크리스트 · 결과 칸
- `10-Live-Rehearsal-Capstone/guides/go-nogo-decision.md` — 3갈래 판정 · 근거 14건 · 투입 조건 · 후속 5단계
- `vl_worklog/20260912_Live-CoMC-App_Final_Retrospective.md` — 초안

**수정**

- `10-Live-Rehearsal-Capstone/guides/incident-classification.md` — 사고 6·7 추가
- `10-Live-Rehearsal-Capstone/README.md` — 남은 것 갱신
- `vl_roadmap/20260802_RoadMap_Live-CoMC-App.md` — 진행표 M10 71%
- `07-CoMC-Engine-POC/output/` — `rundown_index.27.json` · `broadcast_context.27.json` 생성 (실행 산출물)

**비용 메모** — LLM 호출 1회 (`gpt-5 effort=minimal`, 발화 1건).
