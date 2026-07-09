# Slack-Builders-Lounge-Automation Roadmap

**생성일**: 2026-07-05 23:21:11  
**방법론**: VibeLearn AI  
**기간**: 1주 또는 8-10시간 집중 연구/개발  
**목표**: Slack `#club-sg-ai` 수동 수집 업무를 Slack API 기반 Markdown 자동화로 전환합니다.

## 학습 기간 적정성 분석

**사용자 입력 기간**: 1주 또는 8-10시간 집중 연구/개발  
**Topic 복잡도**: 중간  
**권장 기간**: 1주

**분석 결과**:
- 적정합니다. Slack API 자체는 좁은 범위지만, 권한/보안/공개 문서화 기준과 실제 Markdown 자동화가 함께 들어가므로 8-10시간을 6개 모듈로 나누는 것이 현실적입니다.
- 실제 Slack token 승인이나 workspace app 설치가 지연되면 API 실호출 검증은 뒤로 밀리고, fixture 기반 개발과 dry-run 검증을 먼저 완료합니다.

**조치**: 사용자가 VibeLearn Topic 생성과 진행을 요청했으므로, 1주/8-10시간 범위로 Roadmap을 확정하고 진행합니다.

## 핵심 기술 Research Notes

Slack 공식 문서 기준으로 `conversations.history`는 채널 히스토리 메시지를 가져오는 기본 API입니다.

> "Fetches a conversation's history of messages and events."

이 Topic에서는 `conversations.history`로 날짜별 메시지 목록을 가져오고, thread가 있는 메시지는 `conversations.replies`로 보강합니다. 작성자 표시는 `users.info` 또는 `users.list`로 user id를 이름으로 매핑하고, GitHub/Obsidian 문서에서 원문 추적이 필요하면 `chat.getPermalink`로 Slack 원문 링크를 보존합니다. Slack 공식 문서에는 2025-05-29 이후 일부 외부 배포 앱의 `conversations.history` rate limit 변경이 명시되어 있으므로, 내부 workspace용 앱인지 Marketplace/상업 배포 앱인지에 따라 요청 간격과 batch 크기를 조정해야 합니다.

## 전체 모듈 구성

| Module | Name | Time | Output |
|---|---:|---:|---|
| M1 | Slack 자동화 범위와 API 접근 방식 확정 | 1.5h | `01-Research-Brief/` |
| M2 | 기존 Markdown 문서 구조 분석과 출력 Schema 설계 | 1.5h | `02-Markdown-Schema/` |
| M3 | Slack API Prototype 설계 및 Fixture 검증 | 2h | `03-API-Prototype/` |
| M4 | 증분 Sync와 Markdown Generator 구현 | 2h | `04-Sync-Automation/` |
| M5 | Review, Redaction, GitHub Publish Flow 설계 | 1h | `05-Review-Publish-Flow/` |
| M6 | Capstone: 로컬 실행 자동화 통합 | 2h | `06-Capstone-Automation/` |

## M1 - Slack 자동화 범위와 API 접근 방식 확정

**난이도**: ⭐⭐  
**예상 시간**: 1.5시간  
**산출물 폴더**: `01-Research-Brief/`

### 학습 목표

- [ ] Slack Web API와 workspace export 방식의 차이를 설명할 수 있습니다.
- [ ] `#club-sg-ai` 자동화에 필요한 Slack scope 후보를 문서화할 수 있습니다.
- [ ] bot token, user token, channel membership, private/public channel 접근 차이를 구분할 수 있습니다.
- [ ] rate limit과 pagination을 고려한 수집 전략을 AI에게 지시할 수 있습니다.

### 주요 개념

- **Slack App**: Slack API를 호출하기 위한 권한 컨테이너입니다. token은 앱 설치와 scope 승인에 의해 발급됩니다.
- **OAuth Scope**: token이 할 수 있는 일을 제한하는 권한입니다. public channel history는 `channels:history`, private channel은 `groups:history`가 관련됩니다.
- **Conversation ID**: Slack API는 채널 이름보다 channel id를 기준으로 동작합니다. `#club-sg-ai`의 실제 channel id를 별도로 확인해야 합니다.
- **Cursor Pagination**: Slack API 응답이 많을 때 `response_metadata.next_cursor`로 다음 페이지를 이어 가져오는 방식입니다.
- **Rate Limit**: 앱 유형과 method별 제한이 다릅니다. 수집 스크립트는 요청 간 sleep과 재시도 처리를 포함해야 합니다.

### 실습 과제

**과제 1: 접근 방식 결정표 작성**  
**목적**: API app, workspace export, no-code automation 중 이 작업에 맞는 방식을 결정합니다.  
**단계**:
1. Slack API 방식의 장단점을 정리합니다.
2. Slack export ZIP 방식의 장단점을 정리합니다.
3. Zapier/Make/Slack Workflow 같은 대안을 비교합니다.
4. 이 Topic의 권장 접근 방식을 1개로 확정합니다.  
**예상 시간**: 35분  
**난이도**: ⭐  
**검증 방법**: `01-Research-Brief/slack-automation-options.md`에 decision table이 생성됩니다.

**과제 2: 권한과 secret checklist 작성**  
**목적**: 실제 개발 전에 필요한 token, scope, channel id, 보안 규칙을 확정합니다.  
**단계**:
1. 필요한 scope 후보를 나열합니다.
2. token을 환경 변수로만 읽는 규칙을 작성합니다.
3. token 없이도 fixture 기반 개발이 가능하도록 fallback 전략을 정리합니다.  
**예상 시간**: 35분  
**난이도**: ⭐⭐  
**검증 방법**: `01-Research-Brief/slack-access-checklist.md`가 생성됩니다.

### 산출물

```text
01-Research-Brief/
  slack-automation-options.md
  slack-access-checklist.md
  slack-api-notes.md
```

### Definition of Done

- [ ] Slack API 방식과 export 방식의 차이를 문서화했습니다.
- [ ] 필요한 scope 후보와 token 종류를 정리했습니다.
- [ ] channel id 확인 방법을 정리했습니다.
- [ ] rate limit과 pagination 주의점을 정리했습니다.
- [ ] M1 WorkLog와 Daily Retrospective를 작성했습니다.

### Self-Assessment

**개념 이해**:
- [ ] Slack App, token, scope, channel id의 관계를 설명할 수 있습니다.
- [ ] `conversations.history`와 `conversations.replies`의 역할을 구분할 수 있습니다.

**실무 활용**:
- [ ] AI에게 Slack API 수집 스크립트의 권한 요구사항을 정확히 지시할 수 있습니다.
- [ ] token을 코드에 하드코딩하면 안 되는 이유를 설명할 수 있습니다.

**문제 해결**:
- [ ] API 호출이 `missing_scope`나 `not_in_channel`로 실패했을 때 확인할 항목을 제시할 수 있습니다.

### 예상 시간 배분

- 개념 학습: 25분
- 실습 1: 35분
- 실습 2: 35분
- WorkLog: 15분
- **합계**: 1.5시간

### 참조 자료

- https://docs.slack.dev/reference/methods/conversations.history/ - channel history 수집 API
- https://docs.slack.dev/reference/methods/conversations.replies/ - thread reply 수집 API
- https://docs.slack.dev/reference/scopes/ - Slack scope reference
- https://slack.com/help/articles/201658943-Export-your-workspace-data - Slack export 대안

## M2 - 기존 Markdown 문서 구조 분석과 출력 Schema 설계

**난이도**: ⭐⭐  
**예상 시간**: 1.5시간  
**산출물 폴더**: `02-Markdown-Schema/`

### 학습 목표

- [ ] 기존 `AI/Initiatives/Builders Lounge/slack/` 문서의 공통 구조를 추출할 수 있습니다.
- [ ] Slack 메시지 JSON을 Markdown frontmatter, 섹션, quote, permalink로 매핑할 수 있습니다.
- [ ] Obsidian과 GitHub에서 모두 읽기 좋은 Markdown 출력 규칙을 정의할 수 있습니다.
- [ ] 날짜별 파일명과 중복 방지 규칙을 설계할 수 있습니다.

### 주요 개념

- **Markdown Schema**: API 응답을 어떤 frontmatter와 본문 구조로 저장할지 정한 규칙입니다.
- **Idempotency**: 같은 메시지를 여러 번 수집해도 중복 문서가 늘어나지 않게 만드는 성질입니다.
- **Permalink**: Slack 원문으로 돌아갈 수 있는 링크입니다. 공개 GitHub 문서에서는 접근 권한이 없는 사람에게는 열리지 않을 수 있습니다.
- **Frontmatter**: Obsidian/GitHub에서 문서 메타데이터를 표현하는 YAML 블록입니다.

### 실습 과제

**과제 1: 기존 문서 구조 샘플링**  
**목적**: 수동으로 정리된 Slack 문서의 실제 패턴을 파악합니다.  
**단계**:
1. 3-5개 기존 Slack 문서를 읽습니다.
2. frontmatter, heading, 메시지 인용, 요약 구조를 비교합니다.
3. 자동 생성 시 반드시 보존할 요소와 생략 가능한 요소를 나눕니다.  
**예상 시간**: 35분  
**난이도**: ⭐  
**검증 방법**: `02-Markdown-Schema/existing-note-patterns.md`가 생성됩니다.

**과제 2: Slack JSON to Markdown mapping 작성**  
**목적**: 구현 전에 변환 규칙을 명확히 합니다.  
**단계**:
1. Slack message 필드와 Markdown 필드를 매핑합니다.
2. thread, attachment, file, reaction 처리 방식을 정합니다.
3. 날짜별 파일명과 message id anchor 규칙을 정합니다.  
**예상 시간**: 40분  
**난이도**: ⭐⭐  
**검증 방법**: `02-Markdown-Schema/slack-to-markdown-schema.md`가 생성됩니다.

### 산출물

```text
02-Markdown-Schema/
  existing-note-patterns.md
  slack-to-markdown-schema.md
  sample-output.md
```

### Definition of Done

- [ ] 기존 Slack 문서 3개 이상을 비교했습니다.
- [ ] Slack JSON field mapping을 작성했습니다.
- [ ] 날짜별 파일명 규칙을 정했습니다.
- [ ] thread와 permalink 처리 규칙을 정했습니다.
- [ ] M2 WorkLog와 Daily Retrospective를 작성했습니다.

### Self-Assessment

**개념 이해**:
- [ ] Slack message JSON의 핵심 필드를 Markdown 구조로 설명할 수 있습니다.
- [ ] idempotent output이 왜 필요한지 설명할 수 있습니다.

**실무 활용**:
- [ ] AI에게 Markdown generator 구현 요구사항을 구체적으로 줄 수 있습니다.
- [ ] GitHub 공유 문서에서 frontmatter 링크와 본문 링크의 차이를 설명할 수 있습니다.

**문제 해결**:
- [ ] thread와 file attachment가 섞인 메시지를 어떻게 표현할지 판단할 수 있습니다.

### 예상 시간 배분

- 개념 학습: 20분
- 실습 1: 35분
- 실습 2: 40분
- 문서화/WorkLog: 15분
- **합계**: 1.5시간

### 참조 자료

- `AI/Initiatives/Builders Lounge/slack/` - 기존 수동 정리 문서
- https://docs.slack.dev/reference/objects/message-object/ - Slack message object
- https://docs.github.com/en/get-started/writing-on-github - GitHub Markdown rendering 참고

## M3 - Slack API Prototype 설계 및 Fixture 검증

**난이도**: ⭐⭐⭐  
**예상 시간**: 2시간  
**산출물 폴더**: `03-API-Prototype/`

### 학습 목표

- [ ] token이 있을 때 `conversations.history` 호출 흐름을 구현할 수 있습니다.
- [ ] token이 없을 때도 redacted fixture로 parser와 generator를 검증할 수 있습니다.
- [ ] thread reply와 user mapping을 별도 단계로 보강하는 구조를 설계할 수 있습니다.
- [ ] Slack API error response를 로그와 troubleshooting 문서로 연결할 수 있습니다.

### 주요 개념

- **Prototype**: 최종 구조를 만들기 전 API 호출과 데이터 형태를 검증하는 작은 구현입니다.
- **Fixture**: 실제 API 응답을 민감 정보 없이 저장한 테스트 샘플입니다.
- **User Mapping**: Slack user id를 표시 이름으로 바꾸는 과정입니다.
- **API Error Taxonomy**: `not_authed`, `invalid_auth`, `missing_scope`, `not_in_channel`, `ratelimited` 같은 오류를 분류하는 방식입니다.

### 실습 과제

**과제 1: Fixture 기반 parser 구현**  
**목적**: token 없이도 데이터 변환 로직을 검증합니다.  
**단계**:
1. redacted Slack response fixture를 만듭니다.
2. messages, thread count, user id, ts를 읽는 parser를 작성합니다.
3. parser output을 JSON으로 저장합니다.  
**예상 시간**: 45분  
**난이도**: ⭐⭐  
**검증 방법**: fixture 입력으로 normalized JSON output이 생성됩니다.

**과제 2: API client skeleton 작성**  
**목적**: 실제 token이 준비되면 바로 호출 가능한 구조를 만듭니다.  
**단계**:
1. `SLACK_BOT_TOKEN` 또는 `SLACK_USER_TOKEN` 환경 변수를 읽습니다.
2. channel id, oldest/latest, cursor, limit 인자를 받습니다.
3. rate limit response를 처리하는 retry 구조를 설계합니다.  
**예상 시간**: 55분  
**난이도**: ⭐⭐⭐  
**검증 방법**: token이 없으면 명확한 안내를 출력하고, fixture mode는 성공합니다.

### 산출물

```text
03-API-Prototype/
  fixtures/
  api-client-notes.md
  normalized-message-sample.json
  troubleshooting.md
```

### Definition of Done

- [ ] redacted fixture를 만들었습니다.
- [ ] fixture parser가 정상 동작합니다.
- [ ] API client skeleton이 token/env var 규칙을 따릅니다.
- [ ] thread/user/permalink 보강 단계가 설계되었습니다.
- [ ] M3 WorkLog와 Daily Retrospective를 작성했습니다.

### Self-Assessment

**개념 이해**:
- [ ] Slack timestamp `ts`가 message id와 ordering에 어떻게 쓰이는지 설명할 수 있습니다.
- [ ] cursor pagination 처리 흐름을 설명할 수 있습니다.

**실무 활용**:
- [ ] AI에게 Slack API client를 안전하게 구현하도록 지시할 수 있습니다.
- [ ] fixture 기반 테스트와 실제 API 테스트를 분리할 수 있습니다.

**문제 해결**:
- [ ] rate limit이나 scope 오류가 발생했을 때 다음 조치를 정할 수 있습니다.

### 예상 시간 배분

- 개념 학습: 25분
- 실습 1: 45분
- 실습 2: 55분
- 문서화/WorkLog: 15분
- **합계**: 2시간

### 참조 자료

- https://docs.slack.dev/apis/web-api/ - Slack Web API 개요
- https://docs.slack.dev/reference/methods/conversations.history/ - history API
- https://docs.slack.dev/reference/methods/users.info/ - user id 상세 정보
- https://docs.slack.dev/reference/methods/chat.getPermalink/ - Slack permalink 생성

## M4 - 증분 Sync와 Markdown Generator 구현

**난이도**: ⭐⭐⭐  
**예상 시간**: 2시간  
**산출물 폴더**: `04-Sync-Automation/`

### 학습 목표

- [ ] 마지막 수집 시각을 저장하고 다음 실행에서 이어 가져오는 구조를 구현할 수 있습니다.
- [ ] normalized Slack messages를 날짜별 Markdown 문서로 변환할 수 있습니다.
- [ ] 동일 메시지 재수집 시 중복을 만들지 않는 idempotent write 방식을 설계할 수 있습니다.
- [ ] dry-run, fixture-run, real-run mode를 구분할 수 있습니다.

### 주요 개념

- **State File**: 마지막 수집 timestamp, channel id, 실행 결과를 저장하는 파일입니다.
- **Incremental Sync**: 전체를 매번 가져오지 않고 마지막 실행 이후의 메시지만 가져오는 방식입니다.
- **Dry Run**: 파일을 실제로 쓰지 않고 어떤 변경이 생길지 보여주는 실행 모드입니다.
- **Atomic Write**: 파일 손상을 줄이기 위해 임시 파일 작성 후 교체하는 방식입니다.

### 실습 과제

**과제 1: State format 설계와 구현**  
**목적**: 반복 실행 가능한 수집기를 만듭니다.  
**단계**:
1. state JSON schema를 정합니다.
2. load/save 함수를 작성합니다.
3. 실패 시 state를 갱신하지 않는 규칙을 구현합니다.  
**예상 시간**: 40분  
**난이도**: ⭐⭐  
**검증 방법**: sample state를 읽고 저장할 수 있습니다.

**과제 2: Markdown generator 구현**  
**목적**: 실제 Vault 문서 형식의 결과물을 만듭니다.  
**단계**:
1. 날짜별 group을 만듭니다.
2. frontmatter와 본문 섹션을 생성합니다.
3. message ts 기반 anchor 또는 원문 링크를 포함합니다.
4. dry-run에서 생성 예정 파일 목록을 출력합니다.  
**예상 시간**: 65분  
**난이도**: ⭐⭐⭐  
**검증 방법**: fixture 입력으로 Markdown sample output이 생성됩니다.

### 산출물

```text
04-Sync-Automation/
  state-schema.md
  markdown-generator-notes.md
  sample-generated/
```

### Definition of Done

- [ ] state schema가 문서화되었습니다.
- [ ] dry-run/fixture-run/real-run mode가 정의되었습니다.
- [ ] Markdown generator가 sample output을 만듭니다.
- [ ] 중복 방지 기준이 정리되었습니다.
- [ ] M4 WorkLog와 Daily Retrospective를 작성했습니다.

### Self-Assessment

**개념 이해**:
- [ ] incremental sync와 full refresh의 차이를 설명할 수 있습니다.
- [ ] idempotent write가 필요한 이유를 설명할 수 있습니다.

**실무 활용**:
- [ ] AI에게 stateful sync script 구현을 구체적으로 요청할 수 있습니다.
- [ ] dry-run 결과를 보고 실제 적용 여부를 판단할 수 있습니다.

**문제 해결**:
- [ ] 중간 실패 후 다음 실행에서 데이터 누락이 생기지 않도록 조치할 수 있습니다.

### 예상 시간 배분

- 개념 학습: 20분
- 실습 1: 40분
- 실습 2: 65분
- 문서화/WorkLog: 15분
- **합계**: 2시간

### 참조 자료

- https://docs.slack.dev/reference/methods/conversations.history/ - `oldest`, `latest`, cursor pagination 참고
- Python `json` and `pathlib` standard library documentation - state and file handling
- Existing folder: `AI/Initiatives/Builders Lounge/slack/`

## M5 - Review, Redaction, GitHub Publish Flow 설계

**난이도**: ⭐⭐  
**예상 시간**: 1시간  
**산출물 폴더**: `05-Review-Publish-Flow/`

### 학습 목표

- [ ] Slack 메시지에서 공개 문서에 포함하면 안 되는 정보 유형을 분류할 수 있습니다.
- [ ] redaction rule과 manual review checkpoint를 설계할 수 있습니다.
- [ ] GitHub 공유 전 변경 파일 검토 절차를 자동화 흐름에 포함할 수 있습니다.
- [ ] Slack 원문 링크가 GitHub 독자에게 어떤 의미를 갖는지 설명할 수 있습니다.

### 주요 개념

- **Redaction**: 이메일, 전화번호, private URL, token, 초대 링크 같은 민감 정보를 제거하거나 대체하는 처리입니다.
- **Review Gate**: 자동 생성 후 바로 publish하지 않고 사람이 확인하는 단계입니다.
- **Public Context**: GitHub 독자가 Slack workspace에 없더라도 이해할 수 있도록 필요한 맥락을 보강하는 기준입니다.
- **Audit Trail**: 어떤 날짜의 Slack 메시지를 언제 수집했는지 추적하는 기록입니다.

### 실습 과제

**과제 1: Redaction checklist 작성**  
**목적**: 자동화가 공개 리스크를 만들지 않게 합니다.  
**단계**:
1. 민감 정보 유형을 나열합니다.
2. 자동 redaction 가능 항목과 수동 검토 항목을 구분합니다.
3. Markdown generator에 들어갈 warning/comment 규칙을 정합니다.  
**예상 시간**: 30분  
**난이도**: ⭐⭐  
**검증 방법**: `05-Review-Publish-Flow/redaction-checklist.md`가 생성됩니다.

**과제 2: Publish workflow 작성**  
**목적**: 생성된 문서를 GitHub에 공유하기 전 검토 절차를 확정합니다.  
**단계**:
1. sync 실행 후 확인할 diff 항목을 정합니다.
2. approve 후 commit/push하는 순서를 정합니다.
3. 실패/보류 시 state 처리 규칙을 정합니다.  
**예상 시간**: 25분  
**난이도**: ⭐  
**검증 방법**: `05-Review-Publish-Flow/publish-workflow.md`가 생성됩니다.

### 산출물

```text
05-Review-Publish-Flow/
  redaction-checklist.md
  publish-workflow.md
  risk-log.md
```

### Definition of Done

- [ ] 민감 정보 유형을 정리했습니다.
- [ ] 자동 redaction과 수동 review 기준을 구분했습니다.
- [ ] GitHub publish 전 diff 확인 절차를 정의했습니다.
- [ ] Slack permalink 공개 의미를 문서화했습니다.
- [ ] M5 WorkLog와 Daily Retrospective를 작성했습니다.

### Self-Assessment

**개념 이해**:
- [ ] private Slack content를 public Markdown으로 바꿀 때의 리스크를 설명할 수 있습니다.
- [ ] review gate가 자동화 속도를 늦추더라도 필요한 이유를 설명할 수 있습니다.

**실무 활용**:
- [ ] AI에게 redaction rule 구현을 지시할 수 있습니다.
- [ ] 생성된 Markdown을 publish해도 되는지 판단할 수 있습니다.

**문제 해결**:
- [ ] 민감 정보가 발견되었을 때 state와 output을 어떻게 처리할지 정할 수 있습니다.

### 예상 시간 배분

- 개념 학습: 10분
- 실습 1: 30분
- 실습 2: 25분
- WorkLog: 10분
- **합계**: 1시간

### 참조 자료

- Existing publish target: `AI/Initiatives/Builders Lounge/`
- Slack API file and permalink behavior documentation
- Git diff workflow in the local Builders Lounge sharing process

## M6 - Capstone: 로컬 실행 자동화 통합

**난이도**: ⭐⭐⭐  
**예상 시간**: 2시간  
**산출물 폴더**: `06-Capstone-Automation/`

### 학습 목표

- [ ] 연구 산출물과 prototype을 하나의 실행 가능한 sync 흐름으로 통합할 수 있습니다.
- [ ] 환경 변수, config, state, output path를 분리한 실행 방식을 만들 수 있습니다.
- [ ] fixture test와 real API run을 같은 CLI에서 선택할 수 있습니다.
- [ ] 다음에 AI에게 유지보수/확장 작업을 지시할 수 있는 운영 문서를 만들 수 있습니다.

### 주요 개념

- **CLI Entry Point**: 자동화 스크립트를 사람이 반복 실행할 수 있게 하는 명령 인터페이스입니다.
- **Configuration Separation**: token, channel id, output path, state path를 코드에서 분리하는 설계입니다.
- **Operational Runbook**: 실행, 검토, 문제 해결, publish 절차를 한 문서로 정리한 운영 가이드입니다.
- **Capstone**: 학습한 개념을 실제 업무 자동화 산출물로 합치는 최종 실습입니다.

### 실습 과제

**과제 1: 통합 sync command 만들기**  
**목적**: 실제 업무에 사용할 수 있는 실행 단위를 완성합니다.  
**단계**:
1. config와 environment variable 읽기 구조를 확정합니다.
2. fixture mode, dry-run mode, real mode를 하나의 CLI로 묶습니다.
3. output path를 `AI/Initiatives/Builders Lounge/slack/`로 지정할 수 있게 합니다.
4. 실행 결과 summary를 콘솔에 출력합니다.  
**예상 시간**: 75분  
**난이도**: ⭐⭐⭐  
**검증 방법**: fixture mode에서 Markdown output이 생성되고 dry-run summary가 출력됩니다.

**과제 2: Runbook과 next automation plan 작성**  
**목적**: 이후 반복 실행과 유지보수를 가능하게 합니다.  
**단계**:
1. Slack app/token 준비 절차를 정리합니다.
2. sync 실행, review, commit/push 순서를 정리합니다.
3. Windows Task Scheduler 또는 수동 주간 실행 후보를 정리합니다.
4. 향후 thread/file/reaction 확장 계획을 적습니다.  
**예상 시간**: 35분  
**난이도**: ⭐⭐  
**검증 방법**: `06-Capstone-Automation/runbook.md`가 생성됩니다.

### 산출물

```text
06-Capstone-Automation/
  runbook.md
  config-example.json
  test-results.md
```

최종 개발 산출물의 실제 위치는 M6에서 확정합니다. 후보는 Topic 내부 prototype 유지, `_Settings_/Scripts/` 배치, 또는 Builders Lounge 전용 하위 폴더 배치입니다. 공개 GitHub 공유 대상에 포함할지 여부는 review/publish 기준을 먼저 확인한 뒤 결정합니다.

### Definition of Done

- [ ] fixture mode sync가 성공합니다.
- [ ] dry-run mode가 변경 예정 파일을 보여줍니다.
- [ ] real mode 실행 조건과 token 준비 절차가 문서화되었습니다.
- [ ] output path와 state path가 config로 분리되었습니다.
- [ ] runbook이 작성되었습니다.
- [ ] M6 WorkLog와 final retrospective를 작성했습니다.

### Self-Assessment

**개념 이해**:
- [ ] 전체 Slack-to-Markdown sync flow를 5단계 이하로 설명할 수 있습니다.
- [ ] 어떤 부분을 Slack API, 어떤 부분을 local Markdown generator가 담당하는지 구분할 수 있습니다.

**실무 활용**:
- [ ] AI에게 이 자동화의 유지보수 또는 기능 확장을 지시할 수 있습니다.
- [ ] 실제 token이 준비되었을 때 어떤 명령으로 검증할지 설명할 수 있습니다.

**문제 해결**:
- [ ] API 실패, 중복 출력, redaction 실패, publish 보류 상황별 대응을 정리할 수 있습니다.

### 예상 시간 배분

- 개념 정리: 15분
- 실습 1: 75분
- 실습 2: 35분
- final retrospective: 15분
- **합계**: 2시간

### 참조 자료

- M1-M5 산출물 전체
- Slack Web API official docs
- Existing output folder: `AI/Initiatives/Builders Lounge/slack/`

## WorkLog 작성 가이드

각 daily learning 세션은 `vl_worklog/YYYYMMDD_MX_Slack-Builders-Lounge-Automation.md` 형식으로 작성합니다. WorkLog에는 오늘 목표, 완료한 작업, 생성한 파일, DoD 진행률, 문제와 해결, Tomorrow's focus를 포함합니다. 생성한 코드나 문서가 있다면 반드시 상대 경로로 기록합니다.

## Retrospective 가이드

각 세션 끝에는 다음 질문에 답합니다.

- 오늘 Slack 자동화에 대해 새로 이해한 핵심 개념은 무엇입니까?
- AI에게 다음 개발 지시를 내린다면 어떤 요구사항을 더 명확히 말할 수 있습니까?
- 실제 업무 자동화 관점에서 아직 막힌 부분은 무엇입니까?
- GitHub 공개 공유 전에 확인해야 할 리스크가 남아 있습니까?

## 권장 폴더 구조

```text
Slack-Builders-Lounge-Automation/
  topic_info.md
  topic_starter.md
  01-Research-Brief/
  02-Markdown-Schema/
  03-API-Prototype/
  04-Sync-Automation/
  05-Review-Publish-Flow/
  06-Capstone-Automation/
  vl_materials/
  vl_prompts/
    roadmap_prompt.md
    daily_learning_prompt.md
  vl_roadmap/
    20260705_RoadMap_Slack-Builders-Lounge-Automation.md
  vl_worklog/
```

## Progress Table

| Module | Status | DoD | WorkLog |
|---|---|---:|---|
| M1 | Not Started | 0/5 | - |
| M2 | Not Started | 0/5 | - |
| M3 | Not Started | 0/5 | - |
| M4 | Not Started | 0/5 | - |
| M5 | Not Started | 0/5 | - |
| M6 | Not Started | 0/6 | - |

## Success Criteria

- Slack API와 workspace export 중 왜 API 방식을 우선하는지 설명할 수 있습니다.
- `#club-sg-ai` 메시지 수집에 필요한 token, scope, channel id, pagination, rate limit 조건을 AI에게 지시할 수 있습니다.
- fixture 기반으로 Slack message를 Markdown으로 변환하는 자동화가 동작합니다.
- 실제 token이 준비되면 같은 구조에서 real sync를 실행할 수 있습니다.
- 생성된 Markdown은 기존 Builders Lounge Slack 문서와 호환됩니다.
- GitHub 공개 전 review/redaction 절차가 자동화 흐름에 포함됩니다.
