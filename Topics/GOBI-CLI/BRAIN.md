---
title: gobi-cli-study
tags: ["gobi-cli", "learning", "vibelearn-ai", "cli-tool"]
description: GOBI CLI 학습을 위한 VibeLearn AI 기반 지식 저장소. 설치부터 Brain/Session/Space 명령어 마스터까지.
thumbnail:
prompt: You are a GOBI CLI learning assistant. This brain contains structured knowledge about GOBI CLI commands, concepts, and workflows learned through the VibeLearn AI methodology. Help users understand GOBI CLI commands with practical examples.
---

# GOBI CLI Study Brain

> VibeLearn AI v2.0 방법론으로 학습한 GOBI CLI 지식 저장소
> 학습자: Changsoo Park | 시작일: 2026-03-29

---

## Overview

GOBI CLI(`@gobi-ai/cli`)는 Gobi 협업 지식 플랫폼을 터미널에서 사용하는 클라이언트 도구입니다.

**현재 버전**: v0.6.15
**플랫폼**: https://www.gobispace.com
**설치**: `npm install -g @gobi-ai/cli`

---

## Core Concepts

| 개념 | 설명 | 비유 |
|------|------|------|
| **Vault** | 최상위 지식 컨테이너 | GitHub Organization |
| **Space** | 팀 협업 공간 | GitHub Repository |
| **Brain** | AI 기반 지식 자원 | Wiki + AI |
| **Session** | Brain과의 1:1 대화 | ChatGPT 대화창 |
| **Thread** | 팀 토론 스레드 | GitHub Issues |

---

## Key Commands

### 인증 & 초기화
```bash
gobi auth status          # 인증 확인
gobi auth login           # 로그인
gobi init                 # vault 설정 (인터랙티브)
```

### Brain
```bash
gobi brain search --query "검색어"                    # Brain 검색
gobi brain ask --vault-slug <slug> --question "질문"  # Brain에 질문
gobi brain publish                                    # BRAIN.md 발행
gobi brain unpublish                                  # 발행 취소
gobi brain list-updates                               # 업데이트 목록
gobi brain post-update --content "내용"               # 업데이트 게시
```

### Session
```bash
gobi session list                                     # 세션 목록
gobi session get <sessionId>                          # 세션 조회
gobi session reply <sessionId> --content "내용"       # 세션에 답장
```

### Space
```bash
gobi space list                                       # Space 목록
gobi space warp [slug]                                # Space 선택
gobi space list-threads                               # Thread 목록
gobi space create-thread                              # Thread 생성
gobi space create-reply <threadId>                    # Thread 답글
```

---

## Learning Progress

- [x] M1: 설치 & 인증 & 핵심 개념 (2026-03-29)
- [ ] M2: Brain & Session 명령어 마스터
- [ ] M3: Space & Thread 협업 기능
- [ ] M4: 실전 워크플로우 + 교과서 완성

---

## Resources

- [GOBI CLI GitHub](https://github.com/gobi-ai/gobi-cli)
- [Gobi Platform](https://www.gobispace.com)
- [VibeLearn AI](https://github.com/solkit70/CatchUpAI_VL)
