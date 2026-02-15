# Product Requirements Document: Catch Up AI 2026 홈페이지
**Project Name:** Catch Up AI 2026 홈페이지 리뉴얼
**Date:** 2026-02-15
**Version:** 1.0
**Based on:** BRD v1.0

## 1. Product Overview
### 1.1. Product Vision
Catch Up AI 2026 홈페이지는 시애틀 기반 AI 학습 및 연구 채널 Catch Up AI의 YouTube 콘텐츠를 체계적으로 소개하고, 방문자가 핵심 프로젝트와 학습 방법론을 쉽게 이해하며, AI 커뮤니티와의 연결을 강화하는 허브 역할을 수행한다. 최소한의 비용으로 효율적인 개발 및 운영을 지향한다.

### 1.2. Product Goals
- Catch Up AI의 5가지 핵심 프로젝트(Vibe Coding, Vibe Learning, Vibe Guiding, AI4PKM, 시애틀 AI 생태계) 및 방법론에 대한 방문자의 이해도 증진.
- 홈페이지를 통한 YouTube 채널 구독 전환율 및 콘텐츠 시청 시간 증대.
- AI4PKM 코호트 참여, 뉴스레터 구독 등 커뮤니티 활동 참여율 향상.
- AI 학습 및 연구 분야에서 Catch Up AI의 전문성 및 독창성 인지도 강화.

### 1.3. Target Audience
- AI에 관심 있는 개발자 및 비개발자
- 새로운 AI 학습 방법론에 관심 있는 사람
- 시애틀 지역 AI 커뮤니티 멤버

### 1.4. Key Success Criteria
- 핵심 프로젝트 상세 페이지 방문율: 전체 방문자의 60% 이상
- YouTube 채널 구독 전환율: 목표 설정 필요
- 웹사이트 평균 세션 시간: 3분 이상
- AI4PKM Cohort 신청 페이지 전환율: 목표 설정 필요
- 뉴스레터 구독 횟수: 월별 목표 설정 필요
- 소셜 미디어 공유 횟수: 월별 목표 설정 필요

## 2. Technical Architecture
### 2.1. System Architecture Diagram (describe in text)
본 시스템은 정적 웹사이트 아키텍처를 채택하며, Amazon S3를 통해 호스팅된다. 클라이언트(웹 브라우저)는 S3에 저장된 HTML, CSS, JavaScript 파일을 직접 요청하여 렌더링한다. 별도의 백엔드 서버나 데이터베이스는 존재하지 않는다. YouTube 콘텐츠는 iframe 임베드 방식을 주로 사용하며, 필요한 경우 YouTube Data API를 제한적으로 활용한다. 뉴스레터 구독 폼은 Google Forms를 임베드하여 구독자 정보를 Google Sheets에 저장하는 방식으로 구현된다. 웹사이트 성능 향상 및 글로벌 접근성 확보를 위해 향후 Amazon CloudFront CDN 도입을 고려할 수 있다.

### 2.2. Technology Stack
| Layer | Technology | Rationale |
| :---- | :--------- | :-------- |
| Frontend | HTML5 | 웹 콘텐츠 구조화를 위한 표준 마크업 언어. Product Owner의 AI 코딩 도구 활용 및 직접 수정 용이성. |
| Frontend | CSS3 | 웹 페이지 스타일링 및 반응형 디자인 구현. 복잡한 프레임워크 없이 바닐라 CSS로 파일 크기 최소화 및 성능 최적화. |
| Frontend | JavaScript (Vanilla JS) | 웹 페이지의 동적 기능 구현 및 이벤트 처리. 경량화된 스크립팅으로 빠른 로딩 속도 유지. |
| Hosting | Amazon S3 | 정적 웹사이트 호스팅을 위한 비용 효율적이고 고가용성 서비스. BRD의 예산 제약 및 확장성 요구사항 충족. |
| Analytics | Google Analytics 4 (GA4) | 웹사이트 트래픽 및 사용자 행동 분석을 위한 무료 솔루션. 핵심 성공 지표 추적 및 데이터 기반 의사결정 지원. |
| Forms | Google Forms | 뉴스레터 구독 정보 수집을 위한 무료 및 간단한 솔루션. 백엔드 개발 없이 구독자 관리 기능 제공. |
| AI Coding Tool | Claude Code, Cursor | Product Owner의 콘텐츠 생성 및 코드 수정을 보조하는 AI 도구. 개발 생산성 향상 및 유지보수 부담 경감. |

### 2.3. Component Breakdown
- **Static Asset Storage (Amazon S3):** 모든 HTML, CSS, JavaScript, 이미지 및 기타 정적 파일 저장.
- **Web Pages (HTML):** 메인 페이지, 5가지 핵심 프로젝트 상세 페이지, 다국어 페이지 등.
- **Styling (CSS):** 반응형 디자인, 레이아웃, UI 요소 스타일링.
- **Client-side Scripting (JavaScript):** 언어 전환, GA4 이벤트 트래킹, YouTube 플레이어 제어(향후), UI 인터랙션 등.
- **YouTube Content Integrator:** YouTube 플레이리스트/개별 영상 임베드 (iframe) 및 YouTube Data API (제한적, 향후).
- **Newsletter Form Integrator:** Google Forms 임베드.
- **Analytics Tracker:** Google Analytics 4 (GA4) 코드.

### 2.4. Integration Points
- **YouTube:**
    - YouTube 플레이어 임베드 (iframe): 각 프로젝트별 관련 영상 및 플레이리스트 표시.
    - YouTube Data API v3 (향후 고려): 라이브 스트림 정보, 채널 정보 등 동적 데이터 조회 (무료 할당량 내에서 제한적 사용).
- **Google Analytics 4 (GA4):** 웹사이트 트래픽 및 사용자 행동 데이터 수집.
- **Google Forms / Google Sheets:** 뉴스레터 구독 정보 수집 및 관리.
- **Social Media Platforms:** LinkedIn, Twitter 등 Catch Up AI 소셜 미디어 채널로의 외부 링크.

## 3. User Stories & Use Cases
### 3.1. User Personas
- **AI 탐색가 (AI Explorer):** AI 기술 및 학습 방법에 대해 호기심이 많으며, Catch Up AI의 콘텐츠를 통해 새로운 지식을 얻고 싶어 하는 개발자 또는 비개발자.
- **커뮤니티 지향 학습자 (Community-Oriented Learner):** 시애틀 AI 커뮤니티 활동에 관심이 많고, AI4PKM 코호트나 지역 이벤트를 통해 다른 사람들과 교류하며 배우고 싶어 하는 사용자.
- **효율 추구 개발자 (Efficiency-Seeking Developer):** Vibe Coding과 같은 AI 기반 개발 방법론에 관심이 많고, 실용적인 코드 생성 및 학습 팁을 얻고자 하는 개발자.

### 3.2. User Stories
- **As a AI 학습에 관심 있는 사용자,** I want Catch Up AI의 5가지 핵심 프로젝트를 한눈에 볼 수 so that 내가 관심 있는 분야를 쉽게 찾을 수 있다. (P0, Effort: Small)
- **As a Vibe Coding에 관심 있는 개발자,** I want Vibe Coding 프로젝트의 상세 설명과 관련 YouTube 라이브 스트림 영상을 볼 수 so that Vibe Coding의 개념과 실제 적용 사례를 이해할 수 있다. (P0, Effort: Medium)
- **As a AI4PKM Cohort에 참여하고 싶은 사람,** I want AI4PKM 프로그램의 목표, 진행 방식, 신청 방법을 알 수 so that 코호트 참여를 결정하고 신청할 수 있다. (P0, Effort: Medium)
- **As a 해외 사용자,** I want 웹사이트의 모든 콘텐츠를 영어로 볼 수 so that 언어 장벽 없이 정보를 습득할 수 있다. (P0, Effort: Medium)
- **As a 모바일 사용자,** I want 휴대폰에서도 웹사이트 레이아웃이 깨지지 않고 편리하게 정보를 탐색할 수 so that 언제 어디서든 Catch Up AI 콘텐츠에 접근할 수 있다. (P0, Effort: Medium)
- **As a Catch Up AI Product Owner,** I want AI 코딩 도구를 사용하여 손쉽게 웹사이트의 텍스트나 이미지 콘텐츠를 업데이트할 수 so that 최신 정보를 빠르게 반영하고 유지보수 부담을 줄일 수 있다. (P0, Effort: Small)
- **As a Catch Up AI Product Owner,** I want 뉴스레터 구독자 목록을 간단하게 관리할 수 so that 새로운 소식을 구독자들에게 전달할 수 있다. (P1, Effort: Small)
- **As a Catch Up AI Product Owner,** I want 웹사이트 방문 통계를 확인하여 어떤 콘텐츠가 인기 있는지 파악할 수 so that 향후 콘텐츠 전략 수립에 활용할 수 있다. (P1, Effort: Small)

### 3.3. Use Case Scenarios
**Use Case: 핵심 프로젝트 정보 탐색**
1. **사용자 유입:** 사용자가 검색 엔진 또는 YouTube 채널 링크를 통해 홈페이지에 접속한다.
2. **메인 페이지 진입:** 사용자는 메인 페이지에서 Catch Up AI의 소개와 5가지 핵심 프로젝트 요약 정보를 확인한다.
3. **프로젝트 선택:** 사용자는 "Vibe Coding" 프로젝트에 관심이 생겨 해당 프로젝트 카드 또는 메뉴를 클릭한다.
4. **상세 페이지 이동:** 사용자는 Vibe Coding 상세 페이지로 이동하여 프로젝트 목표, 방법론, 관련 YouTube 플레이리스트 및 추천 영상 목록을 확인한다.
5. **YouTube 콘텐츠 시청:** 사용자는 임베드된 YouTube 플레이리스트 또는 추천 영상을 시청한다.

**Use Case: 다국어 콘텐츠 전환**
1. **홈페이지 접속:** 사용자가 Catch Up AI 홈페이지에 접속한다 (기본 영어 페이지).
2. **언어 전환 버튼 확인:** 사용자는 페이지 상단 내비게이션에서 "한국어" 전환 버튼을 확인한다.
3. **언어 전환:** 사용자가 "한국어" 버튼을 클릭한다.
4. **한국어 페이지 로드:** 웹사이트는 `/ko/` 경로의 한국어 버전 페이지로 이동하며, 모든 텍스트 콘텐츠가 한국어로 표시된다.

**Use Case: 뉴스레터 구독**
1. **구독 폼 접근:** 사용자가 웹사이트 하단 또는 특정 섹션에서 뉴스레터 구독 폼을 발견한다.
2. **구독 버튼 클릭:** 사용자가 "뉴스레터 구독" 버튼을 클릭한다.
3. **Google Forms 로드:** 새로운 브라우저 탭에 Google Forms 기반의 구독 양식이 열리거나, 페이지 내에 임베드된 폼이 나타난다.
4. **정보 입력 및 제출:** 사용자가 이메일 주소를 입력하고 "제출" 버튼을 클릭한다.
5. **구독 완료:** Google Forms 제출 완료 메시지를 확인한다. Product Owner는 Google Sheets에서 해당 구독 정보를 확인한다.

## 4. Feature Requirements
### 4.1. Core Features
| Feature | Description | Priority | Dependencies | Acceptance Criteria |
| :------ | :---------- | :------- | :----------- | :------------------ |
| 메인 페이지 | Catch Up AI 소개 및 5가지 핵심 프로젝트 요약 정보 제공 | P0 | 없음 | - Catch Up AI 비전 및 미션이 명확히 제시되어야 한다.<br>- 5가지 핵심 프로젝트(Vibe Coding, Vibe Learning, Vibe Guiding, AI4PKM, 시애틀 AI 생태계)의 간략한 설명과 상세 페이지로의 링크를 제공해야 한다. |
| 프로젝트 상세 페이지 | 각 5개 프로젝트별 상세 설명, 목표, 방법론, 관련 YouTube 플레이리스트 임베드 | P0 | YouTube | - 각 프로젝트의 상세 내용이 명확하게 설명되어야 한다.<br>- 관련 YouTube 플레이리스트가 iframe으로 임베드되어야 한다.<br>- 페이지 로딩 시 임베드된 YouTube 플레이어가 정상적으로 표시되어야 한다. |
| 추천 영상 섹션 | 각 프로젝트 페이지별 Product Owner가 선별한 3-5개 추천 영상 목록 제공 | P1 | YouTube | - 각 프로젝트 상세 페이지에 Product Owner가 선별한 3-5개의 YouTube 영상이 개별적으로 임베드되어야 한다.<br>- 영상 제목과 간단한 설명이 함께 표시되어야 한다. |
| 다국어 전환 기능 | 영어/한국어 웹사이트 간 전환 버튼 제공 | P0 | 없음 | - 페이지 상단에 "English" / "한국어" 전환 버튼이 명확히 표시되어야 한다.<br>- 버튼 클릭 시 해당 언어의 동일한 페이지로 이동해야 한다.<br>- HTML `lang` 속성이 각 언어에 맞게 설정되어야 한다. |
| 반응형 디자인 | 데스크톱, 태블릿, 모바일 기기에서 최적화된 사용자 경험 제공 | P0 | 없음 | - 데스크톱(1024px 이상), 태블릿(768px~1023px), 모바일(767px 이하) 화면 크기에서 레이아웃이 깨지지 않고 콘텐츠가 가독성 있게 표시되어야 한다.<br>- 이미지 및 미디어 요소가 화면 크기에 맞춰 조정되어야 한다.<br>- 내비게이션 메뉴가 모바일 환경에서 사용하기 편리하게 나타나야 한다 (예: 햄버거 메뉴). |
| YouTube 채널 구독 링크 | 모든 페이지에 YouTube 채널로 바로 이동하는 링크 제공 | P0 | YouTube | - 모든 페이지의 눈에 띄는 위치(예: 헤더, 푸터)에 YouTube 채널로 직접 연결되는 링크가 제공되어야 한다.<br>- 링크 클릭 시 Catch Up AI YouTube 채널로 이동해야 한다. |
| 소셜 미디어 링크 | Catch Up AI의 주요 소셜 미디어 채널(예: LinkedIn, Twitter 등) 링크 제공 | P1 | 소셜 미디어 플랫폼 | - 푸터 또는 별도 섹션에 Catch Up AI의 주요 소셜 미디어 채널(LinkedIn, Twitter) 아이콘 및 링크가 제공되어야 한다. |
| 뉴스레터 구독 폼 | 간략한 뉴스레터 구독 신청 폼 제공 | P2 | Google Forms | - 웹사이트 내에 뉴스레터 구독을 위한 버튼 또는 임베드된 Google Forms가 제공되어야 한다.<br>- 사용자가 이메일 주소를 입력하고 제출할 수 있어야 한다.<br>- 제출된 정보가 Google Sheets에 저장되어 Product Owner가 확인할 수 있어야 한다. |

### 4.2. Feature Specifications
**4.2.1. 메인 페이지**
- Catch Up AI 로고, 채널명, 간략한 슬로건(예: "AI 학습, 연구, 그리고 커뮤니티") 포함.
- 5가지 핵심 프로젝트 카드형 요약 정보: 프로젝트명, 1~2줄 요약 설명, 상세 페이지로 연결되는 버튼.
- YouTube 채널 구독 버튼 및 소셜 미디어 링크.
- 영구적인 푸터에 저작권 정보, 연락처(이메일), 개인정보 처리 방침 링크(향후).

**4.2.2. 프로젝트 상세 페이지**
- 각 프로젝트별 고유 URL (예: `/vibe-coding.html`, `/ko/vibe-coding.html`).
- 페이지 상단에 프로젝트명과 핵심 메시지.
- 프로젝트 소개(목표, 방법론, 기대 효과 등) 텍스트 콘텐츠.
- 관련 YouTube 플레이리스트 iframe 임베드.
- Product Owner가 선별한 3-5개의 추천 YouTube 영상 개별 임베드 (영상 제목, 간략 설명 포함).
- "더 많은 영상 보기" 링크를 통해 YouTube 플레이리스트 페이지로 직접 연결.

**4.2.3. 다국어 전환 기능**
- 루트 폴더에 영어(기본) HTML 파일, `/ko/` 폴더에 한국어 HTML 파일 배치.
- 각 페이지 상단 내비게이션 영역에 "English" / "한국어" 텍스트 버튼 또는 아이콘 버튼.
- 버튼 클릭 시 `<a>` 태그를 이용하여 해당 언어의 동일한 경로 페이지로 이동 (예: `/vibe-coding.html` -> `/ko/vibe-coding.html`).
- HTML `lang` 속성: 영어 페이지는 `lang="en"`, 한국어 페이지는 `lang="ko"`로 설정.

**4.2.4. 반응형 디자인**
- **CSS Flexbox & Grid:** 레이아웃 구성에 활용.
- **Media Queries:**
    - `@media (min-width: 1024px)`: 데스크톱 스타일
    - `@media (min-width: 768px) and (max-width: 1023px)`: 태블릿 스타일
    - `@media (max-width: 767px)`: 모바일 스타일 (모바일 우선 접근 방식으로 기본 스타일 설정)
- **CSS Custom Properties (변수):** 색상, 폰트 사이즈, 간격 등을 정의하여 일관된 디자인 유지.
- **이미지 최적화:** `max-width: 100%; height: auto;` 속성을 사용하여 반응형 이미지 구현.

**4.2.5. 뉴스레터 구독 폼**
- 웹사이트 내에 "뉴스레터 구독" 버튼 배치.
- 버튼 클릭 시 Google Forms 링크로 이동.
- Google Forms는 이메일 주소만 필수 입력 필드로 요청.
- Google Forms 제출 시 Google Sheets에 데이터 자동 저장.
- 개인 정보 처리 방침에 대한 간략한 안내 문구 포함 (향후 별도 페이지 링크).

### 4.3. User Interface Requirements
- **와이어프레임 & UI 플로우:** Figma 또는 유사 도구를 사용하여 주요 페이지(메인, 프로젝트 상세)의 와이어프레임 및 사용자 흐름 설계.
- **디자인 시스템:**
    - **색상 팔레트:** Catch Up AI 브랜드 가이드라인에 맞는 주조색, 보조색, 강조색 정의.
    - **타이포그래피:** 본문, 제목, 링크 등에 사용될 폰트(Google Fonts 등 무료 폰트 활용), 폰트 사이즈, 줄 간격 정의.
    - **아이콘:** YouTube, 소셜 미디어 등 주요 아이콘 정의 (SVG 또는 Font Awesome 등 경량 라이브러리 사용).
    - **컴포넌트:** 버튼, 카드, 내비게이션 바 등 재사용 가능한 UI 컴포넌트 스타일 정의.
- **일관성:** 웹사이트 전체에 걸쳐 Catch Up AI의 브랜딩을 반영한 일관된 UI/UX 제공.
- **접근성:** WCAG 2.1 AA 등급 준수를 목표로, 시맨틱 HTML, 적절한 ARIA 속성, 충분한 색상 대비 등을 고려하여 설계.

## 5. API Specifications
### 5.1. API Endpoints
**초기 MVP에서는 YouTube Data API를 사용하지 않음. 향후 필요 시 아래와 같이 정의될 수 있음.**

| Method | Endpoint | Description | Request | Response |
| :----- | :------- | :---------- | :------ | :------- |
| GET | `/youtube/playlist_items?playlistId={playlistId}&maxResults={maxResults}` | 특정 플레이리스트의 영상 목록 조회 | `playlistId` (string, 필수), `maxResults` (int, 선택, 기본 5) | JSON 배열 (영상 ID, 제목, 썸네일 URL, 설명 포함) |
| GET | `/youtube/channel_data?channelId={channelId}` | 채널 정보 조회 (구독자 수 등) | `channelId` (string, 필수) | JSON 객체 (구독자 수, 채널 제목 등) |
| GET | `/youtube/live_stream_status?channelId={channelId}` | 채널의 현재 라이브 스트림 상태 조회 | `channelId` (string, 필수) | JSON 객체 (라이브 중 여부, 스트림 제목, URL 등) |

### 5.2. Authentication & Authorization
- **YouTube API:** Google Cloud Platform에서 발급받은 API Key를 사용하며, 클라이언트 측 JavaScript에서 직접 API Key를 노출하지 않도록 서버리스 함수(예: AWS Lambda)를 통해 프록시하거나, API 호출을 최소화하고 캐싱 전략을 사용한다. 현재 MVP에서는 API Key 사용 없음.
- **Google Forms:** 별도의 인증/인가 없음. Google Forms의 공개 링크를 통해 접근.

### 5.3. Error Handling
- **YouTube API (향후):** API 호출 실패 시 사용자에게 친화적인 메시지 표시 (예: "YouTube 영상을 불러오지 못했습니다. 잠시 후 다시 시도해주세요."). 네트워크 오류, 할당량 초과 등의 경우를 대비.
- **Google Forms:** Google Forms 자체의 오류 처리 메커니즘을 따름.

## 6. Data Models
### 6.1. Database Schema
**정적 웹사이트이므로 별도의 데이터베이스 스키마는 없음.**
모든 콘텐츠는 HTML 파일 내에 직접 포함되거나, Google Forms를 통해 Google Sheets에 저장된다.

**Google Sheets (뉴스레터 구독자 목록):**
- Column 1: 제출 타임스탬프
- Column 2: 이메일 주소

### 6.2. Data Flow Diagrams (describe in text)
1. **웹사이트 접속:** 사용자가 웹 브라우저를 통해 Catch Up AI 홈페이지 URL에 접속.
2. **정적 파일 로딩:** Amazon S3는 요청된 HTML, CSS, JavaScript 및 이미지 파일을 사용자 브라우저로 전송.
3. **페이지 렌더링:** 브라우저는 전송받은 파일을 파싱하여 웹 페이지를 렌더링.
4. **YouTube 콘텐츠 표시:** HTML 내의 iframe 태그를 통해 YouTube 플레이리스트 또는 개별 영상이 로드되어 표시. (YouTube API 호출 없음)
5. **GA4 데이터 전송:** JavaScript에 포함된 GA4 추적 코드가 페이지 뷰 및 사용자 행동(버튼 클릭 등) 데이터를 Google Analytics 서버로 전송.
6. **뉴스레터 구독:** 사용자가 뉴스레터 구독 버튼 클릭 시, Google Forms 링크로 이동. 사용자가 폼 제출 시, 데이터가 Google Sheets로 직접 전송.

### 6.3. Data Validation Rules
- **Google Forms (뉴스레터 구독):**
    - 이메일 주소 필드는 필수 입력.
    - 이메일 주소 형식 유효성 검사 (Google Forms 기본 기능 활용).
- **HTML 콘텐츠:** Product Owner가 AI 코딩 도구 및 직접 검토를 통해 유효한 HTML/CSS/JS 구문 유지.

## 7. Security & Compliance
### 7.1. Security Requirements
- **HTTPS 적용:** Amazon S3 정적 웹사이트 호스팅 시 HTTPS를 강제하여 모든 트래픽 암호화 (CloudFront 연동 시). 초기 S3 직접 호스팅의 경우 HTTP로 제공될 수 있으나, 가급적 HTTPS 적용을 위한 CloudFront 도입을 우선 고려.
- **클라이언트 측 보안:** XSS(Cross-Site Scripting) 방지를 위해 사용자 입력 필드(뉴스레터 폼)는 외부 서비스(Google Forms)를 사용하고, 직접적인 사용자 입력 처리는 없음.
- **데이터 보호:** 뉴스레터 구독 시 수집되는 이메일 주소는 Google Forms/Sheets의 보안 정책을 따르며, Product Owner만 접근 가능하도록 관리.
- **S3 버킷 정책:** 최소 권한 원칙(Least Privilege)에 따라 S3 버킷에 대한 공개 읽기 권한만 부여하고, 쓰기 권한은 Product Owner의 AWS 계정으로만 제한.

### 7.2. Privacy & Compliance
- **개인 정보 수집 최소화:** 뉴스레터 구독 시 이메일 주소 외의 민감한 개인 정보는 수집하지 않음.
- **개인 정보 처리 방침:** 웹사이트 푸터에 개인 정보 처리 방침에 대한 간략한 안내 문구와 함께, 수집 목적, 보관 기간, 삭제 요청 방법 등을 명시한 페이지 링크(향후 별도 HTML 페이지로 작성)를 제공.
- **GDPR/CCPA:** 정적 웹사이트의 특성상 직접적인 규제 대상은 아니지만, 글로벌 사용자 접근을 고려하여 기본적인 개인 정보 보호 원칙 준수.

### 7.3. Security Testing Requirements
- **정적 코드 분석:** AI 코딩 도구 사용 후 생성된 HTML/CSS/JS 코드에 대한 기본적인 보안 취약점 검토.
- **OWASP Top 10:** 웹사이트에 직접적인 서버 측 취약점은 없으나, 클라이언트 측(XSS 등) 잠재적 위험에 대한 기본적인 검토.
- **HTTPS 설정 검증:** HTTPS 적용 시 SSL/TLS 설정의 올바른 구성 여부 확인.

## 8. Performance Requirements
### 8.1. Performance Metrics
| Metric | Target | Measurement Method |
| :----- | :----- | :----------------- |
| 페이지 로딩 시간 (LCP - Largest Contentful Paint) | 2.5초 이내 | Google PageSpeed Insights, Chrome 개발자 도구 |
| 상호작용까지의 시간 (FID - First Input Delay) | 100ms 이내 | Google PageSpeed Insights, Chrome 개발자 도구 |
| 시각적 안정성 (CLS - Cumulative Layout Shift) | 0.1 이하 | Google PageSpeed Insights, Chrome 개발자 도구 |
| 웹사이트 평균 세션 시간 | 3분 이상 | Google Analytics 4 |
| YouTube 임베드 로딩 지연 | 1초 이내 | Chrome 개발자 도구 네트워크 탭 |

### 8.2. Scalability Requirements
- **트래픽:** Amazon S3는 높은 트래픽을 자동으로 처리할 수 있는 스케일링을 제공하므로, 초기 트래픽 증가에 대한 별도 조치는 불필요.
- **콘텐츠:** 현재는 정적 HTML 방식이나, 콘텐츠 양이 크게 증가할 경우 JSON 기반의 동적 로딩 방식으로 확장 가능성 고려.
- **글로벌 접근성:** 향후 트래픽 증가 시 Amazon CloudFront CDN을 추가하여 전 세계 사용자에게 빠른 콘텐츠 전송 보장.

### 8.3. Optimization Strategies
- **이미지 최적화:** WebP/AVIF 등 최신 이미지 포맷 사용, 이미지 압축, `loading="lazy"` 속성 활용.
- **CSS/JS 최적화:** CSS 및 JavaScript 파일 최소화(Minification), 번들링(Bundling) (바닐라 JS 특성상 수동 또는 간단한 스크립트 사용).
- **브라우저 캐싱:** HTTP 헤더를 통해 정적 파일에 대한 적절한 캐싱 정책 설정.
- **YouTube 임베드:** `iframe` 태그에 `loading="lazy"` 속성 추가, `rel=0` 파라미터로 관련 동영상 표시 제한.

## 9. Testing & Quality Assurance
### 9.1. Testing Strategy
- **수동 테스트:** Product Owner가 모든 페이지에 대해 데스크톱, 태블릿, 모바일 환경에서 수동으로 기능 및 UI/UX 테스트 수행.
- **크로스 브라우저 테스트:** 주요 웹 브라우저(Chrome, Firefox, Safari, Edge)에서 웹사이트의 호환성 테스트.
- **접근성 테스트:** Lighthouse, axe DevTools 등 도구를 활용하여 웹 접근성 가이드라인 준수 여부 확인.
- **성능 테스트:** Google PageSpeed Insights, Lighthouse를 사용하여 페이지 로딩 속도 및 Core Web Vitals 지표 측정.

### 9.2. Acceptance Criteria
- 모든 핵심 기능(5.1 Core Features 섹션 참조)이 BRD 및 PRD에 명시된 대로 작동해야 한다.
- 모든 페이지에서 반응형 디자인이 올바르게 적용되어야 한다.
- 다국어 전환 기능이 정상적으로 작동하며, 콘텐츠가 올바른 언어로 표시되어야 한다.
- YouTube 임베드 콘텐츠가 정상적으로 로드되고 재생되어야 한다.
- GA4가 모든 페이지에서 올바르게 추적 데이터를 수집해야 한다.
- 웹사이트 모든 페이지의 로딩 속도가 3초 이내여야 한다 (최초 로딩 기준).
- HTTPS가 적용되어야 한다 (CloudFront 도입 시).

### 9.3. Quality Metrics
- **Core Web Vitals:** Google PageSpeed Insights 점수 90점 이상 목표.
- **HTML/CSS 유효성:** W3C Validator를 통해 HTML 및 CSS 유효성 검사.
- **접근성 점수:** Lighthouse 접근성 점수 90점 이상 목표.
- **버그 밀도:** MVP 출시 전 발견된 P0/P1 버그 0개.

## 10. Deployment & DevOps
### 10.1. Deployment Strategy
- **수동 배포:** Product Owner가 AI 코딩 도구를 사용하여 수정된 HTML, CSS, JavaScript 파일을 Amazon S3 버킷에 직접 업로드 (AWS CLI 또는 AWS Management Console 사용).
- **환경:** 단일 프로덕션 환경. 별도의 개발/스테이징 환경은 없음.
- **CI/CD:** 초기 MVP에서는 CI/CD 파이프라인 구축 없이 수동 배포. 향후 필요 시 GitHub Actions 등을 활용한 간단한 배포 자동화 고려.

### 10.2. Monitoring & Logging
- **Amazon S3 Access Logs:** S3 버킷에 대한 접근 로그를 활성화하여 웹사이트 트래픽 및 접근 패턴 모니터링.
- **Google Analytics 4:** 실시간 및 표준 보고서를 통해 사용자 행동 및 성능 지표 모니터링.
- **Google Search Console:** 웹사이트 검색 노출 및 크롤링 오류 모니터링.

### 10.3. Rollback Procedures
- **S3 버전 관리:** Amazon S3 버킷에 버전 관리(Versioning) 기능을 활성화하여 이전 버전의 파일로 롤백 가능.
- **Git Repository:** 모든 소스 코드(HTML, CSS, JS)는 Git 리포지토리(예: GitHub)에 관리하여 변경 이력 추적 및 필요 시 이전 커밋으로 복원.

## 11. Timeline & Milestones
| Phase | Deliverables | Timeline | Dependencies |
| :---- | :----------- | :------- | :----------- |
| **Phase 1: MVP 구현** | | 2026년 1분기 | |
| | - 메인 페이지 개발 (영어) | 2026-01-31 | UI/UX 디자인 |
| | - 5가지 프로젝트 상세 페이지 개발 (영어) | 2026-02-15 | UI/UX 디자인, YouTube 콘텐츠 |
| | - 반응형 디자인 적용 | 2026-02-28 | UI/UX 디자인 |
| | - YouTube 임베드 기능 구현 | 2026-02-28 | YouTube 콘텐츠 |
| | - Amazon S3 호스팅 설정 및 배포 | 2026-02-28 | AWS 계정 |
| | - Google Analytics 4 연동 | 2026-02-28 | Google Analytics 계정 |
| | - 수동 테스트 및 QA | 2026-03-15 | 모든 기능 개발 완료 |
| | - 런칭 (MVP) | 2026-03-31 | QA 완료 |
| **Phase 2: 개선 및 확장** | | 2026년 2분기 이후 | |
| | - 한국어 버전 페이지 개발 | 2026-04-30 | Product Owner 번역 |
| | - 뉴스레터 구독 폼 (Google Forms) 연동 | 2026-04-30 | Google Forms 설정 |
| | - Amazon CloudFront CDN 도입 (선택) | 2026-05-31 | AWS 계정, 예산 |
| | - YouTube API 활용 (제한적, 선택) | 2026-06-30 | YouTube API Key |
| | - 추가 소셜 미디어 링크 | 2026-06-30 | |

## 12. Assumptions & Constraints
### 12.1. Technical Assumptions
- Product Owner는 HTML/CSS/JavaScript에 대한 기본적인 이해와 AI 코딩 도구 활용 능력을 보유하고 있다.
- YouTube의 플레이리스트 임베드 정책 및 API 무료 할당량 정책이 크게 변경되지 않을 것이다.
- 초기 트래픽은 Amazon S3 단독으로 충분히 감당할 수 있는 수준일 것이다.
- Google Forms 및 Google Sheets의 서비스가 안정적으로 제공될 것이다.
- 주요 웹 브라우저(Chrome, Firefox, Safari, Edge)에서 웹 표준이 일관되게 지원될 것이다.

### 12.2. Resource Constraints
- **예산 제약:** 개인 프로젝트로 예산이 거의 없으므로, 기존 Amazon S3 호스팅 비용 외 추가 비용을 최소화한다. 유료 서비스(고급 분석 도구, 전문 CDN, 검색 솔루션) 사용을 최소화한다.
- **개발 기간 제약:** 본업과 병행하는 개인 프로젝트이므로 개발 및 업데이트에 투입할 수 있는 시간이 제한적이다. MVP(Minimum Viable Product)를 우선 개발하고 점진적으로 개선한다.
- **인력 제약:** Product Owner가 개발, 콘텐츠 관리, 마케팅, 운영 등 대부분의 역할을 수행한다.

### 12.3. External Dependencies
- **YouTube 플랫폼:** YouTube 콘텐츠 임베드 및 API 활용. YouTube 서비스의 안정성과 정책 변경에 의존.
- **Amazon S3:** 웹사이트 호스팅 및 콘텐츠 저장. AWS 서비스의 안정성에 의존.
- **Google Analytics 4:** 웹사이트 분석 데이터 수집. Google 서비스의 안정성에 의존.
- **Google Forms / Google Sheets:** 뉴스레터 구독 기능. Google 서비스의 안정성에 의존.
- **AI 코딩 도구:** Claude Code, Cursor 등. AI 도구의 성능 및 가용성에 의존.