---
title: "Board renderer 수동 실행"
created: 2026-10-02 11:32:31
tags:
  - personal-ops-board
  - guide
---

## Board renderer 수동 실행

PowerShell을 볼트 루트에서 열고 인덱서와 renderer를 차례로 실행한다. 입력이 바뀐 뒤 인덱서를 먼저 실행해야 Board가 최신 상태를 반영한다.

```powershell
python AI/Tasks/scripts/pob_index.py
if ($LASTEXITCODE -ne 0) { throw "POB indexer failed" }
python AI/Tasks/scripts/pob_board.py
if ($LASTEXITCODE -ne 0) { throw "POB board renderer failed" }
```

결과는 `AI/Tasks/views/priority-board.md`에 생성된다. 결과를 열어 네 lane, 완료와 닫음, 점검 필요, 실행 정보를 확인한다. 이 명령은 기존 `AI/Tasks/Task Board.md`나 입력 task를 바꾸지 않는다.

합성 fixture를 시험할 때는 먼저 별도 임시 경로에 인덱스를 만든다. `<fixture>`는 이 문서의 예제 폴더 경로다.

```powershell
$fixture = "Ingest/CatchUpAI_VL/Topics/Personal-Ops-Board/02-Board-Agent/examples/fixtures"
$tempIndex = Join-Path $env:TEMP "pob-m2-fixture-index.json"
$tempBoard = Join-Path $env:TEMP "pob-m2-fixture-board.md"
python AI/Tasks/scripts/pob_index.py --items $fixture --out $tempIndex
if ($LASTEXITCODE -ne 0) { throw "fixture indexer failed" }
python AI/Tasks/scripts/pob_board.py --index $tempIndex --items $fixture --out $tempBoard
if ($LASTEXITCODE -ne 0) { throw "fixture renderer failed" }
Get-Content $tempBoard
```

fixture 결과를 공개 입력처럼 다루지 않고 임시 위치에서만 확인한다. 실행 실패 시 이전 보드가 남아 있는지 확인하고 [ADR 010](../../architecture/decisions/010-M2-보드는-비공개-view만-생성.md#결정)의 실패 정책을 따른다.
