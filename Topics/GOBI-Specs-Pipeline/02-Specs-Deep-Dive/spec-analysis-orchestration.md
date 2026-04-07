# Spec 분석: 19 - Orchestration & Automation

**분석일**: 2026-04-07
**원본 파일**: `gobi-monorepo/specs/19-orchestration-and-automation.md`
**Vibe Guiding 관련도**: ⭐⭐⭐ 핵심 (구현 메커니즘)

---

## 핵심 요약

Orchestration은 Vault별 백그라운드 데몬이 파일 변경·수동 트리거·스케줄을 감지하고 에이전트 워크플로우를 자동 실행하는 시스템. **Reflex = 설정 가능한 자동화 규칙**. Vibe Guiding을 앱 내에서 구현하는 핵심 메커니즘.

---

## 주요 기능 정리

| 기능 | 설명 |
|------|------|
| Orchestrator Daemon | Vault당 1개, 백그라운드 프로세스, Vault 활성화 시 자동 시작 |
| Orchestrator Settings | `.gobi/settings.yaml`에 설정 (프롬프트 경로, 출력 경로, 도구, Watch Patterns) |
| Workflow Nodes | 트리거 + 액션으로 구성된 자동화 단위 |
| Trigger 종류 | 파일 변경 / 수동 실행 / 스케줄(향후) |
| Claude Session Pool | Ready / Running / Dormant 상태 관리, 병렬 실행 지원 |
| Skills | Vault별 오케스트레이터 능력 라이브러리 |
| Tools | 에이전트가 사용할 수 있는 도구 목록 (파일 작업, 검색 등) |
| Logs | 실시간 로그 스트리밍, 영구 저장 |

---

## `.gobi/settings.yaml` 구조 (설정 포인트)

```yaml
orchestrator:
  enabled: true
  prompt_paths:
    - .gobi/prompts/main.md        # ← Vibe Guiding 프롬프트 여기에 추가
  output_paths:
    - .gobi/outputs/
  watch_patterns:
    - _Gobi_/Captures/**/*.md      # ← Capture 감지
    - _Gobi_/Notes/**/*.md
  tools:
    - file_read
    - file_write
    - search
    # ← Vibe Guiding 전용 도구 추가 가능
```

---

## Vibe Guiding 접점 분석

### 🎯 접점 1: Vibe Guiding을 Reflex(Workflow Node)로 구현

**가장 현실적이고 즉시 실현 가능한 접근법**

```yaml
# .gobi/settings.yaml
watch_patterns:
  - _Gobi_/Captures/**/*.md    # 새 캡처 감지
  - _Gobi_/Notes/**/*.md       # 새 노트 감지
```

```
트리거: 새 캡처 파일 생성
        ↓
Reflex 실행:
  에이전트가 캡처 내용 읽기
  → Brain에서 관련 지식 검색
  → 연결 포인트 / 다음 행동 제안
  → 결과를 .gobi/outputs/vibe-guide-{date}.md에 저장
```

**실현 가능성**: ✅ 매우 높음 — 현재 아키텍처에서 즉시 구현 가능

### 🎯 접점 2: Vibe Guiding 전용 System Prompt
`.gobi/settings.yaml`의 `prompt_paths`에 Vibe Guiding 전용 프롬프트 추가:

```markdown
# .gobi/prompts/vibe-guiding.md
You are a Vibe Guide for the GOBI ecosystem.
When the user captures new content, your role is to:
1. Connect new captures to existing Brain knowledge
2. Suggest next learning actions based on the VibeLearn AI methodology
3. Surface relevant GOBI features the user might not know about

Context: [specs에서 추출한 Core Concepts 삽입]
```

**실현 가능성**: ✅ 매우 높음 — 프롬프트 파일 추가만으로 구현

### 🎯 접점 3: Vibe Guiding을 Skill로 패키징
Skills = Vault별 능력 라이브러리. Vibe Guiding을 독립적인 Skill로 만들어 배포:

```
vibe-guiding-skill/
├── SKILL.md          # Vibe Guiding 동작 정의
├── prompts/          # 제품별 가이딩 프롬프트
└── tools/            # Vibe Guiding 전용 도구
```

사용자가 이 Skill을 Vault에 추가하면 Vibe Guiding 활성화.

**실현 가능성**: ✅ 높음 — Skills 아키텍처 이미 존재

### 🎯 접점 4: 스케줄 기반 Vibe Guiding (향후)
스펙에 "스케줄 기반 트리거"가 향후 기능으로 명시됨. 구현되면:
- 매일 아침 "오늘의 Vibe Guide" 자동 생성
- 주간 학습 진도 요약
- 미학습 기능 발견 및 안내

**실현 가능성**: ⭐ 향후 — 스케줄 트리거 구현 후

---

## Vibe Guiding 설계 함의

> **Orchestration = Vibe Guiding 앱 내 구현의 핵심 메커니즘**

세 가지 구현 경로 (난이도 순):

1. **즉시 (Phase 1)**: `.gobi/settings.yaml` + Vibe Guiding 프롬프트 파일 추가
   - GOBI 팀 코드 변경 불필요
   - 사용자가 직접 설정 가능
   - 빠른 프로토타이핑 가능

2. **단기 (Phase 2)**: Vibe Guiding Skill 패키징 + Watch Pattern 최적화
   - 모든 GOBI 사용자에게 배포 가능
   - VibeLearn AI로 생성한 가이드를 Skill에 통합

3. **장기 (Phase 3)**: 스케줄 트리거 + 앱 UI 통합 (GOBI 팀 협업 필요)
   - 사용자가 별도 설정 없이 Vibe Guiding 경험
