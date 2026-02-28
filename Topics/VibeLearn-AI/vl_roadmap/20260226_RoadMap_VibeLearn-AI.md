# VibeLearn-AI 학습 로드맵

**생성일**: 2026-02-26
**방법론**: VibeLearn AI v2.0
**버전**: 1.0

---

## 📚 학습 개요

### Topic 소개

VibeLearn AI는 AI와 함께 무언가를 배우는 과정 전체를 체계적으로 이끌어주는 학습 방법론입니다. 이 Topic에서는 이 시스템을 직접 깊이 분석하고, 처음 접하는 사람도 바로 따라할 수 있는 교과서 품질의 문서를 만들며, 최종적으로 한국어·영어 소개 영상을 제작하여 시스템을 널리 알립니다.

> 이 학습 자체가 VibeLearn AI로 진행되므로 — **배우면서 그 방법론을 동시에 실전 검증하는** 유일한 케이스입니다.

### 학습 목표

- [x] VibeLearn AI 핵심 철학과 4단계 워크플로우를 설명할 수 있다
- [x] topic_starter → roadmap → daily_learning → worklog 사이클을 실행할 수 있다
- [x] 처음 사용자가 30분 안에 시작할 수 있는 가이드를 만들 수 있다
- [x] 기존 케이스(Clearly)를 케이스 스터디로 문서화할 수 있다
- [x] markdown-video 파이프라인으로 KR+EN 소개 영상을 제작할 수 있다

### 예상 학습 기간

집중적으로 빠르게 — 총 3개 모듈, 약 **12-16시간** (1-2주)

### 학습 환경

- **OS**: Windows 11
- **도구**: Claude Code, VS Code, markdown-video 파이프라인, GitHub
- **사전 지식**: GitHub 기본, Claude Code 사용 가능, 이미 VibeLearn AI를 사용 중

---

## 🗺️ 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 |
|------|--------|--------|----------|------------|
| M1 | 시스템 분석 & 개념 정립 | ⭐⭐ | 4h | `01-System-Overview/` |
| M2 | 사용자 가이드 & 케이스 스터디 | ⭐⭐ | 4-5h | `02-User-Guide/` |
| M3 | 소개 영상 제작 (Capstone) | ⭐⭐⭐ | 6-8h | `03-Intro-Video/` |

**총 예상 시간**: 14-17시간 (버퍼 포함)

---

## 📖 모듈별 상세 계획

---

### M1 - 시스템 분석 & 개념 정립

**난이도**: ⭐⭐
**예상 시간**: 4h
**산출물 폴더**: `01-System-Overview/`

#### 학습 목표

- [ ] VibeLearn AI의 핵심 철학("AI와 함께 배우고, 구조화하고, 다음 학습자의 길을 만든다")을 자신의 말로 설명할 수 있다
- [ ] 4단계 워크플로우(Phase 1~4)의 각 단계와 산출물을 정확히 설명할 수 있다
- [ ] templates/ 폴더의 각 파일(topic_starter, roadmap, daily_learning, workflow_guide)의 역할과 사용 시점을 설명할 수 있다
- [ ] 타겟 사용자 페르소나 3가지를 정의하고 각각의 진입 장벽과 해결책을 문서화할 수 있다
- [ ] 기존 학습 방법론 대비 VibeLearn AI의 3가지 차별화 포인트를 설명할 수 있다

#### 주요 개념

1. **핵심 철학**: "AI와 함께 배우고, 배운 것을 구조화하여, 다음 학습자를 위한 길을 만든다" — 개인 학습이 공동 자산이 되는 개념
2. **4단계 워크플로우**: Phase 1(Topic 설정) → Phase 2(Roadmap) → Phase 3(일일 학습) → Phase 4(완료/회고)
3. **템플릿 시스템**: Topic-agnostic 템플릿을 Topic 정보로 주입하여 커스터마이즈 — 범용성의 핵심
4. **교과서 품질 산출물**: 다른 학습자가 바로 따라할 수 있는 수준의 문서 — 재사용 가능성
5. **CVL (Continuous Vibe Learning)**: 지속 변화하는 기술에 대한 동기화 프로세스

#### 실습 과제

**실습 1: 시스템 구조 다이어그램 작성** ⭐
- **목적**: 전체 시스템을 한눈에 파악하고 시각적으로 표현
- **단계**:
  1. README.md, GETTING_STARTED.md, templates/ 모두 읽기
  2. 4단계 워크플로우를 Mermaid 다이어그램으로 표현
  3. 각 단계의 입력/출력 파일 매핑
  4. `01-System-Overview/concepts/workflow-diagram.md`에 저장
- **예상 시간**: 60분
- **검증**: 다이어그램만 봐도 전체 흐름이 이해되는지 확인

**실습 2: 타겟 사용자 페르소나 & 차별화 분석** ⭐⭐
- **목적**: 홍보 메시지 개발의 근거 마련
- **단계**:
  1. 타겟 사용자 3가지 페르소나 정의 (학생/직장인/크리에이터)
  2. 각 페르소나의 현재 학습 방법 vs VibeLearn AI 비교
  3. 경쟁 방법론(노션 메모, 유튜브만 보기, ChatGPT만 쓰기) 대비 차별화 포인트
  4. `01-System-Overview/concepts/target-users.md`에 저장
- **예상 시간**: 90분
- **검증**: 페르소나 문서를 읽은 사람이 "나를 위한 거구나"라고 느낄 수 있는지

**실습 3: 핵심 개념 설명 문서 작성** ⭐⭐
- **목적**: 처음 접하는 사람이 읽을 개념 문서 기초 작성
- **단계**:
  1. 시스템 제작자(본인)에게 핵심 개념 5가지 확인
  2. 각 개념을 1페이지 분량으로 문서화
  3. 실제 사용 예시(Clearly 케이스)와 연결
  4. `01-System-Overview/concepts/` 폴더에 저장
- **예상 시간**: 60분
- **검증**: 개념 문서만 읽어도 "왜 써야 하는지"가 이해되는지

#### 산출물

```
01-System-Overview/
├── README.md                    # M1 전체 요약 및 목차
├── concepts/
│   ├── what-is-vibelearn-ai.md  # VibeLearn AI란 무엇인가
│   ├── core-philosophy.md       # 핵심 철학 & 가치 제안
│   ├── workflow-diagram.md      # 4단계 워크플로우 다이어그램
│   ├── target-users.md          # 타겟 사용자 페르소나
│   └── key-concepts.md          # 핵심 용어 사전
└── guides/
    └── template-system.md       # 템플릿 시스템 설명
```

#### Definition of Done

- [ ] README.md, GETTING_STARTED.md, 모든 templates/ 파일 읽기 완료
- [ ] 4단계 워크플로우 다이어그램 작성 완료
- [ ] 타겟 사용자 페르소나 3가지 문서화 완료
- [ ] 핵심 개념 문서 최소 3개 작성 완료
- [ ] 모든 문서가 "다른 사람이 읽어도 이해되는" 수준인지 확인
- [ ] WorkLog 작성 + Daily Retrospective 완료

#### Self-Assessment

**개념 이해** (5분):
- [ ] VibeLearn AI가 무엇인지 30초 안에 설명할 수 있다
- [ ] 4단계 워크플로우를 순서대로 나열할 수 있다
- [ ] 이 시스템이 없었을 때와 있을 때의 차이를 예시로 설명할 수 있다

**실무 활용** (5분):
- [ ] 새 Topic을 시작할 때 어떤 파일을 열어야 하는지 안다
- [ ] daily_learning_prompt.md를 사용하는 타이밍을 안다

**교과서 품질** (5분):
- [ ] 내가 만든 문서만 보고 다른 사람이 VibeLearn AI를 이해할 수 있다

#### 예상 시간 배분

- 파일 읽기 & 분석: 60분
- 실습 1 (다이어그램): 60분
- 실습 2 (페르소나): 90분
- 실습 3 (개념 문서): 60분
- 문서화 & WorkLog: 30분
- **합계**: 4h 30min (버퍼 포함)

#### 참조 자료

- [VibeLearn AI README](../../../README.md): 전체 시스템 설명
- [GETTING_STARTED](../../../GETTING_STARTED.md): 빠른 시작 가이드
- [GitHub Repository](https://github.com/solkit70/VibeLearn-AI.git): 소스 원본
- [Clearly 케이스](../../Clearly-BRD-PRD/): 실제 사용 케이스 참조

---

### M2 - 사용자 가이드 & 케이스 스터디

**난이도**: ⭐⭐
**예상 시간**: 4-5h
**산출물 폴더**: `02-User-Guide/`

#### 학습 목표

- [ ] 처음 사용자가 30분 안에 첫 Topic을 시작할 수 있는 Step-by-step 가이드를 완성할 수 있다
- [ ] GitHub 클론부터 첫 WorkLog 작성까지 전체 과정을 스크린샷과 함께 문서화할 수 있다
- [ ] Clearly-BRD-PRD 케이스를 "VibeLearn AI로 배운 예시"로 구조화하여 문서화할 수 있다
- [ ] 처음 시작하는 사람이 가장 많이 막히는 3가지 장벽과 해결책을 정리할 수 있다

#### 주요 개념

1. **진입 장벽**: GitHub 클론 + Vibe Coding Tool 설정 — 이것만 넘으면 쉽다는 것이 핵심 메시지
2. **첫 Topic 경험**: topic_starter.md 작성 → AI가 알아서 → 학습 시작의 매끄러운 흐름
3. **케이스 스터디**: 실제 사례가 "나도 할 수 있다"는 확신을 줌
4. **FAQ 패턴**: 처음 사용자의 의문점을 미리 해소

#### 실습 과제

**실습 1: 완전 초보자용 Quick Start 가이드 작성** ⭐⭐
- **목적**: 진입 장벽을 최소화하는 가이드 제작
- **단계**:
  1. "GitHub 한 번도 안 써본 사람" 관점에서 시작
  2. Step 1: GitHub 클론 (스크린샷 포함)
  3. Step 2: Claude Code(또는 Cursor) 설정
  4. Step 3: 첫 Topic 시작 ("배우고 싶다"고 말하는 것만으로)
  5. Step 4: 첫 WorkLog 작성
  6. `02-User-Guide/guides/quick-start-30min.md`에 저장
- **예상 시간**: 90분
- **검증**: 이 가이드를 따라 하면 정말 30분 안에 시작되는지 확인

**실습 2: Clearly-BRD-PRD 케이스 스터디 작성** ⭐⭐
- **목적**: "이렇게 배웠고 이런 결과물이 나왔다"는 실증
- **단계**:
  1. Clearly 학습 과정 전체 回顧 (M1~M3, WorkLog 참조)
  2. 시작 전 상태 → 학습 과정 → 최종 산출물 구조로 정리
  3. "VibeLearn AI 없이 했다면?" 비교 섹션 추가
  4. YouTube 영상 링크 포함
  5. `02-User-Guide/case-studies/clearly-case.md`에 저장
- **예상 시간**: 90분
- **검증**: 케이스 스터디를 읽은 사람이 "나도 이렇게 해볼게"라고 생각하는지

**실습 3: FAQ & 트러블슈팅 가이드 작성** ⭐
- **목적**: 처음 사용자의 의문과 막힘 해소
- **단계**:
  1. 가장 예상되는 질문 10개 도출 (시스템 제작자에게 확인)
  2. 각 질문에 명확한 답변 + 예시 작성
  3. 흔한 실수와 해결책 섹션 추가
  4. `02-User-Guide/guides/faq.md`에 저장
- **예상 시간**: 60분
- **검증**: FAQ 읽은 후 막히는 부분이 없는지

#### 산출물

```
02-User-Guide/
├── README.md                        # M2 전체 요약
├── guides/
│   ├── quick-start-30min.md         # 30분 완성 빠른 시작
│   ├── detailed-workflow.md         # 전체 워크플로우 상세 설명
│   └── faq.md                       # 자주 묻는 질문
└── case-studies/
    ├── clearly-case.md              # Clearly 앱 학습 케이스
    └── overview.md                  # 케이스 스터디 개요
```

#### Definition of Done

- [ ] Quick Start 가이드 작성 완료 (30분 안에 시작 가능한 수준)
- [ ] Clearly 케이스 스터디 완성 (시작 → 과정 → 결과 구조)
- [ ] FAQ 10개 이상 작성 완료
- [ ] 모든 가이드가 실제로 동작하는지 검증
- [ ] WorkLog 작성 + Daily Retrospective 완료

#### Self-Assessment

**개념 이해**:
- [ ] "GitHub 처음 쓰는 사람"에게 시작 방법을 설명할 수 있다
- [ ] VibeLearn AI의 가장 큰 진입 장벽이 무엇인지 알고 해결책을 안다

**실무 활용**:
- [ ] Quick Start 가이드만 보고 누군가가 시작할 수 있다
- [ ] 케이스 스터디가 "나도 할 수 있다"는 확신을 줄 수 있다

#### 예상 시간 배분

- 실습 1 (Quick Start 가이드): 90분
- 실습 2 (케이스 스터디): 90분
- 실습 3 (FAQ): 60분
- 문서화 & WorkLog: 30분
- **합계**: 4h 30min (버퍼 포함)

#### 참조 자료

- [Clearly WorkLog M1](../../Clearly-BRD-PRD/vl_worklog/20260201_M1_Clearly-BRD-PRD.md): 케이스 참조
- [Clearly WorkLog M2](../../Clearly-BRD-PRD/vl_worklog/20260208_M2_Clearly-BRD-PRD.md): 케이스 참조
- [Clearly README](../../Clearly-BRD-PRD/README.md): 최종 산출물 참조
- [GETTING_STARTED.md](../../../GETTING_STARTED.md): 기존 빠른 시작 가이드

---

### M3 - 소개 영상 제작 (Capstone)

**난이도**: ⭐⭐⭐
**예상 시간**: 6-8h
**산출물 폴더**: `03-Intro-Video/`

#### 학습 목표

- [ ] VibeLearn AI 소개 영상 스크립트(KR+EN)를 완성할 수 있다 — M1·M2 문서를 근거로
- [ ] markdown-video 파이프라인을 실행하여 KR+EN 슬라이드 이미지를 생성할 수 있다
- [ ] TTS 오디오 + FFmpeg로 KR+EN MP4 영상을 완성할 수 있다
- [ ] YouTube 업로드용 제목·설명·태그를 KR+EN으로 작성할 수 있다

#### 주요 개념

1. **영상 기획**: 핵심 메시지 → 스토리라인 → 슬라이드 구성의 흐름
2. **markdown-video 파이프라인**: MD 스크립트 → Gemini 슬라이드 → TTS 오디오 → FFmpeg MP4
3. **YouTube 최적화**: 제목·설명·태그·챕터의 SEO 역할
4. **KR/EN 병렬 제작**: 공통 구조로 두 언어 효율적 제작

#### 실습 과제

**실습 1: 영상 기획 & KR 스크립트 작성** ⭐⭐
- **목적**: M1·M2 산출물을 16-20분 영상으로 구조화
- **단계**:
  1. 타겟 시청자와 핵심 메시지 확정 (M1의 페르소나 활용)
  2. 영상 구성 설계 (인트로 → 문제 제기 → 솔루션 → 데모 → 아웃트로)
  3. 슬라이드별 KR 스크립트 작성 (25-30개 슬라이드)
  4. `03-Intro-Video/clearly-intro-script-kr.md` 형식으로 저장
- **예상 시간**: 90분
- **검증**: 스크립트가 Clearly 영상과 동일한 구조와 품질인지

**실습 2: EN 스크립트 작성 & 슬라이드/오디오 생성** ⭐⭐⭐
- **목적**: KR 스크립트를 EN으로 변환하고 파이프라인 실행
- **단계**:
  1. KR 스크립트를 자연스러운 EN으로 번역
  2. `make_video.py --lang kr` 실행: TTS 오디오 생성
  3. `make_video.py --lang kr` Step 2: Gemini 슬라이드 생성
  4. `make_video.py --lang en` 동일 실행
  5. 결과물 확인 및 수정
- **예상 시간**: 120분
- **검증**: 27개 슬라이드 이미지 + 27개 MP3 파일 생성 확인

**실습 3: MP4 합성 & YouTube 메타데이터 작성** ⭐⭐
- **목적**: 최종 영상 완성 및 업로드 준비
- **단계**:
  1. `make_video.py` Step 3: KR+EN MP4 합성
  2. 영상 검토 (재생 시간, 오디오 싱크, 슬라이드 전환)
  3. YouTube 제목·설명·태그·챕터 KR+EN 작성
  4. `03-Intro-Video/youtube-metadata.md`에 저장
- **예상 시간**: 90분
- **검증**: KR·EN MP4 파일 생성 완료, YouTube 메타데이터 준비 완료

#### 산출물

```
03-Intro-Video/
├── README.md                          # M3 요약, 영상 링크
├── vibelearn-intro-script-kr.md       # KR 스크립트 (슬라이드 + 노트)
├── vibelearn-intro-script-en.md       # EN 스크립트
├── vibelearn-intro-script-kr - slides.md  # KR 슬라이드용 MD
├── vibelearn-intro-script-en - slides.md  # EN 슬라이드용 MD
├── audio-kr/                          # KR TTS 오디오 (27개 MP3)
├── audio-en/                          # EN TTS 오디오
├── slides-gemini-kr/                  # KR Gemini 슬라이드 JPEG
├── slides-gemini-en/                  # EN Gemini 슬라이드 JPEG
├── vibelearn-intro-kr.mp4             # 최종 KR 영상
├── vibelearn-intro-en.mp4             # 최종 EN 영상
└── youtube-metadata.md                # YouTube 제목·설명·태그·챕터
```

#### Definition of Done

- [ ] KR 스크립트 완성 (25개 이상 슬라이드)
- [ ] EN 스크립트 완성
- [ ] KR Gemini 슬라이드 생성 완료
- [ ] EN Gemini 슬라이드 생성 완료
- [ ] KR TTS 오디오 생성 완료
- [ ] EN TTS 오디오 생성 완료
- [ ] `vibelearn-intro-kr.mp4` 완성
- [ ] `vibelearn-intro-en.mp4` 완성
- [ ] YouTube 메타데이터 (제목·설명·태그) KR+EN 완성
- [ ] WorkLog 작성 + Daily Retrospective 완료

#### Self-Assessment

**개념 이해**:
- [ ] VibeLearn AI의 핵심 가치를 30초 영상 피치로 설명할 수 있다
- [ ] markdown-video 파이프라인의 3단계를 순서대로 설명할 수 있다

**실무 활용**:
- [ ] 다른 Topic의 소개 영상도 이 파이프라인으로 만들 수 있다
- [ ] YouTube SEO를 고려한 제목·설명·태그를 작성할 수 있다

**교과서 품질**:
- [ ] 두 영상이 Clearly 소개 영상과 동등한 품질인지 확인

#### 예상 시간 배분

- 실습 1 (기획 & KR 스크립트): 90분
- 실습 2 (EN 스크립트 & 파이프라인): 120분
- 실습 3 (MP4 & 메타데이터): 90분
- 문서화 & WorkLog: 30분
- **합계**: 7h (버퍼 포함)

#### 참조 자료

- [Clearly 스크립트 KR](../../Clearly-BRD-PRD/03-Clearly-Intro-Video/clearly-intro-script-kr.md): 형식 참조
- [Clearly 스크립트 EN](../../Clearly-BRD-PRD/03-Clearly-Intro-Video/clearly-intro-script-en.md): 형식 참조
- [markdown-video 파이프라인](../../Claude-Skills/temp-claude-obsidian-skills/markdown-video/): 실행 스크립트
- [make_video.py 사용법](../../Claude-Skills/temp-claude-obsidian-skills/markdown-video/make_video.py): 실행 방법

---

## 📝 WorkLog 작성 가이드

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_VibeLearn-AI.md`

- 예: `vl_worklog/20260226_M1_VibeLearn-AI.md`
- 예: `vl_worklog/20260227_M2_VibeLearn-AI.md`

**WorkLog 필수 섹션**:
1. 오늘의 학습 목표 (체크리스트)
2. 진행 내용 (실습별 상세 기록)
3. 문제 해결 로그
4. DoD 체크리스트
5. Daily Retrospective
6. 다음 세션 준비사항

---

## 🔍 Retrospective 가이드

### Daily Retrospective (매일, 5-10분)
WorkLog 내에 작성:
- What went well?
- What could be improved?
- Insights
- Tomorrow's focus

### Module Retrospective (모듈 완료 시, 15-20분)
`vl_worklog/YYYYMMDD_MX_Retrospective.md`:
- 계획 대비 실제 비교
- 핵심 학습 내용
- 발생한 문제와 해결
- Roadmap 정확도 평가

### Topic Retrospective (전체 완료 시, 30-60분)
`vl_worklog/YYYYMMDD_VibeLearn-AI_Final_Retrospective.md`:
- 전체 학습 여정 통계
- VibeLearn AI 방법론 효과성 평가 (이 시스템으로 이 시스템을 배운 특이점!)
- 산출물 품질 평가

---

## 📂 전체 폴더 구조

```
Topics/VibeLearn-AI/
├── topic_info.md
├── vl_prompts/
│   ├── roadmap_prompt.md
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── 20260226_RoadMap_VibeLearn-AI.md   ← 이 파일
├── vl_worklog/
│   ├── 20260226_M1_VibeLearn-AI.md
│   ├── 20260227_M2_VibeLearn-AI.md
│   └── 20260228_M3_VibeLearn-AI.md
├── 01-System-Overview/
│   ├── README.md
│   ├── concepts/
│   └── guides/
├── 02-User-Guide/
│   ├── README.md
│   ├── guides/
│   └── case-studies/
└── 03-Intro-Video/
    ├── README.md
    ├── *-script-kr.md / *-script-en.md
    ├── audio-kr/ / audio-en/
    ├── slides-gemini-kr/ / slides-gemini-en/
    └── *.mp4
```

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | 2026-02-26 | 2026-02-26 | ✅ | 100% | 6개 문서 생성 |
| M2 | 2026-02-26 | 2026-02-26 | ✅ | 100% | 5개 문서 생성 |
| M3 | 2026-02-27 | 2026-02-27 | ✅ | 100% | KR+EN MP4 완성, YouTube 메타데이터 준비 완료 |

**범례**: ⏳ 대기 / 🔄 진행 중 / ✅ 완료

**Topic 완료일**: 2026-02-27 | **최종 DoD**: 100% ✅

---

## 🎯 성공 기준

- [x] 모든 모듈 완료 (DoD 100%)
- [x] 3개 산출물 폴더 생성 (01, 02, 03)
- [x] KR+EN 소개 영상 완성 (YouTube 업로드 준비 완료)
- [x] Topic Retrospective 작성 (20260227_VibeLearn-AI_Final_Retrospective.md)
- [x] Self-Assessment 평균 ⭐⭐⭐⭐ 이상 (4.8/5 달성)

---

## 📊 학습 기간 적정성 분석

**요청 페이스**: 집중적으로 빠르게
**Topic 복잡도**: 중간 (시스템 분석 + 문서 작성 + 영상 제작)
**권장 기간**: 1-2주 집중 (총 12-17시간)

**분석 결과**: ✅ 적정함
- 시스템 제작자이므로 M1 분석이 빠르게 진행 가능
- markdown-video 파이프라인 경험이 있어 M3 제작이 수월
- 3개 모듈로 집중하면 1-2주 안에 완료 현실적

---

**생성자**: Claude with VibeLearn AI
**Roadmap 버전**: 1.0
**방법론 버전**: VibeLearn AI v2.0
