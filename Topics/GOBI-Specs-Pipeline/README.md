# GOBI-Specs-Pipeline

**방법론**: CUA_VL (VibeLearn AI) | **상태**: ✅ 완료 | **기간**: 2026-04-06 ~ 2026-04-07 (2일, 약 9시간)

---

## Topic 소개

GOBI 개발팀이 운영하는 문서화 파이프라인(`gobi-monorepo/specs` → `gobi-ai/docs` → `docs.gobihq.com`)을 분석하고, **Vibe Guiding을 어떻게 접목할지 방향을 결정**하기 위한 학습입니다.

단순 기술 학습을 넘어, **GOBI 팀에 공유 가능한 Vibe Guiding 전략 제안서**를 산출물로 완성하는 것이 목표입니다.

---

## 핵심 발견 (3줄 요약)

1. **파이프라인 갭**: `gobi-monorepo/specs` → `gobi-ai/docs` 변환이 수동 — 이것이 VibeLearn AI(SPECS_TO_GUIDE)의 핵심 기회
2. **Phase 1은 지금 당장 가능**: `.gobi/settings.yaml` + Vibe Guiding 프롬프트 파일만으로 GOBI 팀 코드 변경 없이 앱 내 Vibe Guiding 구동
3. **CVL이 지속 가능성의 핵심**: specs 업데이트 → VibeLearn AI 자동 재실행 → Vibe Guiding 자동 개선

---

## 파이프라인 구조

```
gobi-monorepo/specs (26개 feature spec)
        ↓ ⚠️ 수동 변환 (자동화 없음)
gobi-ai/docs (Mintlify MDX)
        ↓ ✅ 자동 배포
docs.gobihq.com
```

**Vibe Guiding 통합 후**:

```
gobi-monorepo/specs
        ↓ VibeLearn AI (SPECS_TO_GUIDE) ← CVL 자동화
Vibe Guiding 프롬프트 + gobi-ai/docs
        ↓
앱 내 실시간 Vibe Guiding (Reflex) + docs.gobihq.com
```

---

## 모듈 구조

| 모듈 | 상태 | 학습 시간 | 폴더 |
|------|------|----------|------|
| M1: gobi-monorepo + gobi-ai/docs 전체 구조 파악 | ✅ 완료 | 3h | [01-Monorepo-Overview/](01-Monorepo-Overview/README.md) |
| M2: Vibe Guiding 핵심 Spec 파일 심층 분석 | ✅ 완료 | 3h | [02-Specs-Deep-Dive/](02-Specs-Deep-Dive/README.md) |
| M3: Capstone — Vibe Guiding 전략 제안서 | ✅ 완료 | 3h | [03-Capstone/](03-Capstone/README.md) |

---

## 산출물 목록

### M1 — 구조 파악
- [repo-structure.md](01-Monorepo-Overview/repo-structure.md) — 7개 프로젝트 + 26개 spec 분석표
- [pipeline-diagram.md](01-Monorepo-Overview/pipeline-diagram.md) — 현재 파이프라인 + Vibe Guiding 통합 다이어그램

### M2 — Spec 심층 분석
- [spec-analysis-second-brain-agent.md](02-Specs-Deep-Dive/spec-analysis-second-brain-agent.md) — System Prompt 주입으로 Vibe Guiding 즉시 구현
- [spec-analysis-voice-interaction.md](02-Specs-Deep-Dive/spec-analysis-voice-interaction.md) — Ambient Mode = Vibe Guiding 최적 음성 채널
- [spec-analysis-capture.md](02-Specs-Deep-Dive/spec-analysis-capture.md) — Capture 완료 후 Reflex = 골든 타이밍
- [spec-analysis-orchestration.md](02-Specs-Deep-Dive/spec-analysis-orchestration.md) — `.gobi/settings.yaml` Watch Pattern으로 Phase 1 구현
- [vibe-guiding-touchpoints.md](02-Specs-Deep-Dive/vibe-guiding-touchpoints.md) — 8개 접점 매트릭스 + Phase별 로드맵

### M3 — 전략 제안서
- [integration-options.md](03-Capstone/integration-options.md) — 4가지 통합 옵션 비교 분석
- [**vibe-guiding-strategy-proposal.md**](03-Capstone/vibe-guiding-strategy-proposal.md) — GOBI 팀 공유용 전략 제안서 ⭐
- [topic-retrospective.md](03-Capstone/topic-retrospective.md) — Topic 전체 회고

---

## 전략 제안 요약 (Phase 1/2/3)

| Phase | 기간 | 목표 | GOBI 팀 협업 |
|-------|------|------|------------|
| Phase 1 | 즉시 (1-2주) | Changsoo Vault에서 Reflex 기반 Vibe Guiding 프로토타이핑 | 불필요 |
| Phase 2 | 2-4주 | Vibe Guiding Skill 패키징 + docs 자동화 기여 | PR 리뷰 |
| Phase 3 | 1-3개월 | Ambient Mode 네이티브 통합 | 협업 필요 |

---

## 학습 환경

| 항목 | 내용 |
|------|------|
| 로컬 레포 | `C:\AI_study\2026\GOBI_VibeGuiding\gobi-monorepo\` (Private) |
| 로컬 레포 | `C:\AI_study\2026\GOBI_VibeGuiding\docs\` (Public) |
| GitHub | https://github.com/gobi-ai/gobi-monorepo |
| GitHub | https://github.com/gobi-ai/docs |
| 공식 문서 | https://docs.gobihq.com |

---

## WorkLog

| 날짜 | 모듈 | 링크 |
|------|------|------|
| 2026-04-06 | M1 | [20260406_M1_GOBI-Specs-Pipeline.md](vl_worklog/20260406_M1_GOBI-Specs-Pipeline.md) |
| 2026-04-07 | M2 | [20260407_M2_GOBI-Specs-Pipeline.md](vl_worklog/20260407_M2_GOBI-Specs-Pipeline.md) |
| 2026-04-07 | M3 | [20260407_M3_GOBI-Specs-Pipeline.md](vl_worklog/20260407_M3_GOBI-Specs-Pipeline.md) |

---

*방법론: CUA_VL (VibeLearn AI) — 작성자: Changsoo (Claude Code 활용)*
