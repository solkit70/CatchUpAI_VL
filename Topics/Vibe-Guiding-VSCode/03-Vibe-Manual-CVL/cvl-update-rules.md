---
title: "CVL Update Rules"
created: 2026-05-10 06:52:12
tags:
  - vibe-guiding
  - cvl
  - update-rules
  - gobi-cli
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/vl_worklog/20260510_CVL_GOBI-CLI#GOBI CLI v2.0 주요 변경사항|GOBI CLI CVL WorkLog]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/03-Vibe-Manual-CVL/retrieval-metadata-design#최소 index 후보|Retrieval Metadata Design]]"
---

## 목적

CVL Update Rule은 어떤 변경이 Vibe Manual과 Retrieval Index를 갱신해야 하는지 판단하는 기준이다. GOBI CLI v2.0.12 업데이트처럼 명령어 이름이 바뀌면, 사람이 읽는 문서뿐 아니라 Guiding Engine이 쓰는 metadata도 함께 바뀌어야 한다.

## 영향도 기준

| 영향도 | 조건 | 조치 |
|---|---|---|
| 높음 | 명령어 이름, 파일 이름, 인증 방식, 주요 workflow가 바뀜 | 관련 manual, README, `manual_index`, `trigger_rules` 즉시 업데이트 |
| 중간 | 옵션 이름, 출력 필드, error message, config path가 바뀜 | 관련 guide와 completion signal 업데이트 |
| 낮음 | 설명 문구, 예시 제목, 링크, 보조 참고자료가 바뀜 | 다음 정기 CVL에서 반영 |

## 변경 유형별 규칙

| 변경 유형 | 예시 | 영향도 | 확인할 산출물 |
|---|---|---|---|
| CLI command 변경 | `create-thread` -> `create-post` | 높음 | manual, quick reference, deprecated terms, replacement terms |
| 파일 이름 변경 | `BRAIN.md` -> `PUBLISH.md` | 높음 | schema, sample manual, vault publish guide |
| 인증 방식 변경 | browser OAuth -> device-code flow | 높음 | auth guide, completion signal |
| config path 변경 | `.gobi/settings.yaml` 구조 변경 | 중간 | context collector fields |
| 출력 필드 변경 | `parentThreadId` -> `parentPostId` | 중간 | completion signal, test assertions |
| error message 변경 | auth/token 오류 문구 변경 | 중간 | known failures |
| 새 명령어 추가 | `gobi draft`, `gobi media` | 낮음-중간 | quick reference, optional index |

## CVL WorkLog 템플릿

```markdown
## CVL Change Summary

**변경 감지일**:
**대상 제품/버전**:
**영향도**:

## 변경 내용

| 기존 | 신규 | 영향 |
|---|---|---|

## 수정 대상

- [ ] Human-facing guide
- [ ] README / index
- [ ] manual_index
- [ ] trigger_rules
- [ ] sample user_context
- [ ] tests / completion signal

## 검증

- [ ] 구 명령어 검색
- [ ] 새 명령어 검색
- [ ] sample guide response 생성
- [ ] WorkLog 기록
```

## stale source 감지 규칙

다음 문자열이 현재 manual이나 index에 실행 명령어로 남아 있으면 stale source로 본다. 단, "구 명령어 변환표"나 "사용하면 안 되는 예시" 맥락은 허용한다.

| stale pattern | current replacement |
|---|---|
| `gobi init` | `gobi vault init` |
| `BRAIN.md` | `PUBLISH.md` |
| `gobi brain publish` | `gobi vault publish` |
| `gobi brain post-update` | `gobi global create-post` |
| `gobi brain list-updates` | `gobi global list-posts --mine` |
| `space create-thread` | `space create-post` |
| `space list-threads` | `space list-posts` |
| `session reply` | `session create-reply` |
| `gobi sync` | `gobi vault sync` |

## Guiding Engine 관점의 조치

CVL 업데이트가 발생하면 Guiding Engine 쪽에서는 다음 세 가지를 함께 점검한다.

1. `manual_index.json`의 `version_scope`, `commands`, `deprecated_terms`, `replacement_terms` 갱신
2. `trigger_rules.json`의 problem signal과 fallback 명령어 갱신
3. `guide_response.md` 샘플에서 구 명령어가 나오지 않는지 확인

## M4로 넘길 결정

M4 POC에는 최소한 `stale_command_detected` trigger를 넣는다. 사용자가 "thread를 만들고 싶다" 또는 `create-thread`를 입력하면, Guiding Engine은 구 명령어를 그대로 실행하라고 안내하지 않고 v2.0.12의 `create-post`로 변환해 안내해야 한다.
