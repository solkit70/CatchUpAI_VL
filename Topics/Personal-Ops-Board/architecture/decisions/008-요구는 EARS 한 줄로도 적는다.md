# 008 요구는 EARS 한 줄로도 적는다

- **날짜 · 모듈**: 2026-09-27 M0 (Live #29 방송 중 결정)
- **상태**: ✅ 채택 — 우리 방식으로 변형해 적용

## 맥락
KIRO 공식 문서를 확인해 보니, KIRO 는 요구사항을 **EARS 표기**(Easy Approach to Requirements Syntax)로 쓴다 — 「WHEN [조건/사건] THE SYSTEM SHALL [기대 동작]」. 이 Topic 은 요구 찾기 결과를 WorkLog 에 자연어 표로만 적고 있었다 → [006](<006-두 트랙 개발 방식.md>) 비교표.

사용자 결정 (방송 중):

> 「이 토픽은 KIRO 의 아키텍쳐 를 동시에 업데이트 해 가면서 진행하는 프로젝트 진행 방법을 저의 VibeLearn AI 에 접목시키는 것을 실험하는 단계 입니다. (…) KIRO 의 방법을 곧바로 적용하기 어려은 것은 우리 나람대로 방법을 찾아서 적용하면 됩니다. 위에 제안한 방법은 좋은 시도 인것 같습니다.」

## 검토한 선택지
| 선택지 | 장점 | 단점 |
|---|---|---|
| 자연어 표만 (지금) | 대화 그대로 · 빠름 | 모호함이 남는다 · DoD 로 옮길 때 다시 써야 함 |
| KIRO 그대로 — 모듈마다 `requirements.md` 파일 | 공식 방식 | VibeLearn AI 에 이미 WorkLog · 로드맵 DoD 가 있어 문서가 겹친다 |
| **우리 방식 — WorkLog 「오늘 정한 요구」에 EARS 한 줄을 함께** | 대화 기록은 그대로 두고 검증 가능한 한 줄만 더함 · 그 줄이 DoD 검증 항목이 된다 | 표기에 익숙해지는 시간 |

## 결정
- 매 모듈 ① 요구 찾기에서 정한 요구마다 **EARS 한 줄**을 함께 적는다. 위치는 WorkLog 「오늘 정한 요구」 (별도 `requirements.md` 는 만들지 않는다)
- 한국어로 쓰되 틀은 유지한다: **「WHEN [조건] 이면 THE SYSTEM SHALL [동작] 한다」** · 조건 없는 요구는 「THE SYSTEM SHALL …」
- ④ 검증에서 EARS 한 줄마다 통과/실패를 적는다 — 이것이 DoD 의 검증 항목이 된다
- 첫 적용: M1 인덱서 요구를 EARS 로 다시 적는다 (2026-09-27 WorkLog)

## 이유
KIRO 의 장점(모호하지 않고 바로 테스트로 옮길 수 있는 요구)은 가져오고, VibeLearn AI 의 기존 문서(WorkLog · 로드맵 DoD)와 겹치는 파일은 만들지 않는다.

## 결과 · 대가
- 대가: 요구 찾기 시간이 조금 늘어난다
- 다시 볼 조건: EARS 줄이 DoD 로 잘 옮겨지지 않거나, 대화 속도를 떨어뜨리면 — Module Retrospective 에서 평가
- 이 결정은 VibeLearn AI 새 버전 실험의 첫 「변형 적용」 사례다 → `vl_materials/VibeLearn AI 새 버전 실험 노트.md`

## 대화 출처
[WorkLog](../../vl_worklog/20260927_M0_Personal-Ops-Board.md) · [EARS — Kiro Feature Specs](https://kiro.dev/docs/specs/feature-specs/)
