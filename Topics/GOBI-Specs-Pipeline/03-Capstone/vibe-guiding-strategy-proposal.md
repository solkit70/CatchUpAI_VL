# Vibe Guiding 전략 제안서

**작성자**: Changsoo Park
**작성일**: 2026-04-07
**대상**: GOBI 팀 (Mika, Greg)
**기반**: gobi-monorepo + gobi-ai/docs 구조 분석 + Spec 4개 심층 분석

---

## 1. 핵심 메시지

> **Vibe Guiding을 앱 내에서 구동하는 것은 지금 당장 가능합니다.**
> GOBI 팀의 코드 변경 없이, 기존 Orchestrator + Reflex 인프라만으로 즉시 프로토타이핑할 수 있습니다.

---

## 2. 현재 파이프라인 분석 결과

gobi-monorepo와 gobi-ai/docs를 직접 클론하여 분석한 결과:

```
gobi-monorepo/specs (26개 기능 정의)
        ↓ ⚠️ 수동 변환 (자동화 없음)
gobi-ai/docs (Mintlify MDX)
        ↓ ✅ 자동 배포
docs.gobihq.com
```

**핵심 발견**:
- specs(기능 정의) → docs(사용자 문서) 변환이 수동이며 자동화되어 있지 않음
- gobi-monorepo에 이미 `CODE_TO_SPECS` AI 프롬프트가 존재 (코드 → 스펙 생성)
- Orchestrator는 이미 Vault별 백그라운드 Reflex를 지원
- AI 에이전트가 LINEAR.md 기반 개발 파이프라인에 이미 통합됨

---

## 3. Vibe Guiding = SPECS_TO_GUIDE

개발팀이 구현한 `CODE_TO_SPECS`(코드 → 스펙)의 역방향이 Vibe Guiding입니다.

```
현재 개발팀:   코드 → AI(CODE_TO_SPECS) → 스펙
Vibe Guiding:  스펙 → AI(SPECS_TO_GUIDE) → 사용자 가이드 + 앱 내 컨텍스트
```

VibeLearn AI(CUA_VL)가 이 `SPECS_TO_GUIDE` 역할을 담당합니다.

---

## 4. 구현 전략: 3단계 접근

### Phase 1 — 즉시 실증 (1-2주, GOBI 팀 협업 불필요)

**목표**: Changsoo Vault에서 Vibe Guiding 앱 내 구동 증명

**구현 방법**:

Step 1. VibeLearn AI로 스펙에서 가이드 생성
```
gobi-monorepo/specs/*.md
        ↓ VibeLearn AI (SPECS_TO_GUIDE)
Vibe Guiding 프롬프트 파일 생성
```

Step 2. Vault에 Vibe Guiding 설정 추가
```yaml
# Changsoo_Vault/.gobi/settings.yaml
orchestrator:
  enabled: true
  prompt_paths:
    - .gobi/prompts/vibe-guiding.md  ← VibeLearn AI가 생성한 프롬프트
  watch_patterns:
    - _Gobi_/Captures/**/*.md        ← 새 캡처 감지
```

Step 3. Reflex 동작 확인
```
사용자가 새 캡처 생성
        ↓ Watch Pattern 감지
Vibe Guiding Agent 실행:
  - 캡처 내용 분석
  - Brain에서 관련 지식 검색
  - 연결 포인트 + 다음 행동 제안
        ↓
.gobi/outputs/vibe-guide.md 또는 TTS 안내
```

**소요 리소스**: Changsoo 독립 작업, 2주
**성공 지표**: 새 캡처 후 5초 이내에 관련 Brain 지식 + 다음 행동 제안 자동 출력

---

### Phase 2 — Skill 패키징 & 문서 자동화 (2-4주)

**목표**: 모든 GOBI 사용자가 사용할 수 있도록 배포 + docs 파이프라인 기여

**두 가지 병렬 작업**:

**2-A. Vibe Guiding Skill 패키징**
```
vibe-guiding-skill/
├── SKILL.md              # Vibe Guiding 동작 정의
├── prompts/
│   ├── desktop-guide.md  # Desktop 기능 가이드 (specs에서 추출)
│   ├── space-guide.md    # Space 기능 가이드
│   └── cli-guide.md      # CLI 기능 가이드
└── watch-patterns.yaml   # 자동화 트리거 설정
```
→ GOBI 팀과 Skill 배포 채널 협의 (ai4pkm-cli 또는 직접 배포)

**2-B. docs 파이프라인 자동화 기여**
- VibeLearn AI(SPECS_TO_GUIDE)로 specs → MDX 변환 자동화
- gobi-ai/docs에 PR 기여
- CVL: specs 업데이트 → 자동 재생성 → PR

**GOBI 팀 협업**: Skill 배포 방식 결정, docs PR 리뷰

---

### Phase 3 — 앱 네이티브 통합 (1-3개월, GOBI 팀 협업)

**목표**: 사용자가 별도 설정 없이 Vibe Guiding을 경험

**GOBI 팀과 함께 구현할 기능**:

1. **Ambient Mode + Vibe Guiding 라우팅**
   - 특정 Wake Word → Vibe Guiding Agent 연결
   - 현재 화면/기능 컨텍스트 자동 감지 후 맞춤 안내

2. **스케줄 트리거 구현** (19-orchestration 스펙에 "향후" 명시됨)
   - 일일/주간 Vibe Guide 자동 생성
   - 미사용 기능 발견 및 안내

3. **Gobi Space Vibe Guiding Brain 공개**
   - VibeLearn AI로 생성한 가이드를 공개 Brain으로 운영
   - 커뮤니티 Vibe Guiding 허브

---

## 5. VibeLearn AI + CVL 자동화 파이프라인

```
gobi-monorepo/specs 업데이트
        ↓ (변경 감지)
VibeLearn AI (SPECS_TO_GUIDE)
  - 변경된 spec 읽기
  - Core Concept 추출
  - 사용자 페르소나별 가이드 생성
  - Vibe Guiding 프롬프트 업데이트
        ↓
Vibe Guiding Skill 자동 업데이트
        ↓
모든 사용자 Vibe Guiding 자동 개선
```

이것이 CVL(Continuous Vibe Learning) — GOBI 제품이 발전할수록 Vibe Guiding도 자동으로 발전.

---

## 6. 요청 사항 (GOBI 팀)

### Phase 1 (즉시)
- ✅ 별도 요청 없음 — Changsoo가 독립 진행

### Phase 2
- Vibe Guiding Skill 배포 채널 안내 (ai4pkm-cli 통해 배포 가능한지?)
- docs.gobihq.com PR 리뷰 프로세스 안내

### Phase 3
- Orchestrator 스케줄 트리거 구현 일정 공유
- Ambient Mode Vibe Guiding 라우팅 설계 협의
- gobi-monorepo/specs 업데이트 알림 채널 (spec 변경 시 CVL 트리거 용도)

---

## 7. 기대 효과

| 대상 | 효과 |
|------|------|
| GOBI 신규 사용자 | 온보딩 마찰 감소 — 기능을 찾는 시간 → 사용하는 시간 |
| GOBI 기존 사용자 | 모르고 있던 기능 발견, PCM 방법론 심화 활용 |
| 개발팀 | docs 자동화로 문서 유지 비용 절감 |
| Changsoo | VibeLearn AI 방법론의 실제 제품 적용 사례 구축 |

---

## 8. Phase 1 즉시 실행 계획

| 날짜 | 작업 |
|------|------|
| 2026-04-08 | VibeLearn AI로 Desktop + CLI spec → 가이드 프롬프트 생성 |
| 2026-04-09 | Changsoo Vault에 .gobi/settings.yaml 설정 + Reflex 테스트 |
| 2026-04-10 | Ambient Mode 연결 테스트 (음성 Vibe Guiding) |
| 2026-04-11 | 결과 정리 + GOBI 팀 공유 |

---

*이 제안서는 gobi-monorepo(26개 feature specs) + gobi-ai/docs 직접 분석 결과를 기반으로 작성되었습니다.*
