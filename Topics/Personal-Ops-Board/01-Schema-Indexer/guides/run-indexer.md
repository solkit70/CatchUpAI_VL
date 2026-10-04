---
title: "준비"
created: 2026-10-02 10:43:41
tags:
  - personal-ops-board
  - vibelearn-ai
---

## 준비

Python 3.13과 python-frontmatter가 준비된 기존 볼트 환경을 사용한다. 아래 명령은 볼트 루트에서 실행하며, JSON은 비공개 AI/Tasks/views에 저장한다. 실행 성공 코드만 보지 말고 tasks·valid·problems를 확인한다.

## 실제 입력 실행

```powershell
python AI/Tasks/scripts/pob_index.py
```

--items 기본값은 실제 items 폴더, --out 기본값은 views/index.json이다. 파싱 오류가 있어도 입력을 보존하고 종료 코드는 0일 수 있으므로 error 목록을 확인해야 한다. 오류를 고치는 별도 작업 없이 원본을 자동 수정하지 않는다. → [파서 계약](../concepts/parser-contract.md#읽기-전용-파서-계약)

## 합성 입력 실행

```powershell
python AI/Tasks/scripts/pob_index.py --items "Ingest/CatchUpAI_VL/Topics/Personal-Ops-Board/01-Schema-Indexer/examples/fixtures" --out "AI/Tasks/views/m1-fixture-index.json"
```

실제 index.json 대신 별도 캐시를 사용한다. tasks 3개·valid 2개와 [기대 오류·경고](../examples/README.md#합성-fixture)를 확인하며, 결과 JSON을 공개 레포에 옮기지 않는다.

## 자동 회귀

```powershell
python -m unittest discover -s AI/Tasks/scripts -p test_pob_index.py -v
```

자동 검사는 임시 합성 파일로 실행하며 원본 해시 보존과 입력 누락도 확인한다. 현재 검증 건수와 결과는 [오늘 WorkLog](../../vl_worklog/20261002_M1_Personal-Ops-Board.md#검증)에 기록한다. 전체 실행 시간은 Python 프로세스 시작부터 JSON 저장 완료까지 측정하며 입력 증가 시 재검증한다.
