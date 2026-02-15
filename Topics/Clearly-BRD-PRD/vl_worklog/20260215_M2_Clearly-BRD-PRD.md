# WorkLog - M2: Catch Up AI BRD/PRD 실습 (Session 3)

**날짜**: 2026-02-15
**Topic**: Clearly-BRD-PRD
**모듈**: M2 - Catch Up AI BRD/PRD 실습
**학습 시간**: 약 1.5시간

---

## 오늘의 학습 목표

- [x] Bug #4 재현 확인 (대시보드 프로젝트 표시 여부)
- [x] 새 프로젝트 생성 및 BRD 재생성 (3회차)
- [x] BRD 검토, 내보내기 및 Approve
- [x] PRD Wizard 완료 및 PRD 생성 (3회차)
- [x] PRD 검토, 내보내기 및 Approve
- [x] **Choose Output Tool 단계 최초 완료 (Claude Code 선택)**
- [x] 산출물 로컬 저장 (BRD v3, PRD v2, Claude Code Output)
- [x] Bug #4 재현 확인 및 버그 리포트 업데이트
- [x] WorkLog 작성
- [x] Daily Retrospective 작성

---

## 진행 내용

### 1. Bug #4 재현 확인 (세션 시작)

**목적**: 어제(2/14) 보고한 Bug #4의 수정 여부 확인

**결과**:
- 대시보드: Total Projects: 0, Documents: 0 — Bug #4 여전히 재현
- 개발자에게 버그 리포트 공유 후 10시간 미만이므로 아직 수정 전으로 판단
- 예상대로 새 프로젝트를 생성하여 전체 워크플로우 반복 진행

---

### 2. BRD 생성 (3회차)

**목적**: BRD/PRD 반복 작성을 통한 품질 향상 및 Choose Output Tool 단계 도달

**과정**:
1. "New Project" → Project Title: "Catch Up AI 2026 Homepage" (Unified Mode)
2. BRD Wizard 질문 4개에 답변:
   - Q1: 비즈니스 목표 (YouTube 대비 새 가치, 기존 문제 해결 포함)
   - Q2: 기술적 연동 및 아키텍처 제약사항
   - Q3: 타겟 사용자 및 UX 디자인 강조점
   - Q4: 콘텐츠 관리/업데이트 프로세스 및 오류 최소화 방안
3. Generate BRD → Markdown Export → Approve

**결과**:
- BRD v3 생성 완료
- 로컬 저장: `brd/catchupai-2026-brd-v3.md`

**인사이트**:
- 이전 세션(v1, v2) 답변을 기반으로 새 질문의 갭을 메우는 방식으로 더 풍부한 답변 작성
- BRD Wizard 질문이 매 세션마다 약간씩 다름 — AI가 Initial Idea와 이전 답변을 분석하여 적응적으로 질문 생성

---

### 3. PRD 생성 (3회차)

**목적**: PRD 반복 작성 및 이전 미반영 내용(GA4, 개인정보 등) 보강

**과정**:
1. BRD Approve 후 "Start PRD Wizard" 클릭
2. PRD Wizard 질문 5개에 답변:
   - Q1: 핵심 기술 스택, 다국어 구현, YouTube 통합 방안
   - Q2: JSON 동적 로딩 전환, YouTube API 데이터 모델/캐싱, HTML vs API 관리 비교
   - Q3: 다국어 처리 확장성, 번역/업데이트 프로세스
   - Q4: 디자인 시스템 구축(CSS 변수), AI 코딩 도구 UI 일관성, PO 수정 가이드라인
   - Q5: 서버리스 상호작용 기능, GA4 이벤트 트래킹, 개인정보 보호
3. Generate PRD → Markdown Export → Approve

**결과**:
- PRD v2 생성 완료 (12개 섹션, v1 대비 크게 보강)
- 로컬 저장: `prd/catchupai-2026-prd-v2.md`

**인사이트**:
- PRD Wizard가 BRD 내용을 깊이 분석하여 더 구체적이고 기술적인 질문을 생성
- 이전 세션에서 미반영된 GA4 커스텀 이벤트, 개인정보 보호, 디자인 시스템 내용을 Q5에 통합하여 품질 향상
- PRD에 Timeline & Milestones, Performance Metrics, Deployment Strategy 등 새로운 섹션이 자동 생성됨

---

### 4. Choose Output Tool — 최초 완료

**목적**: Clearly의 전체 워크플로우(BRD → PRD → Output Tool)를 처음으로 끝까지 완료

**과정**:
1. PRD Approve 후 "Choose Output Tool" 화면 표시 (Project Progress: 67%)
2. "Claude Code" 선택 → "Generate Output" 클릭
3. 생성된 산출물:
   - **CLAUDE.md**: 프로젝트 지시사항 파일 (아키텍처, 코딩 컨벤션, 파일 구조 포함)
   - **.claude/settings.json**: 프로젝트 메타데이터, 기술 스택, 코딩 컨벤션 설정
   - **PRD.md**: Output용 PRD 문서
   - **REFERENCE_DOCUMENT.md**: BRD/PRD 종합 참조 문서
4. "Download ZIP" 클릭 → 로컬 다운로드
5. 프로젝트 폴더에 저장: `claude-code-output/`

**결과**:
- Clearly의 전체 3단계 워크플로우 최초 완료
- Claude Code에 바로 사용 가능한 프로젝트 설정 파일 획득
- 로컬 저장: `claude-code-output/` (CLAUDE.md, .claude/settings.json, PRD.md, REFERENCE_DOCUMENT.md, ZIP 백업)

**인사이트**:
- Clearly의 Output Tool은 BRD/PRD를 분석하여 선택한 개발 도구에 최적화된 설정 파일을 자동 생성
- Claude Code용 출력에는 Recommended Skills & Commands (/implement, /build, /test 등)와 Recommended MCP Servers (Context7, Playwright 등) 추천도 포함
- 이 산출물을 실제 프로젝트 루트에 배치하면 Claude Code가 프로젝트 컨텍스트를 자동으로 이해하고 Vibe Coding을 시작할 수 있음

---

### 5. Bug #4 재현 확인 (세션 종료)

**목적**: Output Tool 완료 후 대시보드 상태 확인

**결과**:
- 대시보드: Total Projects: 0, Documents: 0, Completion Rate: 0% — Bug #4 여전히 재현
- 3회 연속 동일 패턴 (Session 1: Bug #3, Session 2: Bug #4, Session 3: Bug #4 재현)
- 버그 리포트 업데이트 완료 (`notes/clearly-bug-report.md`)

**워크어라운드**:
- 대시보드로 돌아가지 않고 프로젝트 페이지 내에서 모든 단계를 완료
- 모든 산출물은 Markdown Export + Download ZIP으로 로컬에 저장하여 데이터 유실 방지

---

## DoD 체크리스트

로드맵 M2의 Definition of Done:

- [x] Clearly에서 "Catch Up AI 2026 Homepage" 프로젝트 생성
- [x] AI Wizard를 통해 BRD 생성 완료
- [x] BRD 검토 및 필요한 수정 완료
- [x] PRD 생성 완료
- [x] BRD/PRD 내보내기 완료
- [x] `02-CatchUpAI-BRD-PRD/` 폴더에 문서 저장
- [x] README.md 작성 (이전 세션에서 완료)
- [x] WorkLog 작성 완료
- [x] Daily Retrospective 작성

**추가 달성 (M2 초과)**:
- [x] Choose Output Tool 단계 완료 (Claude Code)
- [x] Output 산출물 로컬 저장

**완료율**: 9/9 + 2 bonus (100%+)

---

## Daily Retrospective

### What went well (잘된 점)
- **Clearly 전체 워크플로우 최초 완료**: BRD → PRD → Choose Output Tool (Claude Code)의 3단계를 처음으로 끝까지 경험
- 3회차 반복이라 Wizard 답변 준비가 빠르고, 이전 답변의 갭을 보강하여 품질 향상
- 이전 세션에서 미반영된 GA4, 개인정보, 디자인 시스템 내용을 성공적으로 통합
- Bug #4 워크어라운드(대시보드 미이동)로 전체 플로우를 중단 없이 완료

### What could be improved (개선할 점)
- Wizard 질문이 매번 달라지므로, 이전 답변을 질문별이 아닌 주제별로 정리해두면 더 빠르게 대응 가능
- PRD 생성 시 이전 세션의 모든 답변을 한 문서에 모아두면 누락 방지에 도움

### Insights (인사이트)
- **반복을 통한 BRD/PRD 품질 향상**: BRD/PRD 작성은 1회성이 아니라 반복(iteration)할수록 품질이 높아진다. 이전 세션의 답변 + 새 세션의 질문에서 발견된 새로운 관점을 결합하면, 문서의 완성도가 점진적으로 올라간다. (v1 → v2 → v3로 갈수록 더 구체적이고 포괄적인 문서가 됨)
- **Clearly의 Output Tool**: BRD/PRD를 개발 도구(Claude Code, Cursor, v0 등)에 최적화된 설정 파일로 자동 변환해주는 기능이 핵심 가치. Vibe Coding의 출발점이 되는 산출물을 생성
- **Wizard 질문의 적응성**: 동일한 프로젝트를 반복 생성해도 Wizard 질문이 매번 약간 달라짐. Initial Idea의 상세도와 이전 답변의 내용에 따라 AI가 질문을 적응적으로 생성하는 것으로 보임
- **Bug #4 패턴**: 3회 연속 재현으로 안정적인 재현 패턴이 확인됨. 프로젝트 데이터는 서버에 저장되지만 대시보드 UI 조회 로직에 문제가 있는 것으로 추정

### Tomorrow's focus (다음 집중할 것)
- M2 완료 → M3 (문서화 및 사용 가이드) 시작 여부 판단
- Clearly 사용 가이드에 "반복 작성을 통한 품질 향상" 팁 포함
- Output Tool 산출물 분석 (CLAUDE.md, settings.json의 구조와 활용법)

---

## 산출물 요약

### 오늘 생성된 파일

| 파일 | 위치 | 설명 |
|------|------|------|
| BRD v3 | `brd/catchupai-2026-brd-v3.md` | 3회차 BRD (4개 질문 기반) |
| PRD v2 | `prd/catchupai-2026-prd-v2.md` | 3회차 PRD (5개 질문, 12개 섹션) |
| CLAUDE.md | `claude-code-output/CLAUDE.md` | Claude Code 프로젝트 지시사항 |
| settings.json | `claude-code-output/.claude/settings.json` | Claude Code 설정 |
| PRD (Output) | `claude-code-output/PRD.md` | Output Tool용 PRD |
| Reference Doc | `claude-code-output/REFERENCE_DOCUMENT.md` | BRD/PRD 종합 참조 문서 |
| ZIP 백업 | `claude-code-output/claude-code-project-files.zip` | Output 원본 ZIP |
| 버그 리포트 | `notes/clearly-bug-report.md` | Session 3 재현 기록 추가 |

### 전체 산출물 폴더 구조

```
02-CatchUpAI-BRD-PRD/
├── README.md
├── brd/
│   ├── catchupai-2026-brd-v2.md      (Session 2)
│   ├── brd-catch-up-ai-2026-homepage-2026-02-15.pdf  (Session 2)
│   └── catchupai-2026-brd-v3.md      (Session 3 - 오늘)
├── prd/
│   ├── catchupai-2026-prd.md         (Session 2)
│   └── catchupai-2026-prd-v2.md      (Session 3 - 오늘)
├── claude-code-output/               (Session 3 - 오늘, 신규)
│   ├── .claude/
│   │   └── settings.json
│   ├── CLAUDE.md
│   ├── PRD.md
│   ├── REFERENCE_DOCUMENT.md
│   └── claude-code-project-files.zip
└── notes/
    ├── wizard-experience.md
    └── clearly-bug-report.md         (Session 3 업데이트)
```

---

## 학습 시간 비교 (세션별)

| 세션 | 날짜 | 소요 시간 | 범위 | 비고 |
|------|------|----------|------|------|
| Session 1 | 2/8 | ~2h | BRD만 (Bug로 중단) | Bug #2, #3 발생 |
| Session 2 | 2/14 | ~2h | BRD + PRD | Bug #4 발견, Output 미진행 |
| **Session 3** | **2/15** | **~1.5h** | **BRD + PRD + Output** | **전체 완료, 효율 향상** |

3회 반복으로 소요 시간이 줄어들면서 범위는 넓어짐 — 반복 학습의 효과 확인.

---

**작성자**: CUA_VL 학습자
**방법론**: CUA_VL (VibeLearn AI)
