# WorkLog — M1 Day 2 | GOBI-CLI

> **날짜**: 2026-03-29 (토)
> **Topic**: GOBI-CLI
> **모듈**: M1 — 설치 & 인증 & 핵심 개념
> **학습 시간**: ~2시간
> **방법론**: VibeLearn AI v2.0

---

## 🎯 오늘의 목표

| 항목 | 상태 |
|------|------|
| GOBI CLI 설치 + 버전 확인 | ✅ 완료 |
| gobi auth login 인증 | ✅ 완료 (이미 인증됨) |
| gobi init vault 선택/생성 | ✅ 완료 |
| 전체 명령어 탐색 (--help) | ✅ 완료 |
| core-concepts.md 산출물 작성 | ✅ 완료 |

---

## 📚 진행 내용

### 1. GOBI CLI 설치

```bash
node --version    # v22.15.0 ✅ (18+ 조건 충족)
npm --version     # v11.6.2

npm install -g @gobi-ai/cli
gobi --version    # → 0.6.15
```

**특이사항**: `prebuild-install@7.1.3 deprecated` 경고 발생 — 설치에는 영향 없음

---

### 2. 인증 확인

```bash
gobi auth status
# → Authenticated as Changsoo Park (solkit70@gmail.com)
```

별도 로그인 불필요 — 이미 인증 상태 유지 중.

---

### 3. gobi init — vault 생성

```bash
cd Topics/GOBI-CLI
gobi init
```

**선택**: "Create a new vault"

**결과**:
```
Created vault "gobi-cli-study" (gobi-cli-study)
Vault set to "gobi-cli-study" (gobi-cli-study)
Updated .gobi/settings.yaml
Created BRAIN.md
```

**생성된 파일**:
- `.gobi/settings.yaml` → `vaultSlug: gobi-cli-study`
- `BRAIN.md` → frontmatter만 있는 빈 Brain 파일

---

### 4. 전체 명령어 탐색

`--help` 플래그로 모든 명령어와 옵션을 직접 확인.

**Roadmap 대비 새로 발견된 명령어**:

| 명령어 | 설명 | 예상 용도 |
|--------|------|----------|
| `gobi sense activities` | 활동 기록 조회 | 사용자 행동 로그 |
| `gobi sense transcriptions` | 전사 기록 조회 | 회의/음성 전사 |
| `gobi sync` | 로컬 ↔ Webdrive 동기화 | 파일 전체 동기화 |
| `gobi space list` | Space 목록 | Roadmap에 없던 명령어 |

**Roadmap 수정 필요 사항**:
- `gobi session update` → v0.6.15에서 실제로는 존재하지 않음 (list/get/reply 3개만)
- `sense`, `sync` 명령어 추가 필요

---

### 5. 산출물 생성

```
01-Setup-Auth/
├── README.md                        ✅
├── concepts/
│   ├── core-concepts.md             ✅ (핵심 개념 5개 + Quick Reference)
│   └── installation-guide.md       ✅ (단계별 설치/인증 가이드)
└── examples/                        (M1 예제 파일 — 현재 비어있음)
```

---

## 📊 M1 DoD 체크리스트

- [x] `npm install -g @gobi-ai/cli` 설치 완료 (v0.6.15)
- [x] `gobi auth status` 인증 확인
- [x] `gobi init` vault "gobi-cli-study" 생성
- [x] 전체 명령어 탐색 (`--help`) 완료
- [x] `core-concepts.md` 작성 완료
- [x] `installation-guide.md` 작성 완료
- [x] `01-Setup-Auth/README.md` 작성 완료

**M1 완료** ✅

---

## 💡 Daily Retrospective

### What went well (잘된 점)
- 설치부터 산출물 작성까지 2시간 내에 M1 전체 완료
- 이미 인증 상태라서 로그인 단계 생략 → 시간 절약
- `--help` 직접 탐색으로 Roadmap에 없던 `sense`, `sync` 명령어 발견
- 실제 실행 결과를 바탕으로 정확한 문서 작성 (추측 아닌 실증)

### What could be improved (개선할 점)
- `gobi session update` 명령어가 실제로는 없음 → Roadmap 업데이트 필요
- `examples/` 폴더가 비어있음 → M2에서 실습 예제 파일 추가 예정

### Insights (인사이트)
- `gobi init`은 반드시 인터랙티브 터미널에서 직접 실행해야 함 (파이프/자동화 불가)
- BRAIN.md가 생성되는 위치 = vault 루트 (GOBI-CLI 폴더) → `gobi brain publish`의 원본
- `gobi sync`는 `gobi brain publish`보다 더 광범위한 동기화 — 차이점은 M2/M3에서 탐색 예정
- `gobi sense`는 활동/전사 기록 — 팀 협업 로그 관리에 특화된 것으로 추정

### Tomorrow's focus (다음 세션 집중할 것)
- **M2 시작**: Brain & Session 명령어 마스터
  - `gobi brain search --query "..."` 직접 실행
  - `gobi brain ask` → Session 생성 실습
  - `gobi session list / get / reply` 전체 흐름 실습
  - BRAIN.md 내용 채우기 → `gobi brain publish` 실행
  - `gobi brain list-updates` 확인

---

## 🐛 이슈 로그

### 이슈 1: Roadmap 명령어 불일치

**발견**: `gobi session update` 명령어가 v0.6.15에서 존재하지 않음
- Roadmap에는 `gobi session → list / get / reply / update` 로 명시
- 실제: `list / get / reply` 3개만 존재

**조치**: `core-concepts.md`에 정확한 명령어만 기재 완료
**Roadmap 업데이트**: M2 시작 전 반영 예정

---

## 📎 생성된 산출물

| 파일 | 설명 |
|------|------|
| `01-Setup-Auth/README.md` | M1 모듈 인덱스 (학습 순서 안내) |
| `01-Setup-Auth/concepts/core-concepts.md` | 핵심 개념 5개 + 전체 명령어 Quick Reference |
| `01-Setup-Auth/concepts/installation-guide.md` | 설치/인증/초기화 단계별 가이드 |
| `.gobi/settings.yaml` | vault 설정 (gobi init 생성) |
| `BRAIN.md` | Brain 발행용 원본 파일 (gobi init 생성) |

---

> **WorkLog 작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **다음 WorkLog**: `20260329_M2_Day1_GOBI-CLI.md` 또는 `20260330_M2_Day1_GOBI-CLI.md`
