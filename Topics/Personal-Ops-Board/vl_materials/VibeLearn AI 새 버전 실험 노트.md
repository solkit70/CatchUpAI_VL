---
title: "VibeLearn AI 새 버전 실험 노트 — KIRO 식 아키텍처 점진 완성 접목"
created: 2026-09-27 06:50:00
status: 실험 중 (Personal-Ops-Board Topic 전 기간)
tags:
  - vibelearn-ai
  - methodology
  - kiro
  - experiment
---

## 이 노트의 목적

**Personal-Ops-Board Topic 은 앱을 만드는 Topic 이면서, 동시에 방법론 실험이다.** KIRO 처럼 아키텍처 문서를 개발과 동시에 업데이트해 가는 프로젝트 진행 방법을 VibeLearn AI 에 접목한다. 이 실험이 성공적이라고 판단되면 **VibeLearn AI 의 새 버전을 별도로** 만든다 (사용자 결정 2026-09-27, Live #29).

> 「이 토픽은 KIRO 의 아키텍쳐 를 동시에 업데이트 해 가면서 진행하는 프로젝트 진행 방법을 저의 VibeLearn AI 에 접목시키는 것을 실험하는 단계 입니다. 이 실험이 성공적이라고 판단되면 VibeLearn AI 의 새로운 버전을 별도로 만들고 싶습니다. 그래서 KIRO 의 방법을 곧바로 적용하기 어려은 것은 우리 나람대로 방법을 찾아서 적용하면 됩니다.」

**원칙**: KIRO 방식을 그대로 옮기지 않는다. 곧바로 적용하기 어려운 것은 VibeLearn AI 에 맞는 우리 방식으로 바꿔 적용하고, 그 과정을 이 노트에 쌓는다. 이 노트가 새 버전 설계의 원재료다.

## 접목 원장 — KIRO 요소별로

| KIRO 요소 | 적용 방식 | VibeLearn AI 에서의 모습 | 첫 적용 | 평가 |
|---|---|---|---|---|
| 스펙을 개발하며 계속 고친다 | ✅ 그대로 | `architecture/ARCHITECTURE.md` 를 모듈마다 갱신 · 변경 이력 | M0 | ⏳ |
| 단계 사이 승인 게이트 | ✅ 그대로 (이미 있음) | 로드맵 승인 · 일일 계획 승인 · ③ 설계 승인 | M0 | ⏳ |
| 기능마다 스펙 | 🔄 변형 | 모듈마다 「한 바퀴」 6단계 (요구 찾기 → 업계 방식 → 승인 → 구현 → 아키텍처 갱신 → WorkLog) | M0 | ⏳ |
| `requirements.md` + EARS | 🔄 변형 | 별도 파일 없이 **WorkLog 「오늘 정한 요구」에 EARS 한 줄** → DoD 검증 항목 → [decisions/008](<../architecture/decisions/008-요구는 EARS 한 줄로도 적는다.md>) | M1 | ⏳ |
| `design.md` (기능마다) | 🔄 변형 | 앱 전체 `ARCHITECTURE.md` 하나 | M0 | ⏳ |
| (KIRO 에 없음) 결정의 이유 | ➕ 추가 | `architecture/decisions/NNN-제목.md` — 결정 하나 = 파일 하나 (ADR) | M0 | ⏳ |
| (KIRO 에 없음) 업계 방식 조사 | ➕ 추가 | ② 단계 — Builders Lounge 5차 발표자의 「갈라파고스 금지」 | M0 | ⏳ |
| Steering (`product.md` · `tech.md` · `structure.md`) | ≈ 이미 비슷함 | 볼트 `AGENTS.md` · `CLAUDE.md` · 개발 시작 Prompt 「절대 규칙」 | — | ⏳ 새 버전에서 Topic 단위 steering 이 필요한지 판단 |
| `tasks.md` + Sync Files · 병렬 실행 | ⏳ 미정 | 지금은 로드맵 실습 과제 · WorkLog 체크리스트 | — | ⏳ |

**범례**: ✅ 그대로 · 🔄 변형 적용 · ➕ 우리가 더한 것 · ≈ 이미 비슷함 · ⏳ 미정/평가 전

## 성공 판단 기준 (초안 — M10 에서 확정)

- [ ] 모든 모듈이 ⑤ 아키텍처 갱신을 한 상태로 닫혔다 (빠뜨린 모듈 0)
- [ ] EARS 한 줄이 DoD 검증 항목으로 실제로 쓰였다
- [ ] 결정 기록만 읽고 「왜 이렇게 만들었나」를 다른 사람에게 설명할 수 있다
- [ ] 아키텍처 템플릿을 다음 에이전트 앱(첫 재사용 후보)에 대입해 시작 시간이 줄었다
- [ ] 문서 작업 부담이 학습·개발 속도를 크게 떨어뜨리지 않았다 (Module Retrospective 평가)

## 새 버전에 담을 후보 (쌓아 가는 목록)

- 템플릿: `architecture/ARCHITECTURE.md` · `architecture/decisions/` 폴더를 Topic 기본 구조에 추가
- 로드맵 템플릿: 모듈마다 「한 바퀴」와 두 트랙(기능 산출물 + 아키텍처 갱신)을 기본으로
- WorkLog 템플릿: 「오늘 정한 요구 (EARS)」 절 · 「한 바퀴 중 어디까지」 줄

## 기록 규칙

- 모듈을 닫을 때(Module Retrospective) 위 원장의 「평가」 칸을 채운다
- KIRO 식 요소를 새로 적용하거나 바꾸면 원장에 한 줄 더하고, 앱 구조에 관한 것이면 `decisions/` 에도 남긴다
- Topic Final Retrospective 에서 이 노트로 「새 버전을 만들지」 판단한다
