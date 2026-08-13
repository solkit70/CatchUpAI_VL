# WorkLog - M1: 소스 맵 및 리서치 갱신

**날짜**: 2026-08-10  
**Topic**: Seattle-Tech-Week-2026-Article-Writing  
**모듈**: M1 - 소스 맵 및 리서치 갱신  
**학습 시간**: 16:06-16:45 (부분 세션)

## 오늘의 학습 목표

- [x] M1 소스 맵 폴더 구조 만들기
- [x] 공식/기사, 외부 YouTube, Catch Up AI 영상/Transcript 소스 분리하기
- [x] 각 소스 묶음에 1차 트렌드 축 태깅하기
- [x] 기사 분석 전에 확인 필요 항목 분리하기
- [ ] 외부 YouTube 영상 심층 검토 완료하기

## 진행 내용

### 1. Roadmap 및 로컬 맥락 검토

Daily Learning Prompt, Roadmap, Topic starter 자료, Live22 학습 자료, 기존 Seattle-Tech-Week-2026 Topic 파일을 읽었다. 이를 통해 M1에서는 기사 초안을 쓰지 않아야 하며, M2 교차 읽기를 지원하는 소스 맵을 만드는 것이 올바른 산출물임을 확인했다.

### 2. 외부 리서치 갱신

웹 검색과 직접 열람으로 현재 공개 출처를 확인했다.

- Luma / Seattle Tech Week 공식 캘린더: 2026-08-10 기준 2027 날짜는 여전히 TBD다.
- Madrona LinkedIn 호스트 모집 공지: 2026년은 네 번째 Seattle Tech Week로 설명되었고, 호스트 등록이 캘린더 공개 및 참석자 등록보다 먼저 열렸다.
- GeekWire Seattle Tech Week 태그와 현장 노트: 외부 보도는 250개 이상 이벤트 속에서 AI가 주간 전체의 지배적 흐름이었다고 설명한다.
- AI2Work 인프라 분석: AI 인프라, 전력, 비용, 오케스트레이션, 평가, 지역 벤처 긴장을 핵심 이야기로 해석한다.
- GeekWire Tech Universe Map: 시애틀 생태계의 인재 계보와 AI 허브 문제를 보여준다.

### 3. 생성한 M1 산출물

- `01-Source-Map-Research/README.md`: M1 학습 순서와 모듈 목적
- `01-Source-Map-Research/source-maps/01-official-and-articles.md`: 공식 자료 및 기사 소스 맵
- `01-Source-Map-Research/source-maps/02-external-youtube.md`: 외부 YouTube 소스 맵
- `01-Source-Map-Research/source-maps/03-catchupai-video-transcripts.md`: 사용자 직접 녹화 영상 및 Transcript 소스 맵
- `01-Source-Map-Research/verification-gaps.md`: 확인 필요 사실과 피해야 할 주장

## 문제 해결 기록

### 문제 1: 로컬 자료에 이미 외부 리서치가 포함되어 있음

**증상**: Live22 학습 자료에는 이미 성숙한 외부 출처 요약이 들어 있었다. 이를 그대로 다시 작성하면 중복 작업이 된다.

**해결**: 해당 문서를 seed 자료로 보고, 변동 가능성이 높은 항목인 2027 날짜, Luma 캘린더 상태, 외부 기사 프레이밍을 현재 기준으로 갱신했다. M1 산출물은 기존 자료를 보존하면서 M2에서 쓰기 좋게 재구성했다.

### 문제 2: 출처마다 이벤트 수가 다름

**증상**: 로컬 Luma 추출은 전체 이벤트 242개와 AI 태그 이벤트 77개를 말하고, GeekWire는 250개 이상 이벤트를 보도한다.

**해결**: 이 차이를 `verification-gaps.md`에 분리했고, 안전한 표현을 지정했다. “2026-07-24 로컬 추출에서는 242개, 이후 GeekWire 보도에서는 250개 이상”으로 쓴다.

## DoD 체크리스트

Roadmap M1 완료 기준:

- [x] 공식/기사 소스 맵 생성
- [x] 외부 YouTube 소스 맵 생성
- [x] 사용자 영상/Transcript 소스 맵 생성
- [x] 각 소스에 최소 1개 이상의 1차 트렌드 태그 부여
- [x] 2027 날짜 상태와 확인 날짜 기록
- [x] 확인 필요 항목 분리
- [x] M1 WorkLog 작성
- [x] 일일 회고 작성

**완료율**: M1 소스 맵 요구사항 기준 8/8 (100%). 외부 YouTube 심층 검토는 유용한 후속 작업이지만 M1 완료 필수 조건은 아니다.

## 일일 회고

### 잘된 점

- Topic에 이미 강한 seed 문서가 있어서, M1은 전체 영역을 다시 발견하기보다 구조화와 검증에 집중할 수 있었다.
- 공식/기사 소스와 로컬 녹화 자료를 분리하니 다음 모듈의 역할이 명확해졌다. M2는 공개 생태계 서사와 사용자의 현장 증거를 비교해야 한다.

### 개선할 점

- 일부 로컬 리서치 파일에는 발표자 이름, 소속, 영상 공개 허가와 관련된 확인 메모가 남아 있다. 최종 기사 주장 전에 이 항목을 처리해야 한다.

### 인사이트

- 가장 강한 기사 각도는 “Seattle Tech Week에 AI 이벤트가 많았다”가 아니다. 더 강한 각도는 공개 보도가 AI를 생태계/인프라 문제로 강조하는 동안, 사용자의 녹화 자료는 그 인프라 문제가 빌더 워크플로, 신뢰 점검, 의사결정 과학, 소비자 온보딩으로 어떻게 내려오는지를 보여준다는 점이다.
- 2027 준비는 날짜 발표가 아니라 워크플로 카드로 다뤄야 한다. 공식 날짜가 아직 TBD이기 때문이다.

### 다음 집중 작업

- M2 - 트렌드 분석 및 교차 읽기를 시작한다.
- 최소 다섯 개의 트렌드 카드를 만든다: 인프라/비용, 빌더 생태계, 신뢰/평가, 의사결정 과학, 소비자 AI, 커뮤니티/워크플로.
- 기사 구조를 쓰기 전에 외부 자료 vs 현장 기록 비교표를 먼저 만든다.

## 참고 자료 및 산출물

**산출물**:
- `01-Source-Map-Research/README.md`
- `01-Source-Map-Research/source-maps/01-official-and-articles.md`
- `01-Source-Map-Research/source-maps/02-external-youtube.md`
- `01-Source-Map-Research/source-maps/03-catchupai-video-transcripts.md`
- `01-Source-Map-Research/verification-gaps.md`

**외부 참고 자료**:
- https://luma.com/seattletechweek2026
- https://www.linkedin.com/posts/madrona-ventures_seattle-tech-week-2026-is-coming-and-today-activity-7448037111108124672-h1Ka
- https://www.geekwire.com/tag/seattle-tech-week/
- https://www.geekwire.com/2026/seattle-tech-week-takeaways-ai-startups-and-the-best-insights-and-quotes-we-heard/
- https://www.geekwire.com/2026/new-map-traces-washington-states-tech-universe-to-a-few-key-hubs-and-shows-whats-at-risk/
- https://ai2.work/blog/seattle-tech-week-opens-with-ai-infrastructure-as-the-real-story

**작성자**: Codex  
**방법론**: VibeLearn AI
