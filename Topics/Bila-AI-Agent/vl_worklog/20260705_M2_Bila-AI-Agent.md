---
title: M2 WorkLog — 2026-07-05
module: M2 - 데이터 소스 연결 & Phase 1 구현
session: 1
date: 2026-07-05
tags:
  - bila-ai-agent
  - m2
  - worklog
---

# M2 WorkLog — 데이터 소스 연결 & Phase 1 구현

## 세션 정보

| 항목 | 내용 |
|------|------|
| 날짜 | 2026-07-05 (일) |
| 상황 | Live #17 방송 중 실험② 세션 |
| 모듈 | M2 - 데이터 소스 연결 & Phase 1 구현 |
| 예상 시간 | 4h (방송 중 20분 + 이후 추가) |
| 참조 로드맵 | `vl_roadmap/20260628_RoadMap_Bila-AI-Agent.md` |

## 오늘의 목표

- [x] M2 학습 세션 시작 (WorkLog 생성)
- [x] 실습1: GitHub 레포 연결 (`solkit70/builders-lounge-personal-notes`)
- [x] 실습1 검증: 연결 후 기록 참조 답변 확인 → ❌ 실패, 한계 발견 (아래 기록)
- [ ] 실습2: Google Drive 연결 (BL 회의록 폴더)
- [ ] 실습3: Phase 1 최종 10개 질문 테스트 (방송 후 이어서 가능)

---

## 실습1 기록: GitHub 레포 연결

### 연결 결과 (스크린샷 확인, 2026-07-05)

GobiSpace Changbal 스페이스 → Settings → Agents 탭에서 GitHub 연결 완료.

| 항목 | 확인 결과 |
|------|---------|
| 연결 계정 | solkit70 (User, connected by 박창수) |
| 연결 레포 | `solkit70/builders-lounge-personal-notes` |
| 브랜치 | main |
| 권한 | Read / Write 토글 ON |
| 상태 표시 | "Attached solkit70/builders-lounge-personal-notes" (녹색) |

M1 워크로그에서 예정했던 실습1 첫 단계(GitHub 레포 연결)가 완료됐다. Roadmap DoD 항목 "GitHub 레포 연결 완료 + 기록 참조 답변 확인" 중 연결 자체는 완료, 기록 참조 답변 확인은 다음 단계로 남는다.

### 연결 검증 테스트 결과 (2026-07-05, 실측)

**질문**: "김성수님 HebronGuide가 뭔가요?" — Chat 창과 Post(@mention) 두 경로 모두 테스트

**Chat 결과**: ❌ 실패 — "현재 창발(Changbal) 스페이스 내의 포스트나 기록에서 'HebronGuide'라는 이름이나 관련 내용을 찾을 수 없습니다"

**호출된 도구 (Chat 로그 실측)**:
```
mcp__agent_serve__get_space_members "changbal"
mcp__agent_serve__list_space_posts "50"
Grep "HebronGuide"
mcp__agent_serve__get_space_post "146756"
Grep "Hebron"
mcp__agent_serve__list_user_posts "13"
```

**Post(@mention) 결과**: ❌ 실패 — "현재 저희 스페이스 내 포스트에서 HebronGuide에 대한 구체적인 설명이나 정의를 찾을 수 없습니다"

### 🔍 핵심 발견 — GitHub 연결이 검색 도구에 반영되지 않음

호출된 도구 목록을 보면 전부 `get_space_members`, `list_space_posts`, `get_space_post`, `list_user_posts` — **Space 포스트/멤버 조회 도구뿐이고, GitHub 레포를 읽는 도구 호출이 단 한 번도 없다.** Settings 탭에 "Attached solkit70/builders-lounge-personal-notes"로 표시되어 있음에도, 실제 Q&A 검색 경로에는 연결되어 있지 않은 것으로 보인다.

**가설**: Settings 화면에는 GitHub 섹션 위에 별도로 "No vaults mounted yet — Mount one of your vaults to make it readable to the Space Agent"라는 섹션이 있었다. GitHub "Attached" 상태는 코드 읽기·PR 생성용 연결이고(UI 문구: "read your code and open pull requests for you"), Q&A 검색에 실제로 쓰이는 건 별도의 **Vault Mount** 기능일 가능성이 있다.

**다음 진단 단계**: Settings → Agents 탭 상단의 "Mount one of your vaults..." 버튼으로 Vault를 마운트한 뒤 동일 질문으로 재테스트.

이건 브라우저(Edge vs Chrome) 캐시 문제로 보기 어렵다 — 도구 호출 자체가 GitHub를 전혀 시도하지 않았기 때문에, 캐시가 아니라 연결 방식의 구조적 차이일 가능성이 높다. Chrome에서도 같은 결과가 나오는지 확인해 보고, 안 되면 Vault Mount 경로를 시도해 보는 게 좋겠다.

### 연결 전후 비교용 질문 (실습1 목적 + Rundown 방송 계획 반영)

M1 시점(데이터 미연결)과 지금(GitHub 연결 후) 같은 질문의 응답 품질 차이를 비교한다.

| # | 질문 | M1 시점 예상 응답 | 연결 후 확인할 점 |
|---|------|------------------|------------------|
| 1 | 김성수님 HebronGuide가 뭔가요? | "모른다"고 답하거나 일반론만 언급 | `ideas/2026-07-03 Sung Soo Kim - HebronGuide.md` 내용 기반 정확한 답변 여부 |
| 2 | Builders Lounge 멤버가 누가 있나요? | 포스트 기반 일반 소개만 가능 | README.md 멤버 목록(12명) 참조 여부 |
| 3 | 창발 발표 영상 링크가 뭔가요? | 답변 불가 | Rundown/Slack 기록 내 YouTube 링크 참조 여부 |

---

## 문제 해결 로그

### 이슈 1: GitHub 연결이 Q&A 검색에 반영되지 않음 (2026-07-05) — 원인 규명 + 해결

- **증상**: Settings에 GitHub 레포가 "Attached"로 표시되지만, Chat/Post 양쪽에서 레포 관련 질문("김성수님 HebronGuide가 뭔가요?")에 답하지 못함
- **근거**: 실제 호출된 도구가 `get_space_members`/`list_space_posts`/`get_space_post`/`list_user_posts`뿐이고 GitHub 레포 read 도구가 전혀 호출되지 않음
- **1차 가설**: GitHub "Attach"는 코드 읽기·PR 생성 용도이고, Q&A 검색에는 별도의 "Vault Mount" 기능이 필요할 가능성

**✅ 근본 원인 확인**: `@Bila AI 김성수님 HebronGuide가 뭔가요? 연결된 GitHub Repo 도 찾아 보세요`처럼 레포 참조를 명시적으로 지시하면 정상 답변함(정확한 정보, 파일 경로까지 인용). 즉 도구 자체는 작동하지만, **현재 적용된 시스템 프롬프트(v1)가 "볼트/드라이브 미연결"이라고 명시**하고 있어서 Agent가 명시적 지시 없이는 GitHub를 검색 대상으로 고려하지 않았던 것.

- **해결**: `system_prompt_BL_mention.md`, `system_prompt_BL_chat.md`를 v2로 업데이트 — 데이터 소스에 GitHub 레포(`solkit70/builders-lounge-personal-notes`)를 명시하고, 멤버/Product 질문 시 레포 우선 검색을 지시하는 문구 추가
- **상태**: 문서 수정 완료. **GobiSpace Settings → Agents에 v2 프롬프트 붙여넣기 필요** (사용자 실행 대기)

### 이슈 2: README.md에 링크가 없으면 subfolder 파일을 못 찾음 (2026-07-05) — 🚩 GOBI 요구사항 후보 (중요)

- **증상**: v2 프롬프트 적용 후 "Nate Cho님의 Job Search Co-pilot은 어떤 제품인가요?" 질문 — 힌트 없이 자동 참조 여부를 검증하려는 테스트. `ideas/2026-07-02 Nate Cho - Job Search Co-pilot.md` 파일이 레포에 실제로 존재하는데도 **처음에는 답변 실패**
- **조치**: README.md의 "주요 문서" 인덱스 표에 해당 파일 링크(`ideas/2026-07-02%20Nate%20Cho%20-%20Job%20Search%20Co-pilot.md`)를 추가
- **결과**: 링크 추가 후 재질문하니 **정상 답변** — 사용자 실측 확인
- **사용자 가설**: "README.md만 참조하거나, 혹은 README.md에 정보(링크)가 없으면 더 이상 subfolder를 탐색하지 않는 것 같다"

**분석**: 이슈 1(시스템 프롬프트가 "미연결"이라고 선언)과는 별개의 문제다. v2 프롬프트로 "ideas/, feedback/, builders/ 폴더도 확인하라"고 명시했음에도 실패했다는 것은, GitHub 연결 기능 자체가 레포 전체를 자유롭게 탐색(재귀적 파일 검색)하는 방식이 아니라 **README.md를 진입점 삼아 그 안의 링크를 따라가는 방식**일 가능성을 시사한다. 즉 프롬프트 지시로 해결되는 문제가 아니라 플랫폼 리트리버 자체의 동작 방식 문제로 보인다.

**대조 사례**: HebronGuide 테스트(이슈 1)는 README에 링크가 없어도 "GitHub Repo도 찾아보세요"라는 명시적 지시로 성공했다. 반면 Nate Cho는 v2 프롬프트(레포 폴더 확인 지시 포함)만으로는 실패하고 README 링크 추가 후에야 성공했다. 이 차이가 왜 발생하는지는 추가 검증이 필요하다 — 명시적 지시의 강도 차이인지, README 링크 유무 차이인지 통제된 재실험이 필요.

- **임시 대응 (Workaround)**: 새 Builder 프로필을 만들 때마다 README.md "주요 문서" 표에 링크를 함께 추가하는 것을 표준 절차로 삼는다.
- **상태**: 아래 개발자 리포트 작성 완료. M4 GOBI Requirements 문서에 1순위 항목으로도 반영 예정

---

## 🚩 GOBI 개발자 리포트 — GitHub 연결 Repo, README 미링크 파일 검색 실패

**작성일**: 2026-07-05 | **작성자**: 박창수(Changsoo Park) | **수신**: 강민석님 (GOBI 개발자) | **관련 모듈**: Bila-AI-Agent M2

### 요약

Changbal 스페이스의 Bila AI Agent에 GitHub 레포를 연결(Attach)했지만, README.md에서 링크되지 않은 subfolder 파일은 시스템 프롬프트로 명시적으로 검색을 지시해도 찾지 못했습니다. README.md에 해당 파일 링크를 추가하자 바로 정상 참조됐습니다.

### 환경 정보

| 항목 | 내용 |
|------|------|
| Space | Changbal (창발) |
| 연결 레포 | `solkit70/builders-lounge-personal-notes` |
| 브랜치 | main |
| 권한 | Read / Write |
| 연결 상태 | Settings → Agents → GitHub 섹션에 "Attached" 정상 표시 |

### 재현 절차

1. GitHub 레포를 Agents 탭에서 Attach (정상 완료 확인)
2. 시스템 프롬프트(mention/chat)에 "멤버 이름·Product를 물으면 반드시 GitHub 레포의 ideas/, feedback/, builders/, README.md도 확인할 것"이라는 지시를 명시적으로 추가
3. 레포 안에 실제로 존재하지만 README.md에는 링크되지 않은 파일(`ideas/2026-07-02 Nate Cho - Job Search Co-pilot.md`)에 대해 질문: **"Nate Cho님의 Job Search Co-pilot은 어떤 제품인가요?"** (GitHub를 언급하는 힌트 없이)
4. **결과**: 답변 실패 — 해당 정보를 찾을 수 없다고 응답
5. README.md의 "주요 문서" 인덱스 표에 위 파일 링크를 추가
6. 동일 질문 재시도 → **정상 답변** (정확한 제품 설명, 핵심 철학 인용까지 확인)

### 기대 동작 vs 실제 동작

| 구분 | 내용 |
|------|------|
| 기대 | Attach된 레포 안의 모든 파일이 검색 대상이 되어야 함 (시스템 프롬프트로 명시적 지시까지 했으므로) |
| 실제 | README.md에 링크된 파일만 발견됨. 링크 안 된 subfolder 파일은 시스템 프롬프트 지시만으로는 발견되지 않음 |

### 추가 관찰 — 대조 사례

동일한 레포·동일한 조건에서, 사용자가 **채팅 메시지 자체에** "연결된 GitHub Repo도 찾아 보세요"라고 명시적으로 요청했을 때는(김성수님 HebronGuide 질문, 해당 파일도 README에 미링크 상태였음) 정상적으로 레포 내용을 찾아 답변했습니다. 즉:
- **메시지 안의 즉각적 지시** → README 링크 여부와 무관하게 작동
- **시스템 프롬프트(Agent Prompt)의 standing 지시** → README에 링크된 파일에만 작동

### 가설

GitHub 연결 기능의 리트리버가 레포 전체를 재귀적으로 색인하기보다 **README.md를 진입점으로 삼아 그 안의 링크를 따라가는 방식**으로 작동하는 것으로 추정됩니다. 시스템 프롬프트의 standing 지시만으로는 이 진입점 기반 탐색 범위를 벗어나지 못하지만, 사용자의 즉각적 메시지 지시는 (아마 별도의 tool-use 경로를 트리거해서) 이 제약을 우회하는 것으로 보입니다.

### 요청 사항

1. 연결된 레포를 README 진입점과 무관하게 전체 재귀 색인하도록 개선해 주시거나
2. 최소한 이 동작 방식(README 링크 의존)을 공식 문서화해 주시면, 저희가 "새 파일 작성 시 README 링크 필수"를 운영 규칙으로 삼는 데 도움이 될 것 같습니다
3. 가능하다면 "즉각적 메시지 지시 vs 시스템 프롬프트 지시"가 왜 다르게 동작하는지도 궁금합니다

### 참고 자료

- 전체 실험 기록: `Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_worklog/20260705_M2_Bila-AI-Agent.md`
- 연결 레포: https://github.com/solkit70/builders-lounge-personal-notes
- 문제의 파일: `ideas/2026-07-02 Nate Cho - Job Search Co-pilot.md`

### 실험 3: Attach 안 한 레포도 프롬프트 언급만으로 접근되는가 — ✅ 완료

**질문**: GitHub 연결(Attach) 단계가 실제로 필요한가, 아니면 시스템 프롬프트에 레포 이름만 적어도 Agent가 접근하는가?

**실제 테스트**: 원래 `johnfkoo951/cmds-bio`로 계획했으나, 사용자가 본인의 **개인 웹사이트 레포**(Attach 안 함)로 대체 테스트 진행. 시스템 프롬프트 v3에는 이 개인 웹사이트 레포를 데이터 소스로 명시.

**결과**: ❌ 참조 안 됨 — **디자인한 대로 UI에서 Attach(연결)한 GitHub 레포(`solkit70/builders-lounge-personal-notes`)만 참조하고, 프롬프트에 이름만 적은 미연결 레포는 참조하지 않음**

**해석**:
- UI Attach는 **실제로 필수 전제조건**임이 확인됨 — 프롬프트 텍스트만으로 임의 공개 레포에 접근할 수 없다는 뜻
- 보안 관점에서 안심되는 결과: 시스템 프롬프트에 아무 레포 이름이나 적는다고 접근 권한이 생기지 않는다
- 즉 오늘 확인된 3개 이슈는 계층이 다르다: **① Attach(필수, 정상 작동)** → **② 프롬프트가 데이터 소스로 명시해야 함(이슈 1)** → **③ README에 링크된 파일만 발견 가능(이슈 2)**

**후속 조치**: 실험용으로 추가했던 cmds-bio/개인 웹사이트 레포 언급은 프로덕션에 불필요 — 시스템 프롬프트를 v3에서 v2(Attach된 레포만 명시)로 되돌린다.

## DoD 체크리스트 (M2) — 2026-07-05 세션 종료 시점

- [x] GitHub 레포 연결 완료
- [x] 연결 후 기록 참조 답변 확인 → 1차 실패, 원인 규명(시스템 프롬프트 v1 문구, README 링크 부재) 후 해결
- [ ] Google Drive 회의록 폴더 연결 완료 → **다음 세션으로 이월**
- [ ] Phase 1 최종 테스트: 10개 질문 중 7개 이상 적절한 답변 → **다음 세션으로 이월**
- [ ] 데이터 연결 전후 비교 문서 작성 → **다음 세션으로 이월**
- [x] 개선된 시스템 프롬프트 v2 저장 및 검증 (GitHub Attach 필수 확인, 미연결 레포는 참조 안 됨을 실험으로 확인)

**오늘 세션 요약**: 6개 DoD 중 2개 완료, 4개는 다음 세션으로 이월. 다만 계획에 없던 중요한 발견 3개(이슈1·2·실험3)를 얻어 M4 GOBI 요구사항의 핵심 소재를 확보했다.

## Daily Retrospective

- **What went well?**: GitHub 연결 자체는 웹 UI에서 예상대로 한 번에 성공. Read/Write 권한까지 확인됨.
- **What could be improved?**: GitHub 연결과 실제 Q&A 검색 도구가 분리되어 있다는 걸 미리 몰랐다. Roadmap 실습1 검증 단계를 연결 직후 바로 수행한 덕분에 이 격차를 방송 중에 바로 발견할 수 있었다.
- **Insights**: 오늘 세션은 GitHub 연결이 "3단 구조"로 작동한다는 것을 실험으로 규명했다. ① UI Attach는 필수 전제조건(실험3으로 확인 — 프롬프트 언급만으로는 임의 레포 접근 불가, 보안상 안심). ② Attach 되어도 시스템 프롬프트가 "미연결"이라고 선언하면 Agent가 시도조차 안 함(이슈1). ③ 프롬프트가 맞아도 README에 링크 안 된 subfolder 파일은 못 찾음(이슈2). "Attached라고 표시되면 다 된다"는 착각을 세 겹으로 검증하며 걷어낸 세션이었다.
- **Tomorrow's focus**: 시스템 프롬프트를 v3(실험용, cmds-bio/개인 웹사이트 레포 언급 포함)에서 v2(프로덕션, Attach된 레포만 명시)로 되돌리기 → Google Drive 연결(실습2) → Phase 1 최종 10문항 테스트(실습3) → 이슈1·2·실험3 결과를 강민석님께 공유 및 M4 Requirements 문서에 반영

## 오늘 세션 종료 (2026-07-05, Live #17 실험②)

Live #17 방송 중 실험② 세션을 여기서 마무리한다. GitHub 레포 연결과 Q&A 참조 문제를 3단계로 진단·해결한 것이 핵심 성과이며, Google Drive 연결과 Phase 1 최종 검증은 다음 세션에서 이어간다.

## 참조 및 산출물

- Roadmap: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_roadmap/20260628_RoadMap_Bila-AI-Agent]]
- 이전 세션: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_worklog/20260628_M1_Bila-AI-Agent]]
- Live #17 Rundown: [[Roundup/2026-06-29 - Live17 Weekly Rundown#실험③: Bila AI Agent M2 진행 — 데이터 소스 연결]]
