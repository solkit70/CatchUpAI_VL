# Remotion 영상 시리즈 Outline

## 제작 범위

이 문서는 Remotion 실제 구현이 아니라 Claude Code에 넘길 영상 기획 산출물이다. 목표는 FDE 학습 Topic을 6편의 짧은 교육 영상 시리즈로 바꾸는 것이다. 각 편은 독립적으로 시청 가능해야 하지만, 전체를 보면 FDE 정의, 기업 모델, 기술 스택, 커리어 전략, 포트폴리오까지 이어지는 curriculum이 되어야 한다.

## 시리즈 콘셉트

**시리즈 제목**: Forward Deployed Engineer: AI 시대의 고객 현장형 엔지니어  
**대상 시청자**: 미국 AI 취업시장에 관심 있는 학생, 개발자, IT 시니어, 비IT 도메인 전문가  
**톤**: 실무적, 커리어 분석 중심, 과장 없는 설명  
**권장 형식**: 6편, 각 5-8분  
**시각 스타일**: dark neutral background, clean enterprise diagrams, role maps, timeline, comparison tables, minimal animation

## 에피소드 구성

| EP | 제목 | 핵심 질문 | 주요 출처 모듈 | 예상 길이 |
|---|---|---|---|---|
| 1 | FDE란 무엇인가 | FDE는 개발자인가, 컨설턴트인가, 영업인가? | M1, M2 | 6분 |
| 2 | Palantir에서 AI FDE까지 | 왜 Palantir식 역할이 AI 시대에 다시 중요해졌나? | M2, M3 | 6분 |
| 3 | OpenAI, Cursor, Scale AI의 FDE는 어떻게 다른가 | 회사별 FDE archetype은 어떻게 나뉘는가? | M3, M6 | 7분 |
| 4 | FDE가 되려면 어떤 기술을 알아야 하나 | AI FDE의 delivery lifecycle과 technical stack은 무엇인가? | M5 | 7분 |
| 5 | 주니어, 시니어, 비IT 배경자의 진입 전략 | 배경별로 어떤 길이 현실적인가? | M7, M8, M9 | 8분 |
| 6 | FDE 포트폴리오와 면접 준비 | 어떤 증거를 만들어야 채용자가 믿는가? | M6, M10 | 8분 |

## 에피소드별 메시지

### EP1 - FDE란 무엇인가

FDE는 고객 현장에서 문제를 발견하고, 제품과 기술을 실제 업무 흐름에 배포하며, 그 과정에서 얻은 field signal을 제품 개선으로 되돌리는 hybrid engineering role이다. 핵심 메시지는 FDE가 단순 demo 담당자나 컨설턴트가 아니라 production adoption을 책임지는 사람이라는 점이다.

### EP2 - Palantir에서 AI FDE까지

Palantir의 원형은 고객 운영 문제를 플랫폼 위에 모델링하고 현장에서 직접 배포하는 방식이었다. AI 시대에는 frontier model, developer tool, data/agent platform이 고객 workflow에 들어가야 하므로 비슷한 forward deployed 접근이 다시 중요해졌다.

### EP3 - 회사별 FDE archetype

OpenAI형은 frontier model을 고객 production workflow에 연결하는 역할, Cursor형은 developer workflow adoption, Scale AI형은 data/agent infrastructure와 public sector deployment, Hebbia형은 vertical knowledge workflow에 가깝다. 시청자는 title보다 job posting의 동사와 성공 지표를 읽어야 한다.

### EP4 - AI FDE 기술 스택

AI FDE에게 필요한 것은 모든 stack을 깊게 아는 것이 아니라 discovery, prototype, eval, integration, rollout 단계에서 필요한 기술 판단을 할 수 있는 것이다. RAG, agentic workflow, evals, observability, security boundary가 핵심이다.

### EP5 - 배경별 진입 전략

주니어는 portfolio proof가 필요하고, IT 시니어는 기존 delivery/customer/stakeholder 경험을 FDE 언어로 번역해야 하며, 비IT 배경자는 FDE 직행보다 domain solution specialist, AI consultant, implementation analyst 같은 인접 경로가 현실적이다.

### EP6 - 포트폴리오와 면접

FDE 포트폴리오는 일반 SWE 포트폴리오와 다르다. customer scenario, architecture, eval, rollout, security boundary, adoption metric이 들어가야 하며, 면접에서는 모호한 고객 요구를 scope와 next experiment로 바꾸는 능력을 보여줘야 한다.

## Claude Code 핸드오프 메모

- 실제 Remotion 구현 시 `video/episode-scripts.md`를 narration source로 사용한다.
- `video/visual-storyboard.md`의 scene id를 Remotion component 단위로 매핑한다.
- M1-M10의 Markdown 문서를 source content로 사용하되, 화면 텍스트는 짧게 압축한다.
- 차트와 표는 한 화면에 모든 정보를 넣지 말고 2-3개 step animation으로 분리한다.

