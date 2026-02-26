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
Topic 이름: [여기에 입력]
```

### Topic 설명
**목적**: 이 Topic이 무엇인지 한두 문장으로 설명

```
설명: [여기에 입력]
```

### 학습 목적
**왜 이것을 배우는가?**

```
학습 목적:
- [목적 1]
- [목적 2]
- [목적 3]
```

### 예상 학습 기간
**현실적으로 예상되는 기간**

```
예상 기간: [X주 또는 Y시간]
```

---

## 🎯 학습 목표

**이 Topic을 완료했을 때 달성하고 싶은 구체적 목표**

```
- [ ] [목표 1: 예 - MCP 서버를 직접 구현할 수 있다]
- [ ] [목표 2: 예 - MCP 클라이언트와 서버 통신 구조를 이해한다]
- [ ] [목표 3: 예 - 실무 프로젝트에 MCP를 적용할 수 있다]
- [ ] [추가 목표...]
```

**권장**: 3-5개의 명확하고 검증 가능한 목표

---

## 🛠️ 학습 환경

### 운영 체제
```
OS: [Windows / macOS / Linux]
버전: [선택 사항]
```

### 주요 도구 및 기술 스택
**이 Topic 학습에 필요한 도구들**

```
- [예: VS Code]
- [예: Python 3.10+]
- [예: Docker Desktop]
- [예: Node.js 18+]
- [기타...]
```

### 사전 지식 (Prerequisites)
**이 Topic을 학습하기 전에 알아야 할 것**

```
필수:
- [예: Python 기본 문법]
- [예: Git 기본 사용법]

권장:
- [예: RESTful API 개념]
- [예: JSON 데이터 형식]
```

---

## 📚 참조 자료 (Optional)

### 공식 문서
```
- [문서 제목]: [URL]
- [문서 제목]: [URL]
```

### 튜토리얼 및 강의
```
- [튜토리얼 제목]: [URL]
- [강의 제목]: [URL]
```

### 관련 GitHub 저장소
```
- [저장소 이름]: [URL]
```

### 추가 학습 자료
**파일, 문서, 동영상 등을 `vl_materials/` 폴더에 저장 가능**

```
vl_materials/ 폴더에 추가할 자료:
- [자료 1 설명]
- [자료 2 설명]
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
- 주당 학습 시간: [X시간]
- 학습 가능 요일: [월, 수, 금 등]
- 1회당 학습 시간: [1-3시간 권장]
```

### 특별히 집중하고 싶은 영역
```
- [예: 실전 프로젝트 경험]
- [예: 트러블슈팅 능력 향상]
- [예: 아키텍처 설계 이해]
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
