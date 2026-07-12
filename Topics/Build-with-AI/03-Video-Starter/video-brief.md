---
title: "Build with AI Video Brief"
created: 2026-07-05 07:55:23
tags:
  - build-with-ai
  - video-brief
  - catch-up-ai
---

## Status

이 문서는 승인 전 선행 초안이다. M3는 M2 angle이 정식 승인된 뒤 별도 오늘 학습 계획을 사용자에게 제시하고 승인받아야 진행할 수 있다. 아래 DoD 체크는 초안 기준 완료를 뜻하며 Roadmap 정식 완료율에는 반영하지 않는다.

## Working Title

AI로 데모는 만들었는데, 왜 서비스는 안 될까?

## One-Line Thesis

데모는 AI가 만들 수 있지만, 서비스는 문제·데이터·검증·운영 기준이 있어야 한다.

## Video Promise

이 영상은 Build with AI 자료를 바탕으로 비개발자 빌더가 AI 도구로 데모를 만든 뒤 실제 서비스 단계에서 막히는 이유를 설명한다. 시청자는 코딩보다 먼저 정리해야 할 문제 정의, 데이터, 워크플로, 검증, 운영 기준을 이해하게 된다.

## Opening Script Starter

요즘은 AI 도구를 쓰면 생각보다 빨리 데모를 만들 수 있습니다. Cursor나 Claude Code, Codex, Lovable 같은 도구를 쓰면, 예전에는 개발팀이 필요했던 화면이나 자동화도 혼자서 꽤 빠르게 만들어볼 수 있습니다.

그런데 이상하게도, 그 데모가 실제 사용자가 매일 쓰는 서비스가 되는 경우는 훨씬 적습니다. 친구에게 보여주면 "와, 진짜 만들었네"라는 말은 듣지만, 실제 고객이 들어오고, 데이터가 쌓이고, 비용과 오류와 예외 상황을 견디는 서비스까지 가는 경우는 많지 않습니다.

오늘은 송재희님의 Build with AI 자료를 바탕으로, 이 사이에 있는 벽이 정확히 무엇인지 보려고 합니다. 결론부터 말하면, 병목은 코딩 실력만이 아닙니다. 진짜 병목은 문제를 정확히 정의하고, 데이터를 준비하고, 검증 기준과 운영 책임을 설계하는 능력입니다.

## Key Explanation Blocks

| Block | Message | Source Connection |
|---|---|---|
| 1. Demo is easy to show | 데모는 통제된 입력, 제한된 사용자, 준비된 시나리오를 전제로 한다. 그래서 화면상으로는 빠르게 "되는 것처럼" 보일 수 있다. | Build with AI Part 10 |
| 2. Service must survive reality | 서비스는 실제 사용자 데이터, 예측 불가능한 입력, 비용, 지연, 오류, 신뢰 문제를 견뎌야 한다. | Build with AI Part 10, Part 11 |
| 3. Coding is not the first bottleneck | AI가 코드를 빨리 만들어줄수록 병목은 "무엇을 만들 것인가"를 정확히 정의하는 능력으로 이동한다. | Build with AI Part 5, Part 6 |
| 4. Data and context decide quality | 모델보다 데이터와 context 품질이 결과를 좌우한다. 지저분하고 맥락 없는 데이터는 그럴듯하지만 불안정한 결과를 만든다. | Build with AI Part 4 |
| 5. Community can help validation | 혼자 만든 데모는 커뮤니티와 Agent를 통해 작은 파일럿, 피드백 루프, Product Discovery로 이어질 수 있다. | Build with AI Part 3, Part 7, Builders Lounge, Bila AI Agent |

## Draft Narrative Beats

### Beat 1: 데모는 쉬워졌다

AI 도구 덕분에 화면을 만들고, 간단한 자동화를 붙이고, 코드까지 생성하는 일은 훨씬 쉬워졌다. 이 변화는 실제로 크다. 비개발자도 자기 아이디어를 눈에 보이는 형태로 만들 수 있게 됐다.

### Beat 2: 하지만 서비스는 다른 문제다

서비스는 데모보다 훨씬 거칠다. 사용자는 예상대로 행동하지 않고, 데이터는 지저분하고, 비용은 계속 쌓이고, AI는 때때로 틀린 말을 자신 있게 한다. 그래서 데모에서 바로 프로덕션으로 가면 균열이 생긴다.

### Beat 3: 첫 번째 벽은 문제 정의다

"이런 앱을 만들고 싶다"는 말은 충분하지 않다. 구체적인 상황, 사용자, 제약, 성공 조건이 있어야 한다. AI는 모호한 문제에도 그럴듯한 결과를 만들어주기 때문에, 문제 정의가 틀리면 빠르게 잘못된 방향으로 간다.

### Beat 4: 두 번째 벽은 데이터와 context다

AI Agent나 자동화는 모델이 좋아서만 잘 되는 게 아니다. 어떤 데이터를 먹이고, 그 데이터가 얼마나 일관되고, 최신이고, 맥락을 담고 있는지가 중요하다. Builders Lounge의 회의록과 멤버 Product 기록도 이런 관점에서 context 자산이 된다.

### Beat 5: 세 번째 벽은 검증과 운영 책임이다

실제 서비스는 AI 결과를 그대로 내보낼 수 없다. 중요한 영역일수록 출처, 검증, 인간 리뷰, 로그, 피드백 루프가 필요하다. "AI가 만들었다"는 말은 책임을 없애지 않는다.

### Beat 6: Builders Lounge Bridge

그래서 Builders Lounge는 데모와 서비스 사이의 작은 파일럿 환경이 될 수 있다. 혼자 만든 데모를 다른 사람에게 보여주고, 피드백을 받고, Bila AI Agent가 비슷한 문제를 가진 사람을 연결해주는 구조로 발전할 수 있다.

## Visual Beats

| Scene | Visual Idea |
|---|---|
| 1 | 데모 화면과 실제 서비스 운영 체크리스트를 대비한다. |
| 2 | `Demo -> Pilot -> Production` 흐름도를 보여준다. |
| 3 | `Problem -> User -> Data -> Workflow -> Validation -> Operation` 체인을 보여준다. |
| 4 | Bila AI Agent 연결 시나리오를 `Builder A blocked -> Similar Builder alerted -> Feedback loop`로 보여준다. |
| 5 | 다음 영상 예고로 Build with AI 학습 산출물과 Builders Lounge 실험을 연결한다. |

## Suggested Structure

1. Hook: "데모는 되는데 서비스가 안 되는 이유"
2. Build with AI 소개: 비개발자를 위한 실전 가이드라는 맥락
3. 핵심 thesis: 데모는 AI가 만들 수 있지만, 서비스는 문제·데이터·검증·운영 기준이 있어야 한다
4. 세 가지 벽: 문제 정의, 데이터/context, 검증/운영 책임
5. Builders Lounge 연결: 커뮤니티 검증과 Bila AI Agent가 도울 수 있는 지점
6. Close: 다음 단계에서 실제 영상/실험으로 확장

## Review Checklist

- 제목이 Catch Up AI 시청자에게 충분히 직접적인가?
- Build with AI 소개와 Builders Lounge 실험의 비중이 적절한가?
- Bila AI Agent는 본론이 아니라 다음 단계 bridge로 배치되어 있는가?
- 스크립트 확장 전에 사용자의 승인 또는 방향 수정이 필요한가?

## M3 DoD Check

아래 체크는 초안 기준이다. 정식 M3 DoD는 M2 정식 완료와 M3 학습 계획 승인 후 다시 검토한다.

- [x] Working title이 작성되었다.
- [x] Video promise가 작성되었다.
- [x] Opening script starter가 작성되었다.
- [x] Key Explanation Blocks가 5개 이하로 정리되었다.
- [x] 각 block의 source connection이 기록되었다.
- [x] Review Checklist가 포함되었다.
