# 🔄 CVL WorkLog: GOBI-CLI v2.0 업데이트 동기화

**작성일**: 2026-05-10
**세션 유형**: CVL (Continuous Vibe Learning) - 업데이트 동기화 세션
**Topic**: GOBI-CLI
**관련 업데이트 기간**: 2026-04-24 ~ 2026-05-10
**이전 CVL**: 20260424_CVL_GOBI-CLI.md

---

## 🔄 Continuous Vibe Learning - 업데이트 개요

### 동기화 일시
2026-05-10

### 버전 변화
- **이전 CVL 기준**: v0.9.x 이후 구조 (brain/space/session/sync/sense)
- **현재 버전**: v2.0.12 (2026-05-10 출시)
- **영향도**: 🔴 **대규모** — 메이저 버전 전환, 핵심 아키텍처 재편

---

## 📋 GOBI CLI v2.0 주요 변경사항

### Breaking Change 1: `gobi init` → `gobi vault init` 🔴

**내용**: 초기화 명령어가 `gobi vault` 그룹으로 이전
- `gobi init` → `gobi vault init`
- 구 `BRAIN.md` → **`PUBLISH.md`** 로 대체
- **의의**: vault 관리 기능이 독립적인 명령어 그룹으로 분리

### Breaking Change 2: `gobi brain` 그룹 해체 🔴

**내용**: brain 명령어들이 기능별로 분산
| 구 명령어 | 새 명령어 |
|-----------|----------|
| `brain publish/unpublish` | `vault publish/unpublish` |
| `brain post-update` | `global create-post` |
| `brain list-updates` | `global list-posts --mine` |
| `brain edit-update` | `global edit-post` |
| `brain delete-update` | `global delete-post` |
| `brain search` / `brain ask` | 웹 UI / 세션 기반 |

### Breaking Change 3: Thread → Post 명칭 전면 변경 🔴

**내용**: space 그룹의 모든 명령어에서 `thread` → `post`
- `space list-threads` → `space list-posts`
- `space create-thread` → `space create-post`
- `space get-thread` → `space get-post`
- `space edit-thread` → `space edit-post`
- `space delete-thread` → `space delete-post`
- 신규: `space feed`, `space list-topics`, `space list-topic-posts`

### Breaking Change 4: `gobi session reply` → `gobi session create-reply` 🟡

**내용**: reply 서브명령어 명칭 변경
- **의의**: 명명 일관성 (`create-reply`) 확보

### 신규 명령어 그룹 5개 🆕

| 그룹 | 내용 |
|------|------|
| `gobi global *` | 개인 포스트 및 글로벌 피드 (구 brain updates 대체) |
| `gobi saved *` | 개인 노트 + 북마크 관리 |
| `gobi draft *` | 에이전트 standing guidance (시스템 프롬프트 자동 주입) |
| `gobi media *` | 이미지/영상/아바타 생성 |
| `gobi vault sync` | 로컬 ↔ WebDrive 파일 동기화 (구 gobi sync에서 이전, 옵션 대폭 확장) |

### API URL 변경 🟡

- 이전: `https://backend.joingobi.com`
- 현재: `https://api.joingobi.com`

---

## 📊 영향도 종합 평가

| 변경사항 | 영향도 | 조치 완료 |
|---------|--------|---------|
| `gobi init` → `gobi vault init` | 🔴 높음 | ✅ references/init.md 재작성 |
| `gobi brain` 그룹 해체 | 🔴 높음 | ✅ references/brain.md → deprecated 안내 |
| Thread → Post 명칭 변경 | 🔴 높음 | ✅ references/space.md + thread-management.md 업데이트 |
| BRAIN.md → PUBLISH.md | 🔴 높음 | ✅ SKILL.md 반영 |
| `session reply` → `create-reply` | 🟡 중간 | ✅ references/session.md 업데이트 |
| API URL 변경 | 🟡 중간 | ✅ SKILL.md 환경변수 섹션 반영 |
| 신규 global 그룹 | 🆕 신규 | ✅ references/global.md 생성 |
| 신규 saved 그룹 | 🆕 신규 | ✅ references/saved.md 생성 |
| 신규 draft 그룹 | 🆕 신규 | ✅ references/draft.md 생성 |
| 신규 media 그룹 | 🆕 신규 | ✅ references/media.md 생성 |
| sense 옵션 변경 | 🟢 소규모 | ✅ references/sense.md 생성 |

**전체 영향도**: 🔴 높음 (메이저 버전 전환 — 2시간 업데이트 세션 집행)

---

## 📝 업데이트 완료 파일 목록

### 수정 파일 — Skills (gobi-cli 스킬 업데이트)
- [x] `_Settings_/Skills/gobi-cli/SKILL.md` — v2.0.12 전체 재작성 (skill 버전 0.3.7)
- [x] `_Settings_/Skills/gobi-cli/references/auth.md` — device-code flow 설명 추가
- [x] `_Settings_/Skills/gobi-cli/references/init.md` — vault init으로 재작성
- [x] `_Settings_/Skills/gobi-cli/references/brain.md` — deprecated 안내 + 매핑 표
- [x] `_Settings_/Skills/gobi-cli/references/space.md` — thread→post 전면 업데이트
- [x] `_Settings_/Skills/gobi-cli/references/session.md` — create-reply 반영

### 신규 생성 파일 — Skills
- [x] `_Settings_/Skills/gobi-cli/references/vault.md`
- [x] `_Settings_/Skills/gobi-cli/references/global.md`
- [x] `_Settings_/Skills/gobi-cli/references/saved.md`
- [x] `_Settings_/Skills/gobi-cli/references/draft.md`
- [x] `_Settings_/Skills/gobi-cli/references/media.md`
- [x] `_Settings_/Skills/gobi-cli/references/sense.md`

### 수정 파일 — Topic 학습 산출물 업데이트 (2026-05-10 세션 2)
- [x] `01-Setup-Auth/concepts/core-concepts.md` — v2.0 개념 전면 재작성 (8개 핵심 개념)
- [x] `01-Setup-Auth/concepts/installation-guide.md` — device-code auth, vault init, PUBLISH.md
- [x] `02-Brain-Session/guides/brain-publish-guide.md` — vault publish + global posts 가이드로 재작성
- [x] `02-Brain-Session/guides/brain-search-guide.md` — brain search/ask CLI 제거 안내 + 대안 워크플로우
- [x] `02-Brain-Session/guides/session-management.md` — create-reply, 404 이슈 해결 반영
- [x] `03-Space-Thread/guides/thread-management.md` — Post 명칭 + v2.0 옵션 반영
- [x] `03-Space-Thread/guides/space-navigation.md` — list-posts/get-post + feed/topics 신규 명령어
- [x] `04-Capstone/guides/quick-reference.md` — v2.0.12 전면 재작성 (모든 명령어 그룹 갱신)
- [x] `04-Capstone/guides/complete-workflow.md` — 6단계 워크플로우 v2.0 전환 완료

---

## 🎯 오늘 배운 것

- GOBI CLI v2.0은 단순 기능 추가가 아닌 아키텍처 재편 — `brain` 중심에서 `vault + global + saved + draft + media` 분리 구조로 전환
- `draft` 그룹이 에이전트 협업의 핵심 — 시스템 프롬프트에 자동 주입되는 standing guidance 개념이 새로 도입됨
- CVL 프로세스의 중요성 재확인 — 2주 동안 major 버전이 바뀌어 기존 명령어가 전부 broken 상태가 됨

## ✅ 잘된 점

- VibeLearn AI CVL 프로세스를 체계적으로 따라 영향도 분석 → 파일 업데이트 순서로 진행
- 구 명령어 매핑 표를 references 파일에 포함해 이전 학습자도 빠르게 전환 가능

## 📋 다음 할 일

- [x] M1~M4 학습 가이드 전 파일 v2.0.12 업데이트 완료 (2026-05-10 세션 2)
- [ ] `gobi draft` 실습 (에이전트 standing guidance 워크플로우)
- [ ] `gobi media` 실습 (이미지/영상 생성)
- [ ] `gobi vault sync` 실습 (syncfiles 설정 + dry-run)
- [ ] Module README 파일들 버전 번호 업데이트 확인 (M1~M4)

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **마지막 업데이트**: 2026-05-10
