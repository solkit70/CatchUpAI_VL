# M7 — Co-MC 엔진 POC (파일 기반 6단계)

**상태**: 실습 1~6 완료 · DoD 7/8 + 1건 부분 (음성 지연은 M6 라우팅 대기)
**예상 학습 시간**: 16h
**난이도**: ⭐⭐⭐

M1~M6에서 따로 만든 것들을 하나의 파이프라인으로 잇는 모듈이다.
설계(M1~M3)와 하네스(M4~M6)가 여기서 처음으로 **끝에서 끝까지** 연결된다.

---

## 왜 파일 기반인가

각 단계가 JSON 을 읽고 JSON 을 쓴다. 함수 호출로 이어 붙이면 빠르지만,
방송 사고가 났을 때 **어느 단계가 잘못됐는지 알 수 없다.**

```
① 01_parse_rundown    Rundown .md          → rundown_index.json
② 02_resolve_context  + Daily/Weekly 크로스 → broadcast_context.json
③ 03_classify_intent  STT 텍스트            → intent.json
④ 04_compose_answer   + LLM (M5 어댑터)     → answer_draft.json
⑤ 05_verify_and_gate  + safety_policy      → verdict.json
⑥ 06_render_output    화면/음성 분리        → overlay.json / spoken.json
```

전 단계가 `output/session_trace.jsonl` 에 한 줄씩 append 한다.
남지 않는 사고는 재현할 수 없고, 재현할 수 없는 사고는 고칠 수 없다.

---

## 학습 순서

### 1. 전제 (읽고 시작할 것)

1. [../01-Concept-and-Rundown-Contract/examples/case-table.md](../01-Concept-and-Rundown-Contract/examples/case-table.md)
   — 파트 헤딩·커버리지 줄 변동성 케이스. ① 단계 정규식이 여기서 나왔다
2. [../01-Concept-and-Rundown-Contract/guides/forbidden-sections.md](../01-Concept-and-Rundown-Contract/guides/forbidden-sections.md)
   — 금칙 섹션. **안전장치 1층이 ① 단계에서 성립한다**
3. [../05-STT-LLM-Harness/guides/llm-latency-sweep.md](../05-STT-LLM-Harness/guides/llm-latency-sweep.md)
   — ④ 단계의 프로바이더·effort 설정 근거

### 2. 코드

4. [src/common.py](src/common.py)
   — 공통 유틸. 스키마 검증, 추적, 안전 정책 드리프트 감지
5. [src/01_parse_rundown.py](src/01_parse_rundown.py)
   — **구현 완료**. M1 파싱 계약 → `rundown_index.json`
6. [src/02_resolve_context.py](src/02_resolve_context.py)
   — **구현 완료**. 근거 풀 조립 + 불변식 확인 → `broadcast_context.json`
7. [src/03_classify_intent.py](src/03_classify_intent.py)
   — 규칙 기반 의도 분류. LLM 을 쓰지 않는 이유가 docstring 에 있다
8. [src/04_compose_answer.py](src/04_compose_answer.py)
   — M5 LLMProvider 호출 + 생성 전 차단 4종
9. [src/05_verify_and_gate.py](src/05_verify_and_gate.py)
   — 규칙 기반 안전 게이트. `--tamper` 로 게이트가 실제로 잡는지 확인한다
10. [src/06_render_output.py](src/06_render_output.py)
    — overlay/spoken 분리. `spoken.provider` 명시
11. [src/session_state.py](src/session_state.py)
    — 권위값/추정값 분리 (실습 5)
12. [src/run_pipeline.py](src/run_pipeline.py) ·
    [src/evidence_latency_probe.py](src/evidence_latency_probe.py)
    — 지연 측정 (실습 6)

### 3. 테스트

13. [tests/test_part_authority.py](tests/test_part_authority.py)
    — 시각 추정이 권위값을 바꿀 수 없음을 증명
14. [tests/test_claim_evidence.py](tests/test_claim_evidence.py)
    — 5개 샘플 발화의 인용이 근거 풀에 실재하는지 확인

### 4. 결과

15. [guides/latency-report.md](guides/latency-report.md)
    — **핵심 산출물**. 지연 목표 대비 격차와 원인 3분해

---

## 실행 순서

```bash
cd src

# ① 파싱 — 샘플 2편
python 01_parse_rundown.py
python 01_parse_rundown.py --live 21
python 01_parse_rundown.py --path "AI/Roundup/2026-08-17 - Live24 Weekly Rundown.md"

# ② 컨텍스트 조립 — current_part_id 는 권위값이므로 반드시 명시한다
python 02_resolve_context.py --live 21 --part 3
python 02_resolve_context.py --live 20 --part 2
python 02_resolve_context.py --live 20 --part "주간 영상"     # 번호 없는 파트

# ③~⑥ 발화 처리
python session_state.py --init --live 21 --part 3
python 03_classify_intent.py --live 21 --text "오늘 3번 파트에서 뭘 다루나요?"
python 03_classify_intent.py --live 21 --suite          # M5 20문장 일괄
python 04_compose_answer.py --live 21
python 05_verify_and_gate.py --live 21
python 05_verify_and_gate.py --live 21 --tamper         # 게이트가 잡는지 확인
python 06_render_output.py --live 21

# 실습 5·6
python session_state.py --suggest --elapsed 45
python run_pipeline.py --live 21 --repeats 3
python evidence_latency_probe.py --repeats 3

# 테스트
cd .. && python tests/test_part_authority.py && python tests/test_claim_evidence.py
```

---

## 실습 2 검증 결과

로드맵 검증 기준: **두 회차 모두 `status_map` 에 최소 5개 항목**

| | 파트 | 금칙 | 조건부 | 커버리지 항목 | status_map | 근거 풀 |
|---|---|---|---|---|---|---|
| Live20 | 5 (번호 4 + 무번호 1) | 0 | 0 | 17 | 11 (ok 6) | 23~25 |
| Live21 | 3 | 2 | 1 | 5 | 11 (ok 6) | 15 |

Live21 결과는 M1 `forbidden-sections.md` 가 손으로 확인한 3종
(보류 인사이트 / 주간 영상 후보 / 대기 목록)과 **정확히 일치**한다 —
앞의 둘은 `excluded_sections`, 셋째는 `conditional_sections` 로 갈렸다.

---

## 이 모듈에서 확인된 것

| # | 발견 | 영향 |
|---|---|---|
| 1 | **`is_final` 규칙이 실물과 맞지 않았다** — 볼트 Rundown 14편 중 '최종본' 표기 0건 | 스키마 설명대로 구현하면 방송 투입 신호가 영원히 꺼진다. 실물 어형('확정'/'방송 완료')으로 판정 |
| 2 | **커버리지를 가진 무번호 파트가 있다** — Live20 `## 주간 영상` | `N부:` 정규식만 쓰면 발화 허용 범위 2건이 통째로 사라진다. `part.is_numbered` 추가 |
| 3 | **대시는 지시문 신호가 아니다** — 항목 제목에도 흔하다 | Live20 2부 부제를 지시문으로 오인해 항목에서 잘라 냈다. 운영 동사로 판정하도록 교정 |
| 4 | **`spoken` 에 provider 필드가 없었다** | M3 설계 당시엔 프로바이더가 하나였다. 서킷 브레이커가 교체하므로 명시 필요 |
| 5 | **`.canvas` 는 '없음'이 아니라 '안 봄'** | M1 계약상 시각화 사본은 신뢰하지 않는다. 둘을 뭉치면 원인 추적이 막힌다 |
| 6 | **stderr 인코딩을 빼먹으면 사고 시 오류를 못 읽는다** | 한글이 `파트` 로 깨져 나왔다 |
| 7 | **의도 분류에 LLM 을 쓰면 지연이 두 배** | 규칙 기반으로 구현. 20문장 중 18건 분류, 2건은 정직하게 unknown |
| 8 | **`unknown` 과 `out_of_scope` 는 다르다** | 전자는 되묻고 후자는 거절한다. 뭉치면 HITL 대기열이 영원히 못 푸는 요청으로 찬다 → intent enum 에 `out_of_scope` 추가 |
| 9 | **지연의 주범은 프로세스 기동(3.7s) + 연결 설정(3.0s)** | LLM 자체는 2.1~3.5s. 매 발화마다 새 프로세스면 6.7초를 매번 낸다 → **M9 는 단일 장기 프로세스여야 한다** |
| 10 | **근거 풀 크기가 지연을 좌우한다** (2건→15건 +1.3s) | 반면 문장 3→5개는 +122ms. 답변 길이를 줄이는 최적화는 헛수고 |
| 11 | **사전 캐시 효과가 측정되지 않았다** | ①②가 아끼는 800ms 가 LLM 편차(±2,000ms)에 묻힌다 |
| 12 | **부재에 대한 주장은 인용으로 뒷받침될 수 없다** | "문서에 없습니다"에 인용을 붙이면 게이트는 통과시킨다. claim-evidence 모델의 빈틈 → M8 |

---

## Definition of Done

- [x] 6개 스크립트 순차 실행으로 `overlay.json`/`spoken.json` 생성 성공
- [x] Live20·Live21 두 회차 모두 파싱·컨텍스트 조회 성공
- [x] 5개 샘플 발화의 `claim_map` 이 원문과 일치 — 위반 0건
      ([tests/test_claim_evidence.py](tests/test_claim_evidence.py))
- [x] 파트 판정 권위값/추정값 분리 동작 검증 — 8개 항목 전부 통과
      ([tests/test_part_authority.py](tests/test_part_authority.py))
- [x] `session_trace.jsonl` 에 6단계 전부 기록
- [~] 응답 지연 실측 및 목표 대비 결과 문서화 —
      화면 경로는 실측·원인 분해 완료([guides/latency-report.md](guides/latency-report.md)).
      **음성 경로는 M6 오디오 라우팅 후에만 확정 가능** (미측정)
- [x] README 작성 완료
- [x] WorkLog 작성 완료

---

## 다음 세션

M7 실습은 전부 끝났다. 남은 것은 두 갈래다.

**M8 (안전 게이트 심화)** — 이번 세션이 넘긴 것들
- 화이트리스트 검증 강화 (현재는 토큰 겹침만 보는 약한 규칙)
- **부재에 대한 주장** 처리 — "문서에 없습니다"는 인용으로 뒷받침할 수 없다
- 어려운 질문 세트에서 effort=minimal 재검증
- 근거 풀 관련도 판정 강화 → 적은 근거로 같은 품질 (지연 1.3초 절감과 직결)

**M9 (데스크톱 셸)** — 지연 리포트가 요구하는 것
- **단일 장기 실행 프로세스.** 파일 계약은 유지하되 프로세스 경계만 바꾼다 (~6.7초 절감)
- 음성 경로 지연 측정 (M6 라우팅 선행 필요)

---

← 이전: [M6 멀티 TTS 하네스 + 오디오 라우팅](../06-TTS-Audio-Routing-Harness/README.md)
→ 다음: M8 안전 검증 게이트 심화 (`08-Safety-Gate-Scenarios/`)
