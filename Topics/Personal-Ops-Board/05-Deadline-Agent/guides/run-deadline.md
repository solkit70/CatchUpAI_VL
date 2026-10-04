---
title: "마감 경고 실행·검증 안내"
created: 2026-10-03 05:00:00 -07:00
tags:
  - personal-ops-board
  - guide
---

## 마감 경고 실행·검증 안내

### 운영 수동 실행

볼트 루트 PowerShell에서 인덱스를 새로 만든 뒤 마감 경고를 실행한다. 첫 명령이 실패하면 중단하고, 두 명령이 모두 성공했을 때만 `AI/Tasks/views/warnings.md`를 연다.

```powershell
python AI/Tasks/scripts/pob_index.py
if ($LASTEXITCODE -ne 0) { throw "POB indexer failed" }
python AI/Tasks/scripts/pob_deadline.py
if ($LASTEXITCODE -ne 0) { throw "POB Deadline failed" }
```

성공 출력은 기한 초과·오늘·경고 기간의 건수만 표시한다. view에는 비공개 task 링크가 포함되며 공개 레포에 복사하지 않는다. `items/` 및 `priority-board.md`는 읽기만 한다.

### 합성 날짜 경계 회귀

```powershell
python -m unittest discover -s AI/Tasks/scripts -p test_pob_deadline.py -v
```

테스트는 고정 기준일로 임계값과 실패 시 기존 파일 보존을 검사한다. 운영 데이터를 사용하지 않는다. 전체 POB 회귀는 아래처럼 실행한다.

```powershell
python -m unittest discover -s AI/Tasks/scripts -p "test_pob_*.py" -v
```

M5 학습 문서의 상대 링크는 볼트 루트에서 아래 명령으로 검사한다.

```powershell
python Ingest/CatchUpAI_VL/Topics/Personal-Ops-Board/05-Deadline-Agent/scripts/check_links.py
```

### AI4PKM 예약 실행

`orchestrator.yaml`의 POB Deadline 노드는 매일 오전 5시로 등록되어 있다. 실행 시 POB-Deadline prompt가 index를 새로 생성하고 deadline renderer를 호출한다. 현재 CLI에서 `ai4pkm --orchestrator` (`ai4pkm -o`)가 cron scheduler를 포함한 daemon을 시작한다. 해당 프로세스 로그에서 `POB-Deadline` 실행을 확인한다. node registry 수용과 1회 수동 실행은 통과했지만 scheduler 상시 운영 확인은 별도다.
