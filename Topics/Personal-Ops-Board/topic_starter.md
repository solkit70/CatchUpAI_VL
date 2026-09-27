# VibeLearn AI Topic Starter — Personal-Ops-Board

> 이 파일은 새로운 Topic 학습을 시작할 때 작성하는 템플릿입니다.
>
> **작성일**: 2026-09-27 (Live #29 방송 중)
> **소스**: 개발 시작 Prompt 「방송용 — 복사해서 붙여 넣는 시작 프롬프트」 (비공개 `Materials_For_Topics/Personal-Ops-Board/`)

---

## 📌 Topic 기본 정보

### Topic 이름
```
Topic 이름: Personal-Ops-Board
(AI 시대에 맞는 나만의 일정 관리 앱)
```

### Topic 설명
```
설명: 볼트의 마크다운을 그래프로 읽고 AI 에이전트(AI4PKM 노드)가 유지하며 사람은 화면에서 우선순위만 보는
나만의 일정 관리 앱을, 라이브 방송에서 기능 하나씩 만들면서 아키텍처 문서를 함께 완성해 가는 프로젝트형 Topic.
Builders Lounge 5차 모임에서 다른 빌더에게 배운 방식(아키텍처 문서를 만들며 개발)을 적용한다.
```

### 학습 목적
```
학습 목적:
- AI 시대에 맞는 「AI Agent Application」을 실제로 만들어 본다
- 아키텍처를 미리 다 정하지 않고, 개발하며 대화와 결정을 문서로 쌓아 완성한다
- 끝나면 다음 에이전트 앱에 재사용할 아키텍처 템플릿을 얻는다
- 🧪 KIRO 식 「아키텍처를 개발과 동시에 업데이트」를 VibeLearn AI 에 접목하는 실험 —
  성공이면 VibeLearn AI 새 버전을 별도로 만든다 (2026-09-27 추가)
```

### 예상 학습 기간
```
예상 기간: 모듈 M0~M10, 모듈 하나 ≈ 라이브 방송 한 회(약 55분) + 주중 이어가기
          (기간이 적절한지 로드맵 단계에서 사용자에게 확인)
```

---

## 🎯 학습 목표

```
- [ ] 9/12 우선순위 To-Do 같은 4단계 보드를 사람 손 없이 앱이 만든다 (v1 완료 기준)
- [ ] 한 주 동안 우선순위를 손으로 정리하지 않는다
- [ ] 모든 모듈이 ARCHITECTURE.md 와 결정 기록을 갱신한 상태로 닫힌다
- [ ] 왜·어떻게 만들기로 했고 무엇을 준비했는지가 M0 산출물로 남는다
- [ ] 마지막에 재사용 가능한 「AI Agent Application 아키텍처 템플릿」이 나온다
```

---

## 🛠️ 학습 환경

### 운영 체제
```
OS: Windows 11
```

### 주요 도구 및 기술 스택
```
- VS Code
- Claude Code
- Python 3.13 (python-frontmatter)
- AI4PKM 오케스트레이터 (orchestrator.yaml) — 에이전트 런타임
- Obsidian (확인용)
```

### 사전 지식 (Prerequisites)
```
필수:
- Python 기초
- 마크다운 frontmatter
- 이 볼트의 Task Board / GDR(Daily Roundup) 구조

권장:
- AI 에이전트 · 오케스트레이션 개념
- 스펙 기반 개발 (Spec-driven development)
```

---

## 📚 참조 자료 (Optional)

### 공식 문서
```
- KIRO 공식 문서 (스펙 기반 개발): https://kiro.dev/docs/ — M0 에서 확인
- python-frontmatter: https://python-frontmatter.readthedocs.io/
```

### 튜토리얼 및 강의
```
- Builders Lounge 5차 발표 (5차 발표자 — 샌프란시스코의 한 빌더, Multi-Agent AI 개발기)
  KIRO 대목 00:03:22~00:04:40
```

### 관련 GitHub 저장소
```
- CatchUpAI_VL: https://github.com/solkit70/CatchUpAI_VL
```

### 추가 학습 자료
```
vl_materials/ 폴더에 추가할 자료:
- M0 「시작의 기록」 (공개용 — 실제 할 일 내용·이름은 가린다)

비공개 원자료 (Materials_For_Topics/Personal-Ops-Board/, 공개 레포 제외):
- PRD · BRD · 아이디어 정리 · 브레인덤프 원문 · 개발 시작 Prompt
- 개발 방식 — Builders Lounge 에서 배운 아키텍처 점진 완성
- 영상용 이야기 — 아이디어에서 개발 준비까지
- M1 인덱서 사전 점검
- 볼트 AI/Tasks/items/_schema.md (결정 로그)
```

---

## 🎓 학습 접근 방식 (Optional)

### 선호하는 학습 스타일
```
- [ ] 이론 먼저, 실습 나중
- [x] 실습 중심, 필요한 이론만 (권장)
- [ ] 이론과 실습 병행
```

### 시간 투자 계획
```
- 1회당 학습 시간: 라이브 방송 한 회(약 55분) + 주중 이어가기
- 학습 가능 요일: 일요일(라이브) + 주중
```

### 특별히 집중하고 싶은 영역
```
매 모듈의 한 바퀴 규칙:
① 요구 찾기(대화로) → ② 업계 방식 조사(2026년 9월 기준) → ③ 설계 제안 → 사용자 승인
→ ④ 구현·검증 → ⑤ ARCHITECTURE.md · decisions/ 갱신 → ⑥ WorkLog
```

### 지킬 것
```
- 이 Topic 폴더는 GitHub 공개 레포다. 실제 할 일 내용·사람 이름·연락처를 옮기지 않는다
- 앱 코드와 데이터는 볼트의 AI/Tasks/ 에만 둔다
- 승인이 필요한 곳에서는 멈추고 기다린다
```

---

## 🚀 다음 단계

1. ✅ Topic 폴더 생성 — `vl_prompts/` · `vl_roadmap/` · `vl_worklog/` · `vl_materials/` + `architecture/` · `architecture/decisions/`
2. `vl_prompts/roadmap_prompt.md` → STEP 1 학습 기간 검토 → 로드맵 초안 → 승인 뒤 저장
3. `vl_prompts/daily_learning_prompt.md` 로 첫 세션: M0 짧게 → M1 인덱서

---

**Template Version**: 1.0
**Created by**: VibeLearn AI Methodology
