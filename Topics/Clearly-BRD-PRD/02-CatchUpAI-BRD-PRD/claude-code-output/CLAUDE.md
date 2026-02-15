# Claude Code 프로젝트 가이드: Catch Up AI 2026 홈페이지

## 1. 프로젝트 개요

Catch Up AI 2026 홈페이지는 YouTube 채널 Catch Up AI의 핵심 콘텐츠와 활동을 체계적으로 소개하는 정적 웹사이트입니다. 이 프로젝트는 AI에 관심 있는 개발자 및 비개발자, 시애틀 지역 AI 커뮤니티 멤버, Vibe Coding/Learning 방법론에 관심 있는 학습자를 대상으로 합니다. 주요 목표는 Catch Up AI의 5가지 핵심 프로젝트를 명확히 소개하고, YouTube 콘텐츠 접근성을 높이며, 커뮤니티 참여를 유도하고, 브랜드 인지도를 강화하는 것입니다.

이 프로젝트는 백엔드 없이 순수 HTML, CSS, JavaScript로 구성된 정적 웹사이트로, Amazon S3를 통해 호스팅됩니다. Product Owner(PO)가 AI 코딩 도구(Claude Code)를 활용하여 직접 HTML 파일을 수정하는 방식으로 콘텐츠를 관리합니다.

## 2. 아키텍처 설명

본 프로젝트는 클라이언트 측에서만 동작하는 정적 웹사이트 아키텍처를 채택합니다.

*   **Frontend:** HTML5, CSS3, 순수 JavaScript로 구성됩니다. 모든 페이지는 정적 HTML 파일로 제공됩니다.
*   **Hosting:** Amazon S3를 사용하여 정적 파일을 호스팅합니다. 향후 트래픽 증가 시 Amazon CloudFront CDN을 추가하여 성능을 최적화할 수 있습니다.
*   **외부 서비스 연동:**
    *   **YouTube:** `<iframe>` 태그를 사용하여 영상 및 플레이리스트를 직접 임베드합니다.
    *   **Google Forms:** `<iframe>` 임베드 코드 또는 링크를 통해 신청/구독 폼을 연동합니다.
    *   **Utterances:** GitHub 기반 댓글 시스템을 `script` 태그로 임베드합니다.
    *   **Google Analytics 4 (GA4):** `gtag.js`를 사용하여 사용자 행동 데이터를 수집합니다.
*   **콘텐츠 관리:** PO가 Claude Code와 같은 AI 코딩 도구를 활용하여 HTML 파일을 직접 수정하고 Git을 통해 버전 관리합니다.

## 3. 기술 스택

| 레이어/영역 | 기술 | 설명 |
| :---------- | :--- | :--- |
| **프론트엔드** | HTML5 | 웹 표준 마크업, AI 코딩 도구 최적화 및 PO 수정 용이성 |
|             | CSS3 | 웹 표준 스타일시트, AI 코딩 도구 최적화, CSS 변수 기반 디자인 시스템 |
|             | JavaScript (Pure) | 클라이언트 측 로직 (다국어 전환, 이벤트 처리), AI 코딩 도구 최적화 |
| **호스팅**  | Amazon S3 | 정적 웹사이트 호스팅, 기존 인프라 활용, 비용 효율성, 고가용성 |
| **분석**    | Google Analytics 4 (GA4) | 웹사이트 트래픽 및 사용자 행동 분석, BRD 성공 지표 측정 |
| **폼/데이터 수집** | Google Forms | 사용자 데이터 수집 (신청, 구독), 무료 서비스 활용 |
| **데이터 저장 (폼)** | Google Sheets | Google Forms 제출 데이터 저장 및 관리 |
| **댓글**    | Utterances (GitHub) | GitHub 기반 댓글 시스템 임베드, 서버리스 및 무료 |
| **비디오 콘텐츠** | YouTube Embed | YouTube 채널 영상 및 플레이리스트 직접 임베딩 |
| **버전 관리** | Git | 코드 버전 관리, S3 배포 자동화 (향후 CI/CD 도입 시) |

## 4. 개발 명령어 (예시)

본 프로젝트는 정적 웹사이트이므로 복잡한 빌드 스크립트가 필요하지 않습니다.

*   **로컬 개발 서버 실행 (Python 예시):**
    ```bash
    python -m http.server 8000
    # 또는
    npx http-server . -p 8000
    ```
    (프로젝트 루트 디렉토리에서 실행하여 `http://localhost:8000`으로 접속)

*   **Git 관련 명령어:**
    ```bash
    git status
    git add .
    git commit -m "feat: implement main page layout"
    git push origin main
    ```

## 5. 코딩 컨벤션

### 5.1. HTML

*   **시맨틱 태그 사용:** `header`, `nav`, `main`, `section`, `article`, `footer` 등 시맨틱 HTML5 태그를 사용하여 문서 구조를 명확히 합니다.
*   **들여쓰기:** 2칸 공백을 사용합니다.
*   **주석:** AI 코딩 도구 사용 시 콘텐츠 영역을 명확히 구분하기 위해 `<!-- CONTENT START -->` 및 `<!-- CONTENT END -->` 주석을 활용합니다.
*   **다국어:** 영어 버전 파일 (`index.html`, `project-x.html`)과 한국어 버전 파일 (`ko/index.html`, `ko/project-x.html`)을 분리하여 관리합니다.

### 5.2. CSS

*   **CSS 변수 사용:** `/css/variables.css`에 정의된 CSS 변수 (`--primary-color`, `--font-family-base` 등)를 적극적으로 활용합니다. PO가 UI를 수정할 경우, 이 변수 범위 내에서만 변경하도록 가이드합니다.
*   **BEM (Block Element Modifier) 유사 네이밍:** 클래스명은 `block__element--modifier` 형태를 지향하여 예측 가능하고 재사용 가능한 스타일을 만듭니다. (예: `btn`, `btn--primary`, `card__title`, `card__image`)
*   **들여쓰기:** 2칸 공백을 사용합니다.
*   **속성 순서:** 관련된 속성들을 그룹화하여 가독성을 높입니다 (예: 레이아웃 -> 박스 모델 -> 타이포그래피 -> 색상 -> 기타).
*   **미디어 쿼리:** 모바일 우선(Mobile-first) 접근 방식을 따르며, `min-width`를 사용하여 작은 화면에서 큰 화면으로 스타일을 확장합니다.

### 5.3. JavaScript

*   **순수 JavaScript:** ES6+ 문법을 사용하며, 외부 라이브러리 사용을 최소화합니다.
*   **들여쓰기:** 2칸 공백을 사용합니다.
*   **변수 선언:** `const`와 `let`을 사용하고, `var`는 사용하지 않습니다.
*   **함수:** 화살표 함수를 적극적으로 활용합니다.
*   **주석:** 복잡한 로직에는 설명을 위한 주석을 추가합니다.
*   **GA4 이벤트:** `gtag()` 함수를 사용하여 BRD에 명시된 커스텀 이벤트를 추적합니다.

## 6. 주요 패턴 및 모범 사례

*   **정적 사이트 최적화:**
    *   **이미지 최적화:** WebP와 같은 최신 포맷 사용, `loading="lazy"` 속성 활용.
    *   **CSS/JS 최소화:** 배포 전 파일 크기 최소화.
    *   **브라우저 캐싱:** 적절한 HTTP 캐싱 헤더 설정.
*   **다국어 처리:** HTML 파일 분리 방식을 사용하며, JavaScript로 언어 전환 시 해당 언어의 HTML 파일로 리다이렉트합니다.
*   **콘텐츠 관리 용이성:** PO가 AI 코딩 도구를 통해 쉽게 콘텐츠를 수정할 수 있도록 HTML 구조를 단순하게 유지하고, 콘텐츠 영역을 명확히 구분합니다.
*   **접근성 (Accessibility):** WCAG 2.1 AA 수준 준수를 목표로 시맨틱 HTML, ARIA 속성, 키보드 내비게이션 지원 등을 고려합니다.
*   **반응형 디자인:** 모바일 우선 접근 방식과 유연한 그리드 시스템, 미디어 쿼리를 사용하여 모든 기기에서 최적의 경험을 제공합니다.

## 7. 디렉토리 구조

```
.
├── .claude/
│   └── settings.json
├── css/
│   ├── main.css            # 전역 스타일
│   ├── variables.css       # CSS 변수 정의
│   └── components/         # 재사용 가능한 컴포넌트 스타일 (예: button.css, card.css)
├── js/
│   ├── main.js             # 전역 스크립트 (GA4, 다국어 전환 등)
│   └── utils.js            # 유틸리티 함수
├── img/                    # 이미지 파일
├── ko/                     # 한국어 버전 페이지
│   ├── index.html
│   ├── vibe-coding.html
│   ├── vibe-learning.html
│   ├── vibe-guiding.html
│   ├── ai4pkm.html
│   └── seattle-ai-ecosystem.html
├── index.html              # 메인 페이지 (영어)
├── vibe-coding.html        # 프로젝트 상세 페이지 (영어)
├── vibe-learning.html
├── vibe-guiding.html
├── ai4pkm.html
├── seattle-ai-ecosystem.html
├── 404.html                # 404 에러 페이지
├── README.md
├── CLAUDE.md               # Claude Code 프로젝트 가이드
└── REFERENCE_DOCUMENT.md   # 전체 요구사항 및 기술 상세 문서
```

## 8. 구현 시 유의사항 및 참고

*   **AI 코딩 도구 활용:** Claude Code에 프롬프트를 제공할 때, 기존 코드 컨벤션, CSS 변수 사용, 디렉토리 구조, 다국어 처리 방식 등을 명확히 지시하여 일관성을 유지합니다.
*   **콘텐츠 업데이트:** PO가 직접 HTML을 수정하므로, AI 도구로 생성된 코드는 가급적 단순하고 이해하기 쉬워야 합니다. 콘텐츠 영역은 주석으로 명확히 구분합니다.
*   **외부 서비스 변경:** YouTube, Google Forms, Utterances 등의 외부 서비스 정책 변경 시 웹사이트 기능에 영향을 줄 수 있으므로 주기적인 확인이 필요합니다.
*   **성능 최적화:** 이미지, CSS, JS 파일은 항상 최적화된 상태로 배포되도록 관리합니다.
*   **보안:** 정적 웹사이트이지만, XSS 등 클라이언트 측 공격에 대비하여 외부 콘텐츠 임베드 시 주의하고, 사용자 입력(댓글 등)은 반드시 새니타이징 처리된 안전한 서비스를 사용합니다.
*   **Git 커밋 메시지:** 의미 있는 커밋 메시지 (예: `feat: add main page layout`, `fix: correct typo in project-x page`)를 사용하여 변경 이력을 명확히 합니다.