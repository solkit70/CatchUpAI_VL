---
title: "팩트체크 대조표"
created: 2026-08-12 00:00:00
author:
  - "Claude Code"
tags:
  - seattle-tech-week
  - factcheck
---

## 팩트체크 대조표

**모듈**: M8 / **대상**: `07-Articles/` 원고 5편
**검증일**: 2026-08-12

## 1. 인용 원문 1:1 대조

기사에 쓴 인용 32건을 트랜스크립트 원문과 대조했다.

| 결과 | 건수 |
|---|--:|
| **일치** | **32** |
| 불일치 | **0** |

> 초기 자동 대조에서 1건이 불일치로 나왔으나, **타임스탬프가 문장 중간에 삽입된 탓**이었다.
> 타임스탬프 제거 후 재검증하여 일치 확인. (Vivek Radhakrishnan [26:04~26:12])

**대조한 주요 인용**

| 화자 | 인용 핵심구 | 결과 |
|---|---|:--:|
| Quiana Daniels | "caught red-handed" / "72 business hours" / "25 to 30 percent" / "$750,000 just to build half" | ✅ |
| Amit Gupta | "Building is no longer the moat" | ✅ |
| Eden Cohen | "cost of intelligence has now dropped" / "not just easy for you" / "capacity is now potentially 5X" / "Samsung or Hynix" | ✅ |
| Jonathan Greechan | "insider knowledge of a problem" / "building things that nobody wants" | ✅ |
| Levi Velez Reed | "glass wall between me" / "you can't give equity" | ✅ |
| Roddy | "invisible walls on the skills side" / "keep my job to fund my business" | ✅ |
| Sunny Kotwal | "would not advise it if you end up" / "AI is a tool" | ✅ |
| Muazma Zahid | "Models are commodity" / "approve a mortgage" | ✅ |
| Kunal Jain | "most dangerous type of output" / "Rows exist is not the same" / "in someone's memory instead of in an assertion" | ✅ |
| Denny Lee | "it hallucinates, it's wrong" | ✅ |
| Miriam Alvarez-Pintor | "another tool in our toolbox" / "first elementary steps" | ✅ |
| Guvenc Degirmenci | "we want generative AI" | ✅ |
| Apoorv Mathur | "takes 10 years to build" | ✅ |
| Vivek Radhakrishnan | "review or judgment are increasing" / "not taking the accountability" | ✅ |
| Emmy Smith | "a lot of babysitting" | ✅ |
| Prakhar Agarwal | "first percentile on the growth chart" / "38 percentile" | ✅ |

## 2. 화자 이름·소속 대조

기사에 인용한 화자 20명을 frontmatter의 `speaker` / `speaker_affiliation`과 대조했다.

| # | 항목 | 조치 |
|--:|---|---|
| 1 | **Kunal Jain 소속 누락** — 기사에 "커머스 데이터 플랫폼 팀"으로만 표기, frontmatter는 **Adobe** | ✅ **정정 완료** — "어도비의 커머스 데이터 플랫폼 팀에서 일하는 엔지니어" |
| 2 | Eden Cohen — Q&A 파일 frontmatter가 3인 합산 표기 | ✅ 개별 파일 확인: **"Gen AI Product Lead, Google"**. 기사 표현("구글에서 생성 AI 제품을 만드는") 정확 |
| 3 | Denny Lee — frontmatter에 `speaker_affiliation` **없음** | ✅ 본인 발언 [0:50] *"we at Databricks"*가 근거. 기사 표기 유지 |
| 4 | **Roddy — 성(姓) 미상** | ⚠️ 원자료 한계. frontmatter도 이름만 표기. 기사도 이름만 사용. **정정 불가, 그대로 둠** |
| 5 | 나머지 16명 | ✅ frontmatter와 일치 |

## 3. 외부 통계 출처 확인

| 수치 | 결과 | 조치 |
|---|---|---|
| **생성 AI 파일럿 95% 실패** | ✅ **출처 특정** — MIT 프로젝트 난다 「The GenAI Divide: State of AI in Business 2025」(2025-07). 300건 도입 사례, 150명+ 임원 인터뷰, $30~40B 투입 | **본문에 명시 귀속.** 자히드가 발표에서 인용한 조사와 일치 |
| **AI 실패의 85%가 데이터 품질** | ❌ **원 출처 특정 실패.** Gartner·IDC로 재인용이 난립하고 80/85/88/90% 수치가 뒤섞임 | ✅ **본문에서 삭제.** 데이터 품질 논지는 쿠날 자인 현장 발언만으로 성립 |
| 하이퍼스케일러 설비투자 7,250억 달러 (77%↑) | AI2Work 분석 기사 | 출처 매체 명시 없이 "한 지역 분석 매체"로 서술 |
| 시애틀 벤처 27억 달러 / 40% 감소 | 동일 | 동일 |
| 워싱턴 데이터센터 126개 / 1,414MW | 동일 | 동일 |

## 4. 시간 경과 민감 항목 (출고 직전 재확인 필요)

| # | 항목 | 2026-08-12 확인 결과 | 상태 |
|--:|---|---|:--:|
| 12 | **Luma 2027 날짜** | *"Dates for Seattle Tech Week 2027 are TBD - Subscribe to be the first to know!"* + Follow 버튼 존재 | ✅ **TBD 확인.** 5편 내용 유효 |
| 13 | **`techweek@madrona.com`** | 공식 페이지에 문의·주최 창구로 명시 | ✅ **유효 확인** |
| 14 | **스타트업425 모집 상태** | 공식 사이트에 6기 일정 명시 없음 | ⚠️ **본문에서 "6기 모집 중" 삭제.** "다음 기수 준비 중 / 공식 사이트 확인"으로 완화 |
| 11 | 2026 타임라인 (제출 4/9 · 캘린더 5/14 · 등록 6/25) | GeekWire 캘린더·Madrona 공지 기반 | ⚠️ **출고 직전 재확인 권장** |
| 15 | 무료 창구 5곳 | SBA 패널 발언 기준 | ⚠️ 기관 존속은 안정적이나 **담당 지역 변동 가능** |

## 5. ⚠️ 발견된 수치 불일치 — 스타트업425 실적

**현장 발언과 공식 자료의 수치가 다르다.**

| 출처 | 기수 | 등록 | 졸업 |
|---|--:|--:|--:|
| **Levi Reed 현장 발언** (2026-07-29) | 4기 | **155명** | **95명** |
| **Startup425 공식** (웹 확인) | 4기 | **170명** | **89명** |
| Jonathan Greechan 현장 발언 | — | — | **89개사** (전체 프로그램 누적) |

**주목**: 공식 자료의 "89 graduates"가 그리찬이 말한 "89개사"와 일치한다.
리드의 155/95는 그 자리에서 구두로 밝힌 수치라 기준이 다를 가능성이 있다
(수료 기준 vs 법인 설립 완료 기준 등).

**조치**: ✅ **기사에서 수치를 뺐다.** 2편·5편 모두 "네 기수를 진행했다"로만 서술.
어느 수치가 맞는지 확정할 수 없는 상태에서 한쪽을 쓰면 오보가 된다.

> **판단 근거**: 이 수치는 기사의 논지("무료이고 벤처스케일이 아니어도 받는다")에 필수가 아니다.
> 논지에 필수적이지 않은 불확실한 수치는 빼는 것이 맞다.

## 6. 집필 단계에서 선제 회피한 항목

M7 집필 시 **아예 쓰지 않는 방식**으로 처리해 사후 수정이 필요 없었던 것들이다.

| 위험 항목 | 처리 |
|---|---|
| C-Stork **$275,000** (지출액 아님) | 미사용. "75만 달러 견적, 사양의 절반 기준"만 사용 |
| Imagine Meals "몇 주 만에 15파운드" | 체중 생략, 퍼센타일(1→38)만 사용 |
| Meta 월 $2.5B | 미사용 (검증 불가 전언) |
| "Get out of the building" 오귀속 | 해당 인용 자체를 미사용 |
| Databricks quadrillion 토큰 | 미사용 (전사 오류 가능) |
| Amit Dubey · Karl Weaver 전사 품질 불량 | 직접 인용 미사용 |

## 7. 잔여 확인 항목

| # | 항목 | 비고 |
|--:|---|---|
| A | **벤 개프니(OpenAI 법무) 발언 맥락** | GeekWire 원문에서 어느 패널이었는지 미확인. 인용 자체는 GeekWire 보도 기반 |
| B | **패트릭 톰슨 "3개월 만에 3배"** | 원문은 Anthropic 청구서 특정. 기사에서는 **회사명 없이 "AI 사용료"**로 처리. 이 완화가 적절한지 최종 판단 필요 |
| C | **"100마일 고속도로" 비유 귀속** | 필자 본인의 비유인데 기사에 "필자는 이런 비유를 쓴다"로 표기. 표현 다듬기 권장 |
| D | **현장 녹화 21건 링크 유효성** | 비공개 전환 여부 일괄 확인 필요 |
| E | **"한국어 진행 행사 없었다"** (5편) | 필자 관측 범위임을 본문에 명시함("필자가 아는 한") ✅ |

## 검증 요약

| 항목 | 결과 |
|---|---|
| 인용 원문 대조 | **32 / 32 일치** |
| 화자 소속 대조 | 20명 중 **1건 정정**(Kunal Jain → 어도비), 1건 원자료 한계(Roddy 성 미상) |
| 외부 통계 | 95% **출처 특정 후 명시 귀속**, 85% **삭제** |
| 시간 민감 항목 | Luma TBD·이메일 **유효 확인**, 스타트업425 수치 **삭제** |
| 발견한 수치 불일치 | **1건** (스타트업425 155/95 vs 170/89) → 수치 제거로 처리 |
