# WorkLog - M0 · M1: 시작의 기록 · 스키마 + 인덱서

**날짜**: 2026-09-27 (일) — Live #29 방송 중
**모듈**: M0 - 시작의 기록 → M1 - 스키마 + 인덱서 (첫 세션)
**한 바퀴 위치**: M0 ①~④ 초안 완료 · ⑤ 주중 / M1 ④ 구현·검증 1차 완료 · ⑤ 주중

## ▶ 다음 세션 시작 때 먼저 알릴 것 — 승인 대기 (방송 종료 2026-09-27)

> 사용자 요청: 「제안이나 승인을 바라는 것들은 다음 시간에 시작할 떄 저한테 알려 주세요.」 — 다음 세션은 **이 표부터** 보여 주고 승인을 받은 뒤 시작한다.

| # | 승인 요청 | 제안 | 승인되면 |
|---|---|---|---|
| **A1** | **M1 인덱서 속도** (E7 실패 — 86초) | 선택지 A(제외 폴더를 훑는 도중 건너뛰기, `os.walk` — 측정 2.3초) + B(경로 링크는 파일 존재만 바로 확인, 볼트 전체 목록은 이름만 적은 링크가 있을 때만 — 100개 링크 모두 경로형). **E7 목표 = 5초 안** | 코드 수정 → 58건·fixture 재검증 → `decisions/009` · WorkLog |
| **A2** | **방송 후 문서 검토 결과** | 사용자가 방송 후 살펴보기로 한 문서: 시작의 기록 · `ARCHITECTURE.md` · `decisions/001~008` · 실험 노트 (방송 중 훑어본 판단: 「일단 OK」) | 고칠 곳 반영 |
| **A3** | EARS 한국어 틀 확인 | 「WHEN [조건] 이면 THE SYSTEM SHALL [동작] 한다」 (008) | 그대로 M2 부터 사용 |
| **A4** | 공개 레포 커밋·push 시점 | 공개 전 개인정보 재점검(이름·연락처·실제 할 일) 후, 사용자가 요청할 때 | CatchUpAI_VL push |

**승인과 무관하게 남은 일** (M0·M1 닫기): `00-Start-Record/` · `01-Schema-Indexer/` README · Topic 최상위 `README.md` · `check_links.py` · E5 `link_ambiguous` fixture · `_schema.md` 결정 로그 9건 반영표

## 🎯 오늘의 학습 목표

- [x] Topic 생성 — 폴더 · `topic_starter.md` · `roadmap_prompt.md`(템플릿 [1단계]만 채움) · `daily_learning_prompt.md`
- [x] 학습 기간 적정성 검토 → 사용자 「그대로 진행」 (방송 중 못 끝낸 모듈은 주중에)
- [x] 로드맵 초안 → 사용자 의견 반영(멀티 에이전트 구조 열어 두기) → 저장
- [x] M0 「시작의 기록」 초안
- [x] `ARCHITECTURE.md` 첫 판 (에이전트 계약 표 포함)
- [x] M1 인덱서 — 실제 58건 파싱 · fixture 로 오류 탐지 확인 · 원본 무변경
- [x] M0 결정 기록 001~007 (방송 중)
- [x] KIRO 공식 문서 확인 → 006 에 비교표 추가 (방송 중) — 같음: 기능 단위 · 승인 게이트 · 문서를 계속 고침 / 다름: KIRO 는 결정 이유 파일(ADR)이 없음 · 요구를 EARS 로 씀 → M2 에서 EARS 도입 여부를 사용자에게 묻는다

## 📚 진행 내용

### 1. 오늘 정한 요구 (방송 중 사용자와 대화)

| 요구 | 반영 |
|---|---|
| 학습 기간: M0~M10, 모듈 하나 ≈ 방송 한 회 + 주중. 방송 중에 못 끝낸 모듈은 주중에 | 로드맵 「예상 학습 기간」 · 예외 4곳(M0·M1 짧음 · M3 작아질 수 있음 · M6 방송 2회 · M9 달력 7일) |
| 「이것은 저의 첫 멀티 에이전트 시스템」— v1 에이전트는 무엇인가 | Board · Deadline · Intake · Discovery 넷 (PRD 3절). 인덱서는 스크립트, 오케스트레이터는 런타임 |
| 🔑 **에이전트끼리 직접 부르지 않게 하되, 나중에 호출이 필요하면 바꿀 수 있게.** Supervisor 가 팀원을 관리하는 방식, 동급 에이전트가 소통하는 방식 등 다양한 구조의 가능성을 열어 둔다 | 로드맵 「멀티 에이전트 구조 — 열어 둔다」 절 · `ARCHITECTURE.md` 3절 **에이전트 계약 표** · 4절 · 결정 기록 007(예정) · M2 이후 업계 방식 조사에 「구조 검토」 · M10 템플릿에 「구조 고르기」 |
| 🔑 **KIRO 비교 뒤 제안(EARS 한 줄) 채택.** 「이 토픽은 KIRO 의 아키텍쳐 를 동시에 업데이트 해 가면서 진행하는 프로젝트 진행 방법을 저의 VibeLearn AI 에 접목시키는 것을 실험하는 단계 입니다. 이 실험이 성공적이라고 판단되면 VibeLearn AI 의 새로운 버전을 별도로 만들고 싶습니다. 그래서 KIRO 의 방법을 곧바로 적용하기 어려은 것은 우리 나람대로 방법을 찾아서 적용하면 됩니다.」 | `decisions/008` · `vl_materials/VibeLearn AI 새 버전 실험 노트.md`(접목 원장) · 로드맵 학습 목표·한 바퀴 규칙·M10 DoD·성공 기준 · topic_starter · daily_learning_prompt |

**EARS 첫 적용 — M1 인덱서 요구 (소급 작성 · 오늘 검증 결과)**

| # | EARS | 검증 |
|---|---|---|
| E1 | THE SYSTEM SHALL `items/*.md` 중 `_schema.md` 를 뺀 모든 파일을 `views/index.json` 의 `tasks` 에 남긴다 | ✅ 58/58 |
| E2 | WHEN frontmatter 를 읽지 못하면 THE SYSTEM SHALL 그 파일을 건너뛰지 않고 `valid:false` 와 `frontmatter_parse_error` 로 남긴다 | ✅ fixture |
| E3 | WHEN tier 가 1 인데 `due` 가 없으면 THE SYSTEM SHALL `tier_due_required` 경고를 내고 tier 를 고치지 않는다 | ✅ fixture |
| E4 | WHEN status 가 waiting 이면 THE SYSTEM SHALL tier 2 와 `waiting_on` 을 확인해 어긋나면 경고한다 | ✅ fixture |
| E5 | WHEN `project`·`source` 에 링크가 있으면 THE SYSTEM SHALL 대상 파일이 0개면 `link_unresolved`, 2개 이상이면 `link_ambiguous` 를 낸다 | ✅ unresolved (ambiguous 는 주중) |
| E6 | THE SYSTEM SHALL `items/` 의 어떤 파일도 수정하지 않는다 | ✅ SHA-1 전후 동일 |
| E7 | THE SYSTEM SHALL 인덱스를 **N초 안에** 만든다 | ❌ 86초 — 목표값 미정 → 3번 작업 |

### 2. M0 — 시작의 기록 · ARCHITECTURE.md

- `vl_materials/2026-09-27 시작의 기록.md` — 왜(9/12 할 일 62건 · 5건 지남 · 한 시간 수동 정리) · 어떻게(네 문서 · 다섯 결정) · 무엇을 준비(23→58건 · 결정 로그 9건) · 어떤 방식(Builders Lounge 5차에서 배운 세 원칙 · 두 트랙) · 멀티 에이전트 구조 열어 둠. 실제 할 일 내용·이름 없음
- `architecture/ARCHITECTURE.md` v0.1 — 한눈에(mermaid) · 층 · **에이전트 계약 표** · 멀티 에이전트 구조 · 절대 규칙 · 결정 기록 목록 · 변경 이력
- ✅ **사용자 리뷰 (방송 중)**: 「아키텍쳐는 리뷰 했습니다. 지금과 같이 진행하면 될 것 같습니다.」 — v0.1 승인

### 3. M1 — 인덱서

볼트 `AI/Tasks/scripts/pob_index.py` (Python 3.13 · `python-frontmatter`) · `views/` · `inbox/` 폴더 생성.

**실제 items 결과**

| 항목 | 결과 |
|---|---|
| 입력 | 58건 (`_schema.md` 제외) |
| `tasks` | **58** · valid 58 |
| problems | error 0 · warning 16 (`project_missing` 10 · `source_missing` 6) · info 0 |
| 9/25 사전 점검 예상 | 권장 필드 경고 16개 (project 10 · source 6) — **일치** |
| 원본 무변경 | 실행 전후 `items/` 전체 SHA-1 비교 — 차이 0 |

**fixture 결과** (`items/` 바깥 임시 폴더 · 가짜 할 일 3개)

| fixture | 기대 | 결과 |
|---|---|---|
| tier 1 · due 없음 · 없는 링크 | `tier_due_required` · `link_unresolved` | ✅ 둘 다 |
| waiting · tier 3 · waiting_on 없음 | `tier_mismatch_waiting` · `waiting_on_required` | ✅ 둘 다 (+ 권장 필드 경고) |
| YAML 깨짐 | `frontmatter_parse_error` · `valid:false` 로 남음 | ✅ 건너뛰지 않음 |

## 🐛 문제 해결 로그

### 문제 1: 인덱서 한 번 실행에 1분 26초

- **원인**: 링크 실재 검사를 위해 **볼트 전체 파일**을 매번 훑는다 (`rglob`)
- **지금**: 동작은 맞다. 방송에서는 그대로 둔다
- **다음**: 주중에 선택지 비교 → 결정 기록 — ① 링크 대상 후보 폴더만 훑기 ② 파일 목록 캐시 ③ Obsidian CLI(`obsidian unresolved`)에 맡기기. 업계 방식(정적 사이트 생성기·린터의 링크 검사)을 먼저 조사

### 문제 2: 템플릿 주입 스크립트의 한국어 출력 오류

- Windows 콘솔(cp1252)에서 한국어 `print` 가 `UnicodeEncodeError`. 파일은 이미 써진 뒤였다 → `PYTHONIOENCODING=utf-8` 로 재실행해 검증

## 📊 DoD 체크리스트

**M0**
- [x] 「시작의 기록」에 왜·어떻게·무엇을 준비·어떤 방식
- [x] `ARCHITECTURE.md` 첫 판 + 에이전트 계약 표
- [x] 첫 결정 기록 7개 (007 포함) — 방송 중
- [x] 공개 문서에 실제 할 일·이름·연락처 없음 (초안 기준 — 주중 재점검)
- [ ] 모듈 README (`00-Start-Record/`) — 주중
- [ ] `python scripts/check_links.py` — 주중
- [x] WorkLog

**M1**
- [x] 58건 전부 `tasks` 에 있다
- [x] fixture 로 tier 오류 탐지 · 원본 무변경
- [ ] `_schema.md` 결정 로그 9건 반영 여부 표 — 주중
- [ ] `ARCHITECTURE.md` 갱신 + 결정 기록 (예: 캐시가 JSON 인데 원본이 아닌 이유 · 링크 검사 속도) — 주중
- [ ] 모듈 README (`01-Schema-Indexer/`) · 가린 fixture 를 `examples/` 로 — 주중

## 💡 Daily Retrospective

### What went well (잘된 점)
- 2주 동안 데이터를 먼저 키우고 사양을 코드 없이 정해 둔 덕에, 인덱서가 **첫 실행에서 예상과 같은 숫자**(58건 · 경고 16)를 냈다
- 방송 중 사용자 질문(「첫 멀티 에이전트 시스템인데 어떤 에이전트가?」)이 곧바로 아키텍처 결정(구조 열어 두기 · 에이전트 계약 표)이 됐다 — 「대화를 아키텍처 문서에 쌓는」 방식이 첫날부터 작동했다

### What could be improved (개선할 점)
- 링크 검사 속도를 사전 점검에서 보지 못했다 — 사양에 「얼마나 빨라야 하나」가 없었다

### Insights (인사이트)
- v1 은 파일 공유(블랙보드)로 출발하지만, **바꿀 수 있게 하는 장치는 코드가 아니라 문서(계약 표)** 에서 시작한다

### Tomorrow's focus (다음에 이어갈 곳)
0. **맨 먼저: 위 「다음 세션 시작 때 먼저 알릴 것」 A1~A4 를 사용자에게 보여 주고 승인받기**
1. M0 ⑤: `00-Start-Record/README.md` · concepts 3개 · 사용자 문서 검토(방송 후) 반영
2. M1 ⑤: 링크 검사 속도 결정 · 결정 로그 9건 반영표 · `01-Schema-Indexer/` README · 가린 fixture
3. Topic 최상위 `README.md` · `check_links.py`

## 📎 참조 및 산출물

- 로드맵: [../vl_roadmap/20260927_RoadMap_Personal-Ops-Board.md](../vl_roadmap/20260927_RoadMap_Personal-Ops-Board.md)
- 시작의 기록: [../vl_materials/2026-09-27 시작의 기록.md](<../vl_materials/2026-09-27 시작의 기록.md>)
- 아키텍처: [../architecture/ARCHITECTURE.md](../architecture/ARCHITECTURE.md)
- 볼트(비공개): `AI/Tasks/scripts/pob_index.py` · `AI/Tasks/views/index.json`
