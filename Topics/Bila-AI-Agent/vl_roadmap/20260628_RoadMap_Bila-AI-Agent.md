# Bila-AI-Agent 학습 로드맵

**생성일**: 2026-06-28
**방법론**: VibeLearn AI
**버전**: 1.0

---

## 📚 학습 개요

### Topic 소개

GobiSpace Changbal 스페이스의 **Bila AI Agent**를 실제로 구축하는 프로젝트 기반 학습. "기록을 읽고 답하는 것에서 시작해, 멤버들이 서로의 성장을 가속시키는 연결 엔진이 된다"는 비전 아래, Phase 1 구현부터 GOBI 플랫폼 요구사항 도출까지 단계적으로 진행한다.

### 학습 목표

- [ ] Bila AI Agent용 시스템 프롬프트(@mention/채팅 두 버전)를 직접 설계하고 Changbal 스페이스에 적용할 수 있다
- [ ] GobiSpace Agents 탭의 모든 연결 기능(GitHub, Google Drive, Vault, Slack)을 사용할 수 있다
- [ ] Phase 1 Q&A가 실제 BL 멤버 질문 5개에 정확히 답하는 수준에 도달한다
- [ ] Phase 2, 3 구현을 위한 GOBI 개발자 요구사항 문서를 완성하고 강민석님에게 제출할 수 있다

### 예상 학습 기간

2026년 7월 ~ 8월 (주당 2-3시간, 약 4-8주)

### 학습 환경

- OS: Windows 11
- 도구: GobiSpace 웹 UI (어드민 권한), gobi CLI v2.0.35, VS Code + Claude Code, GitHub, Google Drive
- 사전 지식: Changbal 스페이스 어드민 권한 (완료), Bila 원본 시스템 프롬프트 확보 (완료)

---

## 📊 학습 기간 적정성 분석

**사용자 입력 기간**: 2026년 7월 ~ 8월 (주당 2-3시간)
**Topic 복잡도**: 중간 (플랫폼 기반 AI Agent 설계, 데이터 소스 연결, 요구사항 도출)

**분석 결과**: ✅ **적정함**
- 4개 모듈 × 모듈당 3-4시간 = 총 12-16시간
- 주당 2-3시간 기준 약 5-8주 — 기간 내 충분히 완료 가능
- 방송 중 실시간 실험이 포함되어 있어 실습 효율 높음

---

## 🗺️ 전체 로드맵 구조

| 모듈  | 모듈명                     | 난이도 | 예상 시간 | 산출물 폴더                    |
| --- | ----------------------- | --- | ----- | ------------------------- |
| M1  | GobiSpace Agents 설정 마스터 | ⭐   | 3h    | `01-Agents-Setup/`        |
| M2  | 데이터 소스 연결 & Phase 1 구현  | ⭐⭐  | 4h    | `02-DataSource-Phase1/`   |
| M3  | 채널 구조 & 어드민 워크플로우       | ⭐⭐  | 3h    | `03-Channel-Admin/`       |
| M4  | 한계 분석 & GOBI 요구사항       | ⭐⭐⭐ | 3h    | `04-Limits-Requirements/` |

**총 예상 시간**: 13시간 (버퍼 포함)
**성공 기준**: Phase 1 Q&A가 실제 BL 멤버 질문에 정확히 답하는 수준 도달 + Requirements 문서 제출

---

## 📖 모듈별 상세 계획

---

### M1 — GobiSpace Agents 설정 마스터

**난이도**: ⭐
**예상 시간**: 3h
**산출물 폴더**: `01-Agents-Setup/`

> **배경**: 6/23 강민석님으로부터 Changbal 스페이스 어드민 권한 획득. 현재 Bila에는 테스트용 다람쥐 프롬프트가 적용되어 있음. 이번 모듈에서 BL 전용 프롬프트로 교체하고 기본 작동을 검증한다.

#### 학습 목표

- [ ] GobiSpace Agents 탭의 모든 설정 옵션(System Prompt, Language, Vault/GitHub/Drive/Slack 연결)을 이해하고 설명할 수 있다
- [ ] 다람쥐 테스트 프롬프트를 제거하고 Bila AI Agent용 BL 전용 시스템 프롬프트를 적용할 수 있다
- [ ] @mention 트리거와 채팅 대화 두 버전의 프롬프트를 구분해서 설계할 수 있다
- [ ] BL 관련 질문 5개로 응답 품질을 테스트하고 결과를 기록할 수 있다

#### 주요 개념

1. **System Prompt**: 에이전트의 행동, 말투, 역할을 정의하는 지시문. Bila의 "캐릭터"를 만드는 핵심.
2. **@mention 트리거 vs 채팅 대화**: 스페이스 포스트에서 @bila 멘션 시 활성화(mention)와 에이전트와 직접 1:1 채팅(chat)은 컨텍스트와 톤이 달라 별도 프롬프트가 필요.
3. **Language 설정**: 에이전트 응답 언어 고정 (Korean) — 멤버가 다른 언어로 질문해도 한국어로 응답.
4. **CLI vs 웹 UI 한계**: gobi CLI v2.0.35에서 Agent 설정 변경 불가 → 웹 UI Settings 탭 전용.

#### 실습 과제

**실습 1: BL 전용 시스템 프롬프트 설계 및 적용** ⭐
- **목적**: 테스트용 다람쥐 프롬프트를 실제 BL 운영용 프롬프트로 교체
- **단계**:
  1. `system_prompt_mention.md` 원본 읽기 — Changbal 기본 설정 파악
  2. BL 특화 커스터마이징: 역할(Builders Lounge 코디네이터), 지식 범위(BL 기록 기반), 응답 톤(친근하고 실용적)
  3. GobiSpace 웹 UI → Settings → Agents → System Prompt에 적용
  4. 동일하게 채팅 버전(`system_prompt_chat.md` 기반) 작성 및 적용
- **예상 시간**: 60분
- **검증**: Changbal 스페이스에서 @bila 멘션 후 BL 관련 질문 → BL 코디네이터 답변 형식으로 응답

**실습 2: BL 관련 질문 5개로 응답 품질 테스트** ⭐⭐
- **목적**: 프롬프트가 의도한 방향으로 동작하는지 검증
- **단계**:
  1. 테스트 질문 5개 준비:
     - "Builders Lounge가 뭐예요?"
     - "다음 모임 일정이 언제예요?"
     - "BL에서 어떤 프로젝트들이 진행 중인가요?"
     - "백엔드 개발자 멤버 있어요?"
     - "지난 모임에서 어떤 안건이 있었나요?"
  2. 각 질문에 대한 Bila 응답 캡처
  3. 응답 품질 평가 (정확성, 톤, 범위)
  4. 개선 필요 포인트 3개 이상 도출
- **예상 시간**: 60분
- **검증**: 5개 질문 중 3개 이상에서 "BL 코디네이터"답게 응답

#### 산출물

```
01-Agents-Setup/
├── README.md                    ← 모듈 개요 + 학습 순서 안내
├── concepts/
│   └── agents-tab-guide.md     ← GobiSpace Agents 탭 기능 정리
├── guides/
│   ├── system_prompt_BL_mention.md   ← Bila @mention용 커스텀 프롬프트
│   └── system_prompt_BL_chat.md      ← Bila 채팅용 커스텀 프롬프트
└── test-results/
    └── qa-test-20260628.md          ← 5개 Q&A 테스트 결과 기록
```

#### Definition of Done

- [ ] `system_prompt_BL_mention.md` 작성 완료 및 Changbal 스페이스 적용
- [ ] `system_prompt_BL_chat.md` 작성 완료 및 Changbal 스페이스 적용
- [ ] 5개 질문 테스트 완료 및 결과 기록
- [ ] GobiSpace Agents 탭 전체 기능 정리 문서(`agents-tab-guide.md`) 완성
- [ ] 개선 필요 포인트 3개 이상 도출 및 기록
- [ ] WorkLog 작성 + Daily Retrospective 완료

#### Self-Assessment

**개념 이해**:
- [ ] System Prompt가 AI Agent 동작에 어떤 영향을 주는지 다람쥐 실험을 예시로 설명할 수 있다
- [ ] @mention 트리거와 채팅 대화의 차이점을 1-2문장으로 설명할 수 있다

**실무 활용**:
- [ ] 새로운 AI Agent를 위한 시스템 프롬프트 초안을 30분 내에 작성할 수 있다
- [ ] 프롬프트 테스트 결과를 보고 개선 방향을 제시할 수 있다

#### 예상 시간 배분

- 개념 학습 (Agents 탭 기능 파악): 30분
- 실습 1 (프롬프트 설계 및 적용): 60분
- 실습 2 (Q&A 테스트): 60분
- 문서화 + WorkLog: 30분
- **합계**: 3h (버퍼 20% 포함)

#### 참조 자료

- `Materials_For_Topics/Bila_AI_Agent/system_prompt_mention.md`: 강민석님 제공 원본 프롬프트 (@mention)
- `Materials_For_Topics/Bila_AI_Agent/system_prompt_chat.md`: 강민석님 제공 원본 프롬프트 (채팅)
- `Materials_For_Topics/Bila_AI_Agent/gobi_space_settings.md`: GobiSpace Settings 전체 가이드
- `Materials_For_Topics/Bila_AI_Agent/bila_agent_project_plan.md`: 전체 프로젝트 플랜 (Step 1 참조)

---

### M2 — 데이터 소스 연결 & Phase 1 구현

**난이도**: ⭐⭐
**예상 시간**: 4h
**산출물 폴더**: `02-DataSource-Phase1/`

> **배경**: M1에서 시스템 프롬프트를 완성했으나 아직 Bila는 외부 데이터 없이 답하는 상태. M2에서 BL 기록(GitHub 레포 + Google Drive 회의록)을 연결해 진정한 Phase 1 Q&A를 완성한다.

#### 학습 목표

- [ ] GitHub 레포 (`solkit70/builders-lounge-personal-notes`)를 GobiSpace Agents에 연결할 수 있다
- [ ] Google Drive BL 회의록 폴더를 GobiSpace Agents에 연결할 수 있다
- [ ] 데이터 연결 전후 응답 품질 차이를 테스트하고 비교할 수 있다
- [ ] 프롬프트 정제를 반복해 Q&A 정확도를 개선할 수 있다

#### 주요 개념

1. **RAG (Retrieval-Augmented Generation)**: Agent가 외부 데이터(GitHub, Drive)를 검색한 후 그 내용을 기반으로 답변하는 방식. Bila의 "기억"이 여기서 만들어진다.
2. **GitHub 연결 vs Vault 연결**: GitHub는 코드/마크다운 파일 기반 문서, Vault는 GobiSpace 내부 게시물. BL 기록 레포는 GitHub 연결이 적합.
3. **데이터 정제**: 기록의 품질이 Bila의 답변 품질을 결정한다. 파일명, 헤더 구조, 내용 일관성이 중요.
4. **Google Drive 폴더 공유**: Drive 폴더를 GobiSpace와 연결하려면 적절한 공유 권한 설정 필요.

#### 실습 과제

**실습 1: GitHub 레포 연결 및 검증** ⭐⭐
- **목적**: BL 기록 레포를 Bila에 연결해 기록 기반 Q&A 활성화
- **단계**:
  1. GitHub `solkit70/builders-lounge-personal-notes` 레포 현황 확인
  2. GobiSpace Agents 탭 → GitHub 연결 섹션 → 레포 URL 입력
  3. 연결 성공 여부 확인 (오류 시 권한/공개 여부 체크)
  4. 연결 후 "지난 모임 안건" 질문으로 기록 참조 여부 확인
- **예상 시간**: 45분
- **검증**: Bila가 GitHub 레포 내용을 참조한 답변 생성 확인

**실습 2: Google Drive 연결 및 회의록 기반 Q&A** ⭐⭐
- **목적**: 회의록 문서를 Bila가 참조할 수 있도록 Drive 연결
- **단계**:
  1. BL 회의록 폴더를 GobiSpace와 공유 가능한 권한으로 설정
  2. GobiSpace Agents 탭 → Google Drive 연결
  3. 연결 후 "지난 모임에서 결정된 사항" 질문 테스트
- **예상 시간**: 45분
- **검증**: Bila가 Drive 파일 내용을 참조한 답변 생성 확인

**실습 3: Phase 1 최종 검증 — 10개 예상 질문 테스트** ⭐⭐
- **목적**: GitHub + Drive 데이터 기반 Q&A 품질 최종 확인
- **단계**:
  1. BL 멤버가 실제로 물어볼 법한 질문 10개 준비
  2. 각 질문에 대한 Bila 응답 기록
  3. 정확도/적절성 평가 (0-3점 척도)
  4. 개선 포인트 도출 → 프롬프트 정제 1-2회
- **예상 시간**: 90분
- **검증**: 10개 중 7개 이상 적절한 답변 (Phase 1 성공 기준)

#### 산출물

```
02-DataSource-Phase1/
├── README.md                          ← 모듈 개요 + 학습 순서
├── guides/
│   ├── github-connection-guide.md    ← GitHub 연결 방법 + 트러블슈팅
│   └── google-drive-connection-guide.md ← Drive 연결 방법
├── test-results/
│   ├── qa-test-before-data.md        ← 데이터 연결 전 테스트 결과
│   └── qa-test-phase1-final.md       ← Phase 1 최종 10개 질문 결과
└── prompt-iterations/
    └── prompt_v2_after_data.md       ← 데이터 연결 후 개선된 프롬프트
```

#### Definition of Done

- [ ] GitHub 레포 연결 완료 + 기록 참조 답변 확인
- [ ] Google Drive 회의록 폴더 연결 완료
- [ ] Phase 1 최종 테스트: 10개 질문 중 7개 이상 적절한 답변
- [ ] 데이터 연결 전후 비교 문서 작성
- [ ] 개선된 시스템 프롬프트 v2 저장
- [ ] WorkLog 작성 + Daily Retrospective 완료

#### Self-Assessment

**개념 이해**:
- [ ] RAG가 무엇인지 Bila 예시로 설명할 수 있다
- [ ] GitHub 연결과 Vault 연결의 차이를 설명할 수 있다

**실무 활용**:
- [ ] 새로운 데이터 소스를 추가하고 Q&A 품질 변화를 테스트할 수 있다
- [ ] 프롬프트 정제 사이클(테스트 → 분석 → 개선)을 독립적으로 진행할 수 있다

#### 예상 시간 배분

- 개념 학습 (RAG, 연결 방식): 30분
- 실습 1 (GitHub 연결): 45분
- 실습 2 (Drive 연결): 45분
- 실습 3 (Phase 1 최종 테스트): 90분
- 문서화 + WorkLog: 30분
- **합계**: 4h (버퍼 20% 포함)

#### 참조 자료

- `Materials_For_Topics/Bila_AI_Agent/bila_agent_project_plan.md`: Step 2 (데이터 소스 연결) 참조
- CMDS x GOBI Cohort AI (`gobispace.com/spaces/cmds-gobi-1`): 유사 구현 사례

---

### M3 — 채널 구조 & 어드민 워크플로우

**난이도**: ⭐⭐
**예상 시간**: 3h
**산출물 폴더**: `03-Channel-Admin/`

> **배경**: Phase 1 Q&A는 완성됐지만 모임 코디네이터(Phase 3) 역할을 위해서는 어드민 전용 채널과 워크플로우가 필요하다. 현재 자동화 트리거 없이 수동으로 이 흐름을 시뮬레이션해 본다.

#### 학습 목표

- [ ] GobiSpace에서 어드민 전용 채널을 생성하고 권한을 설정할 수 있다
- [ ] 모임 전·중·후 코디네이터 워크플로우를 Bila와 함께 수동으로 시뮬레이션할 수 있다
- [ ] 어드민 전용 채널이 왜 필요한지 기술적으로 설명하고 GOBI 요구사항으로 정리할 수 있다

#### 주요 개념

1. **채널 권한 구조**: Space 전체 공개 채널 vs 특정 멤버만 접근 가능한 채널 — 현재 GobiSpace의 채널 권한 제한 수준 파악.
2. **모임 생애주기 (Meeting Lifecycle)**: 모임 전(안건 공지) → 모임 중(실시간 기록) → 모임 후(회의록 배포 → action item 추적) 전체 흐름.
3. **수동 vs 자동화**: 자동화 트리거가 없는 현재 상황에서 어드민이 수동으로 Bila를 트리거하는 방식.

#### 실습 과제

**실습 1: 어드민 전용 채널 생성 및 설정** ⭐
- **목적**: Bila와 어드민 간 전용 대화 채널 구성
- **단계**:
  1. GobiSpace Settings → Space → 채널 생성
  2. 어드민 멤버(박창수, 강민석님 등)만 접근 가능하도록 설정 시도
  3. 채널 권한 제한 가능 여부 확인 및 문서화
- **예상 시간**: 30분
- **검증**: 어드민 전용 채널 생성 + 권한 설정 결과 기록

**실습 2: 모임 코디네이터 수동 시뮬레이션** ⭐⭐
- **목적**: Bila가 모임 전·중·후를 어떻게 보조할 수 있는지 실제로 경험
- **단계**:
  1. **모임 전**: Bila에게 "다음 BL 모임 안건을 정리하고 공지 초안을 작성해줘" 요청
  2. **모임 중**: 가상 회의록 텍스트를 Bila에게 전달 → "회의록 초안 작성해줘" 요청
  3. **모임 후**: "결정사항 요약하고 다음 action item 리스트 만들어줘" 요청
  4. 각 단계별 Bila 응답 품질 기록
- **예상 시간**: 90분
- **검증**: 3단계 시뮬레이션 완료 + 각 단계 응답 결과 기록

#### 산출물

```
03-Channel-Admin/
├── README.md                             ← 모듈 개요 + 학습 순서
├── concepts/
│   └── meeting-lifecycle.md             ← 모임 생애주기 개념 정리
├── guides/
│   └── admin-channel-setup.md           ← 어드민 채널 생성 가이드
├── simulations/
│   ├── pre-meeting-simulation.md        ← 모임 전 시뮬레이션 결과
│   ├── during-meeting-simulation.md     ← 모임 중 시뮬레이션 결과
│   └── post-meeting-simulation.md       ← 모임 후 시뮬레이션 결과
└── requirements/
    └── admin-channel-requirements.md    ← 어드민 채널 관련 GOBI 요구사항 초안
```

#### Definition of Done

- [ ] 어드민 전용 채널 생성 시도 + 결과(성공/한계) 문서화
- [ ] 모임 전·중·후 시뮬레이션 3단계 완료
- [ ] 각 단계별 Bila 응답 결과 기록 및 품질 평가
- [ ] 어드민 채널 관련 GOBI 요구사항 초안 작성
- [ ] WorkLog 작성 + Daily Retrospective 완료

#### Self-Assessment

**개념 이해**:
- [ ] 모임 생애주기 3단계(전·중·후)에서 Bila의 역할을 각각 설명할 수 있다
- [ ] 어드민 전용 채널이 왜 필요한지 Phase 3 아키텍처 관점에서 설명할 수 있다

**실무 활용**:
- [ ] 수동 시뮬레이션 결과를 보고 자동화가 필요한 지점 3개 이상 도출할 수 있다

#### 예상 시간 배분

- 개념 학습 (채널 구조, Meeting Lifecycle): 30분
- 실습 1 (채널 생성): 30분
- 실습 2 (시뮬레이션 3단계): 90분
- 문서화 + WorkLog: 30분
- **합계**: 3h (버퍼 20% 포함)

#### 참조 자료

- `Materials_For_Topics/Bila_AI_Agent/bila_agent_project_plan.md`: Phase 3 아키텍처 참조 (Section 2)
- `Materials_For_Topics/Bila_AI_Agent/gobi_space_settings.md`: Space 탭 채널 기능

---

### M4 — 한계 분석 & GOBI 요구사항

**난이도**: ⭐⭐⭐
**예상 시간**: 3h
**산출물 폴더**: `04-Limits-Requirements/`

> **배경**: M1~M3를 통해 Phase 1을 구현하고 Phase 3를 시뮬레이션했다. 이제 현재 플랫폼 한계를 체계적으로 정리하고, Phase 2·3 구현을 위해 GOBI 개발자에게 필요한 기능을 요구사항 문서로 제출한다.

#### 학습 목표

- [ ] Phase 2, 3 구현이 현재 불가능한 기술적 이유를 명확히 설명할 수 있다
- [ ] GOBI 개발자 요구사항 문서를 LoFi(기능명, 설명, 필요 이유, 우선순위) 형식으로 작성할 수 있다
- [ ] Phase 1 Q&A의 개선점 3개 이상을 도출하고 개선 계획을 세울 수 있다
- [ ] Topic Retrospective를 작성해 전체 학습 여정을 정리할 수 있다

#### 주요 개념

1. **Cron 트리거**: 시간 기반 자동 실행 (예: 매주 화요일 오전 10시 → Bila가 안건 공지 자동 생성). Phase 2 멤버 매칭의 핵심 요소.
2. **웹훅 트리거 (Webhook)**: 외부 이벤트 기반 실행 (예: Google Meet 종료 → Gemini 노트 → 웹훅 → Bila 활성화). Phase 3의 핵심.
3. **DM 발송 기능**: 특정 멤버에게 직접 메시지 전송 — 멤버 매칭 알림에 필수.
4. **요구사항 명세 작성법**: What(기능명) + Why(필요 이유) + How(구현 방향) + Priority(우선순위)

#### 실습 과제

**실습 1: 현재 기능 한계 체계적 문서화** ⭐⭐
- **목적**: M1~M3 경험 기반으로 플랫폼 한계를 정확히 파악하고 기록
- **단계**:
  1. Phase 2 구현 시도 → Cron 트리거 부재 확인 → 한계 기록
  2. Phase 3 구현 시도 → 웹훅 트리거 부재 확인 → 한계 기록
  3. 어드민 채널 권한 제한 한계 기록
  4. DM 발송 기능 부재 확인 및 기록
  5. M1~M3 실습 중 발견한 기타 한계 모두 기록
- **예상 시간**: 45분
- **검증**: 한계 목록 6개 이상 도출 + 각 한계의 영향 범위 명시

**실습 2: GOBI Requirements 문서 작성 및 제출** ⭐⭐⭐
- **목적**: 강민석님(GOBI 개발자)에게 제출할 공식 요구사항 문서 작성
- **단계**:
  1. `bila_agent_project_plan.md` Section 5의 요구사항 초안 검토
  2. M1~M3 경험을 반영해 보완 및 우선순위 확정
  3. Requirements 문서 최종 작성 (표 형식 + 설명)
  4. gobi CLI 또는 GobiSpace를 통해 강민석님에게 전달
- **예상 시간**: 60분
- **검증**: 요구사항 문서 완성 + 강민석님 전달 완료

**실습 3: Phase 1 회고 및 개선 계획** ⭐
- **목적**: Phase 1 구현 결과를 돌아보고 개선 방향 수립
- **단계**:
  1. M2의 Phase 1 테스트 결과 재검토
  2. 잘된 점, 부족한 점, 개선 방향 정리
  3. 다음 Phase 1 개선 사이클 계획 수립 (프롬프트 v3, 데이터 보강 등)
  4. Topic Retrospective 작성
- **예상 시간**: 45분
- **검증**: 개선 계획 3개 이상 도출 + Topic Retrospective 작성 완료

#### 산출물

```
04-Limits-Requirements/
├── README.md                              ← 모듈 개요 + 학습 순서
├── analysis/
│   └── platform-limits-analysis.md      ← 현재 GobiSpace 한계 분석
├── requirements/
│   └── gobi-requirements-v1.md          ← GOBI 개발자 요구사항 공식 문서
└── phase1-retrospective/
    └── phase1-improvement-plan.md       ← Phase 1 회고 + 개선 계획
```

#### Definition of Done

- [ ] 플랫폼 한계 분석 문서 완성 (최소 6개 한계 항목)
- [ ] GOBI Requirements 문서 v1 완성 (우선순위 포함)
- [ ] 강민석님에게 Requirements 문서 전달 완료
- [ ] Phase 1 회고 + 개선 계획 3개 이상 작성
- [ ] Topic Retrospective 완료
- [ ] WorkLog 작성 + Daily Retrospective 완료

#### Self-Assessment

**개념 이해**:
- [ ] Cron 트리거와 웹훅 트리거의 차이를 실제 Bila 사용 시나리오로 설명할 수 있다
- [ ] GOBI 요구사항 문서의 각 항목(기능명, 이유, 우선순위)을 채울 수 있다

**실무 활용**:
- [ ] 소프트웨어 플랫폼의 한계를 파악하고 개발자에게 요구사항을 전달하는 사이클을 독립적으로 수행할 수 있다
- [ ] Phase 1 결과를 바탕으로 Phase 2 로드맵 초안을 제안할 수 있다

#### 예상 시간 배분

- 실습 1 (한계 분석): 45분
- 실습 2 (Requirements 문서): 60분
- 실습 3 (Phase 1 회고): 45분
- 문서화 + Topic Retrospective: 30분
- **합계**: 3h (버퍼 20% 포함)

#### 참조 자료

- `Materials_For_Topics/Bila_AI_Agent/bila_agent_project_plan.md`: Section 5 (현재 불가능한 기능 & GOBI 요구사항 Draft)
- M1~M3 WorkLog: 실습 중 발견한 한계 사항들

---

## 📝 WorkLog 작성 가이드

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_Bila-AI-Agent.md`
- 예: `vl_worklog/20260628_M1_Bila-AI-Agent.md`

**WorkLog 필수 섹션**:
1. 오늘의 학습 목표 (체크리스트)
2. 진행 내용 (실습별 상세 기록)
3. 문제 해결 로그
4. DoD 체크리스트
5. Daily Retrospective
6. 참조 및 산출물

---

## 🔍 Retrospective 가이드

### Daily Retrospective (매일, 5-10분)

WorkLog 내에 작성:
- What went well? (잘된 점)
- What could be improved? (개선할 점)
- Insights (인사이트)
- Tomorrow's focus (내일 집중할 것)

### Module Retrospective (모듈 완료 시, 15-20분)

`vl_worklog/YYYYMMDD_MX_Retrospective.md`:
- 계획 대비 실제 비교
- 핵심 학습 내용
- 발생한 문제와 해결
- Roadmap 정확도 평가
- 다음 모듈 준비사항

### Topic Retrospective (전체 완료 시, 30-60분)

`vl_worklog/YYYYMMDD_Bila-AI-Agent_Final_Retrospective.md`:
- 전체 학습 여정 통계
- Phase 1 구현 성과 평가
- GOBI 요구사항 제출 결과
- VibeLearn AI 방법론 효과성 평가
- Bila 다음 단계 계획 (Phase 2 waiting for GOBI)

---

## 📂 전체 폴더 구조

```
Topics/Bila-AI-Agent/
├── topic_starter.md
├── vl_prompts/
│   ├── roadmap_prompt.md
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── 20260628_RoadMap_Bila-AI-Agent.md  ← 이 파일
├── vl_worklog/
│   ├── 20260628_M1_Bila-AI-Agent.md
│   ├── 20260628_M2_Bila-AI-Agent.md
│   └── ...
├── vl_materials/
│   └── (Materials_For_Topics/Bila_AI_Agent/ 참조)
├── 01-Agents-Setup/
├── 02-DataSource-Phase1/
├── 03-Channel-Admin/
└── 04-Limits-Requirements/
```

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | 2026-06-28 | 2026-06-28 | ✅ | 6/6 | Live #16 방송 중 완료 |
| M2 | 2026-07-05 | | 🔄 | 3/6 | GitHub 연결·3단 구조 진단 완료, 시스템 프롬프트 단일필드로 정리(v2.2). Drive 연결은 플랫폼 버그(이슈3, 폴더 선택 미저장)로 블로킹 — GOBI 리포트 #2 회신 대기 |
| M3 | | | ⏳ | 0/5 | |
| M4 | | | ⏳ | 0/6 | Requirements 제출이 핵심 |

**범례**: ⏳ 대기 / 🔄 진행 중 / ✅ 완료

---

## 🎯 성공 기준

전체 Topic 완료 기준:
- [ ] 모든 모듈 완료 (DoD 100%)
- [ ] Phase 1 Q&A: 실제 BL 멤버 질문 10개 중 7개 이상 정확 답변
- [ ] GOBI Requirements 문서 v1 강민석님 제출 완료
- [ ] Topic Retrospective 작성 완료
- [ ] 4개 산출물 폴더 생성 완료

---

**생성자**: Claude with VibeLearn AI
**Roadmap 버전**: 1.0
**방법론 버전**: VibeLearn AI 2.0
