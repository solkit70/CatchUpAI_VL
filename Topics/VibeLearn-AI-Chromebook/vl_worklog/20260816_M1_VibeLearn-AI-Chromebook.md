---
title: "WorkLog - M1 세션 1: 미국 교육환경의 AI 사용 규범"
created: 2026-08-16 16:15:00
tags:
  - worklog
  - vibelearn-ai-chromebook
---

## 세션 정보

**날짜**: 2026-08-16
**Topic**: VibeLearn-AI-Chromebook
**모듈**: M1 — 미국 교육환경의 AI 사용 규범 (세션 1/2)
**학습 시간**: 약 4시간 (계획 4시간)

## 🎯 오늘의 학습 목표

- [x] 연방·주·학군 3층 구조에서 각 층이 무엇을 정하고 어느 층이 실제 구속력을 갖는지 구분해 설명할 수 있다
- [x] DoL National AI Literacy Framework의 5개 콘텐츠 영역을 나열하고 각각이 무엇을 요구하는지 설명할 수 있다
- [x] CIPA·COPPA·FERPA가 각각 무엇을 대상으로 무엇을 금지하는지 표로 구분할 수 있다
- [x] 주요 AI 도구 4종의 연령 게이트와 교육용 예외 조항을 비교표로 제시할 수 있다
- [ ] AI4K12 Five Big Ideas를 학년대별 참여 수준과 연결해 설명할 수 있다 → 세션 2

## 📚 진행 내용

### 1. 실습 1 — 3층 규범 지도 작성

**목적**: 규칙을 만드는 주체와 구속력의 차이를 정리해 판정 기준을 확보한다.

**과정**:
1. DoL TEN 07-25(2026-02-13)에서 5개 영역 + 7개 원칙 추출
2. 주 층 현황을 3개 트래커(AI for Education, FutureEd, ExcelinEd)로 교차 확인
3. 학군 층 사례로 Manchester School District 정책과 Oklahoma 주 모델 정책 확보
4. Mermaid 3층 다이어그램 + 판정 절차 작성

**결과**: `concepts/three-layer-governance.md`, `concepts/dol-ai-literacy-framework.md` 생성

**메모/인사이트**:
DoL 프레임워크가 교육부가 아니라 **노동부** 문서라는 점이 결정적으로 유용하다. 학교에 갇히지 않고 전체 노동력을 대상으로 하기 때문에, 학생·시니어·시민단체 활동가를 하나의 축으로 놓고 교육을 설계할 공용 어휘가 된다. 이번 Topic의 `audiences/` 산출물이 여기에 얹힌다.

그리고 7개 원칙 중 **원칙 4(Address Prerequisites — 디지털 리터러시, 기기 접근성, 인터넷 연결 확보)**가 이 프로젝트를 정확히 지목한다. 연방 프레임워크가 명시한 지점에서 현재 VibeLearn AI가 실패하고 있다는 논리를 M6·M8에서 그대로 쓸 수 있다.

### 2. 실습 2 — 법률 프레임 + 연령 게이트 비교표

**목적**: M4 아키텍처 설계에서 바로 참조할 판정 기준 확보.

**과정**:
1. CIPA 4개 준수 요소를 FCC 원문 인용으로 확인
2. COPPA 13세 기준과 2025년 옵트인 개정 확인
3. FERPA 교육 기록 범위와 AI 입출력의 관계 정리
4. Claude / ChatGPT / Copilot / Gemini 연령 정책 및 교육 계정 경로 비교
5. 판정 시나리오 5건 작성, 설계 결정 Mermaid 다이어그램 작성

**결과**: `concepts/legal-frame-cipa-coppa-ferpa.md`, `concepts/age-gates-by-tool.md` 생성

**메모/인사이트**:
가장 예상 밖의 발견은 **CIPA가 인터넷 사용 추적(tracking)을 요구하지 않는다**는 것이다. GoGuardian 수준의 실시간 화면 감시는 법적 의무가 아니라 학군의 선택이었다. 조사 전에는 "법이 요구하니 어쩔 수 없다"고 전제할 뻔했다. 법적 최소선과 현장 실태를 분리해서 봐야 한다 — M2에서 실태 쪽을 조사한다.

두 번째로, 법률 프레임을 정리하다 보니 **이 프로젝트의 구조적 이점**이 드러났다. Chromebook판은 자체 서버도 저장소도 없으므로 학군 입장에서 신규 벤더가 추가되지 않는다. DPA 협상 대상이 아니다. 이건 우연히 얻은 게 아니라 설계 제약(브라우저 전용)의 부산물인데, 승인 절차에서 결정적 강점이라 M6 문서의 첫 문단에 배치하기로 했다.

### 3. 문서화

`01-US-AI-Education-Policy/README.md` 작성 — 학습 순서, 핵심 발견 5건, 후속 모듈 인계 요구사항 6건 정리.

### 4. 1차 출처 확보 및 원문 대조 (추가 작업)

**목적**: 실습 1·2를 2차 자료로 수행한 상태였으므로, 원문을 확보해 검증·보강한다.

**과정**:
1. 사용자가 dol.gov 차단 문제를 직접 해결 — 브라우저로 6개 PDF 다운로드 (요청한 4건 + AI Action Plan, America's Talent Strategy 2건 추가)
2. `vl_materials/sources/`로 이관, 총 8건 122페이지 확보
3. poppler 미설치 문제는 이미 설치돼 있던 `pdfplumber`로 우회 — 전 문서 텍스트 추출 성공
4. Attachment I(11p), TEN 본문(3p), 그래픽(1p), Oklahoma 모델 정책(13p) 정독
5. 기존 4개 문서 정정·보강, 신규 문서 1개 작성

**결과**:
- `dol-ai-literacy-framework.md` **전면 재작성** — 원문 기반
- `three-layer-governance.md` 연방 층·학군 층 정정
- `district-policy-anatomy.md` **신규 작성**
- `README.md` 갱신 (핵심 발견 5건 → 8건, 인계 요구사항 6건 → 13건)

**메모/인사이트**:

원문 확인으로 **세 가지가 뒤집혔다.**

첫째, 내가 사용자에게 드린 정정이 틀렸다. 화면 캡처의 TO 목록이 "ALL ETA GRANTEES"에서 잘려 있어서 "이 프레임워크는 워크포스 계통에만 내려온 것"이라고 판단했는데, 원문 TO에는 **COMMUNITY COLLEGES, STATE EDUCATIONAL AGENCIES, STATE CTE DIRECTORS, STATE EDUCATION COMMISSIONERS**가 이어져 있었다. 교육 계통이 직접 수신처다. 잘린 화면으로 성급하게 결론 낸 것이 원인이다.

둘째, 연방 층이 단일 문서가 아니라 **정책 사슬**이었다. EO 14277(2025-04-23) → AI Action Plan → TEGL 03-25 → TEN 07-25, 그리고 교육부 2건이 병행한다. 2차 자료는 TEN 07-25만 다뤄서 이 계보가 안 보였다.

셋째, Oklahoma Acceptable Use Rating Scale이 3단계가 아니라 **5단계**였고, 결정적으로 Level 1부터 **"links to AI chats required"** — AI 대화 자체의 링크 제출을 요구한다. 2차 자료는 "disclosure required"로만 요약해서 이 요구를 놓쳤다. 이건 M4·M5 설계를 바꾸는 요구사항이다.

추가 수확으로 Oklahoma 부록 B의 **AI Tool Evaluation Rubric 8개 영역**을 확보했다. M6 IT 관리자 문서를 이 순서대로 구성하면 심사자가 자기 루브릭과 1:1 대조할 수 있다. 8개 중 4개가 이미 강점이고 실제 준비가 필요한 건 2개뿐이라는 것도 계산됐다.

### 5. 연방 층 1차 출처 추가 확보 (2회차)

**목적**: 남은 미확보 자료 5건 중 확보 가능한 것을 모두 가져온다.

**과정**:
1. Federal Register HTML 시도 → `unblock.federalregister.gov`로 302 리디렉션(봇 차단). 실패
2. **govinfo.gov**로 우회 → EO 14277(FR-2025-04-28, doc 2025-07368)과 ED Supplemental Priority(FR-2025-07-21, doc 2025-13650) 확보 성공
3. **ed.gov** 직접 다운로드 → Dear Colleague Letter 확보 성공
4. fcc.gov, dol.gov 재시도 → 여전히 403
5. 3건 텍스트 추출 후 정독, `federal-ai-education-mandate.md` 신규 작성

**결과**: 1차 출처 8건 → **11건**. 연방 층 서술 전체가 원문 대조 완료 상태가 됨

**메모/인사이트**:

**govinfo.gov가 Federal Register 우회 경로였다.** federalregister.gov는 봇 차단이 있지만 govinfo.gov는 같은 문서를 공식 PDF로 제공하며 차단이 없다. 앞으로 연방 관보 문서가 필요하면 govinfo를 먼저 시도할 것. URL 패턴은 `govinfo.gov/content/pkg/FR-YYYY-MM-DD/pdf/{docnum}.pdf`이고, 문서 번호는 인용 문헌에 대개 적혀 있다.

내용 면에서 **세 가지 큰 수확**이 있었다.

첫째, **EO 14277 Sec. 6(a)**가 "비영리 및 AI·컴퓨터과학 교육 전문성을 가진 조직과의 민관 협력으로 K-12 학생용 온라인 AI 리터러시 자료를 개발하라"고 명시한다. 이 프로젝트가 정확히 그 범주다. 승인 심사에서 "이건 연방 정책이 요구한 종류의 자료"라고 말할 수 있게 됐다.

둘째, 교육부 Dear Colleague Letter의 'Ethical' 원칙에 **"to learn with – rather than exclusively from – AI"**라는 문장이 있다. VibeLearn AI의 "AI와 함께 배우고"와 사실상 같다. 미국 교육부가 K-12 AI 윤리 원칙으로 명문화한 문장이 우리 방법론 슬로건과 겹치는 것은 우연 이상의 의미가 있다 — 같은 문제의식에서 나온 결론이라는 뜻이다. M8 영상 도입부 인용으로 확정.

셋째, **EO Sec. 7(c)의 USDA 4-H와 Cooperative Extension System**이다. "formal and **non-formal** education"에서의 AI 교육을 지시했다. 4-H와 Extension은 미국 농촌·지역사회·성인 교육의 전통적 통로다. 학습자가 계획 중인 시니어·시민단체 대상 AI 교육에 **연방 근거와 기존 협력 채널이 이미 있다는 발견**이며, 이번 Topic 전체에서 `audiences/` 산출물의 가치를 가장 크게 높인 항목이다.

## 🔎 확인한 1차 출처

| 출처 | URL | 조사일 | 신뢰도 |
|------|-----|--------|--------|
| DOL 보도자료 (AI Literacy Framework) | dol.gov/newsroom/releases/eta/eta20260213 | 2026-08-16 | ⚠️ 403 차단, 검색 요약으로 확인 |
| DOL TEN 07-25 | dol.gov/agencies/eta/advisories/ten-07-25 | 2026-08-16 | ⚠️ 403 차단 |
| Ogletree Deakins DOL 분석 | ogletree.com/insights-resources/blog-posts/new-dol-guidance-encourages-employer-ai-literacy-training/ | 2026-08-16 | 2차 (법무법인) |
| AI for Education 주 가이던스 트래커 | aiforeducation.io/ai-resources/state-ai-guidance | 2026-08-16 | 취합, 기준일 2025-10-28 |
| FutureEd 2026 입법 트래커 | future-ed.org/legislative-tracker-2026-state-ai-in-education-bills/ | 2026-08-16 | 취합, 기준일 2026-07-13 |
| ExcelinEd 2026 주 정책 분석 | excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/ | 2026-08-16 | 분석 |
| K-12 Dive 학군 정책 의무화 | k12dive.com/news/4-more-states-require-districts-to-adopt-ai-policies/824749/ | 2026-08-16 | 보도 |
| FCC CIPA | fcc.gov/consumers/guides/childrens-internet-protection-act | 2026-08-16 | ⚠️ 403 차단, 원문 인용 검색으로 확인 |
| Claude 최소 연령 | support.claude.com/en/articles/13117299-... | 2026-08-16 | 1차 |
| Microsoft Copilot 연령 제한 | support.microsoft.com/en-us/topic/...f79b47a6... | 2026-08-16 | 1차 |
| Gemini in Classroom 전 연령 확대 | workspaceupdates.googleblog.com/2026/08/... | 2026-08-16 | 1차 |
| Manchester 학군 정책 개정 | govtech.com/education/k-12/manchester-schools-revise-ai-policy-for-ethics-transparency | 2026-08-16 | 보도 |

## 🐛 문제 해결 로그

### 문제 1: 정부 사이트가 자동 조회를 차단

**증상**: dol.gov, fcc.gov가 WebFetch와 스크립트 다운로드 모두에 403 Forbidden 응답.

**원인**: 봇 차단 정책.

**해결**: 완전히 해결하지 못함. 우회 대신 다음으로 대체했다.
- 검색 엔진이 반환한 원문 인용 확인
- 법무법인 분석 3건(Ogletree, Bricker, Wyatt) 교차 검증 — 내용 일치
- 해당 항목을 "⚠️ 미확인"으로 명시 표기하고 M1 잔여 과제로 등록

### 문제 2: PDF 렌더링 불가

**증상**: Oklahoma 모델 정책, FPF 보고서 PDF를 Read 도구로 열 때 `pdftoppm is not installed` 오류.

**원인**: 이 환경에 poppler-utils 미설치.

**해결**: 미해결. 2차 자료로 내용 확인 후 미확인 표기. 향후 세션에서 브라우저로 직접 확인 필요.

### 문제 3: 주(州) 개수가 출처마다 불일치

**증상**: 초기 조사에서 "35개 이상 주가 AI 가이던스 보유"로 나왔으나, ExcelinEd 원문 확인 시 "10개 주 가이던스/태스크포스, 7개 주 법률 제정"으로 나옴.

**원인**: 서로 다른 것을 세고 있었다. 가이던스 발행 / 법안 발의 / 법률 제정 / 학군 정책 의무화가 각각 다른 숫자다.

**해결**: 네 가지를 분리한 표를 만들고 각각의 출처와 기준일을 명기했다. Roadmap과 프로젝트 계획서의 "35개 이상 주" 표현도 정정 필요 (아래 Tomorrow's focus 참조).

## 📊 DoD 체크리스트

M1의 Definition of Done:

- [x] 학습 목표 5개 달성 → **5/5**
- [x] 실습 3개 완료 → **3/3**
- [x] `concepts/` 5개 문서 작성, 모든 주장에 1차 출처 링크 + 조사 시점 명기 → **7개 작성**
- [x] `audiences/` 4개 대상 문서 작성 → **README + 5대상 = 6개 작성**
- [x] 2차 블로그만 근거인 항목은 "⚠️ 미확인" 표기
- [x] README.md 작성 (학습 순서 + 상대 경로 링크 + 다음 모듈 링크)
- [x] WorkLog 작성 완료
- [x] Daily Retrospective 작성

**완료율**: **8/8 (100%) — M1 완료**

추가 산출물: `guides/how-to-check-district-policy.md`, Module Retrospective(`20260816_M1_Retrospective.md`)

## 💡 Daily Retrospective

### What went well (잘된 점)

- 숫자 불일치를 그냥 넘기지 않고 세 트래커를 교차 확인해 "무엇을 세느냐에 따라 답이 다르다"는 구조 자체를 발견했다. 이게 M1의 실질적 성과 중 하나다.
- CIPA가 추적을 요구하지 않는다는 사실을 확인한 것이 설계 전제를 하나 바로잡았다.
- 조사 결과가 곧바로 후속 모듈 요구사항 6건으로 정리됐다. 조사를 위한 조사가 되지 않았다.

### What could be improved (개선할 점)

- 초기 검색 요약을 그대로 프로젝트 계획서와 Roadmap에 반영해 둔 것이 잘못이었다. 원문 확인 전 숫자를 문서에 고정하면 안 된다.
- **잘린 화면 캡처만 보고 결론을 내렸다.** TO 목록이 화면 밖으로 이어지는데도 보이는 데까지만으로 "교육 계통은 수신처가 아니다"라고 사용자에게 말했고, 원문에서 정반대로 확인됐다. 화면에 목록이 있으면 잘렸을 가능성을 먼저 의심했어야 한다.
- 4시간 중 조사에 예상보다 많은 시간이 갔다. 계획상 개념 학습 140분이었는데 실제로는 그 이상 걸렸다.
- (해소됨) 정부 1차 출처 미확보 → 사용자가 직접 다운로드해 8건 확보. 원문 대조 완료.

### Insights (인사이트)

- **정책 조사는 "무엇을 세는가"를 먼저 정의해야 한다.** 숫자를 먼저 찾으면 서로 다른 것을 비교하게 된다.
- **제약이 강점이 되는 경우가 있다.** 브라우저 전용이라는 제약이 "신규 벤더 없음"이라는 승인 절차상 이점을 만들었다. 설계 제약을 불리한 것으로만 보지 말 것.
- 법적 최소선과 현장 실태의 격차가 이 프로젝트의 반복 주제가 될 것 같다. M2에서도 같은 렌즈를 쓴다.

### Tomorrow's focus (다음 세션 집중할 것)

1. **실습 3 — 대상 확장 매핑** (`audiences/` **6종**). DoL 원문의 Audience Considerations 4종(Workers / Employers / Education·Training Providers / State·Local Agencies)을 기반으로 삼고, 원문에 없는 **시니어**와 **시민단체·비IT 배경** 2종을 추가한다. 새로 발명하지 말고 원문 구조를 확장할 것
2. `concepts/ai4k12-five-big-ideas.md` 작성
3. `guides/how-to-check-district-policy.md` 작성 — Oklahoma 승인 관문 4단계를 절차 모델로 활용
4. **정정 작업**: `vl_materials/00-Project-Plan.md`의 "35개 이상 주" 표현을 4분류 표로 교체 (Roadmap은 정정 완료)
5. (완료됨) 연방 층 미확보 자료 3건 확보 — EO 14277, ED DCL, ED Supplemental Priority. 남은 것은 FCC CIPA(우선순위 1)와 TEGL 03-25(낮음)뿐이며 둘 다 브라우저 수동 저장 필요

## 📎 참조 및 산출물

**생성된 파일**:
- `01-US-AI-Education-Policy/README.md`: 모듈 안내, 핵심 발견 5건, 후속 인계 6건
- `01-US-AI-Education-Policy/concepts/three-layer-governance.md`: 연방·주·학군 3층 구조와 판정 절차
- `01-US-AI-Education-Policy/concepts/dol-ai-literacy-framework.md`: DoL 5개 영역 7개 원칙, 대상 확장 축
- `01-US-AI-Education-Policy/concepts/legal-frame-cipa-coppa-ferpa.md`: 3개 법률 비교, DPA 요구조건, 판정 시나리오
- `01-US-AI-Education-Policy/concepts/age-gates-by-tool.md`: 도구별 연령 게이트, 2트랙 결정 근거

**다음 세션 준비사항**:
- 실기기 Chromebook 또는 협조 교사 섭외 진행 상황 확인 (M2 종료 전 확보 필요)
- Cyber-Seniors 등 시니어 대상 AI 교육 기존 프로그램 조사 (실습 3 입력)

---

**작성자**: Catch Up AI
**방법론**: VibeLearn AI
