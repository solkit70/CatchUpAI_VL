# WorkLog — 2026-10-24 · M1 한눈에 보기

**Topic**: Civic-Innovation-Challenge-2026 · **모듈**: M1 — 한눈에 보기: 무엇 · 누가 · 언제 · **세션**: 1 (약 1.5시간)

## 🎯 오늘의 학습 목표

- [x] 세 문장 요약(한 · 영)과 「무엇인가」 문서
- [x] 자격 · 일정 문서(한 · 영), 「공고에 없는 것」 분리
- [x] 모듈 README(한 · 영)
- [x] vl_materials 출처 목록 (빈 폴더 방지)
- [x] `check_links.py` 점검

## 📚 진행 내용

### 1. 근거 확인

준비 자료(공개 레포 제외 폴더)의 행사 사실표와 공고 PDF 4종 텍스트를 대조했다. 이번 Topic 을 시작하기 전 같은 날 다른 문서들에 사용 사례를 「9개 중 6개가 AI」로 잘못 셌던 것을 발견해 **8개 중 5개(영상 인식 포함)** 로 바로잡은 상태에서 시작했다. 마감 시각은 Overview 가 「5:00 pm PDT」, Submission 이 「5pm PST」로 적었는데 11/13 은 서머타임이 끝난 뒤라 공개 문서에는 「태평양 시간」으로만 썼다.

### 2. 문서 작성

- `01-Overview/concepts/what-is-it.md` · `.en.md` — 세 문장 요약, Exchange Northwest, PoC 파일럿(도입 보장 아님), 혜택 4가지, 지원금 「대부분 하한 쪽」, 선정 수(1차 23팀 중 4팀 참고)
- `01-Overview/guides/eligibility-and-timeline.md` · `.en.md` — 공식 자격 3가지 / 사실상 필요한 조건 8가지 / 공고에 없는 것 4가지(설명회 확인 예정), 일정 표, 신청처. 1차 일정 지연을 참고로 추가
- 각주 방식으로 문장마다 출처를 달고, 공고 PDF 는 공식 주소로 연결했다

### 3. 점검

`check_links.py` — 상대 링크 정상 10 · 깨짐 0. 빈 폴더 `vl_worklog` 는 이 WorkLog 로 해결.

## 🐛 문제 해결 로그

### 문제 1: 사용 사례 개수 오류
- **증상**: 이전 문서들에 사용 사례 9개, AI 6개로 적혀 있었다
- **원인**: Use Cases PDF 를 다시 세지 않고 처음 요약을 옮겨 썼다
- **해결**: 원문을 다시 세어 8개(Bellevue 3 · King County 4 · WaTech 1), AI 5개로 정정. 공개 문서에는 처음부터 8개로 썼다
- **교훈**: 숫자는 매번 원문에서 다시 센다

### 문제 2: 마감 시각 표기 (PDT vs PST)
- **해결**: 「오후 5시(태평양 시간)」으로 통일

## 📊 DoD 체크리스트 (M1)

- [x] 세 문장 요약(한 · 영)이 README 맨 위에 있다
- [x] 자격 · 일정 문서(한 · 영) 완성, 「공고에 없는 것」 분리
- [x] 모든 숫자에 출처 표기
- [x] 한국어 · 영어 문서 내용이 일치
- [x] 🔴 README 링크 확인 (`check_links.py` — 깨짐 0)
- [x] WorkLog 작성 · Daily Retrospective

**M1 DoD 6/6 (100%)**

## 💡 Daily Retrospective

### What went well (잘된 점)
- 준비 자료가 있어 1.5시간 안에 모듈을 닫았다
- 「공고에 없는 것」을 따로 두어 설명회 뒤 갱신할 자리를 미리 만들었다

### What could be improved (개선할 점)
- 숫자 오류를 Topic 시작 전에 발견하긴 했지만, 처음부터 원문을 세었어야 했다

### Insights (인사이트)
- 「파일럿 = 도입 보장 아님」과 「지원금 대부분 하한 쪽」은 지원자 기대를 맞추는 데 가장 중요한 두 문장이다
- 1차 일정이 2~4개월 밀렸다는 사실은 지원자에게 「일정은 바뀔 수 있다」는 실용 정보가 된다

### Tomorrow's focus (내일 집중할 것)
- **M2 실습 3 — 10/26 설명회 질문 목록 (월요일 18:00 전 필수)**
- M2 사용 사례 카드 8장 · 평가 기준 ↔ 신청서 문항 매핑

## 📎 참조 및 산출물

- 산출물: [01-Overview/README.md](../01-Overview/README.md) · [README.en.md](../01-Overview/README.en.md)
- 출처 목록: [vl_materials/README.md](../vl_materials/README.md)
- Roadmap: [M1 섹션](../vl_roadmap/20261024_RoadMap_Civic-Innovation-Challenge-2026.md)
