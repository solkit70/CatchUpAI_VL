**Document Header:**
# Business Requirements Document: Catch Up AI 2026 홈페이지
**Project Name:** Catch Up AI 2026 홈페이지 리뉴얼
**Date:** 2026-02-15
**Version:** 1.0

## 1. Introduction
본 문서는 Catch Up AI 2026 홈페이지 리뉴얼 프로젝트의 비즈니스 요구사항을 정의합니다. 본 프로젝트는 시애틀 기반 AI 학습 및 연구 채널인 Catch Up AI의 YouTube 콘텐츠를 체계적으로 소개하고, 방문자의 이해도를 높이며, 커뮤니티 참여를 유도하는 정보 허브 웹사이트를 구축하는 것을 목표로 합니다. 예산 및 시간 제약 속에서 효율적인 개발 및 운영 방안을 모색합니다.

## 2. Stakeholder & User Analysis
### 2.1. RACI Matrix

| Role            | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
| :-------------- | :-------------- | :-------------- | :-------------- | :----------- |
| Product Owner   | R               | A               | C               | I            |
| Development Team Lead | R               | A               | C               | I            |
| UI/UX Designer  |                 |                 | C               | I            |
| Marketing Lead  |                 |                 | C               | I            |
| Content Creators | R               |                 | C               | I            |

### 2.2. Target Users
- **AI에 관심 있는 개발자 및 비개발자:** AI 학습 방법론 및 프로젝트에 대한 정보를 얻고자 하는 사용자.
- **새로운 AI 학습 방법론에 관심 있는 사람:** Vibe Coding, Vibe Learning, Vibe Guiding 등 Catch Up AI 고유의 접근 방식에 흥미를 느끼는 사용자.
- **시애틀 지역 AI 커뮤니티 멤버:** 지역 AI 행사 정보 및 커뮤니티 활동에 관심 있는 사용자.

### 2.3. User Journey Map
1. **유입:** YouTube 채널 설명, 소셜 미디어, 검색 엔진 등을 통해 홈페이지 접속.
2. **탐색:** 메인 페이지에서 Catch Up AI의 핵심 5가지 프로젝트(Vibe Coding, Vibe Learning, Vibe Guiding, AI4PKM, 시애틀 AI 생태계)를 확인.
3. **심화 학습:** 관심 있는 프로젝트 페이지로 이동하여 상세 설명, 관련 YouTube 플레이리스트/영상을 시청.
4. **참여 유도:** AI4PKM 코호트 신청, 뉴스레터 구독, YouTube 채널 구독, 소셜 미디어 팔로우 등 커뮤니티 참여 활동 수행.
5. **재방문:** 새로운 콘텐츠나 업데이트 확인을 위해 재방문.

## 3. Business Objectives
### 3.1. Primary Objectives
- **정보 허브 구축:** Catch Up AI의 핵심 5가지 프로젝트 및 방법론에 대한 방문자의 명확한 이해도 증진.
- **YouTube 채널 활성화:** 홈페이지를 통한 YouTube 채널 구독 전환율 및 콘텐츠 시청 시간 증대.
- **커뮤니티 참여 유도:** AI4PKM 코호트 참여, 뉴스레터 구독, 시애틀 AI 이벤트 참여 등 커뮤니티 활동 참여율 향상.
- **브랜드 인지도 강화:** AI 학습 및 연구 분야에서 Catch Up AI의 전문성 및 독창성 인지도를 높임.

### 3.2. Success Metrics

| 지표 (KPI)                      | 목표 값              | 측정 방법                                     |
| :------------------------------ | :------------------- | :-------------------------------------------- |
| 핵심 프로젝트 상세 페이지 방문율   | 전체 방문자의 60% 이상 | 웹사이트 분석 도구(Google Analytics 등)       |
| YouTube 채널 구독 전환율           | 목표 설정 필요       | 홈페이지 내 YouTube 구독 버튼 클릭 및 전환 추적 |
| 웹사이트 평균 세션 시간           | 3분 이상             | 웹사이트 분석 도구                            |
| AI4PKM Cohort 신청 페이지 전환율 | 목표 설정 필요       | AI4PKM 상세 페이지 내 신청 버튼 클릭 및 전환 추적 |
| 뉴스레터 구독 횟수                | 월별 목표 설정 필요  | 뉴스레터 구독 폼 제출 수                       |
| 소셜 미디어 공유 횟수             | 월별 목표 설정 필요  | 소셜 미디어 공유 버튼 클릭 수                  |

### 3.3. Business Value
- AI 학습 및 연구 분야에서 Catch Up AI의 강력한 브랜드 포지셔닝.
- 체계적인 정보 제공을 통한 사용자 경험 향상 및 충성도 증가.
- 커뮤니티 활성화를 통한 네트워크 확장 및 잠재적 협업 기회 증대.
- 장기적인 관점에서 AI 교육 콘텐츠 시장에서의 경쟁 우위 확보.

## 4. Technical Context
### 4.1. System Architecture Overview
- **아키텍처 유형:** 정적 웹사이트 (Static Website)
- **프론트엔드:** HTML, CSS, JavaScript (바닐라 JS)
- **호스팅:** Amazon S3 (정적 웹사이트 호스팅)
- **백엔드:** 없음 (프론트엔드 단독 구성)
- **콘텐츠 관리:** Product Owner가 AI 코딩 도구(Claude Code, Cursor)를 활용하여 HTML 파일 직접 수정.
- **다국어 지원:** 영어(기본) 및 한국어(별도 /ko/ 폴더 내 정적 HTML)
- **YouTube 연동:** YouTube 플레이리스트 임베드 방식 및 필요 시 YouTube API (무료 할당량 내) 활용.

### 4.2. Technical Constraints
- **예산 제약:** 유료 서비스(고급 분석 도구, 전문 CDN, 검색 솔루션) 사용 최소화.
- **개발 기간 제약:** MVP (Minimum Viable Product) 우선 개발 후 점진적 개선.
- **콘텐츠 관리:** CMS 부재로 인한 Product Owner의 직접적인 HTML 수정 관리.
- **YouTube API:** 무료 할당량 내 사용 제한.

### 4.3. Scalability Requirements
- **트래픽:** 초기 낮은 트래픽 예상. 향후 트래픽 증가 시 Amazon CloudFront CDN 추가를 통한 성능 확보 고려.
- **콘텐츠:** 초기 정적 HTML 방식 유지. 콘텐츠 양 증가 시 JSON 기반 동적 로딩 방식으로의 확장 가능성 고려.
- **사용자:** 전 세계 AI 관심 사용자를 대상으로 하므로, CDN을 통한 글로벌 접속 속도 보장 필요성 내재.

## 5. Functional Requirements
### 5.1. Core Features
- **메인 페이지:** Catch Up AI 소개 및 5가지 핵심 프로젝트 요약 정보 제공 (Priority: Must Have)
- **프로젝트 상세 페이지:** 각 5개 프로젝트별 상세 설명, 목표, 방법론, 관련 YouTube 플레이리스트 임베드 (Priority: Must Have)
- **추천 영상 섹션:** 각 프로젝트 페이지별 Product Owner가 선별한 3-5개 추천 영상 목록 제공 (Priority: Should Have)
- **다국어 전환 기능:** 영어/한국어 웹사이트 간 전환 버튼 제공 (Priority: Must Have)
- **반응형 디자인:** 데스크톱, 태블릿, 모바일 기기에서 최적화된 사용자 경험 제공 (Priority: Must Have)
- **YouTube 채널 구독 링크:** 모든 페이지에 YouTube 채널로 바로 이동하는 링크 제공 (Priority: Must Have)
- **소셜 미디어 링크:** Catch Up AI의 주요 소셜 미디어 채널(예: LinkedIn, Twitter 등) 링크 제공 (Priority: Should Have)
- **뉴스레터 구독 폼:** 간략한 뉴스레터 구독 신청 폼 제공 (Priority: Nice to Have)

### 5.2. User Stories
- **As a AI 학습에 관심 있는 사용자,** **I want** Catch Up AI의 5가지 핵심 프로젝트를 한눈에 볼 수 **so that** 내가 관심 있는 분야를 쉽게 찾을 수 있다.
- **As a Vibe Coding에 관심 있는 개발자,** **I want** Vibe Coding 프로젝트의 상세 설명과 관련 YouTube 라이브 스트림 영상을 볼 수 **so that** Vibe Coding의 개념과 실제 적용 사례를 이해할 수 있다.
- **As a AI4PKM Cohort에 참여하고 싶은 사람,** **I want** AI4PKM 프로그램의 목표, 진행 방식, 신청 방법을 알 수 **so that** 코호트 참여를 결정하고 신청할 수 있다.
- **As a 해외 사용자,** **I want** 웹사이트의 모든 콘텐츠를 영어로 볼 수 **so that** 언어 장벽 없이 정보를 습득할 수 있다.
- **As a 모바일 사용자,** **I want** 휴대폰에서도 웹사이트 레이아웃이 깨지지 않고 편리하게 정보를 탐색할 수 **so that** 언제 어디서든 Catch Up AI 콘텐츠에 접근할 수 있다.
- **As a Catch Up AI Product Owner,** **I want** AI 코딩 도구를 사용하여 손쉽게 웹사이트의 텍스트나 이미지 콘텐츠를 업데이트할 수 **so that** 최신 정보를 빠르게 반영하고 유지보수 부담을 줄일 수 있다.

## 6. Non-Functional Requirements
### 6.1. Performance
- **페이지 로딩 시간:** 모든 페이지는 3초 이내에 로드되어야 한다. (CDN 적용 시 2초 이내 목표)
- **정적 콘텐츠 전송:** Amazon S3를 통한 안정적인 콘텐츠 전송 보장.
- **YouTube 임베드:** YouTube 플레이어 로딩 속도 최적화.

### 6.2. Security
- **HTTPS 적용:** 모든 트래픽은 HTTPS를 통해 암호화되어야 한다.
- **클라이언트 측 보안:** XSS(Cross-Site Scripting) 및 기타 클라이언트 측 공격에 대한 기본적인 방어 구현.
- **데이터 보호:** 개인 정보(뉴스레터 구독 정보) 수집 시 관련 법규 준수 및 안전한 저장 방식 고려.

### 6.3. Usability
- **직관적인 내비게이션:** 5개 핵심 프로젝트를 중심으로 한 명확하고 직관적인 메뉴 구조.
- **접근성:** 웹 접근성 표준(WCAG 2.1 AA)을 준수하여 다양한 사용자가 접근할 수 있도록 설계.
- **일관된 UI/UX:** Catch Up AI의 브랜딩을 반영한 일관된 디자인 및 사용자 경험 제공.

### 6.4. Reliability
- **가용성:** Amazon S3의 높은 가용성(99.9% 이상)을 통해 안정적인 서비스 제공.
- **백업:** S3 버킷 버전 관리 및 정기적인 백업 정책 수립.
- **재해 복구:** 정적 웹사이트의 특성상 별도의 복잡한 재해 복구 계획은 불필요하나, S3 버킷 지역 이중화 등 고려.

## 7. Constraints & Assumptions
### 7.1. Budget Constraints
- 개인 프로젝트로 예산이 거의 없으므로, 기존 Amazon S3 호스팅 비용 외 추가 비용을 최소화한다.
- 유료 분석 도구, CDN, 전문 검색 솔루션 사용을 지양한다.
- YouTube API는 무료 할당량 내에서만 사용한다.
- AI 코딩 도구(Claude Code, Cursor)는 기존 구독을 활용하므로 추가 비용으로 간주하지 않는다.

### 7.2. Timeline
- MVP (Minimum Viable Product)를 2026년 1분기 내에 완성하고, 점진적으로 개선한다.
- 본업과 병행하는 개인 프로젝트이므로 개발 및 업데이트에 투입할 수 있는 시간이 제한적이다.

### 7.3. Assumptions
- Product Owner가 HTML/CSS/JavaScript에 대한 기본적인 이해와 AI 코딩 도구 활용 능력을 보유하고 있다.
- YouTube의 플레이리스트 임베드 정책 및 API 무료 할당량 정책이 크게 변경되지 않을 것이다.
- 초기 트래픽은 Amazon S3 단독으로 충분히 감당할 수 있는 수준일 것이다.
- 콘텐츠 번역은 Product Owner가 직접 수행하며, 번역 품질은 Product Owner의 역량에 따른다.

## 8. Risk Analysis

| Risk                              | Impact     | Probability | Mitigation Strategy                                                                                                                                                                                                                                                                       |
| :-------------------------------- | :--------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AI 코딩 도구 생성 코드 품질 문제  | Medium-High | Medium      | - 단순한 기술 스택(HTML/CSS/JS) 유지 및 명확한 구조 사용<br>- Git을 통한 버전 관리 및 롤백 체계 구축<br>- Product Owner의 코드 검토 및 디버깅 역량 강화                                                                                                                             |
| Product Owner의 콘텐츠 업데이트 지연 | Medium     | Medium      | - 명확한 콘텐츠 가이드라인 및 템플릿 제공<br>- AI 코딩 도구를 활용한 업데이트 프로세스 간소화<br>- 콘텐츠와 레이아웃 분리 구조 설계 (JSON 기반 동적 로딩으로 확장 고려)                                                                                                                                    |
| YouTube 서비스 정책 변경          | Medium     | Low         | - 플레이리스트 임베드 방식을 우선 사용하여 API 의존도 최소화<br>- 모듈화된 구조로 정책 변경 시 빠른 대응 가능성 확보<br>- YouTube 외 대체 비디오 플랫폼 고려 (장기적 관점)                                                                                                                                   |
| 다국어 콘텐츠 번역 품질 및 관리 문제 | Low-Medium | Medium      | - 영어 버전을 우선 완성하고 한국어는 단계적으로 추가<br>- 콘텐츠 양이 많지 않은 초기에는 정적 HTML 방식 유지<br>- 번역 가이드라인 수립 및 AI 번역 도구 활용 검토                                                                                                                                         |
| 예산 제약으로 인한 기능 제한      | Medium     | High        | - MVP에 집중하고 필수 기능만 구현<br>- 오픈 소스 또는 무료 서비스 적극 활용<br>- 향후 프로젝트 성과에 따라 예산 확보 및 유료 서비스 도입 검토                                                                                                                                                           |
| 시간 제약으로 인한 프로젝트 지연  | High       | Medium      | - 개발 범위 최소화 및 MVP에 집중<br>- Product Owner의 우선순위 결정 및 유연한 일정 관리<br>- AI 코딩 도구 적극 활용을 통한 개발 생산성 향상 (단, 품질 검증 시간 고려) |

## 9. Dependencies
- **YouTube 플랫폼:** YouTube 콘텐츠 임베드 및 API 활용.
- **Amazon S3:** 웹사이트 호스팅 및 콘텐츠 저장.
- **AI 코딩 도구:** Claude Code, Cursor 등 (Product Owner의 개발 생산성 향상 도구).
- **웹 브라우저:** 최신 웹 표준을 지원하는 주요 웹 브라우저 (Chrome, Firefox, Safari, Edge).

## 10. Approval
본 문서는 Catch Up AI 2026 홈페이지 리뉴얼 프로젝트의 비즈니스 요구사항을 명확히 정의하며, 프로젝트 팀 및 관련 이해관계자들의 합의를 통해 승인된다.

**승인자:**

---
**이름:** [Product Owner 이름]
**직책:** Product Owner, Catch Up AI
**서명:** _________________________
**날짜:** 2026-02-15

---
**이름:** [Development Team Lead 이름]
**직책:** Development Team Lead
**서명:** _________________________
**날짜:** 2026-02-15