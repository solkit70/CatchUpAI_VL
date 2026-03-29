# WorkLog — M2 Day 1 | GOBI-CLI

> **날짜**: 2026-03-29 (토)
> **Topic**: GOBI-CLI
> **모듈**: M2 — Brain & Session 명령어 마스터
> **학습 시간**: ~2시간
> **방법론**: VibeLearn AI v2.0

---

## 🎯 오늘의 목표

| 항목 | 상태 |
|------|------|
| gobi brain search 실습 | ✅ 완료 |
| gobi brain ask → Session 생성 | ✅ 완료 |
| gobi session list/get/reply | ✅ 실습 (⚠️ API 이슈 발견) |
| BRAIN.md 작성 → gobi brain publish | ✅ 완료 |
| brain updates CRUD | ✅ 완료 |
| 산출물 문서 작성 | ✅ 완료 |

---

## 📚 진행 내용

### 1. gobi brain search

```bash
gobi brain search --query "getting started"   # similarity 최고: 0.409
gobi brain search --query "건강 앱"           # similarity 최고: 0.605 ← 한국어 우수
gobi brain search --query "CLI tool"          # similarity 최고: 0.396
gobi brain search --query "건강 앱" --json    # JSON 구조 파악
```

**핵심 발견:**
- 한국어 쿼리 + 한국어 Brain = 높은 similarity (0.6+)
- 영어 쿼리는 0.4 내외로 낮음
- 항상 20개 결과 반환 (페이지네이션 없음)
- JSON 구조: `vault.vaultId`, `owner.name`, `similarity`

---

### 2. gobi brain ask → Session 생성

```bash
gobi brain ask \
  --vault-slug changsoo_vault-df7y0c \
  --question "What is this brain about?" \
  --json
# → Session ID: 677 (숫자), UUID: 9b73ebfd-...
# → mode: manual

gobi brain ask ... --mode auto
# → Session ID: 678, mode: auto
```

**발견:** Session ID가 숫자(`id`)와 UUID(`sessionId`) 두 형식으로 반환됨

---

### 3. Session 명령어 → API 이슈 발견

```bash
gobi session list   # → HTTP 404
gobi session get 677  # → HTTP 404
gobi session reply 677 --content "..."  # → HTTP 404
```

**이슈 내용:** CLI v0.6.15의 session 관련 API 엔드포인트가 서버와 불일치
- `/chat/my-sessions` → 404
- `/chat/677` → 404
- `/chat/677/reply` → 404
- Brain ask로 Session 생성은 성공 (API 일부만 불일치)

**추가 발견:** `gobi session reply`의 올바른 옵션은 `--content` (Roadmap의 `--message`는 틀림)

---

### 4. BRAIN.md 작성 및 publish

BRAIN.md에 다음 내용 추가:
- Frontmatter: title, tags, description, prompt 완성
- Core Concepts 표
- Key Commands 섹션
- Learning Progress 체크리스트

```bash
gobi brain publish
# → Published BRAIN.md to vault "gobi-cli-study" ✅
```

---

### 5. brain updates CRUD 전체 사이클

```bash
# Create
gobi brain post-update --title "M1 완료" --content "..." --json
# → ID: 255

# Read
gobi brain list-updates
# → 전체 사용자 피드 20개 표시 (내 것 포함)

# Update
gobi brain edit-update 255 --content "수정된 내용" --json
# → editedAt 필드 추가됨

# Delete
gobi brain delete-update 255
# → Brain update 255 deleted ✅

# 최종 Update (학습 시작 공유용)
gobi brain post-update --title "GOBI CLI 학습 시작 🚀" --content "..."
# → ID: 256
```

**발견:** `list-updates`는 내 업데이트만이 아닌 **전체 팀 피드** 표시

---

## 📊 M2 DoD 체크리스트

- [x] `gobi brain search` 다양한 쿼리 실험 + JSON 구조 파악
- [x] `gobi brain ask` Session 생성 성공 (ID 677, 678)
- [x] `gobi session list/get/reply` 실습 (⚠️ HTTP 404 이슈 문서화)
- [x] `BRAIN.md` 작성 + `gobi brain publish` 발행 성공
- [x] brain updates CRUD (post → list → edit → delete) 완료
- [x] `brain-search-guide.md` 작성 (실제 결과 포함)
- [x] `session-management.md` 작성 (이슈 상세 포함)
- [x] `brain-publish-guide.md` + `sample-brain.md` 작성
- [x] `02-Brain-Session/README.md` 작성

**M2 완료** ✅

---

## 💡 Daily Retrospective

### What went well (잘된 점)
- brain search/ask/publish/updates 핵심 기능 전체 실습 완료
- API 이슈를 발견하고 상세히 문서화 → 다른 학습자에게 귀중한 정보
- `publish` vs `post-update` 차이를 실제 사용으로 명확히 이해
- JSON 출력으로 API 응답 구조까지 파악

### What could be improved (개선할 점)
- session list/get/reply가 작동하지 않아 멀티턴 대화 실습 미완
- gobispace.com 웹에서 Session 확인하는 것을 추가로 해봤으면 좋았을 것

### Insights (인사이트)
- `brain ask`는 Session을 **생성만** 하고 응답은 비동기로 처리됨 (web에서 확인)
- `brain publish`와 `post-update`는 완전히 다른 목적: 지식 베이스 갱신 vs 팀 피드
- `list-updates`가 전체 사용자 피드를 보여주는 것은 **소셜 피드 기능** — 커뮤니티 학습 도구
- CLI v0.6.15 session 이슈는 GOBI 팀에 GitHub 이슈로 보고할 가치 있음

### Tomorrow's focus (다음 세션 집중할 것)
- **M3 시작**: Space & Thread 협업 기능
  - `gobi space list` — Space 목록 확인
  - `gobi space warp` — 활성 Space 선택
  - `gobi space list-threads` — Thread 목록
  - `gobi space create-thread` — 새 Thread 작성
  - `gobi space create-reply` — Thread 답글
  - Thread CRUD 전체 흐름

---

## 🐛 이슈 로그

### 이슈 2: session list/get/reply → HTTP 404

**발견일**: 2026-03-29
**대상 명령어**: `gobi session list`, `gobi session get`, `gobi session reply`
**오류**: `API error (HTTP 404): Cannot GET /chat/my-sessions?limit=20`

**상세 분석**:
- Brain ask로 Session 생성은 성공 (ID 반환 확인)
- Session 조회/답장만 404 → API 엔드포인트 분리 변경으로 추정
- 정확한 Session ID 형식 미확인 (숫자 vs UUID 중 어느 것이 올바른지)

**조치 필요**:
- [ ] GOBI 팀에 GitHub 이슈 보고
- [ ] 웹 플랫폼에서 Session 동작 확인

### 이슈 3: Roadmap 명령어 오류 (--message → --content)

**발견일**: 2026-03-29
**내용**: `gobi session reply`의 올바른 플래그는 `--content` (Roadmap에 `--message`로 잘못 기재)
**조치**: session-management.md에 올바른 옵션 명시 완료

---

## 📂 생성된 산출물

| 파일 | 설명 |
|------|------|
| `02-Brain-Session/README.md` | M2 모듈 인덱스 |
| `02-Brain-Session/guides/brain-search-guide.md` | brain search + ask 가이드 (실습 결과 포함) |
| `02-Brain-Session/guides/brain-publish-guide.md` | BRAIN.md + publish + updates CRUD 가이드 |
| `02-Brain-Session/guides/session-management.md` | session 명령어 + v0.6.15 이슈 상세 |
| `02-Brain-Session/examples/sample-brain.md` | 재사용 가능한 BRAIN.md 템플릿 |
| `BRAIN.md` | vault "gobi-cli-study" Brain 발행 완료 |

---

> **WorkLog 작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **다음 WorkLog**: `20260329_M3_Day1_GOBI-CLI.md` 또는 `20260330_M3_Day1_GOBI-CLI.md`
