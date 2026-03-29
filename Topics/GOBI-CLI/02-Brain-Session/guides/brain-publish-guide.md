# GOBI CLI — Brain Publish & Updates 가이드

> **모듈**: M2 — Brain & Session 명령어 마스터
> **작성일**: 2026-03-29
> **버전**: GOBI CLI v0.6.15

---

## 1. BRAIN.md 구조

`gobi init`으로 자동 생성되는 파일. vault 루트에 위치해야 합니다.

### Frontmatter 필드

```markdown
---
title: vault 이름              # 필수: Brain 제목
tags: ["태그1", "태그2"]       # 선택: 검색 태그
description: 설명 텍스트       # 선택: Brain 소개
thumbnail:                     # 선택: 썸네일 URL
prompt: AI 지시 프롬프트       # 선택: Brain AI에게 역할 부여
---
```

### 작성 예시

```markdown
---
title: gobi-cli-study
tags: ["gobi-cli", "learning", "vibelearn-ai"]
description: GOBI CLI 학습 지식 저장소
thumbnail:
prompt: You are a GOBI CLI learning assistant. Help users understand CLI commands with examples.
---

# Brain 제목

## Overview
Brain 소개 내용

## Key Topics
- 주요 주제 1
- 주요 주제 2

## Resources
- [링크 이름](URL)
```

---

## 2. gobi brain publish

BRAIN.md를 플랫폼에 업로드합니다.

```bash
# 현재 디렉토리의 BRAIN.md 발행
gobi brain publish

# 실습 결과:
# Published BRAIN.md to vault "gobi-cli-study"
```

**전제 조건**:
- 현재 디렉토리에 BRAIN.md 존재
- `.gobi/settings.yaml`에 vaultSlug 설정됨 (`gobi init` 완료)

---

## 3. gobi brain unpublish

```bash
gobi brain unpublish
# vault에서 BRAIN.md 삭제
```

---

## 4. brain updates CRUD

Brain Updates는 **팀에게 진행 상황을 공유**하는 알림/피드 기능입니다.

### Create (post-update)

```bash
gobi brain post-update \
  --title "업데이트 제목" \
  --content "마크다운 내용"

# 특정 vault 지정 시:
gobi brain post-update \
  --vault-slug <slug> \
  --title "제목" \
  --content "내용"

# 응답:
# Brain update posted!
#   ID: 256
#   Title: GOBI CLI 학습 시작 🚀
#   Vault: gobi-cli-study
#   Created: 2026-03-29T13:31:02.477Z
```

### Read (list-updates)

```bash
gobi brain list-updates

# 출력 예시:
# Brain updates (20 items):
# - [256] "GOBI CLI 학습 시작 🚀" by Changsoo Park (vault: gobi-cli-study)
# - [254] "..." by Minsuk Kang (vault: brave-path-zr962w)
# ...
```

> list-updates는 **전체 사용자의 업데이트**를 보여줍니다 (타임라인 피드).

### Update (edit-update)

```bash
gobi brain edit-update <updateId> \
  --content "수정된 내용"

# --title도 수정 가능:
gobi brain edit-update <updateId> \
  --title "새 제목" \
  --content "새 내용"
```

### Delete (delete-update)

```bash
gobi brain delete-update <updateId>
# Brain update 255 deleted.
```

### CRUD 전체 흐름 요약

```
post-update → ID 발급
    ↓
list-updates → ID 확인
    ↓
edit-update <id> --content "수정"
    ↓
delete-update <id>
```

---

## 5. 핵심 차이점: publish vs post-update

| 기능 | publish | post-update |
|------|---------|-------------|
| **대상** | BRAIN.md 파일 전체 | 짧은 업데이트 텍스트 |
| **목적** | Brain 지식 베이스 갱신 | 진행 상황 알림/공유 |
| **빈도** | Brain 내용 변경 시 | 매일/작업 완료 시 |
| **노출** | Brain 검색에 반영 | 팀 피드/타임라인 |

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
