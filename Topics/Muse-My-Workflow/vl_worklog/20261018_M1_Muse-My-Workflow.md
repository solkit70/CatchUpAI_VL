---
title: "WorkLog - M1: 작업 목록과 Muse 적합도 지도"
author:
  - "박창수"
  - "Claude Code"
created: 2026-10-18 08:30:00
tags:
  - muse-my-workflow
  - worklog
---

# WorkLog - M1: 작업 목록과 Muse 적합도 지도

**날짜**: 2026-10-18
**Topic**: Muse-My-Workflow
**모듈**: M1 - 작업 목록과 Muse 적합도 지도
**학습 시간**: Live #32 방송 4부 (실제 시각 미기록)
**진행 에이전트**: Claude Code

## 🎯 오늘의 학습 목표

- [x] 작업 15개 이상 목록 (18개)
- [x] 적합도 판정 + 상위 작업 확인 (박창수 요청으로 6개)
- [x] Muse 기능 표 (출처 또는 「미확인」)
- [x] `01-Workflow-Fit-Map/` 문서 4개 + README
- [x] WorkLog · Daily Retrospective · 링크 검사

## 📚 진행 내용

### 1. 작업 목록 만들기

**과정**: 볼트 기록(`orchestrator.yaml` 워크플로 · `_Settings_/Prompts/` 21개 · 할 일 목록 · 2026-10-11 Weekly Progress)에서 반복 작업 18개를 뽑았다. 내부 자료 · 의뢰인 정보가 섞이는 작업은 종류만 적었다.

**박창수 답** (원문은 [[Journal/2026-10-18]] Thoughts): 밖에서는 진행 중인 VibeLearn AI Topic 을 이어 가고, 그때그때 떠오르는 아이디어 · 해야 할 일을 Muse 로 먼저 정리한 뒤 집에서 로컬로 내려받고 싶다. 수시로 생기는 일이다. 차 안에서는 음성, 행사장 · 카페에서는 문자로 지시한다. 작업 목록에 이미 다 있다고 확인했다.

### 2. 적합도 판정

판정 기준 4가지로 18개를 판정했다 — 맡김 3 · 초안만 10 · 맡기지 않음 5. 상위 5개를 제시했고, 박창수가 **#10 Remotion 슬라이드 플랜 · 대본**을 더해 6개로 확정했다. 음성 · 문자 지시 방식을 판정 기준 문서에 넣었다.

### 3. Muse 기능 확인 (공식 자료)

Meta 발표문과 도움말 6개 페이지를 직접 열어 확인했다. 핵심:
- ✅ Markdown 을 포함한 파일(Artifact)을 만들고 Library 에 저장한다
- ✅ Settings → Data controls → Download your Muse data 로 전체 데이터를 내려받는다 (형식은 안 나옴)
- ✅ 앱을 닫아도 계속 일하고, 자기 브라우저로 웹에 접근하고, 이메일 등 커넥터가 있다
- ❓ **파일 하나씩 내려받기 · 음성 입력 · GitHub 연결은 공식 자료에 없다** → M2 · M3 에서 직접 확인

## 🐛 문제 해결 로그

- 「기억 가져오기(Import memory)」는 웹 검색 결과 요약에만 나오고, 직접 연 데이터 관리 페이지에서는 찾지 못했다. 「확인」으로 쓰지 않고 「재확인 필요」로 낮췄다.
- 차 안 음성 지시가 박창수의 핵심 사용 방식인데 공식 자료에 음성 입력이 없다. 휴대폰 키보드 받아쓰기를 대안으로 M2 에서 함께 시험하기로 했다.

## 📊 DoD 체크리스트

- [x] 작업 15개 이상 목록 · 적합도 판정 완료
- [x] 「맡김」 · 「초안만」 상위 작업을 박창수가 확인 (6개)
- [x] 「올리면 안 되는 것」 한 장 정리
- [x] Muse 기능 표 — 모든 행에 출처 또는 「미확인」 · 「재확인 필요」
- [x] 공개 문서에 실명 · 의뢰인 · 내부 자료 내용 없음
- [x] 산출물 폴더 README 작성
- [x] README 링크 확인 (`check_links.py` — 정상 11 · 깨짐 0 · 빈 폴더 0)
- [x] WorkLog · Daily Retrospective 작성

**진행 상태**: ✅ M1 완료 (8/8)

## 💡 Daily Retrospective

### What went well
- 볼트 기록으로 작업 목록을 먼저 만들어 보여 드리니, 박창수가 「이미 다 있다」고 바로 확인했다. 질문은 하나로 충분했다.
- 공식 자료를 직접 열어 확인한 것과 검색 요약을 구분해, 확인되지 않은 기능을 「확인」으로 쓰지 않았다.

### What could be improved
- 판정은 Claude Code 가 근거와 함께 매겼지만, 실제로 써 보기 전이라 가설이다. M4 결과로 표를 고쳐야 한다.
- 방송 중이라 각 활동의 실제 시각을 기록하지 못했다.

### Insights
- 이 Topic 의 성패는 **「밖에서 만든 것이 파일로 집에 오는가」**와 **「음성으로 말한 것이 그대로 남는가」** 두 가지에 달려 있다. 둘 다 공식 자료로는 미확인이다.
- 「초안만」이 가장 많다는 것은 Muse 가 볼트를 대신하는 게 아니라, **볼트로 들어오는 입구** 역할이라는 뜻이다.

### Tomorrow's focus
- M2 실습 1: Muse 에서 Markdown 파일을 만들어 하나씩 내려받기부터 시험 (웹 · 휴대폰)
- 음성 입력 — 앱 기능, 없으면 키보드 받아쓰기로 원문이 남는지
- 볼트 착지 위치 후보를 박창수에게 제시

## 📎 참조 및 산출물

- [01-Workflow-Fit-Map/README.md](../01-Workflow-Fit-Map/README.md)
- [concepts/fit-criteria.md](../01-Workflow-Fit-Map/concepts/fit-criteria.md) · [guides/workflow-fit-map.md](../01-Workflow-Fit-Map/guides/workflow-fit-map.md) · [guides/do-not-upload.md](../01-Workflow-Fit-Map/guides/do-not-upload.md) · [examples/muse-feature-check.md](../01-Workflow-Fit-Map/examples/muse-feature-check.md)

## 다음 세션에 넘길 것

1. M1 완료. 상위 6개(#13 메모 · #9 VibeLearn · #4 구술 원문 · #11 공개 행사 리서치 · #7·#8 공개 글 · #10 Remotion 대본)가 M2 시험 재료다.
2. 박창수 결정: 차 안은 음성, 행사장 · 카페는 문자로 지시. #10 을 상위 목록에 추가.
3. 바로 할 일: M2 — `examples/muse-feature-check.md` 의 미확인 4개(개별 다운로드 · 음성 · 전체 다운로드 형식 · GitHub)부터 직접 시험. 메일 · 드라이브 연결은 하기 전에 박창수에게 묻는다.
