---
title: "M6 — Capstone: 결과 영상 제작"
author:
  - "박창수"
  - "Claude Code"
created: "2026-10-19 02:30:00"
tags:
  - ai-agent-apps-compare
  - capstone-video
---

## M6 — Capstone: 결과 영상 제작

[English](README.en.md)

**상태**: ✅ 완료 (2026-10-14 한국어 · 영어 영상 공개)
**예상 학습 시간**: 6시간

M1~M5 의 비교와 Muse 실습 결과를 영상 한 편으로 만들었다. 정보가 많은 비교라 **영상에서는 핵심 비교 · 직접 써 본 장면 · 고르기 전 네 가지 질문만 말하고**, 상세 표 · 출처 · 실습 기록은 GitHub QR 로 이 레포에 보낸다.

## 완성 영상

| 판 | 길이 | 링크 |
|---|---|---|
| 한국어 | 12:06 | [지시도 안했는데 Codex가 Muse에게 일을 시키고 있더라구요 - Grok Bot·Dots·Muse·Instinct 비교 분석 및 Muse 사용 직접 경험 해 보니...](https://youtu.be/BQ_TVly3TZI) |
| 영어 | 12:29 | [I Never Told It To, But Codex Put Muse to Work — 4 New AI Agents Compared & My Hands-On Muse Test](https://youtu.be/zi1iNN3AEBw) |

## 📚 학습 순서

1. [video-slide-plan.md](video-slide-plan.md) — 슬라이드 플랜(24장). 흐름 · 장면별 화면과 내레이션 · 라이브 클립 구간 · QR 배치 · 밝기 대역(L2)
2. [image-prompts.md](image-prompts.md) — AI 이미지 프롬프트 I1~I5 (사용자가 직접 생성)
3. [video-prompts.md](video-prompts.md) — Gemini 동영상 프롬프트 V1~V4 (사용자가 직접 생성)

영어판 짝: [video-slide-plan.en.md](video-slide-plan.en.md) · [image-prompts.en.md](image-prompts.en.md) · [video-prompts.en.md](video-prompts.en.md)

## 제작 과정

1. **슬라이드 플랜** — v1(23장, 10/13) → v2(24장, 10/14). 「밖에서는 Muse, 집에서는 내 2nd Brain」 장면(S20)을 박창수의 설명으로 더했다.
2. **라이브 클립** — Live #31 에서 Codex 가 브라우저의 Muse 를 조작한 장면 두 개를 박창수가 편집했고, 전사로 구간을 정했다. 클립 구간에만 한국어 자막을 달고 원래 소리를 그대로 썼다.
3. **이미지 · 동영상** — 이미지 I1~I5 와 Gemini 동영상 V1~V4(단풍 · 네 가지 질문 체크 등)를 사용자가 만들어 장면에 넣었다.
4. **오디오** — edge-tts 초벌 → 사용자 승인 → Qwen3-TTS 프리셋 목소리 4종. 박창수 복제 목소리는 사용자 판단으로 쓰지 않았다.
5. **렌더링 · 공개** — Remotion 으로 한국어판을 먼저 만들고 같은 구조에서 화면 문구 · 내레이션만 바꿔 영어판을 곧바로 만들었다. GitHub QR 은 S10(비교가 가장 조밀한 막의 끝) · S24(아웃트로)에 두 번 넣었다. 음악은 아웃트로에만 코드로 합성한 곡을 썼다.

제작 파일은 `AI/RemotionStudio/` 에 있고 이 레포에는 넣지 않았다.

## 이 모듈에서 알아낸 것

- **영상에서 「직접 써 본 것은 하나」라고 먼저 밝히니 오히려 신뢰가 생겼다.** 네 서비스를 비교했지만 실습은 Muse 하나, 과제는 가상 데이터 두 개였다. 그래서 순위나 「시간이 얼마나 절약된다」는 말을 하지 않았다.
- **AI 가 다른 AI 에게 일을 시킨 장면**(Codex → Muse)은 설명보다 원래 소리 클립이 더 잘 전한다.
- **한국어 영상을 만든 구조 그대로 영어 영상을 만들 수 있었다** — 코드 기반 영상 도구의 장점이다.

## 이동

- 이전: [M5 — 판단 기준](../05-Decision-Guide/README.md)
- Topic 첫 화면: [README](../README.md)
