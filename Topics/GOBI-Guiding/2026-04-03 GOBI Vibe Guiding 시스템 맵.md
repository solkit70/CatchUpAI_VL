---
title: "GOBI Vibe Guiding 시스템 맵"
created: 2026-04-03
tags:
  - gobi
  - vibe-guiding
  - system-map
  - reference
---

## 개요

GOBI에 Vibe Guiding을 적용하기 위해 파악하고 활용해야 할 시스템들의 전체 지도.

## 시스템 전체 구조

```
[소스]                        [문서화 파이프라인]               [가이딩]
gobi-ai/gobi-monorepo
  /specs (spec 파일 작성)
        ↓
gobi-ai/docs (Public)
        ↓ deploy
  docs.gobihq.com          →  Vibe Guiding
  (사용자 매뉴얼)               (Context → 사용자 맞춤 안내)
```

---

## 1. GitHub 레포지토리 (소스 코드)

| 레포                    | 링크                                       | 공개 여부   | 설명                                                        | 접근 권한                    |
| --------------------- | ---------------------------------------- | ------- | --------------------------------------------------------- | ------------------------ |
| gobi-ai/gobi-web      | https://github.com/gobi-ai/gobi-web      | Private | Gobi Space 웹 앱                                            | ✅                        |
| gobi-ai/gobi-desktop  | https://github.com/gobi-ai/gobi-desktop  | Private | Gobi Desktop (Mac/Windows)                                | ✅                        |
| gobi-ai/gobi-cli      | https://github.com/gobi-ai/gobi-cli      | Public  | Gobi CLI 도구                                               | ✅ 학습 완료 (GOBI-CLI Topic) |
| gobi-ai/gobi-monorepo | https://github.com/gobi-ai/gobi-monorepo | Private | 전체 제품 스펙 통합 레포 — `/specs`에 초기 스펙 생성됨 (2026-04-06 Mika 확인) | ✅                        |
| gobi-ai/docs          | https://github.com/gobi-ai/docs          | Public  | docs.gobihq.com 소스 — gobi-monorepo/specs 내용을 받아 deploy    | ✅                        |
| jykim/AI4PKM          | https://github.com/jykim/AI4PKM          | Public  | AI4PKM CLI 백엔드                                            | ✅                        |
| jykim/ai4pkm-vault    | https://github.com/jykim/ai4pkm-vault    | Public  | AI4PKM Vault                                              | ✅                        |

- **GitHub 계정**: solkit70
- **초대자**: Mika (GitHub: @gpminsuk)

---

## 2. GOBI 제품군 (가이딩 대상)

| 제품 | 설명 | 스펙 시트 탭 |
|------|------|------------|
| Gobi Desktop | Mac/Windows GUI 앱, 로컬 파일 관리 | Gobi Desktop |
| Gobi Space | 웹 기반 팀 협업 공간, 사용자 네트워크 | Gobi Space |
| Gobi CLI | 지식과 Space를 연결하는 CLI 브릿지 | Gobi CLI |
| Gobi Mobile | 모바일 앱 | Gobi Mobile |
| Astra | (세부 파악 필요) | Astra |

---

## 3. 문서화 시스템

### Gobi Specs Google Sheet
- **링크**: https://docs.google.com/spreadsheets/d/1eWGs38ObnjRjOHFY2_Du0TENtM3CSj6I/edit?usp=sharing
- **공유자**: Greg Moon (greg@joingobi.com) — 편집 권한
- **컬럼**: File Name / Description of Spec / Link to Spec / Version / Status / Date Updated / **Core Concept**
- **나의 역할**: Core Concept 컬럼 채우기 (Greg과 협업)
- **탭**: Gobi Desktop / Gobi Space / Astra / Gobi CLI / Gobi Mobile

### docs.gobihq.com
- **파이프라인**: `gobi-ai/gobi-monorepo/specs` → `gobi-ai/docs` (Public) → deploy → `docs.gobihq.com`
- GOBI 개발팀(Mika, Greg)이 gobi-monorepo/specs에 spec 파일 작성 중
- 사용자가 제품별 매뉴얼을 찾아볼 수 있는 공식 문서 사이트
- Vibe Guiding의 핵심 소스 컨텍스트로 활용 예정
- **상태**: 작성 중 (내용 파악 필요)

### Greg의 Docs Sync 자동화 워크플로우 (2026-04-07 Slack)
> Greg이 docs.gobihq.com을 위한 자동화 파이프라인을 개발 중

```
Dev team (Mika atm) pushes changes to specs/ in gobi-monorepo
        ↓
GitHub Action triggers in gobi-monorepo
        ↓
Claude API reads changed spec file
        ↓
Translates to user-facing MDX (strips implementation details)
        ↓
Commits updated .mdx to gobi-ai/docs
        ↓
Mintlify auto-deploys
```

**Specs 업데이트 역할 분담** (Greg → Mika FYI):
- **Dev updates (Greg)**: 기술적 스펙 세부 사항, 기능 동작 방식, 새 기능 스펙 파일
- **Greg updates**: 스펙 내 제품 포지셔닝, 명명/용어 결정, 각 스펙의 Core Concepts 섹션

**Spec → Doc 페이지 매핑** (Greg 현재 구상):
| Spec 파일 | Doc 페이지 |
|----------|-----------|
| 05-second-brain-agent.md | Desktop |
| 09-spaces.md | Personal Space + Community Space |
| 07-capture.md | Mobile |
| 20-terminal.md | CLI |

**미결 사항**:
- Anthropic API key 필요 (sync 스크립트용) — gobi-monorepo GitHub Secret으로 저장 예정
- 전체 spec → doc 페이지 매핑 Mika 확인 필요

### 기존 사이트 (대체 예정)
- https://www.aiforbetter.me/
- https://pub.aiforbetter.me/

---

## 4. 내가 직접 운영하는 시스템

| 시스템 | 역할 |
|--------|------|
| Claude Code (VS Code) | Vibe Learning 실행, 문서 자동 생성 |
| Changsoo Vault (Obsidian) | 지식 저장소, 아이디어 파편 관리 |
| Gobi Desktop | 로컬 Brain/Context 관리 |
| Gobi CLI | Gobi Space 연동 |

---

## 5. 협업 채널

| 채널 | 용도 | 담당자 |
|------|------|--------|
| Slack (GOBI 팀) | 일상 소통, 작업 공유 | Mika, Greg, Jin |
| GitHub | 소스코드 협업 | Mika (gpminsuk) |
| Google Sheets | Specs 공동 작업 | Greg Moon |
| docs.gobihq.com | 공식 문서 도메인 | Greg |

---

## 6. Vibe Guiding 적용 파이프라인 (목표)

```
GitHub 소스코드
      ↓
Vibe Learning → Core Concept + User Manual 자동 생성
      ↓
CVL (Continuous Vibe Learning) → 코드 변경 시 자동 업데이트
      ↓
Vibe Guiding → 각 GOBI 사용자에게 맞춤 안내 제공
```

---

## 7. 우선순위 파악 필요 항목

- [ ] docs.gobihq.com 접속 및 내용 파악
- [ ] Gobi Specs 시트 — Core Concept 컬럼 채우기 (제품별)
- [x] 전체 레포 접근 권한 확인 완료 (2026-04-06)
- [ ] Astra 제품이 무엇인지 파악
- [ ] Google Learn Your Way 직접 체험 후 설계에 반영
