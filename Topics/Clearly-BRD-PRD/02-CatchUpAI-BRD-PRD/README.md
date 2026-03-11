# M2 - Catch Up AI BRD/PRD 실습

**모듈**: M2 - Catch Up AI BRD/PRD 실습
**Topic**: Clearly-BRD-PRD
**기간**: 2026-02-08 ~ 2026-02-15
**상태**: ✅ 완료

---

## 📖 학습 순서

이 폴더를 처음 여는 분은 아래 순서대로 읽으세요.

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [notes/wizard-experience.md](notes/wizard-experience.md) | AI Wizard 사용 경험 상세 기록 (3 Session 과정) |
| 2 | [brd/catchupai-2026-brd-v3.md](brd/catchupai-2026-brd-v3.md) | BRD 최종본 v3 (Catch Up AI 2026 홈페이지) |
| 3 | [prd/catchupai-2026-prd-v2.md](prd/catchupai-2026-prd-v2.md) | PRD 최종본 v2 (12개 섹션, 상세 사양) |
| 4 | [claude-code-output/REFERENCE_DOCUMENT.md](claude-code-output/REFERENCE_DOCUMENT.md) | BRD/PRD 통합 참조 문서 (Claude Code Output) |
| 5 | [claude-code-output/CLAUDE.md](claude-code-output/CLAUDE.md) | Claude Code 프로젝트 지시사항 (자동 생성) |
| 6 | [notes/clearly-bug-report.md](notes/clearly-bug-report.md) | Clearly 앱 버그 리포트 4건 (실사용 QA 기록) |

**이전 모듈**: [01-Clearly-Overview](../01-Clearly-Overview/) | **다음 모듈**: [03-Clearly-Intro-Video](../03-Clearly-Intro-Video/)

---

## 개요

Clearly 앱(https://www.clearlyreqs.com/)의 AI Wizard를 활용하여 "Catch Up AI 2026 Homepage" 프로젝트의 BRD(Business Requirements Document)와 PRD(Product Requirements Document)를 생성하고, Choose Output Tool(Claude Code)까지 전체 워크플로우를 완료한 실습 기록입니다.

---

## 폴더 구조

```
02-CatchUpAI-BRD-PRD/
├── README.md                                          # 이 파일
├── brd/
│   ├── catchupai-2026-brd.md                          # BRD v1 (2026-02-08, 버그 수정 전)
│   ├── catchupai-2026-brd-v2.md                       # BRD v2 (2026-02-14, 버그 수정 후)
│   ├── brd-catch-up-ai-2026-homepage-2026-02-15.pdf   # BRD v2 PDF 버전
│   └── catchupai-2026-brd-v3.md                       # BRD v3 (2026-02-15, 반복 보강)
├── prd/
│   ├── catchupai-2026-prd.md                          # PRD v1 (2026-02-14)
│   └── catchupai-2026-prd-v2.md                       # PRD v2 (2026-02-15, 12개 섹션 보강)
├── claude-code-output/                                # Choose Output Tool 산출물 (2026-02-15)
│   ├── .claude/
│   │   └── settings.json                              # Claude Code 프로젝트 설정
│   ├── CLAUDE.md                                      # Claude Code 프로젝트 지시사항
│   ├── PRD.md                                         # Output Tool용 PRD
│   ├── REFERENCE_DOCUMENT.md                          # BRD/PRD 종합 참조 문서
│   └── claude-code-project-files.zip                  # 원본 ZIP 백업
└── notes/
    ├── wizard-experience.md                           # AI Wizard 사용 경험 상세 기록
    └── clearly-bug-report.md                          # Clearly 앱 버그 리포트 (4건)
```

---

## 실습 진행 과정

### Session 1 (2026-02-08)

1. Clearly 앱에서 "Catch Up AI 2026 Homepage" 프로젝트 생성
2. BRD Wizard 5개 질문 답변 → BRD v1 생성 완료
3. BRD 검토, Markdown 내보내기, Approve
4. PRD Wizard 시작 → **세션 만료 버그로 중단**
5. 재로그인 후 프로젝트 접근 불가 (Critical 버그)
6. 버그 리포트 작성 및 개발자 전달

### Session 2 (2026-02-14)

1. 개발자의 버그 수정 확인 (3개 버그 모두 Fix)
2. 새 프로젝트로 BRD v2 재생성 → 날짜 버그 수정 확인
3. BRD Approve → PRD Wizard 4개 질문 답변 → PRD v1 생성 완료
4. PRD Approve → Project Progress 67% (2/3 completed)
5. Bug #4 발견: 대시보드 복귀 시 프로젝트 사라짐

### Session 3 (2026-02-15) — 전체 완료

1. Bug #4 재현 확인 (대시보드: Total Projects 0)
2. 새 프로젝트 생성 → BRD v3 (4개 질문, 이전 답변 보강)
3. PRD v2 생성 (5개 질문, 12개 섹션, GA4/디자인 시스템/개인정보 보강)
4. **Choose Output Tool 최초 완료** — Claude Code 선택
5. Output 산출물 다운로드 및 로컬 저장
6. Bug #4 재현 확인 (여전히 Open)

---

## 생성된 문서 요약

### BRD (Business Requirements Document)

- **프로젝트**: Catch Up AI 2026 홈페이지
- **핵심 목표**: 5가지 핵심 콘텐츠의 정보 허브 구축, YouTube 구독 전환, 커뮤니티 확장
- **기술 스택**: 정적 웹사이트 (HTML/CSS/JS), Amazon S3 호스팅
- **버전 비교**: v1(5Q) → v2(3Q) → v3(4Q) — 질문 수는 다르지만 반복할수록 문서 품질 향상

### PRD (Product Requirements Document)

- **BRD 기반**: BRD를 기반으로 상세 제품 사양 정의
- **핵심 기능**: 메인 페이지, 5개 프로젝트 상세 페이지, 다국어 지원, 반응형 디자인, 뉴스레터 구독
- **버전 비교**: v1(4Q, 기본 구조) → v2(5Q, 12개 섹션, Timeline/Performance/Deployment 포함)

### Claude Code Output

- **CLAUDE.md**: 프로젝트 아키텍처, 코딩 컨벤션, 파일 구조를 포함한 Claude Code 지시사항
- **settings.json**: 프로젝트 메타데이터, 기술 스택, 코딩 컨벤션 설정
- **Reference Document**: BRD/PRD를 통합한 종합 참조 문서
- **활용**: 실제 프로젝트 루트에 배치하면 Claude Code가 프로젝트 컨텍스트를 자동 이해

---

## 버그 리포트 요약

| # | Bug | 심각도 | 최초 보고 | 최종 상태 |
|---|-----|--------|---------|----------|
| 1 | BRD 날짜 자동 생성 오류 | Low | 2/8 | ✅ Fixed |
| 2 | PRD Wizard 중 세션 만료 | High | 2/8 | ✅ Fixed |
| 3 | 재로그인 후 프로젝트 접근 불가 | Critical | 2/8 | ✅ Fixed |
| 4 | 대시보드에서 프로젝트 사라짐 | Critical | 2/14 | 🔴 Open (3회 재현) |

---

## 학습 인사이트

### 도구 사용
- Clearly의 AI Wizard는 Initial Idea에 구체적인 정보를 넣을수록 정확한 질문을 생성
- BRD → PRD의 흐름이 자연스럽고, BRD 내용이 PRD 질문에 자동 반영됨
- Example answers가 답변 방향을 잡는 데 매우 유용
- 중요한 문서는 항상 로컬에 Markdown으로 백업하는 것이 안전

### 반복을 통한 품질 향상 (핵심 Tip)
- BRD/PRD 작성은 1회성이 아니라 **반복(iteration)할수록 품질이 높아진다**
- 이전 세션의 답변 + 새 세션의 질문에서 발견된 새로운 관점을 결합하면 완성도가 점진적으로 올라감
- v1(첫 시도) → v2(경험 기반) → v3(갭 보강, 누락 내용 추가)
- 효율도 향상: Session 1(2h, BRD만) → Session 3(1.5h, 전체 완료)

### Wizard 질문의 적응성
- 동일한 프로젝트를 반복 생성해도 Wizard 질문이 매번 약간 달라짐
- Initial Idea의 상세도와 이전 답변에 따라 AI가 질문을 적응적으로 생성

---

**작성자**: CUA_VL 학습자
**방법론**: CUA_VL (VibeLearn AI)
