# GOBI CLI — Vault Publish & Global Posts 가이드

> **모듈**: M2 — Vault & Global & Session
> **작성일**: 2026-03-29
> **CVL 업데이트**: 2026-05-10 (v2.0.12 — brain → vault/global 재편)
> **버전**: GOBI CLI v2.0.12

> ⚠️ **v2.0 Breaking Change**: `gobi brain` 명령어 그룹이 해체됨
> - `gobi brain publish` → `gobi vault publish`
> - `gobi brain post-update` 등 → `gobi global create-post` 등
> - `BRAIN.md` → `PUBLISH.md`

---

## 1. PUBLISH.md 구조

`gobi vault init`으로 자동 생성. vault 루트에 위치해야 합니다. (구 BRAIN.md와 동일한 frontmatter 구조)

### Frontmatter 필드

```markdown
---
title: vault 이름              # 필수: vault 제목
tags: ["태그1", "태그2"]       # 선택: 검색 태그
description: 설명 텍스트       # 선택: vault 소개
thumbnail:                     # 선택: 썸네일 URL
prompt: AI 지시 프롬프트       # 선택: AI에게 역할 부여
---
```

### 작성 예시

```markdown
---
title: gobi-cli-study
tags: ["gobi-cli", "learning", "vibelearn-ai"]
description: GOBI CLI v2.0 학습 지식 저장소
thumbnail:
prompt: You are a GOBI CLI learning assistant. Help users understand CLI commands with examples.
---

# Vault 소개

## Overview
GOBI CLI v2.0 학습 산출물 저장소

## Key Topics
- v2.0 명령어 체계 (vault, global, saved, draft, media, sense)
- CVL (Continuous Vibe Learning) 프로세스
```

---

## 2. gobi vault publish

PUBLISH.md를 플랫폼에 업로드합니다. (구 `gobi brain publish`)

```bash
# 현재 디렉토리의 PUBLISH.md 발행
gobi vault publish

# 결과:
# Published PUBLISH.md to vault "gobi-cli-study"
```

**전제 조건**:
- 현재 디렉토리에 `PUBLISH.md` 존재
- `.gobi/settings.yaml`에 `vaultSlug` 설정됨 (`gobi vault init` 완료)

---

## 3. gobi vault unpublish

```bash
gobi vault unpublish
# vault에서 PUBLISH.md 삭제
```

---

## 4. gobi vault status

vault 발행 상태를 확인합니다.

```bash
gobi --json vault status

# 결과:
# {
#   "success": true,
#   "data": {
#     "isPublished": true,
#     "fileCount": 342,
#     "profileUrl": "https://gobispace.com/vault/gobi-cli-study"
#   }
# }
```

---

## 5. Global Posts (구 Brain Updates)

팀에게 진행 상황을 공유하는 기능. `gobi brain post-update` 등이 `gobi global *`으로 이전됨.

### Create (`global create-post`)

```bash
gobi global create-post \
  --title "업데이트 제목" \
  --content "마크다운 내용"

# vault와 연결:
gobi global create-post \
  --vault-slug gobi-cli-study \
  --title "GOBI CLI v2.0 CVL 완료 🎉" \
  --content "v0.6.x → v2.0.12 업데이트: vault/global/saved/draft/media 신규 그룹 추가"

# 응답:
# {
#   "id": 256,
#   "title": "GOBI CLI v2.0 CVL 완료 🎉",
#   "createdAt": "2026-05-10T..."
# }
```

### Read (`global list-posts`)

```bash
# 내 포스트만 보기 (구 brain list-updates)
gobi --json global list-posts --mine

# 전체 글로벌 피드
gobi --json global feed
```

### Update (`global edit-post`)

```bash
gobi global edit-post <postId> \
  --content "수정된 내용"

# --title도 수정 가능:
gobi global edit-post <postId> \
  --title "새 제목" \
  --content "새 내용"
```

### Delete (`global delete-post`)

```bash
gobi global delete-post <postId>
```

### CRUD 전체 흐름

```
global create-post → ID 발급
         ↓
global list-posts --mine → ID 확인
         ↓
global edit-post <id> --content "수정"
         ↓
global delete-post <id>
```

---

## 6. 핵심 차이점: vault publish vs global create-post

| 기능 | vault publish | global create-post |
|------|--------------|-------------------|
| **대상** | PUBLISH.md 파일 전체 | 짧은 텍스트 포스트 |
| **목적** | vault 프로필/지식 갱신 | 진행 상황 공유/피드 |
| **빈도** | vault 내용 변경 시 | 매일/작업 완료 시 |
| **노출** | vault 공개 프로필 | 글로벌 피드/개인 프로필 |
| **구 명령어** | `brain publish` | `brain post-update` |

---

## 7. 구 명령어 매핑

| 구 명령어 (≤v1.x) | 새 명령어 (v2.0+) |
|-------------------|------------------|
| `gobi brain publish` | `gobi vault publish` |
| `gobi brain unpublish` | `gobi vault unpublish` |
| `gobi brain post-update` | `gobi global create-post` |
| `gobi brain list-updates` | `gobi global list-posts --mine` |
| `gobi brain edit-update <id>` | `gobi global edit-post <id>` |
| `gobi brain delete-update <id>` | `gobi global delete-post <id>` |

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **CVL 기준**: v2.0.12 (2026-05-10)
