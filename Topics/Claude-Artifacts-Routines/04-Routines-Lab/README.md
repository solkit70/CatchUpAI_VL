# M4 — Routines · 공식 문서 · 기존 루틴 점검 · 두 번째 루틴

**상태**: 🟡 **실습 1(WBLP 루틴 점검)이 실제 사고로 먼저 끝났다** (2026-09-21, 약 50분) — 개념 문서 · 실습 2(두 번째 루틴) · 실습 3(로컬 vs 클라우드 판단표)은 남음

M4 는 로드맵 순서상 M3 뒤였는데, 유일한 실물 루틴(AWS WBLP 주간 확인)이 **3주 연속 조용히 실패**한 것을 9/21 에 발견해 점검·복구부터 했다. 원인은 루틴이 아니라 **클라우드 환경의 네트워크 모드(`Trusted`)** 였고, 복구 실행에서 그동안 놓친 미국 기술직 공고 4건이 첫 알림 메일로 나갔다. 덤으로 amazon.jobs API 가 검색 파라미터 두 개를 조용히 무시한다는 것도 잡아 프롬프트를 고쳤다.

## 📚 학습 순서

1. [guides/wblp-routine-audit.md](guides/wblp-routine-audit.md) — **3주 실패의 원인 진단 · 환경 설정 변경 · 프롬프트 결함 수정 · 결과** (영상용 배움 4개 포함)
2. [troubleshooting/routine-did-not-run.md](troubleshooting/routine-did-not-run.md) — 루틴이 안 돌았을 때 확인 순서 (`get` → `list_runs` → `get_run_log` → 로컬 재현 → 환경 네트워크)
3. ⬜ `concepts/routines-basics.md` — 트리거·환경·알림·비용 (공식 문서 클리핑 뒤)
4. ⬜ `guides/second-routine.md` — 두 번째 루틴 발행
5. ⬜ `concepts/local-vs-cloud.md` — 로컬 AI4PKM cron vs 클라우드 루틴 판단표

## 이 모듈에서 확인된 것 (9/21)

| | |
|---|---|
| 루틴 실행 이력을 세션 안에서 읽을 수 있다 | `schedule` 스킬 → `RemoteTrigger list_runs` · `get_run_log` — claude.ai 화면 없이 로그 전문 |
| 환경 ≠ 루틴 | 네트워크 규칙은 환경(`Default`)에 있고 웹 UI 에서만 바꾼다. 위치: New → `Default` 칩 → Cloud → 편집 → **Network access** |
| `Trusted` 의 뜻 | 패키지 저장소(npm · PyPI …) + Anthropic API 만. 외부 사이트를 읽는 루틴은 막힌다 |
| WebSearch 는 예외 | 프록시를 안 거쳐서 되지만 2차 정보 — 「확인」의 근거가 못 된다 |
| 조건부 알림의 함정 | 성공도 실패도 「소식 없음」이면 사람이 구분 못 한다 → 실패는 푸시로, 로그는 월 1회 사람이 |
| 수동 실행으로 즉시 검증 | 고친 뒤 다음 주를 기다리지 않는다 — `run` → 113초 뒤 로그 |

## 남긴 것

- 공식 Routines 문서 클리핑 → `vl_materials/` (실습 1 의 ①②는 아직)
- 두 번째 루틴 후보 판정 — (a) POB Deadline 경고는 **볼트 접근**이 관건 (루틴 환경에 레포 소스 필요) (b) BL 6차 알림 (c) 유튜브 주간 지표
- 로컬(GDR 04:00 · TIU 04:30) vs 클라우드(WBLP · 두 번째) 판단표

## 이전 / 다음

- 이전: [../02-Artifacts-Sharing-and-Versions/](../02-Artifacts-Sharing-and-Versions/) · M3 `03-Artifacts-Capabilities-Lab/` 은 아직 미착수 — 순서가 바뀐 이유는 위 상태 줄
- 로드맵: [../vl_roadmap/20260913_RoadMap_Claude-Artifacts-Routines.md](../vl_roadmap/20260913_RoadMap_Claude-Artifacts-Routines.md) · WorkLog: [../vl_worklog/20260921_M4a_Claude-Artifacts-Routines.md](../vl_worklog/20260921_M4a_Claude-Artifacts-Routines.md)
