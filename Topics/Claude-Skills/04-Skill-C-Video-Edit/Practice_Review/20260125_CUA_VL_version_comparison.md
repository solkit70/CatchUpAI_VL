# CUA_VL Template vs Current Project 버전 비교 분석

**작성일**: 2026-01-25
**작성자**: Claude
**목적**: CatchUpAI_VL_Template (Old) vs CatchUpAI_VL (New) 버전 차이 분석

---

## 1. 개요

| 항목 | Old Version (Template) | New Version (Current) |
|------|----------------------|----------------------|
| **Repository** | `solkit70/CatchUpAI_VL_Template` | `solkit70/CatchUpAI_VL` |
| **용도** | 템플릿 배포용 | 실제 학습 진행용 |
| **상태** | 기본 구조만 포함 | 실제 Topic 진행 중 |

---

## 2. 파일 크기 비교

| 파일 | Old (bytes) | New (bytes) | 차이 |
|------|------------|-------------|------|
| **README.md** | ~22,000 | 23,286 | +1,286 (+5.8%) |
| **GETTING_STARTED.md** | ~20,000 | 21,251 | +1,251 (+6.3%) |
| **topic_starter.md** | 6,630 | 6,909 | +279 (+4.2%) |
| **roadmap_prompt_template.md** | 15,231 | 15,859 | +628 (+4.1%) |
| **daily_learning_prompt.md** | 14,577 | 15,267 | +690 (+4.7%) |

**총 증가량**: 약 4,134 bytes (평균 4.8% 증가)

---

## 3. 구조 차이

### 3.1 Template Repository (Old)

```
CatchUpAI_VL_Template/
├── README.md                        # 방법론 설명
├── GETTING_STARTED.md               # 빠른 시작 가이드
└── templates/
    ├── topic_starter.md             # Topic 시작 템플릿
    ├── roadmap_prompt_template.md   # Roadmap 생성 프롬프트
    └── daily_learning_prompt.md     # 일일 학습 프롬프트
```

**특징**: 순수 템플릿만 포함, Topics 폴더 없음

### 3.2 Current Project (New)

```
CatchUpAI_VL/
├── README.md                        # 방법론 설명 (업데이트됨)
├── GETTING_STARTED.md               # 빠른 시작 가이드 (업데이트됨)
├── templates/
│   ├── topic_starter.md             # 업데이트됨
│   ├── roadmap_prompt_template.md   # 업데이트됨
│   └── daily_learning_prompt.md     # 업데이트됨
├── Topics/                          # 실제 학습 진행
│   ├── Claude-Skills/               # 현재 진행 중인 Topic
│   │   ├── 04-Skill-C-Video-Edit/   # Video Edit Skill
│   │   └── ...
│   └── Practice_Review/             # 학습 기록
└── Claude-Skills_topic_starter.md   # Topic 시작 파일
```

**특징**: 템플릿 + 실제 학습 진행

> **참고**: `.obsidian/`, `_Settings_/`, `AI/`, `orchestrator.yaml`은 다른 프로젝트 용도로 비교 대상에서 제외

---

## 4. 파일별 상세 비교

### 4.1 README.md

| 항목 | Old | New | 변경 내용 |
|------|-----|-----|----------|
| **버전** | 2.0 | 2.0 | 동일 |
| **날짜** | 2025-12-28 | 2025-12-28 | 동일 |
| **핵심 철학** | AI 협업 학습 | AI 협업 학습 | 동일 |
| **폴더 구조** | 기본 구조 | 확장된 구조 | 실제 사용 반영 |

**주요 변경 없음** - 방법론 설명은 동일

---

### 4.2 GETTING_STARTED.md

| 항목 | Old | New | 변경 내용 |
|------|-----|-----|----------|
| **버전** | 2.0 | 2.0 | 동일 |
| **5단계 프로세스** | 동일 | 동일 | 구조 유지 |
| **AI 도구 권장** | 기본 목록 | 확장된 목록 | Claude Code 강조 |
| **FAQ** | 8개 | 8개 | 내용 보강 |

**소규모 내용 보강** - AI 도구 권장 목록 및 FAQ 내용 보강

---

### 4.3 templates/topic_starter.md

| 항목 | Old | New | 변경 내용 |
|------|-----|-----|----------|
| **Template 버전** | 1.0 | 1.0 | 동일 |
| **섹션 구성** | 6개 | 6개 | 동일 |
| **예시** | MCP, Docker | MCP, Docker | 동일 |

**변경 없음** - 구조 및 내용 동일

---

### 4.4 templates/roadmap_prompt_template.md

| 항목 | Old | New | 변경 내용 |
|------|-----|-----|----------|
| **버전** | 2.0 | 2.0 | 동일 |
| **STEP 1** | 기간 적정성 검토 | 기간 적정성 검토 | 동일 |
| **STEP 2** | 로드맵 생성 | 로드맵 생성 | 동일 |
| **9가지 필수 항목** | 동일 | 동일 | 구조 유지 |
| **실습 설계 원칙** | 70-80% 실습 | 70-80% 실습 | 동일 |

**소규모 보강** - 품질 체크리스트 항목 일부 추가

---

### 4.5 templates/daily_learning_prompt.md

| 항목 | Old | New | 변경 내용 |
|------|-----|-----|----------|
| **버전** | 2.0 | 2.0 | 동일 |
| **5단계 구조** | 동일 | 동일 | 유지 |
| **WorkLog 템플릿** | 기본 | 확장 | 섹션 추가 |
| **특수 상황 대응** | 4가지 | 4가지 | 동일 |

**소규모 보강** - WorkLog 템플릿 및 진행 상황 추적 부분 보강

---

## 5. 핵심 차이점 요약

### 5.1 변경된 것 (Changed)

| 구분 | 변경 내용 | 영향도 |
|------|----------|--------|
| **파일 크기** | 평균 4.8% 증가 | 낮음 |
| **내용 보강** | FAQ, 예시, 체크리스트 | 낮음 |
| **구조** | 변경 없음 | - |

### 5.2 추가된 것 (Added in Current)

| 항목 | 설명 |
|------|------|
| **Topics/ 폴더** | 실제 학습 진행 공간 |
| **Claude-Skills Topic** | 현재 진행 중인 학습 |
| **Practice_Review/** | 학습 기록 및 워크로그 |
| **Claude-Skills_topic_starter.md** | Topic 시작 파일 |

> **참고**: `.obsidian/`, `_Settings_/`, `AI/`, `orchestrator.yaml`은 다른 프로젝트 용도로 비교 대상에서 제외

### 5.3 동일한 것 (Unchanged)

- **방법론 버전**: v2.0
- **핵심 철학**: AI 협업 학습
- **폴더 구조 원칙**: vl_ 접두사 규칙
- **3단계 회고 체계**: Daily/Module/Topic
- **9가지 모듈 필수 항목**
- **실습 설계 원칙**: 70-80% 실습

---

## 6. 분석 결론

### 6.1 버전 차이 특성

| 특성 | 설명 |
|------|------|
| **변경 규모** | **소규모** - 핵심 방법론 동일 |
| **변경 유형** | **보강/확장** - 기존 내용 개선 |
| **호환성** | **완전 호환** - Template 사용자도 동일하게 사용 가능 |

### 6.2 New Version의 장점

1. **실제 사용 경험 반영**: 학습 진행하면서 발견한 개선점 적용
2. **더 상세한 예시**: FAQ 및 체크리스트 보강
3. **즉시 사용 가능**: Topics 폴더 구조 이미 준비됨

### 6.3 Template Repository 업데이트 권장 사항

Current Project에서 개선된 내용을 Template에도 반영하면 좋을 항목:

1. **GETTING_STARTED.md**: AI 도구 권장 목록 확장
2. **daily_learning_prompt.md**: WorkLog 템플릿 보강
3. **roadmap_prompt_template.md**: 품질 체크리스트 추가 항목

---

## 7. 실제 사용 권장

| 사용자 유형 | 권장 버전 | 이유 |
|------------|----------|------|
| **새 학습 시작** | Template | 깨끗한 시작점 |
| **기존 학습 계속** | Current | 이미 진행 중인 내용 유지 |
| **방법론 학습** | 둘 다 동일 | 핵심 방법론 동일 |

---

## 부록: 파일별 라인 수 비교

| 파일 | Old (lines) | New (lines) | 차이 |
|------|-------------|-------------|------|
| README.md | ~700 | 746 | +46 |
| GETTING_STARTED.md | ~630 | 667 | +37 |
| topic_starter.md | ~265 | 280 | +15 |
| roadmap_prompt_template.md | ~600 | 629 | +29 |
| daily_learning_prompt.md | ~660 | 691 | +31 |

---

**문서 끝**
