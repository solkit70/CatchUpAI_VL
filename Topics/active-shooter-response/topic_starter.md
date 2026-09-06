# VibeLearn AI Topic Starter - Active Shooter Response Training

## 📌 Topic 기본 정보

### Topic 이름
`active-shooter-response`

### Topic 설명
총기난사 사건 발생 시 일반 시민이 생명을 지키기 위한 대처 요령(DHS 자료 및 개인 교육 경험 기반)을 교육하고, 이를 효과적으로 알릴 수 있는 Remotion AI 기반 영상을 기획/제작하는 학습 과정.

### 학습 목적
- 미 국토안보부(DHS) 및 교육 자료의 핵심 행동 지침(Run, Hide, Fight 및 경찰 대응)을 체계적으로 정리하고 학습한다.
- 정리된 내용을 효과적으로 시각화하고 전달하기 위한 Remotion 동영상 발표용 슬라이드 플랜 및 나레이션 스크립트를 설계한다.
- React, TypeScript, Remotion 프레임워크 및 TTS 기술을 활용하여 자막과 음성이 싱크된 완성도 높은 교육 영상을 제작한다.
- 시민 단체 및 소외 계층에 도움이 될 수 있는 공익적 목적의 배포 자료를 구성한다.

### 예상 학습 기간
1주 (총 12~15시간)

---

## 🎯 학습 목표

- [ ] 총기난사 발생 시 3대 핵심 대응 수칙(Run, Hide, Fight)과 대처 흐름을 말로 명확히 설명할 수 있다.
- [ ] Remotion용 슬라이드 플랜(`video-slide-plan.md`) 및 지루하지 않은 감정 마커 나레이션 스크립트를 작성할 수 있다.
- [ ] Remotion 동적 효과(Spring, Stagger, Motion Blur 등)와 다양한 슬라이드 타입을 적용해 UI 컴포넌트를 설계할 수 있다.
- [ ] TTS 스크립트(`gen_audio.py` 및 `gen_audio_qwen.py`)를 활용해 완벽하게 패딩이 적용된 한국어 음성을 생성할 수 있다.
- [ ] 비디오 렌더링을 성공적으로 완료하여 시민 단체 등 필요한 곳에 바로 전파할 수 있는 최종 MP4 영상을 확보한다.

---

## 🛠️ 학습 환경

### 운영 체제
OS: Windows 11

### 주요 도구 및 기술 스택
- VS Code (Remotion 개발)
- Node.js (v18+)
- Python (v3.10+, edge-tts 및 Qwen-TTS 생성 스크립트 실행용)
- FFmpeg (오디오 패딩 및 싱크 확인용)
- Remotion Studio 4.0

### 사전 지식 (Prerequisites)
필수:
- 마크다운 기본 사용법 및 구조적 글쓰기
- 기본적인 React 컴포넌트 구조 이해

권장:
- TypeScript 기본 타이핑 개념
- FFmpeg CLI 기본 사용법

---

## 📚 참조 자료

### 관련 문서 및 파일 (Ingest/CatchUpAI_VL/Topics/active-shooter-response/vl_materials/ 에 배치됨)
- `미 국토안보부(DHS) 자료-총기난사 발생 시 대응요령(국문).pdf`
- `U.S. DHS-Active Shooter_How to Respond (English).pdf`

### 공식 튜토리얼 및 라이브러리
- Remotion 공식 문서: https://www.remotion.dev/
- Remotion Video Skill 지침: `_Settings_/Skills/remotion-video/SKILL.md`
- Remotion Effects Library: `_Settings_/Skills/remotion-video/effects-library.md`

---

## 🚀 다음 단계

이 파일 작성을 마친 후:
1. `vl_prompts/roadmap_prompt.md` 프롬프트 템플릿을 생성하고 Topic 기본 정보를 주입합니다.
2. `roadmap_prompt.md`를 바탕으로 상세 로드맵(`vl_roadmap/YYYYMMDD_RoadMap_active-shooter-response.md`)을 작성합니다.
3. `vl_prompts/daily_learning_prompt.md`를 생성합니다.
4. 사용자에게 최종 검토 및 승인을 요청한 후 일일 학습을 시작합니다.
