# GOBI CLI — End-to-End 완전 워크플로우

> **모듈**: M4 — 실전 워크플로우 + 교과서 완성 (Capstone)
> **작성일**: 2026-03-29
> **CVL 업데이트**: 2026-05-10 (v2.0.12 — 명령어 전면 업데이트)
> **버전**: GOBI CLI v2.0.12

---

## 워크플로우 개요

M1~M3에서 배운 모든 명령어를 실전 시나리오로 연결한 End-to-End 흐름입니다.

```
인증 확인 → 글로벌 피드 탐색 → Session 확인 → Space Post 생성 → Global 업데이트 게시
     ↓              ↓                ↓                ↓                    ↓
 auth status   global feed      session list      create-post        global create-post
               space feed       session get       create-reply       vault sync
```

> **v2.0 변경**: `brain search/ask` → CLI 제거됨 (웹 UI 이용)
> 워크플로우 Step 2는 `global feed` / `space feed`로 대체

---

## 시나리오: "학습 완료 알림 + 팀 공유" 워크플로우 (v2.0)

### Step 1: 인증 상태 확인

```bash
gobi auth status

# 결과:
# Authenticated
# User: Changsoo Park (solkit70@gmail.com)
# Vault: gobi-cli-study
```

**v2.0**: 인증 정상 ✅

---

### Step 2: 글로벌/Space 피드로 관련 지식 자원 확인

> ⚠️ **v2.0 변경**: `gobi brain search`는 CLI에서 제거됨 → `global feed` 또는 `space feed` 사용

```bash
# 글로벌 피드 확인 (커뮤니티 전체 포스트)
gobi --json global feed

# 특정 Space 피드 확인
gobi --json space feed --space-slug changbal

# Space 토픽별 탐색 (v2.0 신규)
gobi --json space list-topics --space-slug changbal
gobi --json space list-topic-posts ai --space-slug changbal
```

**활용**: 피드에서 관련 포스트를 찾아 컨텍스트 파악 후 후속 작업 진행

---

### Step 3: Session 확인 및 대화 이어가기

> ⚠️ **v2.0 변경**: `gobi brain ask`는 CLI에서 제거됨 (웹 UI에서 새 Session 시작)
> ✅ `session list/get`은 v2.0에서 **정상 작동** (v0.6.15 HTTP 404 이슈 해결됨)

```bash
# Session 목록 확인
gobi --json session list

# Session 내용 확인
gobi --json session get 9b73ebfd-f32b-4171-b411-25c56f507ab1

# 대화 이어가기 (구 session reply)
gobi session create-reply 9b73ebfd-f32b-4171-b411-25c56f507ab1 \
  --content "GOBI CLI v2.0의 주요 변경사항을 요약해줘"

# 응답 예시:
# {
#   "sessionId": "9b73ebfd-...",
#   "answer": "v2.0의 주요 변경: vault 명령 그룹 신설, Thread→Post 변경...",
#   "createdAt": "2026-05-10T..."
# }
```

**결과**: Session 대화 이어가기 ✅

---

### Step 4: Space에 학습 완료 Post 게시 (구 Thread)

```bash
gobi space create-post \
  --space-slug changbal \
  --title "GOBI CLI M4 Capstone: End-to-End 워크플로우 완성 (v2.0)" \
  --content "M1~M4 Capstone까지 GOBI CLI v2.0 전체 학습 완료했습니다. 🎉

학습 내용:
- M1: 설치/인증/핵심 개념 (Vault/Space/Session/Saved/Draft/Media/Sense)
- M2: Vault Publish, Global Posts, Session 관리
- M3: Space/Post CRUD 전체 (Thread→Post 변경 반영)
- M4: End-to-End 워크플로우 + Quick Reference 완성

전체 산출물: https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/GOBI-CLI

VibeLearn AI v2.0 방법론으로 학습 — 누구나 이 자료를 참고하여 따라할 수 있습니다." \
  --json

# 응답:
# {
#   "id": 735,
#   "title": "GOBI CLI M4 Capstone: End-to-End 워크플로우 완성 (v2.0)",
#   "replyCount": 0,
#   "createdAt": "2026-05-10T..."
# }
```

**결과**: Post 생성 ✅

---

### Step 5: Global Create-Post로 완료 소식 전파 (구 Brain Update)

```bash
gobi global create-post \
  --vault-slug gobi-cli-study \
  --title "🎓 GOBI CLI v2.0 학습 완료!" \
  --content "M1~M4 전체 모듈 완료:
✅ M1: 설치/인증/핵심 개념
✅ M2: Vault Publish, Global Posts, Session
✅ M3: Space & Post 협업 (Thread→Post 변경)
✅ M4: 실전 워크플로우 + Quick Reference

VibeLearn AI v2.0 방법론으로 체계적으로 정리했습니다. 💪"

# 결과: Post created successfully ✅
```

> **v2.0 변경**: `gobi brain post-update` → `gobi global create-post`

---

### Step 6: 로컬 파일 동기화 (Vault Sync)

학습 산출물 폴더 전체를 Gobi 서버(Webdrive)에 안전하게 백업하고 동기화합니다.

```bash
gobi vault sync \
  --path "Topics/GOBI-CLI" \
  --upload-only

# 결과:
# Syncing...
# [Upload] Topics/GOBI-CLI/topic_info.md
# [Upload] Topics/GOBI-CLI/04-Capstone/guides/complete-workflow.md
# ...
# Sync completed successfully ✅
```

> **v2.0 변경**: `gobi sync` → `gobi vault sync`

---

## 전체 워크플로우 요약

```
1. gobi auth status                   → 인증 확인
2. gobi global feed / space feed      → 관련 지식 탐색 (구 brain search)
3. gobi session list/get/create-reply → Session 확인 및 대화 (구 brain ask)
4. gobi space create-post             → 팀 공유 Post 게시 (구 create-thread)
5. gobi global create-post            → Global 업데이트 게시 (구 brain post-update)
6. gobi vault sync                    → 로컬-서버 파일 동기화 (구 gobi sync)
```

**6개 단계로 완성되는 GOBI CLI v2.0 핵심 워크플로우** ✅

---

## 자동화 스크립트 예시 (v2.0)

반복 작업을 쉘 스크립트로 자동화할 수 있습니다:

```bash
#!/bin/bash
# gobi-daily-check.sh — 매일 아침 실행

VAULT="gobi-cli-study"
SPACE="changbal"
DATE=$(date +%Y-%m-%d)

echo "=== GOBI Daily Check: $DATE ==="

# 1. 인증 확인
echo "[1] 인증 상태:"
gobi auth status

# 2. 최신 Global Posts 확인 (구 Brain Updates)
echo ""
echo "[2] 최신 Global Posts:"
gobi global list-posts --mine --limit 3

# 3. 오늘의 Space Posts 확인 (구 Threads)
echo ""
echo "[3] 최신 Space Posts:"
gobi space list-posts --space-slug $SPACE --limit 5

# 4. 내 Session 목록
echo ""
echo "[4] 최근 Sessions:"
gobi session list --limit 3

echo ""
echo "=== Done ==="
```

---

## 트러블슈팅 핵심 (v2.0 기준)

| 증상 | 원인 | 해결 |
|------|------|------|
| `gobi brain search` → command not found | v2.0에서 CLI 제거됨 | 웹 UI(gobispace.com) 또는 `global feed` 사용 |
| `gobi brain ask` → command not found | v2.0에서 CLI 제거됨 | 웹 UI에서 새 Session 시작 후 `session list`로 확인 |
| `gobi session reply` → 오류 | v2.0에서 명령어 변경됨 | `gobi session create-reply` 사용 |
| `gobi sync` → command not found | v2.0에서 명령어 변경됨 | `gobi vault sync` 사용 |
| `gobi init` → command not found | v2.0에서 명령어 변경됨 | `gobi vault init` 사용 |
| `gobi vault init` → 입력 없음 | 완전 인터랙티브 명령어 | 인터랙티브 터미널에서 직접 실행 |
| `--space-slug` 없이 실행 오류 | `gobi space warp` 미실행 | 각 명령어에 `--space-slug` 직접 지정 |

---

> **다음 문서**: [quick-reference.md](quick-reference.md)
> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **CVL 기준**: v2.0.12 (2026-05-10)
