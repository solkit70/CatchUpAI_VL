---
title: "M1 Build with AI 원본 자료 안내"
created: 2026-07-12 06:30:12
tags:
  - vibelearn-ai
  - build-with-ai
  - source-materials
---

## Purpose

이 문서는 M1의 첫 산출물이다. 영상 기획이나 Source Map으로 넘어가기 전에, 먼저 Build with AI가 어떤 자료인지, 원본은 어디에 있는지, 다시 받으려면 어디로 가야 하는지 확인한다. 실제 PDF/EPUB/치트시트 파일은 `../vl_materials/`에 보관하고, 이 문서는 그 자료들을 학습 가능한 입구로 설명한다.

## Build with AI란 무엇인가

Build with AI는 송재희님이 공개한 비개발자 빌더를 위한 실전 가이드다. 공식 사이트 설명 기준으로, AI로 실제 서비스를 만들고 싶은 사람이 기초, 프롬프트와 데이터, 배포, 바이브 코딩 이후 운영·검증, 필요한 개발 기초를 한 흐름으로 익히도록 구성되어 있다.

이 Topic에서 Build with AI를 다루는 이유는 단순히 "AI 도구를 소개"하기 위해서가 아니다. 핵심 질문은 "AI로 데모는 만들었는데 왜 서비스는 안 되는가"이며, 이 질문을 문제 정의, 데이터 준비, 검증 경계, 운영 기준, 프로덕션 전환 관점으로 학습하는 것이 목적이다.

## 공식 웹 자료

| 구분 | 위치 | 용도 |
|---|---|---|
| 한국어 홈 | https://buildwithai.clearlyreqs.com/ko/ | 전체 시리즈 구조와 대상 독자 확인 |
| 다운로드 페이지 | https://buildwithai.clearlyreqs.com/ko/downloads/ | 전체 시리즈 PDF/ePub 및 치트시트 다운로드 안내 |
| source note | [Build with AI source note](<../../../../../AI/Initiatives/Builders Lounge/builders/Song-Jae-hee-Build-with-AI/2026-06-29 Build with AI source note.md#source-materials>) | Vault에 처음 수집한 출처, Facebook 글, 로컬 파일 링크 확인 |

공식 다운로드 페이지에는 전체 12개 포스트를 하나의 PDF 또는 ePub으로 받을 수 있다는 안내와, 프롬프트 패턴·AI 레고 스택·신뢰 계층·데이터 준비 치트시트가 제공된다는 안내가 있다.

## 로컬 원본 자료 위치

현재 다운로드된 원본 파일은 Topic의 `vl_materials/` 폴더에 복사되어 있다. 최초 수집 위치는 Builders Lounge 자료 폴더이며, 현재 M1 학습에서는 아래 Topic 내부 복사본을 기준으로 사용한다.

```text
Ingest/CatchUpAI_VL/Topics/Build-with-AI/vl_materials/
```

| 파일 | 크기 | 역할 |
|---|---:|---|
| [build-with-ai-complete-ko.pdf](../vl_materials/build-with-ai-complete-ko.pdf) | 2,243,221 bytes | 한국어 완전판 PDF, M1 주 학습 자료 |
| [build-with-ai-complete-ko.epub](../vl_materials/build-with-ai-complete-ko.epub) | 107,653 bytes | 한국어 완전판 EPUB, 텍스트 확인과 파트별 읽기 노트 작성에 사용 |
| [build-with-ai-complete-en.pdf](../vl_materials/build-with-ai-complete-en.pdf) | 1,563,087 bytes | 영어 완전판 PDF, 한국어 표현이 모호할 때 대조 |
| [prompt-patterns-ko.pdf](../vl_materials/prompt-patterns-ko.pdf) | 362,358 bytes | 프롬프트 패턴 한국어 치트시트 |
| [prompt-patterns.pdf](../vl_materials/prompt-patterns.pdf) | 252,839 bytes | 프롬프트 패턴 영어 치트시트 |
| [ai-lego-stack-ko.pdf](../vl_materials/ai-lego-stack-ko.pdf) | 339,350 bytes | AI 레고 스택 한국어 치트시트 |
| [ai-lego-stack.pdf](../vl_materials/ai-lego-stack.pdf) | 267,743 bytes | AI 레고 스택 영어 치트시트 |
| [trust-tier-ko.pdf](../vl_materials/trust-tier-ko.pdf) | 311,071 bytes | 신뢰 계층 한국어 치트시트 |
| [trust-tier.pdf](../vl_materials/trust-tier.pdf) | 230,765 bytes | 신뢰 계층 영어 치트시트 |
| [data-readiness-ko.pdf](../vl_materials/data-readiness-ko.pdf) | 433,619 bytes | 데이터 준비 한국어 치트시트 |
| [data-readiness.pdf](../vl_materials/data-readiness.pdf) | 309,988 bytes | 데이터 준비 영어 치트시트 |

## 학습 전에 확인할 것

1. 먼저 이 문서에서 원본 자료 위치를 확인한다.
2. 다음으로 [Build with AI source note](<../../../../../AI/Initiatives/Builders Lounge/builders/Song-Jae-hee-Build-with-AI/2026-06-29 Build with AI source note.md#summary>)를 읽어 수집 맥락과 Facebook 글의 문제의식을 확인한다.
3. 그 다음 `build-with-ai-complete-ko.pdf` 또는 `build-with-ai-complete-ko.epub`을 기준으로 Part 0~12를 읽는다.
4. 한국어 표현이 어색하거나 의미가 모호한 부분은 `build-with-ai-complete-en.pdf`로 대조한다.
5. 치트시트 4종은 본문을 읽은 뒤 해당 파트를 복습하거나 영상/교과서 산출물의 표·도식 후보를 만들 때 사용한다.

## 산출물 품질 기준

Build with AI를 교과서 수준 산출물로 만들려면 학습 문서가 바로 영상 기획으로 뛰어가면 안 된다. 최소한 다음 정보가 먼저 있어야 한다.

- 이 자료가 무엇인지 설명하는 개요
- 공식 웹사이트와 다운로드 페이지
- Vault 안의 로컬 원본 파일 위치
- PDF/EPUB/치트시트별 역할
- 어떤 순서로 읽고, 어떤 자료를 대조용으로 쓸지에 대한 학습 경로
- Source Map, 영상 angle, 스크립트로 넘어가기 전의 출처 확인 기준

이 기준을 만족한 뒤에야 `reading-notes.md`와 `build-with-ai-source-map.md`로 넘어간다.
