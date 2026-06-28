# VibeLearn AI Roadmap 생성 프롬프트

**버전**: 2.0
**생성일**: 2026-06-28
**방법론**: VibeLearn AI

---

## 📌 사용 방법

이 프롬프트는 `topic_starter.md`에서 입력한 Topic 정보를 바탕으로 학습 로드맵을 자동 생성합니다.

---

## [1단계] Topic 정보 (주입됨)

### 기본 정보

**Topic 이름**: `Bila-AI-Agent`

**Topic 설명**:
```
GobiSpace Changbal 스페이스에서 운영할 Bila AI Agent를 단계적으로 구축하는 실전 프로젝트.
Phase 1 (기록 기반 Q&A) 구현 후 현재 플랫폼 한계를 파악해 GOBI 개발자 요구사항을 도출하는 것이 핵심 목표.
학습보다는 실제 구현 + 실험이 중심.
```

**학습 목적**:
```
- Bila AI Agent Phase 1 (Q&A) 실제 구현 완료
- GobiSpace Agents 설정 마스터 (시스템 프롬프트 설계 + 데이터 소스 연결)
- 현재 플랫폼 한계 파악 → GOBI 개발자 요구사항 문서 작성 및 제출
- Vibe Guiding 프로젝트의 첫 번째 실전 적용 사례 완성
```

**예상 학습 기간**: `2026년 7월 ~ 8월 (주당 2-3시간, 약 4-8주)`

---

### 환경 및 사전 지식

**운영 체제**: `Windows 11`

**주요 도구 및 기술 스택**:
```
- GobiSpace 웹 UI (changbal 스페이스 어드민 권한 보유)
- gobi CLI v2.0.35
- VS Code + Claude Code
- GitHub (solkit70/builders-lounge-personal-notes)
- Google Drive (BL 회의록 폴더)
```

**사전 지식**:
```
필수:
- GobiSpace 기본 사용법 + Changbal 스페이스 어드민 권한 (완료)
- Bila 원본 시스템 프롬프트 확보 (system_prompt_mention.md, system_prompt_chat.md)

권장:
- AI Agent 설계 개념 (시스템 프롬프트 역할)
- GitHub 기본 사용법
```

---

### 산출물 및 참조

**학습 목표** (달성하고 싶은 것):
```
- [ ] Bila AI Agent용 시스템 프롬프트(@mention/채팅 두 버전)를 직접 설계하고 적용할 수 있다
- [ ] GobiSpace Agents 탭의 모든 연결 기능(GitHub, Google Drive, Vault, Slack)을 사용할 수 있다
- [ ] Phase 1 Q&A가 실제 BL 멤버 질문 5개에 정확히 답하는 수준에 도달한다
- [ ] Phase 2, 3 구현을 위한 GOBI 개발자 요구사항 문서를 완성하고 강민석님에게 제출할 수 있다
```

**참조 자료**:
```
- system_prompt_mention.md — @mention 트리거 시스템 프롬프트 원본
- system_prompt_chat.md — 채팅 대화 시스템 프롬프트 원본
- gobi_space_settings.md — GobiSpace Settings 탭 전체 기능 가이드
- bila_agent_project_plan.md — 전체 프로젝트 플랜 (3단계 구현 로드맵)
- CMDS x GOBI Cohort AI — 유사 구현 사례 레퍼런스
```

**vl_materials/ 폴더**:
```
실제 파일 위치: Ingest/CatchUpAI_VL/Topics/Material_For_Topics/Bila_AI_Agent/
- system_prompt_mention.md
- system_prompt_chat.md
- gobi_space_settings.md
- bila_agent_project_plan.md
```

---

## [2단계] AI에게 요청할 작업

위에 주입된 Topic 정보를 바탕으로 **VibeLearn AI 방법론**에 맞는 학습 로드맵을 생성해주세요.

### 🔍 STEP 1: 학습 기간 적정성 검토 (필수)

(이 Topic의 경우 bila_agent_project_plan.md에 4개 모듈이 이미 설계되어 있어 기간 분석 후 로드맵 바로 생성 가능)

### 🗺️ STEP 2: 로드맵 생성 요구사항

프로젝트 플랜 Section 6에 정의된 4개 모듈 구성을 기반으로 생성:

| 모듈 | 제목 | 핵심 산출물 |
|------|------|-----------|
| M1 | GobiSpace Agents 설정 마스터 | 완성된 시스템 프롬프트 (Bila용) |
| M2 | 데이터 소스 연결 & Phase 1 구현 | GitHub + Google Drive 연결 완료, Q&A 검증 |
| M3 | 채널 구조 & 어드민 워크플로우 | 어드민 전용 채널, 수동 코디네이터 흐름 |
| M4 | 한계 분석 & GOBI 요구사항 | Requirements 문서, GOBI 팀 제출 |

---

## [3단계] 출력 형식

`vl_roadmap/20260628_RoadMap_Bila-AI-Agent.md`에 저장
