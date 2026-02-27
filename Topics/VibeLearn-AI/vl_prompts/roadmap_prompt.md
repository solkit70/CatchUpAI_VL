# VibeLearn AI Roadmap 생성 프롬프트 — VibeLearn-AI Topic

**버전**: 2.0
**생성일**: 2026-02-26
**방법론**: VibeLearn AI

---

## [1단계] Topic 정보 (주입됨)

### 기본 정보

**Topic 이름**: `VibeLearn-AI`

**Topic 설명**:
```
VibeLearn AI 학습 방법론 시스템을 깊이 이해하고,
처음 접하는 사람도 바로 시작할 수 있는 교과서 품질 문서를 만들며,
최종적으로 한국어·영어 소개 영상을 제작하여 널리 알리는 프로젝트
```

**학습 목적**:
```
1. VibeLearn AI 시스템의 철학, 구조, 워크플로우를 완전히 이해한다
2. 다른 사람이 바로 쓸 수 있는 고품질 가이드 문서를 만든다
3. KR+EN 소개 영상을 제작하여 시스템을 널리 알린다
```

**예상 학습 기간**: `집중적으로 빠르게 (1-2주)`

---

### 환경 및 사전 지식

**운영 체제**: `Windows 11`

**주요 도구**:
```
- VS Code / Cursor
- Claude Code
- markdown-video 파이프라인 (TTS + Gemini + FFmpeg)
- GitHub
- Python
```

**사전 지식**:
```
필수:
- GitHub 기본 사용법
- Claude Code 사용 가능
- VibeLearn AI를 이미 사용 중 (CatchUpAI_VL 프로젝트)

권장:
- Clearly 소개 영상 제작 경험 (이미 보유)
- markdown-video 파이프라인 경험 (이미 보유)
```

---

### 산출물 및 참조

**학습 목표**:
```
- [ ] VibeLearn AI 핵심 철학과 4단계 워크플로우를 설명할 수 있다
- [ ] topic_starter → roadmap → daily_learning → worklog 사이클을 실행할 수 있다
- [ ] 처음 사용자가 30분 안에 시작할 수 있는 가이드를 만들 수 있다
- [ ] 기존 케이스(Clearly, Remotion)를 케이스 스터디로 문서화할 수 있다
- [ ] markdown-video 파이프라인으로 KR+EN 소개 영상을 제작할 수 있다
```

**참조 자료**:
```
- GitHub: https://github.com/solkit70/VibeLearn-AI.git
- 로컬: templates/, extras/, scripts/, README.md, GETTING_STARTED.md
- 케이스: Topics/Clearly-BRD-PRD/, Topics/Remotion-VideoCreation/
- 영상 파이프라인: Topics/Claude-Skills/temp-claude-obsidian-skills/markdown-video/
```

---

## [2단계] AI에게 요청할 작업

위 Topic 정보를 바탕으로 VibeLearn AI 방법론에 맞는 학습 로드맵을 생성해주세요.
로드맵은 `vl_roadmap/YYYYMMDD_RoadMap_VibeLearn-AI.md`에 저장하세요.
