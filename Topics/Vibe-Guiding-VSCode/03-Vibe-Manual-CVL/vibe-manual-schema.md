---
title: "Vibe Manual Schema"
created: 2026-05-10 06:52:12
tags:
  - vibe-guiding
  - schema
  - vibe-manual
  - atomic-guide-unit
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/01-Vision-and-Architecture/what-is-vibe-guiding#M1 잠정 정의|What Is Vibe Guiding]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/02-Architecture-Design/poc-boundary#출력 파일 계약|POC Boundary]]"
---

## 스키마 목적

Vibe Manual은 일반 사용 설명서가 아니라 Guiding Engine의 입력이다. 사람이 읽을 수 있어야 하고, 동시에 AI가 `goal`, `prerequisites`, `steps`, `completion_signal`, `known_failures`, `related_sources`를 안정적으로 추출할 수 있어야 한다.

> "지금 이 사용자에게 무엇을 알려줘야 작업이 끝나는가"

이 질문에 답하지 못하는 문서는 Vibe Manual로 충분하지 않다. Vibe Manual은 정보 설명보다 사용자의 작업 완료를 우선한다.

## Atomic Guide Unit

Atomic Guide Unit은 하나의 사용자 목표를 끝내기 위한 최소 안내 단위다. 너무 큰 매뉴얼은 retrieval이 부정확해지고, 너무 작은 매뉴얼은 guide response가 여러 조각을 조합하다가 실행 순서를 잃는다.

| 필드 | 필수 | 설명 |
|---|---|---|
| `id` | 예 | manual index에서 쓰는 안정적인 식별자 |
| `title` | 예 | 사람이 읽는 제목 |
| `product` | 예 | 대상 제품 또는 도구 |
| `version_scope` | 예 | 적용 가능한 버전 |
| `user_goal` | 예 | 사용자가 끝내려는 작업 |
| `difficulty` | 예 | beginner, intermediate, advanced |
| `prerequisites` | 예 | 시작 전에 확인할 조건 |
| `steps` | 예 | 실행 가능한 순서 |
| `completion_signal` | 예 | 성공 여부를 확인하는 관찰 가능한 신호 |
| `known_failures` | 예 | 자주 막히는 지점과 fallback |
| `related_sources` | 예 | 근거 문서 경로 |
| `deprecated_terms` | 아니요 | 사용하면 안 되는 구 명령어/구 용어 |
| `retrieval_keywords` | 예 | 검색용 키워드 |

## Markdown 구조

Vibe Manual 문서는 다음 구조를 사용한다.

```markdown
---
title:
manual_id:
product:
version_scope:
difficulty:
guide_type:
retrieval_keywords:
deprecated_terms:
sources:
---

## Goal

## When To Use

## Prerequisites

## Steps

## Completion Signal

## Known Failures And Fallbacks

## Source Notes
```

## Metadata 설계 기준

Metadata는 자연어 검색보다 안정적인 retrieval을 위한 최소 구조다. 예를 들어 사용자가 "Thread를 만들고 싶다"고 말해도 GOBI CLI v2.0.12에서는 `Post`로 안내해야 하므로, `deprecated_terms`와 `replacement_terms`를 index에 같이 넣어야 한다.

| metadata | 예시 | Guiding Engine 사용 방식 |
|---|---|---|
| `manual_id` | `gobi-cli-space-create-post` | retrieval result의 source id |
| `version_scope` | `GOBI CLI v2.0.12+` | 사용자 CLI 버전과 호환성 확인 |
| `retrieval_keywords` | `space`, `post`, `create-post`, `thread` | problem signal matching |
| `deprecated_terms` | `create-thread`, `list-threads` | 구 명령어 감지와 변환 안내 |
| `completion_signal` | `created post id returned` | guide response의 성공 기준 |

## Steps 작성 규칙

Steps는 실제 실행 단위로 작성한다. 각 step은 명령어, 기대 출력, 실패 시 다음 확인 항목을 포함해야 한다.

| 좋은 step | 나쁜 step |
|---|---|
| `gobi space list`로 접근 가능한 Space slug를 확인한다 | Space를 확인한다 |
| `gobi space create-post --space-slug <slug> --title "..." --content "..."`를 실행한다 | Post를 만든다 |
| 출력에서 `id`가 반환되면 성공으로 본다 | 잘 되는지 확인한다 |

## Completion Signal 기준

Completion Signal은 사용자가 주관적으로 "된 것 같다"고 느끼는 상태가 아니라, 관찰 가능한 결과여야 한다.

| 작업 | completion signal |
|---|---|
| CLI 설치 | `gobi --version`이 `2.0.12` 같은 버전을 출력 |
| 인증 | `gobi auth status`가 로그인 사용자와 authenticated 상태 출력 |
| Space Post 생성 | `create-post` 응답에 Post `id`가 반환되고 `get-post <id>`로 조회 가능 |
| Session 답장 | `session create-reply` 이후 `session get`에서 새 reply 확인 |

## Known Failure 작성 규칙

Known Failure는 실패를 설명하는 데서 멈추지 않고 fallback을 포함해야 한다. Guiding Engine은 이 필드를 사용해 "다음에 무엇을 확인할지"를 guide response에 넣는다.

| failure | fallback |
|---|---|
| 구 명령어 `create-thread`를 사용함 | v2.0.12 기준 `create-post`로 변환 |
| Space slug를 모름 | `gobi space list` 실행 후 slug 확인 |
| 인증이 안 됨 | `gobi auth login` 후 `gobi auth status` 재확인 |

## M4로 넘길 계약

M4 POC는 이 스키마를 기준으로 `manual_index.json`을 만든다. 최소 index에는 `manual_id`, `title`, `version_scope`, `guide_type`, `retrieval_keywords`, `completion_signal`, `source_path`가 들어가야 한다.
