---
title: "학군 AI 정책의 해부 — Oklahoma 주 모델 정책 원문 분석"
created: 2026-08-16 19:00:00
tags:
  - ai-education
  - us-policy
  - district-policy
---

## 이 문서가 답하는 질문

학군 AI 정책은 실제로 무엇을 담고 있는가? 새 도구가 승인을 받으려면 어떤 관문을 통과해야 하는가?

**조사 시점**: 2026-08-16 · **출처**: Oklahoma State Department of Education 모델 정책 원문 13p (본문 + 부록 A~F)
**핵심 결론**: 학군 정책은 사용 규칙만이 아니라 **도구 평가 루브릭·위험 등급·부모 동의 절차·공개 도구 목록**까지 포함하는 완결된 체계다. Oklahoma의 8개 평가 영역은 Chromebook판 VibeLearn AI가 통과해야 할 심사표 그 자체이며, 그중 두 항목은 오히려 우리에게 유리하다.

Oklahoma를 표본으로 삼은 이유는 SB1734로 학군 AI 정책 채택을 의무화한 6개 주 중 하나이고, 주 교육청이 **편집 가능한 모델 정책과 부록 6종**을 배포해 학군 정책의 표준 형태를 가장 명확하게 보여주기 때문이다.

## 1. Acceptable Use Rating Scale — 5단계 원문

학생의 AI 사용 수준을 5단계로 나누고 단계별 공개 의무를 지정한다.

| 레벨 | 사용 수준 | 학생 의무 |
|---|---|---|
| **Level 0** | No AI Use | 공개 불필요 |
| **Level 1** | Idea Generation Only (아이디어 생성만) | **공개 + AI 대화 링크** |
| **Level 2** | Editing Only (편집만) | **공개 + AI 대화 링크** |
| **Level 3** | Specific Task with Teacher Oversight (교사 감독 하 특정 과제) | **인용 + 링크** |
| **Level 4** | Full AI Use with Reflection (성찰을 동반한 전면 사용) | **인용 + 링크** |

### ⚠️ 여기서 나온 하드 요구사항 — "links to AI chats required"

Level 1부터 4까지 전부 **AI 대화 자체의 링크 제출**을 요구한다. 단순히 "AI를 썼습니다"라고 밝히는 수준이 아니라 **대화 기록을 교사가 열람할 수 있어야 한다.**

이것은 M4·M5 설계에 직접 영향을 준다.

- 학생 트랙의 AI 도구는 **대화 공유 링크를 생성할 수 있어야 한다.** Gemini의 대화 공유 기능이 학교 계정에서 작동하는지 M4에서 반드시 실측할 것
- WorkLog 템플릿의 AI 사용 표기 필드는 텍스트 한 줄이 아니라 **레벨 + 대화 링크** 두 항목을 가져야 한다
- 링크 공유가 학교 정책상 막혀 있다면 대화 내용을 Drive 문서에 붙여넣는 폴백 경로가 필요하다

> 이 발견 전까지 M5 요구사항은 "AI 사용 표기 필드 기본 탑재" 정도였다. 원문을 보고 나서야 **무엇을 표기해야 하는지**가 구체화됐다. 2차 자료만 봤다면 놓쳤을 항목이다.

## 2. 금지 사용 (Prohibited Uses)

1. 딥페이크 생성·유포
2. 괴롭힘, 사칭, 희롱
3. 표절·학업 정직성 정책 회피
4. 부적절·유해·불법 콘텐츠 접근 또는 전송

## 3. 도구 승인 관문 — 4단계

새 AI 도구는 채택 전 다음을 거친다.

1. 벤더의 프라이버시 및 데이터 처리 관행 검토
2. 교육·운영 목표와의 정합성 확인
3. **접근성, 접근 형평성, 비용** 평가
4. 승인된 도구를 학군의 **공개 AI Tool Inventory**에 게시

여기에 더해 모든 도구는 **위험 평가(Red / Yellow / Green)**를 받고, 벤더 프라이버시 문서와 유출 대응 프로토콜을 제출하며, FERPA·COPPA·주 사이버보안 표준 준수를 입증해야 한다.

## 4. AI Tool Evaluation Rubric — 8개 평가 영역 (M6 심사표)

부록 B의 평가 루브릭이다. **M6의 IT 관리자용 문서는 이 8개 항목에 미리 답해 두어야 한다.**

| # | 영역 | 평가 기준 (원문) | Chromebook판 예상 위치 |
|---|---|---|---|
| 1 | Instructional Alignment | 주 학업 표준 및 커리큘럼 목표와 정합 | ⚠️ 학군별로 매핑 근거 제시 필요 |
| 2 | **Accessibility & Equity** | IEP 학생, 영어 학습자, **농촌 저대역폭 제약**을 포함한 모든 학습자 접근 가능 | ✅ **강점** — 브라우저 전용 설계가 정확히 이 항목을 겨냥 |
| 3 | Data Privacy Compliance | FERPA·COPPA 준수, 동의 없는 PII 수집 없음 | ✅ **강점** — 신규 벤더·저장소 없음 |
| 4 | Transparency & Explainability | AI 결정·출력을 학생과 교사에게 명확히 설명 | ✅ 프롬프트 팩이 공개 텍스트라 완전 투명 |
| 5 | Bias & Fairness Protections | 인종·성별·장애 등 알고리즘 편향 방지 장치 | ⚠️ 기반 모델(Gemini) 책임 — 우리 층위 아님을 명시 |
| 6 | **Teacher Control & Oversight** | 교사가 프롬프트·필터·학생 사용을 통제 가능 | ⚠️ M4·M5 설계에 반영 필요 |
| 7 | Usability & Support | 사용 쉬움, 연수·튜토리얼·온보딩 지원 포함 | ✅ M6 산출물이 정확히 이것 |
| 8 | **Cost & Sustainability** | **무료 또는 저렴**, 명확한 라이선스, 장기 지속 가능 | ✅ **강점** — 무료 오픈 자료 |

최종 판정은 4단계: Approved for Pilot Use / Approved for District Use / Needs Further Review / Not Recommended.

> **전략적 함의**: 8개 중 4개(2·3·4·8)가 이미 강점이고, 2개(5·7)는 설명으로 해소되며, 실제로 준비가 필요한 것은 **1(표준 정합)과 6(교사 통제)** 뿐이다. M6 문서를 이 8개 항목 순서로 구성하면 심사자가 자기 루브릭과 1:1로 대조할 수 있다.

## 5. 부모·가정 대상 절차

Oklahoma 모델은 부록으로 **편집 가능한 템플릿 4종**을 제공한다.

- 부모·보호자 안내 이메일
- 가정용 FAQ 유인물 (평이한 언어)
- **부모·보호자 동의서** (FERPA·COPPA 정합, 옵트인/옵트아웃)
- AI Tool Evaluation / Risk Assessment 루브릭

학군은 연 1회 이상 가정 대상 AI 정보 세션을 열고, 지역사회 자문위원회를 두며, 공개 AI Tool Inventory를 유지하고, 연간 **공개 AI Impact Report**를 발간해야 한다.

> **M6 온보딩에 대한 함의**: 학생용·교사용·IT용 3종으로 잡았는데, **가정용 안내 1종을 추가**하는 것이 좋겠다. Oklahoma 템플릿 구조를 그대로 따르면 학군이 기존 절차에 끼워 넣기 쉽다. 분량은 1페이지 FAQ면 충분하다.

## 6. 연간 전문성 개발 의무

학군은 매년 AI 연수를 제공해야 한다.

| 대상 | 내용 |
|---|---|
| 전 교직원 | 기초, 윤리, 허용 사용 |
| 교사 | 수업 통합 전략, **공개 관행** |
| 관리자 | 감독, 준수, 정책 평가 |
| 기술 담당 | 인프라, 보안, 벤더 검증 |

> **기회**: 교사 대상 항목이 "수업 통합 전략과 공개 관행"이다. M6 교사용 매뉴얼과 M8 사용법 영상이 **학군의 연간 연수 자료로 그대로 쓰일 수 있는 형태**를 갖추면 채택 경로가 하나 더 열린다.

## 7. 법적 근거와 책임 조항

Oklahoma 모델 정책이 스스로 밝히는 정합 대상: OSDE AI Guidance(2025), 주지사 AI 태스크포스(2023), FERPA, COPPA, 주 사이버보안 표준.

정책에 따라 선의로 AI 도구를 사용하거나 오용한 결과에 대해 학군·직원·대리인은 책임을 지지 않는다는 면책 조항도 포함된다.

## 후속 모듈 인계

| 대상 | 요구사항 |
|---|---|
| **M4** | Gemini 대화 **공유 링크 생성**이 학교 계정에서 작동하는지 실측. 안 되면 폴백 설계 |
| **M4** | 교사 통제 가능성(루브릭 6번)을 설계 제약으로 명시 |
| **M5** | WorkLog AI 표기 필드 = **레벨(0~4) + 대화 링크** 2개 항목 |
| **M6** | IT 관리자 문서를 **8개 평가 영역 순서**로 구성 |
| **M6** | 가정용 1페이지 FAQ 추가 (3종 → 4종) |
| **M6** | 교사용 매뉴얼을 학군 연간 연수 자료로 쓸 수 있는 형태로 |
| **M2** | 다른 주(Tennessee·Maryland·Virginia 등) 모델 정책과 대조해 Oklahoma가 대표성이 있는지 확인 |

## 참조 자료

| 자료 | 유형 | 확보 상태 |
|---|---|---|
| Oklahoma 모델 정책 (본문 + 부록 A~F) | 1차 | ✅ `vl_materials/sources/OK-model-policy-AI-use-in-schools.pdf` |
| Oklahoma OSDE AI·디지털 학습 페이지 | 1차 | https://oklahoma.gov/education/services/standards-learning/artificial-intelligence--ai--and-digital-learning1.html |
| Guidance and Considerations for Using AI in Oklahoma K-12 Schools 2.0 | 1차 | ⬜ 미확보 |
| Manchester School District 정책 개정 | 보도 | https://www.govtech.com/education/k-12/manchester-schools-revise-ai-policy-for-ethics-transparency |

> ⚠️ **일반화 주의**: 이 문서는 Oklahoma **한 주의 모델 정책**을 분석한 것이다. 학군 정책의 표준 형태를 보여주는 좋은 표본이지만 전국 대표성은 검증되지 않았다. M2에서 최소 2개 주 모델 정책과 대조할 것.

## 다음 문서

- [three-layer-governance.md](three-layer-governance.md) — 이 학군 층이 3층 구조에서 차지하는 위치
- [legal-frame-cipa-coppa-ferpa.md](legal-frame-cipa-coppa-ferpa.md) — 정책이 근거로 삼는 법률들
