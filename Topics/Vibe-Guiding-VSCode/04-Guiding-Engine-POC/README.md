---
title: "M4 - Guiding Engine POC"
created: 2026-05-10 07:12:00
tags:
  - vibe-guiding
  - guiding-engine
  - poc
  - m4
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/02-Architecture-Design/poc-boundary#POC 목적|POC Boundary]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/03-Vibe-Manual-CVL/retrieval-metadata-design#M4로 넘길 결정|Retrieval Metadata Design]]"
---

## 모듈 정보

**모듈**: M4 - Guiding Engine POC 개발  
**상태**: 진행 중  
**예상 학습 시간**: 12h  
**목표**: GOBI CLI v2.0.12 문서를 기반으로 `user_context -> trigger -> retrieval -> guide_response` 파일 흐름을 검증한다.

## 실행 순서

PowerShell에서 이 폴더를 기준으로 실행한다.

```powershell
python src/collect_context.py
python src/evaluate_trigger.py
python src/retrieve_manual.py
python src/compose_guide.py
```

생성되는 출력:

| 파일 | 설명 |
|---|---|
| `output/user_context.json` | 입력 또는 수집된 사용자 상태 |
| `output/trigger_decision.json` | 선택된 trigger rule |
| `output/retrieval_result.json` | 선택된 manual entry |
| `output/guide_response.md` | 사용자에게 제공할 최종 안내 |

## 학습 순서

1. [data/user_context.sample.json](data/user_context.sample.json)  
   기본 입력 context와 problem signal 예시다.

2. [data/trigger_rules.json](data/trigger_rules.json)  
   problem signal을 guide type으로 연결하는 rule set이다.

3. [data/retrieval_index.json](data/retrieval_index.json)  
   GOBI CLI v2.0.12 Vibe Manual 문서와 metadata를 연결하는 file-based index다.

4. [src/collect_context.py](src/collect_context.py)  
   sample context를 output으로 복사하거나 `--system` 옵션으로 일부 실제 환경 정보를 수집한다.

5. [src/evaluate_trigger.py](src/evaluate_trigger.py)  
   context와 trigger rules를 비교해 가장 적합한 rule을 선택한다.

6. [src/retrieve_manual.py](src/retrieve_manual.py)  
   trigger decision과 retrieval index를 사용해 관련 manual entry를 고른다.

7. [src/compose_guide.py](src/compose_guide.py)  
   선택된 manual과 context를 바탕으로 `guide_response.md`를 생성한다.

8. [tests/test_scenarios.md](tests/test_scenarios.md)  
   최소 3개 테스트 시나리오와 기대 결과를 정리한다.

9. [tests/run_scenarios.py](tests/run_scenarios.py)  
   `data/test_contexts.json`의 3개 시나리오를 실행하고 `output/scenarios/`와 `output/test_results.json`을 생성한다.

## 현재 DoD 진행

- [x] POC 폴더 구조 생성
- [x] `collect_context.py` 실행 성공
- [x] `trigger_rules.json` 기반 Trigger 판정 성공
- [x] `retrieval_index.json` 기반 문서 선택 성공
- [x] `guide_response.md` 자동 생성 성공
- [x] 최소 3개 테스트 시나리오 정의
- [x] 최소 3개 테스트 시나리오 실행 성공
- [x] `04-Guiding-Engine-POC/README.md` 작성
- [x] WorkLog 작성 및 Daily Retrospective 완료

## 이전/다음 모듈

**이전 모듈**: M3 - Vibe Manual과 CVL 설계  
관련 문서: [../03-Vibe-Manual-CVL/README.md](../03-Vibe-Manual-CVL/README.md)

**다음 모듈**: M5 - GOBI 시나리오 검증  
다음 모듈에서는 이 POC의 guide response를 실제 GOBI CLI/Desktop 시나리오 기준으로 평가한다.
