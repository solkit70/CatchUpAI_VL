---
title: "WorkLog - M6: Capstone — 결과 영상 제작"
author:
  - "박창수"
  - "Claude Code"
created: "2026-10-19 02:40:00"
tags:
  - ai-agent-apps-compare
  - worklog
---

# WorkLog - M6: Capstone — 결과 영상 제작

**날짜**: 2026-10-13 ~ 2026-10-14 (기록은 2026-10-19 에 작업 기록 · Daily Roundup 으로 정리)
**Topic**: AI-Agent-Apps-Compare
**모듈**: M6 - Capstone — 결과 영상 제작
**학습 시간**: 실제 시각 미기록 (10/14 하루 대부분)
**진행 에이전트**: Claude Code (M1~M5 는 Codex)

## 🎯 학습 목표

- [x] M1~M5 결과로 영상 슬라이드 플랜을 쓰고 승인받는다 (v1 10/13 → v2 10/14)
- [x] 영상에서 말할 것과 문서로 보낼 것을 나눈다 (상세는 GitHub QR)
- [x] GitHub QR 2회를 넣어 렌더링한다 (S10 · S24)
- [x] Codex 가 Muse 를 직접 조작한 과정과 생활형 위임(단풍 추천)을 소개한다 (라이브 클립 두 개)
- [x] 완성 영상 링크를 Topic README 에 연결한다 (10/19)

## 📚 진행 내용

### 10/13 — 리뷰와 슬라이드 플랜 v1

Codex 가 진행한 M1~M5 산출물을 리뷰해 Roadmap v1.5 · 서비스 카드 · 공개 레포 정리 · M1 · M2 회고를 보완했다. 이어서 슬라이드 플랜 v1(23장, 약 13~14분)을 썼다.

### 10/14 — v2 · 소재 · 오디오 · 렌더링 · 공개

1. 슬라이드 플랜 v2(24장) — 「밖에서는 Muse, 집에서는 내 2nd Brain」 장면(S20) 추가, 이미지 프롬프트 I1~I5 · Gemini 동영상 프롬프트 V1~V4
2. 박창수가 Live #31 클립 두 개를 편집 → 전사로 구간 확정 · 원래 소리 + 한국어 자막
3. Remotion 장면 24장 + edge-tts 초벌(약 12분 18초) → 사용자 생성 이미지 · 동영상 적용
4. Qwen3-TTS 프리셋 목소리 4종으로 최종 음성 (복제 목소리 미사용 — 사용자 판단)
5. 렌더링 — 한국어 12:06 · 영어 12:29 → 유튜브 공개 → 플랫폼별 SNS 홍보

**결과**: 한국어 [https://youtu.be/BQ_TVly3TZI](https://youtu.be/BQ_TVly3TZI) · 영어 [https://youtu.be/zi1iNN3AEBw](https://youtu.be/zi1iNN3AEBw)

### 10/19 — 마무리

모듈 README(한 · 영) 작성, Topic README(한 · 영)에 영상 링크와 M6 연결, Topic 최종 회고 작성, 링크 검사.

## 🐛 문제 해결 로그

- **Muse 는 Meta 의 서비스, 장면 속 조작은 Codex(OpenAI)** — 업로드 문구를 쓰며 「Claude 가 Muse 를 조작」으로 오해할 수 있는 표현을 바로잡았다.
- 슬라이드 플랜은 박창수 복제 목소리를 계획했으나, 최종 음성은 사용자 판단으로 프리셋 목소리 4종을 썼다(복제 목소리는 작업마다 확인 — 메모리 규칙).
- 계획 길이(약 14분)보다 실제 영상이 짧다(12분대) — 장면별 Qwen3 음성 길이를 기준으로 렌더했다.

## 📊 DoD 체크리스트

- [x] 슬라이드 플랜 승인
- [x] 오디오 승인
- [x] 렌더링 완료 · 사용자 검토
- [x] QR 2회 이상 실제 슬라이드로 존재 (S10 · S24)
- [x] 영상에 개인정보 · 계정 화면 없음 (가린 화면만 사용)
- [x] Topic README 에 영상 링크 추가 (10/19)
- [x] README 링크 확인 (`check_links.py`)
- [x] Topic Final Retrospective 작성

**완료율**: 8/8 · **진행 상태**: ✅ M6 완료 → Topic 완료

## 💡 Daily Retrospective

### What went well
- 슬라이드 플랜에서 공개까지 한 · 영 두 편을 하루에 끝냈다.
- 「직접 써 본 것은 하나」를 영상 안에서 먼저 밝혀, 비교 영상이 과장되지 않았다.

### What could be improved
- M6 WorkLog 를 그날 쓰지 않고 5일 뒤에 Daily Roundup · task 기록으로 정리했다.
- README 링크 연결이 공개 뒤 5일 늦었다 — 공개한 날 바로 했어야 한다.

### Insights
- 코드 기반 영상은 한국어판 구조를 그대로 두고 영어판을 만들 수 있어 두 언어 공개 비용이 작다.

### Tomorrow's focus
- (Topic 완료) Muse 활용은 새 Topic Muse-My-Workflow 로 이어 간다.

## 📎 참조 및 산출물

- [06-Capstone-Video/README.md](../06-Capstone-Video/README.md) · [video-slide-plan.md](../06-Capstone-Video/video-slide-plan.md)
- [Topic 최종 회고](20261019_AI-Agent-Apps-Compare_Final_Retrospective.md)
