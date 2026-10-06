---
title: "M6 — Claude Artifacts · Routines 영상 제작"
created: "2026-10-04 07:33:41"
author:
  - "Codex"
tags:
  - claude-artifacts-routines
  - remotion
status: "v4-review-pending"
---

## 현재 상태

사용자가 v1(28장, 약 12~15분)을 리뷰했다. 시청자의 관심을 끌고 유지하는 힘이 부족하다는 판단이었다. 그래서 [Claude 버전 제작 프롬프트](../vl_prompts/video_production_prompt_claude.md)로 바꾸고 플랜을 v2로 다시 짰다. v2는 23장, 약 11~12분이며 3주 동안 조용했던 루틴 이야기로 영상을 연다. 10/4 리뷰에서 플랜 내용이 확정됐다(필터 무시 일화 추가 · 자막 없음 · 아웃트로에만 직접 합성 음악). 남은 것은 사용자의 제목 확정과 필수 실화면 R1~R4 확보다. 음성·영상·QR 이미지는 아직 만들지 않았다.

**v3 (2026-10-06)**: 사용자 요청으로 ① Gemini 10초 동영상 5편 · 실사 이미지 6장 계획과 프롬프트 문서를 만들고 ② S20 「지금은 매주 받는다」(10/5 실제 알림 메일 · Claude 알림 · 워싱턴주 공고가 뜨면 지원)를 넣었다. 24장, 약 11~12분. 필수 실화면은 R1~R6이다.

**v4 (2026-10-06 나레이션 리뷰)**: 결론을 「일을 시키는 사람도 배워야 한다 · 아직은 조심스럽게」로 바꿨다. S04~S09 · S14 · S15 · S19 · S21 · S22 나레이션을 맥락이 따라가지도록 다시 쓰고, S23(다른 일에도 쓰는 다섯 가지)을 새로 넣고, 결론 S24를 새로 썼다. 25장, 약 15분 50초. 근거 C33~C36 추가.

**구현 시작 (2026-10-06)**: `AI/RemotionStudio/src/claude-artifacts-routines-1004/` — 샘플 3장(S01 · S08 · S15)을 Claude Code 가 만들었고, 나머지 22장은 Codex 가 그 폴더의 `CODEX_HANDOFF.md`(볼트 안 · 이 레포 밖)대로 만든다. 25장 전체의 edge-tts 초벌 음성 · 단어 시각은 `AI/RemotionStudio/public/claude-artifacts-routines-1004/audio/` 에 있다.

## 검토 순서

1. [슬라이드 플랜 v4](video-slide-plan.md) — 제목·챕터·장면별 내레이션·시각 자료·AI 이미지·동영상 계획·QR 목적지.
2. [장면별 근거 대장](claim-ledger.md) — v1 S01–S28 근거 + v4 장면 대응표·C29~C36, 날짜, 정정, 미확인 범위.
3. [캡처·자료 요청](capture-request.md) — 실제 화면(R1~R6)이 필요한 장면과 기록 재구성 대안.
4. [실사 이미지 프롬프트](image-prompts.md) (I1~I6, gpt-image-2) · [동영상 프롬프트](video-prompts.md) (V1~V5, Gemini Veo 10초).
5. [M6 WorkLog](../vl_worklog/20261004_M6_Claude-Artifacts-Routines.md) — 이번 세션 진행·남은 리뷰.

## 이어서 할 작업

플랜 승인 뒤 화면·자료를 준비하고 Remotion Studio 미리보기로 진행한다. 구현용 video-id 후보는 `claude-artifacts-routines-1004`이며 `AI/RemotionStudio/src/`와 `public/`에 같은 이름이 없는 것을 확인했다. 아직 구현 파일은 만들지 않았다. edge-tts 초벌 → Qwen3-TTS 최종 음성 → 자막 검수 → 승인 후 렌더 순서를 따른다.

[영상 제작 실행 프롬프트 (Claude 버전)](../vl_prompts/video_production_prompt_claude.md#12-실행-단계와-사용자-리뷰) · [이전 M5](../05-Usage-Patterns/README.md) · [Topic 전체](../README.md)



English companion: [README_en](README_en.md)
