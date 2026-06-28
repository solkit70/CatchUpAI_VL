# CVL WorkLog: GOBI-CLI v2.0.35 업데이트 동기화

**작성일**: 2026-06-27
**세션 유형**: CVL (Continuous Vibe Learning) - 업데이트 동기화 세션
**Topic**: GOBI-CLI
**관련 업데이트 기간**: 2026-05-29 ~ 2026-06-27
**이전 CVL**: 20260529_CVL_GOBI-CLI.md

---

## 동기화 개요

### 버전 변화

- **이전 CVL 기준**: v2.0.19 (2026-05-29)
- **현재 버전**: v2.0.35 (2026-06-27 확인, `gobi update`로 자동 업데이트)
- **영향도**: 🔴 **중간** — Breaking change 있음 (session/saved/draft CLI 전체 제거)

---

## v2.0.19 → v2.0.35 주요 변경사항

### Breaking 1: `gobi session` 전체 제거

v2.0.12에서 정상화됐던 `session list/get/create-reply`가 **v2.0.35에서 CLI에서 완전 제거됨**.

| 제거된 명령어 | 현재 대안 |
|-------------|---------|
| `gobi session list` | 웹 UI(gobispace.com) |
| `gobi session get <id>` | 웹 UI |
| `gobi session create-reply <id>` | 웹 UI |

> 1:1 AI 대화 기능 자체는 유지되지만, CLI에서 더 이상 접근 불가.

### Breaking 2: `gobi saved` 전체 제거

| 제거된 명령어 | 현재 대안 |
|-------------|---------|
| `gobi saved create-note` | `gobi personal create-post` |
| `gobi saved list-notes` | `gobi personal list-posts` |
| `gobi saved create-post --source` | 웹 UI |
| `gobi saved list-posts` | 웹 UI |

### Breaking 3: `gobi draft` 전체 제거

| 제거된 명령어 | 현재 대안 |
|-------------|---------|
| `gobi draft add/list/get/delete` | 웹 UI |
| `gobi draft action <id> <index>` | 웹 UI |
| `gobi draft revise` | 웹 UI |

### Breaking 4: `gobi vault set-primary` 제거

v2.0.19에서 추가됐다가 v2.0.35에서 다시 제거됨. 웹 UI에서만 설정 가능.

---

### 신규 1: `gobi personal` — 프라이빗 개인 포스트

나만 볼 수 있는 프라이빗 포스트. 공개 피드에 노출되지 않음.

```bash
gobi personal feed
gobi personal create-post --content "..."
gobi personal list-posts
gobi personal search-posts <query>   # from:/topic: 연산자 지원
gobi personal get-post <postId>
gobi personal edit-post/delete-post/create-reply/edit-reply/delete-reply
gobi personal react <postId> <emoji>
gobi personal unreact <postId> <emoji>
```

> `saved create-note`의 실용적 대안으로 활용 가능.

### 신규 2: `gobi artifact` — 버전관리 콘텐츠

포스트에 첨부되는 버전관리 창작물. markdown / image / video / gif / meeting_summary 지원.

```bash
gobi artifact create --kind markdown --content "..."
gobi artifact revise <artifactId>
gobi artifact publish <artifactId>
gobi artifact revert <artifactId>
gobi artifact history <artifactId>
gobi artifact download <artifactId>
gobi artifact get/list/delete
```

### 신규 3: `gobi space` 기능 대폭 확장

| 신규 명령어 | 설명 |
|-----------|------|
| `gobi space search-posts <query>` | 키워드 + `from:<name>` + `topic:<tag>` 연산자 검색 |
| `gobi space react <postId> <emoji>` | 이모지 반응 추가 (멱등) |
| `gobi space unreact <postId> <emoji>` | 이모지 반응 취소 |
| `gobi space list-channels` | 채널 목록 (멤버: 내 채널, 어드민: 전체) |
| `gobi space get-channel <channelId>` | 채널 상세 (에이전트 채널도 포함) |
| `gobi space list-channel-members <channelId>` | 채널 멤버 목록 |

### 신규 4: `gobi media` 대폭 확장

v2.0.19의 4개 → v2.0.35의 18개 서브커맨드로 확장.

| 카테고리 | 신규 명령어 |
|---------|-----------|
| 파일 | `upload <file>` |
| 이미지 | `edit-image`, `inpaint-image`, `get-image-status`, `download-image` |
| 영상 | `list-videos`, `get-video`, `get-video-status`, `download-video`, `create-cinematic` |
| 아바타 | `design-avatar`, `confirm-avatar`, `design-avatar-from-selfie`, `get-avatar-job-status` |

---

## 영향도 종합 평가

| 변경사항 | 영향도 | Breaking | 조치 완료 |
|---------|--------|---------|---------|
| session 전체 제거 | 🔴 높음 | ✅ | ✅ 전체 문서 반영 |
| saved 전체 제거 | 🟡 중간 | ✅ | ✅ personal로 대체 안내 |
| draft 전체 제거 | 🟡 중간 | ✅ | ✅ 웹 UI 안내로 전환 |
| vault set-primary 제거 | 🟢 낮음 | ✅ | ✅ 주석 처리 |
| personal 신규 | 🟢 | ❌ | ✅ core-concepts + quick-reference 추가 |
| artifact 신규 | 🟢 | ❌ | ✅ core-concepts + quick-reference 추가 |
| space search/react/채널 신규 | 🟢 | ❌ | ✅ quick-reference 추가 |
| media 대폭 확장 | 🟢 | ❌ | ✅ quick-reference 추가 |

**전체 영향도**: 🟡 중간 (session/saved/draft Breaking, 신규 기능 다수)

---

## 업데이트 완료 파일 목록

- [x] `04-Capstone/guides/quick-reference.md` — v2.0.35 전면 반영
- [x] `01-Setup-Auth/concepts/core-concepts.md` — 개념 트리 + 섹션 재구성
- [x] `04-Capstone/guides/complete-workflow.md` — Step 3 session → personal 대체, 트러블슈팅 업데이트
- [x] `README.md` — 버전/CVL 날짜/개념 트리/CVL 워크로그 링크 업데이트
- [x] `02-Brain-Session/README.md` — session 제거 반영, 버전 이력 테이블 추가

---

## 오늘 배운 것

- v2.0.35는 session/saved/draft를 CLI에서 완전히 제거하는 Breaking change가 있었다. 이는 GOBI 플랫폼이 AI 대화와 노트 기능을 웹 UI 중심으로 집중하는 방향으로 전환한 것으로 보인다.
- `personal` 명령어가 `saved create-note`의 실용적 대안으로 추가됐다 — 프라이빗 포스트이므로 나만 볼 수 있고, 같은 데이터 모델로 react/search도 지원한다.
- `artifact`는 버전관리 기능을 포스트에 붙이는 개념으로, Google Docs처럼 revision 트리를 관리할 수 있다.
- `space search-posts`가 추가되어 이제 CLI에서 키워드와 `from:`, `topic:` 연산자로 Space 내 포스트를 검색할 수 있다.
- `space get-channel`은 에이전트 채널도 조회 가능하여 Bila AI Agent 작업에 유용할 수 있다.

## 잘된 점

- CVL 주기: 29일 (5/29 → 6/27) — 한 달 주기 유지
- `gobi --help`와 각 서브커맨드 `--help` 비교로 신규/제거 항목을 체계적으로 식별

## 다음 할 일

- [ ] `gobi personal create-post`로 개인 메모 워크플로우 실습
- [ ] `gobi artifact create --kind markdown` 실습 (버전관리 콘텐츠)
- [ ] `gobi space search-posts` 실습 (changbal 스페이스)
- [ ] `gobi space get-channel`로 Bila AI 에이전트 채널 조회 실습
- [ ] `gobi media create-cinematic` 실습 (신규 시네마틱 영상)

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **마지막 업데이트**: 2026-06-27
