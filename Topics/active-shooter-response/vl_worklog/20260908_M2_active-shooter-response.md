---
title: "active-shooter-response M2 학습 일지 및 회고"
type: worklog
project: active-shooter-response
date: 2026-09-08
created: "2026-09-08 11:30:00"
tags:
  - active-shooter
  - worklog
  - retro
  - safety-training
  - video-storyboard
---

# WorkLog - M2: NGO 비상대응 자원이 반영된 비디오 슬라이드 기획

**날짜**: 2026-09-08  
**Topic**: `active-shooter-response`  
**모듈**: M2 - NGO 비상대응 자원이 반영된 비디오 슬라이드 기획 (v2.1 개정판)  
**이전 세션**: [[20260908_M1_active-shooter-response|20260908_M1_active-shooter-response (오늘 보강)]]  
**계획 문서**: [[Ingest/CatchUpAI_VL/Topics/active-shooter-response/vl_roadmap/20260908_RoadMap_active-shooter-response|20260908_RoadMap_active-shooter-response.md]]  

---

## 🎯 오늘의 학습 목표

- [x] M1에서 취합한 생존 지침과 **NGO 전문 교육 참여 방법(FEMA IS-907.A, CRASE) 및 단체 비상 자원(EAP, Stop the Bleed) 가이드를 포괄하는 12장 구성의 비디오 슬라이드 플랜(`video-slide-plan.md`)**을 기획한다.
- [x] 각 슬라이드에 어울리는 visual 에셋 매핑을 정의하는 `image-prompts.md` 명세서를 도출한다.
- [x] 다중 슬라이드 템플릿(Title, Run-Hide-Fight, Training, NGO-Safety-Kit, Outro)에 전달될 정교한 데이터 구조인 `data.ts`를 정의한다.

---

## 📝 진행 내용 및 증적

### 1. 실습 1: `video-slide-plan.md` 12장 스토리보드 및 감정 마커 대본 수립
*   **파일**: `02-Remotion-Setup/video-slide-plan.md`
*   **수행 내용**:
    *   FEMA 전문 안전 교육 카드 장표(Slide 10) 및 시민단체의 EAP/Tabletop/지혈대 3열 그리드 카드 장표(Slide 11)를 신설 배치하여 총 12장의 긴박감 넘치는 공익 안전 교육 스토리보드를 집필 완료했습니다.
    *   성우의 목소리에 극적 리얼리즘을 불어넣기 위해 문단마다 `[SERIOUS]`, `[URGENT]`, `[COMPOSED]`, `[RESOLVE]` 감정 마커를 배치하였습니다.

### 2. 실습 2: `image-prompts.md` 자기완결 프롬프트 명세 도출
*   **파일**: `02-Remotion-Setup/image-prompts.md`
*   **수행 내용**:
    *   영상의 미학적 완성도를 위해 `L2`(밝음)에서 `L4`(완전 침묵 소등실)에 이르기까지 밝기 지수(Scale)를 하드코딩하여 명문화했습니다.
    *   Midjourney/DALL-E 3가 문자열 깨짐을 생성하지 못하도록 `no text`, `no letters` 등 네거티브 지침을 완결성 있게 부여했습니다.

### 3. 실습 3: `data.ts` TypeScript 공용 데이터 테이블 코딩
*   **파일**: `02-Remotion-Setup/data.ts`
*   **수행 내용**:
    *   새 12장 스토리보드의 본문 불렛과 강조 토큰들을 객체 배열 형식으로 에러 없이 코딩했습니다.
    *   **FEMA 파란색 강조 컬러 토큰(`#1890ff`, `fema`)을 신설**하여 디자인 시스템 일체화를 획득했습니다.
    *   폴더명과 가상 렌더링 파일 아키바링을 v2.1에 걸맞게 `active-shooter-0908`로 완전 교체하였습니다.

---

## 🛠️ Definition of Done (DoD) 체크리스트

- [x] `video-slide-plan.md` 작성이 완료되고, FEMA 온라인 교육 및 NGO 비상 자원 가이드 슬라이드가 각각 1장 이상 독립 구성됨.
- [x] `image-prompts.md`에 신뢰성 높은 배경 이미지 생성을 위한 고품질 프롬프트 작성 완료.
- [x] `data.ts`에 슬라이드 렌더링을 제어하기 위한 구조화된 객체 배열이 타이핑 에러 없이 작성됨.
- [x] `02-Remotion-Setup/README.md` 가독성 정리 및 레거시 관계 명시 완료.
- [x] WorkLog 및 Daily Retrospective 작성 완료.

---

## 🔍 Daily Retrospective (회고)

### 1. What went well? (성취한 점)
*   사용자님의 승인 및 지시 직후, M1에서 발굴한 NGO 특화 데이터들(FEMA, Tabletop 모의 도상 훈련, Stop the Bleed)이 visual 형태로 흐르며 **영상의 마지막 3분을 가장 가치 있는 정보 마케팅 장표로 빛낼 수 있도록 12장 스토리보드를 극적으로 수립**했습니다.
*   Typescript 데이터 토큰(`fema` 컬러) 및 데이터 구조(`data.ts`)까지 설계해 둠으로써 차후 React 렌더링 컴포넌트 이식이 한층 간결하고 안정적으로 진행될 뼈대를 세웠습니다.

### 2. What could be improved? (개선할 점)
*   Remotion의 기존 SlideType(`title`, `section`, `bullet`, `compare`, `quote`, `stat`, `outro`) 프레임 범주를 완전히 파괴하지 않으면서 FEMA와 NGO Kit 카드 3열을 그릴 수 있는 방법을 궁리할 때, 처음에는 새로운 SlideType을 무수히 기획하려다 구현 복잡도를 대폭 줄이기 위해 `compare` 및 `bullet` 타입을 영리하게 활용하여 schema 결합력을 유지했습니다. 앞으로도 컴포넌트의 단순성을 우선해야겠습니다.

### 3. Insights (본질적 통찰)
*   **"설계가 선언적일수록 개발은 선형적으로 단순해진다."** `data.ts`에 12장 슬라이드의 텍스트와 강조 속성이 완벽히 타입 가드 형태로 규격화되어 있으면, 차후 오디오 재생 시간 durations 매핑과 React DOM 그리기는 단순히 매칭 루프를 돌리는 단순한 조립 작업으로 전환됨을 깊이 깨달았습니다.

---

## 🚀 Tomorrow's Focus (다음 학습 목표)

*   **모듈 M3(모션 애니메이션 컴포넌트 및 배경 개발) 시작**:
    *   `03-Remotion-Development/` 폴더를 가동하고, `AI/RemotionStudio/src/active-shooter-0908/` 개발 환경에 React 슬라이드 렌더러 컴포넌트를 구축합니다.
    *   특히 Slate Charcoal 테마의 `SlateDotsBackground` 컴포넌트 및 3열 카드가 spring 기반으로 stagger 팝업되는 `SlideTraining` 등 특화 렌더러 구현에 돌입합니다.
