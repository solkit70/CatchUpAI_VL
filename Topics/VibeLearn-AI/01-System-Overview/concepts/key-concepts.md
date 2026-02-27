# VibeLearn AI — 핵심 용어 사전 (Key Concepts)

**작성일**: 2026-02-26
**모듈**: M1 - 시스템 분석 & 개념 정립

---

## 이 문서를 사용하는 방법

VibeLearn AI를 처음 접하면 낯선 용어들이 등장합니다.
이 문서는 그 용어들을 명확하게 정의하고 관계를 설명합니다.

---

## 핵심 용어 목록

---

### Topic

**정의**: VibeLearn AI에서 학습하는 하나의 주제 단위

**예시**:
- `Clearly-BRD-PRD` — Clearly 앱으로 BRD/PRD 작성법 학습
- `Remotion-VideoCreation` — Remotion으로 영상 만들기
- `VibeLearn-AI` — VibeLearn AI 시스템 자체 학습

**특징**:
- 영문, 하이픈 사용 (공백 없음)
- 폴더명으로 직접 사용됨: `Topics/VibeLearn-AI/`
- 하나의 Topic = 하나의 완결된 학습 여정

**주의**: "주제"와 다름 — Topic은 폴더 구조, 파일명, Roadmap까지 연결되는 체계적 단위

---

### Phase (페이즈)

**정의**: VibeLearn AI의 4단계 주요 프로세스

```
Phase 1: Topic 설정 (최초 1회)
Phase 2: Roadmap 생성 (Topic당 1회)
Phase 3: 일일 학습 (반복)
Phase 4: 완료 & 회고 (Topic당 1회)
```

**비유**: 여행에서 Phase는 "출발 준비 → 경로 계획 → 여행 → 귀가"와 같음

---

### Module (모듈)

**정의**: Roadmap 내 세부 학습 단위. `M1`, `M2`, `M3` 등으로 표시

**구성**:
- 학습 목표 3-5개
- 핵심 개념 (이론 20-30%)
- 실습 과제 (실습 70-80%)
- Definition of Done (DoD)
- 예상 산출물

**예시**:
- M1: 시스템 분석 & 개념 정립 (4h)
- M2: 사용자 가이드 & 케이스 스터디 (4-5h)
- M3: 소개 영상 제작 (6-8h)

---

### Roadmap (로드맵)

**정의**: Topic 전체의 학습 계획서. 모든 모듈의 상세 계획을 담은 문서

**파일명 규칙**: `YYYYMMDD_RoadMap_{TopicName}.md`

**내용**:
- 전체 학습 기간 및 예상 시간
- 모듈별 목표, 실습, DoD
- Self-Assessment 체크리스트
- 참조 자료

**역할**: 나침반 — 매 학습 세션마다 참조하여 현재 위치 확인

---

### WorkLog (워크로그)

**정의**: 일별 학습 작업 기록 파일

**파일명 규칙**: `YYYYMMDD_MX_{TopicName}.md`

**예시**: `20260226_M1_VibeLearn-AI.md`

**필수 섹션**:
1. 오늘의 학습 목표 (체크리스트)
2. 학습 내용 (상세)
3. 완료한 작업
4. 문제 해결 로그
5. DoD 체크리스트
6. Daily Retrospective
7. 다음 세션 준비사항

**역할**: 항해 일지 — 어디서 왔고 어디로 가는지 기록

---

### topic_info.md

**정의**: Topic의 기본 정보를 담은 파일. `topic_starter.md` 템플릿을 기반으로 생성

**위치**: `Topics/{TopicName}/topic_info.md`

**내용**:
- Topic 이름 및 설명
- 학습 목적 및 목표
- 학습 환경 (OS, 도구)
- 참조 자료

**역할**: Topic의 신분증 — "이 학습이 무엇인지" 한눈에 파악

---

### vl_prompts/ 폴더

**정의**: Topic 전용 프롬프트 파일들이 저장되는 폴더

**내용**:
- `roadmap_prompt.md` — Topic 정보가 이미 주입된 Roadmap 생성 프롬프트
- `daily_learning_prompt.md` — 매일 학습 계획 수립 프롬프트

**역할**: AI와의 협업 인터페이스 — 새 대화 세션에서도 일관된 가이드 제공

---

### vl_worklog/ 폴더

**정의**: Topic의 모든 WorkLog 파일이 저장되는 폴더

**특징**:
- 같은 날은 같은 파일에 추가 작성
- 다음 날은 새 파일 생성
- Module과 연결고리 명시 (파일명으로)

---

### vl_roadmap/ 폴더

**정의**: Topic의 Roadmap 파일이 저장되는 폴더

**내용**: `YYYYMMDD_RoadMap_{TopicName}.md` 파일 1개

---

### NN-ModuleName/ 폴더 (산출물 폴더)

**정의**: 실제 학습 결과물(교과서)이 저장되는 폴더

**명명 규칙**: `순서번호-모듈이름/`

**예시**:
- `01-System-Overview/`
- `02-User-Guide/`
- `03-Intro-Video/`

**하위 구조**:
```
01-System-Overview/
├── README.md          ← 필수: 이 모듈이 뭔지 개요
├── concepts/          ← 개념 문서
├── examples/          ← 실습 예제 (검증된 코드)
└── guides/            ← 단계별 가이드
```

**교과서 품질 기준**: 이 폴더만 보고 다른 사람이 학습 가능한 수준

---

### DoD (Definition of Done)

**정의**: 모듈이 완료되었다고 판단하는 명확한 기준 체크리스트

**예시**:
```
- [ ] README.md, GETTING_STARTED.md 읽기 완료
- [ ] 워크플로우 다이어그램 작성 완료
- [ ] 타겟 사용자 페르소나 3가지 문서화 완료
- [ ] 핵심 개념 문서 최소 3개 작성 완료
```

**역할**: 완료 판단의 객관적 기준 — "다 한 것 같다" 주관성 제거

---

### CVL (Continuous Vibe Learning)

**정의**: 학습 대상이 변화할 때 변경사항을 감지하고 학습 내용을 동기화하는 프로세스

**적용 시점**: 원격 저장소(GitHub)가 있는 프로젝트를 학습할 때

**프로세스**:
1. 매 학습 세션 시작 시 `git fetch` 실행
2. 변경사항 분석
3. 영향도 평가 (대규모/중간/소규모)
4. 필요 시 WorkLog에 동기화 기록

**영향도 기준**:
| 규모 | 예시 | 조치 |
|------|------|------|
| 대규모 | 핵심 아키텍처 변경 | 별도 업데이트 세션 |
| 중간 | 새 기능 추가 | 당일 학습 전 처리 |
| 소규모 | 문서 업데이트 | WorkLog에 메모만 |

---

### Daily Retrospective (데일리 레트로스펙티브)

**정의**: 매 학습 세션 종료 시 5-10분 간 진행하는 회고

**4가지 질문**:
1. What went well? (잘된 점)
2. What could be improved? (개선 필요)
3. Insights (새로 깨달은 것)
4. Tomorrow's focus (내일 할 일)

---

### Self-Assessment (셀프 어세스먼트)

**정의**: 모듈 완료 시 스스로 역량을 평가하는 체크리스트

**VibeLearn AI의 평가 철학**:
- "모든 것을 암기했는가?" ❌
- "AI와 함께 이것을 실행할 수 있는가?" ✅

**점수 기준**:
- 모두 체크: ⭐⭐⭐⭐⭐ (완벽)
- 10-11개: ⭐⭐⭐⭐ (우수)
- 8-9개: ⭐⭐⭐ (보통)
- 6-7개: ⭐⭐ (복습 필요)
- 5개 이하: ⭐ (재학습 권장)

---

### Templates/ 폴더

**정의**: 모든 Topic에 재사용 가능한 범용 템플릿 파일들

**위치**: VibeLearn AI 루트 폴더의 `templates/`

**파일 목록**:
| 파일 | 용도 | 사용 시점 |
|------|------|---------|
| `topic_starter.md` | Topic 정보 수집 | Phase 1 시작 시 |
| `roadmap_prompt_template.md` | Roadmap 생성 가이드 | Phase 2 |
| `daily_learning_prompt.md` | 일일 학습 계획 | Phase 3 매일 |
| `workflow_guide.md` | 전체 워크플로우 참조 | 언제든지 |
| `quick_start_prompt.md` | 빠른 시작용 프롬프트 | 처음 시작 시 |

**특징**: Topic-agnostic — 어떤 주제에도 재사용 가능

---

## 용어 관계도

```
VibeLearn AI
├── Templates/ (범용 템플릿)
│   ├── topic_starter.md ──────────────────────►
│   ├── roadmap_prompt_template.md ────────────►
│   └── daily_learning_prompt.md ──────────────►
│                                               │
└── Topics/ (학습 프로젝트들)                     │
    └── {Topic}/ ◄──────────────────────────────┘
        ├── topic_info.md            (Phase 1 산출물)
        ├── vl_prompts/              (Phase 1 산출물)
        │   ├── roadmap_prompt.md    ← template + Topic 정보 주입
        │   └── daily_learning.md   ← template 복사
        ├── vl_roadmap/              (Phase 2 산출물)
        │   └── YYYYMMDD_RoadMap.md
        ├── vl_worklog/              (Phase 3 산출물)
        │   └── YYYYMMDD_M1.md
        └── 01-ModuleName/           (Phase 3 산출물 = 교과서)
            ├── README.md
            ├── concepts/
            └── guides/
```

---

**작성자**: Claude with VibeLearn AI
**참조**: README.md (전체), GETTING_STARTED.md
