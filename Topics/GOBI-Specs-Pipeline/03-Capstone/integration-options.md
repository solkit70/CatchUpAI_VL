# Vibe Guiding 접목 옵션 비교 분석

**작성일**: 2026-04-07
**기반**: M1(구조 파악) + M2(Spec 분석) 결과

---

## 비교 대상 4가지 옵션

---

### 옵션 A: specs → VibeLearn AI → docs 파이프라인 자동화 (문서 통합)

**개념**:
```
gobi-monorepo/specs (Markdown)
        ↓ VibeLearn AI (SPECS_TO_GUIDE)
gobi-ai/docs (MDX 자동 생성)
        ↓ Mintlify 자동 배포
docs.gobihq.com
```

**장점**:
- 현재 파이프라인의 수동 변환 갭을 해소
- 개발팀이 spec 업데이트 → 문서 자동 반영 (CVL)
- GOBI 팀이 원하는 공식 문서 품질 확보

**단점**:
- 사용자가 docs.gobihq.com을 직접 찾아봐야 함 (push 방식이 아님)
- Vibe Guiding의 핵심 가치인 "맞춤형 실시간 안내"와 거리가 있음
- spec(기능 정의) → MDX(사용자 문서) 변환 품질 검증 필요

**실현 가능성**: ✅ 높음
**GOBI 팀 협업**: △ gobi-ai/docs PR 프로세스 협의 필요
**Vibe Guiding 가치 구현도**: ⭐⭐ (문서화 자동화에 가까움)

---

### 옵션 B: Second Brain Agent의 Reflex로 앱 내 Vibe Guiding (즉시 실증)

**개념**:
```
.gobi/settings.yaml
  prompt_paths: [vibe-guiding.md]   ← VibeLearn AI로 생성
  watch_patterns: [_Gobi_/Captures/**/*.md]
        ↓ 새 캡처 감지 시 Reflex 실행
Vibe Guiding Agent 응답
  → .gobi/outputs/vibe-guide.md 저장
  → (선택) TTS로 음성 안내
```

**장점**:
- GOBI 팀 코드 변경 없이 지금 당장 Changsoo Vault에서 프로토타이핑 가능
- "앱 내 실시간 Vibe Guiding" GOBI 팀 기대와 가장 근접
- Ambient Mode 연계 시 음성 기반 자연스러운 UX 가능
- 개인화: 각 사용자 Vault 컨텍스트 기반 맞춤 안내

**단점**:
- 현재 Reflex 트리거가 파일 변경 / 수동 실행만 가능 (스케줄 미구현)
- Skill 패키징 없이는 다른 사용자에게 배포 어려움
- Ambient Mode 라우팅은 Phase 2 이후

**실현 가능성**: ✅ 매우 높음 (Phase 1 즉시)
**GOBI 팀 협업**: ❌ 불필요 (Phase 1)
**Vibe Guiding 가치 구현도**: ⭐⭐⭐ (핵심 가치 구현)

---

### 옵션 C: Gobi CLI를 통한 Vibe Guiding 독립 운영

**개념**:
```
VibeLearn AI → Vibe Guiding Brain (독립 Vault)
        ↓
gobi brain ask --vault-slug vibe-guiding --question "..."
또는
gobi brain publish → Gobi Space에 Vibe Guiding Brain 공개
```

**장점**:
- 완전 독립 운영 — GOBI 인프라에 최소 의존
- 현재 GOBI CLI 기능(brain ask, brain publish)으로 즉시 구현
- Gobi Space 공개 시 모든 GOBI 사용자 접근 가능
- VibeLearn AI 결과물을 Brain에 직접 업로드

**단점**:
- 사용자가 CLI 명령을 직접 입력해야 함 (낮은 UX)
- 앱 내 자동 트리거 없음 — 수동 질의만 가능
- "실시간 안내"가 아닌 "능동적 질의" 모델

**실현 가능성**: ✅ 매우 높음 (현재 CLI로 즉시)
**GOBI 팀 협업**: ❌ 불필요
**Vibe Guiding 가치 구현도**: ⭐⭐ (수동 조회에 가까움)

---

### 옵션 D: 혼합 전략 (Phase 1 → Phase 2 → Phase 3 순차 진행)

**개념**:
```
Phase 1 (즉시, 1-2주):
  옵션 B로 Changsoo Vault 프로토타이핑
  + 옵션 C로 Vibe Guiding Brain 공개

Phase 2 (2-4주):
  Vibe Guiding Skill 패키징 → 다른 GOBI 사용자 배포
  + 옵션 A로 docs 파이프라인 자동화 기여

Phase 3 (1-3개월):
  GOBI 팀과 Ambient Mode 네이티브 통합
  스케줄 트리거 구현 후 자동 가이드 생성
```

**장점**:
- 즉시 가치 증명 + 점진적 확장
- 각 Phase가 독립적으로 완결됨 (실패 위험 분산)
- GOBI 팀에 단계별 성과를 보여주며 신뢰 구축
- 최종 Phase 3에서 GOBI 팀이 원하는 네이티브 경험 달성

**단점**:
- 3개 Phase 걸쳐 시간 소요
- Phase 간 전환 시 설계 변경 가능성

**실현 가능성**: ✅ 매우 높음
**GOBI 팀 협업**: Phase별 단계적 증가
**Vibe Guiding 가치 구현도**: ⭐⭐⭐ (Phase 3에서 최고)

---

## 비교 요약

| 기준 | 옵션 A | 옵션 B | 옵션 C | 옵션 D |
|------|--------|--------|--------|--------|
| 즉시 실행 가능성 | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 앱 내 실시간 안내 | ❌ | ✅ | ❌ | ✅ (단계적) |
| GOBI 팀 의존도 | 중간 | 낮음 | 없음 | 단계적 |
| 가치 증명 속도 | 느림 | 빠름 | 빠름 | 빠름 |
| 장기 확장성 | 중간 | 높음 | 낮음 | 최고 |
| GOBI 팀 기대 충족 | ⭐⭐ | ⭐⭐⭐ | ⭐ | ⭐⭐⭐ |

## 권장: 옵션 D (혼합 전략)

- Phase 1: **지금 당장** 옵션 B로 실증
- Phase 2: Skill 패키징 + 옵션 A 문서 자동화 기여
- Phase 3: GOBI 팀과 네이티브 통합
