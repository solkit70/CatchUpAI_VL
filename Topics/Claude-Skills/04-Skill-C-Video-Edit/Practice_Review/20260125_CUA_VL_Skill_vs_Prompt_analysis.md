# CUA_VL: Skill vs Prompt 접근법 비교 분석

**작성일**: 2026-01-25
**작성자**: Claude
**목적**: CUA_VL 방법론에 Skill 접근법을 적용할지 여부 분석

---

## 1. 배경

### 1.1 분석 대상
- **02-Skill-A-CUA-VL**: CUA_VL 학습 방법론을 지원하는 Claude Skill 개발 연구
- **기존 CUA_VL**: 프롬프트 템플릿 기반 학습 방법론

### 1.2 핵심 질문
> Skill을 CUA_VL 핵심 방법론에 포함해야 하는가, 아니면 프롬프트 기반을 유지해야 하는가?

### 1.3 사용자 우려
- Skill은 Claude에서만 사용 가능
- 다른 AI 도구 사용자(ChatGPT, Gemini 등)는 Skill을 사용할 수 없음
- 방법론의 범용성이 제한될 수 있음

---

## 2. 핵심 문제: 플랫폼 종속성

| 접근법 | 사용 가능 플랫폼 | 종속성 |
|--------|-----------------|--------|
| **Skill (SKILL.md)** | Claude Code/Desktop만 | 높음 |
| **프롬프트 (Prompt)** | 모든 AI 도구 | 없음 |

---

## 3. 사용자 유형별 분석

### 3.1 Claude 전용 사용자
- Skill 사용 가능
- 70% 시간 절약 효과 누림
- 자동화된 워크플로우

### 3.2 다른 AI 도구 사용자 (ChatGPT, Gemini, Copilot 등)
- **Skill 사용 불가**
- 프롬프트 템플릿만 사용 가능
- 수동 워크플로우

### 3.3 현실적 비율 추정

| AI 도구 | 시장 점유율 (추정) |
|---------|------------------|
| ChatGPT | ~60% |
| Claude | ~20% |
| Gemini | ~10% |
| 기타 | ~10% |

**결론**: CUA_VL 잠재 사용자의 **~80%가 Skill을 사용할 수 없음**

---

## 4. 두 접근법 상세 비교

| 항목 | Skill 접근법 | 프롬프트 접근법 |
|------|-------------|----------------|
| **범용성** | ❌ Claude만 | ✅ 모든 AI |
| **자동화** | ✅ 폴더 생성, 파일 탐색 | ❌ 수동 |
| **유지보수** | 2곳 (SKILL.md + 템플릿) | 1곳 (템플릿만) |
| **학습 곡선** | Skill 설치 필요 | 없음 |
| **시간 절약** | 70% | 0% (기준선) |
| **배포 복잡도** | 높음 | 낮음 |
| **문서화 부담** | 높음 (설치 가이드 필요) | 낮음 |

---

## 5. Skill이 실제로 하는 것 분석

02-Skill-A-CUA-VL의 SKILL.md가 하는 일을 분해:

### 5.1 `/cua-vl start` - 새 Topic 시작

| 단계 | 내용 | 프롬프트로 대체 가능? |
|------|------|---------------------|
| 1 | Topic 이름 질문 | ✅ 가능 |
| 2 | 폴더 생성 (mkdir) | ❌ **자동화의 핵심 가치** |
| 3 | 템플릿 제공 | ✅ 가능 |
| 4 | 다음 단계 안내 | ✅ 가능 |

### 5.2 `/cua-vl roadmap` - Roadmap 생성

| 단계 | 내용 | 프롬프트로 대체 가능? |
|------|------|---------------------|
| 1 | topic_info.md 확인 | ✅ 가능 |
| 2 | 템플릿 읽기 | ✅ 가능 |
| 3 | 변수 치환 | ✅ 가능 |
| 4 | 다음 단계 안내 | ✅ 가능 |

### 5.3 `/cua-vl daily` - 일일 학습

| 단계 | 내용 | 프롬프트로 대체 가능? |
|------|------|---------------------|
| 1 | Roadmap/WorkLog 파일 탐색 | ❌ **자동화의 핵심 가치** |
| 2 | 현재 상황 요약 | ✅ 가능 (파일 제공 시) |
| 3 | 템플릿 제공 | ✅ 가능 |

### 5.4 핵심 발견

> Skill의 진정한 가치는 **파일 시스템 자동화**(폴더 생성, 파일 탐색)뿐
>
> 나머지 기능은 모두 프롬프트로 대체 가능

---

## 6. 대안: "Universal Prompt" 접근법

### 6.1 개념
기존 템플릿을 **워크플로우 가이드 프롬프트**로 재구성

### 6.2 구조 제안

```
templates/
├── topic_starter.md              # (기존 유지)
├── roadmap_prompt_template.md    # (기존 유지)
├── daily_learning_prompt.md      # (기존 유지)
└── workflow_guide.md             # (신규) 워크플로우 가이드 프롬프트
```

### 6.3 `workflow_guide.md` 예시

```markdown
# CUA_VL 워크플로우 가이드

## 1. 새 Topic 시작 시
다음 정보를 AI에게 제공하세요:

"CUA_VL 방법론으로 새 Topic을 시작합니다.
- Topic 이름: [입력]
- 학습 목적: [입력]

다음 폴더 구조를 만들어주세요:
Topics/{TopicName}/
├── topic_info.md
├── vl_prompts/
├── vl_roadmap/
├── vl_worklog/
└── vl_materials/

그리고 topic_starter.md 템플릿을 제공해주세요."

## 2. Roadmap 생성 시
[roadmap_prompt_template.md 사용 방법 안내]

## 3. 일일 학습 시작 시
[daily_learning_prompt.md 사용 방법 안내]
```

---

## 7. 권장 사항

### 7.1 결론: **프롬프트 우선, Skill 선택적**

| 우선순위 | 접근법 | 대상 |
|---------|--------|------|
| **1순위** | 프롬프트 템플릿 | 모든 사용자 (100%) |
| **2순위** | Skill (선택적) | Claude 사용자 (~20%) |

### 7.2 구체적 권장 사항

#### Template Repository에 반영할 것:

1. **`workflow_guide.md` 신규 추가**
   - 워크플로우별 프롬프트 사용법
   - 플랫폼 독립적
   - 모든 AI에서 사용 가능

2. **기존 템플릿 유지**
   - topic_starter.md
   - roadmap_prompt_template.md
   - daily_learning_prompt.md

3. **Skill은 별도 선택 옵션으로**
   - README.md에 "Claude 사용자를 위한 선택적 Skill" 섹션
   - SKILL.md는 extras/ 폴더에 제공
   - 핵심 방법론에 포함하지 않음

### 7.3 문서 구조 제안

```
CatchUpAI_VL_Template/
├── README.md                     # 핵심 방법론
├── GETTING_STARTED.md            # 빠른 시작 (프롬프트 기반)
├── templates/
│   ├── topic_starter.md
│   ├── roadmap_prompt_template.md
│   ├── daily_learning_prompt.md
│   └── workflow_guide.md         # (신규) 워크플로우 프롬프트
└── extras/                       # (신규) 선택적 확장
    └── claude-skill/
        ├── SKILL.md
        └── README.md             # Claude 사용자용 설치 가이드
```

---

## 8. 최종 분석

| 항목 | Skill을 핵심에 포함 | Skill을 선택 옵션으로 |
|------|-------------------|---------------------|
| **사용자 도달률** | ~20% (Claude만) | **100%** |
| **유지보수 부담** | 높음 | 낮음 |
| **방법론 순수성** | 도구 종속 | **도구 독립** |
| **확장성** | 제한적 | 높음 |
| **배포 복잡도** | 높음 | **낮음** |

---

## 9. 최종 권장

> **Skill을 CUA_VL 핵심 방법론에 포함하지 않는 것이 좋습니다.**
>
> 대신:
> 1. **프롬프트 기반 워크플로우 가이드**를 핵심으로
> 2. **Skill은 "Claude 사용자를 위한 선택적 편의 도구"**로 분리
> 3. 방법론의 **플랫폼 독립성** 유지

---

## 10. 다음 단계 (실행 계획)

### 10.1 단기 (권장)
- [ ] `templates/workflow_guide.md` 신규 작성
- [ ] README.md에 "선택적 확장" 섹션 추가
- [ ] `extras/claude-skill/` 폴더 구조 생성

### 10.2 중기 (선택)
- [ ] SKILL.md를 extras/ 폴더로 이동
- [ ] Claude Skill 설치 가이드 작성
- [ ] Template Repository 업데이트

### 10.3 장기 (선택)
- [ ] 다른 AI 도구용 확장 (GPTs, Gemini Gems 등)
- [ ] 커뮤니티 피드백 수집
- [ ] 방법론 v3.0 기획

---

## 부록: 02-Skill-A-CUA-VL 연구 요약

### A.1 구현된 기능
- `/cua-vl start`: 새 Topic 시작
- `/cua-vl roadmap`: Roadmap 생성 지원
- `/cua-vl daily`: 일일 학습 지원

### A.2 측정된 효과
| 작업 | Skill 없음 | Skill 사용 | 시간 절약 |
|------|-----------|-----------|----------|
| Topic 시작 | 5분 | 1분 | 80% |
| Roadmap 생성 | 10분 | 3분 | 70% |
| 일일 학습 시작 | 5분 | 2분 | 60% |
| **전체** | **20분** | **6분** | **70%** |

### A.3 핵심 인사이트
1. "Skill은 Gateway, Repository는 Core"
2. "명확한 다음 단계가 UX의 핵심"
3. "자동 감지보다 명확한 질문"

---

**문서 끝**
