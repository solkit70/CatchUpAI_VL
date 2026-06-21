# VibeLearn AI Roadmap 생성 프롬프트

**버전**: 2.0
**생성일**: 2026-06-21
**방법론**: VibeLearn AI
**템플릿 출처**: `Ingest/CatchUpAI_VL/templates/roadmap_prompt_template.md`

---

## 📌 사용 방법

이 프롬프트는 Topic 정보를 바탕으로 학습 로드맵을 자동 생성합니다.

**사용 절차**:
1. Topic 정보가 이미 주입된 상태
2. 이 파일 전체를 AI에게 전달
3. AI가 VibeLearn AI 표준 로드맵 생성
4. 생성된 로드맵을 `vl_roadmap/YYYYMMDD_RoadMap_{Topic}.md`에 저장

---

## [1단계] Topic 정보 (자동 주입됨)

### 기본 정보

**Topic 이름**: `Tehaleh-Community-Video`

**Topic 설명**:
```
창발 Product Group 발표(2026-06-26) 오프닝 데모 영상 제작 Topic이다.
"AI로 이렇게 뚝딱 만들 수 있습니다"를 실증하기 위해, 사용자가 실제 거주 중인
Tehaleh 커뮤니티 소개 영상(2~3분)을 Remotion으로 제작하는 전 과정을 기록한다.
Phase 1(리서치) → Phase 2(슬라이드 플랜) → Phase 3(Remotion 영상) 3단계로 진행한다.
```

**학습 목적**:
```
- VibeLearn AI 방법론을 사용해 영상 제작 A to Z 과정을 체계적으로 기록한다.
- Tehaleh에 대한 정보를 AI 웹 검색으로 수집·구조화하는 리서치 역량을 쌓는다.
- video-slide-plan.md 작성 → Remotion 컴포넌트 개발 → MP4 렌더링 파이프라인을 완성한다.
- 발표 데모 녹화를 통해 "기록 + AI → 즉석 콘텐츠" 공식을 실제로 증명한다.
```

**예상 학습 기간**: `3~5시간 (1~2 세션)`

---

### 환경 및 사전 지식

**운영 체제**: `Windows 11`

**주요 도구 및 기술 스택**:
```
- Claude Code (AI 에이전트)
- Remotion (Ingest/CatchUpAI_VL/Topics/Remotion-VideoCreation/my-first-video/)
- edge-tts / Qwen3-TTS (gen_audio.py)
- gpt-image-2 (이미지 생성)
- OBS 또는 Windows 게임바 (스크린 녹화)
- PowerShell / VS Code
```

**사전 지식**:
```
필수:
- Remotion 영상 제작 파이프라인 경험 (membership-promo-0614 등 기존 영상 참조)
- Tehaleh 실제 거주 경험 (정보 제공자 = 사용자 본인)
- edge-tts gen_audio.py 사용 경험

권장:
- ANIMATED_DARK 배경 테마 사용 경험
- gpt-image-2 이미지 생성 경험
- Remotion effects-library.md 참조 경험
```

---

### 산출물 및 참조

**학습 목표** (달성하고 싶은 것):
```
- [ ] Tehaleh 기본 정보, 위치, IT 종사자·은퇴자 관점 리서치 문서 완성
- [ ] video-slide-plan.md (15~18슬라이드, ~150초) 확정
- [ ] image-prompts.md 작성 완료 (AI 생성 이미지 프롬프트)
- [ ] Remotion 컴포넌트 개발 완료 (TehalehIntro0619.tsx)
- [ ] edge-tts 오디오 생성 완료 (gen_audio.py)
- [ ] Qwen3-TTS 리뷰 후 최종 오디오 결정
- [ ] MP4 렌더링 완료 (tehaleh-intro-0619.mp4)
- [ ] 발표 데모 녹화 완료 (3~5분 편집본)
```

**참조 자료**:
```
- vl_prompts/tehaleh-video-prompt.md — 메인 실행 프롬프트 (Phase 1~3 전체)
- Ingest/CatchUpAI_VL/Topics/Remotion-VideoCreation/my-first-video/ — Remotion 프로젝트
- Ingest/CatchUpAI_VL/Topics/Remotion-VideoCreation/my-first-video/src/membership-promo-0614/ — 재활용 컴포넌트
- _Settings_/Skills/remotion-video/SKILL.md — Remotion 워크플로우 가이드
- _Settings_/Skills/remotion-video/effects-library.md — 효과 라이브러리
```

**vl_materials/ 폴더**:
```
- tehaleh-research.md: Tehaleh 기본 정보·위치·커뮤니티·IT종사자·은퇴자·한인커뮤니티 리서치
```

**Remotion 산출물 경로**:
```
Video ID: tehaleh-intro-0619
Composition ID: TehalehIntro0619
배경 스타일: ANIMATED_DARK
TTS: edge-tts ko-KR-SunHiNeural → Qwen3-TTS 교체 여부 결정
슬라이드 플랜: public/tehaleh-intro-0619/video-slide-plan.md
오디오: public/tehaleh-intro-0619/audio/
이미지: public/tehaleh-intro-0619/images/
컴포넌트: src/tehaleh-intro-0619/
렌더링: out/tehaleh-intro-0619.mp4
```

---

## [2단계] AI에게 요청할 작업

위에 주입된 Topic 정보를 바탕으로 **VibeLearn AI 방법론**에 맞는 학습 로드맵을 생성해주세요.

---

### 🔍 STEP 1: 학습 기간 적정성 검토 (필수)

사용자가 입력한 학습 기간 `3~5시간`이 해당 Topic에 적절한지 분석하고 피드백을 제공하세요.

#### 분석 기준:
1. **Topic 복잡도 평가** — 기술 학습이 아닌 영상 제작 실습 프로젝트
2. **사전 지식 고려** — Remotion 파이프라인 기존 경험 보유
3. **학습 목표 범위** — 완성 영상(MP4) 산출물 중심

피드백 형식:
```markdown
## 📊 학습 기간 적정성 분석
**사용자 입력 기간**: 3~5시간
**Topic 복잡도**: [간단/중간/복잡]
**권장 기간**: [X시간]
**분석 결과**: ...
**조치 제안**: ...
```

**중요**: 사용자가 확인하고 최종 결정할 때까지 로드맵 생성을 중단하고 대기하세요.

---

### 🗺️ STEP 2: 로드맵 생성 요구사항

사용자가 기간을 최종 확정한 후 아래 요구사항에 따라 로드맵을 생성하세요.

#### 전체 구조

이 Topic은 영상 제작 실습 프로젝트이므로 모듈 = 제작 Phase:
- **M0**: Topic 셋업
- **M1**: Tehaleh 리서치 (Phase 1)
- **M2**: 영상 슬라이드 플랜 (Phase 2)
- **M3**: 이미지 프롬프트 작성 (Phase 3a)
- **M4**: Remotion 컴포넌트 개발 (Phase 3b~c)
- **M5**: 오디오 생성 및 리뷰 (Phase 3d~e)
- **M6**: MP4 렌더링 및 완성 (Phase 3f)

#### 각 모듈 필수 포함 사항 (9가지)

1. 모듈 기본 정보 (난이도, 예상 시간, 산출물 폴더)
2. 학습 목표 3-5개 (체크리스트, 검증 가능)
3. 주요 개념 3-5개 (정의 + 설명)
4. 실습 과제 2-3개 (목적·단계·시간·검증 방법 포함)
5. 산출물 (폴더 구조, 필수 파일)
6. Definition of Done (체크리스트 5-8개)
7. Self-Assessment (개념 이해·실무 활용 각 2-3문항)
8. 예상 시간 배분 (버퍼 20% 포함)
9. 참조 자료 (경로 또는 링크)

#### 실습 설계 원칙

- 실습 우선 (70-80% 실습, 20-30% 이론)
- 검증 가능한 결과 (파일 생성, 렌더링 성공 등)
- Windows 환경 명령어 사용 (PowerShell)
- 기존 컴포넌트 재활용 패턴 명시

#### VibeLearn AI 방법론 통합

로드맵에 다음 항목을 포함:
- WorkLog 작성 가이드 (`vl_worklog/YYYYMMDD_MX_Tehaleh-Community-Video.md`)
- Retrospective 가이드 (Daily / Module / Topic 3단계)
- 전체 폴더 구조
- 학습 진행 상황 추적 테이블 (M0~M6)
- 성공 기준 (전체 Topic 완료 기준)

---

## [3단계] 출력 형식

다음 형식으로 로드맵을 생성하고 아래 경로에 저장:
```
vl_roadmap/20260621_RoadMap_Tehaleh-Community-Video.md
```

절대 경로:
```
C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\Tehaleh-Community-Video\vl_roadmap\20260621_RoadMap_Tehaleh-Community-Video.md
```

### 로드맵 템플릿 구조

```markdown
# Tehaleh-Community-Video 학습 로드맵

**생성일**: 2026-06-21
**방법론**: VibeLearn AI
**버전**: 1.0

## 학습 기간 적정성 분석
## 학습 개요
  ### Topic 소개
  ### 학습 목표
  ### 예상 학습 기간
  ### 학습 환경
## 전체 로드맵 구조 (표)
## 모듈별 상세 계획
  ### M0 ~ M6 (각 9가지 항목 포함)
## WorkLog 작성 가이드
## Retrospective 가이드
## 전체 폴더 구조
## 학습 진행 상황 추적 테이블
## 성공 기준
```

---

## ✅ 로드맵 품질 체크리스트

- [ ] 학습 기간에 맞는 모듈 개수 (7개: M0~M6)
- [ ] 각 모듈 9가지 필수 항목 모두 포함
- [ ] WorkLog 가이드 포함
- [ ] Retrospective 가이드 (3단계) 포함
- [ ] 학습 진행 상황 추적 테이블 포함
- [ ] 성공 기준 포함
- [ ] vl_roadmap/ 경로에 저장 완료
- [ ] 사용자 검토 요청

---

**생성자**: Claude with VibeLearn AI
**Template 버전**: 2.0
**생성일**: 2026-06-21
**방법론**: VibeLearn AI
