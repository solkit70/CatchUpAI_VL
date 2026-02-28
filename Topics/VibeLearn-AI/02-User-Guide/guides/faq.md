# VibeLearn AI — FAQ & 트러블슈팅

**작성일**: 2026-02-26
**대상**: VibeLearn AI를 처음 사용하거나 막힌 부분이 있는 사람

---

## 자주 묻는 질문 (FAQ)

---

### Q1. AI가 없으면 사용할 수 없나요?

**A**: 맞습니다. AI는 VibeLearn AI의 필수 요소입니다.

이유:
- Roadmap 생성: AI가 Topic 정보를 분석하여 맞춤 계획 수립
- Daily Learning: AI가 Roadmap+WorkLog를 읽고 오늘의 계획 수립
- 실시간 학습 지원: 막힐 때 즉시 질문 → 즉각 답변

**권장 AI 도구** (파일을 직접 읽고 쓸 수 있는 것):
- **VS Code + GitHub Copilot** — 가장 보편적, VS Code에 Copilot 확장 설치
- **VS Code + Claude Code** (Extension) — Claude 기반, 강력한 파일 조작 능력
- **Cursor** — AI 통합 에디터 (VS Code 기반)

> 웹 기반 AI(ChatGPT 웹, Claude.ai)는 파일을 직접 읽고 쓸 수 없어서 복사/붙여넣기가 필요하고 비효율적입니다.

---

### Q2. GitHub 없이도 사용할 수 있나요?

**A**: 네, 가능합니다. GitHub는 선택 사항입니다.

GitHub 없이:
- 로컬 폴더에서 모든 작업 진행 가능
- WorkLog, 산출물 모두 로컬에 저장
- 단, 백업 및 공유 기능 없음

GitHub 있으면:
- 버전 관리 (실수해도 되돌리기 가능)
- 산출물 공유 및 커뮤니티 기여
- 다른 기기에서 접근 가능

**추천**: GitHub를 처음 써본다면 이 Topic 학습 중에 GitHub 기초도 함께 배워보세요.

---

### Q3. 어떤 주제에도 쓸 수 있나요?

**A**: 네. 기술적 주제뿐 아니라 어떤 분야에도 적용 가능합니다.

잘 맞는 주제:
- 프로그래밍 언어 (Python, JavaScript 등)
- 프레임워크 & 도구 (React, Docker, Git 등)
- AI/ML 도구 (Claude API, LangChain 등)
- 비기술 분야 (영어 쓰기, 재무 계획, 요리 기술 등)

핵심: 배우고 싶고, 체계적으로 접근하고 싶은 모든 것에 적용 가능

---

### Q4. 학습 기간을 어떻게 정해야 하나요?

**A**: 정하지 않아도 됩니다. AI가 대화를 통해 자동으로 파악합니다.

프로세스:
1. "Python 기초를 배우고 싶어." → AI가 학습 배경을 질문
2. AI가 적정 기간을 제안하며 확인 요청
3. "너무 짧음/적정함/너무 긺" 피드백 제공
4. 사용자가 최종 결정

참고 기준:
- 간단한 Tool 사용법: 3-7일
- 프레임워크/라이브러리: 2-4주
- 복잡한 시스템: 1-3개월

---

### Q5. templates/ 폴더의 파일을 수정해도 되나요?

**A**: 수정하지 않는 것을 강력 권장합니다.

이유:
- templates/는 "범용 원본" — 어떤 Topic에도 재사용
- 수정하면 다음 Topic 시작 시 깨진 템플릿으로 시작하게 됨

대안:
- 수정이 필요하면 `vl_prompts/` 폴더의 복사본을 수정
- templates/는 항상 원본 상태 유지

---

### Q6. WorkLog를 꼭 매일 써야 하나요?

**A**: 학습한 날마다 쓰는 것이 강력 권장입니다.

쓰지 않으면:
- 다음 세션에서 AI가 이전 진도를 파악하지 못함
- 같은 내용을 반복 학습하게 될 가능성 높음
- Daily Retrospective가 없어서 학습 방법이 개선되지 않음

쓰는 방법:
- AI가 자동으로 WorkLog 파일을 생성하고 채워줍니다
- 직접 수정하고 싶으면 파일을 열어서 추가하면 됩니다

---

### Q7. 여러 Topic을 동시에 학습할 수 있나요?

**A**: 기술적으로는 가능하지만, 권장하지 않습니다.

이유:
- 한 Topic에 집중하면 깊이 있는 학습 가능
- 여러 Topic을 병행하면 각각의 DoD 달성이 어려워짐
- AI도 여러 Topic의 맥락을 동시에 관리하기 어려움

예외:
- 서로 보완적인 두 Topic (예: Python + Docker)은 병행 가능
- 단, 각 Topic은 별도 대화 세션에서 진행

---

### Q8. 산출물 폴더의 내용을 다른 사람과 공유하면 안 되나요?

**A**: 공유하는 것이 VibeLearn AI의 핵심 목적입니다!

공유 방법:
1. GitHub에 공개 저장소로 올리기
2. 블로그/노션에 문서 공유
3. YouTube 영상으로 학습 과정 공유 (Clearly 케이스처럼)

주의:
- 개인 정보가 포함된 WorkLog는 공유 전 검토
- API 키, 비밀번호 등 민감 정보가 없는지 확인

---

### Q9. AI가 만든 Roadmap이 너무 어렵거나 쉬워요. 어떻게 하나요?

**A**: Roadmap은 수정 가능합니다.

방법:
1. Roadmap 파일을 열어서 직접 수정
2. AI에게 "M2가 너무 어려운데 쉽게 조정해줘" 요청
3. 모듈을 분리하거나 합치기

중요:
- Roadmap은 출발점이지 절대적 계획이 아닙니다
- 학습하면서 조정하는 것이 자연스럽습니다

---

### Q10. Daily Retrospective를 건너뛰면 안 되나요?

**A**: 건너뛰면 학습의 핵심 가치가 줄어듭니다.

이유:
- Retrospective는 학습 방법 자체를 개선하는 메타 학습
- "오늘 왜 잘 됐나?", "왜 막혔나?" → 다음 세션이 더 효율적
- Clearly 케이스에서 "반복의 힘" 발견도 Retrospective 덕분

최소 5분은 투자:
```markdown
## Daily Retrospective
- What went well? (한 줄)
- What could be improved? (한 줄)
- Tomorrow's focus (한 줄)
```

---

### Q11. 영어로 진행하고 싶어요.

**A**: 완전 지원합니다.

방법:
1. `templates/*.en.md` 파일 사용 (영어 버전 템플릿)
2. AI에게 "영어로 진행하겠습니다" 명시
3. WorkLog, 산출물 모두 영어로 작성

모든 템플릿의 영어 버전:
- `templates/roadmap_prompt_template.en.md`
- `templates/daily_learning_prompt.en.md`
- `templates/topic_starter.en.md`

---

### Q12. 학습 중에 원본 기술/소프트웨어가 업데이트되면 어떻게 하나요?

**A**: CVL(Continuous Vibe Learning) 프로세스를 따르세요.

방법:
1. 매 학습 세션 시작 시 `git fetch` 확인
2. 변경사항 분석 (AI에게 요청)
3. 규모에 따라 즉시 반영 또는 별도 업데이트 세션 진행
4. WorkLog에 동기화 내용 기록

상세 가이드: [key-concepts.md](../../01-System-Overview/concepts/key-concepts.md)의 CVL 섹션 참조

---

## 트러블슈팅

---

### 문제 1: AI가 폴더를 만들어주지 않아요

**원인**: AI 도구가 파일 시스템 접근 권한이 없음

**해결**:
```bash
# Windows PowerShell
$topic = "Python-Basics"
mkdir "Topics/$topic/vl_prompts", "Topics/$topic/vl_roadmap", "Topics/$topic/vl_worklog", "Topics/$topic/vl_materials" -Force

# macOS/Linux Bash
topic="Python-Basics"
mkdir -p "Topics/$topic"/{vl_prompts,vl_roadmap,vl_worklog,vl_materials}
```

---

### 문제 2: Roadmap 파일이 너무 길어요

**원인**: 정상입니다. Roadmap은 전체 학습 계획이므로 길 수 있음

**해결**:
- 현재 모듈 섹션만 열어두기
- AI에게 "M1 부분만 요약해줘" 요청
- VS Code의 코드 폴딩(접기) 기능 활용

---

### 문제 3: WorkLog가 계속 사라져요 (AI가 새로 만들어요)

**원인**: 날짜별로 새 파일을 만드는 설계 — 정상 동작

**해결**:
- 같은 날 같은 모듈이면 기존 파일에 추가
- AI에게 "기존 WorkLog에 추가해줘"라고 명시

---

### 문제 4: "이 방법론이 내 학습에 맞지 않는 것 같아요"

**원인**: 모든 사람에게 완벽히 맞는 방법론은 없음

**해결**:
- Daily Retrospective에 "이 방법의 어떤 부분이 불편했나?" 기록
- 불편한 부분을 수정하면서 자신만의 방식으로 발전
- VibeLearn AI는 가이드라인이지 규칙이 아님

---

### 문제 5: "AI가 자동으로 처리해야 할 단계를 처리하지 않아요"

**원인**: 설계대로 작동하지 않는 상황

**해결**:
- VibeLearn AI는 "배우고 싶어" 한 마디로 모든 과정이 자동 진행되도록 설계되었습니다
- 만약 특정 단계가 자동으로 이루어지지 않는다면, 설계 의도와 다른 것입니다
- [GitHub Issues](https://github.com/solkit70/VibeLearn-AI/issues)에 리포트해주세요 → 반영하여 수정할 예정

리포트 시 포함할 내용:
1. 사용 중인 AI 도구 (VS Code + Copilot, Claude Code, Cursor 등)
2. 어떤 단계에서 막혔는지
3. 입력한 내용과 AI의 응답

---

**작성자**: Claude with VibeLearn AI
**최종 업데이트**: 2026-02-27
