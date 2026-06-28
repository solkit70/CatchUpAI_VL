# GOBI CLI — 핵심 개념 (Core Concepts)

> **모듈**: M1 — 설치 & 인증 & 핵심 개념
> **작성일**: 2026-03-29
> **CVL 업데이트**: 2026-06-27 (v2.0.35 — session/saved/draft 제거, personal/artifact 추가)
> **버전**: GOBI CLI v2.0.35

---

## 1. GOBI란?

GOBI는 **협업 지식 플랫폼**입니다.
팀이 지식을 AI와 함께 관리하고, 검색하고, 공유할 수 있는 도구입니다.
GOBI CLI는 이 플랫폼을 **터미널과 AI 에이전트**에서 사용할 수 있게 해주는 클라이언트입니다.

```
플랫폼:  https://www.gobispace.com
CLI:     npm install -g @gobi-ai/cli
버전:    v2.0.35 (2026-06-27 기준)
```

---

## 2. 핵심 개념 (v2.0.35 기준)

### 개념 관계도

```
Vault (지식 컨테이너)
├── PUBLISH.md  ←  vault publish로 발행 (구 BRAIN.md)
├── .gobi/settings.yaml  ← vault 설정
├── .gobi/syncfiles      ← sync 대상 패턴
└── Space (커뮤니티 협업 공간)
    ├── Channel (채널 — v2.0.35 신규)
    ├── Post (커뮤니티 토론/공유)
    │   ├── Reply
    │   └── Artifact (버전관리 콘텐츠 — v2.0.35 신규)
    └── Global Feed (공개 개인 포스트)
        └── Personal Feed (프라이빗 개인 포스트 — v2.0.35 신규)

Media (이미지/영상/아바타 생성 — v2.0.35에서 대폭 확장)
Sense (활동/전사 데이터)

── v2.0.35에서 제거됨 ──
Session (1:1 AI 대화) ❌ 제거
Saved (개인 노트 + 북마크) ❌ 제거
Draft (에이전트 standing guidance) ❌ 제거
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
> ⚠️ **v2.0.35 변경**: `vault set-primary` 제거됨

**주요 명령어**:
```bash
gobi vault init            # vault 초기화 (인터랙티브)
gobi vault create <slug>   # 새 vault 생성
gobi vault rename <name>   # vault 이름 변경
gobi vault delete <slug>   # vault 삭제 (⚠️ 비가역적)
gobi vault list            # 내 vault 목록
gobi vault publish         # PUBLISH.md 발행
gobi vault unpublish       # 발행 취소
gobi vault status          # 발행 상태 확인
gobi vault sync            # 로컬 ↔ WebDrive 동기화
```

---

### 2-2. Space & Post & Channel

| 항목 | 내용 |
|------|------|
| **정의** | 팀 협업 커뮤니티 공간. 포스트와 답글로 소통 |
| **비유** | GitHub Issues, Slack 채널 |
| **선택** | `gobi space warp` → 인터랙티브 선택 또는 slug 직접 지정 |
| **Post** | 구 Thread. `create-post/edit-post/delete-post` |
| **Channel** | 🆕 v2.0.35. 채널별 포스트 분리 관리 |

> ⚠️ **v2.0 변경**: Thread → **Post** (명칭 전면 변경)
> ⚠️ **Space & member admin은 웹 UI 전용** — CLI로 멤버 추가/제거, Agent 설정 불가

**주요 명령어**:
```bash
gobi space list                     # 내 Space 목록
gobi space warp                     # 활성 Space 선택
gobi space feed                     # 통합 피드 (최신순)
gobi space search-posts <query>     # 포스트 검색 (🆕 v2.0.35)
gobi space list-posts               # Post 목록
gobi space get-post <postId>        # Post 상세 조회
gobi space create-post              # 새 Post 생성
gobi space create-reply <postId>    # Post에 답글
gobi space react <postId> <emoji>   # 이모지 반응 (🆕 v2.0.35)
gobi space unreact <postId> <emoji> # 이모지 반응 취소 (🆕 v2.0.35)
gobi space list-channels            # 채널 목록 (🆕 v2.0.35)
gobi space get-channel <channelId>  # 채널 상세 (🆕 v2.0.35)
```

---

### 2-3. Global Feed (공개 개인 포스트)

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

### 2-4. Personal Feed (프라이빗 개인 포스트) 🆕 v2.0.35

| 항목 | 내용 |
|------|------|
| **정의** | 나만 볼 수 있는 프라이빗 포스트. 공개 피드에 노출되지 않음 |
| **비유** | Notion 개인 노트, 일기장 |
| **특징** | Global과 동일 데이터 모델, personalSpaceUserId로 scope 분리 |

**주요 명령어**:
```bash
gobi personal feed                  # 프라이빗 피드 조회
gobi personal create-post           # 프라이빗 포스트 작성
gobi personal search-posts <query>  # 개인 포스트 검색
gobi personal react <postId> <emoji> # 이모지 반응
```

---

### 2-5. Artifact (버전관리 콘텐츠) 🆕 v2.0.35

| 항목 | 내용 |
|------|------|
| **정의** | 포스트에 첨부되는 버전관리 창작물 |
| **종류** | `image` / `video` / `gif` / `markdown` / `meeting_summary` |
| **특징** | 항상 사람 소유. revision이 draft/published 트리 형성 (published 최대 1개) |
| **비유** | Google Docs 버전 기록, GitHub PR |

**주요 명령어**:
```bash
gobi artifact create --kind markdown --content "내용"  # 생성
gobi artifact revise <artifactId>                       # 새 draft revision
gobi artifact publish <artifactId>                      # draft → published
gobi artifact revert <artifactId>                       # 이전 revision으로 복귀
gobi artifact history <artifactId>                      # 전체 revision 트리
gobi artifact download <artifactId>                     # 콘텐츠 다운로드
```

---

### 2-6. Media (미디어 생성)

> **v2.0 신규**, **v2.0.35에서 대폭 확장**: 이미지/영상/아바타 생성에 편집·다운로드·시네마틱 추가

**주요 명령어**:
```bash
gobi media upload <file>            # 파일 업로드 (🆕 v2.0.35)
gobi media generate-image --prompt "..."   # 이미지 생성
gobi media edit-image               # 이미지 편집 (🆕 v2.0.35)
gobi media create-video             # 아바타 영상
gobi media create-cinematic         # 시네마틱 영상 (🆕 v2.0.35)
gobi media design-avatar            # 아바타 디자인 (🆕 v2.0.35)
```

---

### 2-7. Sense (활동 & 전사 데이터)

> **v2.0 업데이트**: `--start-time`/`--end-time` 옵션 추가 (ISO 8601 UTC 필수)

**주요 명령어**:
```bash
gobi sense list-activities \
  --start-time 2026-06-01T00:00:00Z \
  --end-time   2026-06-27T00:00:00Z
gobi sense list-transcriptions \
  --start-time 2026-06-01T00:00:00Z \
  --end-time   2026-06-27T00:00:00Z
```

---

### ❌ v2.0.35에서 제거된 기능

| 기능 | 제거 전 명령어 | 현재 대안 |
|------|-------------|---------|
| 1:1 AI 대화 | `gobi session list/get/create-reply` | 웹 UI 이용 |
| 개인 노트 | `gobi saved create-note/list-notes` | `gobi personal create-post` |
| 포스트 북마크 | `gobi saved create-post/list-posts` | 웹 UI 이용 |
| 에이전트 guidance | `gobi draft add/list/action` | 웹 UI 이용 |
| Vault primary 설정 | `gobi vault set-primary` | 웹 UI 이용 |

---

## 3. 언제 무엇을 쓰나? (v2.0.35 기준)

| 상황 | 사용할 기능 |
|------|-----------|
| vault 프로필 발행 | `gobi vault publish` |
| 팀에게 진행 상황 공유 | `gobi global create-post` |
| 팀과 토론하기 | `gobi space create-post` |
| 나만 보는 메모 작성 | `gobi personal create-post` (구 `saved create-note`) |
| 특정 포스트 검색 | `gobi space search-posts <query>` |
| 포스트에 반응하기 | `gobi space react <postId> <emoji>` |
| 채널 현황 파악 | `gobi space list-channels` |
| 버전관리 콘텐츠 작성 | `gobi artifact create --kind markdown` |
| 글로벌 피드 보기 | `gobi global feed` |
| 파일 동기화 | `gobi vault sync` |
| 이미지 생성 | `gobi media generate-image` |
| 이미지 편집 | `gobi media edit-image` (🆕 v2.0.35) |
| 1:1 AI 대화 | ⚠️ CLI 불가 — 웹 UI에서 직접 |

---

## 4. 버전별 주요 변경 요약

| 구분 | v0.6.x (구) | v2.0.12 | v2.0.35 (현재) |
|------|------------|---------|--------------|
| 초기화 | `gobi init` | `gobi vault init` | 동일 |
| 발행 파일 | `BRAIN.md` | `PUBLISH.md` | 동일 |
| 팀 공유 | `gobi brain post-update` | `gobi global create-post` | 동일 |
| 팀 토론 | `space create-thread` | `space create-post` | 동일 |
| 1:1 AI 대화 | `session reply` (404) | `session create-reply` (수정) | **CLI 제거** |
| 개인 노트 | 없음 | `saved create-note` | **제거** → `personal create-post` |
| 에이전트 guidance | 없음 | `draft add/list` | **CLI 제거** |
| 프라이빗 포스트 | 없음 | 없음 | **신규** `personal *` |
| 버전관리 콘텐츠 | 없음 | 없음 | **신규** `artifact *` |
| 포스트 검색 | 없음 | 없음 | **신규** `space search-posts` |
| 채널 관리 | 없음 | 없음 | **신규** `space list/get-channel` |

---

## 5. 전체 명령어 Quick Reference (v2.0.35)

```
gobi --version                    버전 확인
gobi --help                       전체 도움말
gobi update                       자가 업데이트

# 인증
gobi auth login                   로그인 (device-code flow)
gobi auth status                  인증 상태 확인
gobi auth logout                  로그아웃

# Vault
gobi vault init                   vault 초기화
gobi vault create <slug>          vault 생성
gobi vault rename <name>          vault 이름 변경
gobi vault delete <slug>          vault 삭제 (비가역적)
gobi vault list                   vault 목록
gobi vault publish                PUBLISH.md 발행
gobi vault unpublish              발행 취소
gobi vault status                 발행 상태
gobi vault sync                   파일 동기화

# Space
gobi space list                   Space 목록
gobi space warp [slug]            활성 Space 선택
gobi space feed                   통합 피드
gobi space search-posts <query>   포스트 검색 (🆕)
gobi space list-posts             Post 목록
gobi space get-post <id>          Post 상세
gobi space create-post            Post 생성
gobi space edit-post <id>         Post 수정
gobi space delete-post <id>       Post 삭제
gobi space create-reply <id>      답글 작성
gobi space edit-reply <id>        답글 수정
gobi space delete-reply <id>      답글 삭제
gobi space react <id> <emoji>     이모지 반응 (🆕)
gobi space unreact <id> <emoji>   이모지 반응 취소 (🆕)
gobi space list-channels          채널 목록 (🆕)
gobi space get-channel <id>       채널 상세 (🆕)
gobi space list-channel-members <id>  채널 멤버 (🆕)
gobi space list-topics            토픽 목록
gobi space list-topic-posts <slug>  토픽별 Post

# Global Feed
gobi global feed                  공개 피드
gobi global create-post           개인 포스트 작성
gobi global list-posts --mine     내 포스트 목록
gobi global edit-post <id>        포스트 수정
gobi global delete-post <id>      포스트 삭제

# Personal Feed (🆕 v2.0.35)
gobi personal feed                프라이빗 피드
gobi personal create-post         프라이빗 포스트 작성
gobi personal list-posts          프라이빗 포스트 목록
gobi personal search-posts <q>    프라이빗 포스트 검색
gobi personal react <id> <emoji>  이모지 반응

# Artifact (🆕 v2.0.35)
gobi artifact create              아티팩트 생성
gobi artifact revise <id>         새 revision 추가
gobi artifact publish <id>        draft → published
gobi artifact revert <id>         이전 revision으로 복귀
gobi artifact history <id>        revision 트리
gobi artifact get <id>            아티팩트 상세
gobi artifact list                내 아티팩트 목록
gobi artifact download <id>       콘텐츠 다운로드
gobi artifact delete <id>         아티팩트 삭제

# Media
gobi media upload <file>          파일 업로드 (🆕)
gobi media generate-image         이미지 생성
gobi media edit-image             이미지 편집 (🆕)
gobi media inpaint-image          이미지 인페인팅 (🆕)
gobi media get-image-status <id>  이미지 작업 상태 (🆕)
gobi media download-image <id>    이미지 다운로드 (🆕)
gobi media create-video           아바타 영상 생성
gobi media create-cinematic       시네마틱 영상 (🆕)
gobi media list-videos            영상 목록 (🆕)
gobi media get-video <id>         영상 메타데이터 (🆕)
gobi media get-video-status <id>  영상 생성 상태 (🆕)
gobi media download-video <id>    영상 다운로드 (🆕)
gobi media list-avatars           아바타 목록
gobi media list-voices            음성 목록
gobi media design-avatar          아바타 디자인 (🆕)
gobi media confirm-avatar         아바타 확정 (🆕)
gobi media design-avatar-from-selfie  셀피 기반 아바타 (🆕)
gobi media get-avatar-job-status <id>  아바타 작업 상태 (🆕)

# Sense
gobi sense list-activities        활동 기록
gobi sense list-transcriptions    전사 기록
```

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **CVL 기준**: v2.0.35 (2026-06-27)
> **다음 문서**: [installation-guide.md](installation-guide.md)
