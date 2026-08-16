# Evals, Security, Observability 체크리스트

## 1. 사용 목적

AI FDE가 prototype을 production deployment로 가져가기 전에 확인해야 할 체크리스트다. 이 문서는 고객 프로젝트 review, portfolio project review, interview case preparation에 사용할 수 있다.

### 체크리스트 사용 원칙

이 문서는 launch 직전 한 번 보는 목록이 아니다. Discovery와 Scoping 단계에서 먼저 위험을 예상하고, Prototype 단계에서 최소한의 관측 지점을 심고, Rollout 단계에서 실제 adoption과 failure를 추적하기 위해 사용한다.

## 2. Evals 체크리스트

### 2.1 Eval 목표

- [ ] AI workflow의 primary task가 명확하다.
- [ ] success metric이 business/workflow outcome과 연결되어 있다.
- [ ] "좋은 답변"의 기준이 domain expert에게 설명 가능하다.
- [ ] unacceptable failure category가 정의되어 있다.

### 2.2 Eval dataset

- [ ] 실제 고객 workflow에서 나온 대표 사례가 포함되어 있다.
- [ ] easy/medium/hard case가 섞여 있다.
- [ ] edge case와 high-risk case가 포함되어 있다.
- [ ] 개인정보/민감정보 처리가 검토되어 있다.
- [ ] regression test에 쓸 golden set이 있다.

### 2.3 평가 방식

- [ ] automatic scoring과 human review의 역할이 나뉘어 있다.
- [ ] retrieval quality를 따로 평가한다.
- [ ] groundedness/source citation을 평가한다.
- [ ] hallucination 또는 unsupported claim을 측정한다.
- [ ] latency와 cost도 평가 항목에 들어간다.

### 2.4 운영 기준

- [ ] launch 전 acceptance threshold가 정해져 있다.
- [ ] model/prompt/tool 변경 시 regression eval을 실행한다.
- [ ] failure taxonomy가 누적된다.
- [ ] 고객 domain expert review process가 있다.
- [ ] eval 결과가 product backlog와 연결된다.

## 3. Security 체크리스트

### 3.1 Identity and Access

- [ ] SSO/SAML/OIDC 요구사항을 확인했다.
- [ ] 사용자 role과 permission이 정의되어 있다.
- [ ] least privilege 원칙을 적용했다.
- [ ] service account와 human user 권한이 분리되어 있다.
- [ ] admin 기능 접근이 제한되어 있다.

### 3.2 Data boundary

- [ ] 어떤 데이터가 model provider로 전송되는지 명확하다.
- [ ] 고객 데이터 retention 정책을 확인했다.
- [ ] PII/PHI/financial data 등 민감 데이터 처리를 확인했다.
- [ ] data residency 요구사항을 확인했다.
- [ ] training use 여부와 opt-out 조건을 확인했다.

### 3.3 Audit and Compliance

- [ ] user action과 AI action이 audit log에 남는다.
- [ ] tool call과 data access가 추적 가능하다.
- [ ] SOC2/GDPR/HIPAA/FedRAMP 등 관련 요구사항을 확인했다.
- [ ] human approval이 필요한 action이 구분되어 있다.
- [ ] incident response contact와 escalation path가 있다.

### 3.4 Prompt and Tool Safety

- [ ] prompt injection risk를 검토했다.
- [ ] retrieval source trust level이 구분되어 있다.
- [ ] tool execution 권한이 제한되어 있다.
- [ ] destructive action에는 human-in-the-loop이 있다.
- [ ] model output이 직접 critical system action을 수행하지 않는다.

## 4. Observability 체크리스트

### 4.1 Logging

- [ ] request/response metadata가 기록된다.
- [ ] prompt version, model version, tool version이 기록된다.
- [ ] retrieval query와 selected source가 기록된다.
- [ ] tool call success/failure가 기록된다.
- [ ] 개인정보가 log에 과도하게 남지 않는다.

### 4.2 Metrics

- [ ] task success rate를 추적한다.
- [ ] user adoption과 active usage를 추적한다.
- [ ] human override 또는 rejection rate를 추적한다.
- [ ] latency p50/p95를 추적한다.
- [ ] cost per task 또는 cost per user를 추적한다.
- [ ] retrieval miss와 tool failure rate를 추적한다.

### 4.3 Debugging

- [ ] 실패 사례를 재현할 수 있다.
- [ ] prompt/model/tool/retrieval 중 실패 원인을 분류할 수 있다.
- [ ] regression test로 재발을 막을 수 있다.
- [ ] support team이 issue를 triage할 runbook이 있다.
- [ ] customer feedback이 issue tracker로 연결된다.

### 4.4 Rollout monitoring

- [ ] pilot group과 control group 또는 baseline이 있다.
- [ ] launch 후 1일/7일/30일 지표를 본다.
- [ ] 사용자 training 완료 여부를 추적한다.
- [ ] critical failure 발생 시 rollback 또는 disable path가 있다.
- [ ] adoption metric이 business sponsor에게 공유된다.

## 5. Cost/Latency Trade-off 체크리스트

- [ ] model 선택 기준이 품질, 비용, latency로 나뉘어 있다.
- [ ] fallback model 또는 degraded mode가 있다.
- [ ] caching 가능성을 검토했다.
- [ ] context size와 retrieval chunk 수가 비용에 미치는 영향을 계산했다.
- [ ] tool call 수와 외부 API latency를 측정했다.
- [ ] streaming 또는 async 처리 필요성을 판단했다.

## 6. Production Readiness Review

아래 항목이 모두 "예"여야 production pilot로 넘어간다.

| 항목 | 질문 | 상태 |
|---|---|---|
| Problem fit | 이 workflow가 AI 적용 가치가 큰가? | 대기 |
| User fit | 실제 target user가 pilot에 포함되어 있는가? | 대기 |
| Data fit | 필요한 데이터가 안정적으로 접근 가능한가? | 대기 |
| Eval fit | launch 기준과 regression 기준이 있는가? | 대기 |
| Security fit | 권한, audit, data boundary가 검토되었는가? | 대기 |
| Observability fit | 실패를 발견하고 디버깅할 수 있는가? | 대기 |
| Support fit | 고객/벤더 ownership과 escalation path가 있는가? | 대기 |
| Business fit | 성공 시 확산 계획과 sponsor가 있는가? | 대기 |

## 7. Mini Case Review

아래 가상 프로젝트에 체크리스트를 적용한다.

**상황**: 고객사는 HR 정책 문서 기반 AI assistant를 만들었다. 데모에서는 질문 20개 중 17개에 그럴듯한 답을 했다. 하지만 아직 SSO가 없고, 문서별 권한은 반영되지 않았으며, 사용자가 틀린 답변을 신고하는 기능도 없다.

### 판정

이 프로젝트는 production pilot로 바로 가면 안 된다. 이유는 모델 답변이 좋아 보이는 것과 enterprise workflow에서 안전하게 운영되는 것은 다르기 때문이다.

| 영역 | 현재 상태 | 필요한 보완 |
|---|---|---|
| Evals | 20개 질문 수동 확인 | 대표/edge/high-risk case가 포함된 eval set과 threshold 필요 |
| Security | SSO 없음, 문서 권한 미반영 | 사용자 role, permission filtering, audit log 필요 |
| Observability | 실패 신고 기능 없음 | feedback capture, trace, failure taxonomy 필요 |
| Rollout | 데모 반응만 확인 | pilot group, training, adoption metric 필요 |
| Support | 운영 owner 불명확 | escalation path와 runbook 필요 |

### 학습자 과제

위 프로젝트가 pilot로 갈 수 있으려면 어떤 최소 조건이 필요한지 5개만 고른다. 이때 "모델 정확도 개선"만 고르면 안 된다. 권한, 관측, 운영, adoption 중 최소 3개 영역을 포함해야 한다.

## 8. Production Readiness 점수표

각 항목을 0-2점으로 평가한다. 0점은 없음, 1점은 부분 준비, 2점은 pilot 가능 수준이다.

| 항목 | 점수 | 판단 근거 |
|---|---:|---|
| Problem fit |  |  |
| User fit |  |  |
| Data fit |  |  |
| Eval fit |  |  |
| Security fit |  |  |
| Observability fit |  |  |
| Support fit |  |  |
| Business fit |  |  |

총점 해석:

| 점수 | 판정 |
|---:|---|
| 0-7 | Demo 단계다. production 논의를 시작하기 이르다. |
| 8-12 | Pilot 후보지만 주요 risk가 남아 있다. |
| 13-16 | 제한된 production pilot를 검토할 수 있다. |

## 9. Interview에서 활용하는 방법

FDE interview case에서 "고객사가 내부 문서 기반 AI assistant를 만들고 싶어 한다"는 문제가 나오면, 바로 솔루션부터 말하지 않는다. 아래 순서로 답하면 FDE다운 판단력이 드러난다.

1. Discovery: 누가 어떤 workflow에서 쓰는지 확인한다.
2. Scoping: MVP와 non-goal을 나눈다.
3. Architecture: data source, identity, retrieval, model, UI, logging을 그린다.
4. Evals: task success, retrieval, groundedness, human review 기준을 만든다.
5. Security: permission, audit, data retention, prompt injection을 검토한다.
6. Rollout: pilot user, training, success metric, support plan을 제시한다.
7. Feedback: 실패 유형을 product backlog와 reusable playbook으로 남긴다.

## 10. 포트폴리오에서 활용하는 방법

FDE 포트폴리오 프로젝트는 기능 화면만 보여주면 약하다. 이 체크리스트를 README에 포함하면 "production을 생각할 줄 아는 후보자"라는 신호를 줄 수 있다.

포트폴리오 README에 넣을 수 있는 섹션:

- Eval design: test case, rubric, acceptance threshold
- Security boundary: 어떤 데이터가 어디로 가고 누가 접근 가능한가
- Observability: 어떤 로그/메트릭으로 실패를 찾는가
- Rollout plan: pilot user, feedback channel, go/no-go 기준
- Known limitations: 아직 production에 부족한 부분

이 방식은 주니어에게도 중요하다. 실제 enterprise production 경험이 없더라도, production readiness를 생각하는 습관을 산출물로 보여줄 수 있기 때문이다.

## 11. 결론

AI FDE가 production 수준으로 일한다는 것은 모델을 연결했다는 뜻이 아니다. 품질을 측정하고, 보안 경계를 지키고, 실패를 관찰하고, 고객 adoption을 추적할 수 있어야 한다. evals, security, observability는 AI FDE의 부가 업무가 아니라 핵심 업무다.
