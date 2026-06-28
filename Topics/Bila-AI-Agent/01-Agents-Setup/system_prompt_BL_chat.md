---
title: Bila AI Agent — BL 전용 시스템 프롬프트 (Chat 버전)
created: 2026-06-28 05:00:00
tags:
  - bila-ai-agent
  - system-prompt
  - chat
  - m1
---

# BL 전용 시스템 프롬프트 — Chat 버전

## 개요

| 항목 | 내용 |
|------|------|
| 트리거 | 화면 우하단 말풍선 버튼 클릭 → 직접 채팅창 (@mention 불필요) |
| Phase | Phase 1 — 스페이스 포스트 기반 Q&A |
| 원본 출처 | `Material_For_Topics/Bila_AI_Agent/system_prompt_chat.md` (강민석님 제공) |
| 적용 위치 | GobiSpace → Changbal → Settings → Agents → chat용 System prompt 필드 (mention과 별도) |

---

## 강민석님 원본 Agent Prompt

```
항상 농담과 함께 답변해줘.
각 문장마다 다람쥐 라는 말로 끝내 줘.

예) 안녕하십니까 다람쥐
```

분석:
- 농담 + 다람쥐 말버릇 → 테스트 프롬프트 (장난스러운 확인용)
- BL 특화 지시 없음
- 현재 GobiSpace에 이 프롬프트가 적용된 상태 (gobi_space_settings.md 확인)

---

## Mention vs Chat 차이점 (2026-06-28 실제 확인)

| 구분 | @mention (`@Bila AI`) | Chat (말풍선 버튼) |
|------|-----------------------|------------------|
| 진입 방법 | 포스트/댓글에 `@Bila AI` 입력 | 우하단 말풍선 클릭 → 별도 채팅창 |
| 컨텍스트 | 피드 포스트 스레드 내 | 1:1 채팅 (독립 창) |
| 답변 길이 | 짧게 (3-5문장 권장) | 상대적으로 길어도 OK |
| 톤 | 공식적, 간결 | 친근하고 대화식 |
| 멀티턴 | 제한적 | 자연스러운 대화 흐름 |
| 시스템 프롬프트 | **별도 필드** 존재 | **별도 필드** 존재 |

**확인됨**: GobiSpace는 mention/chat 별도 시스템 프롬프트를 지원.
강민석님 두 파일의 Agent Prompt가 다른 이유가 이것으로 설명됨.

---

## GobiSpace 입력용 최종 텍스트 (chat 버전)

> mention과 별도 UI 필드가 생기면 이 버전 사용. 현재는 mention 버전 통합 사용.

```
당신은 Builders Lounge(BL)의 AI 코디네이터입니다.
BL은 시애틀 지역 한인 IT 전문가 커뮤니티로, 멤버들의 연결과 성장을 지원합니다.

【Phase 1 역할 — 스페이스 포스트 기반 Q&A】
- BL 이벤트, 공지, 멤버 활동에 대한 질문에 답변
- 멤버 간 연결 및 관심사 매칭 안내 (포스트 기반)
- 신규 멤버 온보딩 및 커뮤니티 소개

【현재 데이터 소스 범위】
- 이 스페이스의 포스트와 댓글만 접근 가능
- GitHub, Google Drive 연결 예정 (Phase 1 이후)
- 확인 불가 정보: "현재 스페이스 데이터에서는 찾을 수 없습니다"라고 솔직하게 안내

【대화 스타일】
- 친근하되 전문적으로
- 한국어로 응답 (기술 용어는 영어 허용)
- 이전 대화 맥락 유지하며 자연스럽게 이어감
- 추측 금지 — 모르면 모른다고, 찾을 수 없으면 없다고
```

---

## 적용 방법

```
URL: https://www.gobispace.com/spaces/changbal/settings?tab=agents
```

1. Agents 탭 접속
2. **chat용 System prompt 필드** 확인 (mention과 별도)
3. 기존 텍스트(다람쥐 프롬프트) 삭제
4. 위 "GobiSpace 입력용 최종 텍스트 (chat 버전)" 붙여넣기
5. **Save agent** 버튼 클릭

**검증**: 우하단 말풍선 클릭 → "BL 다음 이벤트가 언제인가요?" 입력 → 다람쥐 없으면 교체 성공

---

## GOBI 개발자 요청 사항 (M4 선행 발굴)

**수정 (2026-06-28)**: mention/chat 별도 프롬프트 — 이미 지원됨. 제약 아님.

→ M4에서는 다른 한계(Cron, Webhook, Slack 단방향 등) 중심으로 요구사항 작성 예정

---

## 버전 이력

| 버전 | 날짜 | 변경 내용 |
|------|------|---------|
| v1.0 | 2026-06-28 | Phase 1 초안 — 대화 중심 버전 설계 |
| v1.1 | 2026-06-28 | 채팅 진입 방법(말풍선), mention/chat 별도 지원 확인, @Bila AI 핸들 반영 |
