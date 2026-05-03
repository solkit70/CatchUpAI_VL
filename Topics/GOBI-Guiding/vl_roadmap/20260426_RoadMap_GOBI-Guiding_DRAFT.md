# Vibe Guiding 개발 로드맵 (Roadmap) - [DRAFT]

> **⚠️ 주의**: 본 로드맵은 방향성 확인용 드래프트 버전입니다.
> VibeLearn AI v2.0의 정식 프로세스(Template -> Prompt -> Final Roadmap)를 거치지 않았으므로, 다음 세션에서 정식 템플릿을 사용하여 고품질의 최종 로드맵을 다시 생성해야 합니다.


Vibe Guiding은 사용자의 작업 컨텍스트와 시스템 상태를 이해하여 실시간으로 최적의 가이드를 제공하는 초개인화 에이전트 시스템입니다.

## 🎯 핵심 비전
"사용자가 묻기 전에 필요를 파악하고, 실패했을 때 가장 빠른 우회로를 제시하는 인텔리전트 컴패니언"

---

## 📅 단계별 추진 계획

### Phase 1: 컨텍스트 마스터 (Context Mastery) - [현재 단계]
- **목표**: 에이전트가 사용자의 작업 환경을 100% 이해하게 함
- **핵심 기능**:
    - `.gobi/settings.yaml` 등 설정 파일 실시간 파싱 및 분석
    - OS 환경, 설치된 도구 버전 정보 수집 모듈 개발
    - 수집된 정보를 에이전트 시스템 프롬프트에 동적으로 주입 (Harness Engineering)

### Phase 2: 반응형 가이드 엔진 (Reactive Guidance)
- **목표**: 에러나 병목 현상 발생 시 즉각적인 해결책 제시
- **핵심 기능**:
    - 터미널 출력(stdout/stderr) 실시간 모니터링 및 패턴 분석
    - 실패 사례별 '우회 전략(Workaround) 데이터베이스' 구축
    - 에러 발생 시 자동으로 "이렇게 시도해 보세요" 제안 팝업/로그 출력

### Phase 3: 상태 기반 동적 매핑 (Dynamic Mapping)
- **목표**: 버전 변화 및 UI 변경에 강인한 가이드 제공
- **핵심 기능**:
    - 앱 버전별 기능 매핑 테이블 구축 (버튼 위치, 메뉴 명칭 등)
    - 사용자의 현재 상태에 맞춘 맞춤형 매뉴얼 렌더링
    - "이전 버전에는 여기 있었지만, 지금은 저기로 옮겨졌어요"와 같은 변화 대응 가이드

### Phase 4: 하이브리드 오케스트레이션 (Hybrid Orchestration)
- **목표**: 매체(텍스트/이미지/영상)를 넘나드는 입체적 가이드
- **핵심 기능**:
    - `openai-image-skill` 연동을 통한 즉석 설명 이미지 생성
    - `remotion-video` 연동을 통한 숏폼 가이드 영상 자동 제작
    - 에이전트 간 협업을 통한 종합 문제 해결 파이프라인 완성

---

## 🛠️ 참조 데이터 (References)
- **Technical Specs**: `[[Ingest/CatchUpAI_VL/Topics/GOBI-Specs-Pipeline/]]`
- **Business Needs**: `[[Ingest/CatchUpAI_VL/Topics/Clearly-BRD-PRD/]]`
- **Learning History**: `[[Ingest/CatchUpAI_VL/Topics/VibeLearn-AI/]]`

---
*VibeLearn AI 시스템에 의해 2026-04-26에 생성된 개발 로드맵입니다.*
