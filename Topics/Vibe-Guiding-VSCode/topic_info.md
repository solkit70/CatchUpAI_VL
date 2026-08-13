---
title: "Vibe-Guiding-VSCode Topic 정보"
created: 2026-04-26 23:17:07
tags:
  - vibe-guiding
  - vibelearn-ai
  - vscode
  - gobi
  - development-practice
sources:
  - "[[VibeGuiding_BrainDump]]"
  - "[[2026-04-03 GOBI Vibe Guiding 시스템 맵]]"
  - "[[2026-04-05 Vibe Guiding 구현 계획]]"
  - "[[2026-04-09 - Proposal - Vibe Guiding Architecture for Gobi]]"
  - "[[2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]]"
---

## Topic 기본 정보

**Topic 이름**: `Vibe-Guiding-VSCode`

**Topic 설명**:
```
VibeLearn AI 학습 방법론을 사용해 Vibe Guiding의 철학, 아키텍처, GOBI 적용 전략을 학습하고,
VS Code 개발 환경에서 직접 POC를 구현하면서 Vibe Manual, CVL, 사용자 컨텍스트 수집,
Triggering, Retrieval, Guide Response 생성까지 실습하는 개발 중심 Topic.
```

**학습 및 개발 목적**:
```
1. Vibe Guiding을 "VibeLearn AI로 만든 최신 매뉴얼을 사용자 상황에 맞게 활성화하는 시스템"으로 명확히 이해한다.
2. GOBI 시스템을 대상으로 Vibe Manual 생성/유지 컴포넌트와 Vibe Guiding 엔진 컴포넌트를 분리해 설계한다.
3. VS Code에서 실행 가능한 최소 POC를 개발하여 사용자 컨텍스트 수집 -> 트리거 판정 -> 문서 검색 -> 맞춤 안내 생성을 검증한다.
4. 이후 GOBI Desktop/Applet/CLI에 통합할 수 있는 실전 개발 기반을 만든다.
```

**예상 기간**: `4-6주, 실습 중심`

## 학습 목표

- [ ] Vibe Guiding의 핵심 개념을 Vibe Learning, Vibe Manual, CVL, Triggering, User Context, Guide Response로 나누어 설명할 수 있다.
- [ ] GOBI 문서/스펙/소스/기존 테스트 기록을 바탕으로 AI-optimized Vibe Manual 구조를 설계할 수 있다.
- [ ] VS Code에서 실행 가능한 사용자 상태 수집기와 Guiding 엔진 POC를 구현할 수 있다.
- [ ] 최신 매뉴얼 기반 Retrieval과 사용자 맥락 기반 응답 조립을 분리해서 설계할 수 있다.
- [ ] 실제 GOBI 사용 흐름에서 발생한 실패/혼란 상황을 Triggering 테스트 케이스로 바꿀 수 있다.

## 학습 및 개발 환경

**OS**: Windows 11

**주요 도구**:
```
- VS Code
- Claude Code 또는 Codex
- Python 3.12+
- Markdown 기반 VibeLearn AI Topic 구조
- GOBI Desktop / GOBI CLI / GOBI Space
- GitHub 리포지토리 및 docs/specs 자료
```

**사전 지식**:
```
필수:
- VibeLearn AI의 Topic -> Roadmap -> Daily Learning -> WorkLog 흐름
- GOBI 생태계의 기본 구성
- Python 파일/JSON/Markdown 처리

권장:
- VS Code 확장 또는 로컬 CLI 도구 개발 경험
- Retrieval/RAG 기본 개념
- 제품 매뉴얼과 사용자 온보딩 설계 경험
```

## 핵심 참조 자료

**로컬 문서**:
```
- Topics/Materials_For_Topics/Idea/Vibe_Guiding/VibeGuiding_BrainDump.md
- Topics/GOBI-Guiding/2026-04-03 GOBI Vibe Guiding 시스템 맵.md
- Topics/GOBI-Guiding/2026-04-05 Vibe Guiding 구현 계획.md
- Topics/GOBI-Specs-Pipeline/04-Reviews-and-Opinions/2026-04-09 - Proposal - Vibe Guiding Architecture for Gobi.md
- Topics/GOBI-Guiding/2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트.md
- Topics/GOBI-CLI/
- Topics/Clearly-BRD-PRD/
```

**사용자 제공 Substack 글**:
```
- https://substack.com/home/post/p-193035543
- https://substack.com/home/post/p-182036138
- https://substack.com/home/post/p-193863653
```

Substack 글은 현재 로컬 본문이 제공되지 않았으므로 Roadmap에서는 "사용자 제공 참고 링크"로만 취급한다. 이후 본문을 로컬에 저장하거나 접근 가능한 텍스트를 제공하면 Vibe Guiding 철학 정리 모듈의 정식 Source로 편입한다.

## 최종 산출물

```
1. 01-Vision-and-Architecture/
   - Vibe Guiding 개념, GOBI 적용 구조, Two-Component Strategy 정리

2. 02-Vibe-Manual-CVL/
   - GOBI 대상 Vibe Manual 구조
   - CVL 업데이트 판단 기준
   - 문서 chunk/retrieval metadata 설계

3. 03-Guiding-Engine-POC/
   - VS Code에서 실행 가능한 Python 기반 POC
   - user_context.json, trigger_rules.json, retrieval_index.json, guide_response.md

4. 04-GOBI-Integration-Plan/
   - GOBI Desktop/Applet/CLI 통합 계획
   - 테스트 시나리오와 데모 플로우

5. vl_worklog/
   - 각 모듈별 학습/개발 로그와 회고
```

## 접근 방식

이 Topic은 문서 작성만으로 끝내지 않는다. 각 모듈은 개념 학습 30%, 실습 70% 비율로 진행하며, 매 모듈마다 실제 파일, JSON 스키마, Python 코드, 테스트 케이스 중 하나 이상의 실행 가능한 산출물을 남긴다.
