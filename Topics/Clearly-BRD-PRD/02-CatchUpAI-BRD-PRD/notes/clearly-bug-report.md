# Clearly App Bug Report

**보고자**: Changsoo Park
**앱 URL**: https://www.clearlyreqs.com/
**프로젝트**: Catch Up AI 2026 Homepage (Unified Mode)

---

## Session 1 Bugs (2026-02-08) — All Fixed

### Bug #1: BRD 문서 날짜 자동 생성 오류

**심각도**: Low
**상태**: ✅ Fixed (2026-02-14 확인)
**재현 경로**: Create Project → BRD Wizard 완료 → Generate BRD → View Document

**현상**:
- BRD Document Header의 Date가 `2023-11-20`으로 자동 생성됨
- 실제 프로젝트 생성일: 2026-02-08
- Project Details에서는 "Created 2/8/2026"으로 정확하게 표시됨

**기대 동작**:
- BRD Document Header의 Date가 실제 프로젝트 생성일과 일치해야 함

**수정 확인**: 2026-02-14 재테스트 시 Date가 `2026-02-15`로 정확하게 생성됨

---

### Bug #2: PRD Wizard 진행 중 세션 만료 (Session Timeout)

**심각도**: High
**상태**: ✅ Fixed (2026-02-14 확인)
**재현 경로**: BRD Approve → Start PRD Wizard → 질문 응답 중 → 갑자기 로그인 화면으로 이동

**현상**:
- PRD Wizard에서 두 번째 질문이 표시된 상태에서 답변을 작성하던 중 로그인 화면으로 강제 이동됨
- 첫 번째 질문에 대한 답변은 이미 제출한 상태였음
- Wizard 진행 중 별도의 세션 만료 경고 없이 바로 로그아웃됨

**기대 동작**:
- Wizard 진행 중에는 세션이 충분히 유지되어야 함 (최소 30분 이상)
- 세션 만료 전 경고 메시지를 표시하고, 작성 중인 답변이 유실되지 않도록 해야 함

**수정 확인**: 2026-02-14 재테스트 시 PRD Wizard 4개 질문 전체를 완료할 때까지 세션이 정상 유지됨

---

### Bug #3: 재로그인 후 프로젝트 목록 표시 불가

**심각도**: Critical
**상태**: ✅ Fixed (2026-02-14 확인) → 단, Bug #4로 재발 가능성 있음
**재현 경로**: 세션 만료로 로그아웃 → 재로그인 → 대시보드

**현상**:
- 재로그인 후 대시보드 상단 통계에는 "Total Projects: 2, Documents: 1"로 표시됨
- 그러나 "Your Projects" 섹션에는 "No projects yet"으로 표시됨
- 검색창에서 프로젝트명으로 검색해도 결과 없음
- 페이지 새로고침(F5)으로도 해결되지 않음
- **결과적으로 BRD가 승인된 프로젝트에 접근할 수 없어 PRD Wizard를 이어서 진행할 수 없음**

**기대 동작**:
- 재로그인 후 이전에 생성한 프로젝트가 정상적으로 목록에 표시되어야 함
- 프로젝트 데이터가 유지되어야 함

**영향**:
- BRD Wizard에서 약 30분간 작성한 답변과 생성된 BRD에 접근 불가
- PRD 생성 작업을 진행할 수 없음
- 프로젝트를 처음부터 다시 생성해야 할 수 있음

---

## Session 2 Bugs (2026-02-14) — New

### Bug #4: PRD Approve 후 대시보드에서 프로젝트 사라짐

**심각도**: Critical
**상태**: 🔴 Open
**재현 경로**: BRD 생성 → BRD Approve → PRD 생성 → PRD Approve → 대시보드로 이동

**현상**:
- 프로젝트 "Catch Up AI 2026 Homepage"를 생성하고 BRD/PRD를 모두 완료함
- PRD Approve 후 Project Progress가 67% (2/3 completed)로 정상 표시됨
- Current Phase: "Choose Output Tool" 화면까지 정상 진행
- 그러나 대시보드(Landing Page)로 돌아오면:
  - **Total Projects: 0** (방금 생성한 프로젝트가 카운트되지 않음)
  - **Completed: 0**
  - **Documents: 0** (BRD, PRD 2개 문서가 생성되었으나 카운트되지 않음)
  - **Completion Rate: 0%**
  - "Your Projects" 섹션에 "No projects yet" 표시
- Bug #3과 유사하지만, 이번에는 **통계 숫자도 0으로 표시**되는 점이 다름
  - Bug #3 (2/8): 통계는 "Total Projects: 2"로 표시되었으나 목록에 안 나옴
  - Bug #4 (2/14): 통계 자체가 모두 0으로 표시됨

**기대 동작**:
- 대시보드에 "Total Projects: 1", "Documents: 2" (BRD + PRD)로 표시되어야 함
- "Your Projects" 목록에 "Catch Up AI 2026 Homepage" 프로젝트가 67% 진행 상태로 표시되어야 함
- 프로젝트를 클릭하여 "Choose Output Tool" 단계를 이어서 진행할 수 있어야 함

**영향**:
- Project Progress 67%에서 남은 "Choose Output Tool" 단계를 진행할 수 없음
- 프로젝트를 처음부터 다시 생성해야 할 수 있음
- BRD와 PRD는 Markdown으로 로컬에 내보내기(Export) 완료하여 데이터 유실은 없음

**비고**:
- Bug #3의 수정이 완전하지 않은 것으로 보임
- 프로젝트 데이터가 데이터베이스에는 저장되지만 대시보드 UI에서 조회되지 않는 패턴이 반복됨

**Session 3 (2026-02-15) 재현 확인**:
- Bug #4 여전히 재현됨
- 이번 세션에서는 BRD → PRD → **Choose Output Tool(Claude Code)까지 전체 완료** 후 대시보드 확인
- 대시보드: Total Projects: 0, Documents: 0, Completion Rate: 0% — 이전과 동일한 현상
- Output Tool 생성까지 정상 진행되었으나, 대시보드에서는 프로젝트가 표시되지 않음
- 3회 연속 동일 패턴 재현 (Session 1: Bug #3, Session 2: Bug #4, Session 3: Bug #4 재현)
- **워크어라운드**: 대시보드로 돌아가지 않고 프로젝트 페이지 내에서 모든 단계를 완료한 후, 산출물은 Markdown Export로 로컬에 저장하여 데이터 유실을 방지

---

## 환경 정보

### Session 1 (2026-02-08)
- **OS**: Windows 11
- **Clearly 앱 모드**: Unified
- **계정**: Changsoo Park
- **발생 시각**: 약 오전 5:00-5:45 AM (PST)

### Session 2 (2026-02-14)
- **OS**: Windows 11
- **Clearly 앱 모드**: Unified
- **계정**: Changsoo Park
- **발생 시각**: 약 오후 6:00-6:30 PM (PST)

### Session 3 (2026-02-15)
- **OS**: Windows 11
- **Clearly 앱 모드**: Unified
- **계정**: Changsoo Park
- **발생 시각**: 약 오전 4:40-5:30 AM (PST)
- **진행 범위**: BRD → PRD → Choose Output Tool (Claude Code) — 전체 완료
- **Bug #4 재현**: 대시보드 복귀 시 프로젝트 0건 표시

---

## 요약

| # | Bug | 심각도 | 최초 보고 | 상태 |
|---|-----|--------|---------|------|
| 1 | BRD 날짜 자동 생성 오류 (2023-11-20) | Low | 2026-02-08 | ✅ Fixed |
| 2 | PRD Wizard 중 세션 만료 (경고 없음) | High | 2026-02-08 | ✅ Fixed |
| 3 | 재로그인 후 프로젝트 목록 접근 불가 (통계는 표시) | Critical | 2026-02-08 | ✅ Fixed |
| 4 | PRD Approve 후 대시보드에서 프로젝트 사라짐 (통계도 0) | Critical | 2026-02-14 | 🔴 Open |

**비고**: BRD와 PRD는 Markdown/PDF로 로컬에 내보내기 완료하여 문서 데이터의 유실은 없습니다. 그러나 Clearly 앱 내에서 "Choose Output Tool" 단계를 이어서 진행하는 것이 불가능한 상태입니다.
