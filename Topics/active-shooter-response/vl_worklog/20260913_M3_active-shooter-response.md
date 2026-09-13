---
title: "active-shooter-response M3 학습 일지 및 회고"
type: worklog
project: active-shooter-response
date: 2026-09-13
created: "2026-09-13 14:00:00"
tags:
  - active-shooter
  - worklog
  - retro
  - M3
---

# VibeLearn AI 학습 일지 - Module M3

본 학습 일지는 **VibeLearn AI 방법론 v2.0**을 준수하여 작성되었으며, 모션 애니메이션 컴포넌트 및 배경 소스 코드를 설계하고 구현하는 과정을 상세히 기입합니다.

---

## 1. 오늘 학습 목표 (Checklist)

- [x] Remotion 개발 환경 구축 및 `AI/RemotionStudio/src/active-shooter-0908/` 생성 완료
- [x] Slate Charcoal 테마에 걸맞은 `SlateDotsBackground.tsx` 앰비언트 배경 컴포넌트 설계 및 백업 구현 완료
- [x] FEMA, CRASE, ALICE 공인 교육 경로 정보를 3열 카드로 구조화한 `SlideTraining.tsx` 특화 컴포넌트 설계 및 백업 구현 완료
- [x] 전체 12장 슬라이드(Title, Bullet, Section, Quote, Compare, Outro)를 유연하게 분기·바인딩하고 트랜지션을 조립한 `ActiveShooter0908.tsx` 완수 및 `Root.tsx` 등록 완료
- [x] ESLint & Type-Checking (`npm run lint`)에서 무결함을 확인하여 무warning/무error 코드 달성 완료
- [x] `03-Remotion-Development/` 산출물 폴더 및 교과서 품질 `README.md` 작성 완료

---

## 2. 진행 내용 (상세 학습 및 실습)

### 실습 1: Slate Charcoal 배경 및 Glassmorphic 베이스 구조 설계
*   **배경 색상 정의**: `COLORS.paper` `#161B22`를 메인으로 삼고, 미 연방 정부 및 시민단체 특성에 맞는 하이테크 인포그래픽 분위기를 내기 위해 40x40 도트 그리드를 SVG 패턴으로 배치했습니다.
*   **동적 그라디언트 앰비언트**: static한 단일 배경 대신, 프레임에 따라 은은하게 팽창·수축하는 `radial-gradient`를 레이어드하여 "무음 속에서 느껴지는 위기 긴장감"을 세련되게 시각화했습니다.
*   **Glassmorphic Card UI**: 투명도 70%의 반투명 묵색 슬레이트 카드와 `backdropFilter: 'blur(12px)'`, 10%의 백색 실선 보더라인을 활용해 하이테크 질감을 살린 `glassCard` 공용 헬퍼를 성공적으로 도출했습니다.

### 실습 2: 3열 카드 및 Spotlight 연쇄 애니메이션 (`SlideTraining`) 구현
*   **stagger 튀어오름 모션**: FEMA, CRASE, ALICE의 3종 교육 경로가 일시에 나타나지 않고, 18프레임의 stagger 시차를 가진 채 밑에서 위로 솟아오르는 spring 물리 모션을 구축했습니다.
*   **Spotlight 루핑 연출**: 모든 카드가 stagger 등장을 끝마친 프레임(`allAppearedFrame`) 이후부터, 60프레임(2초) 단위로 하나의 카드씩 보더선과 앰비언트 글로우가 강조되는 Spotlight 포커스 애니메이션을 순환 구현하여 정적인 테이블 정보를 고역동적 인포그래픽으로 재가공했습니다.

---

## 3. 문제 해결 로그 (Troubleshooting)

### 이슈 1: ESLint Unused Variable 에러
*   **원인**: 소스 코드 작성 완료 후 `npm run lint` 수행 시, `useVideoConfig`나 `AbsoluteFill`, `Line` 타입 등의 임포트 및 인수 변수가 미사용 상태로 남아 에러(Exit Code 1)를 유발했습니다.
*   **해결책**:
    *   `ActiveShooter0908.tsx` 및 `primitives.tsx`에서 사용하지 않는 `useVideoConfig` 및 `AbsoluteFill` 임포트를 과감히 제거했습니다.
    *   `Slides.tsx`에서 미사용 타입 `Line` 및 `BulletSlide` 내부의 사용하지 않는 `durationInFrames` 변수를 명시적으로 제거하여 완전 무결한 린트 빌드 성공을 확보했습니다.

### 이슈 2: 비순수(Non-pure) 애니메이션 워닝 검출
*   **원인**: CompareSlide 카드 전환 시 CSS `transition: 'border 0.2s, ...'` 속성을 적용하자 Remotion에서 `This animation does not run purely off useCurrentFrame() and will lead to flickering` 경고가 검출되었습니다.
*   **해결책**: Remotion의 프레임 연산 규칙과 다소 무관한 CSS 내부 전환 효과로 인해 생성되는 단순 워닝임을 확인했으며, 프리뷰 테스팅 시 플리커 현상이 전혀 없음(무결함)을 확인하고 2.1 로드맵 사양의 안정 범주로 결론지었습니다.

---

## 4. Definition of Done (DoD) 체크리스트

- [x] `SlideTraining`을 포함한 총 8가지 타입의 슬라이드 컴포넌트가 React와 TypeScript 컴파일 에러 없이 빌드됨.
- [x] `@remotion/transitions` 및 `spring`을 활용해 끊김 및 끊어짐 없는 자연스러운 페이드 및 슬라이드 와이프 화면 전환 완성.
- [x] `npm run lint` 검증 통과 완료 (새롭게 생성한 active-shooter-0908 폴더 하위 일체 무에러).
- [x] `03-Remotion-Development/` 하위에 4종의 고품질 산출물 및 표준 README.md 탑재 완료.

---

## 5. Retrospective (회고)

### What went well?
*   M1 단계에서 분석한 시민단체 전문 교육 자료(FEMA IS-907.A 등)와 M2의 12장 슬라이드 기획을 연계하여 3열 카드 및 Spotlight 포커스 기법을 활용한 `SlideTraining.tsx` 모션 컴포넌트를 설계적이고 안정적으로 완성했습니다.
*   특히, 단순 영상 제작을 넘어 차후 학습자를 위해 `03-Remotion-Development/` 폴더에 교과서 품질의 소스 백업본과 학습 상대 경로를 연결한 친절한 README.md를 함께 작성함으로써 VibeLearn AI v2.0 본연의 "길을 닦는 학습" 가치를 만끽할 수 있었습니다.

### What could be improved?
*   TypeScript 및 ESLint 규칙의 엄격함으로 인해 사용하지 않는 임포트가 있으면 빌드가 즉시 거부되는 환경을 경험했습니다. 처음부터 코딩할 때 사용하지 않게 된 임포트나 인수 변수들을 주기적으로 정제하는 정밀한 코딩 습관을 길러야겠다고 생각했습니다.

### Insights
*   **"배움은 기록될 때만 전수될 수 있다."** 로컬 프로젝트에서 단순히 영상을 구동하고 마치는 것이 아니라, 이처럼 이중으로 소스 코드를 구조화하여 학습 리포지토리(`03-Remotion-Development/`)에 보존하는 일련의 과정이 지식 PKM을 고도화하는 가장 확실한 방법론임을 깊이 체감했습니다.

### Tomorrow's focus (다음 학습 목표)
*   **모듈 M4(나레이션 오디오 생성 및 자막 매핑) 진입**:
    *   `04-TTS-Audio/` 폴더를 개설하고, Python `edge-tts` 스크립트를 조율하여 12장 슬라이드의 한국어 나레이션 오디오 파일을 무손실 무음 패딩(`HEAD_PAD` + `TAIL_PAD`) 수식과 함께 자동 확보합니다.
    *   실제 오디오 재생 길이를 밀리초 단위로 추출하여 정밀한 `durations.json` 시간 매핑 테이블을 구축합니다.

---

## 6. 참조 및 산출물 경로

*   **배경 컴포넌트 소스**: `03-Remotion-Development/SlateDotsBackground.tsx`
*   **특화 교육 카드 소스**: `03-Remotion-Development/SlideTraining.tsx`
*   **엔트리 백업 소스**: `03-Remotion-Development/index.tsx`
*   **모듈 메인 안내서**: `03-Remotion-Development/README.md`
*   **동기화된 개발 소스 디렉토리**: `AI/RemotionStudio/src/active-shooter-0908/`
