# Clearly 앱 사용 가이드: BRD/PRD 작성부터 AI 코딩 도구 연동까지

**작성일**: 2026-02-15
**기반 경험**: 3회 반복 실습 (2026-02-08, 02-14, 02-15)
**대상 독자**: Clearly 앱을 처음 사용하는 학습자, Vibe Coding에 관심 있는 개발자/비개발자

---

## 1. Clearly 앱이란?

Clearly(https://www.clearlyreqs.com/)는 AI 기반 BRD/PRD 생성 플랫폼입니다. 대화형 Wizard를 통해 질문에 답하면서 요구사항 문서를 체계적으로 작성할 수 있으며, 완성된 문서를 AI 코딩 도구(Claude Code, Cursor, v0 등)에 최적화된 설정 파일로 변환해주는 것이 핵심 가치입니다.

### 핵심 워크플로우

```
Create Project → BRD Wizard → Approve BRD → PRD Wizard → Approve PRD → Choose Output Tool
    (0%)           (20%)        (33%)         (50%)        (67%)           (100%)
```

### 누구를 위한 도구인가?

- **비기술자**: AI Wizard가 질문과 예시 답변으로 안내하므로 기술 지식 없이도 BRD/PRD 작성 가능
- **1인 개발자/PO**: Vibe Coding 시작 전 요구사항을 체계화하고, AI 코딩 도구 설정 파일까지 자동 생성
- **학습자**: BRD/PRD 작성 방법을 실습하면서 배울 수 있는 실전 도구

---

## 2. 시작하기: 프로젝트 생성

### Step 1: 로그인 및 New Project

1. https://www.clearlyreqs.com/ 접속
2. 로그인 (Google 계정 등)
3. 대시보드에서 **"New Project"** 또는 **"+ Create Project"** 클릭

### Step 2: 프로젝트 기본 정보 입력

| 필드 | 설명 | 팁 |
|------|------|-----|
| **Project Title** | 프로젝트 이름 (필수) | 명확하고 구체적인 이름 권장 |
| **Initial Idea** | 프로젝트 설명 (최소 20자, 최대 ~2,000단어) | 상세할수록 Wizard 질문 품질이 올라감 |
| **Output Language** | 출력 언어 선택 | 한국어, 영어 등 선택 가능 |

### Tip: Initial Idea 잘 작성하기

Initial Idea의 상세도에 따라 Wizard 질문의 수와 깊이가 달라집니다.

**나쁜 예시**: "홈페이지를 만들고 싶습니다"
**좋은 예시**: "YouTube 채널의 5가지 핵심 콘텐츠를 소개하는 정적 웹사이트를 구축하려 합니다. 타겟은 AI에 관심 있는 개발자/비개발자이며, Amazon S3로 호스팅하고 한국어/영어 다국어를 지원합니다."

포함하면 좋은 정보:
- 프로젝트의 목적과 배경
- 타겟 사용자
- 핵심 기능 3-5개
- 기술적 제약사항 (예산, 기술 스택 제한)
- 구체적인 URL, 리소스 링크

---

## 3. BRD Wizard: 비즈니스 요구사항 정의

### 진행 방식

- AI가 질문을 하나씩 제시하고, 각 질문에 **Example Answers 3개**를 제공
- 진행률 표시: "Questions answered: X/5+" 및 퍼센트 바
- 최소 질문 수를 넘기면 **"Generate BRD"** 버튼 활성화
- 추가 질문에 계속 답변 가능 (더 완성도 높은 BRD 생성)

### 주요 질문 영역

3회 실습에서 확인한 BRD Wizard의 주요 질문 영역:

| 영역 | 설명 | 답변 팁 |
|------|------|---------|
| 비즈니스 목표 | 프로젝트의 궁극적 목표, 기존 문제 해결 | 측정 가능한 성공 지표(KPI) 포함 |
| 기술 스택/아키텍처 | 시스템 구조, 외부 서비스 연동, 제약사항 | 구체적 기술명과 선택 이유 명시 |
| 타겟 사용자/UX | 핵심 사용자, UX 디자인 강조점 | 사용자 유형별 기대 행동 설명 |
| 콘텐츠 관리 | 업데이트 방식, 일관성 유지 방안 | 운영 주체와 프로세스 구체적으로 |
| 리스크/제약 | 예산, 시간, 기술적 위험 | 위험 완화 전략 함께 제시 |

### Tip: Wizard 질문은 매번 달라진다

동일한 프로젝트를 반복 생성해도 Wizard 질문이 매번 약간 달라집니다. Initial Idea의 상세도와 이전 답변의 내용에 따라 AI가 적응적으로 질문을 생성합니다.

- Session 1: 5개 질문
- Session 2: 3개 질문 (Initial Idea가 더 상세했음)
- Session 3: 4개 질문

### BRD 생성 후

1. **검토**: 생성된 BRD를 꼼꼼히 읽고 부정확한 내용 확인
2. **내보내기**: Markdown(권장) 또는 PDF로 로컬 저장 — **반드시 백업!**
3. **Approve**: "Approve Document" 클릭 → PRD Wizard 잠금 해제

---

## 4. PRD Wizard: 제품 요구사항 상세화

### BRD와의 차이

- **BRD**: "왜(Why)"와 "무엇(What)" — 비즈니스 관점
- **PRD**: "무엇(What)"과 "어떻게(How)" — 기술/구현 관점

PRD Wizard는 BRD 내용을 자동 참조하여 더 구체적이고 기술적인 질문을 생성합니다.

### 주요 질문 영역

3회 실습에서 확인한 PRD Wizard의 주요 질문 영역:

| 영역 | 설명 | BRD와의 연결 |
|------|------|-------------|
| 기술 스택 상세 | 프레임워크, 빌드 도구, 구현 방식 | BRD의 Technical Context를 구체화 |
| API/데이터 연동 | 외부 서비스 연동 방식, 데이터 모델 | BRD의 Dependencies를 상세화 |
| 다국어/확장성 | 구현 방식, 장기 전환 계획 | BRD의 Scalability를 구체화 |
| 디자인 시스템 | UI 일관성, CSS 구조, AI 도구 활용 | BRD의 Usability를 구현 수준으로 |
| 상호작용/분석 | 사용자 데이터 수집, GA4 설정 | BRD의 Success Metrics 측정 방법 |

### PRD 생성 결과

PRD는 BRD보다 훨씬 상세한 문서가 생성됩니다 (12개 섹션):

1. Product Overview (비전, 목표, 타겟, 성공 기준)
2. Technical Architecture (시스템 구조, 기술 스택, 컴포넌트, 연동점)
3. User Stories & Use Cases
4. Feature Requirements (Core Features 테이블, Feature Specs, UI Requirements)
5. API Specifications
6. Data Models
7. Security & Compliance
8. Performance Requirements
9. Testing & Quality Assurance
10. Deployment & DevOps
11. Timeline & Milestones
12. Assumptions & Constraints

---

## 5. Choose Output Tool: AI 코딩 도구 연동

### 사용 가능한 도구

PRD Approve 후 "Choose Output Tool" 화면에서 개발 도구를 선택합니다:

**Vibe Coding Tools** (AI 기반 비주얼 빌더):
- v0 (Vercel), Loveable, Bolt.new, Replit, Firebase Studio

**AI Coding Tools** (코드 중심 개발):
- **Claude Code**, Cursor, OpenAI Codex, Google Antigravity

### Claude Code 선택 시 생성되는 산출물

| 파일 | 용도 |
|------|------|
| **CLAUDE.md** | 프로젝트 지시사항 (아키텍처, 코딩 컨벤션, 파일 구조) |
| **.claude/settings.json** | 프로젝트 메타데이터, 기술 스택, 타겟 설정 |
| **REFERENCE_DOCUMENT.md** | BRD/PRD 통합 종합 참조 문서 |

### 활용 방법

1. 다운로드한 ZIP을 프로젝트 루트에 배치
2. `claude` 명령어로 Claude Code 실행
3. Claude Code가 CLAUDE.md를 자동으로 읽고 프로젝트 컨텍스트를 이해
4. Vibe Coding 시작!

---

## 6. 실전 팁 모음

### Tip 1: 반복(Iteration)으로 품질 높이기

BRD/PRD 작성은 1회성이 아니라 **반복할수록 품질이 높아집니다**.

| 회차 | 특징 | 효과 |
|------|------|------|
| 1회차 | 첫 시도, Wizard 학습 | 기본 구조 파악 |
| 2회차 | 이전 답변 재활용, 빠른 진행 | 경험 기반 효율 향상 |
| 3회차 | 이전 답변 + 새 질문의 갭 보강 | 누락 내용 추가, 최고 품질 |

실제 경험: Session 1(2h, BRD만) → Session 3(1.5h, 전체 완료)

**방법**: 이전 세션의 Wizard 답변을 주제별로 정리해두고, 새 세션에서 활용하면서 새 질문에서 발견된 관점을 추가합니다.

### Tip 2: 답변은 미리 준비하기

Wizard 답변을 텍스트 파일로 미리 작성해두면:
- 복사/붙여넣기로 빠르게 진행 가능
- 세션 만료 위험 최소화
- 일관된 품질 유지

### Tip 3: 항상 로컬에 백업

Clearly 앱에서 대시보드 표시 관련 버그가 있을 수 있으므로:
- BRD/PRD 생성 즉시 **Markdown으로 Export**하여 로컬에 저장
- Output Tool 산출물은 **Download ZIP**으로 즉시 다운로드
- 대시보드로 돌아가기 전에 모든 산출물 백업 완료

### Tip 4: Example Answers 활용법

Wizard의 Example Answers는 답변 방향을 잡는 데 유용합니다:
- 3개 예시를 모두 읽고 공통 패턴 파악
- 예시의 구조(섹션 나누기, 구체적 수치 포함)를 참고
- 단, 예시를 그대로 복사하지 말고 실제 프로젝트에 맞게 커스텀

### Tip 5: BRD와 PRD의 답변 연결

BRD Wizard에서 답변한 내용이 PRD Wizard 질문에 반영됩니다:
- BRD에서 "정적 웹사이트"라고 하면 PRD에서 "어떤 빌드 도구를 사용할지" 물어봄
- BRD에서 "다국어 지원"을 언급하면 PRD에서 "구체적 구현 방식"을 물어봄
- 따라서 BRD에서 가능한 구체적으로 답변하면 PRD도 더 정확한 질문을 받을 수 있음

---

## 7. 알려진 이슈 및 워크어라운드

### Bug: 대시보드에서 프로젝트가 사라지는 현상

**현상**: 프로젝트 생성 및 BRD/PRD/Output 완료 후 대시보드로 돌아가면 "No projects yet" 표시
**빈도**: 3회 연속 재현 (2026-02-08 ~ 02-15)
**워크어라운드**:
1. 대시보드로 돌아가지 않고 프로젝트 페이지 내에서 모든 단계를 연속 진행
2. 각 단계 완료 시 즉시 Markdown/PDF Export로 로컬 백업
3. Output Tool은 Download ZIP으로 즉시 다운로드

### 과거 수정된 버그

| 버그 | 수정 상태 |
|------|----------|
| BRD 날짜 자동 생성 오류 (2023년으로 표시) | ✅ Fixed |
| PRD Wizard 중 세션 만료 | ✅ Fixed |
| 재로그인 후 프로젝트 목록 접근 불가 | ✅ Fixed |

---

## 8. Clearly 활용 시나리오

### 시나리오 1: Vibe Coding 프로젝트 시작

```
아이디어 정리 → Clearly에서 BRD/PRD 작성 → Output Tool로 Claude Code 설정 생성
→ 프로젝트 루트에 CLAUDE.md 배치 → Claude Code로 Vibe Coding 시작
```

### 시나리오 2: 요구사항 문서 학습

```
Sample 프로젝트로 BRD Wizard 체험 → BRD 구조와 섹션 이해
→ PRD Wizard 체험 → BRD와 PRD의 차이 이해 → 반복하며 품질 향상
```

### 시나리오 3: 팀 프로젝트 요구사항 정리

```
PM이 Initial Idea 작성 → Clearly에서 BRD 생성 → 이해관계자 검토
→ PRD 생성 → 개발팀 공유 → Output Tool로 개발 환경 설정
```

---

**작성자**: CUA_VL 학습자
**방법론**: CUA_VL (VibeLearn AI)
**기반**: Catch Up AI 2026 Homepage 프로젝트 3회 반복 실습
