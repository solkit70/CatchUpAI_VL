---
title: "M3 실습 3 — 실물 점검: 부스 매니저 (수정 없음)"
created: 2026-09-27 15:50:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m3
  - review
---

## 결론

**수정하지 않는다.** 행사(9/26)가 끝났고 부스 매니저는 제 역할을 했다. 대신 오늘 배운 기능 기준으로 「다음에 비슷한 것을 만든다면 무엇을 다르게 할지」만 남긴다. 사용자 결정: 「간단하게 테스트하고 넘어갈 수 있는 것으로」. 로드맵 DoD 의 「또는 "수정 불필요" 근거」로 닫는다.

대상: 부스 매니저 (Artifact `KugonNUgi9Hm6VFcGPSPxu`) — 세션에서 `Artifact read` 로 읽기만 함. 다시 발행하지 않았다.

## 점검표

| 점검 | 부스 매니저 (실측) | 오늘 배운 것 | 다음에 만든다면 |
|---|---|---|---|
| 공유 상태 저장 | ✅ `db` — `booths` 컬렉션 + `meta/activity` 문서. localStorage 안 씀 | 여러 사람이 같은 데이터를 보려면 db 가 맞다 | 그대로 |
| 런타임 버전 | contract **0.2.41** (발행 당시) | 오늘 예제는 0.2.60 | 다시 발행할 일이 생기면 `contract: "latest"` 로 올릴지 검토 |
| 배치도 이미지 | 실내·실외 배치도 2장을 **HTML 안에 base64(`data:image/jpeg`)로** 넣었다 → 페이지 전체 246KB, 한 줄이 약 10만 자 | `assets` 로 올리면 HTML 은 가벼워지고 이미지는 `/_blob/<id>` 로 참조한다 (예제 ③) | 배치도는 assets 로 |
| 누가 바꿨나 | 활동 로그가 있지만 `user` 기능은 선언하지 않았다 | `user.id()` 로 바꾼 사람의 id 를 남기고, 이름은 볼 때 `profiles()` 로 푼다 (예제 ②) | 활동 로그에 user id |
| 의견 받기 | 댓글 기능 없음 | `composer_only` 댓글은 가볍고, Send to Claude 로 세션이 답할 수 있다 (예제 ④) | 부스마다 「이 부스에 댓글」 버튼 |
| 동시 수정 | 페이지 쓰기는 마지막에 쓴 사람이 이긴다 | 세션 쓰기는 `if_version` 으로 보호된다 (실습 2) | 세션이 부스 데이터를 고칠 때는 반드시 `if_version` |

## 이 점검으로 알게 된 것

부스 매니저는 이미 가장 중요한 선택(공유 상태는 db)을 맞게 했다. 놓친 것은 **이미지를 assets 로 분리하지 않은 것**과 **누가 바꿨는지를 user id 로 남기지 않은 것** 두 가지이고, 둘 다 행사 운영에는 문제가 없었다. 다음 행사용 도구를 만들 때 이 표를 출발점으로 쓴다.


English companion: [bighug-artifacts-review_en](bighug-artifacts-review_en.md)
