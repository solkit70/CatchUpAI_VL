# VibeLearn AI Roadmap 생성 프롬프트

**버전**: 2.0
**생성일**: 2025-12-28
**방법론**: VibeLearn AI

---

## 📌 사용 방법

이 프롬프트는 `topic_starter.md`에서 입력한 Topic 정보를 바탕으로 학습 로드맵을 자동 생성합니다.

**사용 절차**:
1. Topic 폴더가 생성되면 이 파일이 `[TopicName]/vl_prompts/`에 복사됨
2. Topic 정보가 이미 주입된 상태
3. 이 파일 전체를 AI에게 전달
4. AI가 VibeLearn AI 표준 로드맵 생성
5. 생성된 로드맵을 `vl_roadmap/YYYYMMDD_RoadMap_{Topic}.md`에 저장

---

## [1단계] Topic 정보 (자동 주입됨)

> **주의**: 이 섹션은 `topic_starter.md`의 정보로 자동으로 채워집니다.
> 수정이 필요하면 `topic_starter.md` 파일을 편집하세요.

### 기본 정보

**Topic 이름**: `Tehaleh-Community-Video`

**Topic 설명**:
```
Tehaleh 지역 소개 영상을 AI(Remotion)로 제작하는 전 과정 학습 및 실습 — 창발 발표 오프닝 데모 "AI로 이렇게 뚝딱 만들 수 있습니다"의 실제 사례
```

**학습 목적**:
```
- 창발 발표 오프닝 데모 영상 제작 ("AI로 이렇게 뚝딱 만들 수 있습니다" 증명)
- Tehaleh 커뮤니티를 시애틀/벨뷰 IT 종사자·은퇴 예정자에게 소개
- Remotion + edge-tts + gpt-image-2 통합 영상 제작 워크플로우 습득
```

**예상 학습 기간**: `1일 (집중 세션, ~6-8시간)`

---

### 환경 및 사전 지식

**운영 체제**: `Windows 11`

**주요 도구 및 기술 스택**:
```
- Remotion (TypeScript/React 기반 영상 제작 프레임워크)
- edge-tts (ko-KR-SunHiNeural 한국어 TTS)
- gpt-image-2 (OpenAI 이미지 생성 API)
- Node.js 18+
- Python 3 (gen_audio.py 오디오 생성 스크립트)
- VS Code
```

**사전 지식**:
```
필수:
- Remotion 기초 (컴포지션, 슬라이드 타입 이해)
- edge-tts 사용법 (gen_audio.py 실행 경험)

권장:
- gpt-image-2 API 사용법
- TypeScript/React 기초
```

---

### 산출물 및 참조

**학습 목표** (달성하고 싶은 것):
```
- [ ] Tehaleh 리서치 자료를 수집·구조화하여 tehaleh-research.md를 완성할 수 있다
- [ ] 영상 슬라이드 플랜(15-18장)을 video-slide-plan.md로 작성할 수 있다
- [ ] gpt-image-2 이미지 프롬프트를 image-prompts.md로 작성할 수 있다
- [ ] Remotion 컴포넌트(TehalehIntro0619)를 AI 도움으로 개발할 수 있다
- [ ] edge-tts로 한국어 나레이션 오디오를 생성할 수 있다
- [ ] MP4 영상(1920×1080)을 최종 렌더링할 수 있다
```

**참조 자료**:
```
- 기존 프롬프트: Ingest/CatchUpAI_VL/Topics/Material_For_Topics/Idea/Tehaleh-Community-Video/tehaleh-video-prompt.md
- Remotion 프로젝트: Ingest/CatchUpAI_VL/Topics/Remotion-VideoCreation/my-first-video/
- Tehaleh 공식 웹사이트: https://tehaleh.com
- Newland Communities: https://newlandcommunities.com
```

**vl_materials/ 폴더**:
```
- tehaleh-research.md (Phase 1 리서치 결과 — AI가 웹 검색으로 생성)
- 사용자 직접 촬영 사진은 public/tehaleh-intro-0619/images/ 경로에 별도 저장
```

---

## [2단계] AI에게 요청할 작업

위에 주입된 Topic 정보를 바탕으로 **VibeLearn AI 방법론**에 맞는 학습 로드맵을 생성해주세요.

---

### 🔍 STEP 1: 학습 기간 적정성 검토 (필수)

**로드맵 생성 전 반드시 수행:**

사용자가 입력한 학습 기간 `1일 (집중 세션, ~6-8시간)`이 해당 Topic에 적절한지 분석하고 피드백을 제공하세요.

#### 분석 기준:
1. **Topic 복잡도 평가**
   - 간단 (예: CLI 도구, 기본 개념): 3-7일 적정
   - 중간 (예: 프레임워크, 라이브러리): 2-4주 적정
   - 복잡 (예: 대규모 시스템, 다중 기술): 1-3개월 적정

2. **사전 지식 고려**
   - 사전 지식이 충분: 기간 단축 가능
   - 사전 지식 부족: 기간 연장 필요

3. **학습 목표 범위**
   - 기본 이해 수준: 짧은 기간
   - 실무 적용 수준: 중간 기간
   - 전문가 수준: 긴 기간

#### 피드백 형식:

```markdown
## 📊 학습 기간 적정성 분석

**사용자 입력 기간**: 1일 (집중 세션, ~6-8시간)
**Topic 복잡도**: [간단/중간/복잡]
**권장 기간**: [X주 또는 Y일]

**분석 결과**:
- ✅ **적정함**: 입력하신 기간이 이 Topic 학습에 적합합니다.
- ⚠️ **너무 짧음**: 이 Topic은 일반적으로 [권장 기간]이 필요합니다. 현재 기간으로는 핵심만 빠르게 학습하게 됩니다.
- ⚠️ **너무 김**: 이 Topic은 보통 [권장 기간]이면 충분합니다. 여유 있게 학습하거나 심화 내용까지 다룰 수 있습니다.

**조치 제안**:
- [적정함인 경우] 계획대로 진행합니다.
- [너무 짧은 경우] 1) 기간 연장 권장 또는 2) 학습 범위 축소 (기본만)
- [너무 긴 경우] 1) 기간 단축 또는 2) 심화 내용 추가

**사용자 확인 필요**:
위 분석 결과를 확인하시고 다음 중 선택해주세요:
1. "그대로 진행" - 입력한 기간으로 진행
2. "기간 조정" - 권장 기간으로 변경
3. "범위 조정" - 기간은 유지하되 학습 범위 조정
```

**중요**: 사용자가 확인하고 최종 결정할 때까지 로드맵 생성을 중단하고 대기하세요.

---

### 🗺️ STEP 2: 로드맵 생성 요구사항

사용자가 기간을 최종 확정한 후 아래 요구사항에 따라 로드맵을 생성하세요.

#### 전체 구조

**학습 기간**: `1일 (집중 세션, ~6-8시간)`에 맞춰 조정
- 3일 이하: 3-5개 모듈

**모듈 구성 원칙**:
- 각 모듈은 독립적으로 완료 가능한 단위
- 난이도는 점진적 상승 (Basics → Intermediate → Advanced)
- 마지막 모듈은 Capstone 프로젝트 (통합 실습)

**명명 규칙**:
- 모듈: `M1`, `M2`, `M3`, ...
- 산출물 폴더: `01-{TopicName}/`, `02-{TopicName}/`, ...

---

#### 각 모듈 필수 포함 사항

각 모듈은 다음 9가지 항목을 반드시 포함해야 합니다:

##### 1. 모듈 기본 정보
```markdown
### MX - {모듈명}

**난이도**: ⭐/⭐⭐/⭐⭐⭐ (1-3)
**예상 시간**: X시간
**산출물 폴더**: `0X-{모듈명}/`
```

##### 2. 학습 목표 (3-5개)
- 검증 가능하게 작성 ("~을 이해한다" X, "~을 구현할 수 있다" O)
- 체크리스트 형식 `- [ ]`
- 구체적이고 측정 가능한 목표

##### 3. 주요 개념
- 핵심 용어 정의 (3-5개)
- 각 개념에 대한 1-2문장 설명
- 오해하기 쉬운 포인트 명시

##### 4. 실습 과제 (2-3개)
각 실습마다:
- **과제명**: 명확한 이름
- **목적**: 왜 이 실습을 하는가
- **단계**: 구체적인 실행 단계 (1, 2, 3, ...)
- **예상 시간**: X분
- **난이도**: ⭐/⭐⭐/⭐⭐⭐
- **검증 방법**: 성공 여부를 어떻게 확인하는가

##### 5. 산출물
- 생성할 폴더 구조
- 필수 파일 목록 (README.md, 코드, 문서 등)
- 권장 하위 폴더 (`concepts/`, `examples/`, `guides/`, `troubleshooting/`)

##### 6. Definition of Done (완료 기준)
체크리스트 형식으로 5-8개:
```markdown
- [ ] 모든 학습 목표 달성
- [ ] 실습 과제 X개 완료
- [ ] 핵심 명령어/API Y개 실행 성공
- [ ] 산출물 폴더 생성 및 README 작성
- [ ] WorkLog 작성 완료
- [ ] Daily Retrospective 작성
```

##### 7. Self-Assessment (자가 평가)
AI 시대에 맞는 평가 기준 (3-5문항):
```markdown
**개념 이해** (5분):
- [ ] 이 기술/기능이 무엇인지 1-2문장으로 설명 가능
- [ ] 왜 필요한지 예시와 함께 설명 가능

**실무 활용** (5분):
- [ ] AI에게 이 기술을 사용한 작업 요청 가능
- [ ] AI가 생성한 코드의 품질 판단 가능

**문제 해결** (5분):
- [ ] 문제 발생 시 AI에게 디버깅 방향 제시 가능
```

##### 8. 예상 시간 배분
```markdown
- 개념 학습: X분 (20-30%)
- 실습 1: X분
- 실습 2: X분
- 문서화: X분
- **합계**: X시간 (버퍼 20% 포함)
```

##### 9. 참조 자료
- 공식 문서 링크 (필수)
- 튜토리얼/예제 (권장)
- 각 링크마다 1줄 설명

---

#### 실습 설계 원칙 (중요!)

실습 과제를 설계할 때 다음 원칙을 **반드시** 준수하세요:

##### 1. 실습 우선
- 이론 설명: 20-30%
- 실습 시간: 70-80%
- "개념 설명 → 즉시 실습" 패턴 반복

##### 2. 점진적 복잡도
- 실습 1: 간단 (⭐) - "Hello World" 수준
- 실습 2: 중간 (⭐⭐) - 실용적 기능
- 실습 3: 고급 (⭐⭐⭐) - 선택사항, 심화

##### 3. 검증 가능성
- 모든 실습은 실행 결과로 성공 여부 확인 가능
- 예: "로그 출력", "파일 생성", "API 응답 성공"
- 명확한 성공 기준 제시

##### 4. AI 시대 학습 범위
**인간이 알아야 할 것**:
- 개념적 이해 (무엇, 왜, 언제)
- 아키텍처 및 구조
- AI에게 효과적으로 지시하는 방법
- 기본 사용 패턴 (3-5개 핵심 기능)

**암기 불필요**:
- 상세 API 파라미터 목록
- 모든 옵션과 플래그
- 내부 구현 디테일

##### 5. 산출물 중심
- 매 모듈마다 폴더 생성 (`01-xxx/`, `02-xxx/`)
- **"교과서 품질"**: 다른 학습자가 이것만으로 학습 가능한 수준
- **README.md는 반드시 포함**

##### 6. 환경 고려
- Windows: PowerShell 명령어
- 경로 표기도 OS에 맞게 조정

---

#### VibeLearn AI 방법론 통합

로드맵에 다음 VibeLearn AI 요소들을 통합하세요:

##### 1. WorkLog 가이드
```markdown
## WorkLog 작성 가이드

각 학습 세션마다 WorkLog를 작성하여 진행 상황을 추적합니다.

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_{Topic}.md`
- 예: `vl_worklog/20260621_M1_Tehaleh-Community-Video.md`

**WorkLog 필수 섹션**:
1. 오늘의 학습 목표 (체크리스트)
2. 진행 내용 (실습별 상세 기록)
3. 문제 해결 로그
4. DoD 체크리스트 (모듈 완료 기준)
5. Daily Retrospective
6. 참조 및 산출물
```

##### 2. Retrospective 가이드
```markdown
## Retrospective 가이드

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
- 다음 모듈 준비사항

### Topic Retrospective (전체 완료 시, 30-60분)
`vl_worklog/YYYYMMDD_Tehaleh-Community-Video_Final_Retrospective.md`:
- 전체 학습 여정 통계
- VibeLearn AI 방법론 효과성 평가
- 산출물 품질 평가
- 향후 학습 개선 사항
```

---

## [3단계] 출력 형식

다음 Markdown 형식으로 로드맵을 생성하고 `vl_roadmap/YYYYMMDD_RoadMap_Tehaleh-Community-Video.md`에 저장하세요.

### 로드맵 템플릿 구조

```markdown
# Tehaleh-Community-Video 학습 로드맵

**생성일**: YYYY-MM-DD
**방법론**: VibeLearn AI
**버전**: 1.0

---

## 📚 학습 개요

### Topic 소개
{Topic 설명}

### 학습 목표
{topic_starter.md의 학습 목표}

### 예상 학습 기간
1일 (집중 세션, ~6-8시간)

### 학습 환경
- OS: Windows 11
- 도구: Remotion, edge-tts, gpt-image-2, Node.js 18+, Python 3
- 사전 지식: Remotion 기초, edge-tts 사용법

---

## 🗺️ 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 |
|------|--------|--------|----------|------------|
| M1 | Tehaleh 리서치 | ⭐ | ~2h | 01-Research/ |
| M2 | 슬라이드 플랜 | ⭐⭐ | ~1h | 02-SlidePlan/ |
| M3 | Remotion 개발 | ⭐⭐⭐ | ~3h | 03-RemotionDev/ |
| M4 | 오디오·렌더링 | ⭐⭐ | ~1.5h | 04-AudioRender/ |

**총 예상 시간**: ~7.5시간 (버퍼 포함)

---

## 📖 모듈별 상세 계획

{각 M1-M4 모듈 9개 항목 포함}

---

## 📝 WorkLog 작성 가이드
## 🔍 Retrospective 가이드
## 📂 전체 폴더 구조
## 📊 학습 진행 상황 추적
## 🎯 성공 기준
```

---

## ✅ 로드맵 품질 체크리스트

생성된 로드맵이 다음 기준을 충족하는지 확인하세요:

### 구조
- [ ] 학습 기간에 맞는 적절한 모듈 개수 (1일 → 3-5개)
- [ ] 점진적 난이도 상승 (Basics → Advanced)
- [ ] 마지막 Capstone 모듈 포함
- [ ] 각 모듈의 독립성 확보

### 각 모듈
- [ ] 학습 목표 3-5개 (검증 가능)
- [ ] 주요 개념 3-5개 (명확한 정의)
- [ ] 실습 과제 2-3개 (구체적 단계)
- [ ] 산출물 구조 명시
- [ ] DoD 체크리스트 5-8개
- [ ] Self-Assessment 3-5문항
- [ ] 시간 배분 명시 (버퍼 포함)
- [ ] 참조 자료 링크
- [ ] 9가지 필수 항목 모두 포함

### VibeLearn AI 통합
- [ ] WorkLog 가이드
- [ ] Retrospective 가이드 (3단계)
- [ ] 폴더 구조 명시
- [ ] 진행 상황 추적 테이블

---

**생성자**: Claude with VibeLearn AI
**Template 버전**: 2.0
**생성일**: 2025-12-28
**방법론**: VibeLearn AI
