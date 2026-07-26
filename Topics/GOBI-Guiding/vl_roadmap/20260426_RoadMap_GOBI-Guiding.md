---
title: "Vibe Guiding 실전 개발 로드맵 (Roadmap)"
created: 2026-04-26 15:00:00
tags:
  - vibe-guiding
  - roadmap
  - gobi
  - vibe-learn
  - cvl
---

# Vibe Guiding 실전 개발 로드맵 (Roadmap)

> ⏸️ **상태: 중단 (2026-07-26 기준)** — GOBI Desktop 자체의 성능이 아직 이 작업을 진행할 수 있는
> 수준으로 성숙하지 않아 M1(2026-05-03) 이후 중단됐다. 실패나 포기가 아니라 **외부 플랫폼(GOBI
> Desktop) 성숙도에 막힌 대기 상태**다. GOBI Desktop 성능이 개선되면 재개 검토. 같은 "Vibe
> Guiding" 개념을 VS Code + Codex 조합으로 별도 진행 중인 작업은
> [[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode|Vibe-Guiding-VSCode]]
> 참고 — 그쪽은 계속 진행 중이며 이 Topic과는 별개다.

Vibe Guiding은 사용자의 작업 컨텍스트와 시스템 상태를 실시간으로 파악하여, **VibeLearn AI로 구축된 최신 지식 베이스**로부터 최적의 안내를 추출하여 제공하는 초개인화 에이전트 시스템입니다.

## 🎯 핵심 비전
"사용자가 묻기 전에 상황을 파악하고, 실패하기 전에 최신 매뉴얼 기반의 최적 우회로를 제시하는 자가 진화형 가이드 시스템"

---

## 🏗️ 이원화 아키텍처 (Two-Component Strategy)

본 프로젝트는 상호 보완적인 두 개의 핵심 컴포넌트로 구성됩니다.

### 컴포넌트 1: 지식 관리 및 유지보수 (VibeLearn AI & CVL)
*   **역할**: 가이드의 근거가 되는 '살아있는 지식 베이스' 구축.
*   **핵심 기술**: Vibe Learning 방법론을 통한 매뉴얼 생성 + CVL (Continuous Vibe Learning)을 통한 자동 업데이트.
*   **목표**: 소스코드 변경을 감지하여 항상 최신 상태의 AI 최적화 매뉴얼(Structured Context) 유지.

### 컴포넌트 2: 가이딩 엔진 (Vibe Guiding Engine)
*   **역할**: 유저의 환경을 감시하고 적시에 지식을 주입.
*   **핵심 기술**: Triggering 메커니즘 + 하네스 엔지니어링 (Harness Engineering).
*   **목표**: 유저의 OS, 버전, 숙련도를 파악하여 컴포넌트 1에서 필요한 정보를 실시간으로 추출/제공.

---

## 📅 단계별 추진 마일스톤 (Milestones)

### M1: Foundation & 지식 레이어 구축 (Component 1 중심)
*   **목표**: 가이드 대상 시스템에 대한 VibeLearn AI 환경 구축 및 CVL 가동.
*   **주요 과제**:
    *   GOBI 주요 리포지토리(CLI, Desktop, Space 등)에 대한 Vibe 학습 환경 세팅 (`[[2026-04-03 GOBI Vibe Guiding 시스템 맵]]` 참조).
    *   `GOBI-Specs-Pipeline` 분석을 통한 시스템별 핵심 로직 및 인터페이스 파악.
    *   Vibe Learning 프로세스를 통한 'AI 최적화 매뉴얼' 초안 생성.
    *   GitHub 연동을 통한 CVL 파이프라인 구축 (코드 변경 시 매뉴얼 자동 갱신).

### M2: 엔진 설계 및 트리거링 메커니즘 (Component 2 중심)
*   **목표**: "언제, 무엇을 가이드할 것인가"를 결정하는 지능형 엔진 설계.
*   **주요 과제**:
    *   **Triggering Logic**: 에러 발생, 특정 명령 지연 등 도움 필요 상황 감지 로직 개발.
    *   **Context Collector**: 사용자의 OS, 도구 버전, 설정값 등 환경 정보 실시간 수집 모듈 고도화.
    *   **Harness Engineering**: 수집된 환경 정보를 에이전트 프롬프트에 동적으로 주입하는 체계 구축.
    *   **참조**: `[[2026-04-09 - Proposal - Vibe Guiding Architecture for Gobi]]`

### M3: 실전 배포 및 자가 진화 테스트 (Integration)
*   **목표**: 실제 앱 환경에서 작동하는 Vibe Guiding POC 완성.
*   **주요 과제**:
    *   **Workaround DB**: 실제 발생한 기술적 난제(예: Node 버전 충돌)와 그 해결책(npx 우회)을 지식화하여 컴포넌트 1에 통합.
    *   **Dynamic Mapping**: 앱 UI 변경 시 매뉴얼과 실시간 매핑되는 가이드 기능 구현.
    *   **GOBI Applet 연동**: 음성 명령("I want to...")에 반응하여 단계별 가이딩 시연.

### M4: 하이브리드 오케스트레이션 및 고도화 (Optimization)
*   **목표**: 매체(텍스트/이미지/영상)를 넘나드는 입체적 가이드 완성.
*   **주요 과제**:
    *   `openai-image-skill` 연동: 필요 시 즉석 가이드 이미지 생성 제공.
    *   `remotion-video` 연동: 복잡한 절차에 대한 짧은 가이드 영상 자동 제작.
    *   **Self-Healing**: 가이드 결과에 대한 피드백을 받아 스스로 매뉴얼을 보완하는 루프 완성.

---

## 🛠️ 참조 문서 및 데이터 (References)

1.  **아이디어 원천**: `[[VibeGuiding_BrainDump]]` (철학 및 인사이트)
2.  **시스템 스펙**: `[[Ingest/CatchUpAI_VL/Topics/GOBI-Specs-Pipeline/]]` (상세 아키텍처 및 파이프라인)
3.  **학습 방법론**: `[[Ingest/CatchUpAI_VL/Topics/VibeLearn-AI/]]` (디자인 표준)
4.  **비즈니스 요건**: `[[Ingest/CatchUpAI_VL/Topics/Clearly-BRD-PRD/]]` (프로젝트 위상)
5.  **구현 가이드**: `[[2026-04-05 Vibe Guiding 구현 계획]]` (CVL 및 단계별 상세)

---
*VibeLearn AI 시스템에 의해 2026-04-26에 업데이트된 정식 로드맵입니다.*
