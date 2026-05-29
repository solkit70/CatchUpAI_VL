# 🔄 CVL WorkLog: GOBI-CLI v2.0.19 업데이트 동기화

**작성일**: 2026-05-29
**세션 유형**: CVL (Continuous Vibe Learning) - 업데이트 동기화 세션
**Topic**: GOBI-CLI
**관련 업데이트 기간**: 2026-05-10 ~ 2026-05-29
**이전 CVL**: 20260510_CVL_GOBI-CLI.md

---

## 🔄 Continuous Vibe Learning - 업데이트 개요

### 동기화 일시
2026-05-29

### 버전 변화
- **이전 CVL 기준**: v2.0.12 (2026-05-10)
- **현재 버전**: v2.0.19 (2026-05-29 확인)
- **영향도**: 🟢 **소규모** — Breaking change 없음, 기능 추가 위주

---

## 📋 v2.0.12 → v2.0.19 주요 변경사항

### 신규 1: `gobi vault` CRUD 명령어 추가 🆕

Vault 관리 기능이 대폭 확장됐다.

| 신규 명령어 | 설명 |
|------------|------|
| `gobi vault create <slug> [--name]` | 새 Vault 생성. slug는 고유해야 함. init이나 set-primary는 별도 실행 필요 |
| `gobi vault rename <newName> [--vault-slug]` | Vault 표시 이름 변경 (PUBLISH.md frontmatter의 title과는 별개) |
| `gobi vault delete <slug>` | Vault 삭제 (**비가역적**). slug 명시 필수. 콘텐츠가 남아있으면 API가 거부 |
| `gobi vault set-primary <slug>` | Primary Vault 설정. 다른 vault의 primary는 자동 해제 |

> ⚠️ `vault delete`는 비가역적 — posts, members, files를 먼저 정리해야 API가 수락

### 신규 2: `gobi update` 명령어 🆕

```bash
gobi update     # gobi-cli를 최신 버전으로 자동 업데이트
```

> 이전에는 `npm install -g @gobi-ai/cli`로만 업데이트 가능했음

### 신규 3: `create-post` 미디어·첨부·리포스트 옵션 🆕

`gobi space create-post` 및 `gobi global create-post` 모두에 추가:

| 신규 옵션 | 설명 |
|----------|------|
| `--attach <file>` | 로컬 미디어 파일 첨부 (반복 가능). X 스타일: 사진 최대 4장 OR GIF 1개 OR 동영상 1개. 용량: 사진 5MB / GIF 15MB / 동영상 512MB |
| `--repost-post-id <postId>` | 기존 포스트를 임베드 카드로 감싸서 리포스트. 리포스트의 리포스트는 서버에서 루트로 축약 |
| `--auto-attachments` | 포스트 내 `[[wiki-link]]` 파일들을 webdrive에 먼저 업로드 후 포스팅 |
| `--draft-id <draftId>` | draft를 title/content 소스로 사용 (--title/--content/--rich-text와 상호 배타적) |
| `--rich-text <json>` | Rich-text JSON 배열 (--content와 상호 배타적) |

### 신규 4: `draft revise` 인라인 업데이트 옵션 🆕

```bash
# 기존: comment만 입력 가능
gobi draft revise <draftId> <comment>

# 신규: comment + 내용 동시 수정 가능
gobi draft revise <draftId> <comment> \
  --title "새 제목" \
  --content "새 내용" \
  --action "레이블::메시지"   # 최대 3회 반복, 기존 actions 전체 교체
```

### 신규 5: `saved create-note`에 `--draft-id` 추가 🆕

```bash
gobi saved create-note --draft-id <draftId>   # draft 내용을 note로 변환
```

---

## 📊 영향도 종합 평가

| 변경사항 | 영향도 | Breaking | 조치 완료 |
|---------|--------|---------|---------|
| vault create/rename/delete/set-primary | 🆕 신규 | ❌ | ✅ SKILL.md + quick-reference.md 반영 |
| `gobi update` 명령어 | 🆕 신규 | ❌ | ✅ SKILL.md + quick-reference.md 반영 |
| create-post `--attach/--repost/--auto-attachments` | 🆕 신규 | ❌ | ✅ SKILL.md + quick-reference.md 반영 |
| create-post `--draft-id/--rich-text` | 🆕 신규 | ❌ | ✅ SKILL.md 반영 |
| draft revise 인라인 옵션 | 🆕 신규 | ❌ | ✅ SKILL.md 반영 |
| saved create-note `--draft-id` | 🆕 신규 | ❌ | ✅ SKILL.md 반영 |

**전체 영향도**: 🟢 낮음 (Breaking change 없음, 기존 워크플로우 유지)

---

## 📝 업데이트 완료 파일 목록

- [x] `_Settings_/Skills/gobi-cli/SKILL.md` — v2.0.19 반영, 신규 명령어 추가
- [x] `04-Capstone/guides/quick-reference.md` — vault CRUD + update + create-post 옵션 추가
- [x] `README.md` — CVL 기록 업데이트

---

## 🎯 오늘 배운 것

- v2.0.19는 Breaking change 없이 vault 관리 기능과 미디어 포스팅 기능이 크게 강화됐다.
- `--repost-post-id` 옵션이 추가되어 GobiSpace에서 X(Twitter)처럼 리포스트 기능이 가능해졌다.
- `--draft-id` 연동으로 draft → post/note 워크플로우가 통합됐다 — 에이전트가 draft를 만들고 사용자가 승인하면 바로 게시하는 흐름이 완성.
- `gobi update`로 자가 업데이트가 가능해져 npm 없이도 최신 버전 유지 가능.

## ✅ 잘된 점

- CVL 프로세스 실행 간격: 19일 (5/10 → 5/29) — 적절한 주기로 동기화 유지
- `--help` 명령어 비교로 신규 옵션을 빠르게 식별

## 📋 다음 할 일

- [ ] `gobi vault create/delete` 실습
- [ ] `--attach` 옵션으로 이미지 포함 포스트 실습
- [ ] `--repost-post-id` 리포스트 워크플로우 실습
- [ ] `draft → create-post --draft-id` 에이전트 워크플로우 실습

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **마지막 업데이트**: 2026-05-29
