# 2026-08-16 M10 WorkLog - 포트폴리오와 Remotion 영상화 Capstone

## 오늘의 학습 목표

- VibeLearn AI daily learning 절차에 따라 사용자 승인 후 M10을 진행한다.
- FDE 지망자를 위한 최종 포트폴리오 가이드 패키지를 구성한다.
- FDE 포트폴리오 프로젝트 3개 spec을 customer scenario, architecture, eval, rollout, metric 중심으로 작성한다.
- Remotion 실제 제작 전 단계의 6편 영상 outline, episode script, visual storyboard를 작성한다.

## 진행 내용

### 1. Roadmap 및 이전 WorkLog 확인

M9 WorkLog의 Tomorrow's Focus를 확인했다. 다음 작업은 M10에서 포트폴리오와 Remotion 영상화 Capstone을 작성하는 것이었다. 사용자는 마지막 Remotion 실제 영상 제작은 Claude Code에게 맡길 예정이라고 명시했으므로, 이번 세션은 영상 제작 전 기획/핸드오프 문서까지로 범위를 제한했다.

### 2. M10 산출물 폴더 생성

`10-Capstone-Video/` 폴더와 하위 `guides/`, `examples/`, `video/` 폴더를 생성했다. 로드맵 산출물 구조에 맞춰 README, FDE 포트폴리오 가이드, 면접 준비 문서, 포트폴리오 프로젝트 spec, Remotion 영상 outline, episode scripts, visual storyboard를 작성했다.

### 3. 포트폴리오 가이드 및 프로젝트 spec 작성

`guides/fde-portfolio-guide.md`에는 FDE 포트폴리오가 일반 SWE 포트폴리오와 다른 점을 정리했다. `examples/portfolio-project-specs.md`에는 Enterprise Policy RAG Assistant, Customer Support Triage Agent, Regulated Workflow Review Copilot의 3개 프로젝트를 customer scenario, architecture, stack, eval, rollout, success metric 기준으로 설계했다.

### 4. 면접 준비 문서 작성

`guides/fde-interview-prep.md`에는 FDE 지원자 최종 가이드 패키지 목차와 면접 루프별 준비 전략을 작성했다. recruiter screen, hiring manager, technical screen, system design, customer scenario, portfolio demo, executive/bar raiser 면접에서 어떤 역량을 보여줘야 하는지 정리했다.

### 5. Remotion 핸드오프 문서 작성

`video/remotion-series-outline.md`에는 6편 영상 시리즈의 제목, 핵심 질문, 주요 출처 모듈, 에피소드별 메시지를 작성했다. `video/episode-scripts.md`에는 각 편의 30초 hook, narration flow, closing line을 작성했다. `video/visual-storyboard.md`에는 scene id, visual, on-screen text, motion cue, source module을 연결하여 Claude Code가 Remotion 구현을 이어받을 수 있게 했다.

## 문제 해결 로그

- 문제: M10 로드맵에는 Remotion 영상화가 포함되어 있지만, 사용자는 실제 Remotion 제작을 Claude Code에게 맡기겠다고 했다.
- 해결: 이번 세션 범위를 Remotion 구현 전 단계로 제한했다. Codex는 outline, script, storyboard, asset list, implementation boundary를 작성했고, 실제 Remotion 프로젝트 생성과 렌더링은 수행하지 않았다.

## DoD 체크리스트

- [x] 포트폴리오 프로젝트 3개 spec 작성
- [x] FDE 지원자 최종 가이드 패키지 목차 작성
- [x] Remotion 영상 6편 outline 작성
- [x] episode script 초안 작성
- [x] visual storyboard 작성
- [x] README 업데이트
- [x] Topic Retrospective 작성

## Daily Retrospective

### 오늘 배운 것

FDE Topic의 최종 산출물은 단순 요약보다 재사용 가능한 지원자 패키지와 영상 제작 입력물로 만드는 것이 더 가치 있다. 특히 포트폴리오는 코드보다 customer scenario, architecture, eval, rollout, adoption metric이 중심이어야 한다.

### 잘한 점

Remotion 실제 제작을 하지 않는다는 사용자 제약을 명확히 반영했다. 영상 outline, scripts, storyboard를 분리해 Claude Code가 다음 단계에서 구현 단위로 가져갈 수 있도록 만들었다.

### 개선할 점

Claude Code가 실제 Remotion 작업을 시작할 때는 영상 톤, 자막 언어, TTS 사용 여부, 에피소드별 길이, visual theme을 추가로 확정해야 한다. 또한 각 에피소드의 화면 텍스트는 구현 단계에서 더 짧게 다듬어야 한다.

### Tomorrow's Focus

- Claude Code에게 `10-Capstone-Video/video/` 문서 3개를 전달해 Remotion 제작을 시작한다.
- 필요하면 Topic Retrospective를 별도 문서로 확장한다.
- FDE 전체 Topic 산출물을 웹/영상/포트폴리오 패키지로 재배치할지 결정한다.

## 참조 및 산출물

- `10-Capstone-Video/README.md`
- `10-Capstone-Video/guides/fde-portfolio-guide.md`
- `10-Capstone-Video/guides/fde-interview-prep.md`
- `10-Capstone-Video/examples/portfolio-project-specs.md`
- `10-Capstone-Video/video/remotion-series-outline.md`
- `10-Capstone-Video/video/episode-scripts.md`
- `10-Capstone-Video/video/visual-storyboard.md`
- `06-US-Job-Market/guides/fde-interview-loop-guide.md`
- `07-Junior-Track/guides/six-month-plan.md`
- `08-Senior-Transition/guides/senior-transition-map.md`
- `09-Non-IT-Global-Context/guides/non-it-entry-path.md`

