---
title: "조사 카드 — Remotion: 인트로·자막·반복 템플릿"
author:
  - "Codex"
created: 2026-10-24 22:52:50
source: "https://www.remotion.dev/docs"
tags:
  - ai-event-video-editing
  - research-card
---

## 요약

**범주 E · 확인일 2026-10-24 · 자료로만 / 이번 Topic 실습 안 함.** 코드로 영상과 그래픽을 조립하는 후보이며, 장면을 이해해 알아서 선별하는 모델과 구분한다. 인트로·자막·로고를 행사마다 반복하는 템플릿에 적합할 가능성이 있다는 조사자 판단이다.

## 기능·언어·한도

[영상 삽입 문서](https://www.remotion.dev/docs/videos/)는 시작 구간·프레임 길이·배치를, [매개변수 문서](https://www.remotion.dev/docs/parameterized-rendering)는 행사명·날짜처럼 입력값으로 콘텐츠를 바꾸는 구조를 안내한다. [자막 문서](https://www.remotion.dev/docs/captions/)는 SRT/VTT 가져오기와 자막 출력 경로를 안내한다. 어떤 장면을 쓸지는 사람이 정하거나 별도 분석을 연결해야 한다.

한국어 문구·폰트·줄바꿈과 렌더 결과는 실제 확인이 필요하다. 고정 SaaS 업로드 한도가 있는 후보가 아니며, 로컬 렌더와 클라우드 렌더의 자원·비용·미디어 위치는 구분한다. 출력 영상을 Premiere로 가져오는 것과 소스 코드의 텍스트·효과가 Premiere 요소로 넘어가는 것은 다르다.

## 비용과 라이선스

> “free to use for individuals and companies up to three people”
> — [Remotion 공식 라이선스 페이지](https://www.remotion.pro/license), 2026-10-24 확인

공식 페이지는 개인·3명 이하 회사의 Free License와, 협업 및 4명 이상 회사의 Company License 조건을 구분한다. Company License에는 Creators 월 $25/좌석, Automators 렌더당 $0.01·최소 월 $100이 안내되어 있다. **의뢰인 조직과 협업 형태가 미확인이므로 무료 사용 가능하다고 확정하지 않는다.** 외부 렌더·AI·폰트·음악 비용도 별도다.

## 이 Topic에서의 판단

짧은 인트로와 반복 템플릿의 비교 후보로 두고, 긴 영상 장면 선택은 다른 도구와 조합한다. [공식 시작 안내](https://www.remotion.dev/docs)는 코딩 에이전트 경로와 ChatGPT 데스크톱 플러그인 경로를 소개하지만, 이번에 플러그인을 설치하거나 사용 가능 여부를 확인한 것은 아니다.

후속 실습에서는 행사명·날짜·로고만 바꾼 5~10초 템플릿을 만들고 한국어 렌더·Premiere 가져오기를 확인한다. 이는 M5에 해당하며 이번 자료 조사에서 데모 영상이 완성되었다고 표시하지 않는다.
