---
title: "GOBI에 Vibe Guiding 적용 - 아이디어 파편"
created: 2026-04-03
tags:
  - vibe-guiding
  - gobi
  - pcm
  - idea-spark
---

## 배경

GOBI 시스템에 Vibe Guiding을 적용하는 프로젝트를 구상 중. 이 문서는 그 과정에서 떠오르는 아이디어와 참고 사항들을 기록하는 파편 모음.

## GitHub 접근 권한 현황

Mika (GitHub: @gpminsuk)가 초대한 GOBI 관련 레포지토리:

| 레포지토리 | 상태 | 초대일 |
|-----------|------|--------|
| gobi-ai/gobi-web | ✅ Accept 완료 | 2026-03-31 |
| gobi-ai/gobi-desktop | ✅ Accept 완료 | 2026-03-31 |

- 초대 이메일은 solkit70@gmail.com 으로 발송됨
- GitHub 계정: solkit70

## 팀 내 나의 Role & Task

### 2026-04-02 (수요일) Slack 대화 요약

Jinyoung Kim이 documentation 작업 분담을 정리:

| 담당자 | 역할 |
|--------|------|
| mika & greg | 각 repo의 live (up-to-date) spec 자동 생성 |
| **Changsoo Park & greg** | **User Manual 작성** — 기존 aiforbetter.me 사이트 대체 |
| Jinyoung Kim | Lecture note 변형 버전 |
| (팀 전체) | Chatbots/Persona 변형 버전 |

**대체 대상 사이트:**
- https://www.aiforbetter.me/
- https://pub.aiforbetter.me/

**문서 도메인**: docs.gobihq.com (greg이 각 제품 core concepts 추가 중)

### 나의 구체적 Task

1. **Greg과 함께 User Manual 작성** — aiforbetter.me를 대체할 GOBI User Manual
2. **Spec Sheet 협업** — Greg이 solkit70@gmail.com으로 초대 완료 (확인 필요)
3. **docs.gobihq.com 검토** — Greg이 추가 중인 core concepts 파악 → Vibe Guiding Source Context로 활용 가능

### 핵심 연결점

Greg이 작성 중인 core concepts (`docs.gobihq.com`) + 내가 작성할 User Manual = Vibe Learning의 인풋으로 활용할 수 있다. 이것이 곧 **GOBI에 Vibe Guiding을 적용하는 출발점**이 될 수 있음.

## 참고 링크 및 메모

### 2026-04-01 Greg 이메일 — Gobi Specs 시트 공유 (편집 권한)

Greg Moon (greg@joingobi.com)이 4월 1일 12:18 PM에 Google Sheets 편집 권한으로 초대.

**시트 이름**: Gobi Specs
**링크**: https://docs.google.com/spreadsheets/d/1eWGs38ObnjRjOHFY2_Du0TENtM3CSj6I/edit?usp=sharing&ouid=109099432758822886377&rtpof=true&sd=true

#### 시트 구성 (탭 5개)

| 탭 | 내용 |
|----|------|
| Gobi Desktop | 데스크탑 앱 기능 스펙 |
| Gobi Space | 웹 협업 공간 스펙 |
| Astra | Astra 제품 스펙 |
| Gobi CLI | CLI 도구 스펙 |
| Gobi Mobile | 모바일 앱 스펙 |

#### 각 탭의 컬럼 구조

| 컬럼 | 설명 |
|------|------|
| File Name | 스펙 파일명 |
| Description of Spec | 스펙 설명 |
| Link to Spec | 스펙 문서 링크 |
| # Version | 버전 |
| Status | Approved / Draft / Final / Review |
| Date Updated | 최종 수정일 |
| **Core Concept** | **비어있음 — Greg & Changsoo가 채워야 함** (분홍색 컬럼) |

#### 현재 상태 및 할 일

- **Core Concept 컬럼이 비어있음** — 이것이 나의 주요 작업 대상
- Jin의 메시지: "For docs I left it blank for @greg & @Changsoo Park to fill"
- 각 탭별로 Core Concept을 정의하는 것 = User Manual의 뼈대가 됨
- Vibe Guiding 적용 시 이 Core Concept이 Context의 핵심 단위가 됨

#### 연결점

이 스펙 시트의 Core Concept → Vibe Learning 인풋 → Vibe Guiding Context로 이어지는 파이프라인의 시작점이다.

### 2026-04-02 Jin 메시지 — Feature List & Specs 시트

Jin이 Slack에서 공유한 내용 (4:15 PM):

> "Here's the feature list (mostly from desktop onboarding) & specs (from template vault)"
> - I can imagine we'll need more rows for Gobi Space and other endpoints
> - For docs I left it blank for @greg & @Changsoo Park to fill
> - For each new release we can test on all features coverages & ensure docs are updated

### 2026-04-01 Greg 메시지 (확인 필요)

Greg이 Slack에서 공유한 내용:

> docs.gobihq.com
> @Changsoo Park @Jinyoung Kim fyi, i'm adding core concepts of each product

- **확인 필요**: docs.gobihq.com — GOBI 각 제품의 core concepts 문서
- Greg이 직접 작성 중인 문서 → Vibe Guiding의 Source Context로 활용 가능성 검토
- Vibe Learning으로 이 문서를 학습시키면 GOBI 사용자 가이드의 기반이 될 수 있음
