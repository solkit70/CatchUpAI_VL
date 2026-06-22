---
title: Tehaleh-Community-Video
created: 2026-06-22 12:17:07
completed: 2026-06-22
status: completed
methodology: VibeLearn AI
tags:
  - cua-vl
  - vibelearn-ai
  - remotion
  - tehaleh
  - presentation-demo
---

# Tehaleh-Community-Video

Tehaleh 지역 소개 영상을 AI와 Remotion으로 제작한 전 과정을 기록하는 Topic이다. 지역 리서치부터 슬라이드 구성, 이미지 준비, 한국어·영어 나레이션 생성, 영상 렌더링과 YouTube 업로드 메타데이터 작성까지 하나의 실제 콘텐츠 제작 사례로 관리한다.

## 상위 발표 프로젝트

이 영상은 창발(Changbal) Product Group의 온라인 이벤트 `[Product 그룹] The AI Powered Creator` 발표에서 사용할 샘플 영상으로 제작했다. 발표에서는 완성 영상과 제작 과정을 통해 기록이 AI의 Context가 되고, Context가 리서치·스크립트·이미지·나레이션·영상 제작을 연결하는 방식을 보여준다.

- 발표 준비 Topic: [The-AI-Powered-Creator](../The-AI-Powered-Creator/README.md)
- 행사명: `[Product 그룹] The AI Powered Creator`
- 행사 부제: `AI 시대에 컨텐츠 제작하기: Video, Social Media, and Blogging`
- 행사 일시: 2026년 6월 26일 금요일 오후 7:00–8:00
- 행사 형식: Google Meet 온라인 발표, 등록 후 접속 링크 제공
- 공식 행사 정보 및 등록: [Changbal — The AI Powered Creator](https://www.changbal.org/en/event-info/product-geulub-the-ai-powered-creator)

### 공식 행사 소개

> Agentic Coding, Vibe Coding 덕분에 누구나 쉽게 프로덕트를 만들 수 있는 시대가 되었습니다. 이제는 만드는 것보다 '어떻게 유저에게 도달할 것인가(Distribution)'가 더 중요한 차별점이 되었는데요. 수많은 서비스 홍수 속에서 내 콘텐츠와 제품을 돋보이게 만드려면 컨텐츠를 만드는것이 필수가 되었습니다.

> 이번 창발 프로덕 그룹 모임에서는 베테랑 엔지니어에서 AI 엔지니어로, 그리고 이제는 AI 크리에이터(유튜브/블로그)로 계시는 창수님을 모셨습니다! AI를 도구 삼아 직접 AI 콘텐츠를 기획하고 제작해 온 창수님만의 리얼한 경험담을 이번 기회에 꼭 만나보세요.

## 영상 내용과 역할

영상은 실제 거주자의 관점에서 워싱턴주 Tehaleh 커뮤니티를 소개한다. Post & Pour에서 직접 촬영한 레이니어 산 사진, 커뮤니티 시설과 트레일, 주택 가격, 재택·하이브리드 근무, 은퇴 생활과 인근 한인 생활권을 다루며 한국어와 영어 두 버전으로 완성했다. 발표에서는 이 결과물을 AI 콘텐츠 제작 워크플로우의 실증 사례이자 오프닝 데모로 사용한다.

## 최종 산출물

| 산출물 | 상태 | 위치 |
|--------|------|------|
| 한국어 영상 | 공개 완료 | [YouTube](https://youtu.be/Cucvcz9bVPU) |
| 영어 영상 | 공개 완료 | [YouTube](https://youtu.be/YygPvJbKPvU) |
| 한국어 로컬 렌더 | 완료 | `out/tehaleh-intro-0619.mp4` |
| 영어 로컬 렌더 | 완료 | `out/tehaleh-intro-0619-en.mp4` |
| YouTube 배포 메타데이터 | 완료 | [WorkLog의 YouTube 업로드 메타데이터](vl_worklog/20260621_M1-M4_Tehaleh-Community-Video.md#youtube-업로드-메타데이터) |
| Topic Final Retrospective | 완료 | [20260622 Final Retrospective](vl_worklog/20260622_Tehaleh-Community-Video_Final_Retrospective.md) |

로컬 렌더는 1920×1080, 30fps로 검증했다. 초기 90~150초 길이 목표는 리서치 내용과 실제 거주 경험을 충분히 전달하기 위해 확장했으며, 이 범위 변경과 품질 평가는 Final Retrospective에 기록했다.

## 시작하기

1. [topic_starter.md](topic_starter.md) — Topic 목적, 학습 목표와 제작 범위
2. [vl_materials/tehaleh-research.md](vl_materials/tehaleh-research.md) — Tehaleh 지역 리서치
3. [vl_roadmap/20260621_RoadMap_Tehaleh-Community-Video.md](vl_roadmap/20260621_RoadMap_Tehaleh-Community-Video.md) — 영상 제작 로드맵
4. [vl_worklog/20260621_M1-M4_Tehaleh-Community-Video.md](vl_worklog/20260621_M1-M4_Tehaleh-Community-Video.md) — 제작 과정, 최종 렌더 정보와 YouTube 메타데이터
5. [vl_worklog/20260622_Tehaleh-Community-Video_Final_Retrospective.md](vl_worklog/20260622_Tehaleh-Community-Video_Final_Retrospective.md) — Topic 완료 평가, Self-Assessment와 다음 프로젝트 개선안

## 제작 위치

Remotion 소스, 이미지, TTS 스크립트와 렌더 결과는 로컬 `Topics/Remotion-VideoCreation/my-first-video/` 프로젝트에서 관리한다. 이 디렉터리는 빌드 의존성과 대용량 미디어를 포함하므로 `CatchUpAI_VL` 저장소의 `.gitignore` 정책에 따라 GitHub에는 포함하지 않는다.
