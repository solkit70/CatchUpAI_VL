# Module 2 (M2) - Remotion 프로젝트 구성 및 슬라이드 기획

*   **모듈 번호**: M2
*   **모듈 제목**: Remotion 프로젝트 구성 및 슬라이드 기획
*   **상태**: ✅ 완료 (Completed)
*   **예상 학습 시간**: 3.0시간 (실제 소요: 약 2.5시간)

---

## 📖 모듈 소개 및 학습 안내

본 모듈에서는 앞서 설계된 M1의 디자인 콘셉트(L3 Slate Charcoal 대역, 첫 30초 후킹 멘트 등)를 기반으로 Remotion 비디오의 실제 기술 구조(정적 정의 파일)를 생성하고, 영상 전반에 녹아들 상세 슬라이드 흐름 및 이미지 생성 프롬프트를 완전 설계하였습니다.

이 폴더에 포함된 모든 문서는 아래 **학습 순서**에 따라 구조화되어 있습니다. 순서대로 읽고 다음 단계(M3 컴포넌트 개발)로 전이하시기 바랍니다.

---

## 🗂️ 학습 산출물 및 문서 목록 (학습 순서순)

1.  **비디오 슬라이드 전체 구조 기획안**
    *   **링크**: [video-slide-plan.md](video-slide-plan.md)
    *   **설명**: 10장으로 구성된 동영상의 전체 흐름, 각 장의 슬라이드 타입(`TITLE`, `BULLET`, `COMPARE`, `QUOTE`, `STAT` 등), 비주얼 배치 계획, 자막 및 나레이션 스크립트를 정밀하게 수립한 비디오 설계도입니다.
2.  **AI 이미지 생성용 프롬프트 명세서**
    *   **링크**: [image-prompts.md](image-prompts.md)
    *   **설명**: Remotion Video Skill의 「자기완결 프롬프트 원칙」에 입각하여 Slide 03(Run), Slide 05(Fight), Slide 07(Police)용 고품질 이미지를 생성할 수 있는 Midjourney / DALL-E 3 전용 프롬프트를 정의한 기술 명세서입니다.
3.  **Remotion 데이터 정의 파일**
    *   **링크**: [data.ts](data.ts)
    *   **설명**: Remotion 리액트 렌더러가 데이터를 읽고 자동으로 총 러닝타임(Total Frames), 슬라이드 높이, 트랜지션, 색상 팔레트 및 오디오 durations를 산출할 수 있도록 데이터 구조를 구현한 TypeScript 공용 데이터 원장입니다.

---

## 🔄 모듈 이동 및 진행 상황

*   **이전 모듈**: [[../01-DHS-Analysis/README|M1 - 안전 지침 분석 및 핵심 메시지 도출]]
*   **다음 모듈**: `M3 - Remotion 컴포넌트 개발 및 동적 연출` (산출물 폴더: `03-Remotion-Development/` 대기 중)
*   **전체 학습 계획**: [[../vl_roadmap/20260906_RoadMap_active-shooter-response|active-shooter-response 학습 로드맵]]
