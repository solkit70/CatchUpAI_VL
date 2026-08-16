---
title: "특정 학군의 AI 정책 확인 절차"
created: 2026-08-16 23:20:00
tags:
  - ai-education
  - district-policy
  - how-to
---

## 언제 쓰는가

특정 학교·학군에 도구를 소개하거나 교육을 제안하기 전에, **그 학군에서 무엇이 허용되는지** 확인해야 할 때 쓴다.

**대전제**: 주 가이던스는 답이 아니다. 실질 구속력은 학군 AUP에 있고, 같은 주 안에서도 학군마다 다르다. 반드시 해당 학군 문서를 직접 봐야 한다.

## 1단계 — 층위 판정 (1분)

확인하려는 사항이 어느 층 소관인지 먼저 가른다. 상세는 [../concepts/three-layer-governance.md](../concepts/three-layer-governance.md).

| 질문 | 해당 시 | 조치 |
|---|---|---|
| 학생 데이터가 외부로 나가는가? | 1층 (법률) | CIPA·COPPA·FERPA 확인. **우회 불가** |
| 학생이 18세 미만이고 도구가 연령 제한이 있는가? | 1층 (계약) | [연령 게이트 표](../concepts/age-gates-by-tool.md) 확인. **우회 불가** |
| 해당 주가 학군 AI 정책을 의무화했는가? | 2층 | TN·OH·ID·MD·OK·VA면 학군에 정식 정책이 반드시 있다 |
| 그 밖의 모든 것 | 3층 | 아래 2단계로 |

## 2단계 — 학군 문서 찾기

찾을 문서는 세 종류다.

| 문서 | 일반적 명칭 | 어디에 있나 |
|---|---|---|
| AI 정책 | "AI Use Policy", "Artificial Intelligence Policy", "Responsible Use of AI" | 교육위원회(Board) 정책 페이지 |
| 승인 도구 목록 | **"AI Tool Inventory"**, "Approved Technology List" | 기술부(Technology/IT) 페이지. 공개 의무가 있는 주도 있다 |
| 기존 기술 사용 정책 | "Acceptable Use Policy (AUP)", "Responsible Use Policy" | AI 정책이 없으면 여기에 AI 조항이 들어 있다 |

**검색 요령**

- `"[학군명]" AI policy site:.k12.[주약자].us` 또는 `"[학군명]" board policy artificial intelligence`
- 교육위원회 정책은 번호로 관리된다 (예: Minnesota 계열은 Policy 625). 번호를 알면 바로 찾는다
- 없으면 **기술부에 직접 문의**하는 것이 빠르다. Maryland처럼 **AI 조정관(coordinator) 지정을 의무화**한 주에서는 담당자가 지정돼 있다

## 3단계 — 확인 항목 체크리스트

찾은 문서에서 다음을 확인한다. Oklahoma 모델 정책 구조를 기준으로 삼았다.

**학생 사용 규칙**

- [ ] AI 사용 **공개(disclosure) 의무**가 있는가? 단계별인가 일률적인가?
- [ ] **AI 대화 링크 제출**을 요구하는가? (Oklahoma는 Level 1부터 요구)
- [ ] 인용(citation) 형식이 지정돼 있는가?
- [ ] 금지 사용 목록은 무엇인가?
- [ ] 위반 시 학업 정직성 처리 기준은?

**도구 승인**

- [ ] 승인 도구 목록이 존재하는가? 공개돼 있는가?
- [ ] 신규 도구 승인 절차와 담당 부서는?
- [ ] 위험 평가 체계가 있는가? (Oklahoma는 Red/Yellow/Green)
- [ ] 평가 루브릭이 공개돼 있는가? → 있으면 그 항목 순서대로 제안 자료를 구성한다

**데이터·법률**

- [ ] DPA(데이터 처리 계약) 요구 조건은?
- [ ] 부모 동의·옵트아웃 절차가 있는가?
- [ ] 학생 데이터의 상업적 이용 금지 조항이 있는가?

**기술 환경** (M2에서 상세)

- [ ] Google Workspace for Education 등급은? (Fundamentals 무료 / Standard / Plus)
- [ ] **Gemini in Classroom이 활성화돼 있는가?**
- [ ] **18세 미만 OU가 별도로 차단돼 있는가?**
- [ ] Gems 공유가 허용돼 있는가?
- [ ] 필터링·모니터링 도구는 무엇인가? (GoGuardian / Securly / Lightspeed)

**교사·연수**

- [ ] 연간 AI 연수 의무가 있는가? 내용은?
- [ ] 교사가 과제별 AI 허용 수준을 지정하는가?

## 4단계 — 판정

| 상황 | 판정 |
|---|---|
| 승인 목록에 있음 | 바로 사용 가능 |
| 목록에 없고 신규 승인 절차 있음 | 절차 진행. 평가 루브릭 항목대로 자료 준비 |
| 목록에 없고 절차도 없음 | 기술부 문의가 유일한 경로. 소규모 파일럿 제안이 통과 확률이 높다 |
| 명시적으로 금지됨 | 중단. 교사 개인 사용 가능 여부만 별도 확인 |
| 정책 자체가 없음 | 기존 AUP 적용. 담당자에게 **문서로** 확인받아 둘 것 |

## 5단계 — 도구 제안 시

승인 절차를 밟게 되면 다음을 준비한다. Oklahoma 승인 관문 4단계 기준이다.

1. 벤더 프라이버시·데이터 처리 관행 문서
2. 교육·운영 목표와의 정합성 설명
3. 접근성·형평성·비용 평가
4. (승인 시) AI Tool Inventory 등재

> **Chromebook판 VibeLearn AI의 경우**: 1번이 특수하다. **신규 벤더가 없기 때문**이다. 자체 서버·저장소가 없고 데이터는 학교가 이미 승인한 Google Workspace에 머문다. 이 점을 제안서 첫 문단에 배치하면 심사 부담이 크게 줄어든다. 상세는 [../concepts/district-policy-anatomy.md](../concepts/district-policy-anatomy.md).

## 주의

**정책은 자주 바뀐다.** 2026년 회기에만 27개 주에서 77건의 법안이 나왔고 10건이 제정됐다. 확인 시점을 기록하고, 6개월 이상 지났으면 재확인한다.

**문서에 없다고 허용된 것은 아니다.** 특히 정책 공백기에는 담당자 판단이 실질 기준이 된다. 애매하면 문서로 확인받아 둔다.

## 참조

- [../concepts/three-layer-governance.md](../concepts/three-layer-governance.md) — 층위 판정
- [../concepts/district-policy-anatomy.md](../concepts/district-policy-anatomy.md) — 학군 정책의 전체 구조
- [../concepts/age-gates-by-tool.md](../concepts/age-gates-by-tool.md) — 연령 제한
- [../concepts/legal-frame-cipa-coppa-ferpa.md](../concepts/legal-frame-cipa-coppa-ferpa.md) — 법률 판정
