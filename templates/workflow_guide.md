# VibeLearn AI 워크플로우 가이드

**버전**: 1.0
**생성일**: 2026-01-25
**방법론**: VibeLearn AI

---

## 📌 개요

이 가이드는 VibeLearn AI 학습 방법론을 **어떤 AI 도구**에서든 사용할 수 있도록 워크플로우별 프롬프트 사용법을 안내합니다.

**지원 AI 도구**:
- ChatGPT (OpenAI)
- Claude (Anthropic)
- Gemini (Google)
- Copilot (Microsoft)
- 기타 LLM 기반 AI 도구

---

## 🚀 전체 워크플로우

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  1. Topic 시작   │ ──▶ │  2. Roadmap 생성 │ ──▶ │  3. 일일 학습    │
│  topic_starter  │     │  roadmap_prompt │     │  daily_learning │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        ▼                       ▼                       ▼
   topic_info.md         RoadMap_{Topic}.md      WorkLog_{Date}.md
```

---

## 📋 단계별 가이드

---

### 1단계: 새 Topic 시작

**사용 시점**: 새로운 기술/프레임워크/개념 학습을 시작할 때

#### 1.1 AI에게 보낼 프롬프트

```
VibeLearn AI(VibeLearn AI) 방법론으로 새로운 학습 Topic을 시작하려고 합니다.

아래 정보를 바탕으로:
1. Topic 폴더 구조를 만들어주세요
2. topic_info.md 파일 작성을 도와주세요

## Topic 정보
- Topic 이름: [예: Docker-Fundamentals]
- 설명: [예: Docker 컨테이너 기술의 기본 개념부터 실전 활용까지]
- 학습 목적: [예: 개발 환경 컨테이너화로 생산성 향상]
- 예상 기간: [예: 2주 (주당 5시간)]
- 학습 목표:
  - [예: Docker 이미지와 컨테이너 개념을 이해한다]
  - [예: Dockerfile을 작성하여 커스텀 이미지를 만들 수 있다]
  - [예: docker-compose로 멀티 컨테이너 환경을 구성할 수 있다]

## 생성할 폴더 구조
Topics/{TopicName}/
├── topic_info.md           # Topic 기본 정보
├── vl_prompts/             # 프롬프트 템플릿
├── vl_roadmap/             # 학습 로드맵
├── vl_worklog/             # 학습 일지
└── vl_materials/           # 참조 자료
```

#### 1.2 수동으로 폴더 생성 (선택)

AI가 직접 폴더를 생성하지 못하는 경우:

**Windows (PowerShell)**:
```powershell
$topic = "Docker-Fundamentals"
mkdir "Topics/$topic/vl_prompts", "Topics/$topic/vl_roadmap", "Topics/$topic/vl_worklog", "Topics/$topic/vl_materials" -Force
```

**macOS/Linux (Bash)**:
```bash
topic="Docker-Fundamentals"
mkdir -p "Topics/$topic"/{vl_prompts,vl_roadmap,vl_worklog,vl_materials}
```

#### 1.3 다음 단계

- [ ] topic_info.md 작성 완료
- [ ] 2단계: Roadmap 생성으로 진행

---

### 2단계: Roadmap 생성

**사용 시점**: topic_info.md 작성 완료 후

#### 2.1 AI에게 보낼 프롬프트

```
VibeLearn AI 방법론에 따라 학습 Roadmap을 생성해주세요.

## Topic 정보
[topic_info.md 내용을 여기에 붙여넣기]

## Roadmap 생성 요청
아래 VibeLearn AI 표준에 맞춰 Roadmap을 생성해주세요:

### 필수 포함 항목 (모듈별)
1. 모듈 기본 정보 (번호, 제목, 예상 시간)
2. 학습 목표 (3-5개)
3. 핵심 개념 (이론 20-30%)
4. 실습 과제 (실습 70-80%)
5. 예상 산출물
6. Definition of Done
7. 자기 평가 체크리스트
8. 시간 배분
9. 참조 자료

### 모듈 구성 원칙
- 첫 모듈은 환경 설정 + 빠른 성공 경험
- 각 모듈은 1-2일 완료 가능한 분량
- 마지막 모듈은 종합 프로젝트

### 출력 형식
마크다운 형식으로 출력해주세요.
파일명: YYYYMMDD_RoadMap_{TopicName}.md
```

#### 2.2 상세 프롬프트 사용 (권장)

더 정교한 Roadmap이 필요하면 `templates/roadmap_prompt_template.md` 파일 전체를 사용하세요.

#### 2.3 Roadmap 저장

생성된 Roadmap을 다음 위치에 저장:
```
Topics/{TopicName}/vl_roadmap/YYYYMMDD_RoadMap_{TopicName}.md
```

#### 2.4 다음 단계

- [ ] Roadmap 검토 및 저장 완료
- [ ] 3단계: 일일 학습으로 진행

---

### 3단계: 일일 학습 시작

**사용 시점**: 매일 학습 세션 시작 시

#### 3.1 AI에게 보낼 프롬프트

```
VibeLearn AI 방법론에 따라 오늘의 학습을 시작합니다.

## 현재 상황
- Topic: [예: Docker-Fundamentals]
- 현재 모듈: [예: M2 - Dockerfile 작성]
- 가용 시간: [예: 3시간]

## Roadmap
[Roadmap 파일 내용 또는 현재 모듈 부분만 붙여넣기]

## 이전 WorkLog (있으면)
[가장 최근 WorkLog 내용 붙여넣기]

## 요청
1. 오늘의 학습 계획을 수립해주세요
2. 현재 모듈의 어디서부터 시작해야 하는지 알려주세요
3. 미완료 작업이 있으면 먼저 처리하도록 안내해주세요
```

#### 3.2 상세 프롬프트 사용 (권장)

더 체계적인 학습 세션이 필요하면 `templates/daily_learning_prompt.md` 파일 전체를 사용하세요.

#### 3.3 학습 중 WorkLog 작성

학습하면서 실시간으로 WorkLog 작성:
```
Topics/{TopicName}/vl_worklog/YYYYMMDD_M{X}_{TopicName}.md
```

**WorkLog 필수 항목**:
- 오늘 완료한 작업
- 발생한 문제 및 해결 방법
- 학습 인사이트
- 내일 할 일 (Tomorrow's focus)

---

## 📁 폴더 구조 참조

### 전체 구조

```
VibeLearn-AI/
├── README.md                        # 방법론 설명
├── GETTING_STARTED.md               # 빠른 시작 가이드
├── templates/                       # 프롬프트 템플릿
│   ├── topic_starter.md             # Topic 시작 템플릿
│   ├── roadmap_prompt_template.md   # Roadmap 생성 프롬프트
│   ├── daily_learning_prompt.md     # 일일 학습 프롬프트
│   └── workflow_guide.md            # 이 파일
└── Topics/                          # 학습 Topic들
    └── {TopicName}/
        ├── topic_info.md
        ├── vl_prompts/
        ├── vl_roadmap/
        │   └── YYYYMMDD_RoadMap_{TopicName}.md
        ├── vl_worklog/
        │   └── YYYYMMDD_M{X}_{TopicName}.md
        └── vl_materials/
```

### vl_ 접두사 규칙

| 폴더 | 용도 |
|------|------|
| `vl_prompts/` | Topic별 프롬프트 템플릿 |
| `vl_roadmap/` | 학습 로드맵 |
| `vl_worklog/` | 학습 일지 (WorkLog) |
| `vl_materials/` | 참조 자료 |

---

## 🔄 회고 (Retrospective)

### Daily Retrospective (매일 5-10분)

학습 종료 시 WorkLog에 추가:

```markdown
## Daily Retrospective

### 오늘 배운 것 (What I Learned)
- [핵심 내용 1]
- [핵심 내용 2]

### 잘한 점 (What Went Well)
- [성공 경험]

### 개선할 점 (What Could Be Better)
- [개선 사항]

### Tomorrow's Focus
- [내일 할 일 1]
- [내일 할 일 2]
```

### Module Retrospective (모듈 완료 시 15-20분)

```markdown
## Module Retrospective - M{X}

### 학습 목표 달성도
- [ ] 목표 1: [달성/미달성]
- [ ] 목표 2: [달성/미달성]

### 핵심 인사이트
1. [인사이트 1]
2. [인사이트 2]

### 다음 모듈 준비
- [준비 사항]
```

### Topic Retrospective (Topic 완료 시 30-60분)

```markdown
## Topic Retrospective - {TopicName}

### 전체 학습 목표 달성도
- [ ] 목표 1: [달성/미달성]

### 가장 가치 있었던 학습
- [내용]

### 실무 적용 계획
- [계획]

### 방법론 개선 제안
- [제안]
```

---

## 💡 팁 & 모범 사례

### Tip 1: Topic 이름 짓기

**좋은 예시**:
- `Docker-Fundamentals` (기술-난이도)
- `React-Hooks` (기술-특정 주제)
- `ML-Basics` (약어-난이도)

**피해야 할 예시**:
- `Docker` (너무 광범위)
- `docker advanced` (공백 사용)

### Tip 2: 학습 목표 작성

**좋은 예시**:
- "Dockerfile을 작성하여 커스텀 이미지를 만들 수 있다"
- "docker-compose.yml로 3개 이상의 서비스를 연동할 수 있다"

**피해야 할 예시**:
- "Docker를 이해한다" (검증 불가)
- "Docker 전문가가 된다" (측정 불가)

### Tip 3: WorkLog 실시간 작성

- 학습 **중에** 즉시 기록
- "공부함" (X) → "Pandas DataFrame 5개 예제 실습 완료" (O)
- 문제 해결 과정을 상세히 기록

### Tip 4: 실습 비율 유지

- **이론 20-30%** : 개념 이해, 문서 읽기
- **실습 70-80%** : 코드 작성, 프로젝트 진행

---

## 📞 도움말

### 더 자세한 정보

- **방법론 전체 설명**: `README.md`
- **빠른 시작 가이드**: `GETTING_STARTED.md`
- **상세 템플릿**: `templates/` 폴더

### 문의

- 이메일: solkit70@gmail.com
- GitHub: [VibeLearn-AI Repository]

---

**Template Version**: 1.0
**Created by**: VibeLearn AI Methodology
**Last Updated**: 2026-01-25
