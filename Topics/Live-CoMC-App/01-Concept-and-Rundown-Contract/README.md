# M1 — 개념 정의와 Rundown 파싱 계약

**상태**: ✅ 완료
**예상 학습 시간**: 6h
**Topic**: [[../topic_starter|Live-CoMC-App]]

---

## 이 모듈에서 배우는 것

라이브 방송 보조 MC 앱이 매주 읽어야 할 Rundown 문서의 구조를 파악하고, 파트 헤딩·커버리지 줄을 안정적으로 파싱하는 정규식 계약을 실제 방송 문서(Live14, Live20, Live21) 두 회차 이상에 대입해 검증한다. 동시에 "말하면 안 되는 섹션"을 실제 사례로 확보해 이후 M3 안전장치 설계의 입력을 만든다.

## 문서 목록 (학습 순서)

1. [concepts/document-map.md](concepts/document-map.md) — Rundown/Daily Roundup/Weekly Progress/Dashboard 4종 문서가 frontmatter `links:`로 어떻게 양방향 연결되는지 Mermaid 다이어그램으로 정리
2. [concepts/coverage-and-parts.md](concepts/coverage-and-parts.md) — 파트(Part)와 커버리지 줄(Coverage Line)의 핵심 개념, Rundown 정본 원칙(`.md` vs `.canvas`)
3. [examples/case-table.md](examples/case-table.md) — 파트 헤딩·커버리지 정규식을 Live20·Live21(+ 소수 파트 검증용 Live14)에 대입한 8개 변동성 케이스 표
4. [guides/forbidden-sections.md](guides/forbidden-sections.md) — 안전장치 1층(컨텍스트 진입 차단)의 입력이 될 금칙 섹션 3종(보류된 인사이트 후보/주간 영상 후보/대기 목록) 실제 사례와 파서 규칙 초안

## 핵심 결론 (다음 모듈로 넘어가는 것)

- 파트 헤딩 정규식 `^## (\d+(?:\.\d+)?)부: (.+?) \((.+?)\)$`은 실측 검증 완료
- 커버리지 상태 3종 중 "정의됨"·"운영 지시문 첨부"는 실물 확인, "미정"은 이 볼트 내 미관찰(방어적 파싱 규칙은 유지)
- 운영 지시문은 항목 단위가 아니라 **커버리지 줄 전체 끝**에 붙는다는 것을 실측으로 정정 — M3 스키마 설계에 반영 필요
- "대기 목록"은 완전 금칙이 아니라 조건부 발화 섹션 — M3에서 조건부 로직으로 별도 설계 필요

## 다음 모듈

→ [M2 - 파이프라인 아키텍처와 App Boundary 확정](../02-Architecture-and-Boundary/README.md)
