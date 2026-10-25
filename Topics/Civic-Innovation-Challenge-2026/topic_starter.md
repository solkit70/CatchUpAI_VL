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
Topic 이름: Civic-Innovation-Challenge-2026
```

### Topic 설명
**목적**: 이 Topic이 무엇인지 한두 문장으로 설명

```
설명: Exchange Northwest(Bellevue 시 · Bellevue College · King County IT · 워싱턴주 WaTech)의
「제2차 Civic Innovation Challenge」를 누구나 이해할 수 있게 정리해 GitHub 에 공개하고,
그 문서를 근거로 Remotion 한국어 · 영어 영상을 만들어 Catch Up AI 채널에서 알린다.
1차(2025, Bellevue) 결과를 토대로 「선정에 유리하게 준비하는 법」과, 워싱턴주 한인상공회의소
스타트업지원팀이 도울 수 있는 것과 연락 방법을 함께 안내한다. 신청 마감은 2026-11-13(금) 오후 5시(PT).
```

### 학습 목적
**왜 이것을 배우는가?**

```
학습 목적:
- (첫째 목적) 이 사업에 참여하고 싶고 자격이 되는 개인 · 스타트업 · 기업이 더 많이 알 수 있도록, 무엇인지 · 누가 지원할 수 있는지 · 어떻게 지원하는지를 알기 쉽게 정리해 정보를 제공한다
- 1차(2025) 선정 4팀 · 평가 기준 · 신청서 질문을 분석해, 선정되는 데 더 유리하게 준비하려면 무엇을 어떻게 준비해야 하는지 가이드한다
- 워싱턴주 한인상공회의소 스타트업지원팀이 지원하려고 노력하고 있다는 것, 도울 수 있는 것, 필요하면 연락하라는 안내를 넣는다 (단, 게시 주체는 Catch Up AI 이며 상공회의소 자격으로 올리는 것이 아니다)
- 1차 산출물(GitHub 문서)을 근거로 Remotion 한국어판 · 영어판 홍보 영상을 만든다
```

### 예상 학습 기간
**현실적으로 예상되는 기간**

```
예상 기간: 약 1.5주 (2026-10-25 ~ 11/4 목표) — 신청 마감(11/13) 전에 문서와 영상을 공개해야 효과가 있다
```

---

## 🎯 학습 목표

**이 Topic을 완료했을 때 달성하고 싶은 구체적 목표**

```
- [ ] 공식 공고 4종 · 1차 자료를 중심으로 관련 보도 · 기관 발표 · 선정 기업 자료 · 설명회 내용까지 근거로 삼아(출처를 문장마다 표시하고, 공식 자료와 다르면 공식 자료를 따른다), 「무엇인지 · 지원 자격 · 일정 · 사용 사례 8개 · 신청 방법」을 처음 보는 사람이 순서대로 읽고 이해할 수 있는 한국어 · 영어 문서로 GitHub 에 공개한다
- [ ] 1차 선정 4팀 · 평가 기준 9항목 · 신청서 16문항을 근거로 「선정에 유리한 준비 가이드」(준비 체크리스트 · 문항별 작성 요령 · 2분 피치 영상 요령)를 만든다
- [ ] 10/26 Tukwila 설명회에서 확인한 내용(미국 법인 · 거주지 요건, 보험 수준, 개념 단계 선정 가능성, 지역 단체 지지 서한 반영 여부)으로 문서를 갱신한다
- [ ] 워싱턴주 한인상공회의소 스타트업지원팀의 지원 내용 · 연락 방법 안내를 임원 검토 결과에 맞춰 넣는다
- [ ] GitHub 문서를 근거로 Remotion 한국어판 · 영어판 영상을 만들어 마감 전에 공개할 수 있게 한다
```

**권장**: 3-5개의 명확하고 검증 가능한 목표

---

## 🛠️ 학습 환경

### 운영 체제
```
OS: Windows 11
버전: 박창수 실습 PC — i7-1355U · 16GB RAM · GPU 없음 (렌더링 · TTS 는 가능한 가벼운 방식)
```

### 주요 도구 및 기술 스택
**이 Topic 학습에 필요한 도구들**

```
- VS Code + Claude Code (문서 정리 · 분석)
- Python 3.13 (공고 PDF 텍스트 추출 · 링크 검사)
- Remotion (AI/RemotionStudio — 기존 영상 제작 환경) + remotion-video 스킬
- edge-tts (초벌) · Qwen3-TTS (한국어 최종 음성), 영어 음성
- GitHub — CatchUpAI_VL 공개 레포 (1차 정보 제공 창구)
- YouTube (Catch Up AI 채널)
```

### 사전 지식 (Prerequisites)
**이 Topic을 학습하기 전에 알아야 할 것**

```
필수:
- 영어 공고를 읽을 수 있는 정도의 이해 (또는 AI 번역으로 확인하는 습관)
- Remotion 영상 제작 흐름 경험 (슬라이드 플랜 → TTS → 컴포지션 → 렌더링)

권장:
- 공공기관 파일럿 · 조달(vendor 등록 · W-9 · 보험 증명서) 기본 개념
- 워싱턴주 한인 사업자 · 스타트업 커뮤니티 맥락 (상공회의소 · Builders Lounge · 창발)
```

---

## 📚 참조 자료 (Optional)

### 공식 문서
```
- Exchange Northwest — Civic Innovation Challenge (2차 공고 · 신청서): https://exchangenw.org/programs
- 2차 신청서: https://exchangenw.org/civic-innovation-challenge-application
- Bellevue 시 — 1차 Civic Innovation Challenge: https://bellevuewa.gov/city-government/departments/ITD/innovation-programs/civic-innovation-challenge
- Bellevue 시 — 1차 선정 4팀: https://bellevuewa.gov/city-government/departments/ITD/innovation-programs/civic-innovation-challenge/civic-challenge-participants
- Bellevue 시 — 1차 일정 · 마일스톤: https://bellevuewa.gov/city-government/departments/ITD/innovation-programs/accomplishments
```

### 튜토리얼 및 강의
```
- 10/26(월) 18:00~20:00 Tukwila Community Center 대면 질의응답 (박창수 참석): https://www.eventbrite.com/e/the-exchange-nw-civic-innovation-challenge-working-session-tickets-2003631120618
- 11/4(수) 13:00~15:00 온라인 10분 상담 (신청제) — 공고 Overview 참조
```

### 관련 GitHub 저장소
```
- CatchUpAI_VL: https://github.com/solkit70/CatchUpAI_VL
```

### 추가 학습 자료
**파일, 문서, 동영상 등을 `vl_materials/` 폴더에 저장 가능**

```
vl_materials/ 폴더에 추가할 자료:
- 공식 공고 PDF 4종 (Overview · Use Cases · Submission Process · FAQ) — 공개 문서
- 1차(2025) Bellevue 공고 PDF — 공개 문서
- 볼트 준비 자료(공개 레포 제외): Topics/Materials_For_Topics/Civic-Innovation-Challenge-2026/ — 사실표(한 · 영), 1차 정리, 스타트업지원팀 지원 안내 초안
- ⚠️ 공개 레포에 넣지 않는 것: 상공회의소 임원방 대화 · 회장님 메일 · 임원 이름, 임원 검토 전의 지원 안내 확정본
- ⚠️ 공개 영상 · 문서에는 박창수 이름 대신 Catch Up AI / Builders Lounge 를 쓴다
```

---

## 🎓 학습 접근 방식 (Optional)

### 선호하는 학습 스타일
```
- [ ] 이론 먼저, 실습 나중
- [x] 실습 중심, 필요한 이론만 (권장) — 이 Topic 의 「실습」은 공고 분석 · 문서 작성 · 영상 제작
- [ ] 이론과 실습 병행
```

### 시간 투자 계획
```
- 주당 학습 시간: 6~8시간 (마감 때문에 짧고 집중적으로)
- 학습 가능 요일: 일요일 라이브 방송 포함 주중 틈틈이
- 1회당 학습 시간: 1-3시간
```

### 특별히 집중하고 싶은 영역
```
- GitHub 문서만 순서대로 읽어도 「나도 지원할 수 있나, 무엇을 준비하나」가 판단되는 구성
- 1차 결과에 근거한 실질적인 선정 준비 가이드 (추측은 추측이라고 표시)
- 근거의 폭은 넓게, 표시는 분명하게 — ① 공식 공고 · 기관 웹페이지 ② 시 · 카운티 · 주 정부 보도자료 ③ 언론 보도 · 선정 기업 발표 · 행사 페이지 ④ 설명회 현장 확인 순으로 무게를 두고, 출처를 적으며, 서로 다르면 공식 자료를 따른다
- 한국어 · 영어 두 언어로 같은 내용 (한국어 문서를 고치면 영어 짝도 같이 맞춘다)
- 마감 전에 영상까지 공개하는 일정 관리
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
