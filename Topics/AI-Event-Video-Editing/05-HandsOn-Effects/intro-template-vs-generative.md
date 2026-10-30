---
title: "M5 인트로 — 코드 템플릿과 생성형의 검증 경계"
author:
  - "Codex"
created: "2026-10-25 07:42:03"
tags:
  - ai-event-video-editing
  - effects
---

## 실습 지시문

같은 기술 커뮤니티 행사 인트로 조건으로 생성형 결과를 만들었다. 기존 코드 기반 타이틀 카드와 비교할 수 있도록 행사명·로고를 새로 지어내지 않고, 제목은 후편집으로 넣을 수 있게 중앙 여백을 요청했다.

> Create a 5-second widescreen 16:9 opening for a technology community event. Dark navy background, teal light trails and subtle geometric particles moving forward, clean cinematic motion, professional but warm. No people, no logos, no readable text, no music, no voiceover. Keep the center uncluttered for a title to be added later.

## 실제 실행 결과

| 경로 | 이번 상태 | 관찰·한계 |
|---|---|---|
| 코드 기반 타이틀 템플릿 | 로컬 제작·렌더 실행 | Python이 글자·도형을 배치하고 FFmpeg가 영상으로 조립했다. 행사명과 발표자 이름을 새로 확정하지 않은 중립 제목 카드다. → [원본 발췌 주제](../04-HandsOn-Highlight/method-A.md#2026-10-25-발표-b-요약-초안) |
| CapCut 템플릿 `INTRODUCTION 16:9` | 사양 확인, 편집기 진입 실패 | 상세 페이지에 16:9, 3개 클립, 8초, 624.61K uses로 표시됐다. `Use this template`을 눌러 편집기를 열었지만 CapCut이 `Network error. Check your internet connection and try again.`을 표시했다. 편집기 내 새로고침과 페이지 전체 새로고침 후에도 편집 자산은 계속 로딩 상태였다. 템플릿 교체·렌더는 못 했다. |
| 생성형 인트로 — CapCut Seedance 2.0 Mini | 생성·MP4 다운로드·기본 파일 검증 완료 | 출력은 5.062초·1280×720·24fps H.264와 AAC 44.1kHz 스테레오다. 전체 프레임에서 요청하지 않은 중앙의 `Penhin` 문구와 좌측 상단 `Ai` 표시가 확인되어, 무문자·중앙 여백 요청을 충족하지 못했다. 오디오 스트림은 있으나 청취해 내용은 판별하지 않았다. |

## 제한적인 비교

생성형 결과는 실제로 만들어졌지만 CapCut 템플릿 결과는 만들지 못해, 로드맵이 요구하는 템플릿·생성형 두 결과의 품질·시간·비용 비교는 아직 성립하지 않는다. 템플릿 사양과 AI 생성 결과의 관찰은 비교표에 참고로 기록하되, 템플릿 편집 시간·템플릿 비용·최종 렌더 품질은 미확인으로 둔다. Seedance 생성 화면은 60 credits 차감을 예고했으며, 별도 유료 체험이나 결제는 시작하지 않았다.

프롬프트는 텍스트만 입력했고 사용자 영상·이미지·음원을 업로드하지 않았다. CapCut이 제안한 후속 편집 중 `Add text overlay`는 실행하지 않았지만, 생성 결과 자체에 의도치 않은 `Penhin` 문구가 나타나 제목 없는 깨끗한 배경이라고 할 수 없다. 화면상의 생성 설명은 요청대로 만들었다고 안내해도 실제 전 구간을 재생해 검수해야 한다는 점을 확인했다. 행사명·로고의 정확성이나 상업 이용 권리를 보증하는 결과도 아니다.

## 2026-10-29 다운로드와 전체 프레임 확인

AI Creator에서 채팅 패널을 접고 생성 영상 카드를 선택하면 영상 위에 다운로드 화살표가 표시됐다. 이를 눌러 `Video 1.mp4`를 내려받았다. 원본 다운로드는 공개 Topic 밖의 로컬 작업 폴더에 보관했다. 파일은 2,015,277 bytes이며 전체 길이 5.062초, 영상 1280×720·24fps H.264, 음성 AAC 44.1kHz 스테레오다. FFmpeg 전체 디코드 검사에서 오류는 없었다. 미리보기 DOM 표시는 854×480·약 5.125초였으므로 미리보기 규격을 다운로드 출력 규격으로 기록하지 않는다.

초당 대표 프레임을 살펴보니 중간 구간 중앙에 `Penhin`으로 읽히는 생성 문구가 있고 좌측 상단에 `Ai` 표시가 보였다. 따라서 프롬프트의 “No readable text”와 중앙 여백 조건은 실패했다. 오디오 스트림은 무음이 아니지만 실제 내용을 청취하지 않아 음악·음성 여부는 미확인이다. 이 결과는 수정·재생성 여부를 판단하기 전의 검수용 초안이며, 추가 크레딧 사용이나 결제는 하지 않았다. CapCut 템플릿은 여전히 렌더되지 않아 두 결과 비교 DoD는 미완료다.

따라서 M5의 「인트로 2가지(템플릿·생성형) 비교」 DoD는 미완료다. 다음에는 편집기 네트워크 문제가 해결되면 같은 조건으로 CapCut 템플릿을 실제로 렌더하고 두 결과를 나란히 평가한다.

## 2026-10-29 공식 자료

CapCut 공식 Intro Creator는 인트로 템플릿을 선택해 영상·브랜딩을 넣는 흐름을 안내한다. 이번에 본 템플릿 상세는 [CapCut Introduction Templates](https://www.capcut.com/template/social/introduction)에서 연결됐다. 별도 제품 페이지는 [CapCut Intro Creator](https://www.capcut.com/create/intro-maker)다.

ByteDance Seed의 2026-07-31 공지는 Seedance 2.5의 다중 참조·편집 기능을 소개한다. 이번 CapCut 실습 결과는 Seedance 2.5가 아니라, 편집기에서 선택된 **Seedance 2.0 Mini**로 생성했다. → [Seedance 2.5 공식 발표](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)

## 사용한 시각·음원 자료

이번 생성에는 외부 이미지·음악·원본 촬영 영상을 사용하지 않았다. 기존 코드 템플릿은 로컬 설치된 맑은 고딕과 코드 생성 그래픽을 사용했고 글꼴 파일 자체는 배포하지 않는다. 원본 촬영본을 포함한 모든 자산의 사용 권리를 검증한 법적 판단으로 기록하지 않는다.
