---
title: "Vibe-Guiding-VSCode 학습 로드맵"
created: 2026-04-26 23:17:07
tags:
  - vibe-guiding
  - roadmap
  - vibelearn-ai
  - vscode
  - gobi
sources:
  - "[[VibeGuiding_BrainDump]]"
  - "[[2026-04-03 GOBI Vibe Guiding 시스템 맵]]"
  - "[[2026-04-05 Vibe Guiding 구현 계획]]"
  - "[[2026-04-09 - Proposal - Vibe Guiding Architecture for Gobi]]"
  - "[[2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]]"
---

## 학습 기간 적정성 분석

**사용자 입력 기간**: 4-6주, 총 30-45시간  
**Topic 복잡도**: 복잡  
**권장 기간**: 4-6주

**분석 결과**: 적정하다. 이 Topic은 단순 개념 학습이 아니라 Vibe Manual/CVL 설계, 사용자 상태 수집, Triggering, Retrieval, Guide Response 생성까지 포함하는 개발 실습 Topic이다. 이미 [[2026-04-03 GOBI Vibe Guiding 시스템 맵]], [[2026-04-05 Vibe Guiding 구현 계획]], [[2026-04-09 - Proposal - Vibe Guiding Architecture for Gobi]] 같은 선행 자료가 있으므로 4-6주 안에 첫 POC까지 도달하는 계획이 현실적이다.

**조치 제안**: 계획대로 진행한다. 단, M3의 POC 개발 범위가 커지면 GOBI Desktop/Applet 통합은 M5 이후 별도 Topic 또는 후속 모듈로 분리한다.

## 학습 개요

### Topic 소개

Vibe-Guiding-VSCode는 VibeLearn AI 학습 방법론을 사용해서 Vibe Guiding을 공부하고, VS Code에서 직접 개발 실습까지 진행하는 Topic이다. 핵심 목표는 VibeLearn AI가 만든 최신 Vibe Manual을 사용자의 상황에 맞게 활성화하는 Guiding Engine의 최소 POC를 만드는 것이다.

> "이 매뉴얼을 인간이 보기도 하겠지만 AI 에게는 이 Topic 에 대해 잘 정리된 context 가 되어서 해당 Topic 에 대해 필요한 사람에게 필요한 내용을 필요할 때에 알려주는 Guide 를 할 수 있게 만들 수 있겠다"  
> - [[VibeGuiding_BrainDump]]

### 학습 목표

- [ ] Vibe Guiding의 핵심 개념을 Vibe Learning, Vibe Manual, CVL, Triggering, User Context, Guide Response로 나누어 설명할 수 있다.
- [ ] GOBI 문서/스펙/소스/기존 테스트 기록을 바탕으로 AI-optimized Vibe Manual 구조를 설계할 수 있다.
- [ ] VS Code에서 실행 가능한 사용자 상태 수집기와 Guiding Engine POC를 구현할 수 있다.
- [ ] 최신 매뉴얼 기반 Retrieval과 사용자 맥락 기반 응답 조립을 분리해서 설계할 수 있다.
- [ ] 실제 GOBI 사용 흐름에서 발생한 실패/혼란 상황을 Triggering 테스트 케이스로 바꿀 수 있다.

### 예상 학습 기간

4-6주, 총 30-45시간

### 학습 환경

- OS: Windows 11
- 도구: VS Code, Claude Code 또는 Codex, Python 3.12+, Markdown, GOBI Desktop, GOBI CLI, GOBI Space
- 사전 지식: VibeLearn AI 흐름, GOBI 생태계 기본 구성, Python 파일/JSON/Markdown 처리, VS Code 기본 사용

## 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 |
|------|--------|--------|----------|-------------|
| M1 | Vibe Guiding 개념과 Source Map | ⭐⭐ | 5h | `01-Vision-and-Architecture/` |
| M2 | Two-Component Architecture 설계 | ⭐⭐ | 6h | `02-Architecture-Design/` |
| M3 | Vibe Manual과 CVL 설계 | ⭐⭐ | 7h | `03-Vibe-Manual-CVL/` |
| M4 | Guiding Engine POC 개발 | ⭐⭐⭐ | 12h | `04-Guiding-Engine-POC/` |
| M5 | GOBI 시나리오 검증 | ⭐⭐⭐ | 7h | `05-GOBI-Scenario-Tests/` |
| M6 | 통합 계획과 Demo Capstone | ⭐⭐ | 6h | `06-Integration-Demo/` |

**총 예상 시간**: 43시간

## 모듈별 상세 계획

### M1 - Vibe Guiding 개념과 Source Map

**난이도**: ⭐⭐  
**예상 시간**: 5h  
**산출물 폴더**: `01-Vision-and-Architecture/`

#### 학습 목표

- [ ] Vibe Guiding을 Vibe Learning의 후속 레이어로 설명할 수 있다.
- [ ] 핵심 Source 문서 5개의 역할과 연결 관계를 정리할 수 있다.
- [ ] Substack 글 3개를 현재 접근 가능한 범위와 미확보 본문으로 구분할 수 있다.
- [ ] Vibe Guiding의 30초 설명과 3분 설명을 작성할 수 있다.

#### 주요 개념

1. **Vibe Learning**: 특정 Topic에 대한 학습과 실습을 통해 교과서 품질의 매뉴얼을 만드는 과정이다.
2. **Vibe Guiding**: 만들어진 매뉴얼을 사용자 맥락에 맞게 필요할 때 활성화하는 안내 시스템이다.
3. **Build the Brain**: Vibe Manual과 CVL로 최신 지식 기반을 만드는 단계다.
4. **Activate the Brain**: 사용자 상태를 보고 필요한 안내를 제공하는 단계다.
5. **Source Map**: 어떤 문서가 어떤 판단의 근거인지 추적하는 지도다.

#### 실습 과제

**실습 1: Source Map 작성** ⭐
- **목적**: 흩어진 자료를 Roadmap 실행에 필요한 근거 자료로 재정렬한다.
- **단계**:
  1. `VibeGuiding_BrainDump.md`에서 핵심 철학 문장을 추출한다.
  2. [[2026-04-03 GOBI Vibe Guiding 시스템 맵]]에서 대상 시스템과 리포지토리를 정리한다.
  3. [[2026-04-05 Vibe Guiding 구현 계획]]에서 Phase 구조를 정리한다.
  4. [[2026-04-09 - Proposal - Vibe Guiding Architecture for Gobi]]에서 엔진 구성 요소를 추출한다.
  5. [[2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]]에서 실패/한계 항목을 Trigger 후보로 바꾼다.
- **예상 시간**: 90분
- **검증**: `source-map.md`에 모든 Source의 역할, 핵심 인사이트, 다음 사용 모듈이 기록되어 있다.

**실습 2: Vibe Guiding 설명문 작성** ⭐⭐
- **목적**: 개발 전에 개념을 흔들리지 않게 고정한다.
- **단계**:
  1. 30초 설명을 작성한다.
  2. 3분 설명을 작성한다.
  3. Vibe Learning과의 차이를 표로 정리한다.
  4. GOBI 적용 예시를 한 단락으로 작성한다.
- **예상 시간**: 90분
- **검증**: 설명문만 읽어도 Vibe Guiding이 "문서 검색 챗봇"이 아니라 "사용자 상황 기반 안내 시스템"임이 드러난다.

**실습 3: POC 대상 후보 평가** ⭐⭐
- **목적**: 첫 개발 실습 대상을 좁힌다.
- **단계**:
  1. GOBI CLI, GOBI Desktop Custom Homepage/Applet, GOBI Space를 후보로 둔다.
  2. 로컬 재현 가능성, 상태 수집 가능성, 테스트 난이도를 비교한다.
  3. M4 POC의 1차 대상을 확정한다.
- **예상 시간**: 60분
- **검증**: `poc-target-selection.md`에 선택 대상과 제외 이유가 명확히 기록되어 있다.

#### 산출물

```
01-Vision-and-Architecture/
├── README.md
├── source-map.md
├── what-is-vibe-guiding.md
└── poc-target-selection.md
```

#### Definition of Done

- [ ] 핵심 Source 5개를 읽고 Source Map 작성
- [ ] Vibe Guiding 30초 설명 작성
- [ ] Vibe Learning vs Vibe Guiding 비교표 작성
- [ ] 첫 POC 대상 후보 평가 완료
- [ ] `01-Vision-and-Architecture/README.md` 작성
- [ ] WorkLog 작성 및 Daily Retrospective 완료

#### Self-Assessment

**개념 이해**:
- [ ] Vibe Guiding이 왜 Vibe Learning 위에서 의미가 생기는지 설명할 수 있다.
- [ ] Build the Brain과 Activate the Brain을 구분할 수 있다.

**실무 활용**:
- [ ] AI에게 Vibe Guiding Source Map 작성을 지시할 수 있다.
- [ ] 첫 POC 대상 선택 기준을 설명할 수 있다.

**문제 해결**:
- [ ] Source 본문이 없는 Substack 링크를 Roadmap에서 어떻게 취급해야 하는지 판단할 수 있다.

#### 예상 시간 배분

- 개념 학습: 60분
- 실습 1: 90분
- 실습 2: 90분
- 실습 3: 60분
- 문서화/WorkLog: 60분
- **합계**: 5h

#### 참조 자료

- [[VibeGuiding_BrainDump]]: Vibe Guiding의 원래 문제의식과 철학
- [[2026-04-03 GOBI Vibe Guiding 시스템 맵]]: GOBI 대상 시스템과 리포지토리 지도
- [[2026-04-05 Vibe Guiding 구현 계획]]: Vibe Manual, PCM, CVL, 제품 통합 단계
- [[2026-04-09 - Proposal - Vibe Guiding Architecture for Gobi]]: 통합 컨텍스트와 가이딩 엔진 구조
- [[2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]]: 실제 테스트에서 드러난 한계와 개선 포인트

### M2 - Two-Component Architecture 설계

**난이도**: ⭐⭐  
**예상 시간**: 6h  
**산출물 폴더**: `02-Architecture-Design/`

#### 학습 목표

- [ ] Vibe Manual/CVL 컴포넌트와 Guiding Engine 컴포넌트의 책임을 분리할 수 있다.
- [ ] 각 컴포넌트의 입력, 출력, 데이터 저장 위치, 실패 모드를 정의할 수 있다.
- [ ] 사용자 상태 수집, Triggering, Retrieval, Guide Composer의 흐름을 Mermaid로 표현할 수 있다.
- [ ] VS Code POC에서 앱 통합 전 검증해야 할 경계를 정할 수 있다.

#### 주요 개념

1. **Vibe Manual/CVL 컴포넌트**: 최신 GOBI 지식을 구조화하고 유지하는 컴포넌트다.
2. **Guiding Engine 컴포넌트**: 사용자 맥락을 받아 필요한 지식을 찾아 안내로 바꾸는 컴포넌트다.
3. **Context Collector**: OS, 도구 버전, 설정, 현재 문제 신호를 수집하는 모듈이다.
4. **Trigger Evaluator**: 안내가 필요한 시점인지 판단하는 모듈이다.
5. **Guide Composer**: 검색된 지식을 사용자 수준에 맞게 재구성하는 모듈이다.

#### 실습 과제

**실습 1: 컴포넌트 책임표 작성** ⭐
- **목적**: 구현 중 책임이 섞이지 않게 한다.
- **단계**:
  1. 각 컴포넌트의 입력과 출력을 표로 만든다.
  2. 각 컴포넌트가 절대 하지 말아야 할 일을 정의한다.
  3. 실패 모드와 fallback을 정리한다.
- **예상 시간**: 90분
- **검증**: `component-responsibilities.md`만 보고도 코드 모듈 경계를 설명할 수 있다.

**실습 2: Architecture Diagram 작성** ⭐⭐
- **목적**: 데이터 흐름과 제어 흐름을 시각화한다.
- **단계**:
  1. Vibe Manual 생성/업데이트 흐름을 Mermaid로 작성한다.
  2. Guiding Engine 실행 흐름을 Mermaid로 작성한다.
  3. 두 흐름이 만나는 지점을 표시한다.
- **예상 시간**: 90분
- **검증**: 다이어그램에 `manual_index`, `user_context`, `trigger_rules`, `guide_response`가 모두 포함된다.

**실습 3: POC Boundary 정의** ⭐⭐
- **목적**: 처음 POC의 범위를 앱 통합이 아니라 로컬 검증으로 제한한다.
- **단계**:
  1. 이번 Topic에서 구현할 것과 구현하지 않을 것을 나눈다.
  2. GOBI Desktop/Applet 통합은 M6의 계획으로 미룬다.
  3. Python CLI 방식의 POC 입출력 파일을 정의한다.
- **예상 시간**: 90분
- **검증**: `poc-boundary.md`에 MVP 범위와 제외 범위가 명확히 구분되어 있다.

#### 산출물

```
02-Architecture-Design/
├── README.md
├── component-responsibilities.md
├── architecture-diagrams.md
└── poc-boundary.md
```

#### Definition of Done

- [ ] 컴포넌트 책임표 작성
- [ ] Vibe Manual/CVL 다이어그램 작성
- [ ] Guiding Engine 다이어그램 작성
- [ ] POC 범위와 제외 범위 정의
- [ ] `02-Architecture-Design/README.md` 작성
- [ ] WorkLog 작성 및 Daily Retrospective 완료

#### Self-Assessment

**개념 이해**:
- [ ] Vibe Manual/CVL과 Guiding Engine의 책임 차이를 설명할 수 있다.
- [ ] Triggering과 Retrieval이 왜 분리되어야 하는지 설명할 수 있다.

**실무 활용**:
- [ ] AI에게 각 컴포넌트별 파일 구조 생성을 지시할 수 있다.
- [ ] POC 범위가 커질 때 어떤 기능을 뒤로 미룰지 판단할 수 있다.

#### 예상 시간 배분

- 개념 학습: 60분
- 실습 1: 90분
- 실습 2: 90분
- 실습 3: 90분
- 문서화/WorkLog: 90분
- **합계**: 6h

#### 참조 자료

- [[2026-04-05 Vibe Guiding 구현 계획]]: Phase 1-3 구현 구조
- [[2026-04-09 - Proposal - Vibe Guiding Architecture for Gobi]]: 통합 컨텍스트 폴더와 Vibe Guiding 엔진
- `Topics/GOBI-Guiding/current_system_context.json`: 사용자 상태 수집 예시
- `Topics/GOBI-Guiding/vibe_guiding_status_collector.py`: Context Collector 초기 구현 참고

### M3 - Vibe Manual과 CVL 설계

**난이도**: ⭐⭐  
**예상 시간**: 7h  
**산출물 폴더**: `03-Vibe-Manual-CVL/`

#### 학습 목표

- [ ] AI가 검색하고 조합하기 쉬운 Vibe Manual 스키마를 설계할 수 있다.
- [ ] GOBI 기능 문서를 goal, prerequisites, steps, completion_signal, known_failures로 구조화할 수 있다.
- [ ] 코드/스펙/doc 변경이 매뉴얼 업데이트를 요구하는 조건을 정의할 수 있다.
- [ ] 파일 기반 Retrieval Index 초안을 만들 수 있다.

#### 주요 개념

1. **Vibe Manual**: 인간과 AI가 함께 사용할 수 있도록 구조화된 최신 매뉴얼이다.
2. **Atomic Guide Unit**: 하나의 목표, 단계, 완료 신호, 실패 대응을 담는 최소 안내 단위다.
3. **Completion Signal**: 사용자가 작업을 제대로 끝냈는지 확인할 수 있는 관찰 가능한 신호다.
4. **Known Failure**: 사용자가 막히는 흔한 실패 상황과 우회 방법이다.
5. **CVL Update Rule**: 변경 사항이 매뉴얼 갱신을 요구하는지 판단하는 규칙이다.

#### 실습 과제

**실습 1: Vibe Manual Schema 작성** ⭐⭐
- **목적**: 문서가 단순 설명이 아니라 Guiding Engine의 입력이 되게 한다.
- **단계**:
  1. 사람이 읽는 Markdown 구조를 정의한다.
  2. AI가 읽는 metadata 필드를 정의한다.
  3. `goal`, `prerequisites`, `steps`, `completion_signal`, `known_failures`, `related_sources`를 필수 필드로 둔다.
- **예상 시간**: 120분
- **검증**: 샘플 매뉴얼 1개가 스키마에 맞게 작성된다.

**실습 2: Sample Manual 작성** ⭐⭐
- **목적**: GOBI 실제 사례를 스키마에 적용한다.
- **단계**:
  1. GOBI CLI 인증 또는 GOBI Desktop Custom Homepage/Applet 중 하나를 선택한다.
  2. 기존 문서와 테스트 기록에서 절차와 실패 지점을 뽑는다.
  3. `sample-manual/`에 매뉴얼을 작성한다.
- **예상 시간**: 150분
- **검증**: 매뉴얼에 초보/중급 사용자 분기와 fallback이 포함된다.

**실습 3: CVL Update Rules 작성** ⭐⭐
- **목적**: 어떤 변경이 매뉴얼 업데이트를 요구하는지 판단한다.
- **단계**:
  1. UI label 변경, CLI command 변경, config path 변경, error message 변경을 분류한다.
  2. 영향도 대/중/소 기준을 만든다.
  3. 변경 감지 후 WorkLog에 기록할 템플릿을 만든다.
- **예상 시간**: 90분
- **검증**: `cvl-update-rules.md`에 영향도 기준과 조치가 표로 정리된다.

#### 산출물

```
03-Vibe-Manual-CVL/
├── README.md
├── vibe-manual-schema.md
├── retrieval-metadata-design.md
├── cvl-update-rules.md
└── sample-manual/
    ├── gobi-cli-getting-started.md
    └── gobi-desktop-custom-homepage.md
```

#### Definition of Done

- [ ] Vibe Manual Schema 작성
- [ ] Retrieval Metadata 설계 작성
- [ ] Sample Manual 최소 1개 작성
- [ ] CVL Update Rules 작성
- [ ] `03-Vibe-Manual-CVL/README.md` 작성
- [ ] WorkLog 작성 및 Daily Retrospective 완료

#### Self-Assessment

**개념 이해**:
- [ ] 일반 매뉴얼과 Vibe Manual의 차이를 설명할 수 있다.
- [ ] Completion Signal이 왜 필요한지 설명할 수 있다.

**실무 활용**:
- [ ] GOBI 기능 하나를 Atomic Guide Unit으로 바꿀 수 있다.
- [ ] 변경 사항을 보고 CVL 영향도를 판단할 수 있다.

#### 예상 시간 배분

- 개념 학습: 60분
- 실습 1: 120분
- 실습 2: 150분
- 실습 3: 90분
- 문서화/WorkLog: 60분
- **합계**: 7h

#### 참조 자료

- [[2026-04-05 Vibe Guiding 구현 계획]]: Vibe Manual 설계 원칙과 CVL 연결
- [[2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]]: Known Failure와 품질 기준
- `Topics/GOBI-CLI/`: GOBI CLI 매뉴얼/실습 자료
- `Topics/Clearly-BRD-PRD/`: VibeLearn AI 산출물 구조 참고

### M4 - Guiding Engine POC 개발

**난이도**: ⭐⭐⭐  
**예상 시간**: 12h  
**산출물 폴더**: `04-Guiding-Engine-POC/`

#### 학습 목표

- [ ] Python으로 사용자 상태 수집기를 구현할 수 있다.
- [ ] JSON 기반 Trigger Rule을 설계하고 판정할 수 있다.
- [ ] 파일 기반 Retrieval Index에서 관련 매뉴얼을 선택할 수 있다.
- [ ] 사용자 수준과 상황에 맞는 `guide_response.md`를 생성할 수 있다.
- [ ] 최소 3개 테스트 케이스로 POC를 검증할 수 있다.

#### 주요 개념

1. **User Context**: OS, 도구 버전, GOBI 설정, 사용자 수준, 현재 문제 신호를 담는 상태 객체다.
2. **Problem Signal**: "명령어 없음", "설정 경로 불명확", "UI 메뉴를 찾지 못함" 같은 도움 요청 단서다.
3. **Trigger Rule**: Problem Signal과 User Context를 보고 안내 필요 여부를 판단하는 규칙이다.
4. **Retrieval Index**: Vibe Manual 문서와 metadata를 연결하는 파일 기반 색인이다.
5. **Guide Response**: 사용자가 바로 실행할 수 있는 단계별 안내 결과물이다.

#### 실습 과제

**실습 1: POC 파일 구조 생성** ⭐
- **목적**: 개발 실습을 시작할 최소 프로젝트 구조를 만든다.
- **단계**:
  1. `04-Guiding-Engine-POC/data`, `src`, `output`, `tests` 폴더를 만든다.
  2. `user_context.sample.json`, `trigger_rules.json`, `retrieval_index.json`을 만든다.
  3. `collect_context.py`, `evaluate_trigger.py`, `retrieve_manual.py`, `compose_guide.py` 파일을 만든다.
- **예상 시간**: 60분
- **검증**: 모든 파일이 생성되고 README에 실행 순서가 기록된다.

**실습 2: Context Collector 구현** ⭐⭐
- **목적**: 실제 사용자 환경 정보를 수집한다.
- **단계**:
  1. Windows OS 정보를 수집한다.
  2. Python/Node 버전을 수집한다.
  3. `.gobi/settings.yaml`의 주요 값을 읽는다.
  4. 결과를 `output/user_context.json`에 저장한다.
- **예상 시간**: 150분
- **검증**: `user_context.json`이 생성되고 기존 `current_system_context.json`과 비교 가능하다.

**실습 3: Trigger + Retrieval 구현** ⭐⭐⭐
- **목적**: 사용자가 막힌 상황에 맞는 매뉴얼을 선택한다.
- **단계**:
  1. `trigger_rules.json`에 5개 규칙을 작성한다.
  2. 문제 신호를 입력받아 matching rule을 찾는다.
  3. `retrieval_index.json`에서 관련 manual path를 선택한다.
  4. 선택 근거를 로그로 출력한다.
- **예상 시간**: 180분
- **검증**: 3개 problem signal에 대해 서로 다른 manual candidate가 선택된다.

**실습 4: Guide Composer 구현** ⭐⭐⭐
- **목적**: 검색된 매뉴얼을 사용자 맥락에 맞는 안내로 변환한다.
- **단계**:
  1. 초보/중급/고급 사용자 수준별 템플릿을 만든다.
  2. completion signal과 fallback을 반드시 포함한다.
  3. 결과를 `output/guide_response.md`로 저장한다.
  4. Quality Checklist를 통해 누락 항목을 검사한다.
- **예상 시간**: 210분
- **검증**: `guide_response.md`가 생성되고 단계, 완료 신호, fallback이 모두 포함된다.

#### 산출물

```
04-Guiding-Engine-POC/
├── README.md
├── data/
│   ├── user_context.sample.json
│   ├── trigger_rules.json
│   └── retrieval_index.json
├── src/
│   ├── collect_context.py
│   ├── evaluate_trigger.py
│   ├── retrieve_manual.py
│   └── compose_guide.py
├── output/
│   ├── user_context.json
│   └── guide_response.md
└── tests/
    └── test_scenarios.md
```

#### Definition of Done

- [ ] POC 폴더 구조 생성
- [ ] `collect_context.py` 실행 성공
- [ ] `trigger_rules.json` 기반 Trigger 판정 성공
- [ ] `retrieval_index.json` 기반 문서 선택 성공
- [ ] `guide_response.md` 자동 생성 성공
- [ ] 최소 3개 테스트 시나리오 통과
- [ ] `04-Guiding-Engine-POC/README.md` 작성
- [ ] WorkLog 작성 및 Daily Retrospective 완료

#### Self-Assessment

**개념 이해**:
- [ ] User Context, Trigger, Retrieval, Composer의 차이를 설명할 수 있다.
- [ ] 파일 기반 POC가 앱 통합 전에 왜 필요한지 설명할 수 있다.

**실무 활용**:
- [ ] AI에게 Context Collector 구현을 정확히 지시할 수 있다.
- [ ] Trigger Rule이 잘못 작동할 때 디버깅 방향을 제시할 수 있다.

**문제 해결**:
- [ ] 매뉴얼 검색 실패 시 fallback을 설계할 수 있다.

#### 예상 시간 배분

- 개념 학습: 90분
- 실습 1: 60분
- 실습 2: 150분
- 실습 3: 180분
- 실습 4: 210분
- 테스트/문서화/WorkLog: 90분
- **합계**: 12h

#### 참조 자료

- `Topics/GOBI-Guiding/current_system_context.json`: 수집 결과 예시
- `Topics/GOBI-Guiding/vibe_guiding_status_collector.py`: 기존 수집기 참고
- [[2026-04-09 - Proposal - Vibe Guiding Architecture for Gobi]]: Trigger/Retrieval/Compose 흐름
- [[2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]]: Trigger 후보와 품질 기준

### M5 - GOBI 시나리오 검증

**난이도**: ⭐⭐⭐  
**예상 시간**: 7h  
**산출물 폴더**: `05-GOBI-Scenario-Tests/`

#### 학습 목표

- [ ] 실제 GOBI 사용 상황을 POC 테스트 시나리오로 바꿀 수 있다.
- [ ] 입력 user_context와 problem_signal을 정의할 수 있다.
- [ ] 생성된 guide_response의 품질을 평가할 수 있다.
- [ ] 실패한 안내를 Vibe Manual, Trigger Rule, Retrieval Index 중 어디에서 고쳐야 하는지 분류할 수 있다.

#### 주요 개념

1. **Scenario Test**: 실제 사용자 막힘 상황을 재현 가능한 입력/출력 테스트로 바꾼 것이다.
2. **Expected Guide**: 특정 상황에서 최소한 포함되어야 하는 안내 기준이다.
3. **Guide Quality Checklist**: 할루시네이션, 완료 신호, fallback, 사용자 수준 반영을 검사하는 기준이다.
4. **Failure Classification**: 실패 원인을 manual, trigger, retrieval, compose 중 하나로 분류하는 과정이다.

#### 실습 과제

**실습 1: GOBI Desktop Custom Homepage/Applet 시나리오 작성** ⭐⭐
- **목적**: 기존 실패 테스트를 POC 입력으로 바꾼다.
- **단계**:
  1. [[2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]]에서 실패 지점을 뽑는다.
  2. `user_context`와 `problem_signal`을 작성한다.
  3. 기대 guide 기준을 만든다.
- **예상 시간**: 90분
- **검증**: 테스트 파일에 입력, 기대 출력, 평가 기준이 모두 있다.

**실습 2: GOBI CLI 인증/Space 연결 시나리오 작성** ⭐⭐
- **목적**: CLI 기반으로 재현 가능한 테스트를 만든다.
- **단계**:
  1. `Topics/GOBI-CLI/`의 설치/인증/Space 관련 문서를 읽는다.
  2. 사용자가 `gobi` 명령을 찾지 못하는 상황을 만든다.
  3. POC를 실행해 guide response를 생성한다.
- **예상 시간**: 120분
- **검증**: guide response가 CLI 설치 확인, 인증 상태 확인, fallback을 포함한다.

**실습 3: Version/Environment Mismatch 시나리오 작성** ⭐⭐⭐
- **목적**: 사용자 환경 차이를 반영하는 안내를 검증한다.
- **단계**:
  1. Node/Python/GOBI 설정 값이 다른 상황을 만든다.
  2. Trigger Rule이 버전/환경 차이를 감지하는지 확인한다.
  3. guide response가 "먼저 확인할 정보"를 제시하는지 평가한다.
- **예상 시간**: 120분
- **검증**: 없는 메뉴나 확인되지 않은 정보를 단정하지 않는다.

#### 산출물

```
05-GOBI-Scenario-Tests/
├── README.md
├── guide-quality-checklist.md
├── scenario-gobi-desktop-custom-homepage.md
├── scenario-gobi-cli-auth.md
├── scenario-version-mismatch.md
└── test-results.md
```

#### Definition of Done

- [ ] GOBI Desktop 시나리오 작성 및 테스트
- [ ] GOBI CLI 시나리오 작성 및 테스트
- [ ] Version/Environment Mismatch 시나리오 작성 및 테스트
- [ ] Guide Quality Checklist 작성
- [ ] 실패 원인 분류표 작성
- [ ] `05-GOBI-Scenario-Tests/README.md` 작성
- [ ] WorkLog 작성 및 Daily Retrospective 완료

#### Self-Assessment

**개념 이해**:
- [ ] Scenario Test가 왜 Vibe Guiding 개발에 필요한지 설명할 수 있다.
- [ ] guide failure를 컴포넌트별로 분류할 수 있다.

**실무 활용**:
- [ ] 새로운 GOBI 사용 문제를 테스트 케이스로 바꿀 수 있다.
- [ ] 생성된 guide response를 품질 기준으로 평가할 수 있다.

#### 예상 시간 배분

- 개념 학습: 60분
- 실습 1: 90분
- 실습 2: 120분
- 실습 3: 120분
- 평가/문서화/WorkLog: 90분
- **합계**: 7h

#### 참조 자료

- [[2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]]: Desktop/Applet 테스트 근거
- `Topics/GOBI-CLI/01-Setup-Auth/`: CLI 설치와 인증 관련 자료
- `Topics/GOBI-CLI/03-Space-Thread/`: Space와 Thread 관련 자료
- [[2026-04-03 GOBI Vibe Guiding 시스템 맵]]: 제품군과 리포지토리 관계

### M6 - 통합 계획과 Demo Capstone

**난이도**: ⭐⭐  
**예상 시간**: 6h  
**산출물 폴더**: `06-Integration-Demo/`

#### 학습 목표

- [ ] VS Code POC 이후 GOBI Desktop/Applet/CLI 통합 후보를 비교할 수 있다.
- [ ] 5분 데모 플로우를 작성할 수 있다.
- [ ] MVP Backlog와 후속 고도화 Backlog를 분리할 수 있다.
- [ ] GOBI 팀 공유용 요약 문서를 작성할 수 있다.

#### 주요 개념

1. **Integration Option**: POC를 실제 사용 환경에 붙이는 방식이다.
2. **Demo Flow**: 문제 상황부터 안내 생성까지 보여주는 짧은 시연 흐름이다.
3. **MVP Backlog**: 지금 당장 제품 검증에 필요한 최소 기능 목록이다.
4. **Team Collaboration Note**: GOBI 팀과 논의할 결정 사항과 요청 사항이다.
5. **Capstone**: 전체 학습 결과를 하나의 작동 가능한 시연으로 통합하는 마지막 실습이다.

#### 실습 과제

**실습 1: 통합 후보 비교** ⭐⭐
- **목적**: 다음 개발 방향을 현실적으로 결정한다.
- **단계**:
  1. VS Code CLI, VS Code Extension, GOBI Desktop Applet, GOBI CLI command, docs companion guide를 비교한다.
  2. 구현 난이도, 사용자 가치, GOBI 팀 협업 필요도를 평가한다.
  3. 1차 통합 후보를 선택한다.
- **예상 시간**: 90분
- **검증**: `integration-options.md`에 선택 근거가 기록된다.

**실습 2: Demo Flow 작성** ⭐⭐
- **목적**: POC의 가치를 짧게 보여줄 수 있게 만든다.
- **단계**:
  1. 사용자가 막히는 상황을 하나 고른다.
  2. Context Collector 실행 장면을 정리한다.
  3. Trigger/Retrieval/Guide Response 생성 장면을 정리한다.
  4. 결과 평가와 feedback loop를 보여준다.
- **예상 시간**: 120분
- **검증**: 5분 안에 시연 가능한 순서와 파일 경로가 정리된다.

**실습 3: MVP Backlog 작성** ⭐⭐
- **목적**: 후속 개발을 실행 가능한 단위로 만든다.
- **단계**:
  1. Must/Should/Could로 기능을 분류한다.
  2. GOBI 팀 확인이 필요한 항목을 별도 표시한다.
  3. 다음 Topic 또는 다음 Sprint 후보를 정한다.
- **예상 시간**: 90분
- **검증**: `mvp-backlog.md`에 우선순위와 의존성이 기록된다.

#### 산출물

```
06-Integration-Demo/
├── README.md
├── integration-options.md
├── demo-flow.md
├── mvp-backlog.md
└── team-collaboration-notes.md
```

#### Definition of Done

- [ ] 통합 후보별 장단점 비교
- [ ] 1차 통합 후보 선택
- [ ] 5분 Demo Flow 작성
- [ ] MVP Backlog 작성
- [ ] GOBI 팀 공유용 요약 작성
- [ ] `06-Integration-Demo/README.md` 작성
- [ ] Final Retrospective 작성 준비

#### Self-Assessment

**개념 이해**:
- [ ] POC와 제품 통합의 차이를 설명할 수 있다.
- [ ] MVP와 후속 고도화 범위를 구분할 수 있다.

**실무 활용**:
- [ ] GOBI 팀에게 Vibe Guiding POC의 가치를 설명할 수 있다.
- [ ] 다음 개발 작업을 backlog item으로 쪼갤 수 있다.

#### 예상 시간 배분

- 개념 학습: 45분
- 실습 1: 90분
- 실습 2: 120분
- 실습 3: 90분
- 문서화/회고: 75분
- **합계**: 6h

#### 참조 자료

- [[2026-04-05 Vibe Guiding 구현 계획]]: 제품 통합과 협업 전략
- [[2026-04-09 - Proposal - Vibe Guiding Architecture for Gobi]]: Action 단계와 feedback loop
- [[2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]]: 데모 시나리오 후보

## WorkLog 작성 가이드

각 학습 세션마다 WorkLog를 작성하여 진행 상황을 추적한다.

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_Vibe-Guiding-VSCode.md`

**WorkLog 필수 섹션**:
1. 오늘의 학습 목표
2. 진행 내용
3. 문제 해결 로그
4. DoD 체크리스트
5. Daily Retrospective
6. 참조 및 산출물

## Retrospective 가이드

### Daily Retrospective

WorkLog 내에 5-10분 분량으로 작성한다.

- What went well?
- What could be improved?
- Insights
- Tomorrow's focus

### Module Retrospective

모듈 완료 시 `vl_worklog/YYYYMMDD_MX_Retrospective.md`에 작성한다.

- 계획 대비 실제 비교
- 핵심 학습 내용
- 발생한 문제와 해결
- Roadmap 정확도 평가
- 다음 모듈 준비사항

### Topic Retrospective

전체 Topic 완료 시 `vl_worklog/YYYYMMDD_Vibe-Guiding-VSCode_Final_Retrospective.md`에 작성한다.

- 전체 학습 여정 통계
- VibeLearn AI 방법론 효과성 평가
- 산출물 품질 평가
- 향후 학습 개선 사항

## 전체 폴더 구조

```
Vibe-Guiding-VSCode/
├── topic_info.md
├── vl_prompts/
│   ├── roadmap_prompt.md
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── 20260426_RoadMap_Vibe-Guiding-VSCode.md
├── vl_worklog/
│   ├── YYYYMMDD_M1_Vibe-Guiding-VSCode.md
│   └── ...
├── vl_materials/
├── 01-Vision-and-Architecture/
├── 02-Architecture-Design/
├── 03-Vibe-Manual-CVL/
├── 04-Guiding-Engine-POC/
├── 05-GOBI-Scenario-Tests/
└── 06-Integration-Demo/
```

## 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | 2026-05-03 | 2026-05-03 | 완료 | 100% | POC 대상: GOBI CLI |
| M2 | 2026-05-10 | 2026-05-10 | 완료 | 100% | GOBI CLI v2.0.12 기준 Two-Component Architecture 정리 |
| M3 | 2026-05-10 | 2026-05-10 | 완료 | 100% | Vibe Manual Schema, Retrieval Metadata, CVL Rules, Sample Manual 작성 |
| M4 | 2026-05-10 | 2026-05-10 | 완료 | 100% | 파일 기반 Guiding Engine POC, 3개 시나리오 통과 |
| M5 | 2026-05-10 | 2026-05-10 | 완료 | 100% | 5개 GOBI 시나리오 검증, guide quality checklist, 실패 원인 분류 |
| M6 | | | 대기 | 0% | Capstone Demo 준비 |

**범례**:
- 대기
- 진행 중
- 완료

## 성공 기준

- [ ] 모든 모듈 완료
- [ ] 최소 6개 산출물 폴더 생성
- [ ] `vl_prompts/roadmap_prompt.md`와 `vl_prompts/daily_learning_prompt.md`를 사용한 학습 사이클 유지
- [ ] VS Code에서 실행 가능한 Guiding Engine POC 완성
- [ ] 최소 3개 GOBI 시나리오에서 `guide_response.md` 생성
- [ ] Topic Retrospective 작성
- [ ] Self-Assessment 평균 4점 이상

## 다음 Daily Learning 시작 정보

다음 세션은 `vl_prompts/daily_learning_prompt.md`를 사용해 시작한다.

```
Topic 이름: Vibe-Guiding-VSCode
Topic 폴더 경로: C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\Vibe-Guiding-VSCode\
Roadmap 파일 경로: vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode.md
현재 진행 중인 모듈: M6 - 통합 계획과 Demo Capstone
가장 최근 WorkLog 파일: vl_worklog/20260510_M5_Vibe-Guiding-VSCode.md
이전 세션의 Tomorrow's focus: M6 시작. `06-Integration-Demo/` 폴더를 만들고 통합 후보 비교, 5분 demo flow, MVP backlog, GOBI 팀 협업 노트를 작성한다.
사용 가능한 시간: 사용자가 세션 시작 시 입력
```

**생성자**: Codex with VibeLearn AI  
**Roadmap 버전**: 1.0  
**방법론 버전**: VibeLearn AI 2.0
