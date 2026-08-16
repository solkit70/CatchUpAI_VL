# Visual Storyboard for Remotion Handoff

## 공통 제작 지침

이 문서는 Claude Code가 Remotion 영상 제작을 시작하기 위한 장면 설계서다. 실제 구현 시 각 scene id를 React component 또는 composition segment로 매핑한다. 화면 텍스트는 짧게 유지하고, 상세 설명은 narration에 둔다.

권장 visual language:

- 배경: dark neutral 또는 off-white enterprise theme 중 하나 선택
- 색상: role별 accent color 4개 이하
- 주요 시각 요소: timeline, 2x2 map, flowchart, comparison table, architecture diagram
- 화면 밀도: 한 장면에 핵심 메시지 1개
- 모션: fade, slide, highlight, progressive reveal 중심

## EP1 Storyboard

| Scene ID | Visual | On-screen Text | Motion Cue | Source |
|---|---|---|---|---|
| EP1-S1 | 제품팀과 고객 현장 사이에 서 있는 FDE 아이콘 | FDE = Product x Engineering x Customer Field | 세 영역이 중앙으로 합쳐짐 | M1 |
| EP1-S2 | role overlap Venn diagram | Engineer / Consultant / Solutions / Product Signal | FDE 영역 highlight | M1, M4 |
| EP1-S3 | workflow flowchart | Discovery -> Prototype -> Deploy -> Adoption -> Feedback | 단계별 reveal | M5 |
| EP1-S4 | demo vs production comparison | Demo is not adoption | demo card가 production workflow로 변환 | M1 |

## EP2 Storyboard

| Scene ID | Visual | On-screen Text | Motion Cue | Source |
|---|---|---|---|---|
| EP2-S1 | timeline | Palantir Origin -> Enterprise Software -> Generative AI -> AI FDE | timeline sweep | M2 |
| EP2-S2 | Palantir model diagram | Embedded delivery + operational workflow | customer system 위에 platform layer 표시 | M2 |
| EP2-S3 | old vs new comparison | What changed / What did not change | two-column reveal | M2, M3 |
| EP2-S4 | AI adoption gap | Model capability != workflow adoption | gap을 bridge가 연결 | M3 |

## EP3 Storyboard

| Scene ID | Visual | On-screen Text | Motion Cue | Source |
|---|---|---|---|---|
| EP3-S1 | company archetype cards | OpenAI / Cursor / Scale AI / Hebbia | cards enter sequentially | M3 |
| EP3-S2 | 2-axis map | Model/product depth x Customer workflow depth | companies plotted | M3 |
| EP3-S3 | job posting verbs cloud | build, deploy, integrate, evaluate, unblock | relevant verbs brighten | M6 |
| EP3-S4 | candidate fit selector | Which FDE archetype fits you? | checklist fills | M3, M6 |

## EP4 Storyboard

| Scene ID | Visual | On-screen Text | Motion Cue | Source |
|---|---|---|---|---|
| EP4-S1 | lifecycle pipeline | Discovery -> Scoping -> Prototype -> Eval -> Integration -> Rollout | pipeline reveal | M5 |
| EP4-S2 | technical stack layers | Frontend / Backend / Data / LLM / Evals / Security | layers stack upward | M5 |
| EP4-S3 | eval dashboard mock | Quality, latency, cost, risk | metric tiles count up | M5 |
| EP4-S4 | security boundary diagram | Data boundary matters | boundary line protects sensitive data | M5 |

## EP5 Storyboard

| Scene ID | Visual | On-screen Text | Motion Cue | Source |
|---|---|---|---|---|
| EP5-S1 | three path lanes | Junior / IT Senior / Non-IT | lanes appear side by side | M7, M8, M9 |
| EP5-S2 | junior portfolio ladder | Build proof before title | ladder steps fill | M7 |
| EP5-S3 | senior translation table | Delivery experience -> FDE narrative | before/after swap | M8 |
| EP5-S4 | non-IT bridge roles | Domain specialist -> AI consultant -> FDE-adjacent | bridge path draw | M9 |
| EP5-S5 | global context map | US FDE / Korea AX / Japan DX to AX / Europe regulated AI | regions highlight | M9 |

## EP6 Storyboard

| Scene ID | Visual | On-screen Text | Motion Cue | Source |
|---|---|---|---|---|
| EP6-S1 | portfolio package stack | README + Architecture + Eval + Demo + Metrics | documents stack | M10 |
| EP6-S2 | architecture diagram | Customer workflow to AI system | data flow animates | M10 |
| EP6-S3 | demo script timer | 5-minute demo structure | progress bar moves | M10 |
| EP6-S4 | interview loop map | Recruiter -> Technical -> System Design -> Customer Scenario -> Demo | nodes connect | M6, M10 |
| EP6-S5 | final checklist | Can you prove adoption? | checklist completes | M10 |

## Asset List for Claude Code

| Asset | Type | Notes |
|---|---|---|
| Role Venn Diagram | SVG/React component | 4 circles, center FDE |
| FDE Lifecycle Pipeline | React component | reusable in EP1 and EP4 |
| Company Archetype Cards | React component | cards with company labels and archetype |
| Technical Stack Layers | React component | vertical layer diagram |
| Global Context Map | Simple map or region cards | avoid complex geographic detail if asset unavailable |
| Portfolio Package Stack | React component | document cards |
| Interview Loop Map | React component | node-link diagram |

## Implementation Boundary

Codex prepared the content and storyboard only. Claude Code should handle Remotion implementation, visual component coding, timing, subtitles, audio/TTS if needed, and final rendering.

