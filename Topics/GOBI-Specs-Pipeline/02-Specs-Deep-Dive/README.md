# M2 - Vibe Guiding 핵심 Spec 파일 심층 분석

**모듈**: M2 | **상태**: ✅ 완료 | **학습 시간**: 약 3h (2026-04-07)

---

## 이 모듈에서 배우는 것

Vibe Guiding과 직접 관련된 spec 4개를 심층 분석하고, 앱 내 실시간 Vibe Guiding 구현 방안을 도출합니다.

| # | 문서 | 설명 |
|---|------|------|
| 1 | [spec-analysis-second-brain-agent.md](spec-analysis-second-brain-agent.md) | System Prompt 주입 + Targeted Session으로 Vibe Guiding 구현 방안 |
| 2 | [spec-analysis-voice-interaction.md](spec-analysis-voice-interaction.md) | Ambient Mode = Vibe Guiding의 자연스러운 음성 채널 |
| 3 | [spec-analysis-capture.md](spec-analysis-capture.md) | Capture 전/중/후가 Vibe Guiding 개입 최적 타이밍 |
| 4 | [spec-analysis-orchestration.md](spec-analysis-orchestration.md) | Reflex + Skill로 Vibe Guiding 앱 내 구현 메커니즘 |
| 5 | [vibe-guiding-touchpoints.md](vibe-guiding-touchpoints.md) | **통합 분석**: 접점 매트릭스 + Phase별 구현 로드맵 |

---

## 핵심 결론

### 1. Vibe Guiding은 새로운 제품이 아니다
기존 GOBI 인프라(에이전트 + 음성 + 캡처 + 오케스트레이터)를 조합하면 구현된다.  
추가해야 할 것은 **컨텍스트(스펙 기반 가이드)와 프롬프트**뿐이다.

### 2. Phase 1은 지금 당장 가능하다
`.gobi/settings.yaml` + Vibe Guiding 프롬프트 파일만 추가하면  
GOBI 팀 코드 변경 없이 Changsoo Vault에서 즉시 프로토타이핑 가능.

### 3. VibeLearn AI의 역할이 명확해졌다
```
specs → VibeLearn AI(SPECS_TO_GUIDE) → Vibe Guiding 프롬프트 → Orchestrator → 사용자 안내
```

### 4. CVL(Continuous Vibe Learning)이 자동화의 핵심
specs 업데이트 → VibeLearn AI 자동 재실행 → Vibe Guiding 자동 업데이트

---

## 다음 모듈

→ **[M3: Capstone — Vibe Guiding 전략 제안서](../03-Capstone/README.md)**
