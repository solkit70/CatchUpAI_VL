# GOBI CLI 학습 — Topic 인덱스

> **Topic**: GOBI-CLI
> **방법론**: VibeLearn AI v2.0
> **최초 완료일**: 2026-03-29
> **CVL 업데이트**: 2026-06-27 (GOBI CLI v2.0.35 반영 — session/saved/draft 제거, personal/artifact 추가)
> **상태**: 완료, CVL 최신화 완료

## 이 Topic에 대하여

GOBI CLI(`@gobi-ai/cli`)는 GOBI 플랫폼을 터미널과 AI 에이전트 환경에서 사용할 수 있게 해주는 커맨드라인 도구입니다. v2.0.35 기준으로 `vault`, `global`, `personal`, `artifact`, `media`, `space`, `sense` 명령 그룹으로 구성됩니다. (v2.0.19까지 있던 `session`, `saved`, `draft`는 v2.0.35에서 제거됨)

이 Topic을 마치면 다음을 수행할 수 있습니다.

- GOBI CLI를 설치하고 device-code flow로 인증할 수 있다.
- `gobi vault init`으로 Vault를 초기화하고 `PUBLISH.md`를 발행할 수 있다.
- `global` 포스트, `personal` 프라이빗 포스트, `space` Post/Reply, `artifact` 버전관리 콘텐츠를 구분할 수 있다.
- v0.6.x 문서나 예전 명령어를 v2.0.35 명령어로 변환할 수 있다.
- `space search-posts`, `react/unreact`, 채널 관련 신규 기능을 활용할 수 있다.

## 모듈 목록

| 모듈 | 제목 | 상태 | 링크 |
|------|------|------|------|
| M1 | 설치 & 인증 & 핵심 개념 | 완료, v2.0.12 반영 | [01-Setup-Auth/README.md](01-Setup-Auth/README.md) |
| M2 | Vault/Global/Session 명령어 | 완료, v2.0.12 반영 | [02-Brain-Session/README.md](02-Brain-Session/README.md) |
| M3 | Space Post & Reply 협업 기능 | 완료, v2.0.12 반영 | [03-Space-Thread/README.md](03-Space-Thread/README.md) |
| M4 | 실전 워크플로우 + Quick Reference | 완료, v2.0.12 반영 | [04-Capstone/README.md](04-Capstone/README.md) |

## 처음 시작하는 분께

순서대로 읽으세요.

1. [01-Setup-Auth/README.md](01-Setup-Auth/README.md) — 설치, 인증, Vault 초기화
2. [02-Brain-Session/README.md](02-Brain-Session/README.md) — Vault 발행, Global Post, Session 관리
3. [03-Space-Thread/README.md](03-Space-Thread/README.md) — Space Post/Reply 협업
4. [04-Capstone/README.md](04-Capstone/README.md) — 전체 워크플로우와 Quick Reference

바로 명령어 참조가 필요하면 [04-Capstone/guides/quick-reference.md](04-Capstone/guides/quick-reference.md)를 보세요.

## 핵심 개념 한눈에 보기 (v2.0.35)

```text
Vault
├── PUBLISH.md          # vault publish 대상
├── .gobi/settings.yaml # vault 설정
├── .gobi/syncfiles     # vault sync 대상 패턴
└── Space
    ├── Channel         # 채널 (v2.0.35 신규)
    └── Post
        ├── Reply
        └── Artifact    # 버전관리 콘텐츠 (v2.0.35 신규)

Global Feed             # 공개 개인 포스트
Personal Feed           # 프라이빗 개인 포스트 (v2.0.35 신규)
Media                   # 이미지/영상/아바타 생성 (v2.0.35에서 대폭 확장)
Sense                   # 활동/전사 데이터

── v2.0.35에서 제거됨 ──
Session ❌              # 1:1 AI 대화 (CLI 제거 → 웹 UI만 가능)
Saved ❌                # 개인 노트 + 북마크 (CLI 제거)
Draft ❌                # 에이전트 standing guidance (CLI 제거)
```

## v2.0.12 주요 변경

| v0.6.x | v2.0.12 |
|---|---|
| `gobi init` | `gobi vault init` |
| `BRAIN.md` | `PUBLISH.md` |
| `gobi brain publish` | `gobi vault publish` |
| `gobi brain post-update` | `gobi global create-post` |
| `gobi brain list-updates` | `gobi global list-posts --mine` |
| `gobi space create-thread` | `gobi space create-post` |
| `gobi space list-threads` | `gobi space list-posts` |
| `gobi session reply` | `gobi session create-reply` |
| `gobi sync` | `gobi vault sync` |

## CVL WorkLog

- [vl_worklog/20260627_CVL_GOBI-CLI.md](vl_worklog/20260627_CVL_GOBI-CLI.md) — GOBI CLI v2.0.35 업데이트 동기화 (session/saved/draft 제거, personal/artifact/채널 신규)
- [vl_worklog/20260529_CVL_GOBI-CLI.md](vl_worklog/20260529_CVL_GOBI-CLI.md) — GOBI CLI v2.0.19 업데이트 동기화 (vault CRUD + 미디어 첨부)
- [vl_worklog/20260510_CVL_GOBI-CLI.md](vl_worklog/20260510_CVL_GOBI-CLI.md) — GOBI CLI v2.0.12 업데이트 동기화
- [vl_worklog/20260424_CVL_GOBI-CLI.md](vl_worklog/20260424_CVL_GOBI-CLI.md) — 이전 CVL 기록

## 학습 산출물

| 폴더 | 내용 |
|------|------|
| `01-Setup-Auth/` | 설치, 인증, Vault 초기화, 핵심 개념 |
| `02-Brain-Session/` | Vault 발행, Global Post, Session 관리 |
| `03-Space-Thread/` | Space Post/Reply 협업 기능 |
| `04-Capstone/` | E2E 워크플로우와 Quick Reference |
| `vl_worklog/` | 학습 일지와 CVL 기록 |
| `vl_roadmap/` | 원 학습 로드맵 |

## GitHub

이 Topic의 전체 산출물은 공개되어 있습니다:
https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/GOBI-CLI

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
