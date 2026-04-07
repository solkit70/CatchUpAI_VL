# Spec 분석: 05 - Second Brain Agent

**분석일**: 2026-04-07
**원본 파일**: `gobi-monorepo/specs/05-second-brain-agent.md`
**Vibe Guiding 관련도**: ⭐⭐⭐ 핵심

---

## 핵심 요약

Second Brain Agent는 사용자의 Vault(지식 저장소)를 컨텍스트로 작동하는 AI 어시스턴트. 단순 Q&A가 아닌 Vault를 읽고/쓰고/추론하는 진정한 지식 파트너.

---

## 주요 기능 정리

| 기능 | 설명 |
|------|------|
| 채팅 세션 | Vault 단위로 스코프, 새 세션 / 이어서 / 기록 탐색 |
| 세션 모드 | Auto(자동 응답) / Manual(명시적 지시 대기) |
| 메시지 스트리밍 | SSE 기반 실시간 스트리밍, 중단 가능 |
| Tool Calls | 파일 읽기/쓰기, 검색, 웹 서치, 커스텀 도구 |
| Multi-Session | 동시 다중 세션 (Ready / Running / Dormant 상태) |
| Pre-spawning | 낮은 레이턴시를 위한 웜 풀 유지 |
| Targeted Session | 다른 Brain에 질의 (`gobi brain ask`) |
| System Prompt | Vault별 커스텀 시스템 프롬프트 설정 가능 |
| 컨텍스트 윈도우 | 대화 이력 + 관련 Vault 파일 + 시스템 프롬프트 + 도구 정의 |

---

## Vibe Guiding 접점 분석

### 🎯 접점 1: System Prompt 주입
**위치**: `Orchestrator Settings > prompt paths`

Vault별 시스템 프롬프트를 설정할 수 있음. Vibe Guiding 컨텍스트(제품 스펙 기반 안내)를 시스템 프롬프트로 주입하면 에이전트가 자동으로 Vibe Guiding 역할을 수행.

```
현재: 일반 Second Brain Agent
      ↓ 시스템 프롬프트 변경
Vibe Guiding: GOBI 제품 전문가 에이전트
```

**실현 가능성**: ✅ 매우 높음 — 기존 인프라 그대로 활용

### 🎯 접점 2: Targeted Session (Ask a Brain)
**관련 기능**: `gobi brain ask --vault-slug <slug> --question "..."`

Vibe Guiding 전용 Brain을 만들고, 사용자가 `gobi brain ask`로 질의하는 방식. VibeLearn AI로 생성한 가이드를 이 Brain에 주입.

```
vibe-guiding Brain
  └─ specs에서 추출한 Core Concept + User Manual
        ↓
사용자: gobi brain ask --vault-slug vibe-guiding --question "캡처 사용법"
        ↓
Vibe Guiding Brain이 답변
```

**실현 가능성**: ✅ 높음 — 현재 CLI로 즉시 프로토타이핑 가능

### 🎯 접점 3: Tool Calls 확장
에이전트가 Tool Calls를 통해 Vibe Guiding 관련 작업 수행 가능:
- `search_guide(query)`: Vibe Guiding 문서에서 관련 섹션 검색
- `get_feature_context(feature_name)`: 특정 기능의 Core Concept 반환

**실현 가능성**: ⭐⭐ 중간 — 커스텀 Tool 개발 필요

---

## Vibe Guiding 설계 함의

> 핵심 결론: **Vibe Guiding은 새로운 제품이 아니라 Second Brain Agent의 특수화된 버전**으로 구현 가능

- 기존 에이전트 인프라(세션 풀, 스트리밍, Tool Calls) 그대로 재사용
- System Prompt + 전용 Vault만 교체하면 Vibe Guiding 에이전트 완성
- VibeLearn AI가 생성한 가이드 → Vibe Guiding Vault → 에이전트 컨텍스트
