# WorkLog - M1: 이벤트 전수 조사 (Research)

**날짜**: 2026-07-19
**Topic**: Seattle-Tech-Week-2026
**모듈**: M1 - 이벤트 전수 조사 (Research)
**학습 시간**: 방송 중 실시간 진행

---

## 🎯 오늘의 학습 목표

- [x] Seattle Tech Week 개요 조사 (시작·주최·철학·운영·분야·규모) → overview.md
- [x] luma 허브에서 Tech Week 2026 이벤트 목록 확인 시도
- [x] 7/27(월) 전체 43개 이벤트를 시간·호스트·장소·카테고리까지 표로 수집 (사용자 luma 화면 캡처 기반)
- [x] 7/27 전체 43개 이벤트의 Luma/주관사 링크 조사 (35개 확인, 8개 미확인)
- [~] 7/28~31(화~금) 동일 작업(시간+링크) — 대기 중

---

## 📚 진행 내용

### 1. luma 허브 조회

- `https://luma.com/seattletechweek2026` WebFetch → **동적 SPA**라 이벤트 제목·카테고리·일부 장소만 노출, 개별 날짜·시간 미노출.
- 기간 확정: **2026-07-27(월)~31(금)**, Madrona Ventures 주최, 약 200개 이벤트.

### 2. 웹 검색 보완

- WebSearch로 AI 관련 이벤트 추가 확인(엔터프라이즈 AI 패널, AI&SaaS 빌더 모임, Lightspeed AI 모닝 패널, AI2 Incubator @ AI House 700명+ 등). 단 정식 제목·시간은 미확인.
- GeekWire 캘린더(`geekwire.com/calendar/...`) → **403 Forbidden**으로 자동 조회 실패.

### 3. 산출물 작성

- `01-Event-Research/events.md` — AI 관련 이벤트 10건 표(제목·장소·카테고리) + 추가 확인 후보 4건.
- `01-Event-Research/README.md` — 조사 요약 + 시간 확보 방법 3가지.

### 4. 사용자 luma 화면 캡처로 7/27 전체 확보

- 사용자가 luma 허브의 **7/27(월) 일정 전체를 화면 캡처**해 제공 → 43개 이벤트의 시간·호스트·장소·카테고리·상태(Waitlist/Sold Out/Near Capacity)까지 정확히 확보.
- `events.md`를 실제 데이터로 전면 갱신, AI 태그(🤖) 14개 별도 요약표 추가.

### 5. 43개 이벤트 링크 조사 (Luma/주관사 페이지)

- 43개를 3개 배치(1-15, 16-29, 30-43)로 나눠 subagent 3개를 병렬 실행, 각 이벤트의 Luma 페이지
  또는 대체 링크(주관사 사이트·LinkedIn·Meetup)를 검색+직접 페이지 조회로 검증.
- 첫 실행 중 세션 usage limit 도달로 배치 1은 중단(부분 결과), 배치 2·3은 즉시 실패. limit 리셋
  후 배치 1은 SendMessage로 재개, 배치 2·3은 새로 재실행하여 완료.
- **결과**: 35개 확인(Luma 직접 링크 또는 검증된 대체 링크), 8개 미확인(#21 DOMENICA, #27
  Pitch4Impact, #28 UW HCDE/Lightspeed AI, #31 Agentic Commerce ASO, #33 Pickleball
  Tournament, #34 Value Edge, #36 Amplitude+Statsig, #37 Portal Space Systems) — 여러 차례
  검색해도 못 찾은 것은 추측하지 않고 미확인으로 남김.
- **주의 케이스 2건**: #38(Founder Happy Hour)은 Luma 페이지의 호스트 표기·날짜가 원 목록과
  일부 불일치(재확인 필요), #43(Kickoff Party)은 유사한 "Kickoff Party" 페이지가 2개 더 있어
  혼동 주의 — 두 건 모두 `events.md`에 ⚠️ 표시.

---

## 🐛 문제 해결 로그

### 문제 1: 개별 이벤트의 날짜·시간이 자동 조회로 안 나옴

**증상**: luma 허브·검색 모두 제목/장소까지만, 정확한 시간 미노출.
**원인**: luma는 이벤트 상세가 동적 렌더링/로그인 기반. 집계 페이지는 시간을 정적 HTML로 내보내지 않음. GeekWire는 봇 차단(403).
**해결**: README 옵션 1(사용자가 luma 화면을 열어 캡처)을 사용자가 선택 → 7/27 전체 일정을 스크린샷으로 전달받아 정확한 시간까지 구조화 완료. 자동 조회의 한계를 사람이 메꾸는 방식이 실제로 가장 빠르고 정확했음.

---

## 📊 DoD 체크리스트 (M1)

- [x] luma 허브에서 이벤트 확인 (제목·장소 수준)
- [x] 7/27 이벤트 표 — 시간·제목·호스트·장소·카테고리 완성 (43개, AI 14개)
- [x] 7/27 이벤트 링크(Luma/주관사) 조사 — 35개 확인, 8개 미확인
- [~] 7/28~31 — 대기 중 (같은 방식으로 캡처 필요)
- [x] `01-Event-Research/` 폴더 + README 작성
- [x] WorkLog 작성

**완료율**: 5/6 — 7/27 완료(시간+링크), 7/28~31 확보 시 M1 완전 완료

---

## 💡 Daily Retrospective

### What went well
- 기간·주최·규모·AI 이벤트 제목/장소를 빠르게 확보. 표 구조를 잡아 이후 선별·등록에 바로 쓸 수 있게 함.

### What could be improved
- 집계 페이지의 시간 미노출을 처음부터 예상하고, 사용자에게 luma 화면 공유를 먼저 요청했으면 더 빨랐을 것.

### Insights
- 동적 이벤트 허브(luma)는 자동 조회에 한계 → "사람이 화면을 열어 붙여넣기 + AI가 구조화"가 현실적. (이번 주 채널 회생 인사이트 "AI가 아직 못 하는 Action"과도 통함)

### Tomorrow's focus
- 시간 정보 확보(옵션 1~3 중 택1) → M1 시간 열 채우기 → M2 선별로 진행.

---

## 📎 참조 및 산출물

**생성된 파일**:
- `01-Event-Research/events.md`: AI 이벤트 표(제목·장소·카테고리)
- `01-Event-Research/README.md`: 조사 요약 + 시간 확보 방법

**참조 자료**:
- [Seattle Tech Week 허브](https://luma.com/seattletechweek2026)

**다음 세션 준비사항**:
- 관심 이벤트의 정확한 날짜·시간 (luma 화면 또는 개별 URL)

---

**작성자**: Changsoo (with Claude, VibeLearn AI)
