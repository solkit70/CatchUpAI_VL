# WorkLog - M1: 개념 정의와 Rundown 파싱 계약

**날짜**: 2026-08-02
**Topic**: Live-CoMC-App
**모듈**: M1 - 개념 정의와 Rundown 파싱 계약
**학습 시간**: 사용자 가용 시간 2~3h 중 진행 (Claude Code 세션 사용량 91% 경고 상태로 시작 — 중간 종료 리스크를 감안해 실습 3개를 모두 우선 마무리하는 순서로 진행)

---

## 🎯 오늘의 학습 목표

- [x] 실습 1: 4종 문서 관계 지도 그리기
- [x] 실습 2: 파트 헤딩·커버리지 정규식 대조
- [x] 실습 3: 금칙 섹션 목록화

---

## 📚 진행 내용

### 1. 실습 1 — 4종 문서 관계 지도 그리기

**목적**: 앱이 참조할 문서 생태계를 눈으로 확인한다

**과정**:
1. `AI/Roundup/2026-07-26 - Live21 Weekly Rundown.md` frontmatter `links:` 확인 — Weekly Progress, Weekly Dashboard.canvas, Daily Roundup 5건(7/28~8/1), Weekly/Claude Code, Research 문서로 연결됨을 확인
2. `AI/Roundup/2026-08-01 - Daily Roundup.md` frontmatter 확인 — Journal, Weekly Progress, Weekly Dashboard, **Live21 Rundown**, 전날(7/31) Daily Roundup으로 연결되는 것을 확인. 즉 Rundown → Daily Roundup, Daily Roundup → Rundown 양방향 링크 존재
3. 문서 관계를 Mermaid 다이어그램으로 정리 → `concepts/document-map.md`

**결과**: 4종 문서가 단방향 계층이 아니라 **양방향 그래프**임을 확인. Rundown이 한 주의 Daily Roundup 여러 건을 링크하고, 각 Daily Roundup도 Rundown과 Weekly 문서를 되짚어 링크한다.

**메모/인사이트**: 앱이 "이번 주 Rundown"에서 출발해 관련 Daily Roundup을 따라가는 것도 가능하고, 반대로 특정 날짜의 Daily Roundup에서 시작해 이번 주 Rundown으로 거슬러 올라가는 것도 가능하다. 다만 M1 범위에서는 Rundown 단일 문서 파싱 계약만 다루고, 문서 간 그래프 탐색은 MVP 경계 밖(M2에서 boundary 문서화 예정)으로 남긴다.

---

### 2. 실습 2 — 파트 헤딩·커버리지 정규식 대조

**목적**: 문서 변동성이 실제로 어느 정도인지 손으로 확인한다

**과정**:
1. Live20(`2026-07-19`)과 Live21(`2026-07-26`) Rundown을 나란히 대조
2. 커버리지 줄 형태를 회차 간 비교
3. 소수 파트(`4.5부` 등)와 자유형 시간 문자열 사례를 볼트 전체 Rundown에서 검색
4. `examples/case-table.md`로 정리

**결과**:
- 파트 헤딩 정규식 `^## (\d+(?:\.\d+)?)부: (.+?) \((.+?)\)$`은 Live20·Live21 두 회차 모두에서 매칭됨 (Live20은 `(시간 미정)`, Live21은 `(20분)`/`(10분)`/`(나머지 시간 전부)` 형태)
- 커버리지 줄 `> **이번 방송 커버리지**: ①...`도 두 회차 모두 동일 포맷
- **소수 파트**: Live20·Live21에는 없었고, `2026-06-08 - Live14 Weekly Rundown.md`에서 `4.5부`, `4.8부`, `4.9부` 확인 — 정규식이 소수점 첫째 자리까지 대응해야 함을 실증
- **운영지시문 첨부형**: 볼트 전체에서 "미정 — 방송 전 확정 필요" 같은 리터럴 문구는 발견되지 않음(방송 준비 시점엔 이미 커버리지가 확정된 상태로 저장되기 때문으로 추정). 대신 Live21 3부 커버리지 줄 끝의 "— 이 두 개를 메인으로 진행하고, 시간이 남으면 아래 대기 목록에서 이어간다"가 **커버리지 뒤 운영 지시문이 붙는 실제 사례**로 확인됨
- **coverage_state: "undefined"** 케이스는 이번 대조에서 실물을 찾지 못함 → M3(안전 정책 스펙)에서 스키마상 상태값으로는 유지하되, "실사용 빈도 낮음"으로 주석 처리

**메모/인사이트**: 원래 계획서(`ethereal-puzzling-seahorse.md`)가 가정한 3가지 커버리지 상태 중 "미정"은 실제 데이터에서 관찰되지 않았다. 이건 설계가 틀렸다는 뜻이 아니라, **방송 전날 최종 정리 단계에서만 이 볼트에 Rundown이 저장되기 때문**일 가능성이 높다 — 즉 미정 상태의 초안은애초에 파일로 존재하지 않을 수 있다. M3에서 "만약 미정 텍스트를 만나면"이라는 방어적 파싱 규칙은 유지하되, 실측 빈도가 0이었다는 사실 자체를 케이스 표에 기록해 둔다.

---

### 3. 실습 3 — 금칙 섹션 목록화

**목적**: 안전장치 1(컨텍스트 진입 차단)의 입력이 될 목록을 만든다

**과정**:
1. Live21 Rundown 전체에서 `## 보류된 인사이트 후보`, `## 주간 영상 후보`, `### 대기 목록` 3개 섹션을 모두 확인
2. 각 섹션이 왜 발화되면 안 되는지(혹은 조건부로만 허용되는지) 근거를 정리
3. `guides/forbidden-sections.md`로 정리

**결과**: 3종 모두 한 회차(Live21) 안에서 실물 확보. 그중 "대기 목록"은 계획서가 가정한 단순 금칙과 달리 **조건부 발화 허용** 섹션임을 발견 — `excluded_sections[]`와 `conditional_sections[]`를 분리하는 스키마 조정이 필요하다는 것을 M3로 넘김.

**메모/인사이트**: "보류된 인사이트 후보" 섹션에는 사용자 자신의 미정리 개인 생각(예: burn-out 경험 초안)이 포함되어 있었다. 이건 안전장치 1층이 막아야 할 대상의 실제 민감도를 보여주는 구체적 증거다 — 단순히 "형식이 다른 섹션"이 아니라 "아직 공개할 준비가 안 된 콘텐츠"라는 걸 확인했다.

---

## 🐛 문제 해결 로그

특이 문제 없음. 다만 "미정" 커버리지 실물 부재는 위 인사이트로 기록.

---

## 📊 DoD 체크리스트

- [x] 문서 관계 지도 완성 (Mermaid)
- [x] 파트 헤딩·커버리지 정규식이 Live20·Live21 두 회차 모두에서 검증됨
- [x] 금칙 섹션 패턴 3종 이상 확보
- [x] `case-table.md`에 최소 6개 변동성 케이스 등재 (8개 확보)
- [x] README 작성 완료
- [x] WorkLog 작성 완료

**완료율**: 6/6 (100%) — M1 DoD 전체 달성

---

## 💡 Daily Retrospective

### What went well (잘된 점)
- 실제 볼트 데이터(Live14/17/20/21 Rundown)를 근거로 케이스를 잡아, 계획서의 가정을 검증하며 진행할 수 있었다

### What could be improved (개선할 점)
- "미정" 커버리지 상태는 실물 확인 없이 설계에만 존재 — 추후 실제로 방송 전날 초안 저장을 시작하게 되면 재검증 필요

### Insights (인사이트)
- 문서 그래프가 양방향이라는 점은 M2 아키텍처 설계(App Boundary)에서 "Rundown 단일 문서만 신뢰 소스로 삼는다"는 범위 제한을 더 명확히 정당화한다

### Tomorrow's focus (다음에 할 것)
- M2 - 파이프라인 아키텍처와 App Boundary 확정 시작
- M2에서 M1 발견 사항 2건 즉시 반영: ①운영 지시문은 커버리지 줄 전체 끝에 붙는 자유 문장 형태(항목 단위 아님) ②"대기 목록"류 섹션은 완전 금칙이 아니라 조건부 발화 — `excluded_sections[]`와 `conditional_sections[]` 분리 필요

---

## 📎 참조 및 산출물

**생성된 파일/폴더**:
- `01-Concept-and-Rundown-Contract/concepts/document-map.md`: 4종 문서 관계 Mermaid 다이어그램
- `01-Concept-and-Rundown-Contract/concepts/coverage-and-parts.md`: 파트/커버리지 줄 핵심 개념
- `01-Concept-and-Rundown-Contract/examples/case-table.md`: 파트 헤딩·커버리지 변동성 케이스 표 (8개)
- `01-Concept-and-Rundown-Contract/guides/forbidden-sections.md`: 금칙 섹션 3종 + 파서 규칙 초안
- `01-Concept-and-Rundown-Contract/README.md`: 모듈 개요 및 문서 목록

**참조 자료**:
- `AI/Roundup/2026-07-19 - Live20 Weekly Rundown.md`
- `AI/Roundup/2026-07-26 - Live21 Weekly Rundown.md`
- `AI/Roundup/2026-06-08 - Live14 Weekly Rundown.md`
- `AI/Roundup/2026-08-01 - Daily Roundup.md`

**다음 세션 준비사항**:
- 없음 — M1 완료, M2(파이프라인 아키텍처 & App Boundary)로 바로 진행 가능

---

**작성자**: solkit70
**방법론**: VibeLearn AI
