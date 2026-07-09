# VibeLearn AI Topic Starter

> 이 파일은 새로운 Topic 학습을 시작할 때 작성하는 템플릿입니다.
>
> **사용 방법**:
> 1. 이 파일을 복사하여 `[TopicName]_topic_starter.md`로 저장
> 2. 아래 항목들을 채워서 작성
> 3. AI에게 이 파일을 전달하여 Topic 폴더 구조 생성 요청
> 4. 생성된 폴더에서 학습 시작!

## 📌 Topic 기본 정보

### Topic 이름

**형식**: 영문, 하이픈 또는 언더스코어 사용 (공백 없음)

```text
Topic 이름: Slack-Builders-Lounge-Automation
```

### Topic 설명

**목적**: 이 Topic이 무엇인지 한두 문장으로 설명

```text
설명: changbal.slack.com의 #club-sg-ai 채널에서 Builders Lounge 관련 Slack 글을 가져와 AI/Initiatives/Builders Lounge/slack/ 아래 Markdown 문서로 자동 정리하는 방법을 연구하고 구현한다.
```

### 학습 목적

**왜 이것을 배우는가?**

```text
학습 목적:
- Slack API의 conversations.history, conversations.replies, users, permalink, OAuth scope 구조를 AI에게 지시할 수 있을 정도로 이해한다.
- 현재 수동으로 진행하는 Slack 글 수집과 Markdown 정리 작업을 자동화한다.
- 기존 Builders Lounge Slack 문서와 호환되는 출력 형식과 증분 동기화 방식을 설계한다.
- GitHub 공개 공유 전에 민감 정보와 비공개 맥락을 점검하는 review/publish 흐름을 만든다.
- 최종적으로 환경 변수 기반 토큰, 채널 ID, 상태 파일, Markdown 생성기를 포함한 로컬 실행 가능한 자동화 스크립트를 만든다.
```

### 예상 학습 기간

**현실적으로 예상되는 기간**

```text
예상 기간: 1주 또는 8-10시간 집중 연구/개발
```

## 🎯 학습 목표

**이 Topic을 완료했을 때 달성하고 싶은 구체적 목표**

- [ ] Slack API 접근 방식, 필요한 권한, rate limit, workspace export 대안을 정리한다.
- [ ] `#club-sg-ai` 채널의 메시지, 스레드, 작성자, permalink를 가져오는 prototype을 만든다.
- [ ] 기존 `AI/Initiatives/Builders Lounge/slack/` 문서와 호환되는 Markdown schema를 정의한다.
- [ ] 마지막 수집 시각을 저장하는 증분 동기화 구조를 만든다.
- [ ] 공개 GitHub 공유 전 검토와 redaction 기준을 자동화 흐름에 포함한다.
- [ ] 실제 로컬 실행 가능한 Slack-to-Markdown sync 스크립트를 만든다.

## 🛠️ 학습 환경

### 운영 체제

```text
OS: Windows 11 / Obsidian Vault
버전: 2026-07-05 기준 로컬 Vault
```

### 주요 도구 및 기술 스택

**이 Topic 학습에 필요한 도구들**

```text
- Codex
- Obsidian
- VibeLearn AI
- PowerShell
- Python
- Slack Web API
- Markdown
- JSON
- Git / GitHub
- Windows Task Scheduler 또는 수동 실행 스크립트
```

### 사전 지식 (Prerequisites)

**이 Topic을 학습하기 전에 알아야 할 것**

```text
필수:
- Builders Lounge 문서 구조
- Markdown frontmatter와 상대 링크 기본
- 환경 변수로 secret을 관리하는 방법
- Slack workspace/channel 개념

권장:
- OAuth scope와 token permission 기본
- REST API pagination
- Python requests/httpx 기반 API 호출
- GitHub 공개 문서에 포함하면 안 되는 정보 구분
```

## 📚 참조 자료 (Optional)

### 공식 문서

```text
- Slack conversations.history: https://docs.slack.dev/reference/methods/conversations.history/
- Slack conversations.replies: https://docs.slack.dev/reference/methods/conversations.replies/
- Slack scopes: https://docs.slack.dev/reference/scopes/
- Slack workspace export guide: https://slack.com/help/articles/201658943-Export-your-workspace-data
```

### 튜토리얼 및 강의

```text
- 해당 없음. 공식 Slack API 문서와 로컬 Vault의 기존 Slack 정리 문서를 기준으로 진행한다.
```

### 관련 GitHub 저장소

```text
- Builders Lounge 공개 노트 저장소는 기존 GitHub 공유 흐름을 따른다.
```

### 추가 학습 자료

**파일, 문서, 동영상 등을 `vl_materials/` 폴더에 저장 가능**

```text
vl_materials/ 폴더에 추가할 자료:
- Slack API response sample fixture
- redacted message sample
- Markdown output sample
- sync state sample
```

## 🎓 학습 접근 방식 (Optional)

### 선호하는 학습 스타일

- [ ] 이론 먼저, 실습 나중
- [x] 실습 중심, 필요한 이론만 (권장)
- [ ] 이론과 실습 병행

### 시간 투자 계획

```text
- 주당 학습 시간: 8-10시간
- 학습 가능 요일: 이번 주 일정 안에서 짧은 daily session으로 진행
- 1회당 학습 시간: 1-2시간
```

### 특별히 집중하고 싶은 영역

```text
- Slack API 권한과 rate limit을 정확히 이해하기
- AI에게 개발 지시를 줄 수 있을 정도의 기술 구조 파악
- 기존 수동 Slack 정리 문서와 호환되는 Markdown 변환
- 공개 공유 전 privacy/review workflow
- 실제 로컬 자동화 스크립트 완성
```

## 🚀 다음 단계

### 이 파일 작성 완료 후:

1. **Topic 폴더 생성 요청**
   - AI에게 이 파일을 전달
   - "이 Topic Starter를 기반으로 VibeLearn AI Topic 폴더 구조를 생성해주세요"

2. **Roadmap 생성**
   - 생성된 Topic 폴더에서 `vl_prompts/roadmap_prompt.md` 사용
   - AI에게 Roadmap 생성 요청

3. **학습 시작**
   - 생성된 Roadmap을 기반으로 Module 1부터 시작
   - 각 학습 세션은 `vl_prompts/daily_learning_prompt.md` 사용

## 📝 메모

```text
이 Topic은 단순 연구가 아니라 실제 자동화 개발까지 포함한다. 단, Slack token과 workspace permission은 사용자가 별도로 준비해야 하므로, 개발 산출물은 token이 없을 때도 fixture/dry-run으로 검증할 수 있게 만든다.
```
