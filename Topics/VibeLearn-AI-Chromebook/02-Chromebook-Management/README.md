---
title: "M2 · 학교 지급 Chromebook의 관리 실체"
created: 2026-08-17 00:40:00
tags:
  - chromeos
  - device-management
  - module-readme
---

## 모듈 정보

**모듈**: M2 — 학교 지급 Chromebook의 관리 실체
**상태**: 🔄 진행 중 (세션 1/2 — 핵심 질문 1/4 답변)
**예상 학습 시간**: 8시간 (현재까지 약 1시간)
**난이도**: ⭐⭐

**학습 질문**: 학교가 나눠준 Chromebook에는 무엇이 설치·강제돼 있고, 교사는 그것을 어떻게 관리하는가?

## 핵심 질문 진행 상황

| | 질문 | 상태 |
|---|---|---|
| Q1 | 학교 지급 Chromebook에서 무엇이 가능하고 무엇이 차단되는가? 근거는? | ✅ **답변 완료** |
| Q2 | 교사는 학생 기기에 대해 실제로 무엇을 할 수 있는가? | ⏳ 세션 2 |
| Q3 | 신규 AI 도구가 학군 승인을 받으려면 어떤 관문을 거치는가? | ⏳ 세션 2 |
| Q4 | CIPA 법적 최소선과 실제 학군 감시 수준의 격차는? | ⏳ 세션 2 |

## 📚 학습 순서

1. [concepts/chromeos-runtimes.md](concepts/chromeos-runtimes.md) — ChromeOS 3개 런타임과 관리 정책이 각각을 어떻게 닫는가
2. [concepts/managed-device-capability-matrix.md](concepts/managed-device-capability-matrix.md) — **가부 판정표 24개 항목**. M3의 직접 입력

**다음 세션 예정**

3. `concepts/filtering-monitoring-vendors.md` — GoGuardian·Securly·Lightspeed 비교 (Q2·Q4)
4. `guides/teacher-control-surface.md` — 교사가 행사 가능한 통제 권한 (Q2)
5. `guides/district-tool-approval-process.md` — 도구 승인 절차 + 체크리스트 (Q3)
6. `troubleshooting/why-linux-is-unavailable.md` — 학생이 Crostini를 못 켜는 이유

## 세션 1에서 나온 핵심 발견

**1. Linux는 "꺼진" 게 아니라 "켜지지 않은" 것이다.** `VirtualMachinesAllowed` 정책의 기본값이 관리형 기기에서 **실행 불가**다. 관리자가 아무 조치를 하지 않아도 Linux는 안 된다. 학교에 요청할 때 "왜 껐나요"가 아니라 **"켜 주실 수 있나요"**가 맞는 접근이며, 대부분의 학군은 의도적 차단이 아니라 기본값 유지 상태다.

**2. Crostini를 켜려면 정책 3개를 조합해야 한다.** `VirtualMachinesAllowed`(기기) + `CrostiniAllowed`(사용자), 비제휴 사용자는 `DeviceUnaffiliatedCrostiniAllowed`까지. 관리자에게 "그냥 켜주세요"가 간단한 요청이 아니다.

**3. 확장 allowlist 등재가 유일한 배포 경로다.** `ExtensionInstallBlocklist`에 `*`를 넣으면 전체 차단이고, `ExtensionInstallForcelist`는 blocklist보다 우선하며 강제 설치 항목은 사용자가 제거할 수 없다. 학생이 임의 확장을 넣을 방법은 없지만, 학군이 채택하면 전체 배포가 된다.

**4. 개인 Gmail 로그인은 우회 수단이 아니다.** 기기 수준 정책은 "게스트나 개인 Gmail로 로그인해도" 그대로 적용된다.

**5. 살아남는 것은 넷뿐이다.** Chrome 브라우저·웹앱 / Google Drive / Workspace 내부 서비스 / allowlist 등재 확장. 개발 도구 계열은 전멸이며 **전부 Crostini 하나에 연쇄로 걸려 있다.**

**6. Admin Console 자체에 "사용자 활동 보고" 기능이 있다.** 별도 감시 제품 없이도 일정 수준의 가시성이 존재한다. Q4(CIPA 격차)를 다룰 때 벤더 제품이 그 위에 무엇을 더 얹는지를 봐야 한다.

## 후속 모듈로 넘기는 요구사항

| 대상 | 내용 |
|---|---|
| **M3** | 현재 VibeLearn AI의 의존성을 이 판정표에 1:1 대조. **A1(Crostini) 하나가 만드는 연쇄**를 차단 다이어그램의 중심에 둘 것 |
| **M3** | 기술적 차단(A1 — 관리자가 켜면 열림)과 정책적 차단(E2 Claude 18세 — 누구도 못 염)의 구분이 이 모듈의 핵심 |
| **M4** | 조건부(⚠️) 항목 중 **E4(Gemini 활성화 + 18세 미만 OU 차단), D2(외부 AI 도메인 차단), B5/B6(확장 allowlist)** 3개를 최우선 실측 |
| **M6** | IT 문서에 "확장 allowlist 등재 요청" 절차를 포함. 이것이 유일한 배포 경로 |

## ⚠️ 검증 한계

- **실물 Chromebook 미검증**이다. 판정표의 `추론` 근거 항목(B1~B4, B7, C1·C2·C4, D2·D4, E1)은 정책 문서로 직접 확인하지 않았다
- `chromeenterprise.google/policies/` 정책 페이지가 JavaScript 렌더링이라 직접 열람 실패. `admx.help` 미러는 조사 시점 다운(HTTP 522). 정책 기본값은 **원문을 인용한 검색 결과**로 확인했으며 페이지 직접 대조는 미완료
- M6 IT 문서 작성 전 정책 원문 재확인 필요

## 이전 / 다음

- **이전**: [../01-US-AI-Education-Policy/README.md](../01-US-AI-Education-Policy/README.md)
- **다음**: `03-Gap-Analysis/` (M2 완료 후)
- **Roadmap**: [../vl_roadmap/20260816_RoadMap_VibeLearn-AI-Chromebook.md](../vl_roadmap/20260816_RoadMap_VibeLearn-AI-Chromebook.md)
