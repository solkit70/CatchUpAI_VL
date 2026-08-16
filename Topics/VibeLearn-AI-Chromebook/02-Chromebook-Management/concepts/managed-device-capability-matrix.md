---
title: "관리형 Chromebook 가부 판정표"
created: 2026-08-17 00:15:00
tags:
  - chromeos
  - device-management
  - capability-matrix
---

## 이 문서의 용도

학교 지급 Chromebook에서 **무엇이 되고 무엇이 안 되는지**를 근거와 함께 판정한 표다. M3(갭 분석)에서 현재 VibeLearn AI의 의존성을 하나씩 이 표에 대조해 판정한다.

**조사 시점**: 2026-08-17
**판정 기호**: ✅ 가능 · ⚠️ 조건부 · ❌ 불가

**근거 유형**
- `정책` — Chrome Enterprise 정책 문서 또는 Google 관리자 지원 문서
- `M1` — M1 모듈에서 확인한 법률·정책·연령 제약
- `추론` — 위 둘에서 논리적으로 도출. **직접 확인 필요**

## A. 실행 환경

| # | 행위 | 판정 | 근거 | 비고 |
|---|---|---|---|---|
| A1 | Linux 터미널 실행 (Crostini) | ❌ | `정책` | 관리형 기기에서 `VirtualMachinesAllowed` 미설정 시 VM 실행 불가가 **기본값**. 학생 권한으로 변경 불가 |
| A2 | 가상머신 실행 | ❌ | `정책` | 위와 동일 |
| A3 | Linux를 관리자가 켜 준 경우 | ⚠️ | `정책` | `VirtualMachinesAllowed` + `CrostiniAllowed` 둘 다 Enabled 필요. 비제휴 사용자는 `DeviceUnaffiliatedCrostiniAllowed`까지 3개 |
| A4 | Android 앱 설치 (Play Store) | ⚠️ | `정책` | 관리자 정책으로 제어. 학군마다 다름 |
| A5 | Android 앱 사이드로드 | ⚠️ | `정책` | 별도 정책 항목으로 존재. 교육 환경에서는 대개 차단 |
| A6 | 웹앱·PWA 사용 | ✅ | `정책` | Chrome 런타임은 항상 살아 있음. 단 URL 필터링 적용 |

## B. 개발 도구

| # | 행위 | 판정 | 근거 | 비고 |
|---|---|---|---|---|
| B1 | `git clone` / 로컬 저장소 | ❌ | `추론` | git 실행에 Crostini 필요 (A1). 웹 기반 git 클라이언트는 별개 |
| B2 | Node.js / npm 실행 | ❌ | `추론` | A1에 종속 |
| B3 | Python 실행 | ❌ | `추론` | A1에 종속 |
| B4 | 데스크톱 VS Code 설치 | ❌ | `추론` | A1에 종속. ChromeOS용 네이티브 빌드는 Linux 환경 요구 |
| B5 | **Chrome 확장 프로그램 설치** | ❌ | `정책` | Chrome Web Store를 "Block all, admin manages allowlist"로 설정 가능. `ExtensionInstallBlocklist`에 `*` 지정 시 전체 차단 |
| B6 | 관리자가 allowlist에 넣은 확장 | ✅ | `정책` | `ExtensionInstallForcelist`는 blocklist보다 우선. **강제 설치 항목은 사용자가 제거 불가** |
| B7 | localhost 개발 서버 실행 | ❌ | `추론` | A1에 종속 |

> **B5·B6이 이 프로젝트의 결정적 지점이다.** 학생이 Claude Code나 임의의 개발 도구 확장을 설치할 방법은 없다. 반대로 학군이 채택을 결정하면 강제 설치로 전체 배포가 가능하다. **allowlist 등재가 유일한 경로**이며, 이것이 M6 IT 관리자 문서가 승인 심사 자료여야 하는 이유다.

## C. 파일

| # | 행위 | 판정 | 근거 | 비고 |
|---|---|---|---|---|
| C1 | 다운로드 폴더 읽기·쓰기 | ✅ | `추론` | ChromeOS 기본 파일 앱. 단 로컬 저장은 기기 초기화 시 소실 |
| C2 | 앱이 로컬 파일을 지속적으로 읽기 | ❌ | `추론` | 웹앱은 File System Access API 권한이 세션 단위. CLI처럼 작업 디렉터리를 상시 읽는 모델 불가 |
| C3 | USB 외부 저장장치 사용 | ⚠️ | `정책` | Admin Console에 **USB 기기 접근** 정책 존재. 교육 환경에서 흔히 차단 |
| C4 | Google Drive 읽기·쓰기 | ✅ | `추론` | Workspace for Education 기본 제공. **학생 트랙의 파일 기반이 될 곳** |
| C5 | 기기 초기화(powerwash) | ⚠️ | `정책` | Admin Console에서 powerwash 제어 및 강제 재등록 정책 |

## D. 네트워크

| # | 행위 | 판정 | 근거 | 비고 |
|---|---|---|---|---|
| D1 | 임의 웹사이트 접근 | ⚠️ | `M1` | CIPA에 따라 음란·아동포르노·유해 **이미지** 필터링 의무. 실제 차단 범위는 학군 선택 |
| D2 | 외부 AI 서비스 접근 (claude.ai 등) | ⚠️ | `M1`+`추론` | 학군 AI Tool Inventory 미등재 시 차단이 일반적 |
| D3 | 교사·성인의 필터링 해제 | ⚠️ | `M1` | CIPA 원문: 권한 있는 자는 **성인**의 정당한 연구·합법 목적 사용 시 필터를 해제할 수 있음 |
| D4 | Google Workspace 내부 서비스 | ✅ | `추론` | 학교가 이미 승인·배포한 범위 |

## E. 계정·인증

| # | 행위 | 판정 | 근거 | 비고 |
|---|---|---|---|---|
| E1 | 개인 Google 계정으로 로그인 | ⚠️ | `정책` | 가능하더라도 **기기 정책은 그대로 적용된다**("게스트나 개인 Gmail로 로그인해도 적용"). 우회 수단 아님 |
| E2 | Claude 계정 생성·사용 (18세 미만) | ❌ | `M1` | 부모 동의로도 예외 없음. 기술이 아니라 계약·정책 차단 |
| E3 | ChatGPT 사용 (13-17세) | ⚠️ | `M1` | 부모 동의 필요 + 학군 승인 필요 |
| E4 | Gemini in Classroom (K-12 전 연령) | ⚠️ | `M1` | 2026-08-10부터 전 연령. 단 **관리자가 활성화**했고 18세 미만 OU를 별도 차단하지 않았을 때만 |
| E5 | Gemini Gems 사용 | ⚠️ | `M1` | 유료 Workspace for Education 등급 + 관리자의 Gems 공유 허용 필요 |

## F. 클라우드 대안 (브라우저 내 개발 환경)

| # | 행위 | 판정 | 근거 | 비고 |
|---|---|---|---|---|
| F1 | GitHub Codespaces (브라우저 VS Code) | ⚠️ | `M1`+`추론` | 기술적으로는 브라우저만으로 동작. **GitHub 계정 필요**(연령·학군 승인 문제) + 도메인 차단 여부 |
| F2 | claude.ai/code (Claude Code on the web) | ❌(학생) / ⚠️(교사) | `M1` | 18세 미만 불가. 성인도 Pro/Max 구독 + GitHub 연결 필요 |
| F3 | Firebase Studio | ❌ | `M1` | 2026-06-22부로 신규 가입 중단, 2027-03-22 종료 |

## 판정 요약 — 무엇이 살아남는가

관리형 Chromebook에서 **확실히 살아 있는 것은 다음 넷뿐이다.**

1. **Chrome 브라우저와 웹앱** (A6)
2. **Google Drive 파일 읽기·쓰기** (C4)
3. **Google Workspace 내부 서비스** (D4)
4. **관리자가 allowlist에 올린 확장** (B6) — 단 등재가 전제

나머지는 전부 조건부이거나 불가다. 특히 **개발 도구 계열(B1~B4, B7)은 전멸**이며, 그 원인은 전부 A1 하나(Crostini 비활성)로 수렴한다.

> **M3 갭 분석에 넘길 핵심 관찰**: 현재 VibeLearn AI가 무너지는 지점은 여러 개처럼 보이지만 실은 **A1 하나가 연쇄를 일으킨 것**이다. Crostini가 닫히면 git·Node·Python·VS Code·localhost가 한꺼번에 사라진다. 그러나 A1은 **기술적 차단**이라 관리자가 켜면 열린다. 반면 E2(Claude 18세 미만 불가)는 **정책적 차단**이라 누구도 열 수 없다. 이 둘을 구분하는 것이 M3의 핵심이다.

## 조건부(⚠️) 항목의 확인 방법

⚠️ 항목은 학군마다 다르므로 실제 확인이 필요하다. 확인 경로는 [../../01-US-AI-Education-Policy/guides/how-to-check-district-policy.md](../../01-US-AI-Education-Policy/guides/how-to-check-district-policy.md)의 "기술 환경" 체크리스트를 쓴다.

가장 먼저 확인해야 할 3개는 이것이다.

1. **E4 — Gemini in Classroom 활성화 + 18세 미만 OU 차단 여부** (학생 트랙 전체가 여기 걸림)
2. **D2 — 외부 AI 서비스 도메인 차단 여부**
3. **B5/B6 — 확장 allowlist 정책과 등재 절차**

## ⚠️ 이 표의 한계

- **`추론` 근거 항목(B1~B4, B7, C1·C2·C4, D2·D4, E1)은 정책 문서로 직접 확인하지 않았다.** ChromeOS 구조상 자명해 보이는 것들이지만, 실기기 검증 전까지는 가설이다
- **실물 Chromebook 미검증 상태다.** M4 시작 전까지 실기기 또는 협조 교사를 확보해 이 표를 검증해야 한다
- 정책 페이지가 JS 렌더링이라 직접 대조하지 못한 항목이 있다 ([chromeos-runtimes.md](chromeos-runtimes.md) 하단 참조)

## 다음 문서

- [chromeos-runtimes.md](chromeos-runtimes.md) — 이 판정의 구조적 배경
- `filtering-monitoring-vendors.md` — 필터링 3사 비교 (다음 세션)
- `../guides/teacher-control-surface.md` — 교사 통제 권한 (다음 세션)
