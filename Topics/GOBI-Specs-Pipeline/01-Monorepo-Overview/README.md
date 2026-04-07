# M1 - gobi-monorepo + gobi-ai/docs 전체 구조 파악

**모듈**: M1 | **상태**: ✅ 완료 | **학습 시간**: 약 3h (2026-04-06)

---

## 이 모듈에서 배우는 것

GOBI 에코시스템의 두 핵심 레포를 직접 클론하여 분석합니다.

| # | 문서 | 설명 |
|---|------|------|
| 1 | [repo-structure.md](repo-structure.md) | gobi-monorepo 7개 프로젝트 + specs/ 26개 파일 + gobi-ai/docs 구조 전체 정리 |
| 2 | [pipeline-diagram.md](pipeline-diagram.md) | specs → docs.gobihq.com 파이프라인 다이어그램 + Vibe Guiding 통합 제안 |

---

## 핵심 요약

### 1. gobi-monorepo = 7개 프로젝트 + specs + AI 워크플로우
- 각 프로젝트는 독립 레포로 분리 관리 (root에 빌드 시스템 없음)
- `specs/` = 26개 cross-cutting feature spec (구현 방식 X, 기능 정의 O)
- `prompts/CODE_TO_SPECS.md` = AI가 코드에서 spec을 생성하는 프롬프트 (이미 존재!)
- `LINEAR.md` = Planner AI → Developer AI → PR Reviewer AI 에이전트 파이프라인 운영 중

### 2. gobi-ai/docs = Mintlify 기반 문서 사이트
- MDX 포맷, docs.json으로 내비게이션 설정
- git push → Mintlify 자동 빌드 → docs.gobihq.com 배포 (자동)
- 현재 초기 단계 (Products 4개 + Reference 2개)

### 3. 핵심 발견: 파이프라인에 수동 단계가 있다
```
specs (Markdown) → [수동 변환 ⚠️] → docs (MDX) → [자동 배포 ✅] → docs.gobihq.com
```
- specs는 기능별, docs는 제품별 → 직접 1:1 변환 불가
- **이 수동 변환 단계 = VibeLearn AI/Vibe Guiding의 핵심 기회**

### 4. CODE_TO_SPECS → SPECS_TO_GUIDE 방향 제안
- 개발팀: 코드 → AI → specs (이미 구현)
- Vibe Guiding 제안: specs → VibeLearn AI → 사용자 가이드 + 앱 내 Vibe Guiding 컨텍스트

---

## 다음 모듈

→ **[M2: Vibe Guiding 핵심 Spec 파일 심층 분석](../02-Specs-Deep-Dive/README.md)**
- 분석 대상: 05(Second Brain Agent), 06(Voice), 07(Capture), 19(Orchestration)
