# VibeLearn AI Topic Starter — Tehaleh-Community-Video

---

## 📌 Topic 기본 정보

### Topic 이름

```
Topic 이름: Tehaleh-Community-Video
```

### Topic 설명

```
설명: 창발 Product Group 발표(2026-06-26) 오프닝 데모 영상 제작 Topic이다.
"AI로 이렇게 뚝딱 만들 수 있습니다"를 실증하기 위해, 사용자가 실제 거주 중인
Tehaleh 커뮤니티 소개 영상(2~3분)을 Remotion으로 제작하는 전 과정을 기록한다.
Phase 1(리서치) → Phase 2(슬라이드 플랜) → Phase 3(Remotion 영상) 3단계로 진행한다.
```

### 학습 목적

```
학습 목적:
- VibeLearn AI 방법론을 사용해 영상 제작 A to Z 과정을 체계적으로 기록한다.
- Tehaleh에 대한 정보를 AI 웹 검색으로 수집·구조화하는 리서치 역량을 쌓는다.
- video-slide-plan.md 작성 → Remotion 컴포넌트 개발 → MP4 렌더링 파이프라인을 완성한다.
- 발표 데모 녹화를 통해 "기록 + AI → 즉석 콘텐츠" 공식을 실제로 증명한다.
```

### 예상 학습 기간

```
예상 기간: 3~5시간 (1~2 세션)
```

---

## 🎯 학습 목표

```
- [ ] Tehaleh 기본 정보, 위치, IT 종사자·은퇴자 관점 리서치 문서 완성 (tehaleh-research.md)
- [ ] video-slide-plan.md (15~18슬라이드, ~150초) 확정 및 나레이션 스크립트 작성
- [ ] image-prompts.md 작성 완료 (AI 생성 이미지 프롬프트, no-text 규칙 적용)
- [ ] Remotion 컴포넌트 개발 완료 (TehalehIntro0619.tsx + 슬라이드 6종)
- [ ] edge-tts 오디오 생성 완료 (gen_audio.py, ko-KR-SunHiNeural, 1.10x)
- [ ] Qwen3-TTS 리뷰 후 최종 오디오 결정
- [ ] MP4 렌더링 완료 (tehaleh-intro-0619.mp4, 2~3분)
- [ ] 발표 데모 녹화 완료 (스크린 녹화 → 3~5분 편집본)
```

---

## 🛠️ 학습 환경

### 운영 체제

```
OS: Windows 11
```

### 주요 도구 및 기술 스택

```
- Claude Code (AI 에이전트, VS Code 확장)
- Remotion (C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\Remotion-VideoCreation\my-first-video\)
- edge-tts + gen_audio.py (TTS 초벌)
- Qwen3-TTS + gen_audio_qwen.py (TTS 최종)
- gpt-image-2 (AI 이미지 생성)
- OBS 또는 Windows 게임바 Win+G (스크린 녹화)
- PowerShell / VS Code
```

### 사전 지식

```
필수:
- Remotion 영상 제작 파이프라인 경험 (membership-promo-0614, live13-0607-summary 등)
- Tehaleh 실제 거주 경험 (정보 제공자 = 사용자 본인)
- edge-tts gen_audio.py 사용 경험

권장:
- ANIMATED_DARK 배경 테마 사용 경험
- gpt-image-2 이미지 생성 경험
- effects-library.md 참조 경험
```

---

## 📚 참조 자료

### 내부 자료

```
- vl_prompts/tehaleh-video-prompt.md — 메인 실행 프롬프트 (Phase 1~3 전체)
- Ingest/CatchUpAI_VL/Topics/Remotion-VideoCreation/my-first-video/ — Remotion 프로젝트
- Ingest/CatchUpAI_VL/Topics/Remotion-VideoCreation/my-first-video/src/membership-promo-0614/ — 재활용 참조 컴포넌트
- _Settings_/Skills/remotion-video/SKILL.md — Remotion 워크플로우 가이드
- _Settings_/Skills/remotion-video/effects-library.md — 효과 라이브러리
- Ingest/CatchUpAI_VL/Topics/The-AI-Powered-Creator/ — 부모 발표 Topic
```

### vl_materials/ 폴더에 추가할 자료

```
- tehaleh-research.md: Phase 1 리서치 결과 (위치·편의시설·IT종사자·은퇴자·한인커뮤니티)
```

---

## 🎓 학습 접근 방식

### 선호하는 학습 스타일

```
- [x] 실습 중심, 필요한 이론만 (영상 제작 실습 프로젝트)
```

### 시간 투자 계획

```
- 총 학습 시간: 3~5시간
- 1회당 학습 시간: 2~3시간
- 특이사항: 발표 전(2026-06-26) 완료 필요
```

### 특별히 집중하고 싶은 영역

```
- Phase 1 리서치 품질 (실제 거주 경험 + AI 검색 정보 결합)
- Phase 3 Remotion 시각 효과 (effects-library.md 최대 활용)
- 스크린 녹화 → 3~5분 편집 가능한 장면 구성
```

---

## 🚀 다음 단계

1. `vl_prompts/roadmap_prompt.md` 생성 (이 파일 정보로 플레이스홀더 채움)
2. `roadmap_prompt.md`를 AI에게 전달 → Roadmap 생성
3. `daily_learning_prompt.md`로 매일 학습 세션 진행
