# M2 - Catch Up AI BRD/PRD 실습

**모듈**: M2 - Catch Up AI BRD/PRD 실습
**Topic**: Clearly-BRD-PRD
**기간**: 2026-02-08 ~ 2026-02-14

---

## 개요

Clearly 앱(https://www.clearlyreqs.com/)의 AI Wizard를 활용하여 "Catch Up AI 2026 Homepage" 프로젝트의 BRD(Business Requirements Document)와 PRD(Product Requirements Document)를 생성한 실습 기록입니다.

---

## 폴더 구조

```
02-CatchUpAI-BRD-PRD/
├── README.md                                          # 이 파일
├── brd/
│   ├── catchupai-2026-brd.md                          # BRD v1 (2026-02-08, 버그 수정 전)
│   ├── catchupai-2026-brd-v2.md                       # BRD v2 (2026-02-14, 버그 수정 후)
│   └── brd-catch-up-ai-2026-homepage-2026-02-15.pdf   # BRD v2 PDF 버전
├── prd/
│   └── catchupai-2026-prd.md                          # PRD (2026-02-14)
└── notes/
    ├── wizard-experience.md                           # AI Wizard 사용 경험 상세 기록
    └── clearly-bug-report.md                          # Clearly 앱 버그 리포트
```

---

## 실습 진행 과정

### Session 1 (2026-02-08)

1. Clearly 앱에서 "Catch Up AI 2026 Homepage" 프로젝트 생성
2. BRD Wizard 5개 질문 답변 → BRD 생성 완료
3. BRD 검토, Markdown 내보내기, Approve
4. PRD Wizard 시작 → **세션 만료 버그로 중단**
5. 재로그인 후 프로젝트 접근 불가 (Critical 버그)
6. 버그 리포트 작성 및 개발자 전달

### Session 2 (2026-02-14)

1. 개발자의 버그 수정 확인 (3개 버그 모두 Fix)
2. 새 프로젝트로 BRD 재생성 → 날짜 버그 수정 확인 (이전: 2023-11-20 → 현재: 2026-02-15 정상)
3. BRD Approve → PRD Wizard 진행
4. PRD Wizard 4개 질문 답변 → PRD 생성 완료 (세션 만료 없이 정상 완료)
5. PRD Approve → Project Progress 67% (2/3 completed)
6. Tool Output 단계는 다음 세션에서 진행 예정

---

## 생성된 문서 요약

### BRD (Business Requirements Document)

- **프로젝트**: Catch Up AI 2026 홈페이지 리뉴얼
- **핵심 목표**: 5가지 핵심 콘텐츠의 정보 허브 구축, YouTube 구독 전환, 커뮤니티 확장
- **기술 스택**: 정적 웹사이트 (HTML/CSS/JS), Amazon S3 호스팅
- **주요 섹션**: Introduction, Stakeholder Analysis, Business Objectives, Technical Context, Functional/Non-Functional Requirements, Constraints, Risk Analysis, Dependencies, Approval

### PRD (Product Requirements Document)

- **BRD 기반**: BRD v1.0을 기반으로 상세 제품 사양 정의
- **핵심 기능**: 메인 페이지, 5개 프로젝트 상세 페이지, 다국어 지원(영어 기본 + 한국어 /ko/), 반응형 디자인, 뉴스레터 구독
- **기술 구현**: YouTube 플레이리스트 임베드, 바닐라 CSS (Flexbox/Grid), GA4 분석

---

## 버그 수정 확인 결과

| # | Bug | 심각도 | 상태 (2/8) | 상태 (2/14) |
|---|-----|--------|-----------|------------|
| 1 | BRD 날짜 자동 생성 오류 | Low | Open | **Fixed** (2026-02-15로 정상 생성) |
| 2 | PRD Wizard 중 세션 만료 | High | Open | **Fixed** (PRD 완료까지 세션 유지) |
| 3 | 재로그인 후 프로젝트 접근 불가 | Critical | Open | **Fixed** (프로젝트 정상 표시) |

---

## 학습 인사이트

- Clearly의 AI Wizard는 Initial Idea에 구체적인 정보를 넣을수록 정확한 질문을 생성함
- BRD → PRD의 흐름이 자연스럽고, BRD 내용이 PRD 질문에 자동 반영됨
- Example answers가 답변 방향을 잡는 데 매우 유용
- 중요한 문서는 항상 로컬에 Markdown으로 백업하는 것이 안전

---

## 다음 단계

- Clearly 앱의 "Choose Output Tool" 단계 진행 (Project Progress 67% → 100%)
- Tool Output 생성 및 검토

---

**작성자**: CUA_VL 학습자
**방법론**: CUA_VL (VibeLearn AI)
