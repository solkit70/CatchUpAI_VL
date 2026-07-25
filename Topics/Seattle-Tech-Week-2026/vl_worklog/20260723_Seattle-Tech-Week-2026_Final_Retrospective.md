# Topic Retrospective - Seattle-Tech-Week-2026

**날짜**: 2026-07-23  
**Topic**: Seattle-Tech-Week-2026  
**방법론**: VibeLearn AI  
**상태**: 참가 계획 완료, 실제 Luma 신청 후속 필요

## 전체 학습 목표 달성도

- [x] AI 관련 이벤트 목록을 표로 정리
- [x] 관심 이벤트 후보 선별
- [x] 시간 충돌 정리 및 하루별 참석 일정 확정
- [x] Google Calendar 등록
- [x] 등록 링크 기록
- [x] 후속 Luma 신청 필요 목록 정리

## 가장 가치 있었던 학습

가장 큰 학습은 **행사 참가 계획도 데이터 수집 → 후보 선별 → 현실 일정화 → 캘린더 커밋으로 나누면 AI와 함께 품질 있게 끝낼 수 있다**는 점이다. 처음에는 Seattle Tech Week 전체 Luma 페이지가 동적 웹앱이라 세부 이벤트 수집이 어렵다는 문제가 있었지만, 공개 JSON/API 흐름을 찾아 전체 이벤트를 구조화하면서 조사 품질이 크게 올라갔다.

두 번째 학습은 **관심 후보를 전부 캘린더에 넣으면 계획이 아니라 소음이 된다**는 점이다. M2에서는 넓게 수집하고, M3에서는 실제 행동 가능성이 높은 것만 남기는 분리가 필요했다. Approval Required, Waitlist, Registration Closed, Open 상태를 구분하고, 기존 개인 캘린더와 충돌을 확인하면서 실제 참가 가능한 조합으로 줄였다.

세 번째 학습은 **Google Calendar 등록과 Luma RSVP는 별개**라는 점이다. 캘린더는 실행 계획을 고정하는 도구이고, 실제 참석 권한은 Luma에서 별도 신청해야 한다. 그래서 최종 산출물에는 캘린더 링크뿐 아니라 "실제 Luma 신청 필요 목록"을 별도로 남겼다.

## 실무 적용 계획

이번 Topic 산출물은 다음 행사 계획에도 그대로 재사용할 수 있다. 특히 `final.md`의 구조는 행사 후보가 많을 때 유용하다.

1. M1: 전체 이벤트 수집 및 자동화 가능한 데이터 원천 찾기
2. M2: 관심 후보와 날짜별 충돌 정리
3. M3: 실제 캘린더 등록 가능한 항목만 남기기
4. 후속: RSVP/승인 상태를 별도 열로 추적

Builders Lounge, BigHug, Seattle AI Ecosystem 활동에서도 이 방식은 그대로 쓸 수 있다. 특히 오프라인 행사 계획은 사람의 이동 시간, 기존 일정, 승인 상태가 모두 중요하므로, 단순 이벤트 목록보다 "실행 가능한 일정"으로 변환하는 단계가 핵심이다.

## 방법론 평가

VibeLearn AI 방식은 이번처럼 학습과 실무가 섞인 task형 Topic에 잘 맞았다. Roadmap의 M1/M2/M3 구조가 명확했기 때문에, 처음 조사 자동화에서 막혔을 때도 어디까지가 M1이고 어디부터 M2인지 구분할 수 있었다. 또한 WorkLog가 있었기 때문에 7/19에 멈춘 지점을 7/23에 다시 이어받기 쉬웠다.

다만 개선할 점도 있다. `daily_learning_prompt.md`의 현재 진행 상황 필드가 아직 예시 상태로 남아 있어서, 다음 Topic부터는 M1/M2/M3 진행 후 daily prompt의 "현재 모듈"과 "최근 WorkLog" 필드를 실제 값으로 업데이트하면 이어받기가 더 쉬워진다. 또한 행사 planning Topic에는 `RSVP Status`, `Calendar Status`, `Action Owner` 같은 열을 표준 필드로 추가하는 것이 좋다.

## 산출물 품질 체크

- [x] `01-Event-Research/events-auto.md`로 전체 AI 후보 수집
- [x] `02-Curation/shortlist.md`로 관심 후보와 충돌 정리
- [x] `03-Schedule/final.md`로 최종 참가 계획 작성
- [x] Google Calendar 이벤트 생성 및 링크 기록
- [x] 최신 WorkLog 작성
- [x] Retrospective 작성

## 남은 운영 후속

- [ ] Luma에서 `[Apply]` 항목을 실제 신청한다.
- [ ] 승인된 항목은 Google Calendar 제목에서 `[Apply]`를 제거한다.
- [ ] OpenAI Builder Lounge, Seattle World Models Carnival, How AI Gets Built at Ai2, AI & the Future of Consumer Experiences의 승인 상태와 실제 장소를 확인해 캘린더를 보강한다.
- [ ] Seattle Tech Week 이후 실제 참석 후기와 얻은 인사이트를 별도 Daily Roundup 또는 Weekly Roundup에 반영한다.

## 결론

Seattle Tech Week 2026 Topic은 VibeLearn AI의 "교과서 품질 산출물" 원칙을 실무 일정 계획에 적용한 사례다. 학습 내용은 특정 기술 개념이 아니라, **AI와 함께 동적 이벤트 데이터를 수집하고, 관심사를 기준으로 선별하고, 실제 캘린더 실행 계획으로 커밋하는 방법**이었다. 최종 산출물은 다음 Tech Week, 컨퍼런스, 커뮤니티 행사 계획에 재사용 가능한 템플릿 역할을 할 수 있다.
