# GOBI CLI — 핵심 개념 (Core Concepts)

> **모듈**: M1 — 설치 & 인증 & 핵심 개념
> **작성일**: 2026-03-29
> **CVL 업데이트**: 2026-05-10 (v2.0.12 전면 반영)
> **버전**: GOBI CLI v2.0.12

---

## 1. GOBI란?

GOBI는 **협업 지식 플랫폼**입니다.
팀이 지식을 AI와 함께 관리하고, 검색하고, 공유할 수 있는 도구입니다.
GOBI CLI는 이 플랫폼을 **터미널과 AI 에이전트**에서 사용할 수 있게 해주는 클라이언트입니다.

```
플랫폼:  https://www.gobispace.com
CLI:     npm install -g @gobi-ai/cli
버전:    v2.0.12 (2026-05-10 기준)
```

---

## 2. 핵심 개념 (v2.0 기준)

### 개념 관계도

```
Vault (지식 컨테이너)
├── PUBLISH.md  ←  vault publish로 발행 (구 BRAIN.md)
├── .gobi/settings.yaml  ← vault 설정
├── .gobi/syncfiles      ← sync 대상 패턴
└── Space (커뮤니티 협업 공간)
    ├── Post (커뮤니티 토론/공유)
    │   └── Reply (포스트 답글)
    └── Global Feed (개인 포스트)
        └── Personal Post + Reply

Session (1:1 AI 대화)
Saved (개인 노트 + 북마크)
Draft (에이전트 standing guidance)
Media (이미지/영상 생성)
Sense (활동/전사 데이터)
```

---

### 2-1. Vault

| 항목 | 내용 |
|------|------|
| **정의** | GOBI의 최상위 지식 컨테이너. 하나의 프로젝트/조직 단위 |
| **비유** | GitHub Organization, Notion Workspace |
| **생성** | `gobi vault init` → 새로 만들거나 기존 것 선택 |
| **설정 파일** | `.gobi/settings.yaml` (vaultSlug 저장) |
| **PUBLISH.md** | vault 루트에 위치, vault publish의 원본 (구 BRAIN.md) |

> ⚠️ **v2.0 변경**: `gobi init` → `gobi vault init` / `BRAIN.md` → `PUBLISH.md`

**주요 명령어**:
```bash
gobi vault init            # vault 초기화 (인터랙티브)
gobi vault list            # 내 vault 목록
gobi vault publish         # PUBLISH.md 발행
gobi vault unpublish       # 발행 취소
gobi vault status          # 발행 상태 확인
gobi vault sync            # 로컬 ↔ WebDrive 동기화
```

---

### 2-2. Space & Post

| 항목 | 내용 |
|------|------|
| **정의** | 팀 협업 커뮤니티 공간. 포스트와 답글로 소통 |
| **비유** | GitHub Issues, Slack 채널 |
| **선택** | `gobi space warp` → 인터랙티브 선택 또는 slug 직접 지정 |
| **Post** | 구 Thread. `create-post/edit-post/delete-post` |

> ⚠️ **v2.0 변경**: Thread → **Post** (명칭 전면 변경)

**주요 명령어**:
```bash
gobi space list                     # 내 Space 목록
gobi space warp                     # 활성 Space 선택
gobi space feed                     # 통합 피드 (최신순)
gobi space list-posts               # Post 목록
gobi space get-post <postId>        # Post 상세 조회
gobi space create-post              # 새 Post 생성
gobi space create-reply <postId>    # Post에 답글
```

---

### 2-3. Global Feed (개인 포스트)

> **v2.0 신규**: 구 `gobi brain post-update` 등이 `gobi global *`으로 대체됨

| 항목 | 내용 |
|------|------|
| **정의** | 저자 프로필에 표시되고 공개 글로벌 피드에 노출되는 개인 포스트 |
| **비유** | Twitter/X 포스트, LinkedIn 게시물 |

**주요 명령어**:
```bash
gobi global feed                    # 공개 글로벌 피드
gobi global create-post             # 개인 포스트 작성 (구 brain post-update)
gobi global list-posts --mine       # 내 포스트 목록 (구 brain list-updates)
```

---

### 2-4. Session (1:1 대화)

| 항목 | 내용 |
|------|------|
| **정의** | Brain과의 1:1 AI 대화 세션 |
| **시작** | 웹 UI 또는 Brain ask (웹 기반) |
| **CLI 관리** | `gobi session list/get/create-reply` |

> ⚠️ **v2.0 변경**: `session reply` → `session create-reply`
> ✅ v2.0에서 session 404 이슈 **해결됨**

**주요 명령어**:
```bash
gobi session list                           # 내 Session 목록
gobi session get <sessionId>                # Session 내용 확인
gobi session create-reply <sessionId>       # 대화 이어가기
  --content "메시지"
```

---

### 2-5. Saved (개인 지식 저장소)

> **v2.0 신규**: 개인 노트 작성 + 포스트 북마크 기능

**주요 명령어**:
```bash
gobi saved create-note --content "노트 내용"    # 개인 노트 작성
gobi saved list-notes                           # 노트 목록
gobi saved create-post --source <postId>        # 포스트 북마크
gobi saved list-posts                           # 북마크 목록
```

---

### 2-6. Draft (에이전트 guidance)

> **v2.0 신규**: 에이전트가 작성하는 standing guidance. 시스템 프롬프트에 자동 주입됨

**주요 명령어**:
```bash
gobi draft add "제목" "내용"     # draft 추가 (에이전트용)
gobi draft list                  # draft 목록
gobi draft action <id> 0         # suggested action 실행
```

---

### 2-7. Media (미디어 생성)

> **v2.0 신규**: 이미지/영상/아바타 생성

**주요 명령어**:
```bash
gobi media generate-image --prompt "..."     # 이미지 생성
gobi media create-video --avatar-id ...      # 아바타 영상
```

---

### 2-8. Sense (활동 & 전사 데이터)

> **v2.0 업데이트**: `--start-time`/`--end-time` 옵션 추가 (ISO 8601 UTC 필수)

**주요 명령어**:
```bash
gobi sense list-activities \
  --start-time 2026-05-10T00:00:00Z \
  --end-time   2026-05-11T00:00:00Z
gobi sense list-transcriptions \
  --start-time 2026-05-10T00:00:00Z \
  --end-time   2026-05-11T00:00:00Z
```

---

## 3. 언제 무엇을 쓰나? (v2.0 기준)

| 상황 | 사용할 기능 |
|------|-----------|
| vault 프로필 발행 | `gobi vault publish` (구 `brain publish`) |
| 팀에게 진행 상황 공유 | `gobi global create-post` (구 `brain post-update`) |
| 팀과 토론하기 | `gobi space create-post` (구 `space create-thread`) |
| AI와 대화 이어가기 | `gobi session create-reply` (구 `session reply`) |
| 개인 노트 작성 | `gobi saved create-note` |
| 글로벌 피드 보기 | `gobi global feed` |
| 파일 동기화 | `gobi vault sync` (구 `gobi sync`) |
| 이미지 생성 | `gobi media generate-image` |

---

## 4. v2.0 핵심 변경 요약

| 구분 | v0.6.x (구) | v2.0.12 (현재) |
|------|------------|--------------|
| 초기화 | `gobi init` | `gobi vault init` |
| 발행 파일 | `BRAIN.md` | `PUBLISH.md` |
| 발행 | `gobi brain publish` | `gobi vault publish` |
| 팀 공유 | `gobi brain post-update` | `gobi global create-post` |
| 팀 토론 | `space create-thread` | `space create-post` |
| 대화 답장 | `session reply` | `session create-reply` |
| 파일 동기화 | `gobi sync` | `gobi vault sync` |

---

## 5. 전체 명령어 Quick Reference (v2.0)

```
gobi --version                    버전 확인
gobi --help                       전체 도움말

# 인증
gobi auth login                   로그인 (device-code flow)
gobi auth status                  인증 상태 확인
gobi auth logout                  로그아웃

# Vault
gobi vault init                   vault 초기화
gobi vault list                   vault 목록
gobi vault publish                PUBLISH.md 발행
gobi vault unpublish              발행 취소
gobi vault status                 발행 상태
gobi vault sync                   파일 동기화

# Space
gobi space list                   Space 목록
gobi space warp [slug]            활성 Space 선택
gobi space feed                   통합 피드
gobi space list-posts             Post 목록
gobi space get-post <id>          Post 상세
gobi space create-post            Post 생성
gobi space edit-post <id>         Post 수정
gobi space delete-post <id>       Post 삭제
gobi space create-reply <id>      답글 작성
gobi space edit-reply <id>        답글 수정
gobi space delete-reply <id>      답글 삭제

# Global Feed
gobi global feed                  공개 피드
gobi global create-post           개인 포스트 작성
gobi global list-posts --mine     내 포스트 목록
gobi global edit-post <id>        포스트 수정
gobi global delete-post <id>      포스트 삭제

# Session
gobi session list                 Session 목록
gobi session get <id>             Session 내용
gobi session create-reply <id>    대화 이어가기

# Saved
gobi saved list-notes             노트 목록
gobi saved create-note            노트 작성
gobi saved list-posts             북마크 목록
gobi saved create-post            북마크 추가

# Draft
gobi draft list                   draft 목록
gobi draft add <title> <content>  draft 추가
gobi draft action <id> <index>    action 실행

# Media
gobi media generate-image         이미지 생성
gobi media create-video           영상 생성

# Sense
gobi sense list-activities        활동 기록
gobi sense list-transcriptions    전사 기록
```

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **CVL 기준**: v2.0.12 (2026-05-10)
> **다음 문서**: [installation-guide.md](installation-guide.md)
