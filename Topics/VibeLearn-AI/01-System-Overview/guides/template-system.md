# VibeLearn AI — 템플릿 시스템 완전 가이드

**작성일**: 2026-02-26
**모듈**: M1 - 시스템 분석 & 개념 정립

---

## 템플릿 시스템이 왜 중요한가?

VibeLearn AI의 가장 강력한 특징은 **누구나 같은 방법으로 시작할 수 있다**는 것입니다.
이를 가능하게 하는 것이 바로 템플릿 시스템입니다.

```
템플릿 없이:
  사람마다 다른 방식 → 공유 어려움 → 재사용 불가

템플릿 있으면:
  표준 구조 → 쉬운 공유 → 즉시 재사용 가능
```

---

## 템플릿 파일 목록

`templates/` 폴더에는 5개의 핵심 파일이 있습니다:

| 파일 | 역할 | 사용 Phase | 사용 빈도 |
|------|------|-----------|---------|
| `topic_starter.md` | Topic 정보 입력 템플릿 | Phase 1 | Topic당 1회 |
| `roadmap_prompt_template.md` | Roadmap 생성 프롬프트 | Phase 2 | Topic당 1회 |
| `daily_learning_prompt.md` | 일일 학습 계획 프롬프트 | Phase 3 | **매일** |
| `workflow_guide.md` | 전체 워크플로우 참조 | 언제든 | 필요 시 |
| `quick_start_prompt.md` | 처음 시작하는 사람용 | Phase 1 이전 | 1회 |

---

## 각 템플릿 상세 설명

---

### 1. topic_starter.md

**목적**: 새 Topic을 시작할 때 필요한 모든 정보를 체계적으로 수집

**사용 방법**:
```
Option A (AI와 대화):
  "Python을 배우고 싶어. topic_starter.md 작성을 도와줘" → AI가 질문하며 자동 완성

Option B (직접 작성):
  cp templates/topic_starter.md Python-Basics_topic_starter.md
  → 파일 열어서 직접 채우기
```

**수집하는 정보**:
- Topic 이름, 설명, 학습 목적
- 예상 학습 기간
- 학습 목표 3-5개
- 학습 환경 (OS, 도구)
- 사전 지식 (필수/권장)
- 참조 자료

**다음 단계**: 완성된 내용을 `topic_info.md`로 저장 → AI에게 폴더 구조 생성 요청

---

### 2. roadmap_prompt_template.md

**목적**: AI에게 전달하여 Topic에 맞는 학습 Roadmap 생성

**사용 방법**:
```
1. vl_prompts/roadmap_prompt.md 열기 (이미 Topic 정보가 주입됨)
2. AI에게 파일 전달:
   "vl_prompts/roadmap_prompt.md를 읽고 학습 로드맵을 생성해주세요"
3. AI가 생성한 Roadmap → vl_roadmap/ 폴더에 저장
```

**주입되는 Topic 정보**:
- Topic 이름 및 설명
- 학습 목표
- 예상 기간
- 학습 환경

**생성되는 Roadmap 구조** (모듈별 9개 항목):
1. 모듈 기본 정보
2. 학습 목표
3. 핵심 개념 (이론 20-30%)
4. 실습 과제 (실습 70-80%)
5. 예상 산출물
6. Definition of Done (DoD)
7. Self-Assessment 체크리스트
8. 시간 배분
9. 참조 자료

---

### 3. daily_learning_prompt.md

**목적**: 매일 학습 세션 시작 시 AI에게 전달하여 그날의 학습 계획 수립

**사용 방법**:
```
매일 학습 시작 시:
"daily_learning_prompt.md를 읽고 오늘의 학습을 도와주세요.
현재 상황: M1 진행 중, 첫 세션, 3시간 가용"
```

**AI가 하는 일** (5단계 프로세스):
1. Roadmap + 최신 WorkLog 읽기 → 현재 상태 파악
2. 오늘의 학습 계획 수립 (우선순위, 시간 배분)
3. 계획을 사용자에게 제시 → **승인 대기**
4. 승인 후 실습 중심 학습 가이드 시작
5. WorkLog 작성 안내 + Daily Retrospective

**핵심 특징**: 승인 단계 — 사용자가 계획을 검토하고 수정 후 시작

---

### 4. workflow_guide.md

**목적**: 전체 워크플로우를 한눈에 참조할 수 있는 가이드

**사용 시점**:
- 처음 VibeLearn AI를 배울 때
- Phase 전환 시 다음 단계가 뭔지 확인할 때
- 팀원에게 방법론을 설명할 때

**내용**:
- 1단계~3단계 프롬프트 템플릿
- 폴더 구조 전체 참조
- 회고 템플릿 (Daily, Module, Topic)
- 팁 & 모범 사례

---

### 5. quick_start_prompt.md

**목적**: VibeLearn AI를 처음 접하는 사람이 30분 안에 시작할 수 있도록 하는 올인원 프롬프트

**사용 방법**:
```
이 파일 전체를 AI에게 복사+붙여넣기
마지막에: "학습하고 싶은 주제: [주제]" 추가
```

**AI가 하는 일** (7단계):
1. Topic 정보 대화형 수집
2. 수집 정보 요약 및 확인
3. 폴더 구조 생성 안내
4. topic_info.md 생성
5. Roadmap 생성 여부 확인
6. Roadmap 생성
7. 학습 시작 안내

**언제 쓰나**: GETTING_STARTED.md보다 더 빠르게 시작하고 싶을 때

---

## 템플릿 → 프롬프트 주입 메커니즘

이것이 VibeLearn AI의 핵심 엔진입니다.

```
templates/roadmap_prompt_template.md
(Topic 정보 없는 범용 템플릿)
          +
topic_info.md
(이 Topic의 구체적 정보)
          │
          ▼
vl_prompts/roadmap_prompt.md
(이 Topic 전용으로 맞춤화된 프롬프트)
          │
          ▼
AI에게 전달 → Topic에 최적화된 Roadmap 생성
```

**왜 이렇게 하는가?**
- templates/는 수정하지 않음 → 다음 Topic에도 재사용 가능
- vl_prompts/는 이 Topic만을 위한 것 → 이 Topic에 최적화
- 새 대화 세션에서도 vl_prompts/를 AI에게 주면 → 맥락 즉시 복원

---

## 템플릿 사용 체크리스트

### Phase 1 시작 전
- [ ] `topic_starter.md` 기반으로 `topic_info.md` 작성
- [ ] AI에게 폴더 구조 생성 요청
- [ ] `vl_prompts/roadmap_prompt.md` 생성 확인

### Phase 2 시작 전
- [ ] `vl_prompts/roadmap_prompt.md` 읽기
- [ ] AI에게 Roadmap 생성 요청
- [ ] `vl_roadmap/YYYYMMDD_RoadMap_{Topic}.md` 저장 확인

### Phase 3 매일
- [ ] `vl_prompts/daily_learning_prompt.md` 읽기 (AI가 자동)
- [ ] 현재 상황 정보 제공 (모듈, 가용 시간, 최근 WorkLog)
- [ ] 오늘의 계획 승인 후 시작

---

## 자주 묻는 질문

**Q: 템플릿 파일을 수정해도 되나요?**
A: templates/ 폴더의 파일은 수정하지 않는 것을 권장합니다. 수정이 필요하면 복사본을 만들어 수정하세요. templates/는 "범용 원본"으로 보존해야 다음 Topic에도 재사용 가능합니다.

**Q: 영어로 진행하고 싶어요.**
A: `templates/` 폴더에 `.en.md` 버전이 있습니다. `roadmap_prompt_template.en.md`, `daily_learning_prompt.en.md` 등을 사용하세요.

**Q: AI가 템플릿 파일을 직접 읽나요?**
A: Claude Code나 Cursor처럼 파일을 읽을 수 있는 AI라면 "파일명을 읽어줘"라고 하면 됩니다. 읽을 수 없는 AI(ChatGPT 웹)라면 파일 내용을 복사해서 붙여넣어야 합니다. CLI 환경 AI 사용을 강력히 권장합니다.

---

**작성자**: Claude with VibeLearn AI
**참조**: templates/ 폴더 전체, GETTING_STARTED.md Step 2-5
