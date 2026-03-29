# GOBI CLI 학습 — Topic 인덱스

> **Topic**: GOBI-CLI
> **방법론**: VibeLearn AI v2.0
> **기간**: 2026-03-29 (단일 세션 완료)
> **총 소요 시간**: ~6시간
> **상태**: ✅ 완료

---

## 이 Topic에 대하여

GOBI CLI(`@gobi-ai/cli`)는 [GOBI 플랫폼](https://gobispace.com)의 커맨드라인 도구입니다.
Brain(AI 지식 자원), Space(팀 협업 공간), Thread(토론), Session(AI 대화)을 터미널에서 관리합니다.

**이 Topic을 마치면**:
- GOBI CLI를 설치하고 인증할 수 있다
- Brain을 검색하고 AI 질의를 할 수 있다
- BRAIN.md를 작성하고 발행할 수 있다
- Space Thread/Reply를 생성/수정/삭제할 수 있다
- 실전 End-to-End 워크플로우를 수행할 수 있다

---

## 모듈 목록

| 모듈 | 제목 | 상태 | 링크 |
|------|------|------|------|
| M1 | 설치 & 인증 & 핵심 개념 | ✅ 완료 | [01-Setup-Auth/README.md](01-Setup-Auth/README.md) |
| M2 | Brain & Session 명령어 마스터 | ✅ 완료 | [02-Brain-Session/README.md](02-Brain-Session/README.md) |
| M3 | Space & Thread 협업 기능 | ✅ 완료 | [03-Space-Thread/README.md](03-Space-Thread/README.md) |
| M4 | 실전 워크플로우 + 교과서 완성 | ✅ 완료 | [04-Capstone/README.md](04-Capstone/README.md) |

---

## 처음 시작하는 분께

**순서대로 읽으세요**:

1. 👉 [01-Setup-Auth/README.md](01-Setup-Auth/README.md) — 설치부터 시작
2. [02-Brain-Session/README.md](02-Brain-Session/README.md) — Brain 다루기
3. [03-Space-Thread/README.md](03-Space-Thread/README.md) — 팀 협업
4. [04-Capstone/README.md](04-Capstone/README.md) — 전체 워크플로우

**바로 명령어 참조가 필요하다면**:
- [04-Capstone/guides/quick-reference.md](04-Capstone/guides/quick-reference.md) — 전체 Quick Reference

---

## 핵심 개념 한눈에 보기

```
Vault (최상위 지식 컨테이너 — GitHub Organization 비유)
└── Space (팀 협업 공간 — GitHub Repository 비유)
    ├── Brain (AI 지식 자원 — Wiki + AI)
    │   ├── Session (1:1 AI 대화)
    │   └── Updates (팀 피드)
    └── Thread (팀 토론)
        └── Reply (답글)
```

---

## 알려진 이슈 (v0.6.15)

- `gobi session list/get/reply` → **HTTP 404** (서버 엔드포인트 미매칭)
- 자세한 내용: [vl_worklog/ISSUE_REPORT_GOBI-CLI.md](vl_worklog/ISSUE_REPORT_GOBI-CLI.md)

---

## 학습 산출물

| 폴더 | 내용 |
|------|------|
| `01-Setup-Auth/` | 설치 가이드, 핵심 개념 문서 |
| `02-Brain-Session/` | Brain 검색/발행/updates 가이드, Session 이슈 문서 |
| `03-Space-Thread/` | Space 탐색, Thread CRUD 가이드 |
| `04-Capstone/` | E2E 워크플로우, Quick Reference |
| `vl_worklog/` | 학습 일지 (M1~M4 + Issue Report) |
| `vl_roadmap/` | 학습 로드맵 |

---

## GitHub

이 Topic의 전체 산출물은 공개되어 있습니다:
https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/GOBI-CLI

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **완료일**: 2026-03-29
