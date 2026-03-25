# GOBI-CLI 학습 로드맵

**Topic**: GOBI-CLI
**생성일**: 2026-03-24
**예상 기간**: 2주 (주당 6-8시간)
**총 예상 시간**: 12-16시간
**방법론**: VibeLearn AI v2.0

---

## 📋 전체 모듈 개요

| 모듈 | 제목 | 예상 시간 | 상태 |
|------|------|----------|------|
| M1 | 설치 & 인증 & 핵심 개념 | 3-4시간 | ⏳ 진행 예정 |
| M2 | Brain & Session 명령어 마스터 | 4-5시간 | ⏳ 진행 예정 |
| M3 | Space & Thread 협업 기능 | 3-4시간 | ⏳ 진행 예정 |
| M4 | 실전 워크플로우 + 교과서 완성 (Capstone) | 2-3시간 | ⏳ 진행 예정 |

**전체 학습 흐름**:
```
M1 (환경/인증/개념) → M2 (Brain/Session 핵심) → M3 (Space/Thread 협업) → M4 (Capstone/참조문서)
```

---

## M1: 설치 & 인증 & 핵심 개념

### 1. 모듈 기본 정보

| 항목 | 내용 |
|------|------|
| **모듈 번호** | M1 |
| **제목** | 설치 & 인증 & 핵심 개념 |
| **예상 시간** | 3-4시간 |
| **산출물 폴더** | `01-Setup-Auth/` |
| **선수 조건** | Node.js 18+ 설치됨, GOBI 계정 있음 |

### 2. 학습 목표

- [ ] `npm install -g @gobi-ai/cli`로 GOBI CLI를 설치하고 버전을 확인할 수 있다
- [ ] `gobi auth login`으로 인증을 완료하고 `gobi auth status`로 확인할 수 있다
- [ ] `gobi init`으로 vault를 선택하고 초기 설정을 완료할 수 있다
- [ ] vault / space / brain / thread / session 5개 핵심 개념을 자신의 말로 설명할 수 있다
- [ ] GOBI CLI 전체 명령어 체계를 한 눈에 파악할 수 있다

### 3. 핵심 개념 (이론 30%)

| 개념 | 설명 | 비유 |
|------|------|------|
| **Vault** | 최상위 지식 컨테이너 (조직의 workspace) | GitHub Organization |
| **Space** | Vault 내 팀 협업 공간 (관련 작업과 brain 그룹) | GitHub Repository |
| **Brain** | AI 기반 지식 자원 — 검색, 질의, 발행 가능 | Wiki + AI 어시스턴트 |
| **Thread** | Space 내 토론 스레드 (팀 커뮤니케이션) | GitHub Issues |
| **Session** | Brain과의 1:1 대화 세션 (AI 질의응답) | ChatGPT 대화창 |

**개념 관계도**:
```
Vault (최상위)
└── Space (팀 협업 공간)
    ├── Brain (지식 자원)
    │   └── Session (1:1 AI 대화)
    └── Thread (팀 토론)
        └── Reply (답글)
```

**전체 명령어 구조**:
```
gobi auth    → login / status / logout
gobi init    → 초기화 (vault 선택)
gobi brain   → search / ask / publish / unpublish / list-updates / post-update / edit-update / delete-update
gobi session → list / get / reply / update
gobi space   → warp / list-threads / get-thread / create-thread / edit-thread / delete-thread / create-reply / edit-reply / delete-reply
```

### 4. 실습 과제 (실습 70%)

#### 실습 1: 설치 및 버전 확인 (30분)
```bash
# Node.js 버전 확인
node --version  # 18+ 필요

# GOBI CLI 전역 설치
npm install -g @gobi-ai/cli

# 설치 확인
gobi --version
gobi --help
```
**성공 기준**: `gobi --version`이 버전 번호를 출력한다

#### 실습 2: 인증 (30분)
```bash
# 로그인
gobi auth login

# 인증 상태 확인
gobi auth status
```
**성공 기준**: `gobi auth status`가 로그인된 계정 정보를 표시한다

#### 실습 3: 초기화 (30분)
```bash
# 프로젝트 초기화 (vault 선택)
gobi init

# 전체 명령어 탐색
gobi --help
gobi brain --help
gobi session --help
gobi space --help
```
**성공 기준**: `gobi init` 완료 후 vault가 선택된 상태

#### 실습 4: 핵심 개념 카드 작성 (60분)
- `01-Setup-Auth/concepts/core-concepts.md` 작성
  - 5개 개념 정의 + 관계도
  - 실제 명령어와 연결된 설명
- 설치~인증 단계별 가이드 작성

### 5. 예상 산출물

```
01-Setup-Auth/
├── README.md                    ← 모듈 학습 순서 가이드
├── concepts/
│   └── core-concepts.md         ← vault/space/brain/thread/session 정의 + 관계도
└── guides/
    ├── installation-guide.md    ← 설치 + 인증 단계별 가이드
    └── first-time-setup.md      ← gobi init 완주 가이드
```

### 6. Definition of Done (DoD)

- [ ] GOBI CLI 설치 완료 (`gobi --version` 동작)
- [ ] `gobi auth login` 인증 완료 (`gobi auth status` 확인)
- [ ] `gobi init` 완료 (vault 선택됨)
- [ ] `core-concepts.md` 작성 완료 (5개 개념 + 관계도)
- [ ] `installation-guide.md` 작성 완료 (재현 가능한 단계별 가이드)
- [ ] `first-time-setup.md` 작성 완료
- [ ] `01-Setup-Auth/README.md` 작성 완료 (학습 순서대로 문서 목록 + 링크)

### 7. 자기 평가 체크리스트

- [ ] "GOBI CLI를 처음 쓰는 팀원에게 설치부터 init까지 직접 설명할 수 있다"
- [ ] "vault, space, brain의 차이를 예시를 들어 설명할 수 있다"
- [ ] "brain과 session의 관계를 설명할 수 있다"
- [ ] "내가 작성한 installation-guide.md를 따라 다른 사람이 설치할 수 있을 것 같다"

### 8. 시간 배분

| 활동 | 시간 | 비중 |
|------|------|------|
| 설치 및 버전 확인 | 30분 | 15% |
| 인증 (auth login/status) | 30분 | 15% |
| 초기화 (init) | 30분 | 15% |
| 명령어 체계 탐색 (--help) | 30분 | 15% |
| 핵심 개념 카드 작성 | 60분 | 25% |
| 산출물 문서화 + README | 30분 | 15% |
| **총계** | **3-4시간** | |

### 9. 참조 자료

- **GitHub**: [https://github.com/gobi-ai/gobi-cli](https://github.com/gobi-ai/gobi-cli)
- **Gobi 플랫폼**: [https://www.gobispace.com](https://www.gobispace.com)
- **설치 명령어**: `npm install -g @gobi-ai/cli`
- **Node.js 공식**: [https://nodejs.org](https://nodejs.org) (버전 확인용)

---

## M2: Brain & Session 명령어 마스터

### 1. 모듈 기본 정보

| 항목 | 내용 |
|------|------|
| **모듈 번호** | M2 |
| **제목** | Brain & Session 명령어 마스터 |
| **예상 시간** | 4-5시간 |
| **산출물 폴더** | `02-Brain-Session/` |
| **선수 조건** | M1 완료 (설치/인증/init 완료) |

### 2. 학습 목표

- [ ] `gobi brain search --query "..."` 로 brain에서 정보를 검색할 수 있다
- [ ] `gobi brain ask --question "..."` 로 AI 세션을 시작할 수 있다
- [ ] `gobi session list / get / reply / update` 로 세션을 관리할 수 있다
- [ ] `BRAIN.md` 파일을 작성하고 `gobi brain publish` 로 발행할 수 있다
- [ ] `gobi brain post-update / list-updates / edit-update / delete-update` 로 updates를 관리할 수 있다

### 3. 핵심 개념 (이론 20%)

**Brain 명령어 전체 맵**:
```
gobi brain search   --query "..."             # brain에서 정보 검색
gobi brain ask      --question "..."          # AI 세션 시작 (새 session 생성)
gobi brain publish  [파일경로]                # BRAIN.md 발행
gobi brain unpublish                          # 발행 취소
gobi brain list-updates                       # 업데이트 목록 조회
gobi brain post-update  --content "..."       # 업데이트 게시
gobi brain edit-update  --update-id X --content "..."  # 업데이트 수정
gobi brain delete-update --update-id X        # 업데이트 삭제
```

**Session 명령어 전체 맵**:
```
gobi session list                             # 세션 목록 조회
gobi session get    --session-id X            # 특정 세션 조회
gobi session reply  --session-id X --message "..."  # 세션에 답장
gobi session update --session-id X --title "..."    # 세션 제목 수정
```

**Brain ask → Session 흐름**:
```
gobi brain ask --question "질문"
  → 새 Session 생성됨
  → session-id 반환
  → gobi session reply --session-id X --message "후속 질문"
  → 대화 이어가기
```

**BRAIN.md 구조**:
```markdown
# Brain Name

## Overview
{brain에 대한 설명}

## Key Topics
{주요 주제들}

## Resources
{참조 자료}
```

### 4. 실습 과제 (실습 80%)

#### 실습 1: brain search 실험 (45분)
```bash
# 다양한 쿼리로 검색 실험
gobi brain search --query "getting started"
gobi brain search --query "API"
gobi brain search --query "authentication"

# JSON 출력으로 구조 파악
gobi brain search --query "test" --json
```
**성공 기준**: 검색 결과가 출력되고 구조를 이해한다

#### 실습 2: brain ask + session 관리 (60분)
```bash
# AI 세션 시작
gobi brain ask --question "What is this brain about?"

# 세션 목록 확인
gobi session list

# 특정 세션 조회
gobi session get --session-id [SESSION_ID]

# 세션에 후속 질문
gobi session reply --session-id [SESSION_ID] --message "Tell me more about..."

# 세션 제목 수정
gobi session update --session-id [SESSION_ID] --title "My First Session"
```
**성공 기준**: 멀티턴 대화를 이어가고 session list에서 확인된다

#### 실습 3: BRAIN.md 작성 및 publish (60분)
```bash
# BRAIN.md 파일 작성 (에디터에서)
# gobi brain publish로 발행
gobi brain publish ./BRAIN.md

# 발행 확인
gobi brain list-updates

# unpublish 실습
gobi brain unpublish
```
**성공 기준**: BRAIN.md가 발행되고 플랫폼에서 확인된다

#### 실습 4: brain updates CRUD (45분)
```bash
# 업데이트 게시
gobi brain post-update --content "First update: Learning GOBI CLI"

# 업데이트 목록 확인
gobi brain list-updates

# 업데이트 수정
gobi brain edit-update --update-id [ID] --content "Updated content"

# 업데이트 삭제
gobi brain delete-update --update-id [ID]
```
**성공 기준**: update CRUD 전체 사이클 완료

### 5. 예상 산출물

```
02-Brain-Session/
├── README.md                        ← 모듈 학습 순서 가이드
├── guides/
│   ├── brain-search-guide.md        ← brain search + ask 사용법 + 실습 로그
│   ├── session-management.md        ← session 명령어 전체 가이드
│   └── brain-publish-guide.md       ← BRAIN.md 작성 + publish 방법
└── examples/
    └── sample-brain.md              ← 예시 BRAIN.md 파일 (재사용 가능)
```

### 6. Definition of Done (DoD)

- [ ] `gobi brain search` 로 검색 결과 확인 및 구조 파악
- [ ] `gobi brain ask` 로 새 session 생성 성공
- [ ] `gobi session reply` 로 멀티턴 대화 완료
- [ ] `gobi session list / get / update` 전체 실습 완료
- [ ] `BRAIN.md` 작성 후 `gobi brain publish` 발행 성공
- [ ] `gobi brain post-update` / `list-updates` / `edit-update` / `delete-update` CRUD 완료
- [ ] `brain-search-guide.md` 작성 완료 (실제 출력 결과 포함)
- [ ] `session-management.md` 작성 완료
- [ ] `brain-publish-guide.md` + `sample-brain.md` 작성 완료
- [ ] `02-Brain-Session/README.md` 작성 완료

### 7. 자기 평가 체크리스트

- [ ] "brain search와 brain ask의 차이를 설명할 수 있다"
- [ ] "session reply로 대화를 이어가는 방법을 안다"
- [ ] "BRAIN.md를 작성하고 발행하는 전체 흐름을 혼자 할 수 있다"
- [ ] "brain updates로 팀에 진행 상황을 공유하는 방법을 안다"
- [ ] "내가 작성한 가이드로 다른 사람이 brain/session을 사용할 수 있을 것 같다"

### 8. 시간 배분

| 활동 | 시간 | 비중 |
|------|------|------|
| 개념 파악 (brain/session 구조) | 30분 | 10% |
| brain search 실험 | 45분 | 15% |
| brain ask + session 관리 | 60분 | 20% |
| BRAIN.md 작성 + publish | 60분 | 20% |
| brain updates CRUD | 45분 | 15% |
| 산출물 문서화 + README | 60분 | 20% |
| **총계** | **4-5시간** | |

### 9. 참조 자료

- **GitHub GOBI CLI**: [https://github.com/gobi-ai/gobi-cli](https://github.com/gobi-ai/gobi-cli)
- **gobi brain --help**: 터미널에서 직접 확인
- **gobi session --help**: 터미널에서 직접 확인
- **M1 산출물**: `01-Setup-Auth/concepts/core-concepts.md`

---

## M3: Space & Thread 협업 기능

### 1. 모듈 기본 정보

| 항목 | 내용 |
|------|------|
| **모듈 번호** | M3 |
| **제목** | Space & Thread 협업 기능 |
| **예상 시간** | 3-4시간 |
| **산출물 폴더** | `03-Space-Collaboration/` |
| **선수 조건** | M1 + M2 완료 |

### 2. 학습 목표

- [ ] `gobi space warp` 로 space를 전환하고 현재 context를 확인할 수 있다
- [ ] `gobi space list-threads / get-thread` 로 thread를 조회할 수 있다
- [ ] `gobi space create-thread / edit-thread / delete-thread` 로 thread CRUD를 수행할 수 있다
- [ ] `gobi space create-reply / edit-reply / delete-reply` 로 reply CRUD를 수행할 수 있다
- [ ] `--json`, `--space-slug`, `--vault-slug` 글로벌 옵션을 활용할 수 있다

### 3. 핵심 개념 (이론 20%)

**Space 명령어 전체 맵**:
```
gobi space warp                                    # space 전환 (대화형 선택)
gobi space list-threads                            # thread 목록 조회
gobi space get-thread    --thread-id X             # 특정 thread 조회
gobi space create-thread --title "..." --body "..." # thread 생성
gobi space edit-thread   --thread-id X --title "..." --body "..." # thread 수정
gobi space delete-thread --thread-id X             # thread 삭제
gobi space create-reply  --thread-id X --body "..." # reply 생성
gobi space edit-reply    --thread-id X --reply-id Y --body "..." # reply 수정
gobi space delete-reply  --thread-id X --reply-id Y # reply 삭제
```

**글로벌 옵션**:
```
--json                   # JSON 형식으로 출력 (파이프 처리, 자동화에 유용)
--vault-slug [slug]      # 특정 vault 지정 (기본값: init으로 선택한 vault)
--space-slug [slug]      # 특정 space 지정 (warp 없이 바로 지정)
```

**Space vs Thread vs Reply 관계**:
```
Space (팀 협업 공간)
└── Thread (토론 주제)
    ├── Body (본문)
    └── Reply (답글)
        ├── Reply 1
        └── Reply 2
```

### 4. 실습 과제 (실습 80%)

#### 실습 1: space warp + 탐색 (30분)
```bash
# space 전환
gobi space warp

# thread 목록 조회
gobi space list-threads

# thread 목록 JSON 출력
gobi space list-threads --json

# 특정 space 지정
gobi space list-threads --space-slug [SPACE_SLUG]
```
**성공 기준**: space 전환 후 thread 목록이 출력된다

#### 실습 2: thread CRUD (60분)
```bash
# thread 생성
gobi space create-thread --title "GOBI CLI 학습 기록" --body "GOBI CLI 학습을 시작했습니다."

# thread 목록에서 ID 확인
gobi space list-threads

# thread 조회
gobi space get-thread --thread-id [THREAD_ID]

# thread 수정
gobi space edit-thread --thread-id [THREAD_ID] --title "GOBI CLI 학습 기록 (업데이트)" --body "M1 완료!"

# thread 삭제 (선택)
# gobi space delete-thread --thread-id [THREAD_ID]
```
**성공 기준**: thread 생성/조회/수정이 플랫폼에서 확인된다

#### 실습 3: reply CRUD (45분)
```bash
# reply 생성
gobi space create-reply --thread-id [THREAD_ID] --body "M2도 시작합니다!"

# thread 조회로 reply 확인
gobi space get-thread --thread-id [THREAD_ID]

# reply 수정
gobi space edit-reply --thread-id [THREAD_ID] --reply-id [REPLY_ID] --body "M2 brain search 완료!"

# reply 삭제 (선택)
# gobi space delete-reply --thread-id [THREAD_ID] --reply-id [REPLY_ID]
```
**성공 기준**: reply CRUD 전체 사이클 완료

#### 실습 4: 글로벌 옵션 실험 (30분)
```bash
# --json 옵션으로 구조화된 출력
gobi space list-threads --json
gobi space get-thread --thread-id [ID] --json

# --vault-slug, --space-slug 옵션
gobi space list-threads --vault-slug [VAULT] --space-slug [SPACE]
```
**성공 기준**: --json 출력 구조를 이해하고 활용할 수 있다

### 5. 예상 산출물

```
03-Space-Collaboration/
├── README.md                        ← 모듈 학습 순서 가이드
└── guides/
    ├── space-navigation.md          ← space warp + list-threads + 탐색
    ├── thread-management.md         ← thread CRUD 전체 가이드 (예시 포함)
    └── global-options.md            ← --json, --slug 옵션 활용 가이드
```

### 6. Definition of Done (DoD)

- [ ] `gobi space warp` 로 space 전환 성공
- [ ] `gobi space list-threads` 로 thread 목록 확인
- [ ] `gobi space create-thread` 로 thread 생성 성공
- [ ] `gobi space edit-thread` 로 thread 수정 성공
- [ ] `gobi space delete-thread` 로 thread 삭제 성공
- [ ] `gobi space create-reply / edit-reply / delete-reply` CRUD 완료
- [ ] `--json` 옵션 출력 구조 파악
- [ ] `space-navigation.md` 작성 완료
- [ ] `thread-management.md` 작성 완료 (CRUD 예시 포함)
- [ ] `global-options.md` 작성 완료
- [ ] `03-Space-Collaboration/README.md` 작성 완료

### 7. 자기 평가 체크리스트

- [ ] "gobi space warp와 --space-slug 옵션의 차이를 설명할 수 있다"
- [ ] "thread와 reply의 관계를 설명할 수 있다"
- [ ] "thread CRUD 전체를 터미널에서 혼자 수행할 수 있다"
- [ ] "--json 옵션 출력을 jq나 다른 도구로 파이프할 수 있다"
- [ ] "내가 작성한 thread-management.md를 보고 다른 사람이 바로 사용할 수 있다"

### 8. 시간 배분

| 활동 | 시간 | 비중 |
|------|------|------|
| space 개념 + 명령어 구조 파악 | 30분 | 12% |
| space warp + 탐색 실습 | 30분 | 12% |
| thread CRUD 실습 | 60분 | 25% |
| reply CRUD 실습 | 45분 | 19% |
| 글로벌 옵션 실험 | 30분 | 12% |
| 산출물 문서화 + README | 45분 | 19% |
| **총계** | **3-4시간** | |

### 9. 참조 자료

- **GitHub GOBI CLI**: [https://github.com/gobi-ai/gobi-cli](https://github.com/gobi-ai/gobi-cli)
- **gobi space --help**: 터미널에서 직접 확인
- **M1 핵심 개념**: `01-Setup-Auth/concepts/core-concepts.md`
- **M2 brain 가이드**: `02-Brain-Session/guides/brain-search-guide.md`

---

## M4: 실전 워크플로우 + 교과서 완성 (Capstone)

### 1. 모듈 기본 정보

| 항목 | 내용 |
|------|------|
| **모듈 번호** | M4 |
| **제목** | 실전 워크플로우 + 교과서 완성 (Capstone) |
| **예상 시간** | 2-3시간 |
| **산출물 폴더** | `04-Real-World/` |
| **선수 조건** | M1 + M2 + M3 완료 |

### 2. 학습 목표

- [ ] init → brain search → brain ask → session reply → thread 생성까지 end-to-end 시나리오를 혼자 수행할 수 있다
- [ ] 전체 GOBI CLI 명령어를 1페이지 Quick Reference Card로 정리할 수 있다
- [ ] 처음 보는 사람이 바로 따라할 수 있는 README.md를 작성할 수 있다
- [ ] GOBI CLI 학습 전체를 돌아보고 실무 활용 방안을 제시할 수 있다

### 3. 핵심 개념 (이론 10%)

**실전 시나리오 흐름**:
```
시나리오: "새 팀원이 GOBI CLI를 처음 쓰는 날"

1. gobi auth login          → 인증
2. gobi init                → vault 선택
3. gobi brain search --query "onboarding"  → 기존 지식 검색
4. gobi brain ask --question "What should I know first?"  → AI 질의
5. gobi session reply --session-id X --message "더 자세히 알고 싶어요"  → 대화 이어가기
6. gobi space warp          → 팀 space로 이동
7. gobi space create-thread --title "신규 팀원 온보딩" --body "..."  → 팀에 공유
8. gobi space create-reply --thread-id X --body "AI 답변 내용 정리"  → 답글
```

**교과서 품질 기준**:
- 처음 보는 사람이 README만 보고 순서대로 학습 가능
- 모든 명령어에 실제 예시 포함
- 에러 케이스 및 해결 방법 포함
- 복사-붙여넣기로 바로 실행 가능한 코드

### 4. 실습 과제 (실습 90%)

#### 실습 1: End-to-End 시나리오 수행 (60분)

위 시나리오를 처음부터 끝까지 혼자 수행:
```bash
# 1단계: 인증 확인
gobi auth status

# 2단계: brain 검색
gobi brain search --query "getting started"

# 3단계: AI 세션 시작
gobi brain ask --question "What are the most important features of this brain?"

# 4단계: 세션 이어가기
gobi session list
gobi session reply --session-id [ID] --message "Can you elaborate on the first point?"

# 5단계: space에서 팀 공유
gobi space warp
gobi space create-thread --title "Today's Learning: GOBI CLI" --body "Completed M1-M3!"
gobi space create-reply --thread-id [ID] --body "Key insight: brain ask creates a persistent session"
```
**성공 기준**: 모든 단계가 오류 없이 실행된다

#### 실습 2: Quick Reference Card 작성 (45분)

`04-Real-World/guides/quick-reference.md` 작성:
- 전체 명령어 1페이지 요약
- 각 명령어별 가장 유용한 옵션
- 자주 쓰는 패턴 예시
- 글로벌 옵션 정리

#### 실습 3: 최종 README.md 완성 (30분)

`Topics/GOBI-CLI/README.md` 작성:
- 학습 순서 안내 (M1 → M2 → M3 → M4)
- 각 모듈 링크 및 1줄 설명
- 빠른 시작 가이드 (처음 사용자용)
- Quick Reference Card 링크

### 5. 예상 산출물

```
04-Real-World/
├── README.md                        ← 모듈 학습 순서 가이드
└── guides/
    ├── complete-workflow.md         ← end-to-end 시나리오 가이드 (실제 출력 포함)
    └── quick-reference.md           ← 전체 명령어 Quick Reference Card

Topics/GOBI-CLI/
└── README.md                        ← 전체 Topic 학습 가이드 (처음 사용자 진입점)
```

### 6. Definition of Done (DoD)

- [ ] End-to-End 시나리오 (init → search → ask → reply → thread) 완료
- [ ] `complete-workflow.md` 작성 완료 (실제 출력 결과 포함)
- [ ] `quick-reference.md` 작성 완료 (전체 명령어 + 옵션 + 예시)
- [ ] `Topics/GOBI-CLI/README.md` 작성 완료 (학습 순서 가이드)
- [ ] `04-Real-World/README.md` 작성 완료
- [ ] 전체 Topic Retrospective 작성 완료

### 7. 자기 평가 체크리스트

- [ ] "GOBI CLI를 처음 쓰는 팀원에게 30분 안에 핵심을 가르칠 수 있다"
- [ ] "Quick Reference Card만 보고 모든 명령어를 사용할 수 있다"
- [ ] "내가 만든 산출물을 다른 학습자가 재사용할 수 있다"
- [ ] "GOBI CLI를 실무에서 어떤 상황에 활용할지 구체적으로 말할 수 있다"
- [ ] "VibeLearn AI 방법론으로 학습했을 때의 장점을 경험으로 설명할 수 있다"

### 8. 시간 배분

| 활동 | 시간 | 비중 |
|------|------|------|
| End-to-End 시나리오 수행 | 60분 | 37% |
| Quick Reference Card 작성 | 45분 | 28% |
| Topic README.md 완성 | 30분 | 19% |
| Topic Retrospective 작성 | 15분 | 9% |
| 최종 정리 + git push | 15분 | 7% |
| **총계** | **2-3시간** | |

### 9. 참조 자료

- **M1 산출물**: `01-Setup-Auth/`
- **M2 산출물**: `02-Brain-Session/`
- **M3 산출물**: `03-Space-Collaboration/`
- **GitHub GOBI CLI**: [https://github.com/gobi-ai/gobi-cli](https://github.com/gobi-ai/gobi-cli)
- **VibeLearn AI 방법론**: `CLAUDE.md`

---

## 📊 전체 학습 로드맵 요약

```
Week 1 (1주차)
├── Day 1-2: M1 설치 & 인증 & 핵심 개념 (3-4h)
│   └── 산출물: 01-Setup-Auth/ (core-concepts.md, installation-guide.md, first-time-setup.md)
└── Day 3-5: M2 Brain & Session 명령어 (4-5h)
    └── 산출물: 02-Brain-Session/ (brain-search-guide.md, session-management.md, brain-publish-guide.md, sample-brain.md)

Week 2 (2주차)
├── Day 6-8: M3 Space & Thread 협업 (3-4h)
│   └── 산출물: 03-Space-Collaboration/ (space-navigation.md, thread-management.md, global-options.md)
└── Day 9-10: M4 Capstone + 교과서 완성 (2-3h)
    └── 산출물: 04-Real-World/ (complete-workflow.md, quick-reference.md) + Topics/GOBI-CLI/README.md
```

**최종 산출물 목록** (교과서 품질):
1. `01-Setup-Auth/` — 설치/인증/개념 가이드
2. `02-Brain-Session/` — Brain & Session 완전 가이드
3. `03-Space-Collaboration/` — Space & Thread 협업 가이드
4. `04-Real-World/quick-reference.md` — 전체 명령어 Quick Reference Card ⭐
5. `Topics/GOBI-CLI/README.md` — 처음 사용자 진입점 ⭐

---

**Roadmap 생성일**: 2026-03-24
**방법론**: VibeLearn AI v2.0
**다음 단계**: `vl_prompts/daily_learning_prompt.md`를 사용하여 M1 Day1 학습 시작
