# VibeLearn AI Topic Starter

> 이 파일은 새로운 Topic 학습을 시작할 때 작성하는 템플릿입니다.
>
> **사용 방법**:
> 1. 이 파일을 복사하여 `[TopicName]_topic_starter.md`로 저장
> 2. 아래 항목들을 채워서 작성
> 3. AI에게 이 파일을 전달하여 Topic 폴더 구조 생성 요청
> 4. 생성된 폴더에서 학습 시작!

---

## 📌 Topic 기본 정보

### Topic 이름
**형식**: 영문, 하이픈 또는 언더스코어 사용 (공백 없음)
**예시**: `MCP-Basics`, `Docker_Fundamentals`, `FastAPI-Tutorial`

```
Topic 이름: Seattle-AI-Week-2026
```

### Topic 설명
**목적**: 이 Topic이 무엇인지 한두 문장으로 설명

```
설명: 2026-10-26~30 Seattle AI Week(WTIA 주최, 75+ 행사)에 「배우기」를 첫째 목표로 참가한다. 사전에 Luma 전수 수집 → 큐레이션 → 참가 일정·티켓 확정, 현장에서는 세션 녹화 + 그날그날 현장 정리, 사후에 녹화본을 한국어 자막 유튜브 영상으로 올리고, Transcript · 현장 정리 · 외부 언론 보도 세 소스를 종합해 「행사 소개 · 진행 상황 · 취재 내용 · 2026 시애틀 AI 트렌드」 콘텐츠를 유튜브 영상 · 신문 기사 · Substack 글로 낸다. 7월 Seattle Tech Week 두 Topic(참가 계획 · 기사 연재)의 파이프라인을 재사용한다
```

### 학습 목적
**왜 이것을 배우는가?**

```
학습 목적:
- AI 에 관심이 많아 **배우는 것이 첫째** — 큐레이션 기준은 취업·네트워킹보다 「내가 배울 것」
- 현장에서 놓치기 쉬운 내용을 충실히 배우려고 **녹화**하고, 그것을 한국어 자막 유튜브 영상으로 공유한다
- 녹화 Transcript · 그날그날 현장 정리 · 외부 언론 보도 **세 소스를 종합**해 콘텐츠를 만든다
- 콘텐츠 4축(행사 소개 · 진행 상황 · 취재 내용 · 2026 시애틀 AI 트렌드)을 매체 3종(유튜브 · 신문 기사 · Substack)으로 낸다
```

### 예상 학습 기간
**현실적으로 예상되는 기간**

```
예상 기간: 12주 (2026-09-13 → 12-06) · 총 약 48시간 — 사전 6주 8h · 현장 1주 15h · 사후 5주 25h (사용자 선택 9/13: 「기간 조정」 — 사후 콘텐츠를 11월 말까지)
```

---

## 🎯 학습 목표

**이 Topic을 완료했을 때 달성하고 싶은 구체적 목표**

```
- [ ] Luma 캘린더 전수(75+)를 API 로 수집해 날짜·시간·가격·온/오프라인·녹화 정책이 있는 사실표를 만들고, 「배울 것」 기준으로 우선순위 큐레이션을 할 수 있다
- [ ] 10/26~30 참가 일정을 확정해 티켓(Opening $125 · Summit $225 등)을 얼리버드 안에 사고 Google Calendar 에 등록할 수 있다
- [ ] 녹화 장비·허가·저장·백업 절차와 일일 현장 정리 템플릿을 리허설로 검증해, 현장 5일을 사고 없이 운영할 수 있다
- [ ] 녹화본을 `video-subtitles` 파이프라인으로 한국어 자막 유튜브 영상으로 올릴 수 있다 (세션당 목표 리드타임 3일)
- [ ] Transcript · 현장 정리 · 외부 보도 세 소스를 Evidence Bank 로 종합해 「2026 시애틀 AI 트렌드」를 근거 표기로 정리할 수 있다
- [ ] 콘텐츠 4축을 유튜브 영상 · 신문 기사 · Substack 글로 각 1편 이상 내고 claim ledger 로 출처를 댈 수 있다
```

**권장**: 3-5개의 명확하고 검증 가능한 목표

---

## 🛠️ 학습 환경

### 운영 체제
```
OS: Windows 11
버전: Home 10.0.26200
```

### 주요 도구 및 기술 스택
**이 Topic 학습에 필요한 도구들**

```
- Luma 공개 API (`api.luma.com/calendar/get-items`) + `web-data-extraction` 스킬 — 행사 전수 수집
- Google Calendar MCP — 참가 일정 등록 (Tech Week 선례)
- 녹화: 폰/카메라 + 외장 마이크 (장비 목록은 M3 에서 확정) · 현장 노트: 폰 Obsidian 또는 음성 메모
- `video-subtitles` 스킬 (전사 → 번역 → 자막 렌더 → MP4) · ffmpeg · Remotion
- `youtube-channel-archiver` / `youtube-transcript-summarizer` — 외부 영상 소스
- Substack · 유튜브 · (기사) — Tech Week Article-Writing 파이프라인
- Obsidian 볼트 — 일일 현장 정리 · Evidence Bank
```

### 사전 지식 (Prerequisites)
**이 Topic을 학습하기 전에 알아야 할 것**

```
필수:
- `Topics/Seattle-Tech-Week-2026/` 의 수집→큐레이션→일정 절차 (04-Process-Notes 포함)
- `Topics/Seattle-Tech-Week-2026-Article-Writing/` 의 Evidence Bank · Factcheck 구조
- `video-subtitles` 스킬 실사용 경험 (9/10~12 Seattle Data·AI·Security 3연사 자막)

권장:
- 행사 녹화 에티켓·정책 (세션별 촬영 허용 여부 확인 습관)
- `youtube-sns-promo` 스킬 (영상 공개 후 홍보)
- 2026 상반기 시애틀 AI 생태계 배경 (Tech Week 기사 연재의 트렌드 분석)
```

---

## 📚 참조 자료 (Optional)

### 공식 문서
```
- Seattle AI Week 공식: https://www.seattleaiweek.com
- Luma 캘린더: https://luma.com/Seattle-AI-Week-2026
- Opening Reception: https://luma.com/9hfhvzkt · The Summit: https://luma.com/gi2fceh5
```

### 튜토리얼 및 강의
```
- (없음)
```

### 관련 GitHub 저장소
```
- (해당 없음)
```

### 추가 학습 자료
**파일, 문서, 동영상 등을 `vl_materials/` 폴더에 저장 가능**

```
vl_materials/ 폴더에 추가할 자료:
- 시작 시점: Materials_For_Topics/Seattle-AI-Week-2026/ 의 두 문서 (원문 · 사실표)
- M1 에서 Luma API JSON 원본 · 행사 페이지 클리핑 추가
- M4 현장 주간: 녹화 파일은 볼트 밖(C:/Users/dougg/Videos/...), 볼트에는 목록·해시·정리만
- M6 에서 외부 보도 클리핑(Ingest/Clippings)
```

---

## 🎓 학습 접근 방식 (Optional)

### 선호하는 학습 스타일
```
- [ ] 이론 먼저, 실습 나중
- [x] 실습 중심, 필요한 이론만 (권장)
- [ ] 이론과 실습 병행
```

### 시간 투자 계획
```
- 주당 학습 시간: 사전 3h · 현장 주간 15h · 사후 4h
- 학습 가능 요일: 일요일 라이브 + 주중 1~2회 · 10/26~30 은 현장
- 1회당 학습 시간: 1-2시간 (현장은 하루 단위)
```

### 특별히 집중하고 싶은 영역
```
- 「배울 것」 기준 큐레이션 — 취업·네트워킹은 부차
- 녹화 → 자막 → 업로드 리드타임을 세션당 3일로
- 세 소스(Transcript · 현장 정리 · 외부 보도) 종합과 근거 표기
- 매체 3종(유튜브 · 기사 · Substack) 각 1편 이상
```

---

## 🚀 다음 단계

### 이 파일 작성 완료 후:

1. **Topic 폴더 생성 요청**
   - AI에게 이 파일을 전달
   - "이 topic_starter.md를 바탕으로 Topic 폴더 구조를 만들어주세요" 요청

2. **생성될 폴더 구조**
   ```
   [TopicName]/
   ├── topic_info.md              # 이 파일이 복사됨
   ├── vl_prompts/
   │   ├── roadmap_prompt.md      # Topic 정보가 주입된 프롬프트
   │   └── daily_learning_prompt.md
   ├── vl_roadmap/                # Roadmap 저장 위치
   ├── vl_worklog/                # 학습 일지 저장 위치
   └── vl_materials/              # 참조 자료 저장 위치 (Optional)
   ```

3. **Roadmap 생성**
   - `[TopicName]/vl_prompts/roadmap_prompt.md` 파일을 AI에게 전달
   - AI가 체계적인 학습 로드맵 생성
   - 생성된 로드맵을 `vl_roadmap/` 폴더에 저장

4. **학습 시작!**
   - `daily_learning_prompt.md`로 매일 학습 진행
   - WorkLog 작성으로 진행 상황 추적
   - Retrospective로 지속적 개선

---

## 📝 작성 예시

### 예시 1: MCP Basics 학습
```markdown
## 📌 Topic 기본 정보
Topic 이름: MCP-Basics
설명: Model Context Protocol의 기본 개념과 서버/클라이언트 구현 학습
학습 목적:
- MCP 프로토콜 이해 및 실무 적용
- AI 에이전트와 도구 통합 능력 향상
예상 기간: 3주 (주당 6-8시간)

## 🎯 학습 목표
- [ ] MCP 프로토콜 아키텍처를 설명할 수 있다
- [ ] 간단한 MCP 서버를 직접 구현할 수 있다
- [ ] Claude Desktop과 MCP 서버를 연동할 수 있다
- [ ] 실무 프로젝트에 MCP를 적용할 수 있다

## 🛠️ 학습 환경
OS: Windows 11
주요 도구:
- VS Code
- Python 3.11
- Node.js 20
- Claude Desktop

사전 지식:
필수:
- Python 기본 문법
- JSON 데이터 형식
권장:
- HTTP/JSON-RPC 개념
- TypeScript 기본 (Node.js 서버 구현 시)

## 📚 참조 자료
- MCP 공식 문서: https://modelcontextprotocol.io
- GitHub 저장소: https://github.com/anthropics/mcp
```

### 예시 2: Docker Fundamentals 학습
```markdown
## 📌 Topic 기본 정보
Topic 이름: Docker-Fundamentals
설명: 컨테이너 기술 Docker의 기본 개념부터 실전 활용까지
학습 목적:
- 개발 환경 컨테이너화로 생산성 향상
- 배포 프로세스 자동화
예상 기간: 2주 (주당 5시간)

## 🎯 학습 목표
- [ ] Docker 이미지와 컨테이너 개념을 이해한다
- [ ] Dockerfile을 작성하여 커스텀 이미지를 만들 수 있다
- [ ] docker-compose로 멀티 컨테이너 환경을 구성할 수 있다

## 🛠️ 학습 환경
OS: macOS Sonoma
주요 도구:
- Docker Desktop
- VS Code with Docker extension

사전 지식:
필수:
- Linux 기본 명령어
- 네트워크 기본 개념
```

---

## 💡 작성 팁

### ✅ Do's (권장)
- **구체적으로**: "프레임워크 배우기" → "FastAPI로 RESTful API 구축하기"
- **검증 가능하게**: "이해하기" → "직접 구현할 수 있다"
- **현실적으로**: 예상 기간을 너무 빡빡하게 잡지 않기
- **참조 자료 포함**: 학습에 도움될 링크나 문서 명시

### ❌ Don'ts (지양)
- 너무 광범위한 Topic (예: "프로그래밍 전체")
- 애매한 목표 (예: "잘하기", "많이 배우기")
- 비현실적 기간 (예: "1주일에 전문가 되기")
- 참조 자료 없이 시작

---

## 📞 도움이 필요하신가요?

- VibeLearn AI 방법론 전체: `VibeLearn AI/README.md` 참조
- 빠른 시작 가이드: `VibeLearn AI/GETTING_STARTED.md` 참조
- 문의: solkit70@gmail.com

---

**Template Version**: 1.0
**Created by**: VibeLearn AI Methodology
**Last Updated**: 2025-12-28
**Topic Created**: 2026-09-13 (Live #27 방송 중)
