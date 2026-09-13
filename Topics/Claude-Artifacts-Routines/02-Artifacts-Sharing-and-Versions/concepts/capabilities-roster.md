---
title: "이 계정의 런타임 capability 8종 — 한 줄씩 (contract 0.2.46)"
created: 2026-09-13 08:07:00
tags:
  - claude-artifacts-routines
  - m2
  - concept
---

`Skill: artifact-capabilities` 가 2026-09-13 이 계정에 서빙한 목록. 계정·시점에 따라 다르다. 원문 발췌는 `vl_materials/2026-09-13 artifact-capabilities 스킬 발췌 (contract 0.2.46).md`.

| # | capability | 한 줄 | 언제 쓰나 | 공개 공유 |
|---|---|---|---|---|
| 1 | `artifact` (구 `self`) | 페이지가 **자기 자신을 새 버전으로 발행** — 상태를 HTML 에 박아 두고 상호작용 후 republish | 설문·체크리스트·보드처럼 "페이지가 곧 기록"이면 | 가능 |
| 2 | `db` | 서버 측 JSON 문서 저장소. 모든 뷰어가 공유 문서를 읽고 씀 · `data/users/<id>/` 는 개인 전용 · 세션도 `read_db/write_db` 로 접근 | 화면 밖에 두는 데이터 · Claude 가 나중에 읽는 데이터 · 편집자 여럿 | 페이지만. 데이터는 로그인 필요 |
| 3 | `assets` | 이미지·PDF·폰트·CSS/JS 업로드 (20 MiB) | 큰 이미지를 data URI 대신 | **불가** (조직 내부) |
| 4 | `downloads` | 페이지가 만든 파일을 뷰어가 저장 (확인 대화상자) | CSV 내보내기 등 | 미확인 |
| 5 | `mcp` | 뷰어 본인의 커넥터로 도구 호출 (뷰어 동의) | 라이브 데이터 대시보드 | **불가** |
| 6 | `room` | 지금 열어 둔 사람들끼리 실시간 이벤트·프레즌스. **아무것도 저장 안 됨** | 커서·반응·"같이 보기" | 미확인 (same-org 전제) |
| 7 | `sample` | 페이지가 Claude 에게 질문 — 뷰어가 과금·동의 | 페이지 안 AI 기능 | 미확인 |
| 8 | `permissions` (내장) | 선언 안 함. 상태 조회·묶음 요청 | 여러 권한을 한 번에 물을 때 | — |

**부스 매니저 재검토 포인트(M3)**: 편집 내용을 db 에 두는데, "페이지가 곧 기록"이면 `artifact`(republish)가 더 맞고, 공개 공유도 된다. 반대로 여러 사람이 동시에 편집하고 Claude 가 읽어야 하면 db 가 맞다 — 지금은 후자에 가깝다.
