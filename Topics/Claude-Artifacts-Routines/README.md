# Claude-Artifacts-Routines — Claude 의 Artifacts 와 Routines 제대로 쓰기

> **일하다 마주쳐 쓰게 된 두 기능을, 이미 만든 실물에서 출발해 공식 문서와 실험으로 다시 배운 Topic.** Artifacts(Claude 가 발행하는 웹페이지·앱 — db · 보는 사람 · 파일 · 댓글 같은 런타임 기능 포함)와 Routines(내 PC 가 꺼져 있어도 클라우드에서 정해진 시각에 스스로 도는 Claude Code 작업)를 VibeLearn AI 방법론으로 공부했다. 끝은 「내가 몰랐던 기능을 AI 가 찾아냈다」 Remotion 영상이다.

| | |
|---|---|
| 기간 | 2026-09-13 로드맵 → 진행 중 (M1~M5 완료 · 2026-09-27) |
| 상태 | ✅ **M1~M5 완료** · ⏳ M6 영상 (M5 플레이북이 대본의 뼈대) |
| 실소요 | M1 50분 · M2 45분 · M3 약 1시간 · M4 약 1시간 35분 (9/21 + 9/27) · M5 약 25분 — 로드맵 예상 15시간 중 약 4시간 40분 |
| 출발점 | 이미 만든 실물 — 행사 부스 배치 편집기 · 부스 현황판 · 모임 입장 안내 페이지 · 채용 공고 주간 확인 루틴 (재검토하니 실물은 4건이 아니라 **7건**이었다) |
| 한 줄 결과 | **사람과 AI 가 같은 데이터를 고칠 때 `if_version` 이 사람의 변경을 지켜 주고, 조용한 자동화는 실패까지 조용하게 만든다.** 둘 다 실측으로 확인했다 |

## 무엇을 알아냈나

- **db 페이지는 공개 링크로 공유해도 데이터가 안 보인다.** 페이지와 데이터의 공개 범위가 다르다. 공개 링크로 HTML 은 누구나 보지만 db 데이터는 로그인한 사용자만 본다. 설정이 아니라 구조다 → [M2 sharing-matrix](02-Artifacts-Sharing-and-Versions/guides/sharing-matrix.md)
- **AI 세션의 쓰기는 `if_version` 으로 보호된다.** 사람이 화면에서 v2 → v4 로 바꾼 뒤 세션이 v2 기준으로 쓰자 `version_mismatch` 로 거부됐고, 다시 읽은 v4 로는 통과했다. 페이지 쪽 쓰기는 마지막에 쓴 사람이 이긴다 → [M3 db-roundtrip](03-Artifacts-Capabilities-Lab/guides/db-roundtrip.md)
- **「조건이 맞을 때만 알림」 루틴은 3주 동안 조용히 실패했다.** 원인은 루틴이 아니라 클라우드 환경의 네트워크 규칙(`Trusted` = 허용 목록만)이었다. 실패한 주와 공고가 없던 주가 똑같이 「소식 없음」으로 보였다 → [M4 wblp-routine-audit](04-Routines-Lab/guides/wblp-routine-audit.md)
- **커넥터(Gmail · 캘린더)는 네트워크 허용 목록과 무관하다.** 두 번째 루틴은 환경을 건드리지 않고 25초 만에 성공했다. 실행 목록의 초록색은 「인프라 오류 없음」일 뿐 할 일의 성공이 아니다 → [M4 second-routine](04-Routines-Lab/guides/second-routine.md)
- **볼트를 쓰면 로컬, 외부만 보면 클라우드.** 클라우드 루틴은 선택한 GitHub 레포만 clone 하므로 로컬 볼트를 읽지 못한다 → [M4 판단표](04-Routines-Lab/concepts/local-vs-cloud.md)
- **「안 된다」도 실측으로 닫아야 한다.** M2 에서 문서 한 문장으로 「이 계정에서 댓글 불가」라고 결론 냈는데, M3 에서 댓글과 Send to Claude 가 실제로 작동했다 → [M5 안티패턴 10](05-Usage-Patterns/guides/anti-patterns.md)

## 모듈 (학습 순서)

| # | 모듈 | 상태 | 핵심 산출물 |
|---|---|---|---|
| 1 | [실물 재검토와 질문 목록](01-Inventory-and-Questions/README.md) | ✅ 9/13 | [실물 상태표](01-Inventory-and-Questions/guides/inventory.md) (시크릿 창 실측 6/6) · [질문 9개](01-Inventory-and-Questions/guides/questions.md) |
| 2 | [Artifacts 공개 범위 · 버전](02-Artifacts-Sharing-and-Versions/README.md) | ✅ 9/13 | [공개 범위](02-Artifacts-Sharing-and-Versions/concepts/sharing-scopes.md) · [2×2 실험 실측표](02-Artifacts-Sharing-and-Versions/guides/sharing-matrix.md) · [옛 버전이 보일 때](02-Artifacts-Sharing-and-Versions/troubleshooting/shared-link-shows-old-version.md) |
| 3 | [Artifacts 런타임 기능 실험](03-Artifacts-Capabilities-Lab/README.md) | ✅ 9/27 | 예제 5종 (db · user · assets · comments · 다중 파일) · [db 왕복 실측](03-Artifacts-Capabilities-Lab/guides/db-roundtrip.md) · [기능 선택표](03-Artifacts-Capabilities-Lab/concepts/capability-selection-table.md) |
| 4 | [Routines](04-Routines-Lab/README.md) | ✅ 9/27 | [3주 실패 진단](04-Routines-Lab/guides/wblp-routine-audit.md) · [루틴 기본](04-Routines-Lab/concepts/routines-basics.md) · [두 번째 루틴](04-Routines-Lab/guides/second-routine.md) · [로컬 vs 클라우드](04-Routines-Lab/concepts/local-vs-cloud.md) |
| 5 | [사용 패턴 가이드](05-Usage-Patterns/README.md) | ✅ 9/27 | **[플레이북](05-Usage-Patterns/guides/artifacts-routines-playbook.md)** · [패턴 6장](05-Usage-Patterns/guides/patterns.md) · [안티패턴 10개](05-Usage-Patterns/guides/anti-patterns.md) |
| 6 | Capstone — Remotion 영상 | ⏳ | 「내가 몰랐던 기능을 AI 가 찾아냈다」 5~8분 한국어 영상 |

> 처음 온 사람이라면 **[플레이북](05-Usage-Patterns/guides/artifacts-routines-playbook.md)** 한 장부터 보면 된다. 만들기 전에 고를 것과 체크리스트가 모여 있다.

## 순서가 바뀐 곳

M4 의 실습 1(루틴 점검)을 9/21 에 먼저 했다. 유일한 실물 루틴이 3주 연속 실패한 것을 발견해 사고 대응으로 앞당겼다. M3 는 9/27 오전 다른 도구(Codex)로 시작하려다 막혀, 같은 날 오후 VS Code 의 Claude Code 확장에서 처음부터 진행했다. 이 확장에는 Artifact 를 발행하고 db 를 읽고 쓰는 도구가 직접 있어서 브라우저 조작 없이 실습했다.

## 확인 못 한 것

- 조직 밖 사람이나 공개 링크 방문자가 댓글을 달 수 있는가 (작성자 댓글만 실측)
- 페이지에서 여러 사람이 동시에 +1 할 때 실제로 한 번이 사라지는가 (문서로만 확인)
- 실습 예제는 모두 비공개라 다른 계정 · 시크릿 창 확인은 생략했다

## 폴더

| 폴더 | 내용 |
|---|---|
| [vl_roadmap/](vl_roadmap/20260913_RoadMap_Claude-Artifacts-Routines.md) | 로드맵 · 진행 상황 표 |
| [vl_worklog/](vl_worklog/) | 세션별 WorkLog — M1 · M2 · M4a · M3 · M4b · M5 |
| [vl_materials/](vl_materials/) | 공식 문서 발췌 (Artifacts · Routines · capability 스킬) |
| [vl_prompts/](vl_prompts/) | 로드맵 · 일일 학습 프롬프트 |
| [topic_starter.md](topic_starter.md) | Topic 시작 정보 |
