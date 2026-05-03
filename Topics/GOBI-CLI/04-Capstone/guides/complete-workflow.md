# GOBI CLI — End-to-End 완전 워크플로우

> **모듈**: M4 — 실전 워크플로우 + 교과서 완성 (Capstone)
> **작성일**: 2026-03-29
> **버전**: GOBI CLI v0.6.15

---

## 워크플로우 개요

M1~M3에서 배운 모든 명령어를 실전 시나리오로 연결한 End-to-End 흐름입니다.

```
인증 확인 → Brain 검색/질의 → Space Thread 생성 → Brain 업데이트 게시
     ↓              ↓                  ↓                    ↓
 auth status   brain search        create-thread        post-update
               brain ask           create-reply         list-updates
```

---

## 시나리오: "학습 완료 알림 + 팀 공유" 워크플로우

### Step 1: 인증 상태 확인

```bash
gobi auth status

# 결과:
# Authenticated
# User: Changsoo Park (solkit70@gmail.com)
# Vault: gobi-cli-study
```

**M4 실습 결과**: 인증 정상 ✅

---

### Step 2: Brain 검색으로 관련 지식 자원 확인

```bash
gobi brain search --query "GOBI CLI"

# 결과:
# Brain Search Results:
# 1. [gobi-cli-study] GOBI CLI Study Brain  ← 우리 Brain!
#    Similarity: 0.911
#    By: Changsoo Park
#    Tags: gobi-cli, learning, vibelearn-ai, cli-tool
#
# 2. [gobi-brain] Gobi Brain
#    Similarity: 0.743
#
# 3. [changbal-brain] Changbal Brain
#    Similarity: 0.512
```

**핵심 발견**: 우리가 publish한 `gobi-cli-study` Brain이 **similarity 0.911**로 1위 ✅
→ BRAIN.md 내용이 정확히 인덱싱되었음을 확인

---

### Step 3: Brain에 질의 (AI 대화 세션 생성)

```bash
gobi brain ask \
  --vault-slug gobi-cli-study \
  --question "What GOBI CLI commands are covered in this brain?" \
  --json

# 응답:
# {
#   "id": 679,
#   "sessionId": "uuid-...",
#   "answer": "This brain covers the following GOBI CLI commands:
#     1. gobi auth (login/status/logout)
#     2. gobi brain (search/ask/publish/post-update...)
#     3. gobi space (list/warp/list-threads/get-thread/create-thread...)
#     4. gobi session (list/get/reply - v0.6.15 issues noted)
#     ...",
#   "vaultSlug": "gobi-cli-study",
#   "createdAt": "2026-03-29T..."
# }
```

**결과**: Session 679 생성 ✅ — Brain이 M1~M3 내용을 정확히 답변

> **참고**: `session list/get/reply`는 v0.6.15에서 HTTP 404 이슈. Brain ask로 생성된 세션은
> gobispace.com 웹에서 확인 가능.

---

### Step 4: Space에 학습 완료 Thread 게시

```bash
gobi space create-thread \
  --space-slug changbal \
  --title "GOBI CLI M4 Capstone: End-to-End 워크플로우 완성" \
  --content "M1~M4 Capstone까지 GOBI CLI 전체 학습 완료했습니다. 🎉

학습 내용:
- M1: 설치/인증/핵심 개념 (Vault/Space/Brain/Thread/Session)
- M2: Brain 검색, BRAIN.md 발행, Brain Updates CRUD
- M3: Space/Thread CRUD 전체 (8개 명령어)
- M4: End-to-End 워크플로우 + Quick Reference 완성

전체 산출물: https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/GOBI-CLI

VibeLearn AI v2.0 방법론으로 학습 — 누구나 이 자료를 참고하여 따라할 수 있습니다." \
  --json

# 응답:
# {
#   "id": 735,
#   "title": "GOBI CLI M4 Capstone: End-to-End 워크플로우 완성",
#   "replyCount": 0,
#   "createdAt": "2026-03-29T..."
# }
```

**결과**: Thread 735 생성 ✅

---

### Step 5: Brain Update로 완료 소식 전파

```bash
gobi brain post-update \
  --vault-slug gobi-cli-study \
  --content "🎓 GOBI CLI 학습 M4 Capstone 완료!

M1~M4 전체 모듈 완료:
✅ M1: 설치/인증/핵심 개념
✅ M2: Brain & Session 마스터
✅ M3: Space & Thread 협업
✅ M4: 실전 워크플로우 + Quick Reference

학습 산출물은 GitHub에서 누구나 열람 가능합니다.
VibeLearn AI v2.0 방법론으로 체계적으로 정리했습니다. 💪"

# 결과: Update posted successfully ✅
```

---

### Step 6: 로컬 파일 동기화 (Webdrive Sync) 🆕

학습 산출물 폴더 전체를 Gobi 서버(Webdrive)에 안전하게 백업하고 동기화합니다.

```bash
gobi sync \
  --path "Topics/GOBI-CLI" \
  --upload-only

# 결과:
# Syncing...
# [Upload] Topics/GOBI-CLI/topic_info.md
# [Upload] Topics/GOBI-CLI/04-Capstone/guides/complete-workflow.md
# ...
# Sync completed successfully ✅
```

---

## 전체 워크플로우 요약

```
1. gobi auth status              → 인증 확인
2. gobi brain search --query ... → 관련 Brain 탐색
3. gobi brain ask --vault-slug   → AI 질의 (Session 생성)
4. gobi space create-thread      → 팀 공유 Thread 게시
5. gobi brain post-update        → Brain Feed 업데이트
6. gobi sync                     → 로컬-서버 파일 동기화
```

**6개 명령어, 6단계로 완성되는 GOBI CLI 핵심 워크플로우** ✅

---

## 자동화 스크립트 예시

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

# 2. 최신 Brain Updates 확인
echo ""
echo "[2] 최신 Brain Updates:"
gobi brain list-updates --vault-slug $VAULT --limit 3

# 3. 오늘의 Thread 확인
echo ""
echo "[3] 최신 Threads:"
gobi space list-threads --space-slug $SPACE --limit 5

echo ""
echo "=== Done ==="
```

---

## 트러블슈팅 핵심

| 증상 | 원인 | 해결 |
|------|------|------|
| `session list/get/reply` → HTTP 404 | v0.6.15 서버 엔드포인트 미매칭 | 웹(gobispace.com)에서 확인 |
| `gobi init` → "User force closed the prompt" | 비인터랙티브 환경 | 인터랙티브 터미널에서 직접 실행 |
| Brain search 결과 유사도 낮음 | 언어 불일치 (한글 Brain에 영어 쿼리) | 쿼리 언어를 Brain 언어와 맞춤 |
| `--space-slug` 없이 실행 오류 | `gobi space warp` 미실행 | 각 명령어에 `--space-slug` 직접 지정 |

---

> **다음 문서**: [quick-reference.md](quick-reference.md)
> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
