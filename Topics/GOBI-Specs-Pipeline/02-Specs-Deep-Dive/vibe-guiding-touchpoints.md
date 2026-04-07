# Vibe Guiding 접점 통합 분석

**작성일**: 2026-04-07
**기반**: Spec 05, 06, 07, 19 분석 결과

---

## 핵심 결론

> **Vibe Guiding은 새로운 제품이 아니다.**
> GOBI의 기존 인프라(에이전트 + 음성 + 캡처 + 오케스트레이터)를 **조합**하면 구현된다.
> 추가해야 할 것은 **컨텍스트(스펙 기반 가이드)와 프롬프트**뿐이다.

---

## 접점 전체 지도

```
┌─────────────────────────────────────────────────────────────┐
│                    GOBI Desktop 앱                           │
│                                                             │
│  [캡처 탭]          [에이전트 탭]        [오케스트레이터]      │
│   ↓ 새 캡처          ↓ 음성/텍스트         ↓ 파일 변경 감지   │
│   파일 저장          입력 수신             Reflex 트리거      │
│      └──────────────────┴───────────────────┘               │
│                          ↓                                  │
│              Vibe Guiding Agent                             │
│         (System Prompt + 스펙 기반 컨텍스트)                 │
│                          ↓                                  │
│         음성(TTS) 또는 텍스트로 사용자에게 안내               │
└─────────────────────────────────────────────────────────────┘
```

---

## 접점별 실현 가능성 매트릭스

| # | 접점 | 관련 Spec | 구현 난이도 | GOBI 팀 협업 필요 | Phase |
|---|------|----------|-----------|-----------------|-------|
| 1 | System Prompt 주입 | 05 Agent | ⭐ 매우 낮음 | ❌ 불필요 | 1 |
| 2 | Vibe Guiding 전용 Vault/Brain | 05 Agent | ⭐ 매우 낮음 | ❌ 불필요 | 1 |
| 3 | Capture 후 Reflex 트리거 | 07+19 | ⭐ 낮음 | ❌ 불필요 | 1 |
| 4 | Ambient Mode + Vibe 컨텍스트 | 06+05 | ⭐⭐ 중간 | △ 설정 수준 | 2 |
| 5 | Vibe Guiding Skill 패키징 | 19 | ⭐⭐ 중간 | △ Skill 배포 | 2 |
| 6 | ACB 세션 중 실시간 안내 | 07+06 | ⭐⭐⭐ 높음 | ✅ 필요 | 3 |
| 7 | Wake Word → Vibe Guiding 라우팅 | 06 | ⭐⭐⭐ 높음 | ✅ 필요 | 3 |
| 8 | 스케줄 기반 자동 가이드 | 19 | ⭐⭐⭐ 높음 | ✅ 필요 | 3 |

---

## Phase별 구현 로드맵 제안

### Phase 1 — 즉시 실증 (1-2주, GOBI 팀 협업 불필요)

**목표**: Vibe Guiding 컨셉 프로토타입을 지금 당장 만들 수 있음을 증명

**구현 방법**:
1. Changsoo Vault에 Vibe Guiding 전용 프롬프트 파일 추가
   ```
   Changsoo_Vault/.gobi/prompts/vibe-guiding.md
   ```
2. 프롬프트 내용: specs에서 추출한 Core Concepts + 가이딩 지침
3. Watch Pattern 설정: 새 Capture/Note 파일 감지 시 Reflex 실행
4. Reflex 결과 → `.gobi/outputs/`에 저장 또는 TTS로 출력

**VibeLearn AI 역할**:
- gobi-monorepo/specs 읽기
- 각 기능의 Core Concept 추출
- Vibe Guiding 프롬프트 자동 생성 (`SPECS_TO_GUIDE`)

**검증 지표**:
- 새 Capture 후 관련 Brain 지식이 자동 연결되는가?
- 음성으로 "캡처 사용법" 물으면 정확한 답변이 나오는가?

---

### Phase 2 — Skill 패키징 (2-4주, 최소 GOBI 팀 협업)

**목표**: 모든 GOBI 사용자가 사용할 수 있는 Vibe Guiding Skill 배포

**구현 방법**:
1. `vibe-guiding` Skill 패키지 생성
   ```
   vibe-guiding-skill/
   ├── SKILL.md              # 동작 정의
   ├── prompts/
   │   ├── desktop-guide.md  # Desktop 기능 가이드
   │   ├── space-guide.md    # Space 기능 가이드
   │   └── cli-guide.md      # CLI 기능 가이드
   └── watch-patterns.yaml   # 자동화 트리거 설정
   ```
2. VibeLearn AI로 specs → 각 가이드 프롬프트 자동 생성 (CVL)
3. GOBI 팀과 Skill 배포 방식 협의

**CVL (Continuous Vibe Learning)**:
- gobi-monorepo/specs 업데이트 감지
- 변경된 spec → 해당 가이드 프롬프트 자동 재생성
- Vibe Guiding Skill 자동 업데이트

---

### Phase 3 — 앱 내 네이티브 통합 (1-3개월, GOBI 팀 협업 필수)

**목표**: GOBI Desktop/Space 사용자가 별도 설정 없이 Vibe Guiding 경험

**구현 방법**:
1. Ambient Mode에 Vibe Guiding 라우팅 추가
   - 특정 Wake Word → Vibe Guiding Agent 연결
   - 현재 화면/기능 컨텍스트 자동 감지
2. ACB 세션 중 실시간 관련 지식 사이드패널 표시
3. 스케줄 트리거 구현 후 → 일일/주간 Vibe Guide 자동 생성
4. Gobi Space에 Vibe Guiding 공개 Brain 운영

---

## "앱 내 실시간 Vibe Guiding" 가능성 평가

**GOBI 팀 기대**: "현재 파이프라인(docs) 방식보다 실제 앱에서 Vibe Guiding이 가동되는 방법"

**평가**:
- Phase 1(즉시): ✅ **지금 당장 가능** — Orchestrator + 프롬프트만으로 Changsoo Vault에서 실증
- Phase 2(단기): ✅ **2-4주 안에 가능** — Skill로 패키징하여 다른 사용자에게 배포
- Phase 3(장기): 🔄 **GOBI 팀 협업 필요** — 네이티브 UX 통합은 앱 코드 변경 필요

> **핵심 메시지**: Vibe Guiding을 앱에서 구동하는 것은 Phase 1부터 가능하다.
> 완전한 네이티브 경험은 Phase 3이 필요하지만, 가치 증명은 지금 시작할 수 있다.

---

## VibeLearn AI의 역할 (파이프라인 내 위치)

```
gobi-monorepo/specs (26개 기능 정의)
        ↓
VibeLearn AI (SPECS_TO_GUIDE)
  - Core Concept 추출
  - 사용자 페르소나별 가이드 생성
  - Vibe Guiding 프롬프트 작성
        ↓
Vibe Guiding Skill / Vault 프롬프트
        ↓
GOBI Orchestrator (Reflex / Ambient Mode)
        ↓
사용자에게 실시간 맞춤 안내
```

**CVL (Continuous Vibe Learning)**:
```
specs 파일 변경 감지
        ↓
VibeLearn AI 자동 재실행
        ↓
업데이트된 Vibe Guiding 프롬프트
        ↓
자동 배포 → 사용자 경험 자동 개선
```
