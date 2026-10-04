---
title: "합성 fixture"
created: 2026-10-02 10:43:41
tags:
  - personal-ops-board
  - vibelearn-ai
---

## 합성 fixture

아래 세 파일은 실제 할 일에서 복사하지 않은 합성 입력이다. 의도적인 누락·깨진 YAML을 포함하므로 실제 `AI/Tasks/items/`에 옮기지 않고 이 폴더를 --items로 지정한다. → [실행법](../guides/run-indexer.md#합성-입력-실행)

| 입력 | 필수 기대 결과 |
|---|---|
| [due-missing.md](fixtures/due-missing.md) | tier_due_required warning |
| [waiting-mismatch.md](fixtures/waiting-mismatch.md) | tier_mismatch_waiting·waiting_on_required warning |
| [broken-yaml.md](fixtures/broken-yaml.md) | valid:false·frontmatter_parse_error error |

총 tasks 3개·valid 2개가 기대 결과다. project/source를 비워 두었으므로 그 권장 필드 경고도 함께 나오는 것이 정상이다. 링크 중복·paused·상시·닫음·이름 변경은 비공개 자동 회귀 테스트의 임시 합성 입력으로 검증한다.
