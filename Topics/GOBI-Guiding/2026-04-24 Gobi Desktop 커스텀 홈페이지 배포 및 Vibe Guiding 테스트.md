---
title: "2026-04-24 Gobi Desktop 커스텀 홈페이지 배포 및 Vibe Guiding 테스트"
created: 2026-04-24 10:00:00
tags:
  - vibe-guiding
  - gobi-desktop
  - test-report
  - applet
  - cvl
---

## 1. 테스트 개요

*   **일시**: 2026-04-24
*   **테스트 대상**: Gobi Desktop 커스텀 홈페이지(Applet) 배포 프로세스
*   **사용 방법론**: VibeLearn AI - CVL (Continuous Vibe Learning) 프로세스
*   **목표**:
    1. 최신화된 GOBI CLI 매뉴얼(CVL 적용 버전)을 바탕으로 실제 배포를 완수할 수 있는지 검증
    2. 지난번 실패했던 홈페이지 적용 이슈를 해결하고 실시간 라이브 방송 중 배포 성공 여부 확인

## 2. 테스트 과정 및 조치 사항

### 🛠️ 시도 및 트러블슈팅
1.  **CLI 환경 복구**: 로컬의 `better-sqlite3` 모듈 충돌 문제를 해결하기 위해 `npm install -g @gobi-ai/cli` 재설치 시도.
2.  **버전 우회 (Bypass)**: 재설치 후에도 Node.js 버전 불일치(20 vs 22)가 지속되어, `npx @gobi-ai/cli sync` 명령어를 통해 최신 바이너리를 직접 호출하는 방식으로 배포 성공.
3.  **설정 자동화**: 고비 앱 UI 내에서 설정 메뉴를 찾는 대신, `.gobi/settings.yaml` 파일에 `homepagePath: app/home.html` 속성을 직접 추가하여 동기화하는 로우 레벨 접근 방식 선택.

## 3. 테스트 결과 분석

### ✅ 성공 사례 (Success)
*   **VibeLearn AI 시스템 활용 성공**: Gobi Desktop 앱 환경 내에서 VibeLearn AI 학습 시스템을 가동하고 지시를 수행하는 데 성공함.
*   **CVL 프로세스 실전 적용 성공**: Continuous Vibe Learning(CVL) 프로세스를 적용하여, 한 달 전 학습했던 GOBI CLI의 변경 사항을 분석하고 기존 학습 산출물(Quick Reference 등)을 최신화하는 데 성공함.
*   **파일 배포 기술적 돌파**: 이전 작업에서 실패했던 커스텀 홈페이지(`home.html`)의 서버 업로드 과정을 `npx` 우회 전략을 통해 완수함.
*   **Vibe Guiding 유효성**: AI가 제안한 CVL 기반의 매뉴얼 최신화와 배포 전략이 실제 문제 해결로 이어지는 과정을 확인하여 가이딩 시스템의 잠재력을 입증함.

### ⚠️ 잔존 이슈 (Blockers)
*   **설정 미반영**: 파일은 업로드되었으나, 서버의 보관함 메타데이터가 `homepagePath`를 즉시 인식하지 못해 웹 브라우저에서는 여전히 디폴트 화면이 노출됨.
*   **Vibe Guiding 통찰**: AI가 설정 파일 수정을 가이드하더라도, 서버 측의 '변경 감지 트리거'가 작동하지 않으면 사용자는 최종 결과물을 볼 수 없는 '배포 단절' 현상을 겪게 됨.

## 4. 향후 보완 포인트 (개발팀 전달용)

1.  **Metadata Auto-Refresh**: `.gobi/settings.yaml` 파일이 `sync` 명령어로 업로드될 때, 서버가 이를 감지하여 보관함의 메타데이터(홈페이지 경로 등)를 자동으로 갱신하는 로직 필요.
2.  **CLI Compatibility**: 윈도우 환경에서의 Node.js 버전 파편화에 따른 `better-sqlite3` 바이너리 호환성 문제 해결 또는 `npx` 기반의 안정적인 실행 가이드 공식화.
3.  **Vibe Guiding 로직**: 배포 성공 후 "실제 반영까지 최대 N분이 소요될 수 있다"는 안내나, 반영 여부를 AI가 실시간으로 체크하여 알려주는 '피드백 루프' 강화.

---
**관련 리포트**:
*   [Issue Report: Custom Homepage (Applet) Deployment Failure] (작성 완료)
*   [[2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]]
