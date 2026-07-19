---
title: "Build with AI Remotion Video Handoff"
created: 2026-07-19 07:16:00
tags:
  - vibelearn-ai
  - build-with-ai
  - remotion-video
  - video-handoff
---

## Purpose

이 문서는 나중에 `_Settings_/Skills/remotion-video/SKILL.md`를 사용해 Build with AI 영상을 제작할 때 넘길 handoff 데이터다. 이 Topic의 M1-M5 산출물을 Remotion Video Skill의 Phase 1 입력으로 바꾸기 위해 필요한 기준을 정리한다.

## Recommended Skill

이 Topic은 `remotion-video` 스킬로 제작하는 것이 적합하다.

| 후보 스킬 | 적합도 | 판단 |
|---|---|---|
| `remotion-video` | 높음 | 슬라이드 플랜 리뷰 → 이미지 프롬프트 → Remotion 컴포지션 → TTS → 렌더링 승인 흐름이 있어, 12부 해설형 영상에 적합하다. 동적 도식, 표, 섹션 전환, TTS 음성 리뷰를 단계적으로 관리할 수 있다. |
| `markdown-video` | 보조 가능 | Deckset 형식 markdown과 speaker notes가 이미 있을 때 빠르게 MP4를 만들기 좋다. 하지만 이 영상은 출처 화면, 도식, 여러 slide type, TTS 리뷰 단계가 중요하므로 Remotion 쪽이 더 적합하다. |

## Video Project Defaults

| 항목                      | 값                                                                                      |
| ----------------------- | -------------------------------------------------------------------------------------- |
| video-id 후보             | `build-with-ai-0719`                                                                   |
| Remotion project        | `AI/RemotionStudio/`                                                                   |
| output package source   | `Ingest/CatchUpAI_VL/Topics/Build-with-AI/05-Production-Package/production-package.md` |
| language                | Korean                                                                                 |
| target length           | 12-14분                                                                                 |
| target viewer           | 도메인 지식은 풍부하지만 컴퓨터·IT에는 익숙하지 않은 비개발자, 특히 시니어 도메인 전문가                                    |
| tone                    | 존중 + 쉬운 설명 + 현실적 격려                                                                    |
| recommended voice draft | `nova` 기본, 핵심 강조/클로징은 `shimmer` 또는 `onyx` 후보                                           |

## Required Source Documents for Video Skill

Remotion Video Skill을 실행할 때 아래 문서를 먼저 읽도록 지시한다.

1. `05-Production-Package/production-package.md` — 최종 제작 기준
2. `04-Slide-Plan/slide-plan.md` — 장면/시각 자료/asset map
3. `03-Video-Starter/video-brief.md` — opening script와 explanation blocks
4. `02-Video-Angle/first-video-angle.md` — 대상 시청자와 통합 angle
5. `01-Source-Map/easy-12-part-summary.md` — 12부 쉬운 설명 원고 재료
6. `01-Source-Map/source-materials.md` — Build with AI 공식 출처와 로컬 원본 파일

## Phase 1 Output Needed by Remotion Skill

Remotion Video Skill의 첫 작업은 아래 파일을 만드는 것이다.

```text
AI/RemotionStudio/public/build-with-ai-0719/video-slide-plan.md
```

`video-slide-plan.md`에는 최소한 다음이 포함되어야 한다.

| 항목 | 필요 데이터 |
|---|---|
| 제목 | `도메인 지식이 있다면, AI로 제품을 만들 수 있습니다: Build with AI 쉽게 보기` 또는 최종 승인 제목 |
| 스타일 | 교육형, 밝고 신뢰감 있는 테크 설명 영상 |
| 테마 컬러 | 너무 어둡지 않은 밝은 배경 + blue/green 계열 강조색. 시니어 대상이므로 대비와 글자 크기 우선 |
| 총 길이 | 12-14분 |
| 슬라이드 수 | 18-24장 예상. 12개 Part를 모두 다루므로 각 Part 1장 또는 묶음별 2-4장 구성 |
| 첫 30초 hook | 도메인 지식이 AI 시대에 제품의 씨앗이 될 수 있다는 질문과 약속 |
| 섹션 구조 | Opening → Source Setup → Target Viewer → 12부 큰 지도 → Part 0-12 해설 → 사용자 해석 → Practical Next Step → Close |
| 나레이션 | 각 슬라이드에 speaker narration 전문 포함 |
| 출처 표시 | Build with AI는 송재희님 자료로 화면/나레이션에서 명확히 attribution |

## Suggested Remotion Slide Types

| 구간 | Slide type | 이유 |
|---|---|---|
| Opening | `[TITLE]` 또는 `[QUOTE]` | 첫 30초 hook과 핵심 질문을 강하게 제시 |
| Source Setup | `[PHOTO+BULLET]` 또는 `[BULLET]` | 공식 사이트/다운로드 화면을 보여주며 자료 출처 소개 |
| Target Viewer | `[COMPARE]` | `도메인 지식 많음` vs `컴퓨터 익숙하지 않음`을 대비 |
| 12부 큰 지도 | `[WORKFLOW]` 또는 `[SVG]` | 12부를 네 묶음으로 시각화 |
| Part 0-2 | `[COMPARE]` | AI에게 맡길 일/사람이 확인할 일/사람이 결정할 일 |
| Part 3-6 | `[WORKFLOW]` | 도메인 지식 → 기록/context → 데이터 → AI 브리핑 |
| Part 7-9 | `[COMPARE]` | Agent / Vibe Coding / Code Assistant 비교 |
| Part 10-11 | `[WORKFLOW]` | 내가 쓰는 데모 → 남도 쓰는 제품 |
| Part 12 | `[QUOTE]` 또는 `[STAT]` | 도메인 지식이 해자라는 메시지 강조 |
| Next Step | `[WORKFLOW]` | 시청자의 실행 단계 제시 |
| Close | `[OUTRO]` | 따뜻하고 명확한 마무리 |

## Image / Capture Requirements

### Must Capture

- Build with AI 한국어 홈 화면: https://buildwithai.clearlyreqs.com/ko/
- Build with AI 다운로드 페이지: https://buildwithai.clearlyreqs.com/ko/downloads/

### Optional Capture

- `vl_materials/build-with-ai-complete-ko.pdf` 표지 또는 목차 화면
- 치트시트 4종의 표지 화면: prompt patterns, AI lego stack, trust tier, data readiness

### AI Image Prompt File

Remotion Video Skill Phase 1.5에서 아래 파일을 만들면 좋다.

```text
AI/RemotionStudio/public/build-with-ai-0719/image-prompts.md
```

이미지 생성이 필요한 경우에는 다음 주제를 프롬프트로 만든다.

- 도메인 전문가가 AI와 함께 지식을 제품으로 바꾸는 장면
- 도메인 지식 → 기록/context → AI 브리핑 → 작은 데모 → 검증 흐름
- 내가 쓰는 데모와 남도 쓰는 제품의 차이

단, 이 영상은 실제 출처 화면과 자체 도식이 중요하므로 AI 이미지는 보조적으로만 사용한다.

## TTS Notes

- 기본 말투는 존댓말, 밝고 차분한 교육형 톤.
- 시니어 대상이므로 문장을 너무 빠르게 읽지 않는다.
- `AI`, `Build with AI`, `Codex`, `Claude Code`, `Cursor`, `Bila AI Agent` 같은 영문 용어는 TTS에서 발음이 어색할 수 있으므로 음성 생성 전에 발음 테스트가 필요하다.
- 화면에는 원래 영문 표기를 유지하되, TTS 스크립트에서는 필요 시 한글 발음 표기를 병기한다.
- `Gobi` 또는 `GOBI`가 들어갈 경우 Remotion 스킬 규칙에 따라 TTS 원고에서는 `고비`로 표기한다.

## Approval Gates for Later Video Production

Remotion Video Skill을 사용할 때는 아래 승인 순서를 지킨다.

1. `video-slide-plan.md` 작성 후 사용자 리뷰
2. `image-prompts.md` 작성 후 사용자 리뷰
3. Remotion Studio 미리보기 후 시각 리뷰
4. edge-tts 초벌 오디오 리뷰
5. Qwen3-TTS 교체 후 최종 음성 리뷰
6. 최종 렌더링 승인 후 MP4 렌더링

초벌 TTS 상태에서는 렌더링하지 않는다.

## Handoff Prompt Draft

나중에 영상 제작 스킬을 호출할 때 아래처럼 요청하면 된다.

```text
remotion-video 스킬로 Build with AI 소개 영상을 제작해 주세요.

Topic 산출물 경로:
C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\Build-with-AI

먼저 아래 문서를 읽고 Phase 1 video-slide-plan.md부터 작성해 주세요:
- 05-Production-Package/production-package.md
- 05-Production-Package/remotion-video-handoff.md
- 04-Slide-Plan/slide-plan.md
- 03-Video-Starter/video-brief.md
- 01-Source-Map/easy-12-part-summary.md
- 01-Source-Map/source-materials.md

중요 조건:
- 이번 영상에서 Build with AI 12부를 모두 다룹니다.
- 각 Part는 원문 핵심 + 쉬운 설명 + 사용자 의견/예시 구조로 설명합니다.
- 대상은 도메인 지식이 많은 비개발자와 컴퓨터/IT에 익숙하지 않은 시니어 전문가입니다.
- Build with AI는 송재희님 자료로 명확히 출처 표시합니다.
- 먼저 video-slide-plan.md만 작성하고 사용자 리뷰를 받은 뒤 다음 단계로 진행하세요.
```

## Remaining Data Needed Before Actual Production

- [ ] 최종 제목 확정
- [ ] Build with AI 공식 사이트/다운로드 페이지 캡처 확보
- [ ] PDF 표지/목차 화면 사용 여부 결정
- [ ] 12개 Part별 사용자 예시를 어느 정도 구체적으로 말할지 결정
- [ ] 실제 영상 길이 목표를 12-14분으로 유지할지, 15분까지 허용할지 결정
