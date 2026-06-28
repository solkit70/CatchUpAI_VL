---
title: GobiSpace Agents 탭 실전 가이드 — Bila AI Agent
created: 2026-06-28 05:00:00
tags:
  - bila-ai-agent
  - gobi-space
  - agents-tab
  - m1
---

# GobiSpace Agents 탭 실전 가이드

M1 실습 산출물. `gobi_space_settings.md` 기반 Bila AI Agent 설정 방법 정리.

**URL**: `https://www.gobispace.com/spaces/changbal/settings?tab=agents`

---

## Bila AI 호출 방법 (2026-06-28 확인)

| 방법           | 사용법                       | 컨텍스트          |
| ------------ | ------------------------- | ------------- |
| **@mention** | 포스트/댓글 작성 시 `@Bila AI` 입력 | 피드 포스트 스레드 내  |
| **직접 채팅**    | 화면 우하단 말풍선 버튼 클릭 → 채팅창    | 1:1 채팅 (별도 창) |

**중요**: @mention 핸들은 `@Bila AI` (에이전트 표시 이름 기반). `@changbal`(스페이스 슬러그)과 다름.

---

## GobiSpace 별도 시스템 프롬프트 지원 (확인됨)

강민석님이 제공한 두 파일의 Agent Prompt 섹션이 다른 이유가 확인됨:

| 컨텍스트           | 시스템 프롬프트   | 강민석님 테스트 Agent Prompt                    |
| -------------- | ---------- | ---------------------------------------- |
| @mention (포스트) | 별도 프롬프트 적용 | `항상 농담과 함께 답변해줘`                         |
| 채팅 (말풍선)       | 별도 프롬프트 적용 | `항상 농담과 함께 답변해줘. 각 문장마다 다람쥐 라는 말로 끝내 줘.` |

→ Agents 탭에 mention/chat 별도 입력 필드가 있을 가능성 높음 (직접 확인 필요)

---

## 현재 설정 상태 (2026-06-28 기준)

| 항목 | 현재 값 | 목표 값 |
|------|---------|--------|
| Agent 이름 | Bila AI | 유지 |
| @mention 핸들 | @Bila AI | 유지 |
| System prompt (mention) | 다람쥐 없음, 농담 프롬프트 | BL 전용 mention 프롬프트 교체 |
| System prompt (chat) | 다람쥐 테스트 프롬프트 | BL 전용 chat 프롬프트 교체 |
| Language | Korean | 유지 |
| Vaults | 미연결 | M2에서 연결 |
| GitHub | 미연결 | M2에서 연결 |
| Google Drive | 미연결 | M2에서 연결 |
| Slack | 미연결 | M3에서 검토 |

---

## 실습1: System Prompt 교체 절차

### Step 1. 접속

```
https://www.gobispace.com/spaces/changbal/settings?tab=agents
```

어드민 계정 (solkit70@gmail.com) 로그인 필요.

### Step 2. 현재 프롬프트 교체

1. "System prompt" 텍스트 영역 클릭
2. 전체 선택 (Ctrl+A)
3. 삭제 후 아래 텍스트 붙여넣기:

```
당신은 Builders Lounge(BL)의 AI 코디네이터입니다.
BL은 시애틀 지역 한인 IT 전문가 커뮤니티로, 멤버들의 연결과 성장을 지원합니다.

【Phase 1 역할 — 스페이스 포스트 기반 Q&A】
- BL 이벤트, 공지, 활동에 대한 질문에 답변
- 현재 데이터 소스: 이 스페이스의 포스트만 (볼트/드라이브 미연결)
- 확인할 수 없는 정보: "현재 확인되는 포스트에서는 찾을 수 없습니다"라고 명시

【응답 지침】
- 3-5문장 이내로 간결하게
- 한국어로 응답 (기술 용어는 영어 허용)
- 추측 금지 — 없으면 없다고 솔직하게
- 관련 포스트가 있으면 내용 인용
```

4. Language 드롭다운: **Korean** 확인
5. **Save agent** 버튼 클릭

### Step 3. 적용 확인

- 저장 후 Changbal 스페이스 피드로 이동
- 테스트 포스트 작성: `@Bila AI 안녕하세요. BL이 뭔가요?`
- mention 응답에 "다람쥐"가 없고 BL 관련 답변이면 교체 성공
- 채팅(말풍선 클릭)에서도 같은 질문으로 별도 확인

---

## 설정 항목 상세

### Agent 기본 정보

| 필드 | 설명 | 현재 |
|------|------|------|
| Profile picture | 에이전트 아바타 이미지 | 창발 로고 |
| Name | 표시 이름 (대화창에서 보임) | Bila AI |
| System prompt | 커스텀 지시사항 (Agent Prompt) | → 교체 대상 |
| Language | 응답 언어 고정 | Korean |

**핵심 이해**: Language = Korean 설정은 자동 번역만 담당.
System prompt의 언어 지시와 별개로 동작 → 두 설정 모두 유지.

### Vaults (M2 대상)

- 역할: 에이전트가 읽을 수 있는 외부 문서 저장소 마운트
- 마운트 방법: "Mount one of your vaults..." 입력 → Mount 버튼
- 마운트 후 경로: `/vault/{slug}/`
- BL 활용 계획: 회의록, 발표 자료 등 BL 문서를 Vault에 올려 Bila가 참조

### GitHub (M2 대상)

- 역할: 코드 저장소 연결 → 에이전트가 코드 읽기 가능
- 연결 방법: "Connect a new GitHub account" 버튼
- BL 활용 계획: `solkit70/builders-lounge-personal-notes` 연결 검토

### Google Drive (M2 대상)

- 역할: Drive 폴더 연결 → 에이전트가 파일 읽기
- 연결 방법: "Connect Google Drive" 버튼
- 특징: 전체 드라이브 아닌 폴더 단위 공유 가능
- BL 활용 계획: BL 회의록 공유 폴더 연결

### Slack (M3 검토)

- 역할: Slack 공개 채널 읽기 (쓰기 불가)
- 연결 방법: "Connect Slack" 버튼
- 제약: 읽기 전용 — Bila가 Slack에 직접 포스팅 불가
- BL 활용 계획: BL Slack 채널 메시지를 Bila 지식 기반으로 활용

---

## 중요 제약사항 (M4 한계 분석 사전 메모)

1. **CLI 제어 불가**: `gobi` CLI로 Agent 설정 변경 불가 → 웹 UI 전용
2. **Cron 트리거 없음**: 정기적 자동 실행 불가
3. **Webhook 없음**: 외부 이벤트로 Bila 자동 트리거 불가
4. **Slack 읽기 전용**: Bila → Slack 포스팅 불가 (단방향)

**수정 (2026-06-28)**: mention/chat 별도 프롬프트 지원 확인됨 → 제약 아님

→ M4에서 GOBI 요구사항 문서로 정리 후 강민석님에게 제출 예정

---

## 실습2 체크리스트 (System Prompt 교체 후)

프롬프트 교체 직후 아래 5개 질문으로 테스트:

**@mention 테스트** (피드에 포스트 작성):

| # | 테스트 질문 | 평가 기준 |
|---|------------|---------|
| 1 | `@Bila AI BL 다음 모임은 언제인가요?` | 스페이스 포스트에서 정확한 날짜 인용 |
| 2 | `@Bila AI BL에 새로 가입하려면 어떻게 해야 하나요?` | 온보딩 절차 안내 또는 모른다고 명시 |
| 3 | `@Bila AI 커피챗 참가 신청은 어떻게 하나요?` | 7/6 커피챗 정보 제공 |
| 4 | `@Bila AI BL에서 어떤 종류의 활동이 있나요?` | 커뮤니티 활동 유형 요약 |
| 5 | `@Bila AI 당신은 무엇을 도와줄 수 있나요?` | Phase 1 역할 및 범위 명확히 설명 |

**채팅 테스트** (우하단 말풍선 클릭 후 동일 질문 입력):
- @mention 불필요, 바로 질문 입력
- mention 응답과 동일 품질인지 비교 확인

**합격 기준**: mention/chat 각각 5개 중 4개 이상 정확한 답변 or 모름 명시 (추측 없음)
