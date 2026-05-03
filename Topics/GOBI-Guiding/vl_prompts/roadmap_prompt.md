# VibeLearn AI Roadmap 생성 프롬프트 — GOBI-Guiding Topic

**버전**: 2.0
**생성일**: 2026-04-26
**방법론**: VibeLearn AI

---

## [1단계] Topic 정보 (주입됨)

### 기본 정보

**Topic 이름**: `GOBI-Guiding`

**Topic 설명**:
```
GOBI 에코시스템(Desktop, Space, CLI 등)에 Vibe Guiding 방법론을 적용하여,
사용자의 작업 컨텍스트와 시스템 상태를 실시간으로 이해하고
최적의 가이드를 제공하는 초개인화 AI 안내 시스템을 개발하는 프로젝트
```

**학습 및 개발 목적**:
```
1. Vibe Guiding의 핵심 철학(Build the Brain -> Activate the Brain)을 제품으로 구현한다.
2. GOBI 제품별 AI-optimized Vibe Manual을 구축하고 이를 가이딩 엔진의 인풋으로 활용한다.
3. 사용자의 OS, 도구 버전, 설정을 실시간 수집하는 Harness Engineering을 구현한다.
4. 실패 상황에서 즉각적인 우회로(Workaround)를 제안하는 지능형 피드백 루프를 만든다.
```

**예상 학습 기간**: `M1-M4 단계를 거쳐 완성 (약 4-8주)`

---

### 환경 및 사전 지식

**운영 체제**: `Windows 11 / macOS`

**주요 도구**:
```
- GOBI Desktop / GOBI Space / GOBI CLI
- VS Code + Claude Code (Main Development)
- Python (Status Collection & Logic)
- VibeLearn AI 학습 시스템
- Remotion (가이드 영상 제작용)
```

**사전 지식**:
```
필수:
- VibeLearn AI 방법론 숙지
- GOBI CLI 및 설정 구조 이해
- Python 기초 및 JSON 데이터 처리
```

---

### 산출물 및 참조

**학습 및 개발 목표**:
```
- [ ] Vibe Guiding 4단계 로드맵(Context -> Reactive -> Dynamic -> Hybrid) 수립
- [ ] GOBI 제품군(Desktop, CLI, Space)에 대한 Vibe Manual 설계 및 작성
- [ ] 사용자 상태 수집 엔진(Status Collector) 프로토타입 고도화
- [ ] 수집된 컨텍스트를 시스템 프롬프트에 동적으로 주입하는 Harness 레이어 구현
- [ ] GOBI Applet을 통한 실시간 음성 가이딩 데모 완성
```

**참조 자료**:
```
- 핵심 전략: [[2026-04-03 GOBI Vibe Guiding 시스템 맵]], [[2026-04-05 Vibe Guiding 구현 계획]]
- 인사이트: [[2026-04-25 Substack Draft - AI 시대의 자가 진화하는 SDLC]]
- 테스트 이력: [[2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]], [[2026-04-24 Gobi Desktop 커스텀 홈페이지 배포 및 Vibe Guiding 테스트]]
```

---

## [2단계] AI에게 요청할 작업

위 Topic 정보를 바탕으로 VibeLearn AI 방법론에 맞는 학습 및 개발 로드맵을 생성해주세요.
로드맵은 다음 모듈 구조를 따라야 합니다:

1. **M1: Foundation & Alignment** (철학 이해 및 제품 분석)
2. **M2: Knowledge Engineering** (Vibe Manual 설계 및 작성)
3. **M3: Engine Development** (Harness 레이어 및 가이딩 엔진 구현)
4. **M4: Integration & Capstone** (제품 통합 및 데모 완성)

로드맵은 `vl_roadmap/20260426_RoadMap_GOBI-Guiding.md`에 저장하세요.
특히 실제 발생했던 에러 사례(Node 버전 충돌, 설정 미반영 등)를 어떻게 가이딩 데이터로 전환할지에 대한 실전적인 단계를 포함해주세요.
