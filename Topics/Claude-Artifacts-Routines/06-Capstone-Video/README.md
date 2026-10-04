---
title: "M6 — Claude Artifacts · Routines 영상 제작"
created: "2026-10-04 07:33:41"
author:
  - "Codex"
tags:
  - claude-artifacts-routines
  - remotion
status: "slide-plan-review-pending"
---

## 현재 상태

사용자가 v1(28장, 약 12~15분)을 리뷰했다. 시청자의 관심을 끌고 유지하는 힘이 부족하다는 판단이었다. 그래서 [Claude 버전 제작 프롬프트](../vl_prompts/video_production_prompt_claude.md)로 바꾸고 플랜을 v2로 다시 짰다. v2는 22장, 약 10~11분이며 「3주 동안 조용했던 AI 자동화」를 Cold Open으로 연다. 음성·영상·QR 이미지는 아직 만들지 않았고, 플랜 v2 리뷰와 필수 실화면 R1~R4 확보 여부 결정을 기다린다.

## 검토 순서

1. [슬라이드 플랜 v2](video-slide-plan.md) — 제목·챕터·장면별 내레이션·시각 자료·QR 목적지.
2. [장면별 근거 대장](claim-ledger.md) — v1 S01–S28 근거 + v2 장면 대응표·C29, 날짜, 정정, 미확인 범위.
3. [캡처·자료 요청](capture-request.md) — 실제 화면이 필요한 장면과 기록 재구성 대안.
4. [M6 WorkLog](../vl_worklog/20261004_M6_Claude-Artifacts-Routines.md) — 이번 세션 진행·남은 리뷰.

## 이어서 할 작업

플랜 승인 뒤 화면·자료를 준비하고 Remotion Studio 미리보기로 진행한다. 구현용 video-id 후보는 `claude-artifacts-routines-1004`이며 `AI/RemotionStudio/src/`와 `public/`에 같은 이름이 없는 것을 확인했다. 아직 구현 파일은 만들지 않았다. edge-tts 초벌 → Qwen3-TTS 최종 음성 → 자막 검수 → 승인 후 렌더 순서를 따른다.

[영상 제작 실행 프롬프트 (Claude 버전)](../vl_prompts/video_production_prompt_claude.md#12-실행-단계와-사용자-리뷰) · [이전 M5](../05-Usage-Patterns/README.md) · [Topic 전체](../README.md)

