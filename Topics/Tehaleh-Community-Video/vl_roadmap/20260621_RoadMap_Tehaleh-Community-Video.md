# Tehaleh-Community-Video 학습 로드맵

**생성일**: 2026-06-21
**방법론**: VibeLearn AI
**버전**: 1.0
**방법론 버전**: VibeLearn AI 2.0

## 학습 기간 적정성 분석

**사용자 입력 기간**: 3~5시간 (1~2 세션)
**Topic 복잡도**: 중간
**권장 기간**: 3~5시간

**분석 결과**: 적정하다. 이 Topic은 새로운 기술 학습이 아니라 기존 Remotion 파이프라인을 활용해 Tehaleh 소개 영상을 제작하는 실습 프로젝트다. Phase 1(리서치)과 Phase 2(슬라이드 플랜)는 비교적 빠르게 진행되며, Phase 3(Remotion 컴포넌트 개발)이 가장 많은 시간을 차지한다. 기존 영상(membership-promo-0614 등)의 컴포넌트를 재활용하면 Phase 3를 2시간 이내로 완료할 수 있다.

**조치 제안**: tehaleh-video-prompt.md의 3-Phase 구조를 그대로 따른다. 각 Phase 완료 시 사용자 승인을 받고 다음 단계로 진행한다.

## 학습 개요

### Topic 소개

`Tehaleh-Community-Video`는 창발 Product Group 발표(2026-06-26) 오프닝 데모 영상 제작 Topic이다. "AI로 이렇게 뚝딱 만들 수 있습니다"를 실증하기 위해, 사용자가 실제 거주 중인 Tehaleh 커뮤니티 소개 영상(2~3분)을 Remotion으로 제작한다. 전 과정을 스크린 녹화 후 3~5분으로 편집해 발표 오프닝 자료로 활용한다.

### 학습 목표

- [ ] Tehaleh 기본 정보·위치·IT종사자·은퇴자·한인커뮤니티 리서치 문서 완성
- [ ] video-slide-plan.md (15~18슬라이드, ~150초) 확정
- [ ] image-prompts.md 작성 완료 (AI 생성 이미지 프롬프트)
- [ ] Remotion 컴포넌트 개발 완료 (TehalehIntro0619.tsx)
- [ ] edge-tts 오디오 생성 완료 (gen_audio.py)
- [ ] Qwen3-TTS 리뷰 후 최종 오디오 결정
- [ ] MP4 렌더링 완료 (tehaleh-intro-0619.mp4)
- [ ] 발표 데모 녹화 완료 (3~5분 편집본)

### 예상 학습 기간

3~5시간 (1~2 세션)

### 학습 환경

- OS: Windows 11
- 도구: Claude Code, Remotion, edge-tts, Qwen3-TTS, gpt-image-2, OBS/게임바
- 사전 지식: Remotion 파이프라인 경험 (membership-promo-0614 등), Tehaleh 거주 경험

## 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 |
|------|--------|--------|-----------|--------|
| M0 | Topic 셋업 | ⭐ | 0.3h | topic_info.md, RoadMap.md, daily_learning_prompt.md |
| M1 | Tehaleh 리서치 | ⭐ | 0.5~1h | vl_materials/tehaleh-research.md |
| M2 | 영상 슬라이드 플랜 | ⭐⭐ | 0.5h | public/tehaleh-intro-0619/video-slide-plan.md |
| M3 | 이미지 프롬프트 | ⭐ | 0.3h | public/tehaleh-intro-0619/image-prompts.md |
| M4 | Remotion 컴포넌트 개발 | ⭐⭐⭐ | 1~1.5h | src/tehaleh-intro-0619/ |
| M5 | 오디오 생성 및 리뷰 | ⭐⭐ | 0.5h | audio/*.mp3, durations.json |
| M6 | MP4 렌더링 및 완성 | ⭐ | 0.2h | out/tehaleh-intro-0619.mp4 |

**총 예상 시간**: 3.3~4.3시간

## 모듈별 상세 계획

### M0 - Topic 셋업

**학습 목표**:
- CUA_VL 표준 폴더 구조 생성
- topic_info.md, RoadMap.md, daily_learning_prompt.md 작성

**DoD**:
- [x] 폴더 구조 생성 완료
- [x] tehaleh-video-prompt.md 이동 완료
- [ ] topic_info.md 작성 완료
- [ ] RoadMap.md 작성 완료 (이 파일)
- [ ] daily_learning_prompt.md 작성 완료

**예상 시간**: 20분

---

### M1 - Tehaleh 리서치

**학습 목표**:
- Tehaleh에 대한 6개 카테고리 정보를 웹 검색으로 수집
- 사용자의 실제 거주 경험과 공식 정보를 구분해 정리

**주요 수집 항목**:
1. 기본 정보 (위치, 개발사, 규모, 공식 웹사이트)
2. 위치 및 접근성 (Seattle/Bellevue/SeaTac 거리·시간)
3. 커뮤니티 특성 (주거 유형, 가격대, 편의시설, 학교)
4. IT 종사자 관점 (재택근무, 자연환경, 출퇴근, 가성비)
5. 은퇴자 관점 (안전, 액티브 라이프, 의료 접근성)
6. 한인/아시안 커뮤니티 (H마트, 한인 식당, 교회 접근성)

**DoD**:
- [ ] tehaleh-research.md 생성 (6개 섹션 완성)
- [ ] 출처 목록 포함
- [ ] 사용자 검토 및 승인

**산출물**: `vl_materials/tehaleh-research.md`
**예상 시간**: 30~60분

---

### M2 - 영상 슬라이드 플랜

**학습 목표**:
- tehaleh-research.md 기반으로 15~18슬라이드 구성
- 나레이션 스크립트 초안 작성 (한국어, 구어체)

**슬라이드 흐름**:
```
[TITLE] → [SECTION: 위치] → [STAT: 거리] → [SECTION: 커뮤니티]
→ [BULLET: 편의시설] → [BULLET: 가격] → [SECTION: IT종사자]
→ [BULLET: 재택] → [SECTION: 은퇴자] → [BULLET: 생활]
→ [QUOTE: 거주자 시점] → [OUTRO]
```

**DoD**:
- [ ] video-slide-plan.md 생성 (슬라이드별 타입·내용·시간)
- [ ] 나레이션 스크립트 초안 포함
- [ ] 총 예상 시간 ~150초 내외
- [ ] 사용자 검토 및 승인

**산출물**: `public/tehaleh-intro-0619/video-slide-plan.md`
**예상 시간**: 20~30분

---

### M3 - 이미지 프롬프트

**학습 목표**:
- 슬라이드별 AI 생성 이미지 프롬프트 작성
- 실제 거주자 촬영 사진 활용 슬라이드 명시

**DoD**:
- [ ] image-prompts.md 생성
- [ ] S0·S13·S14는 거주자 사진 사용 명시
- [ ] AI 생성 필요 슬라이드: 영어 프롬프트 + `no text` 규칙 적용

**산출물**: `public/tehaleh-intro-0619/image-prompts.md`
**예상 시간**: 15~20분

---

### M4 - Remotion 컴포넌트 개발

**학습 목표**:
- 기존 영상(membership-promo-0614 등) 컴포넌트 패턴 재활용
- ANIMATED_DARK 배경 테마 적용
- 최대한 시각 효과 활용 (effects-library.md 참조)

**DoD**:
- [ ] `src/tehaleh-intro-0619/data.ts` 생성
- [ ] `src/tehaleh-intro-0619/TehalehIntro0619.tsx` 생성
- [ ] `src/tehaleh-intro-0619/slides/` 6개 슬라이드 컴포넌트 완성
- [ ] `remotion.config.ts` 등록 완료
- [ ] 개발 서버 미리보기 확인

**산출물**: `src/tehaleh-intro-0619/`
**예상 시간**: 60~90분

---

### M5 - 오디오 생성 및 리뷰

**학습 목표**:
- edge-tts gen_audio.py로 초벌 오디오 생성
- Qwen3-TTS 교체 여부 결정

**DoD**:
- [ ] `gen_audio.py` 작성 (ko-KR-SunHiNeural, 1.10x)
- [ ] 슬라이드별 .mp3 생성 완료
- [ ] `durations.json` 생성 완료
- [ ] Qwen3-TTS 리뷰 후 결정
- [ ] `AUDIO_DURATIONS` 업데이트

**산출물**: `public/tehaleh-intro-0619/audio/`
**예상 시간**: 20~30분

---

### M6 - MP4 렌더링 및 완성

**학습 목표**:
- Remotion render 명령으로 최종 MP4 생성
- 영상 품질 확인 후 완성

**DoD**:
- [ ] `npx remotion render TehalehIntro0619` 성공
- [ ] `out/tehaleh-intro-0619.mp4` 생성 완료
- [ ] 영상 길이 2~3분 확인
- [ ] 발표 데모 녹화 준비 완료

**산출물**: `out/tehaleh-intro-0619.mp4`
**예상 시간**: 10~15분
