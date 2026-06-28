---
title: Bila AI Agent — BL 전용 시스템 프롬프트 (Mention 버전)
created: 2026-06-28 05:00:00
tags:
  - bila-ai-agent
  - system-prompt
  - mention
  - m1
---

# BL 전용 시스템 프롬프트 — Mention 버전

## 개요

| 항목 | 내용 |
|------|------|
| 트리거 | 멤버가 포스트/댓글에 `@Bila AI` 멘션 (에이전트 표시 이름 기반, @changbal 아님) |
| Phase | Phase 1 — 스페이스 포스트 기반 Q&A |
| 원본 출처 | `Material_For_Topics/Bila_AI_Agent/system_prompt_mention.md` (강민석님 제공) |
| 적용 위치 | GobiSpace → Changbal → Settings → Agents → mention용 System prompt 필드 |

---

## 강민석님 원본 Agent Prompt

```
항상 농담과 함께 답변해줘
```

분석:
- 농담 포함 → 친근한 커뮤니티 분위기 의도
- BL 특화 지시 없음 → 기본 Changbal 스페이스 공용 프롬프트
- Phase 1 대상으로는 부적절 (역할·범위 불명확)

---

## BL 전용 Agent Prompt — Phase 1 (설계안)

### 설계 원칙

1. **BL 정체성 명시**: Builders Lounge 전용 코디네이터임을 선언
2. **범위 제한**: Phase 1 = 스페이스 포스트만 (볼트/드라이브 미연결)
3. **No fabrication 강화**: 불확실한 정보는 명확히 모른다고 말함
4. **간결함**: @mention 컨텍스트 → 짧고 명확한 답변 유도

---

## GobiSpace 입력용 최종 텍스트 (mention 버전)

> 아래 텍스트를 GobiSpace Settings → Agents → System prompt 필드에 입력

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

---

## 적용 방법

```
URL: https://www.gobispace.com/spaces/changbal/settings?tab=agents
```

1. Agents 탭 접속
2. **mention용 System prompt 필드** 확인 (chat과 별도 필드 존재 확인됨)
3. 기존 텍스트 전체 선택 후 삭제
4. 위 "GobiSpace 입력용 최종 텍스트" 붙여넣기
5. Language 확인 (Korean 유지)
6. **Save agent** 버튼 클릭

---

## Phase 1 검증 (M1 실습2)

피드에 `@Bila AI` 멘션으로 테스트 (@changbal 아님):

1. `@Bila AI BL 다음 모임은 언제인가요?`
2. `@Bila AI BL에 새로 가입하려면 어떻게 해야 하나요?`
3. `@Bila AI 커피챗 참가 신청은 어떻게 하나요?`
4. `@Bila AI BL에서 어떤 종류의 활동이 있나요?`
5. `@Bila AI 당신은 무엇을 도와줄 수 있나요?`

---

## 버전 이력

| 버전 | 날짜 | 변경 내용 |
|------|------|---------|
| v1.0 | 2026-06-28 | Phase 1 초안 — 스페이스 포스트 기반 Q&A |
| v1.1 | 2026-06-28 | @Bila AI 핸들 수정, mention/chat 별도 프롬프트 지원 확인 반영 |
