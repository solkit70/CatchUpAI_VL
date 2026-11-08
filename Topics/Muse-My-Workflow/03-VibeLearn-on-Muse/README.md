# M3 — VibeLearn AI on Muse

[English](README.en.md)

**상태**: ✅ 완료 (2026-11-05) — 실습 1(10/25 · Claude Code) · 실습 2 · 3(11/1 Live #34 · Claude Code) · 실습 4(11/5 · Codex), DoD 8/8
**예상 학습 시간**: 1.5시간 (실제로는 세 세션에 나눠 진행)
**판정**: 밖에서 시작한 VibeLearn AI Topic 을 집에서 이어받기 — **가능**

Muse가 공개 저장소의 VibeLearn AI 지시를 읽고, 필요한 곳에서 멈추고, 다음 대화에서도 기억한 규칙을 따르는지 시험했다. 마지막에는 Muse Library에서 원본 파일을 내려받아 Codex가 집의 볼트에서 기간 검토 단계까지 이어받았다.

## 학습 순서

1. [지시를 읽고 따른다는 것](concepts/vibelearn-as-instructions.md) — 원문 읽기, 절차 준수, 결과물 확인을 구분한다.
2. [Muse 시험과 결과](guides/muse-vibelearn-test.md) — 원문 읽기, 순서, 기억, 이어받기의 관찰 결과를 확인한다.
3. [공개 행사 Topic 예시](examples/muse-topic-starter-sample.md) — Muse가 만든 Topic 정보와 프롬프트의 범위를 본다.
4. [집에서 이어받는 방법](guides/handoff-to-home.md) — 원본을 내려받고 어느 단계에서 재개할지 확인한다.

## 이 모듈에서 알아낸 것

- **읽기** — Muse 는 공개 레포의 지시 파일을 직접 읽었고, 지어낸 내용이 없었다. 파일끼리 맞지 않는 곳까지 스스로 짚었다.
- **멈추기** — 지시문에 「멈춰라」를 넣지 않았는데도 폴더 생성 · Phase 2 진입 · Roadmap 생성 앞에서 세 번 멈췄다. 「Topic 설명」 칸만 따로 묻지 않았다. 요약했다는 것과 지시를 따랐다는 것은 이렇게 따로 확인해야 한다.
- **기억** — 규칙을 `MEMORY.md` 에 저장하자 링크나 규칙을 다시 주지 않은 새 대화에서도 지켰다. 지우기를 요청하면 범위 · 부작용을 먼저 보여 준다(이번엔 지우지 않고 둠).
- **이어받기** — Library 에서 원본 3개를 내려받으니 SHA-256 이 모두 같았고, 두 프롬프트의 [2단계] · [3단계] 가 원본 템플릿과 일치했다. Codex 가 기간 검토(2주 × 주 3시간 적정)까지 이어받고 승인 지점에서 멈췄다.
- **비교 사례** — 처음에 실수로 Meta AI(meta.ai)에서 시험했는데, Meta AI 는 원문을 못 읽은 채 Roadmap 을 지어내고 기억도 못 했다. 같은 Meta 계열이라도 Muse 와는 다른 제품이다. 「원문을 못 읽으면 먼저 알려 줘」 한 줄이 지어내기를 막는다.
- **확인 못 한 것** — 휴대폰 앱의 Import memory · 학습 끄기 스위치.

회고: [M3 Module Retrospective](../vl_worklog/20261105_M3_Retrospective.md)

## 이동

- 이전 · [M2 — Muse ↔ 볼트 옮기기](../02-Muse-to-Vault/README.md)
- 다음 · [M4 — 볼트 연결 해법](../04-Vault-Connection/README.md)

## 영상용 재현 화면

아래 화면은 실제 M3 진행 당시의 녹화가 아니라, 2026-11-05 영상 제작을 위해 공개 저장소 기반의 가상 Topic 시작 절차를 재현한 화면이다. 승인 전 폴더나 파일을 만들지 않고 첫 확인 질문에서 멈춘 상태다.

![M3 Muse 승인 전 확인 질문 재현 화면](assets/M3-recreated-screen.jpg)
