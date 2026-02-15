# Catch Up AI 2026 홈페이지: 종합 참조 문서

## 1. 프로젝트 개요

### 1.1. 제품 비전
Catch Up AI의 2026년 홈페이지는 AI 학습 및 연구 채널 Catch Up AI의 핵심 콘텐츠와 활동을 체계적으로 소개하는 정보 허브 역할을 수행한다. 방문자들이 채널의 주요 프로젝트와 방법론을 쉽게 이해하고, AI에 관심 있는 개발자 및 비개발자 모두에게 접근 가능한 콘텐츠를 제공하며, YouTube 채널의 콘텐츠를 주제별로 탐색할 수 있도록 구성하여 시애틀 지역 AI 커뮤니티와의 연결을 강화하는 것을 목표로 한다.

### 1.2. 제품 목표
*   Catch Up AI의 5가지 핵심 프로젝트(Vibe Coding, Vibe Learning, Vibe Guiding, AI4PKM, 시애틀 AI 생태계)를 방문자가 명확히 이해할 수 있도록 체계적으로 소개한다.
*   YouTube 채널의 콘텐츠를 주제별로 쉽게 탐색할 수 있는 구조를 제공하여 콘텐츠 접근성을 높인다.
*   시애틀 지역 AI 커뮤니티와의 연결을 강화하고, 커뮤니티 활동(코호트, 이벤트) 참여를 유도한다.
*   AI 학습 및 연구 분야에서 Catch Up AI의 전문적이고 신뢰할 수 있는 이미지를 구축하고 인지도를 높여 잠재적 파트너십 및 지속 가능한 성장 기반을 마련한다.

### 1.3. 대상 사용자
*   **AI에 관심 있는 개발자 및 비개발자:** Catch Up AI의 5가지 핵심 프로젝트를 파악하고 관련 YouTube 콘텐츠를 소비하고자 하는 사용자.
*   **시애틀 지역 AI 커뮤니티 멤버:** '시애틀 AI 생태계' 섹션에서 최신 이벤트 정보를 확인하고 커뮤니티 활동에 참여하고자 하는 사용자.
*   **Vibe Coding/Learning 방법론에 관심 있는 학습자:** 방법론의 개요 및 적용 사례를 확인하고 YouTube 채널을 구독하여 지속적으로 학습하고자 하는 사용자.

### 1.4. 주요 성공 지표
*   핵심 프로젝트 상세 페이지 방문율: 전체 방문자의 60% 이상
*   YouTube 채널 구독 전환율: 홈페이지 경유 구독 클릭 수 증가
*   웹사이트 평균 세션 시간: 3분 이상
*   AI4PKM Cohort 신청 전환율: 전년 대비 10% 증가
*   뉴스레터 구독 및 소셜 미디어 공유 횟수: 월 50건 이상

## 2. 기술 아키텍처

### 2.1. 시스템 아키텍처
본 프로젝트는 백엔드 없이 순수 HTML, CSS, JavaScript로 구성된 정적 웹사이트로 구축된다. 콘텐츠는 Product Owner(PO)가 AI 코딩 도구를 활용하여 직접 HTML 파일을 수정하는 방식으로 관리하며, Amazon S3를 통해 호스팅된다. YouTube 플레이리스트 임베드, Google Forms 연동, GitHub 기반 댓글(Utterances) 등 외부 서비스는 클라이언트 측에서 직접 연동된다. GA4를 통해 사용자 행동 데이터를 수집하며, 향후 콘텐츠 증가 시 JSON 기반 동적 로딩 방식으로 전환을 고려한다.

### 2.2. 기술 스택

| 레이어/영역 | 기술 | 설명 |
| :---------- | :--- | :--- |
| **프론트엔드** | HTML5 | 웹 표준 마크업, AI 코딩 도구 최적화 및 PO 수정 용이성 |
|             | CSS3 | 웹 표준 스타일시트, AI 코딩 도구 최적화, CSS 변수 기반 디자인 시스템 |
|             | JavaScript (Pure) | 클라이언트 측 로직 처리 (다국어 전환, 이벤트 처리, 동적 렌더링), AI 코딩 도구 최적화 |
| **호스팅**  | Amazon S3 | 정적 웹사이트 호스팅, 기존 인프라 활용, 비용 효율성, 높은 가용성 |
| **분석**    | Google Analytics 4 (GA4) | 웹사이트 트래픽 및 사용자 행동 분석, BRD 성공 지표 측정 |
| **폼/데이터 수집** | Google Forms | AI4PKM 코호트 신청, 뉴스레터 구독, 문의/피드백 등 사용자 데이터 수집, 무료 서비스 활용 |
| **데이터 저장 (폼)** | Google Sheets | Google Forms 제출 데이터 저장 및 관리 |
| **댓글**    | Utterances (GitHub) | GitHub 기반의 댓글 시스템 임베드, 서버리스 및 무료, 타겟 사용자 친화적 |
| **비디오 콘텐츠** | YouTube Embed | YouTube 채널 영상 및 플레이리스트 직접 임베딩, 최신 영상 자동 반영 |
| **버전 관리** | Git | 코드 버전 관리 및 협업, S3 배포 자동화 (향후 CI/CD 도입 시) |

### 2.3. 컴포넌트 구성
*   **메인 페이지 (index.html):** Catch Up AI 소개, 5가지 핵심 프로젝트 개요 및 링크, 최신/추천 YouTube 영상, 뉴스레터 구독 CTA, 소셜 미디어 링크.
*   **프로젝트 상세 페이지 (5개):** 각 프로젝트(Vibe Coding, Vibe Learning, Vibe Guiding, AI4PKM, 시애틀 AI 생태계)의 목표, 내용, 진행 방식, 관련 YouTube 플레이리스트 임베드, 추천 영상, 커뮤니티 활동 CTA.
*   **AI4PKM 코호트 신청 페이지:** 코호트 소개, Google Forms 연동 신청 기능.
*   **시애틀 AI 생태계 페이지:** 시애틀 AI 커뮤니티 소개, AI 관련 이벤트 정보, 관련 리소스 링크.
*   **뉴스레터 구독 섹션/페이지:** 뉴스레터 구독 양식 (Google Forms 연동).
*   **다국어 전환 버튼:** 한국어/영어 전환 버튼.
*   **글로벌 컴포넌트:** 헤더 (내비게이션), 푸터 (소셜 미디어 링크, 저작권), CSS (디자인 시스템 정의), JavaScript (공통 기능).

### 2.4. 통합 지점
*   **YouTube:** 영상 및 플레이리스트 임베딩을 통한 콘텐츠 통합.
*   **Google Forms:** AI4PKM 코호트 신청, 뉴스레터 구독, 문의/피드백 기능 연동.
*   **Google Sheets:** Google Forms를 통해 수집된 데이터 저장.
*   **Google Analytics 4 (GA4):** 웹사이트 트래픽 및 사용자 행동 데이터 수집.
*   **GitHub (Utterances):** 댓글 기능 연동.

## 3. 사용자 스토리 및 유스케이스

### 3.1. 사용자 페르소나
*   **AI 학습자 (개발자/비개발자):** Catch Up AI의 다양한 AI 학습 방법론과 프로젝트에 관심이 많으며, YouTube 채널 콘텐츠를 체계적으로 탐색하고 싶어 한다.
*   **시애틀 지역 AI 커뮤니티 멤버:** 시애틀에서 열리는 AI 관련 행사 정보에 관심이 많고, 지역 커뮤니티 활동에 참여하고자 한다.
*   **잠재적 협력 파트너/후원사:** Catch Up AI의 비전과 전문성을 이해하고, 협력 가능성을 모색한다.

### 3.2. 사용자 스토리
*   As a AI 학습자, I want to easily find information about Catch Up AI's 5 core projects so that I can understand their value and choose what to explore further. (P0, Effort: Small)
*   As a new visitor, I want to see a clear overview of Catch Up AI's methodology (Vibe Coding -> Vibe Learning -> Vibe Guiding) so that I can understand its logical progression. (P0, Effort: Small)
*   As a YouTube subscriber, I want to find the latest videos related to a specific project on the website so that I don't miss new content. (P0, Effort: Medium)
*   As a Seattle AI community member, I want to quickly find upcoming AI events so that I can plan my participation. (P0, Effort: Small)
*   As a potential cohort participant, I want to easily apply for the AI4PKM cohort so that I can join the learning program. (P0, Effort: Small)
*   As an interested user, I want to subscribe to the newsletter so that I can receive updates from Catch Up AI. (P0, Effort: Small)
*   As a global user, I want to switch between Korean and English content so that I can consume information in my preferred language. (P0, Effort: Medium)
*   As a mobile user, I want the website to be easy to navigate and read on my smartphone so that I can access information on the go. (P0, Effort: Medium)

### 3.3. 유스케이스 시나리오
1.  **홈페이지 방문 및 핵심 콘텐츠 탐색:**
    *   사용자는 YouTube 채널, 소셜 미디어 또는 검색을 통해 홈페이지에 접속한다.
    *   메인 페이지에서 Catch Up AI 소개 및 5가지 핵심 프로젝트 개요를 확인한다.
    *   관심 있는 프로젝트를 클릭하여 상세 페이지로 이동한다.
2.  **프로젝트 상세 탐색 및 YouTube 콘텐츠 소비:**
    *   프로젝트 상세 페이지에서 해당 프로젝트의 목표, 방법론, 관련 YouTube 플레이리스트(임베드)를 확인한다.
    *   임베드된 YouTube 영상을 시청하거나, 관련 YouTube 플레이리스트로 이동하여 더 많은 영상을 시청한다.
3.  **커뮤니티 활동 참여:**
    *   AI4PKM 코호트 상세 페이지에서 "신청하기" 버튼을 클릭하여 Google Forms로 이동, 신청서를 작성하고 제출한다.
    *   시애틀 AI 생태계 페이지에서 최신 AI 이벤트 정보를 확인한다.
    *   뉴스레터 구독 섹션에서 이메일을 입력하고 구독 신청을 완료한다.
4.  **다국어 전환:**
    *   페이지 상단의 언어 전환 버튼을 클릭하여 한국어 또는 영어 버전의 페이지로 전환한다.
5.  **모바일 환경 접근:**
    *   스마트폰 또는 태블릿에서 웹사이트에 접속하여 최적화된 레이아웃과 콘텐츠를 경험한다.

## 4. 기능 요구사항

### 4.1. 핵심 기능

| 기능 | 설명 | 우선순위 | 의존성 | 인수 기준 |
| :--- | :--- | :--- | :--- | :--- |
| **메인 페이지** | Catch Up AI 소개, 5개 핵심 프로젝트 개요 및 링크, 최신/추천 YouTube 영상, 뉴스레터 구독 CTA, 소셜 미디어 링크 제공 | Must Have | - | - Catch Up AI의 핵심 메시지가 명확하게 전달된다. <br> - 5개 핵심 프로젝트로 쉽게 이동할 수 있다. <br> - 최신/추천 YouTube 영상 썸네일과 링크가 표시되며 클릭 시 이동한다. <br> - 뉴스레터 구독 CTA가 명확하게 표시된다. <br> - 소셜 미디어(YouTube, LinkedIn 등) 링크가 제공된다. |
| **프로젝트 상세 페이지** | 각 프로젝트(5가지)의 목표, 내용, 진행 방식 상세 설명, 관련 YouTube 플레이리스트 임베드, 추천 영상 3-5개 표시, 커뮤니티 활동 CTA | Must Have | YouTube Embed | - 각 프로젝트의 상세 내용이 명확하게 설명된다. <br> - 관련 YouTube 플레이리스트가 임베드되어 자동으로 최신 영상이 반영된다. <br> - Product Owner가 선별한 추천 영상 3-5개가 표시되며 클릭 시 시청 가능하다. <br> - 프로젝트 관련 커뮤니티 활동(예: AI4PKM 코호트 신청)으로 이동하는 CTA가 제공된다. |
| **AI4PKM 코호트 신청** | 코호트 소개 및 참여 안내, Google Forms 연동을 통한 신청 기능 제공 | Must Have | Google Forms | - AI4PKM 코호트에 대한 상세한 정보가 제공된다. <br> - Google Forms로 연결되는 "신청하기" 버튼이 있으며, 클릭 시 신청 페이지로 이동한다. <br> - 신청 완료 후 사용자에게 감사 메시지가 표시된다. |
| **시애틀 AI 생태계 페이지** | 시애틀 AI 커뮤니티 소개 및 Catch Up AI의 역할 설명, 시애틀 AI 관련 이벤트 정보(수동 업데이트), 관련 외부 커뮤니티/리소스 링크 | Must Have | - | - 시애틀 AI 커뮤니티와 Catch Up AI의 역할이 소개된다. <br> - 최신 시애틀 AI 이벤트 정보가 업데이트되어 표시된다. <br> - 관련 외부 커뮤니티 및 리소스 링크가 제공된다. |
| **뉴스레터 구독** | 뉴스레터 구독 양식(Google Forms 연동) 제공 | Must Have | Google Forms | - 뉴스레터 구독을 위한 양식(이메일 입력 필드)이 제공된다. <br> - 구독 신청 시 Google Forms를 통해 데이터가 수집된다. <br> - 구독 완료 후 사용자에게 확인 메시지가 표시된다. |
| **다국어 지원 (한국어/영어)** | 한국어/영어 전환 버튼, 모든 콘텐츠의 한국어 및 영어 버전 제공 (HTML 파일 분리 방식) | Must Have | - | - 페이지 상단에 한국어/영어 전환 버튼이 명확하게 표시된다. <br> - 버튼 클릭 시 해당 언어 버전의 페이지로 리다이렉트된다. <br> - 모든 핵심 콘텐츠가 한국어 및 영어로 제공된다. |
| **반응형 디자인** | 데스크톱, 태블릿, 모바일 환경에서 최적화된 레이아웃 및 기능 제공 | Must Have | - | - 모든 페이지가 데스크톱, 태블릿, 모바일 화면 크기에 맞춰 레이아웃이 유동적으로 조정된다. <br> - 모바일 환경에서 내비게이션 및 콘텐츠 가독성이 확보된다. |
| **댓글 기능** | GitHub 기반 Utterances 위젯 임베드를 통한 댓글 기능 제공 | Should Have | GitHub (Utterances) | - 각 프로젝트 상세 페이지 하단에 댓글 섹션이 표시된다. <br> - GitHub 계정을 통해 로그인하여 댓글을 작성하고 조회할 수 있다. |
| **GA4 연동** | 웹사이트 트래픽 및 사용자 행동 추적을 위한 Google Analytics 4 연동 | Must Have | Google Analytics 4 | - 모든 웹페이지에 GA4 추적 코드가 삽입된다. <br> - 페이지뷰, 세션 시간, 이벤트 클릭 등 주요 사용자 행동 데이터가 수집된다. <br> - BRD에 명시된 성공 지표 측정을 위한 커스텀 이벤트(YouTube 구독 클릭, AI4PKM 신청 클릭 등)가 설정된다. |

### 4.2. 기능 상세 명세
*   **다국어 지원 (HTML 파일 분리 방식):**
    *   기본 언어는 영어이며, 한국어는 별도 `/ko/` 폴더에 정적 HTML 파일로 구성한다.
    *   예: 영어 메인 페이지 `index.html`, 한국어 메인 페이지 `/ko/index.html`.
    *   각 페이지 상단에 언어 전환 버튼을 배치하고, 클릭 시 JavaScript로 해당 언어 버전의 HTML 파일로 리다이렉트한다.
    *   콘텐츠 양이 많지 않으므로 초기에는 이 방식을 채택한다. 향후 JSON 기반 동적 로딩 전환 시 언어별 JSON 파일 분리 방식으로 확장한다.
*   **YouTube 콘텐츠 통합:**
    *   **플레이리스트 임베드:** 각 프로젝트 상세 페이지에 해당 YouTube 플레이리스트를 `<iframe>`으로 직접 임베드한다. 새 영상이 플레이리스트에 추가되면 자동으로 반영된다.
    *   **추천 영상 섹션:** Product Owner가 각 프로젝트별 핵심 영상 3-5개를 선별하여 개별 `<iframe>`으로 임베드한다.
    *   **YouTube API:** 초기 MVP에서는 사용하지 않는다. 향후 동적 기능(예: 최신 영상 자동 로딩)이 필요할 경우 YouTube Data API v3를 무료 할당량(일 10,000 units) 내에서 제한적으로 활용하는 것을 검토한다.
*   **콘텐츠 관리 (PO 직접 수정):**
    *   Product Owner는 AI 코딩 도구(Claude Code, Cursor 등)를 활용하여 HTML 파일을 직접 수정한다.
    *   콘텐츠 영역은 주석(`<!-- CONTENT START/END -->`)으로 명확히 구분하여 PO가 쉽게 식별하고 수정할 수 있도록 한다.
    *   Git을 통해 버전 관리를 수행하며, 로컬에서 변경 사항을 미리보기 후 커밋한다.
*   **GA4 이벤트 트래킹:**
    *   YouTube 채널 구독 버튼, YouTube 영상/플레이리스트 링크 클릭 시 `youtube_subscribe_click`, `video_click` 등의 커스텀 이벤트를 `gtag()` 함수를 통해 기록한다.
    *   AI4PKM 코호트 신청 버튼, 뉴스레터 구독 버튼 클릭 시 `cohort_apply_click`, `newsletter_subscribe_click` 등의 커스텀 이벤트를 기록한다.

### 4.3. 사용자 인터페이스 요구사항
*   **일관된 디자인 시스템:** Catch Up AI의 브랜드 아이덴티티를 반영하는 일관된 UX/UI를 제공한다.
    *   CSS 변수(Custom Properties)를 활용하여 색상, 폰트, 간격 등 디자인 토큰을 중앙에서 관리한다.
    *   `/css/variables.css` 파일에 모든 디자인 토큰을 정의하며, 모든 CSS 파일에서 이 변수들을 참조한다.
    *   AI 코딩 도구 사용 시, 기존 CSS 변수 및 클래스 사용을 명시적으로 프롬프트에 지시하여 일관성을 유지한다.
    *   PO가 UI 코드를 수정할 경우, 정의된 CSS 변수 범위 내에서만 변경하도록 가이드라인을 제공한다 (새로운 인라인 스타일 또는 클래스 추가 금지).
*   **반응형 디자인:**
    *   모바일 우선(Mobile-first) 접근 방식을 적용하여 다양한 기기에서 최적화된 사용자 경험을 제공한다.
    *   Viewport 메타 태그를 사용하여 반응형 동작을 보장한다.
*   **와이어프레임/UI 흐름:**
    *   각 페이지(메인, 프로젝트 상세, 코호트, 생태계)의 주요 섹션 배치 및 내비게이션 흐름을 정의한다.
    *   간결하고 직관적인 내비게이션 구조를 통해 사용자가 원하는 정보를 최소한의 클릭으로 찾을 수 있도록 한다.

## 5. API 상세 명세

### 5.1. API 엔드포인트
*   **YouTube Embed:** `<iframe>` 태그를 사용하여 YouTube 영상 및 플레이리스트를 직접 임베드한다. 특정 API 엔드포인트 호출은 없음.
*   **Google Forms:** Google Forms가 제공하는 `<iframe>` 임베드 코드 또는 링크를 활용하여 신청/구독 폼을 연동한다.
*   **Utterances:** GitHub 기반 Utterances 위젯의 `script` 태그를 사용하여 댓글 기능을 임베드한다.

### 5.2. 인증 및 권한 부여
*   웹사이트 자체적으로 사용자 인증 및 권한 부여 기능은 없다.
*   Google Forms는 Google의 인증 및 권한 모델을 따른다.
*   Utterances는 GitHub의 인증 모델을 따른다.

### 5.3. 오류 처리
*   외부 서비스(YouTube, Google Forms) 연동 시 오류 발생 시 사용자에게 친화적인 폴백 메시지를 표시하거나, 해당 기능이 일시적으로 작동하지 않음을 안내한다.
*   예: YouTube 영상 로딩 실패 시 "영상을 불러올 수 없습니다" 메시지 표시.
*   정적 웹사이트이므로 서버 측 에러 핸들링은 없다.

## 6. 데이터 모델

### 6.1. 데이터베이스 스키마
본 프로젝트는 데이터베이스를 사용하지 않는다. 모든 콘텐츠는 HTML 파일 또는 JSON 파일(향후 전환 시)에 저장된다.

### 6.2. 데이터 흐름
1.  **사용자 웹사이트 접속:** 사용자가 웹 브라우저를 통해 Catch Up AI 홈페이지 URL에 접속한다.
2.  **S3 콘텐츠 로딩:** Amazon S3에 호스팅된 정적 HTML, CSS, JavaScript 파일이 사용자 브라우저로 전송된다.
3.  **YouTube 콘텐츠 로딩:** 브라우저에서 HTML 내의 `<iframe>` 태그를 통해 YouTube 서버로부터 영상/플레이리스트 콘텐츠를 직접 로딩한다.
4.  **Google Forms 연동:** 사용자가 신청/구독 폼을 제출하면, 브라우저에서 Google Forms 서버로 직접 데이터가 전송되고 Google Sheets에 저장된다.
5.  **Utterances 댓글 연동:** 사용자가 댓글을 작성하면, 브라우저에서 Utterances 위젯을 통해 GitHub API로 직접 댓글 데이터가 전송되어 GitHub Issues에 저장된다.
6.  **GA4 데이터 전송:** 사용자 행동(페이지 뷰, 이벤트 클릭 등) 데이터는 브라우저에서 Google Analytics 4 서버로 직접 전송된다.

### 6.3. 데이터 유효성 검사 규칙
*   **Google Forms:** Google Forms 자체에서 제공하는 입력 필드 유효성 검사(필수 항목, 이메일 형식 등)를 활용한다.
*   **클라이언트 측 유효성 검사:** HTML5 `required` 속성 및 간단한 JavaScript를 사용하여 폼 제출 전 기본적인 클라이언트 측 유효성 검사를 수행할 수 있다.

## 7. 보안 및 규정 준수

### 7.1. 보안 요구사항
*   **HTTPS:** 모든 웹사이트 트래픽은 HTTPS를 통해 암호화되어야 한다. (Amazon S3 + CloudFront 또는 S3 자체 HTTPS 구성)
*   **데이터 보호:** Google Forms를 통해 수집되는 개인 정보(이름, 이메일 등)는 Google의 보안 정책을 따르며, Catch Up AI 웹사이트 자체에서는 민감한 개인 정보를 직접 저장하지 않는다.
*   **악성 코드 방지:** 정적 웹사이트이므로 서버 측 공격에는 비교적 안전하나, XSS (Cross-Site Scripting) 공격 방지를 위해 사용자 입력 필드에 대한 적절한 새니타이징(sanitizing)을 고려한다 (Utterances와 같은 외부 서비스 사용 시 해당 서비스의 보안 정책에 의존).
*   **Git 보안:** Git 저장소는 적절한 접근 제어(비공개 저장소)를 통해 코드 무결성을 유지한다.

### 7.2. 개인정보 보호 및 규정 준수
*   **개인정보 처리 방침:** 웹사이트 하단에 간단한 개인정보 처리 안내(수집 목적, 보관 기간, 삭제 요청 방법 등)를 명시한다.
*   **GDPR/CCPA:** 웹사이트 자체적으로 개인 식별 정보를 저장하지 않으므로 직접적인 규제 준수 부담은 적으나, Google Forms 및 GA4 사용 시 해당 서비스의 개인정보 처리 방침을 따른다.
*   **쿠키 동의:** GA4를 사용하므로, 초기 로딩 시 사용자에게 쿠키 사용에 대한 동의를 얻는 배너 또는 팝업을 구현할 수 있다 (선택 사항).

### 7.3. 보안 테스트 요구사항
*   **정기적인 코드 검토:** PO의 HTML 직접 수정 방식에 따른 잠재적 취약점(예: 스크립트 삽입) 방지를 위해 정기적으로 코드를 검토한다.
*   **외부 서비스 보안:** 연동된 Google Forms, YouTube, Utterances 등 외부 서비스의 보안 정책 및 업데이트를 주시한다.

## 8. 성능 요구사항

### 8.1. 성능 지표

| 지표 | 목표 | 측정 방법 |
| :--- | :--- | :--- |
| 페이지 로딩 시간 (LCP) | 2초 이내 | Google Lighthouse, Google PageSpeed Insights |
| 응답 시간 (FID) | 100ms 이내 | Google Lighthouse, Google PageSpeed Insights |
| 동시 접속자 처리 | 월간 최대 10,000명 | GA4 트래픽 모니터링, S3/CloudFront 지표 |
| CLS (Cumulative Layout Shift) | 0.1 이하 | Google Lighthouse, Google PageSpeed Insights |

### 8.2. 확장성 요구사항
*   **트래픽 증가 대응:** 초기 S3 호스팅만으로 충분하나, 트래픽이 급증할 경우 Amazon CloudFront CDN을 추가하여 지리적으로 분산된 캐싱을 통해 성능 및 가용성을 확보한다.
*   **콘텐츠 증가 대응:** 콘텐츠 양이 증가할 경우, JSON 기반 동적 로딩 방식으로 전환을 고려한다. Product Owner가 JSON 파일만 수정하도록 하여 HTML 직접 수정의 부담을 줄이고 확장성을 확보한다.
*   **다국어 지원:** 초기부터 한국어/영어 다국어 지원을 구현하여 글로벌 사용자에게 확장 가능한 구조를 갖춘다. (HTML 파일 분리 방식 -> JSON 기반 다국어 파일 전환)

### 8.3. 최적화 전략
*   **이미지 최적화:** 웹페이지에 사용되는 모든 이미지는 웹에 최적화된 형식(WebP 등) 및 크기로 압축하여 사용한다. `<img>` 태그에 `loading="lazy"` 속성을 적용하여 지연 로딩을 구현한다.
*   **CSS 및 JS 최소화:** 모든 CSS 및 JavaScript 파일은 배포 전 최소화(Minification)하여 파일 크기를 줄인다.
*   **브라우저 캐싱:** HTTP 헤더를 통해 브라우저 캐싱 정책을 설정하여 재방문 시 로딩 속도를 향상시킨다.
*   **CDN 활용:** (향후 필요 시) CloudFront와 같은 CDN을 도입하여 정적 콘텐츠 전송 속도를 향상시킨다.

## 9. 테스트 및 품질 보증

### 9.1. 테스트 전략
*   **수동 테스트:** 모든 페이지에 대한 기능 테스트 (링크 작동, 폼 제출, 다국어 전환 등) 및 UI/UX 테스트 (디자인 일관성, 반응형 확인)를 수동으로 수행한다.
*   **크로스 브라우징 테스트:** 주요 웹 브라우저(Chrome, Firefox, Safari, Edge) 및 모바일 기기에서 웹사이트가 올바르게 렌더링되고 기능하는지 확인한다.
*   **성능 테스트:** Google Lighthouse 및 PageSpeed Insights를 사용하여 웹페이지 성능 지표를 주기적으로 측정하고 개선한다.
*   **접근성 테스트:** 웹 콘텐츠 접근성 지침(WCAG) 2.1 AA 수준 준수를 위해 수동 검사 및 자동화 도구(예: axe DevTools)를 활용한다.

### 9.2. 인수 기준
*   모든 핵심 기능(메인 페이지, 프로젝트 상세, 신청 폼, 다국어 전환 등)이 BRD 및 PRD에 명시된 대로 정상 작동한다.
*   모든 페이지는 2초 이내에 로딩된다.
*   데스크톱, 태블릿, 모바일 환경에서 일관되고 최적화된 UI/UX를 제공한다.
*   GA4를 통해 주요 성공 지표 측정을 위한 데이터가 올바르게 수집된다.
*   Google Forms 연동 기능이 정상 작동하며 데이터가 Google Sheets에 올바르게 저장된다.
*   콘텐츠 관리 가이드라인에 따라 PO가 AI 코딩 도구를 활용하여 콘텐츠를 업데이트할 수 있다.

### 9.3. 품질 지표
*   Google Lighthouse Score: Performance 80점 이상, Accessibility 90점 이상, Best Practices 90점 이상, SEO 90점 이상.
*   버그 밀도: 출시 전 Critical/High 버그 0개.
*   코드 일관성: CSS 변수 및 BEM(Block Element Modifier) 유사 네이밍 컨벤션 준수율 90% 이상.

## 10. 배포 및 DevOps

### 10.1. 배포 전략
*   **수동 배포 (초기):** Product Owner가 Git 저장소에 커밋된 HTML, CSS, JavaScript 파일을 Amazon S3 버킷에 직접 업로드한다.
*   **Git 기반 배포 (향후 고려):** Git push 시 S3 버킷으로 자동 동기화되는 간단한 CI/CD 파이프라인(예: GitHub Actions, AWS CodePipeline) 도입을 검토한다.
*   **환경:** 운영 환경(Production)만 존재하며, 개발 및 테스트는 로컬 환경에서 진행한다.

### 10.2. 모니터링 및 로깅
*   **GA4 모니터링:** Google Analytics 4를 통해 실시간 트래픽, 사용자 행동, 오류 발생 여부(예: 404 페이지)를 모니터링한다.
*   **S3 접근 로그:** Amazon S3 접근 로그를 활성화하여 웹사이트 접근 패턴 및 잠재적 문제점을 분석할 수 있다.
*   **오류 추적:** 클라이언트 측 JavaScript 오류는 GA4의 오류 추적 기능을 활용하거나, Sentry와 같은 경량 오류 추적 도구를 통합할 수 있다 (선택 사항).

### 10.3. 롤백 절차
*   Git을 통해 모든 코드 변경 사항이 버전 관리되므로, 문제가 발생할 경우 이전 Git 커밋으로 롤백하여 S3에 재배포한다.
*   Amazon S3의 버전 관리 기능을 활용하여 이전 버전의 객체로 손쉽게 복구할 수 있다.

## 11. 타임라인 및 마일스톤

| 단계 | 산출물 | 타임라인 | 의존성 |
| :--- | :--- | :--- | :--- |
| **Phase 1: 계획 및 설계** | BRD/PRD 승인, 초기 디자인 가이드라인, 핵심 기술 스택 확정 | 2026-02-15 ~ 2026-02-29 | BRD |
| **Phase 2: MVP 개발 (핵심 기능)** | 메인 페이지, 5개 프로젝트 상세 페이지 (영어), 다국어 전환 (HTML 기반), AI4PKM 신청, 뉴스레터 구독, GA4 연동 | 2026-03-01 ~ 2026-04-30 | - |
| **Phase 3: MVP 배포 및 테스트** | S3 배포, 기능 테스트, 반응형 테스트, 성능 최적화, 보안 점검 | 2026-05-01 ~ 2026-05-15 | Phase 2 완료 |
| **Phase 4: 한국어 콘텐츠 추가** | 모든 MVP 페이지의 한국어 버전 생성 및 적용 | 2026-05-16 ~ 2026-06-30 | Phase 3 완료 |
| **Phase 5: 추가 기능 및 고도화** | 시애틀 AI 생태계 페이지, 댓글 기능 (Utterances), JSON 기반 동적 로딩 전환 (필요 시), YouTube API 연동 (필요 시) | 2026-07-01 ~ 2026-09-30 | Phase 4 완료 |

## 12. 제약사항 및 가정

### 12.1. 기술적 가정
*   Product Owner는 AI 코딩 도구를 활용하여 HTML 파일을 직접 수정하고 Git을 통해 배포할 수 있는 기본적인 기술 역량을 갖추고 있다.
*   Google Forms, Google Sheets, YouTube Embed 등 외부 무료 서비스는 안정적으로 운영될 것이다.
*   초기에는 복잡한 동적 콘텐츠나 사용자 상호작용 기능이 필요하지 않을 것이다.
*   콘텐츠 관리를 위한 별도의 CMS 솔루션은 도입하지 않는다.
*   Amazon S3 정적 웹사이트 호스팅 비용은 최소화되며, 예상 트래픽 범위 내에서 무료 또는 저렴하게 운영될 수 있다.

### 12.2. 리소스 제약
*   **예산 제약:** 본 프로젝트는 개인 프로젝트로 예산이 거의 없으므로 유료 서비스 사용을 최소화하고 무료 또는 저렴한 솔루션을 우선적으로 활용한다.
*   **개발 인력:** Product Owner가 AI 코딩 도구를 활용하여 개발 및 콘텐츠 관리를 주도한다.

### 12.3. 외부 의존성
*   **YouTube:** YouTube 채널 콘텐츠(영상, 플레이리스트) 제공 및 임베딩.
*   **Google Forms:** AI4PKM 코호트 신청 및 뉴스레터 구독 기능 제공.
*   **Google Sheets:** Google Forms를 통해 수집된 데이터 저장.
*   **Amazon S3:** 웹사이트 호스팅 인프라 제공.
*   **Google Analytics 4 (GA4):** 웹사이트 트래픽 및 사용자 행동 분석.
*   **GitHub (Utterances):** 댓글 기능 제공.