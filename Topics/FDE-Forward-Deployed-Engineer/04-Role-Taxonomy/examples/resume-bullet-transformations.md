# FDE형 Resume Bullet 변환 예시

## 1. 변환 원칙

FDE형 resume bullet은 단순히 "무엇을 만들었다"가 아니라 다음 구조를 보여줘야 한다.

```
고객/사용자 문제 → 기술적 행동 → 배포/운영 맥락 → 측정 가능한 결과 → 재사용 가능한 학습
```

좋은 bullet은 다음 요소 중 3개 이상을 포함한다.

- 고객 또는 사용자 workflow
- 모호한 문제를 scope한 과정
- 직접 build/integration/deployment한 내용
- production adoption 또는 운영 영향
- metric 또는 measurable outcome
- stakeholder communication
- reusable playbook/component/product feedback

## 2. Software Engineer 출신

### Before

- Built a dashboard for internal users using React and Node.js.

### After

- Scoped and built a React/Node.js operational dashboard with sales operations users, integrating CRM and billing data into a production workflow that reduced manual account review time by 45%.

### 왜 좋아졌나

고객/사용자, integration, production workflow, 측정 가능한 impact가 들어갔다. 단순 기능 개발이 아니라 FDE식 outcome ownership으로 보인다.

## 3. Backend Engineer 출신

### Before

- Developed APIs for data processing service.

### After

- Designed and deployed customer-facing data processing APIs that connected three internal systems, handled 2M+ records/day, and enabled support teams to resolve enterprise customer requests without engineering escalation.

### 왜 좋아졌나

API 개발을 고객 workflow와 operational impact에 연결했다.

## 4. Data Engineer 출신

### Before

- Created ETL pipelines in Airflow and Snowflake.

### After

- Partnered with finance analysts to redesign a fragmented reporting workflow, then built Airflow/Snowflake pipelines that unified five data sources and cut weekly close reporting from two days to four hours.

### 왜 좋아졌나

데이터 파이프라인을 사용자 문제, workflow redesign, business outcome과 연결했다.

## 5. ML Engineer 출신

### Before

- Trained a churn prediction model with 82% accuracy.

### After

- Built and deployed a churn prediction workflow for customer success teams, combining model scoring, CRM integration, and human review so account managers could prioritize at-risk customers before renewal cycles.

### 왜 좋아졌나

모델 accuracy보다 실제 workflow deployment를 강조했다. FDE는 model metric만이 아니라 adoption과 actionability를 본다.

## 6. Solutions Engineer 출신

### Before

- Delivered demos and supported enterprise sales calls.

### After

- Led technical discovery with enterprise prospects, converted ambiguous workflow requirements into working API prototypes, and created reusable demo environments that shortened technical validation cycles by 30%.

### 왜 좋아졌나

pre-sales 경험을 discovery, scoping, prototype, reusable pattern 언어로 바꿨다. 다만 production ownership이 없으면 FDE보다는 FDE-adjacent로 보일 수 있다.

## 7. Consultant 출신

### Before

- Managed digital transformation project for manufacturing client.

### After

- Led workflow discovery for a manufacturing transformation project, mapped operator pain points across planning and production teams, and translated findings into a phased data application roadmap adopted by client engineering leadership.

### 왜 좋아졌나

컨설팅 경험을 FDE가 보는 problem immersion, workflow mapping, technical roadmap 언어로 바꿨다. FDE 지원용으로는 여기에 직접 build한 PoC나 prototype 경험을 추가하면 더 강해진다.

## 8. SI/Implementation Engineer 출신

### Before

- Implemented enterprise software for multiple clients.

### After

- Delivered end-to-end enterprise software deployments across four client environments, customizing integrations, resolving production blockers, and training user teams to reach stable adoption within the first month after launch.

### 왜 좋아졌나

단순 implementation을 production blocker, integration, user adoption까지 확장했다.

## 9. Product Manager 출신

### Before

- Defined requirements for AI chatbot project.

### After

- Drove discovery for an AI support assistant by interviewing support agents, defining escalation and quality metrics, and partnering with engineering to launch a RAG prototype evaluated against 200 historical tickets.

### 왜 좋아졌나

PM 경험을 customer discovery, eval, AI workflow, engineering collaboration으로 바꿨다. 직접 coding이 없다면 FDE보다 Applied AI PM 또는 Deployment Strategist에 가까울 수 있다.

## 10. 비IT 도메인 전문가 출신

### Before

- Worked as a financial analyst and created investment reports.

### After

- Built a repeatable due diligence workflow for investment research, translating analyst review steps into structured prompts, source checklists, and evaluation criteria later used to prototype an AI-assisted research process.

### 왜 좋아졌나

도메인 업무를 AI workflow로 번역한 경험을 보여준다. 비IT 배경자는 "직접 시스템을 만들었다"보다 "업무를 구조화해 AI/engineering team이 구현 가능하게 만들었다"는 증거가 중요하다.

## 11. 강한 FDE bullet 템플릿

### 템플릿 1: 고객 workflow 중심

```
Partnered with {customer/user team} to identify {workflow bottleneck}, then built {technical solution} that {deployment/adoption detail} and improved {metric/result}.
```

### 템플릿 2: AI deployment 중심

```
Designed and deployed {LLM/RAG/agent workflow} integrated with {customer data/system}, using {eval/monitoring method} to achieve {quality/business metric}.
```

### 템플릿 3: field-to-product 중심

```
Converted recurring customer deployment issues into {reusable component/playbook/internal tool}, reducing {delivery friction metric} across {number/type of engagements}.
```

### 템플릿 4: ambiguity handling 중심

```
Scoped an ambiguous {business/operational problem} into {technical roadmap/prototype}, aligning {stakeholders} and shipping {solution} within {timeframe}.
```

## 12. 변환 실습 Worksheet

아래 순서로 본인의 경험 1개를 FDE형 bullet로 바꾼다.

### Step 1: 원래 경험 적기

```
원래 bullet:
-
```

### Step 2: FDE 요소 분해

| 요소 | 내 경험에서 찾을 내용 |
|---|---|
| 고객/사용자 문제 |  |
| 모호했던 요구사항 |  |
| 내가 직접 한 기술적 행동 |  |
| 연결한 시스템/데이터/workflow |  |
| 배포 또는 운영 맥락 |  |
| 측정 가능한 결과 |  |
| 재사용 가능한 학습 또는 product feedback |  |

### Step 3: FDE형 bullet 초안

```
Rewritten bullet:
-
```

### Step 4: 품질 점검

- [ ] 고객 또는 사용자가 명확히 드러난다.
- [ ] 단순 task가 아니라 problem scope가 보인다.
- [ ] 직접 build, integration, deployment 중 하나 이상이 들어간다.
- [ ] 결과가 수치, adoption, 시간 단축, 비용 절감, escalation 감소 중 하나로 표현된다.
- [ ] 가능하면 reusable pattern, playbook, product feedback까지 연결된다.

## 13. 배경별 추천 변환 방향

| 배경 | 강조할 강점 | 보완해야 할 약점 | FDE형 표현 방향 |
|---|---|---|---|
| Software Engineer | build, production quality | 고객 discovery | user workflow와 business outcome을 앞에 둔다. |
| Data/ML Engineer | data, model, eval | adoption과 stakeholder | 모델 성능보다 업무 의사결정으로 연결된 흐름을 강조한다. |
| Solutions Engineer | discovery, demo, technical communication | production ownership | prototype, integration, reusable demo environment를 구체화한다. |
| Consultant | 문제 구조화, change management | coding depth | workflow mapping을 technical roadmap과 PoC로 연결한다. |
| SI/Implementation | deployment, integration, 운영 문제 해결 | product feedback | 반복 문제를 playbook/component로 일반화한 경험을 강조한다. |
| PM/Domain Expert | 사용자 문제, 우선순위, 도메인 | hands-on build | eval criteria, prompt workflow, prototype collaboration을 증거로 만든다. |

## 14. 피해야 할 bullet

| 약한 표현 | 문제 |
|---|---|
| Built an AI chatbot. | 고객 문제, 데이터, 배포, 성과가 없다. |
| Helped with customer meetings. | 책임 범위와 결과가 불명확하다. |
| Used LangChain and OpenAI API. | 기술 나열일 뿐 workflow impact가 없다. |
| Participated in deployment. | ownership이 약하다. |
| Improved productivity. | 어떻게 측정했는지 없다. |

## 15. 자기 평가 질문

- 내 bullet은 "무엇을 만들었는가"보다 "어떤 고객 문제를 어떤 결과로 바꿨는가"를 먼저 보여주는가?
- 기술 이름이 나열되는 데서 끝나지 않고 workflow, deployment, adoption으로 이어지는가?
- FDE 면접관이 이 bullet을 보고 customer-facing engineering 경험을 질문할 수 있는가?
- 수치가 없다면 adoption, 반복 사용, stakeholder decision, escalation 감소 같은 대체 증거가 있는가?

## 16. 결론

FDE형 resume는 기술 목록보다 "고객 문제를 production outcome으로 바꾼 경험"을 보여줘야 한다. 경력이 SWE, data, ML, consulting, SI, PM 어디에서 왔든 discovery, scoping, build, deployment, adoption, feedback의 언어로 재구성하면 FDE 적합성을 더 분명히 전달할 수 있다.
