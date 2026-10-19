---
title: "Topic Final Retrospective — AI-Agent-Apps-Compare"
author:
  - "박창수"
  - "Claude Code"
created: "2026-10-19 02:50:00"
tags:
  - ai-agent-apps-compare
  - retrospective
---

# Topic Final Retrospective — AI-Agent-Apps-Compare

## 전체 학습 여정

| 모듈 | 기간 | 진행 | 결과 |
|---|---|---|---|
| M1 서비스 정체 확인 | 10/4 (Live #30) | Codex | 네 서비스의 공개 정체 · 접근 조건 · 확인 필요 항목. 10/9 Instinct 추가, Dots 는 ChatGPT Plus 에서 불가 |
| M2 비교표 | 10/4 | Codex | 다섯 기준 비교 · 공식 근거와 보조 자료 구분 |
| M3 Muse 첫 사용 | 10/11 (Live #31) | Codex | 실제 UI · 권한 · 출처 검증 — Sources 패널이 공식 출처만은 아니었다 |
| M4 내 일 하나 맡겨 보기 | 10/11 | Codex | 가상 과제 두 개 — 시간표 계산은 「쓸 만함」, 형식 제한 글은 「고치면 쓸 만함」 |
| M5 판단 기준 | 10/11 | Codex | 판단 흐름도 · 예상/실제 표 · Topic README |
| M6 결과 영상 | 10/13~10/14 | Claude Code | 슬라이드 플랜 24장 → 한국어(12:06) · 영어(12:29) 공개, README 연결 10/19 |

**기간**: 2026-10-04 ~ 2026-10-14 (마무리 문서 10/19). 라이브 방송 두 번(Live #30 · #31)에서 실험했고, 결과는 영상 두 편과 공개 Topic 문서로 남았다.

## 학습 목표 달성도

- [x] 새 AI 에이전트 네 개를 공식 자료로 비교하고 근거 수준을 구분했다
- [x] 쓸 수 있는 서비스(Muse)를 직접 써 보고 결과를 기록했다 — Dots 는 요금제 문제로 실습하지 못했다
- [x] 업무 성격 · 위험 · 검증 가능성으로 맡길 범위를 정하는 판단 기준을 만들었다
- [x] 결과를 영상으로 만들어 공개했다

## 가장 가치 있었던 학습

1. **「쓸 수 있는가」가 비교의 첫 기준이었다.** 네 서비스 중 바로 쓸 수 있던 것은 Muse 하나였다(Instinct 는 대기 명단, Dots 는 상위 요금제). 기능표보다 접근 조건이 먼저 결과를 정했다.
2. **검증 방법은 일의 종류마다 다르다.** 정답을 먼저 만들 수 있는 계산 · 검출은 바로 검산했고, 글쓰기는 형식이 맞아도 근거 밖 표현이 남아 사람이 검토해야 했다.
3. **출처 패널의 링크가 곧 공식 자료는 아니다.** 공식 URL 을 따로 요구해야 했다.
4. **AI 가 다른 AI 에게 일을 시키는 장면을 실제로 봤다.** VS Code 의 Codex 가 브라우저의 Muse 를 조작해 단풍 추천을 받아 왔다 — 이 경험이 「밖에서는 Muse, 집에서는 2nd Brain」이라는 다음 아이디어로 이어졌다.

## 틀렸던 판단 · 확인하지 못한 것

- 처음에는 Dots 를 실습 대상으로 잡았지만 ChatGPT Plus 에서는 쓸 수 없었다(10/9 범위 갱신).
- 시간 절약은 측정하지 않았다 — 기준 작업 시간과 사람의 검토 시간을 재지 않아 「얼마나 아꼈다」는 말을 하지 않았다.
- 실습은 한 서비스 · 가상 과제 두 개뿐이라 서비스 순위를 만들지 않았다.
- Muse 의 결과를 내 컴퓨터로 옮기는 방법은 영상에서 「한 번 시도」 수준으로만 다뤘다 → 새 Topic **Muse-My-Workflow**(10/18 시작)에서 직접 시험한다.

## VibeLearn AI 방법론 효과성

- **에이전트를 나눠 썼다**: M1~M5 는 Codex, M6 는 Claude Code. Claude Code 가 M6 에 들어가며 Codex 산출물을 먼저 리뷰해 Roadmap · 서비스 카드를 보완했다 — 두 에이전트가 같은 Roadmap · WorkLog 를 읽으면 이어받을 수 있었다.
- **라이브 방송 + Topic 이 잘 맞았다**: 방송에서 실험하고, 문서로 남기고, 영상으로 다시 전했다. 영상 · README · 회고까지 가야 「끝났다」가 된다는 점도 확인했다.
- **아쉬운 점**: M6 WorkLog 와 README 영상 링크 연결이 공개 뒤 5일 늦었다. 영상 공개와 Topic 마무리 문서를 같은 날 하는 습관이 필요하다.

## 산출물 품질

- 한 · 영 짝 문서(M1~M6), 공식 출처 목록, 화면 캡처는 계정 상태를 가린 것만 썼다. 회의 · 고객 정보는 쓰지 않았다.
- 링크 검사(`check_links.py`)로 깨진 링크 · 빈 폴더 0 을 확인했다.

## 실무 적용과 다음

- Muse 를 내 작업 흐름에 맞추는 일은 **Muse-My-Workflow** Topic 으로 이어 간다 — 작업 18개의 적합도 지도(M1)는 끝났고, 옮기기 · 음성 지시 · VibeLearn on Muse 를 시험한다.
- 판단 흐름도(M5)는 시니어 AI 가이드(Senior-AI-Enablement)에서도 쓸 수 있다.
- Instinct 초대가 오면 후속 실습을 한다.

## 참조

- [Topic README](../README.md) · [M6 README](../06-Capstone-Video/README.md) · [M6 WorkLog](20261014_M6_AI-Agent-Apps-Compare.md) · [M5 회고](20261011_M5_Retrospective_AI-Agent-Apps-Compare.md) · [Roadmap](../vl_roadmap/20261004_RoadMap_AI-Agent-Apps-Compare.md)
