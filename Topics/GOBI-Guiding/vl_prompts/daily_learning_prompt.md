# VibeLearn AI 일일 학습/개발 계획 생성 프롬프트 — GOBI-Guiding

**버전**: 2.0
**생성일**: 2026-04-26
**방법론**: VibeLearn AI

---

## [1단계] 컨텍스트 주입

### 전체 로드맵 정보
로드맵 파일 `vl_roadmap/20260426_RoadMap_GOBI-Guiding.md`의 내용을 참조하세요.

### 현재 진행 상태
*   **현재 모듈**: `M0 (Setup & Vision)` 완료
*   **다음 목표**: `M1 (Foundation & Alignment)` 시작

### 학습 및 개발 목적
```
사용자의 OS, 도구 버전, 설정을 실시간 수집하여, 실패 상황에서 즉각적인 우회로(Workaround)를 제안하는
'Vibe Guiding' 시스템의 첫 번째 실전 레이어를 구축한다.
```

---

## [2단계] AI에게 요청할 작업

오늘의 학습 및 개발 세션을 위한 **Daily Plan**을 생성해주세요.
문서는 `vl_worklog/YYYYMMDD_DX_Session_Name.md` 형식으로 저장하세요.

오늘 작업에는 다음이 반드시 포함되어야 합니다:
1. **학습 세션**: GOBI CLI의 에러 메시지와 설정 구조를 다시 한번 분석하여 가이딩 트리거(Trigger) 식별.
2. **개발 실습**: `vibe_guiding_status_collector.py`에서 수집한 데이터를 AI 에이전트의 시스템 프롬프트에 자동으로 주입하는 **Harness 초기 로직** 작성.
3. **인사이트 도출**: 실습 중 발생한 기술적 문제(블로커)를 어떻게 가이딩 지식으로 변환할지 기록.

결과물은 VibeLearn AI v2.0의 워크로그 형식을 따라 작성해주세요.
