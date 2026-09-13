# M2 — Artifacts 공식 문서 · 공개 범위 · 버전

**상태**: ✅ 완료 (2026-09-13 Live #27 방송 중 · 실소요 45분 / 예상 2.5h) — 댓글·watch 는 계정 제약으로 「해당 없음」

원문의 질문 **「db 연동 페이지는 왜 링크 공유가 안 되는가」** 에 답했다: **페이지와 데이터의 공개 범위가 다르다.** 공개 링크를 켜면 HTML 은 누구나 보지만 db 데이터는 로그인한 Claude 사용자만 본다 — 익명 시청자에게 db 페이지는 빈 껍데기다. 설정으로 풀 수 없다(구조). 부수로 **이 계정이 Pro/Max 라 댓글·편집자·조직 공유가 불가**하다는 것을 알았다.

## 📚 학습 순서

1. [../vl_materials/2026-09-13 Claude Code Artifacts 공식 문서 발췌 (code.claude.com).md](../vl_materials/2026-09-13%20Claude%20Code%20Artifacts%20공식%20문서%20발췌%20(code.claude.com).md) — 공식 문서 인용 (공유·버전·댓글·제약)
2. [../vl_materials/2026-09-13 artifact-capabilities 스킬 발췌 (contract 0.2.46).md](../vl_materials/2026-09-13%20artifact-capabilities%20스킬%20발췌%20(contract%200.2.46).md) — 이 계정의 capability 8종과 공유 관련 문장
3. [concepts/sharing-scopes.md](concepts/sharing-scopes.md) — 공개 범위 3종 · 페이지 층 vs 데이터 층 · 남에게 링크 주기 전 확인 순서
4. [concepts/capabilities-roster.md](concepts/capabilities-roster.md) — 8종 한 줄씩 · 언제 쓰나 · 공개 가능 여부
5. [guides/sharing-matrix.md](guides/sharing-matrix.md) — **2×2 실험 실측표와 질문 1 의 답**
6. [examples/minimal-static.html](examples/minimal-static.html) · [examples/minimal-db.html](examples/minimal-db.html) — 실험 페이지 소스 (실물: [정적](https://claude.ai/code/artifact/3f864d29-c5c5-4d6c-b696-37fcc798ee62) · [db](https://claude.ai/code/artifact/a3bb593a-c879-42c2-b996-e11cc167ec1d))
7. [troubleshooting/shared-link-shows-old-version.md](troubleshooting/shared-link-shows-old-version.md) — 9/7 이슈 재해석

## 남긴 것

- 로그인한 **다른** 계정이 db 데이터를 실제로 읽는지 (대화상자 문구의 실측) → M3
- 공개 후 Share 메뉴의 "Always share latest version" 토글 유무 → 다음 세션에 사용자 확인
- 댓글·편집자 실습 — Team/Enterprise 계정이 생길 때까지 보류

## 이전 / 다음

- 이전: [../01-Inventory-and-Questions/](../01-Inventory-and-Questions/) · 다음: `03-Artifacts-Capabilities-Lab/` (M3 시작 시 생성)
