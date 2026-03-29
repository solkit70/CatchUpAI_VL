# GOBI CLI — 핵심 개념 (Core Concepts)

> **모듈**: M1 — 설치 & 인증 & 핵심 개념
> **작성일**: 2026-03-29
> **버전**: GOBI CLI v0.6.15
> **목적**: GOBI CLI를 처음 배우는 사람이 핵심 개념을 한 번에 이해하기 위한 참조 문서

---

## 1. GOBI란?

GOBI는 **협업 지식 플랫폼**입니다.
팀이 지식을 AI와 함께 관리하고, 검색하고, 공유할 수 있는 도구입니다.
GOBI CLI는 이 플랫폼을 **터미널에서** 사용할 수 있게 해주는 클라이언트입니다.

```
플랫폼:  https://www.gobispace.com
CLI:     npm install -g @gobi-ai/cli
버전:    v0.6.15 (2026-03-29 기준)
```

---

## 2. 핵심 개념 5가지

### 개념 관계도

```
Vault (최상위 지식 컨테이너)
├── BRAIN.md  ←  brain publish로 발행
├── .gobi/settings.yaml  ← vault 설정
└── Space (팀 협업 공간)
    ├── Brain (AI 지식 자원)
    │   └── Session (Brain과의 1:1 대화)
    └── Thread (팀 토론 스레드)
        └── Reply (스레드 답글)
```

---

### 2-1. Vault

| 항목 | 내용 |
|------|------|
| **정의** | GOBI의 최상위 지식 컨테이너. 하나의 프로젝트/조직 단위 |
| **비유** | GitHub Organization, Notion Workspace |
| **생성** | `gobi init` → 새로 만들거나 기존 것 선택 |
| **설정 파일** | `.gobi/settings.yaml` (vaultSlug 저장) |
| **BRAIN.md** | vault 루트에 위치, brain publish의 원본 |

**실습에서 생성한 Vault**:
```
이름: gobi-cli-study
Slug: gobi-cli-study
설정: .gobi/settings.yaml → vaultSlug: gobi-cli-study
```

---

### 2-2. Space

| 항목 | 내용 |
|------|------|
| **정의** | Vault 내 팀 협업 공간. 관련 Brain과 Thread를 묶는 단위 |
| **비유** | GitHub Repository, Notion Page |
| **선택** | `gobi space warp` → 인터랙티브 선택 또는 slug 직접 지정 |
| **목록** | `gobi space list` → 내가 속한 Space 목록 확인 |
| **옵션** | `--space-slug <slug>` → 명령어에서 직접 Space 지정 가능 |

**주요 명령어**:
```bash
gobi space list                        # 내 Space 목록
gobi space warp                        # 활성 Space 선택 (인터랙티브)
gobi space warp <slug>                 # 특정 Space로 바로 이동
gobi space list-threads                # 현재 Space의 Thread 목록
gobi space create-thread               # 새 Thread 생성
```

---

### 2-3. Brain

| 항목 | 내용 |
|------|------|
| **정의** | AI 기반 지식 자원. 검색하고, 질문하고, 업데이트를 발행할 수 있는 지식 단위 |
| **비유** | Wiki + AI 어시스턴트 |
| **원본** | `BRAIN.md` 파일 (로컬에 위치, publish로 플랫폼에 업로드) |
| **발행** | `gobi brain publish` → BRAIN.md를 vault에 업로드 |

**주요 명령어**:
```bash
gobi brain search --query "검색어"    # 공개 Brain 검색 (텍스트 + 의미 기반)
gobi brain ask --vault-slug <slug> --question "질문"   # Brain에 질문 → Session 생성
gobi brain publish                    # BRAIN.md → vault 업로드
gobi brain unpublish                  # vault에서 BRAIN.md 삭제
gobi brain list-updates               # 최근 Brain 업데이트 목록
gobi brain post-update                # Brain 업데이트 게시
```

**BRAIN.md 구조** (gobi init이 생성한 기본 형태):
```markdown
---
title: gobi-cli-study
tags: []
description:
thumbnail:
prompt:
---
(본문: Brain의 지식 내용)
```

---

### 2-4. Session

| 항목 | 내용 |
|------|------|
| **정의** | Brain과의 1:1 대화 세션. `gobi brain ask`로 시작, `gobi session reply`로 이어감 |
| **비유** | ChatGPT 대화창 (특정 Brain에 연결된) |
| **시작** | `gobi brain ask` → sessionId 반환 |
| **이어가기** | `gobi session reply <sessionId>` |
| **확인** | `gobi session get <sessionId>` |

**핵심 플로우**:
```
Brain ask → Session 생성 (sessionId)
              ↓
         session reply → 대화 계속
              ↓
         session get → 전체 대화 내용 확인
```

**주요 명령어**:
```bash
gobi brain ask --vault-slug <slug> --question "질문"
gobi session list                         # 내 Session 목록
gobi session get <sessionId>              # 특정 Session 내용 확인
gobi session reply <sessionId> --message "메시지"   # 대화 계속
```

---

### 2-5. Thread & Reply

| 항목 | 내용 |
|------|------|
| **정의** | Space 내 팀 토론 스레드. 여러 팀원이 참여하는 비동기 커뮤니케이션 |
| **비유** | GitHub Issues, Slack 채널 |
| **위치** | Space 안에 존재 |
| **구성** | Thread (원글) + Reply (답글) |

**주요 명령어**:
```bash
gobi space list-threads                  # Thread 목록
gobi space get-thread <threadId>         # Thread 내용 확인
gobi space create-thread                 # 새 Thread 작성
gobi space create-reply <threadId>       # Thread에 답글
gobi space edit-thread <threadId>        # Thread 수정 (본인만)
gobi space delete-thread <threadId>      # Thread 삭제 (본인만)
```

---

## 3. Brain vs Session vs Thread — 언제 무엇을 쓰나?

| 상황 | 사용할 기능 |
|------|-----------|
| 공개된 지식 베이스에서 정보 찾기 | `gobi brain search` |
| 특정 Brain의 AI에게 질문하기 | `gobi brain ask` → Session |
| AI와 대화를 이어가기 | `gobi session reply` |
| 팀과 토론하기 | `gobi space create-thread` |
| 내 지식을 플랫폼에 발행하기 | `gobi brain publish` |

---

## 4. Roadmap에 없던 추가 명령어 (v0.6.15 발견)

> 실제 설치 후 `--help` 탐색에서 발견된 명령어

### gobi sense
```bash
gobi sense activities       # 활동 기록 조회 (시간 범위 지정)
gobi sense transcriptions   # 전사(트랜스크립션) 기록 조회
```
→ 활동 로그, 음성/회의 전사 관련 기능으로 추정. M3에서 추가 탐색 예정.

### gobi sync
```bash
gobi sync                          # 로컬 vault ↔ Gobi Webdrive 동기화
gobi sync --upload-only            # 로컬 → 서버만
gobi sync --download-only          # 서버 → 로컬만
gobi sync --dry-run                # 변경사항 미리보기 (실제 적용 안 함)
gobi sync --conflict ask|server|client|skip   # 충돌 해결 전략
```
→ 로컬 파일과 플랫폼 간 동기화. `gobi brain publish`와 다르게 전체 파일 동기화 기능.

### gobi session update (Roadmap에 있었으나 help에는 없음)
```bash
# gobi session update → v0.6.15에서는 확인 안 됨
# list / get / reply 3개만 실제 존재
```

---

## 5. 전체 명령어 Quick Reference

```
gobi --version                    버전 확인
gobi --help                       전체 도움말

# 인증
gobi auth login                   로그인
gobi auth status                  인증 상태 확인
gobi auth logout                  로그아웃

# 초기화
gobi init                         vault 설정 (선택 또는 생성)

# Brain
gobi brain search --query <q>     공개 Brain 검색
gobi brain ask --vault-slug <s> --question <q>   Brain에 질문
gobi brain publish                BRAIN.md 발행
gobi brain unpublish              BRAIN.md 발행 취소
gobi brain list-updates           Brain 업데이트 목록
gobi brain post-update            Brain 업데이트 게시

# Session
gobi session list                 내 Session 목록
gobi session get <id>             Session 내용 확인
gobi session reply <id>           Session에 답장

# Space
gobi space list                   Space 목록
gobi space warp [slug]            활성 Space 선택
gobi space list-threads           Thread 목록
gobi space get-thread <id>        Thread 내용
gobi space create-thread          Thread 생성
gobi space edit-thread <id>       Thread 수정
gobi space delete-thread <id>     Thread 삭제
gobi space create-reply <id>      Thread에 답글
gobi space edit-reply <id>        답글 수정
gobi space delete-reply <id>      답글 삭제

# Sense (추가 발견)
gobi sense activities             활동 기록 조회
gobi sense transcriptions         전사 기록 조회

# Sync (추가 발견)
gobi sync                         로컬 ↔ Webdrive 동기화
gobi sync --dry-run               동기화 미리보기
```

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **다음 문서**: [installation-guide.md](installation-guide.md)
