---
title: "Personal-Ops-Board M1 — A1 인덱서 성능 개선"
created: 2026-10-02 10:34:02
tags:
  - vibelearn-ai
  - personal-ops-board
  - worklog
---

## 오늘의 학습 목표

- [x] 승인된 A1: 가지치기 순회 + 경로 직접 확인 + 이름 색인 지연 생성
- [x] 기존 파서 계약·원본 무변경·5초 목표 검증
- [x] ARCHITECTURE와 ADR을 구현 결과에 맞춰 갱신

**한 바퀴 위치**: 기존 ①~③ 제안에 대한 A1 승인 → ④ 구현·검증 → ⑤ 아키텍처 갱신 → ⑥ 기록. M0·M1 전체를 닫는 작업은 아직 남아 있다. 후속 「위 표에 있는 제안 대로 진행」 승인으로 A3 EARS 틀을 유지하고 마무리 문서를 작성했다. 10/2 사용자가 문서 검토 완료를 확인했다. 공개 커밋·push는 A4에 따라 별도 요청 후 한다.

## 진행 내용

### 승인과 문서 검토

사용자 A1 승인:

> A1 은 제안대로 해 주세요.

Go 검토 질문은 현재 Python 선택을 유지하면서 필요해지면 도입 가능하다는 의미로 확인했다. ADR 005의 보류를 영구 배제로 읽지 않도록 명확히 했고, 기존 v4 표기는 재검토 시기의 예시로 정리했다. Go 도입 자체를 승인받거나 구현한 것은 아니다. → [ADR 005의 결정](../architecture/decisions/005-Go%20는%20보류.md#결정)

### 구현

비공개 `AI/Tasks/scripts/pob_index.py`의 전체 순회는 `os.walk`로 바꾸고 제외 폴더에 들어가기 전에 가지치기한다. `LinkIndex`는 경로 링크를 직접 확인하고 이름만 있는 링크를 해석할 때만 전체 색인을 만든다. 합성 회귀 테스트는 비공개 `AI/Tasks/scripts/test_pob_index.py`에 두었다.

## 오늘 정한 요구 — EARS

| # | 요구 | 결과 |
|---|---|---|
| E1 | THE SYSTEM SHALL `_schema.md`를 제외한 모든 입력을 tasks에 남긴다 | 통과: 현재 69/69, 합성 중첩 파일 제외 |
| E2 | WHEN frontmatter 파싱이 실패하면 THE SYSTEM SHALL valid:false와 오류를 남긴다 | 통과: 실제 1개와 합성 오류 보존 |
| E3 | WHEN tier 1에 due가 없으면 THE SYSTEM SHALL 경고하고 원본을 고치지 않는다 | 통과: 합성 검사 |
| E4 | WHEN status가 waiting이면 THE SYSTEM SHALL tier 2와 waiting_on을 검증한다 | 통과: 합성 검사 |
| E5 | WHEN 링크 대상이 없거나 여러 개이면 THE SYSTEM SHALL unresolved 또는 ambiguous 경고를 낸다 | 통과: 합성 검사, 실제 링크 120개 기존 판정과 일치 |
| E6 | THE SYSTEM SHALL items 원본을 수정하지 않는다 | 통과: 실제·합성 SHA-256 동일 |
| E7 | THE SYSTEM SHALL 현재 입력의 전체 CLI 실행을 5초 안에 완료한다 | 통과: 0.221초, Python 프로세스 시작과 JSON 저장 포함 |
| E8 | WHEN 경로 링크만 있으면 THE SYSTEM SHALL 이름 색인을 만들지 않는다 | 통과: 전체 순회 호출 시 실패하는 합성 검사 |

## 검증

`python -m unittest discover -s AI/Tasks/scripts -p test_pob_index.py -v`: **10건 통과**. 경로 링크의 색인 생략, 이름 색인의 1회 생성, 중복·미해결 링크, 가지치기, 제외 경로, 기존 해석과 동등성, tier·waiting·필수·done 판정, CLI 입력 보존과 원본 무변경을 검사했다.

실제 인덱스: **69개·valid 68·error 1·warning 16·info 0**. 9/27의 58개와 현재 입력 수가 달라 당시 결과는 그대로 보존한다. 파싱 오류 1개는 입력에 있던 문제로 이번 작업에서 원본을 수정하지 않았다. 실제 정상 파싱 task의 문제 목록과 링크 120개를 기존 전체 색인 방식과 비교해 차이가 없었다.

전체 실행 0.221초로 5초 목표를 달성했다. 9/27의 86초와는 입력·측정 시점이 다르므로 같은 조건의 성능 비교로 취급하지 않는다. 생성 결과는 볼트의 `AI/Tasks/views/index.json`에만 저장했다.

### 후속 마무리 검증

후속 승인으로 합성 회귀 6건을 추가했다. `python -m unittest discover -s AI/Tasks/scripts -p test_pob_index.py -v` **16건 통과**: tier 2의 due·빈 waiting_on, paused 재개 조건, 상시 작업, priority 문자열, 파일명 변경·닫음 메타데이터·본문 보존까지 확인했다. 공개 fixture 세 개도 별도 캐시에 실행해 기대 결과와 원본 무변경을 확인했다.

기존 링크 검사기의 angle-bracket 경로 오탐은 Topic 링크를 공백 인코딩 표기로 맞춰 해결했다. 상대 링크 **81개 정상·깨짐 0·빈 폴더 0**, 섹션 앵커도 확인했다. 템플릿 예시 10개는 기존 도구 기준으로 제외했다. Task Board와 대응 items 파일을 같은 상태로 갱신했으며, 진행 중 task를 전체 완료로 표시하지 않았다.

## DoD와 남은 일

- [x] A1 구현·자동 회귀·실제 데이터·무변경·성능 검사
- [x] ARCHITECTURE 갱신 + ADR 009
- [x] M1 스키마 결정 로그 1~10 반영표 (당시 9건·현재 10건 구분)
- [x] M0·M1 README·계획된 학습 문서·합성 fixture·Topic 링크 검사
- [x] A2 사용자 문서 검토 완료 및 피드백 반영

**모듈 완료 판정**: M1 DoD 6/6 완료. M0는 문서·구조·링크 정리를 끝냈고 사용자 A2 검토 및 공개 전 개인정보 최종 확인은 남아 있다 (DoD 6/7). M2 코드는 시작하지 않았다.

## Daily Retrospective

### What went well

승인된 설계가 코드·테스트·ADR·현재 아키텍처로 이어졌다. E7의 모호했던 N초를 5초로 구체화하고 실제 전체 실행으로 확인했다.

### What could be improved

현재 원본에 YAML 파싱 오류 1개가 있다. 원본 수정은 이 읽기 전용 인덱서 개선과 별도 작업으로 남기며, 이름 링크가 많아질 때 성능도 다시 확인해야 한다.

### Insights

이번 병목은 언어 변경 없이 순회 범위를 필요한 순간으로 미루는 것으로 해결됐다. 방법론 실험에는 요구·승인·검증·아키텍처 갱신을 연결한 사례로 남기되, 전체 방법론의 성공 판정은 보류한다.

### Tomorrow's focus

M0 검토를 완료했다. 다음 M2는 요구·업계 방식 조사·설계 제안을 먼저 기록하고, 승인받은 뒤 구현한다. 공개는 별도 요청 후 진행한다.

## 참조 및 산출물

- [ADR 009](../architecture/decisions/009-링크는%20직접%20확인하고%20색인은%20지연%20생성.md#결정)
- [ARCHITECTURE 인덱서](../architecture/ARCHITECTURE.md#21-m1-인덱서)
- [Python 3.13 os.walk](https://docs.python.org/3.13/library/os.html#os.walk)
- 비공개 코드·테스트·캐시: `AI/Tasks/scripts/pob_index.py`, `AI/Tasks/scripts/test_pob_index.py`, `AI/Tasks/views/index.json`

## 실행 환경 메모

이번 후속 작업에서는 샌드박스 초기화 오류로 일반 셸과 Node 실행이 실패했다. 자동 승인 검토를 거친 로컬 명령으로 승인된 문서 작성·검증을 마쳤다. 공개 커밋·push와 M2 구현은 실행하지 않았다.

## 사용자 문서 검토 완료

10/2 사용자 확인: 「문서 검토 했고 다음을 진행해도 좋습니다.」 M0 학습 문서를 최종 점검했고, 공개 문서의 실명·연락처·개별 할 일 내용은 추가되지 않았음을 확인했다. 검토는 완료됐으며 외부 게시 요청은 별도다.
