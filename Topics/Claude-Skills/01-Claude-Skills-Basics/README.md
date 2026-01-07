# M1 - Claude Skills 기본 개념

**모듈**: M1 - Claude Skills 기본 개념
**난이도**: ⭐
**학습 기간**: 2026-01-04 ~ 2026-01-07 (실제 학습일: 2일)
**현재 진행 상황**: ✅ 완료 (100%)

---

## 📚 모듈 개요

이 모듈에서는 Claude Skills의 기본 개념을 이해하고, Skill의 구조와 작동 원리를 학습합니다. 또한 CUA_VL 방법론을 Claude Skill로 만들 것인지 GitHub Repository로 유지할 것인지 판단하는 기초 지식을 습득합니다.

---

## 🎯 학습 목표

- [x] Claude Skills가 무엇인지, 왜 사용하는지 설명할 수 있다 ✅
- [x] Skill의 기본 구조 (manifest, entry point 등)를 이해한다 ✅
- [x] 간단한 "Hello World" Skill을 작성하고 실행할 수 있다 ✅
- [x] Claude Code에서 Skill을 등록하고 실행하는 방법을 안다 ✅
- [x] CUA_VL을 Skill vs GitHub Repository로 관리하는 것의 장단점을 비교할 수 있다 ✅

---

## 📂 폴더 구조

```
01-Claude-Skills-Basics/
├── README.md                 # 이 파일 - 모듈 개요
├── concepts/
│   └── claude-skills-overview.md    # Claude Skills 전체 개념 정리 ✅
├── examples/
│   └── hello-skill/                  # 첫 번째 실습 Skill ✅
│       ├── SKILL.md                  # Skill 정의 파일
│       └── README.md                 # 학습 가이드 (219줄)
├── guides/
│   └── cua-vl-skill-vs-repo.md      # CUA_VL Skill vs Repository 비교 분석 ✅
└── references/
    └── useful-links.md               # 공식 문서 및 참조 링크 ✅
```

---

## 📖 학습 내용

### Day 1 (2026-01-04) ✅

**실습 1: Claude Skills 공식 문서 탐색** (완료)

- Claude Skills의 정의와 목적 이해
- Skill의 기본 구조 (SKILL.md, 메타데이터, 지침) 파악
- Skill 작동 방식 3단계 (Discovery → Activation → Execution) 학습
- Skill 저장 위치 및 우선순위 이해
- Progressive Disclosure 개념 이해

**산출물**:
- ✅ [concepts/claude-skills-overview.md](concepts/claude-skills-overview.md) - 상세한 개념 정리
- ✅ [references/useful-links.md](references/useful-links.md) - 공식 문서 링크 모음

### Day 2 (2026-01-07) ✅

**실습 2: "Hello World" Skill 작성** (완료)
- 간단한 Skill 프로젝트 생성
- SKILL.md 파일 작성 (description 기반 자동 활성화)
- Personal Skills 폴더에 설치 (`~/.claude/skills/hello-skill/`)
- 실제 대화를 통한 실행 테스트 성공
- 산출물:
  - ✅ [examples/hello-skill/SKILL.md](examples/hello-skill/SKILL.md)
  - ✅ [examples/hello-skill/README.md](examples/hello-skill/README.md) - 219줄 학습 가이드

**실습 3: CUA_VL Skill vs Repository 비교 분석** (완료)
- CUA_VL을 Skill로 만들 경우 장단점 분석
- Repository로 유지할 경우 장단점 분석
- Option 3: 하이브리드 접근 (권장 ⭐)
- **결론**: Repository 유지 + 선택적 Skill 래퍼
- 산출물:
  - ✅ [guides/cua-vl-skill-vs-repo.md](guides/cua-vl-skill-vs-repo.md) - 394줄 심층 분석

**Module Retrospective 작성** (완료)
- M1 전체 학습 내용 정리
- 핵심 인사이트 3가지 도출
- 학습 효율성 분석
- M2 준비 사항 정리
- 산출물:
  - ✅ [vl_worklog/20260107_M1_Retrospective.md](../vl_worklog/20260107_M1_Retrospective.md)
  - ✅ [vl_worklog/20260107_M1_Day2_Claude-Skills.md](../vl_worklog/20260107_M1_Day2_Claude-Skills.md)

---

## 💡 핵심 학습 내용

### Claude Skills의 3가지 핵심 특징

1. **자동 활성화**: 사용자 요청과 Skill 설명의 의미적 일치로 자동 선택
2. **Progressive Disclosure**: 필요한 정보만 단계적으로 로드하여 성능 최적화
3. **간단한 포맷**: 마크다운 파일 하나로 시작 가능

### Skill의 기본 구조

```yaml
---
name: skill-name                # 소문자, 하이픈만 (최대 64자)
description: 무엇을 언제 사용   # Claude가 자동 선택하는 기준 (최대 1024자)
allowed-tools: [선택]           # Read, Bash, Grep 등
model: [선택]                   # 특정 모델 지정
---

# 지침
Claude가 따를 단계별 지침
```

### Skills vs. 다른 Claude Code 기능

| 기능 | 실행 시기 | 호출 방법 |
|------|---------|---------|
| **Skills** | Claude가 자동 선택 | 자동 (설명 기반) |
| **Slash Commands** | `/command` 입력 시 | 명시적 |
| **CLAUDE.md** | 모든 대화에 로드 | 자동 (항상) |

---

## 📚 참조 자료

상세한 참조 링크는 [references/useful-links.md](references/useful-links.md)를 참조하세요.

**주요 문서**:
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills.md)
- [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md)
- [Agent Skills Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md)

---

## 🎓 M1 완료 성과

### 학습 목표 달성도: 5/5 (100%) ✅

### 산출물 현황
- ✅ concepts/claude-skills-overview.md (350+ 줄)
- ✅ references/useful-links.md
- ✅ examples/hello-skill/SKILL.md
- ✅ examples/hello-skill/README.md (219줄)
- ✅ guides/cua-vl-skill-vs-repo.md (394줄)
- ✅ vl_worklog/20260107_M1_Retrospective.md
- ✅ vl_worklog/20260107_M1_Day2_Claude-Skills.md

**총 산출물**: 7개 파일, 1000+ 줄

### 핵심 결론
⭐ **CUA_VL은 GitHub Repository로 유지 + 선택적 Skill 래퍼 (하이브리드)**

---

## 🚀 다음 단계

**M2: Skill A - CUA_VL Skill 개발 (Day 3-4)**:
- 최소 기능 Skill 래퍼 실험
- Topic 폴더 생성 자동화
- 템플릿 복사 자동화
- Repository는 메인으로 유지

**M3: Skill B - YouTube→MD Skill 개발 (Day 5-8, 우선 완료)**:
- Jan 16 마감 (Seattle AI Memory 360 Tour)
- 한국어 자막 추출
- 마크다운 변환

---

**작성자**: CUA_VL Claude Skills 학습
**최종 업데이트**: 2026-01-07
**상태**: ✅ M1 완료 (100%)
