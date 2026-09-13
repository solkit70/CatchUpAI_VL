# VibeLearn AI Topic Starter

> 이 파일은 새로운 Topic 학습을 시작할 때 작성하는 템플릿입니다.
>
> **사용 방법**:
> 1. 이 파일을 복사하여 `[TopicName]_topic_starter.md`로 저장
> 2. 아래 항목들을 채워서 작성
> 3. AI에게 이 파일을 전달하여 Topic 폴더 구조 생성 요청
> 4. 생성된 폴더에서 학습 시작!

---

## 📌 Topic 기본 정보

### Topic 이름
**형식**: 영문, 하이픈 또는 언더스코어 사용 (공백 없음)
**예시**: `MCP-Basics`, `Docker_Fundamentals`, `FastAPI-Tutorial`

```
Topic 이름: Claude-Artifacts-Routines
```

### Topic 설명
**목적**: 이 Topic이 무엇인지 한두 문장으로 설명

```
설명: 다른 Topic(Datacenter-Workforce-Programs · WA-Caregiver-Pathways)을 공부하다 "일하다 마주쳐" 쓰게 된 Claude 의 두 기능 — Artifacts(발행되는 웹페이지·앱, db/자산/댓글 등 런타임 기능 포함)와 Routines(클라우드에서 정해진 시각·조건에 스스로 도는 작업) — 를 이미 만든 실물 4건(BigHug 부스 매니저·현황판, Builders Lounge 입장 안내, AWS WBLP 주간 확인 루틴)을 출발점으로 삼아 공식 문서와 실험으로 정확히 이해하고, 더 잘·효율적으로 쓰는 사용 패턴을 정리한 뒤, 그 정보와 경험을 다른 사람에게 전달하는 Remotion 영상으로 마무리하는 Topic
```

### 학습 목적
**왜 이것을 배우는가?**

```
학습 목적:
- 두 기능을 "써 보니 되더라" 수준에서 "무엇이 되고 무엇이 안 되는지 알고 쓰는" 수준으로 올린다 — 특히 BigHug 에서 부딪힌 「db 연동 페이지는 왜 링크 공유가 안 되는가」를 정확히 답한다
- 이미 만든 실물 4건을 재검토해 잘못 쓰거나 놓친 기능(버전·공유·댓글·자산·트리거 조건)을 찾아 고친다
- 볼트의 실제 일(BigHug 행사, Builders Lounge 운영, 취업 공고 확인, Personal Ops Board)에 바로 적용할 사용 패턴을 5개 안팎으로 정리한다
- 「내가 몰랐던 기능을 AI 가 찾아냈다」는 경험을 포함해, 정보와 경험을 전달하는 유튜브용 Remotion 영상을 만든다
```

### 예상 학습 기간
**현실적으로 예상되는 기간**

```
예상 기간: 3주 (주당 약 5시간, 총 15시간) — 9/13 시작, Personal Ops Board 착수(9/27) 전후로 영상 제작
```

---

## 🎯 학습 목표

**이 Topic을 완료했을 때 달성하고 싶은 구체적 목표**

```
- [ ] Artifacts 의 공개 범위(비공개·링크·조직·db 있음/없음)와 버전·재발행·pin·댓글 동작을 공식 문서 근거로 설명하고, 「db 연동 페이지는 왜 공유가 안 되는가」에 정확히 답할 수 있다
- [ ] 기존 Artifact 3건(부스 매니저·부스 현황판·입장 안내)을 재검토해 공유 범위·버전 상태를 시크릿 창으로 검증하고, 잘못된 것을 고칠 수 있다
- [ ] Artifact 런타임 기능(db · user · assets · comments · 다중 파일)을 각각 최소 예제로 한 번씩 만들어 보고, 어떤 일에 어떤 기능이 맞는지 표로 정리할 수 있다
- [ ] Routines 의 트리거(cron · 조건) · 실행 환경 · 알림 · 비용 구조를 공식 문서 근거로 설명하고, 기존 루틴 1건(AWS WBLP)을 점검해 개선할 수 있다
- [ ] 볼트의 실제 일에서 두 번째 루틴 1건을 설계·발행해, 로컬 AI4PKM cron 과 클라우드 루틴을 언제 어느 쪽으로 쓸지 판단 기준을 세울 수 있다
- [ ] 두 기능의 「더 잘·효율적으로 쓰는 패턴」 가이드 1편을 쓰고, 그 정보와 경험을 전달하는 Remotion 영상 1편(한국어, 5~8분)을 제작해 유튜브에 올릴 수 있다
```

**권장**: 3-5개의 명확하고 검증 가능한 목표

---

## 🛠️ 학습 환경

### 운영 체제
```
OS: Windows 11
버전: Home 10.0.26200
```

### 주요 도구 및 기술 스택
**이 Topic 학습에 필요한 도구들**

```
- Claude Code (VS Code 확장 · CLI) — Artifact 도구(publish/read/list/db/assets/comments) · 클라우드 루틴(/schedule)
- claude.ai 웹 — 아티팩트 갤러리(claude.ai/code/artifacts) · 루틴 관리(claude.ai/code/routines)
- 브라우저 시크릿 창 — 공유 상태 검증용 (소유자 브라우저는 항상 최신을 보여 준다)
- AI4PKM 오케스트레이터(orchestrator.yaml) — 로컬 cron 과의 비교 대상
- Remotion (AI/RemotionStudio) + edge-tts — 캡스톤 영상
- Obsidian — 볼트 기록·인덱스
```

### 사전 지식 (Prerequisites)
**이 Topic을 학습하기 전에 알아야 할 것**

```
필수:
- Claude Code 기본 사용 (이 볼트에서 매일 사용 중)
- HTML/CSS/JS 를 읽고 고칠 수 있는 정도 (Artifact 는 HTML 한 장이다)
- 이미 만든 실물 4건의 맥락 — Materials_For_Topics/Claude-Artifacts-Routines/2026-09-13 사례 인덱스.md

권장:
- cron 표현식 (Routines · AI4PKM 둘 다 쓴다)
- VibeLearn AI 영상 제작 흐름 (remotion-video 스킬 — 이전 Topic 캡스톤 경험)
- Personal-Ops-Board PRD (Deadline 에이전트를 루틴으로 돌릴 수 있는지가 이 Topic 의 실습 후보)
```

---

## 📚 참조 자료 (Optional)

### 공식 문서
```
- Claude Code Artifacts (아티팩트 발행·갤러리·공유·capabilities): https://docs.claude.com/ — 학습 M2 에서 정확한 페이지를 찾아 클리핑한다 (현재 볼트에 클리핑 0건)
- Claude Code Routines / Scheduled cloud agents: https://docs.claude.com/ — 학습 M4 에서 클리핑
- Claude Code 세션 내 스킬 문서: artifact-capabilities · artifact-design · schedule (Skill 도구로 로드 가능)
```

### 튜토리얼 및 강의
```
- (없음 — 이 Topic 은 공식 문서 + 자기 실물로 간다)
```

### 관련 GitHub 저장소
```
- (해당 없음)
```

### 추가 학습 자료
**파일, 문서, 동영상 등을 `vl_materials/` 폴더에 저장 가능**

```
vl_materials/ 폴더에 추가할 자료:
- Materials_For_Topics/Claude-Artifacts-Routines/2026-09-13 시작 프롬프트 (원문).md — 사용자 구술 원문
- Materials_For_Topics/Claude-Artifacts-Routines/2026-09-13 사례 인덱스.md — 볼트 안 실사용 4건 + 계기 기록 + 「없는 것」 목록
- 실물 링크: 부스 매니저 991fb41f… · 부스 현황판 aa2d46bf… · 입장 안내 e9c029bd… · WBLP 루틴 trig_01LKgvHWt4ZfJbTqJgn5KvVT
- (M2·M4 에서 추가) 공식 문서 클리핑 · 화면 스크린샷
```

---

## 🎓 학습 접근 방식 (Optional)

### 선호하는 학습 스타일
```
- [ ] 이론 먼저, 실습 나중
- [x] 실습 중심, 필요한 이론만 (권장)
- [ ] 이론과 실습 병행
```

### 시간 투자 계획
```
- 주당 학습 시간: 5시간
- 학습 가능 요일: 일요일 라이브 방송 + 주중 1~2회
- 1회당 학습 시간: 1-2시간
```

### 특별히 집중하고 싶은 영역
```
- 「공유가 안 된다」의 정확한 이유와 우회 — 실무에서 바로 부딪힌 문제
- 이미 만든 실물을 고치는 실습 — 새 예제보다 내 것을 재검토
- 로컬(AI4PKM cron) vs 클라우드(Routines) 판단 기준 — Personal Ops Board 설계와 직결
- 영상은 기능 나열이 아니라 「어떻게 알게 됐고 무엇이 달라졌는가」
```

---

## 🚀 다음 단계

### 이 파일 작성 완료 후:

1. **Topic 폴더 생성 요청**
   - AI에게 이 파일을 전달
   - "이 topic_starter.md를 바탕으로 Topic 폴더 구조를 만들어주세요" 요청

2. **생성될 폴더 구조**
   ```
   Claude-Artifacts-Routines/
   ├── topic_starter.md
   ├── vl_prompts/
   │   ├── roadmap_prompt.md
   │   └── daily_learning_prompt.md
   ├── vl_roadmap/
   ├── vl_worklog/
   └── vl_materials/
   ```

3. **Roadmap 생성**
   - `vl_prompts/roadmap_prompt.md` 파일을 AI에게 전달
   - AI가 체계적인 학습 로드맵 생성
   - 생성된 로드맵을 `vl_roadmap/` 폴더에 저장

4. **학습 시작!**
   - `daily_learning_prompt.md`로 매일 학습 진행
   - WorkLog 작성으로 진행 상황 추적
   - Retrospective로 지속적 개선

---

**Template Version**: 1.0
**Created by**: VibeLearn AI Methodology
**Topic Created**: 2026-09-13 (Live #27 방송 중)
