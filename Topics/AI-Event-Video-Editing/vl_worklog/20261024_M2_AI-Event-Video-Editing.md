---
title: "WorkLog - M2: 방법별 리서치와 비교표"
author:
  - "박창수"
  - "Codex"
created: 2026-10-24 22:45:54
tags:
  - ai-event-video-editing
  - worklog
---

# WorkLog - M2: 방법별 리서치와 비교표

**날짜**: 2026-10-24 (America/Los_Angeles)
**모듈**: M2 - 방법별 리서치와 비교표
**작업 구간**: 1차 22:44:36–22:49:13 PT / 후속 22:50:11–22:55:40 PT (AI 조사·작성 구간, 사용자 실습 시간 아님)
**상태**: 문서 조사 산출물 완료. 직접 체험 0건·사용자 자기평가 미실시

## 오늘의 학습 목표

- [x] 의뢰인 답변 미확인으로 진행하도록 사용자 승인 확인
- [x] 5개 범주·후보 8개 조사 카드 작성
- [x] 기능·요금·한도·한국어·Premiere 연계 비교표 작성
- [x] Claude·ChatGPT 연결 방식의 역할과 검증 경계 정리
- [x] 학습 안내·로드맵·프롬프트 갱신, 링크 검사·회고

## 진행 내용

### 1. 범위와 사용자 승인

첫 세션은 Premiere 자체 AI·Vidio.ai·OpusClip 3개 사전 조사였다. 사용자는 이어서 남은 후보 조사를 승인해 Premiere MCP(A)·VEA(B)·Seedance(D)·FFmpeg와 전사(E)·Remotion(E)을 추가했다. 의뢰인 답변은 미확인으로 유지하며, 가입·설치·유료 API·영상 업로드는 하지 않았다.

60분 계획과 로드맵의 3.5시간은 학습 배분 기준이며 실제 사용자 학습 시간을 뜻하지 않는다. 이번에는 문서 조사와 산출물 정리만 수행했다.

### 2. 처음 조사한 3개 후보

- Premiere: 검색·전사와 공식 AI Assistant 베타를 분리했다. → [공식 Assistant 절](../02-Methods-Research/cards/premiere-native-ai.md#공식-ai-assistant-공개-베타)
- Vidio.ai: 연간 결제 환산 가격·원본 기준 크레딧·XML 누락 요소와 무료 XML 안내의 조건 차이를 기록했다. → [가격·입력 한도](../02-Methods-Research/cards/vidio-vibeedit.md#가격과-입력-한도)
- OpusClip: 체험 기능 제한·한국어 베타·XML 길이 안내를 기록했다. → [Premiere 전달 조건](../02-Methods-Research/cards/opusclip-clipanything.md#premiere-연계와-길이-주의)

### 3. 후속 5개 후보와 연결 방식

- Premiere MCP: 커뮤니티 작성자의 지원 설명과 실제 연결·호환성 검증을 구분했다. → [기능·조건](../02-Methods-Research/cards/premiere-mcp.md#기능조건)
- VEA: 개요의 XML 전달과 관리형 Edit Video API의 제공 범위를 구분했다. 후자는 출력 길이를 직접 지정할 수 없다고 명시한다. → [문서별 경계](../02-Methods-Research/cards/memories-vea.md#기능과-서로-다른-문서의-경계)
- Seedance: 참조 편집도 지원하므로 기존 「편집 불가」 단정을 정정했다. 긴 행사 원본의 구간 선택·조립 기능은 미확인이다. → [정정 근거](../02-Methods-Research/cards/seedance.md#기능과-기존-설명-정정)
- FFmpeg + 전사: 의미 판단과 구간 편집 역할을 나누고, 클라우드 전사 API와 로컬 처리 조건을 구분했다. → [역할과 한계](../02-Methods-Research/cards/ffmpeg-transcript.md#역할과-한계)
- Remotion: 인트로·자막·매개변수 템플릿과 조직·협업 라이선스를 확인했다. → [라이선스 조건](../02-Methods-Research/cards/remotion.md#비용과-라이선스)

[연결 방식 문서](../02-Methods-Research/claude-chatgpt-plugins.md#연결-방식별-판단)는 Claude 공식 MCP 문서와 OpenAI 공식 MCP 문서를 확인해 작성했다. ChatGPT 웹·로컬 클라이언트·실제 편집 도구의 역할을 구분했고, 연결 가능성이 최종 납품 자동화를 보장하지 않는다고 명시했다.

### 4. 갱신한 산출물

카드 8개·비교표·연결 방식 분석·M2 README를 완성하고 한·영 Topic README·방법 지도·로드맵·일일 프롬프트를 갱신했다. M1의 단정적 Seedance 설명도 정정했으며, M1 의뢰인 확인 대기는 완료로 바꾸지 않았다. 과거 WorkLog의 당시 판단은 정정 주석으로 보존한다.

## 리뷰 후 보완 — 23:08 PT 이후

사용자가 Claude 리뷰를 전달하고 수정 계획을 승인했다. OpusClip 월/연 화면·Pro 내보내기 포함을 실제 공개 브라우저에서 다시 대조했고, Vidio 월 결제 가격을 확인해 카드에 보완했다. 가격과 후보 누락의 상세 기록은 [리뷰 반영 기록](../02-Methods-Research/review-followup.md#중요-수치-재확인)에 있다.

CapCut을 추가해 현재 카드는 5개 범주·9개이며 미조사 후보의 보류 이유를 기록했다. M3의 조건부 추천과 한 장 요약은 작성했지만 실제 체험·사용자 본인의 가격 대조는 하지 않았다. 과거 8개 조사 단계의 작업 기록은 그대로 보존한다.

## 문제 해결 로그

일부 공식 도움말은 본문 추출이 되지 않거나 동적 가격이 로딩 상태로 남았다. 검색 요약의 숫자를 확정하지 않고 본문이 보이는 공식 자료를 따라가거나 미확인으로 남겼다. Seedance는 BytePlus의 실제 요금 본문을 확인해 단일 생성 조건의 추정 가격으로 기록했다.

VEA 개요의 로컬 서비스 예시와 관리형 API는 다른 층위의 문서다. 한쪽의 XML 기능을 다른 API에서도 제공한다고 합치지 않았고, 가격·길이·한국어·무료 체험에서 남은 질문을 카드에 기록했다.

## M2 DoD 체크리스트

- [x] 5개 범주 · 후보 8개 이상 조사 카드 — 초기 8개, 리뷰 후 A 1개·B 3개·C 2개·D 1개·E 2개로 9개
- [x] 모든 카드에 공식 출처와 확인 날짜 — 커뮤니티 MCP는 작성자 원문으로 구분
- [x] 비교표 완성 — 가격·무료 체험·한도·한국어·연계, 미확인 값 명시
- [x] Claude·ChatGPT 연결 방식의 가능·불가능 및 미검증 범위 정리
- [x] 산출물 폴더·README
- [x] README 링크 검사 — 상대 링크 111개 정상·깨짐 0·빈 폴더 0, 로컬 절 링크 56개 확인
- [x] WorkLog·Daily Retrospective

**문서 산출물 DoD**: 7/7 (100%). 실제 연결·편집 품질·무료 계정 제공 범위·사용자 자기평가는 이 수치에 포함하지 않는다.

## Daily Retrospective

### What went well

의뢰인 조건이 비어 있어도 조사할 수 있는 기능·과금·연계 경로를 확보했다. 공식 문서에서 확인한 설명과 실제 계정·영상에서 검증해야 하는 항목을 분리했다.

### What could be improved

영상 길이·언어 품질·XML 전달은 서비스마다 문서화 수준이 다르다. M3에서는 아직 모르는 조건이 추천에 미치는 영향을 정리하고, M4에서는 동일 원본과 지시로 검증해야 한다.

### Insights

생성형·편집형이라는 이름만으로 기능을 단정하면 최신 참조 편집 기능을 놓칠 수 있다. 또한 연결 도구가 편집 프로그램을 조작하는 능력과, 좋은 장면을 선별하는 능력은 별개다. 근거는 [Seedance 정정](../02-Methods-Research/cards/seedance.md#기능과-기존-설명-정정)과 [연결 경계 분석](../02-Methods-Research/claude-chatgpt-plugins.md#되는-것과-아직-증거가-없는-것)에 기록했다.

### Tomorrow's focus

M3의 조건부 추천안·체험 계획을 수립한다. 답변이 없다면 의뢰인 조건을 가정으로 명시하고, 어떤 답에 따라 후보가 바뀌는지 먼저 설명한다. 무료 서비스의 가입·기능 조건과 공개 가능한 시험 영상을 정한 뒤 실습한다.

## Module Retrospective — M2 자료 점검

### 목표와 실제 결과

계획한 문서 산출물 7개 항목을 갖췄으며, 미확인 수치·실제 품질을 추정으로 채우지 않았다. 사용자 자기평가는 실시하지 않았으므로 「사용자가 도구를 설명·사용할 수 있다」는 학습 목표는 자동 체크하지 않는다.

### 다음 모듈 준비

추천안은 아직 확정하지 않았고 유료 도구를 체험하지 않았다. M3는 별도 학습 계획에 따라 진행하며, [비교표의 미확인 조건](../02-Methods-Research/comparison-table.md#m3에서-확인할-조건)을 출발점으로 사용한다.

## 참조 및 산출물

- [이전 M1 WorkLog](20261017_M1_AI-Event-Video-Editing.md#tomorrows-focus)
- [로드맵 M2](../vl_roadmap/20261017_RoadMap_AI-Event-Video-Editing.md#m2---방법별-리서치와-비교표)
- [M2 안내](../02-Methods-Research/README.md)
- [비교표](../02-Methods-Research/comparison-table.md)
- [연결 방식 분석](../02-Methods-Research/claude-chatgpt-plugins.md)
