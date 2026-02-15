# WorkLog - M2: Catch Up AI BRD/PRD 실습 (Session 2)

**날짜**: 2026-02-14
**Topic**: Clearly-BRD-PRD
**모듈**: M2 - Catch Up AI BRD/PRD 실습
**학습 시간**: 약 2시간

---

## 🎯 오늘의 학습 목표

- [x] Clearly 앱 버그 수정 확인 (3개 버그 모두 Fix)
- [x] 새 프로젝트 생성 및 BRD 재생성
- [x] BRD 검토, 내보내기 및 Approve
- [x] PRD Wizard 완료 및 PRD 생성
- [x] PRD 검토, 내보내기 및 Approve
- [x] BRD/PRD 로컬 저장 (brd/, prd/ 폴더)
- [x] README.md 작성
- [x] WorkLog 작성
- [x] Daily Retrospective 작성

---

## 📚 진행 내용

### 1. Clearly 앱 버그 수정 확인

**목적**: 지난주(2/8) 보고한 3개 버그의 수정 여부 확인

**과정**:
1. Clearly 앱 접속 및 로그인
2. 대시보드 확인 - 기존 프로젝트 데이터 초기화 상태 (버그 수정 과정에서 리셋)
3. 새 프로젝트 생성으로 버그 수정 확인 진행

**결과**:
- Bug #1 (날짜 오류): **Fixed** - BRD 생성 시 Date가 2026-02-15로 정확하게 표시됨
- Bug #2 (세션 만료): **Fixed** - PRD Wizard 완료까지 세션이 정상 유지됨
- Bug #3 (프로젝트 접근 불가): **Fixed** - 프로젝트가 대시보드에 정상 표시됨

---

### 2. BRD 재생성

**목적**: 버그 수정 후 BRD를 새로 생성하고 품질 확인

**과정**:
1. "New Project" → Project Title: "Catch Up AI 2026 Homepage"
2. Initial Idea에 상세 프로젝트 설명 입력 (지난주 내용을 재사용)
3. Output Language: 한국어
4. BRD Wizard 질문 3개에 답변:
   - Q1: 비즈니스 목표 및 성공 측정 지표
   - Q2: 기술 스택, YouTube 연동 방안
   - Q3: 제약사항 및 잠재적 위험
5. Generate BRD → 날짜 정상 확인 (2026-02-15)
6. BRD 검토 → Markdown 및 PDF 내보내기
7. Approve Document → PRD Wizard 잠금 해제

**결과**:
- BRD v2 생성 완료 (날짜 버그 수정 확인)
- 로컬 저장: `brd/catchupai-2026-brd-v2.md`, `brd/brd-catch-up-ai-2026-homepage-2026-02-15.pdf`

**메모/인사이트**:
- 지난주 경험이 있어 Wizard 답변을 미리 준비하여 빠르게 진행
- BRD Wizard 질문이 지난주(5개)와 다르게 3개로 줄어듦 - Initial Idea의 상세도에 따라 질문 수가 달라질 수 있음

---

### 3. PRD 생성 (지난주 미완료 → 오늘 완료)

**목적**: BRD를 기반으로 PRD 생성 - 지난주 세션 만료로 중단된 작업 완료

**과정**:
1. BRD Approve 후 "Start PRD Wizard" 클릭 (Project Progress: 33%)
2. PRD Wizard 질문 4개에 답변:
   - Q1: 정적 웹사이트 아키텍처 선택 이유, YouTube 콘텐츠 통합 방안, API 할당량 관리
   - Q2: 다국어 지원 구현 (영어 기본 + /ko/ 폴더), 반응형 디자인, CSS 프레임워크 미사용
   - Q3: 뉴스레터 구독 폼 구현 (Google Forms + Google Sheets)
   - Q4: 성공 지표 추적 (GA4 활용, 커스텀 이벤트 트래킹)
3. Generate PRD → PRD 문서 생성 완료
4. PRD 검토 → Markdown 내보내기
5. Approve Document → Project Progress: 67% (2/3)

**결과**:
- PRD 생성 및 Approve 완료
- 로컬 저장: `prd/catchupai-2026-prd.md`
- 세션 만료 없이 PRD Wizard 전 과정 정상 완료 (Bug #2 수정 확인)

**메모/인사이트**:
- PRD Wizard는 BRD 내용을 기반으로 더 구체적인 기술/구현 질문을 함
- 다국어 설계(영어 기본 + /ko/), 뉴스레터(Google Forms), 분석(GA4) 등 구체적 구현 방향이 결정됨
- "Choose Output Tool" 단계가 새로 확인됨 - Clearly의 프로젝트는 BRD → PRD → Tool Output의 3단계 구조

---

### 4. 문서 정리

**목적**: 산출물 정리 및 README.md 작성 (M2 DoD 미완료 항목)

**과정**:
1. BRD (MD + PDF), PRD (MD)를 로컬 폴더에 저장
2. `02-CatchUpAI-BRD-PRD/README.md` 작성 (실습 진행 과정, 문서 요약, 버그 수정 확인 결과 등)

**결과**:
- README.md 작성 완료
- 모든 산출물 로컬 저장 완료

---

## 📊 DoD 체크리스트

로드맵 M2의 Definition of Done:

- [x] Clearly에서 "Catch Up AI 2026 Homepage" 프로젝트 생성
- [x] AI Wizard를 통해 BRD 생성 완료
- [x] BRD 검토 및 필요한 수정 완료
- [x] PRD 생성 완료
- [x] BRD/PRD 내보내기 완료
- [x] `02-CatchUpAI-BRD-PRD/` 폴더에 문서 저장
- [x] README.md 작성
- [x] WorkLog 작성 완료
- [x] Daily Retrospective 작성

**완료율**: 9/9 (100%)

---

## 💡 Daily Retrospective

### What went well (잘된 점)
- 지난주 보고한 3개 버그가 모두 수정되어 BRD/PRD를 끝까지 완료할 수 있었음
- 지난주 Wizard 경험 덕분에 답변을 미리 준비하여 빠르게 진행
- PRD Wizard를 처음으로 끝까지 완료 - Clearly의 전체 BRD→PRD 워크플로우를 체험
- 날짜 버그 수정을 직접 확인하여 버그 리포트의 효과를 체감

### What could be improved (개선할 점)
- Wizard 답변을 더 구조적으로 미리 준비하면 더 빠르게 진행할 수 있었음
- BRD Wizard 질문 수가 지난주(5개)와 오늘(3개)이 달랐는데, Initial Idea 상세도와의 관계를 더 분석해볼 필요

### Insights (인사이트)
- 버그 리포트를 구체적으로 작성하면 개발자가 빠르게 수정할 수 있음 - 실무에서도 동일
- Clearly의 프로젝트는 BRD → PRD → Tool Output의 3단계 구조 (각 33%)
- PRD가 BRD 내용을 자동 참조하여 더 구체적인 질문을 생성하는 것이 인상적
- 다국어 설계, 뉴스레터, 분석 등 PRD 단계에서 구현 세부사항이 구체화됨

### Tomorrow's focus (내일 집중할 것)
- Clearly "Choose Output Tool" 단계 진행 (Project Progress 67% → 100%)
- Tool Output 생성 및 검토
- M2 완료 후 M3 (문서화 및 사용 가이드) 시작 여부 판단

---

## 📎 참조 및 산출물

**생성된 파일/폴더**:
- `02-CatchUpAI-BRD-PRD/brd/catchupai-2026-brd-v2.md`: 오늘 새로 생성한 BRD v2
- `02-CatchUpAI-BRD-PRD/brd/brd-catch-up-ai-2026-homepage-2026-02-15.pdf`: BRD v2 PDF
- `02-CatchUpAI-BRD-PRD/prd/catchupai-2026-prd.md`: PRD (오늘 첫 완료)
- `02-CatchUpAI-BRD-PRD/README.md`: M2 산출물 개요

**참조 자료**:
- [Clearly 앱](https://www.clearlyreqs.com/): BRD/PRD 생성 실습
- `02-CatchUpAI-BRD-PRD/notes/wizard-experience.md`: 지난주 Wizard 경험 기록
- `02-CatchUpAI-BRD-PRD/notes/clearly-bug-report.md`: 버그 리포트 (3개 모두 Fixed)

**다음 세션 준비사항**:
- Clearly 앱에서 "Select Tool & Generate" 클릭하여 Tool Output 단계 진행
- 생성된 Tool Output 검토 및 로컬 저장

---

**작성자**: CUA_VL 학습자
**방법론**: CUA_VL (VibeLearn AI)
