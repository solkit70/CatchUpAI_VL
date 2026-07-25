# WorkLog - M2: 관심 이벤트 검토·선별 (Curate)

**날짜**: 2026-07-19  
**Topic**: Seattle-Tech-Week-2026  
**모듈**: M2 - 관심 이벤트 검토·선별 (Curate)  
**학습 시간**: 자동 수집 결과 기반 후속 정리

## 오늘의 학습 목표

- [x] M1 자동 수집 결과를 기준 자료로 확정
- [x] AI 태그 이벤트 74개 중 사용자 관심사와 맞는 후보 선별
- [x] 날짜별 1차 추천 일정 작성
- [x] 시간 충돌 구간과 대체 후보 정리
- [x] M3로 넘길 최종 결정 사항 정리

## 진행 내용

### 0. 사용자 기준 반영

사용자는 오프라인 일정을 우선 계획하고, 온라인 이벤트는 유튜브나 녹화로 볼 가능성이 높으므로 실시간 참여 가치가 높은 것만 별도로 보겠다고 밝혔다. 관심사는 AI 관련 세미나, Pitch, Hackathon이며, 각 행사가 사용자의 Build with AI, Catch Up AI, VibeLearn, AI Agent 관심사와 어떻게 연결되는지 보고 참석 여부를 결정하고자 했다. 이에 따라 `02-Curation/shortlist.md`를 온라인/오프라인 분리 구조로 다시 정리했다.

### 1. 현재 상태 분석

M1은 기존 화면 캡처 기반 7/27 조사에서 Luma 공개 JSON API 기반 전체 조사로 확장되었다. 자동 수집 산출물 `01-Event-Research/events-auto.md`에는 2026년 7월 27일~31일 전체 237개 이벤트와 AI 태그 74개 이벤트가 정리되어 있다. 기존 `events.md`는 파일 잠금 때문에 교체하지 못했지만, M2 기준 자료로는 `events-auto.md`를 사용했다.

### 2. 선별 기준 적용

선별 기준은 AI 직접 관련성, 사용자 프로젝트 관련성, 등록 가능성, 시간 충돌, 이동 부담으로 잡았다. 특히 Build with AI, Vibe Coding, AI Agent, OpenAI, Claude Code, AI 제품화, GTM, 거버넌스와 연결되는 이벤트를 우선했다. Waitlist와 Sold Out 이벤트는 의미가 크더라도 바로 참석 가능성이 낮으므로 대체 후보 또는 관심 후보로 표시했다.

### 3. 날짜별 추천 일정 작성

`02-Curation/shortlist.md`에 7/27~7/31 날짜별 1차 추천 이벤트를 정리했다. 각 이벤트에는 상태, 추천 이유, Luma 링크를 포함했고, 같은 시간대에 겹치는 이벤트는 충돌 메모로 따로 설명했다. 최우선 신청 후보는 Claude Code Workshop, OpenAI Builder Lounge, You Vibe-Coded an App Now What, AI Agents as Force Multipliers for Solo Product Managers 등으로 정리했다. 이후 사용자 기준을 반영해 오프라인 후보와 온라인/Virtual 후보를 분리하고, 각 후보가 사용자의 실제 작업과 어떻게 연결되는지도 보강했다.

## 문제 해결 로그

### 문제 1: 기존 M1 산출물과 자동 수집 산출물의 기준 차이

**증상**: 기존 `events.md`는 7/27 중심이고, 새 `events-auto.md`는 5일 전체 일정이다.  
**해결**: M2에서는 더 최신이고 완전한 `events-auto.md`를 기준으로 사용했다. 다만 기존 파일은 삭제하거나 덮어쓰지 않고 보존했다.

### 문제 2: 모든 관심 이벤트를 실제 참석 후보로 넣으면 일정이 과밀해짐

**증상**: AI 태그 이벤트만 74개라 모든 이벤트를 캘린더 등록 대상으로 삼기 어렵다.  
**해결**: 등록 가능성과 사용자 관심사에 따라 1차 추천, 대체 후보, 충돌 메모로 나누었다. M3에서는 이 shortlist를 바탕으로 실제 캘린더 등록 대상을 확정한다.

## DoD 체크리스트

- [x] 관심 후보 표시 완료
- [x] 온라인/오프라인 별도 정리
- [x] 날짜별 타임라인 작성
- [x] 시간 충돌 정리 및 우선순위 결정
- [x] 사용자 업무와의 관련성 설명
- [x] `02-Curation/shortlist.md` 작성
- [x] WorkLog 작성
- [~] 사용자 최종 리뷰 후 M3 등록 대상 확정

## Daily Retrospective

### What I Learned

Luma 공개 JSON API를 사용하면 화면 캡처 없이 전체 일정과 링크를 자동 수집할 수 있다. 이벤트 선별 단계에서는 단순히 AI 태그만 보는 것보다 사용자의 실제 프로젝트와 연결되는 키워드, 예를 들어 Vibe Coding, Agent, OpenAI, Claude Code, GTM, governance를 함께 봐야 더 좋은 참석 후보가 나온다.

### What Went Well

M1의 수집 병목이 해결되어 M2를 전체 5일 일정 기준으로 진행할 수 있었다. 특히 `You Vibe-Coded an App, Now What?`, `AI Agents as Force Multipliers`, `OpenAI Builder Lounge`, `Claude Code Workshop`처럼 사용자의 현재 관심사와 직접 연결되는 이벤트를 명확히 뽑아냈다.

### What Could Be Better

실제 참석 가능성은 이벤트 상태뿐 아니라 이동 동선, 등록 승인 여부, 사용자의 개인 일정에 좌우된다. 또한 M2 시작 전 승인 절차가 먼저 있어야 했는데, 이전 진행에서 이 절차가 누락되었다. 이후 단계에서는 문서 변경과 모듈 전환 전에 계획과 승인 상태를 명확히 남겨야 한다.

### Tomorrow's Focus

M3로 진행한다. `shortlist.md`의 최우선 신청 후보를 사용자와 확정하고, Google Calendar 기존 일정과 충돌을 확인한 뒤 실제 등록할 이벤트를 `03-Schedule/final.md`로 정리한다.

## 참조 및 산출물

**생성된 파일**:
- `02-Curation/shortlist.md`: 날짜별 1차 추천 일정, 충돌 메모, 최우선 신청 후보

**참조 자료**:
- `01-Event-Research/events-auto.md`: Luma API 기반 전체 이벤트 자동 수집 결과
- Seattle Tech Week Luma 허브: https://luma.com/seattletechweek2026
