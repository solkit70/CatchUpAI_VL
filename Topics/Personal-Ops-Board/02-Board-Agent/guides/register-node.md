---
title: "AI4PKM에 POB 연결"
created: 2026-10-02 11:32:31
tags:
  - personal-ops-board
  - guide
---

## AI4PKM에 POB 연결

비공개 볼트의 `_Settings_/Prompts/Personal Ops Board (POB).md`는 AI4PKM registry metadata와 인덱서·결정적 renderer를 순서대로 실행하는 얇은 진입점이다. `orchestrator.yaml`에는 새 파일을 위한 `Personal Ops Board - Created` 노드와 기존 파일 수정을 위한 `Personal Ops Board - Updated` 노드를 등록했다. 두 노드 모두 `AI/Tasks/items/*.md`를 감시하고 `_schema.md`는 제외하며, `AI/Tasks/views/priority-board.md`를 갱신한다.

AI4PKM CLI 0.1.25에서 registry는 두 node를 정상 로드하는 것을 확인했다. 실제 수정 trigger 명령은 `ai4pkm trigger POB-UPDATED`, 새 파일 trigger는 `ai4pkm trigger POB-CREATED`다. 사용자 Scripts 폴더를 PATH에 추가해 새 터미널에서 `ai4pkm` 명령을 사용할 수 있다. `input_type`은 CLI 런타임 값인 `new_file` 또는 `updated_file`을 사용한다.

두 node는 현재 `enabled: false`다. 승인된 `POB-UPDATED` 1회 실행에서 index와 priority board 갱신을 확인한 뒤 비활성화했다. AI4PKM 실행 log는 completed를 기록했지만 CP1252 콘솔의 Unicode 표시 예외로 프로세스 종료 코드는 1을 반환했다. 자동 파일 감시는 계속 꺼져 있다.

노드와 prompt 모두 읽기 전용 원칙을 따른다. 원본 `items/`와 기존 Task Board를 고치지 않고 생성 view만 갱신한다. 등록 전에 합성 결과를 보려면 [합성 예제](../examples/README.md)를 사용한다.
