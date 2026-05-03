# WorkLog: Vibe Guiding 프로젝트 초기 설정 및 비전 수립

**Date**: 2026-04-26
**Module**: M0 (Preparation & Setup)
**Status**: 완료

## 📊 학습/개발 목표
- [x] VibeLearn AI v2.0 표준 폴더 구조 구축
- [x] Vibe Guiding 핵심 로드맵(Phase 1-4) 수립 (이원화 아키텍처 반영)
- [x] 사용자 상태 수집 엔진(Status Collector) 프로토타입 개발
- [x] 자가 진화형 SDLC 인사이트 문서화
- [x] VibeLearn AI 시스템 디자인 준수 여부 검증 완료

## 📝 활동 내용
- **시스템 구조화**: `vl_prompts`, `vl_roadmap`, `vl_worklog`, `vl_materials` 폴더 생성 및 기존 문서 재배치 준비.
- **비전 수립**: "사용자가 묻기 전에 상태를 파악하고 우회로를 제안하는 에이전트"로서의 Vibe Guiding 방향성 정의.
- **아키텍처 정립**: 컴포넌트 1(지식 관리/CVL)과 컴포넌트 2(가이딩 엔진/Triggering)로 구성된 이원화 전략을 로드맵에 명문화.
- **기술 실습**: Python을 이용해 현재 OS, Node.js 버전, GOBI 설정 파일을 파싱하는 초기 코드 구현.
- **인사이트 도출**: 고비 데스크탑 홈페이지 배포 과정에서의 트러블슈팅(npx 우회)을 통해 '기능의 부재를 메우는 AI의 창의성' 발견.
- **디자인 검증**: 로드맵과 산출물이 VibeLearn AI v2.0 표준(README.md, CLAUDE.md)을 준수하는지 교차 검증 수행.

## ✅ 완료한 작업
- [x] `GOBI-Guiding` 토픽 폴더 구조 생성
- [x] `20260426_RoadMap_GOBI-Guiding.md` 정식 버전 생성 (이원화 아키텍처 및 GOBI-Specs-Pipeline 반영)
- [x] `vibe_guiding_status_collector.py` 프로토타입 작성
- [x] `2026-04-25 Substack Draft - AI 시대의 자가 진화하는 SDLC.md` 작성
- [x] 시스템 표준 프로세스 검증 및 승인 완료

## ⚠️ 발생한 문제와 해결
- **문제**: Gobi Desktop 내장 파이썬과 시스템 파이썬 간의 라이브러리(Gemini) 충돌 발생.
- **해결**: 완벽한 해결 대신, '왜 안 되는지'에 대한 기술적 원인을 분석하고 이를 Vibe Guiding의 핵심 기능(환경 인지)으로 승화시킴.

## 💡 학습 포인트
- 소프트웨어는 완성형으로 출시되는 것이 아니라, 사용자의 시도와 AI의 보완을 통해 실시간으로 '자가 진화'할 수 있음을 체득함.

## 🚀 다음 세션 준비
- **정식 프로세스 이행**: 현재 로드맵은 드래프트이므로, 다음 세션에서 VibeLearn AI 정식 루프를 실행함.
- **Topic Starter 작성**: `topic_info.md` 파일을 템플릿 기반으로 생성.
- **프롬프트 생성**: 템플릿을 이용하여 `roadmap_prompt.md` 및 `daily_learning_prompt.md` 생성.
- **최종 로드맵 확정**: 정식 로드맵 프롬프트를 실행하여 고품질의 최종 로드맵을 다시 생성하고 저장.
- **Phase 1 고도화**: 수집된 정보를 시스템 프롬프트에 주입하는 Harness Engineering 구현.

---
*VibeLearn AI 시스템 디자인에 따라 작성된 워크로그입니다.*
