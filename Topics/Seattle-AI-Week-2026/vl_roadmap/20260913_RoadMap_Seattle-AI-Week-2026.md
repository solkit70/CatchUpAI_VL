# Seattle-AI-Week-2026 학습 로드맵

**생성일**: 2026-09-13 (Live #27 방송 중)
**방법론**: VibeLearn AI
**버전**: 1.0

---

## 📊 학습 기간 적정성 분석

**사용자 입력 기간**: 12주 (2026-09-13 → 12-06) · 약 48시간 — AI 가 9주를 제안했고 사용자가 「2. 기간 조정」으로 사후 콘텐츠 기간을 11월 말까지 늘렸다 (9/13)
**Topic 복잡도**: 복잡 — 사전 조사·큐레이션·티켓, 현장 5일 녹화 운영, 세션별 자막 영상, 세 소스 종합, 매체 3종 콘텐츠. 행사 날짜(10/26~30)가 고정돼 있다
**권장 기간**: 8~12주

**분석 결과**: ✅ **적정함.** 행사를 축으로 사전(M1~M3) · 현장(M4) · 사후(M5~M7)로 나뉜다. 사후를 5주로 늘린 만큼 M7 은 매체 3종을 각 1편 이상 내는 데 여유가 생긴다.

**조치 제안**: 계획대로 진행한다. 단 **M2(참가 일정·티켓)는 9/27 전에 끝낸다** — 얼리버드·매진이 이미 시작됐다. 이 Topic 은 Live-CoMC-App Retrospective 의 방법론 개선 제안 4건(실소요 기록 · 직전 회고 체크 · 모듈마다 실물 1건 DoD · `[실측]/[문서]/[추론]` 표기)을 적용하는 두 번째 Topic 이다.

---

## 📚 학습 개요

### Topic 소개
2026-10-26~30 Seattle AI Week(WTIA 주최, 75+ 행사, 5,000+ 참가)에 **「배우기」를 첫째 목표**로 참가한다. 사전에 Luma 전수 수집 → 큐레이션 → 참가 일정·티켓 확정, 현장에서는 세션 녹화 + 그날그날 현장 정리, 사후에 녹화본을 한국어 자막 유튜브 영상으로 올리고, **Transcript · 현장 정리 · 외부 언론 보도** 세 소스를 종합해 **「행사 소개 · 진행 상황 · 취재 내용 · 2026 시애틀 AI 트렌드」** 콘텐츠를 **유튜브 영상 · 신문 기사 · Substack 글**로 낸다. 7월 Seattle Tech Week 두 Topic(참가 계획 · 기사 연재)의 파이프라인을 재사용한다.

사용자 원문: `Materials_For_Topics/Seattle-AI-Week-2026/2026-09-13 참가 목표 (구술 원문).md`
행사 사실표: `Materials_For_Topics/Seattle-AI-Week-2026/2026-09-13 행사 사실표.md`

### 학습 목표
- [ ] Luma 캘린더 전수(75+)를 API 로 수집해 날짜·시간·가격·온/오프라인·녹화 정책이 있는 사실표를 만들고, 「배울 것」 기준으로 우선순위 큐레이션을 할 수 있다
- [ ] 10/26~30 참가 일정을 확정해 티켓(Opening $125 · Summit $225 등)을 얼리버드 안에 사고 Google Calendar 에 등록할 수 있다
- [ ] 녹화 장비·허가·저장·백업 절차와 일일 현장 정리 템플릿을 리허설로 검증해, 현장 5일을 사고 없이 운영할 수 있다
- [ ] 녹화본을 `video-subtitles` 파이프라인으로 한국어 자막 유튜브 영상으로 올릴 수 있다 (세션당 목표 리드타임 3일)
- [ ] Transcript · 현장 정리 · 외부 보도 세 소스를 Evidence Bank 로 종합해 「2026 시애틀 AI 트렌드」를 근거 표기로 정리할 수 있다
- [ ] 콘텐츠 4축을 유튜브 영상 · 신문 기사 · Substack 글로 각 1편 이상 내고 claim ledger 로 출처를 댈 수 있다

### 예상 학습 기간
12주 (2026-09-13 → 12-06) · 약 48시간 — 사전 6주 8h · 현장 1주 15h · 사후 5주 25h

### 학습 환경
- OS: Windows 11 Home 10.0.26200
- 도구: Luma 공개 API + `web-data-extraction` 스킬 · Google Calendar MCP · 녹화 장비(M3 확정) · `video-subtitles` 스킬(ffmpeg · Remotion) · `youtube-transcript-summarizer` · Substack · Obsidian
- 사전 지식: Tech Week 두 Topic 의 절차 · `video-subtitles` 실사용(9/10~12) / 권장: 녹화 에티켓 · `youtube-sns-promo` · 2026 상반기 시애틀 AI 배경

---

## 🗺️ 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 | 기한 |
|------|--------|--------|----------|------------|------|
| M1 | 행사 전수 수집과 사실표 | ⭐⭐ | 3h | `01-Event-Research/` | 9/20 |
| M2 | 큐레이션 · 참가 일정 · 티켓 · 캘린더 | ⭐⭐ | 3h | `02-Curation-and-Schedule/` | **9/27** |
| M3 | 녹화·현장 정리 리허설 | ⭐⭐ | 2h | `03-Field-Kit-Rehearsal/` | 10/18 |
| M4 | 현장 5일 운영 | ⭐⭐⭐ | 15h | `04-Field-Week/` | 10/26~30 |
| M5 | 자막 영상 — 세션별 전사·한국어 자막·유튜브 | ⭐⭐⭐ | 9h | `05-Subtitled-Videos/` | 11/15 |
| M6 | 종합 — 외부 보도 · Evidence Bank · 2026 시애틀 AI 트렌드 | ⭐⭐⭐ | 7h | `06-Synthesis/` | 11/22 |
| M7 | Capstone — 콘텐츠 4축 × 매체 3종 + Retrospective | ⭐⭐⭐ | 9h | `07-Content-Capstone/` | 12/6 |

**총 예상 시간**: 48시간 (모듈마다 버퍼 20% 포함)

**리듬**: 사전(M1~M3, 8h)은 주 1회 · 현장(M4)은 하루 3h × 5일 · 사후(M5~M7, 25h)는 주 5h. **M5 는 M4 둘째 날부터 병행** — 첫 세션 녹화본을 이튿날 자막 파이프라인에 넣어 리드타임 3일을 지킨다.

---

## 📖 모듈별 상세 계획

### M1 - 행사 전수 수집과 사실표

**난이도**: ⭐⭐
**예상 시간**: 3h
**산출물 폴더**: `01-Event-Research/`

#### 학습 목표
- [ ] Luma 캘린더의 `calendar_api_id` 를 찾아 API 로 전수(75+)를 JSON 으로 받을 수 있다
- [ ] 행사마다 날짜·시간·장소·온/오프라인·가격·주최·**녹화 정책(있으면)** 이 있는 사실표를 만들 수 있다
- [ ] Opening · Summit · Frontier Day · GTM Day 등 메인 행사와 커뮤니티 행사를 구분하고, 얼리버드 마감을 표시할 수 있다

#### 주요 개념
1. **화면이 아니라 원천**: Luma 페이지는 JS 렌더라 WebFetch 로는 날짜가 안 나온다 `[실측 09-13]`. `api.luma.com/calendar/get-items?calendar_api_id=…&period=future` 가 원천 `[Tech Week 실측]`
2. **사실표는 판단을 안 한다**: 큐레이션(M2)과 분리. 사실표 열에 "추천"이 있으면 안 된다
3. **녹화 정책은 행사마다 다르다**: 세션 페이지·주최자 안내에 "no recording" 이 있는지 지금 적어 둬야 M3·M4 에서 놀라지 않는다 `[추론 — M1 에서 확인]`
4. **Tech Week 선례 재사용**: `Seattle-Tech-Week-2026/04-Process-Notes/claude-code-to-codex-automation.md` 의 절차 — 어디까지 그대로 되는지 먼저 시험

#### 실습 과제

**실습 1: calendar_api_id 찾기 + 전수 수집** ⭐⭐
- **목적**: 75+ 행사를 손으로 안 베끼고 받는다
- **단계**: ① `web-data-extraction` 스킬 로드 ② Luma 페이지 HTML/네트워크에서 `cal-…` id 확보 (WebFetch 로 안 나오면 사용자가 브라우저 개발자도구 Network 탭에서 `get-items` 요청 URL 을 복사) ③ API JSON 을 `vl_materials/luma-events-YYYYMMDD.json` 으로 저장 ④ Tech Week 스크립트를 재사용해 `examples/events-auto.md` 생성
- **예상 시간**: 60분
- **검증**: JSON 의 행사 수가 페이지의 "75+" 와 맞거나 차이가 설명된다

**실습 2: 사실표** ⭐⭐
- **목적**: 판단 없는 원장
- **단계**: `guides/events-table.md` — 열: 날짜 · 시간 · 이름 · 주최 · 장소/온라인 · 가격/얼리버드 마감 · 링크 · 녹화 정책(확인/미확인) · 비고. 메인 행사 6개는 개별 페이지를 열어 세부(연사·프로그램)를 `guides/main-events.md` 에
- **예상 시간**: 60분
- **검증**: 모든 행에 링크가 있고, 녹화 정책 열이 「확인/미확인」으로 채워져 있다 (빈칸 없음)

**실습 3: 갱신 절차** ⭐
- **목적**: 행사는 10월까지 계속 추가된다 ("Submit your community events")
- **단계**: 실습 1 을 한 명령으로 재실행할 수 있게 `examples/fetch_luma.py` 정리 → 주 1회 재수집 · 차이만 `guides/changes.md` 에
- **예상 시간**: 30분
- **검증**: 두 번째 실행에서 「추가/변경/삭제」가 나온다 (0건이어도 표시)

#### 산출물
```
01-Event-Research/
├── README.md
├── examples/
│   ├── fetch_luma.py          ← API 수집 (Tech Week 재사용)
│   └── events-auto.md         ← 자동 생성 목록
├── guides/
│   ├── events-table.md        ← 사실표 (판단 없음)
│   ├── main-events.md         ← 메인 6개 세부
│   └── changes.md             ← 재수집 차이 로그
└── troubleshooting/
    └── luma-api-notes.md      ← id 찾기 · 페이지네이션 · 실패 사례
```

#### Definition of Done
- [ ] API JSON 원본이 `vl_materials/` 에 있다
- [ ] 사실표 — 녹화 정책 열 포함, 빈칸 없음
- [ ] 🔴 실물 1건: `fetch_luma.py` 실행 로그와 행사 수
- [ ] 재수집 절차 1회 재실행
- [ ] README · 링크 검사 통과 (`python scripts/check_links.py Topics/Seattle-AI-Week-2026`)
- [ ] WorkLog — 헤더에 실소요 · Daily Retrospective

#### Self-Assessment
**개념 이해**: Luma 화면과 API 의 차이를 한 문장으로 / **실무 활용**: 새 Luma 캘린더를 받으면 10분 안에 전수 JSON 을 낼 수 있는가 / **문제 해결**: API 가 막히면 다음 원천은 무엇인가

#### 예상 시간 배분
- 개념: 20분 · 실습 1: 60분 · 실습 2: 60분 · 실습 3: 30분 · 문서화: 20분 — **합계 3h10m** (표 3h)

#### 참조 자료
- `Topics/Seattle-Tech-Week-2026/04-Process-Notes/claude-code-to-codex-automation.md` · `01-Event-Research/events-auto.md`
- `_Settings_/Skills/web-data-extraction/SKILL.md`
- https://luma.com/Seattle-AI-Week-2026 · https://www.seattleaiweek.com

---

### M2 - 큐레이션 · 참가 일정 · 티켓 · 캘린더

**난이도**: ⭐⭐
**예상 시간**: 3h
**산출물 폴더**: `02-Curation-and-Schedule/`
**기한**: **2026-09-27** (얼리버드 · 매진)

#### 학습 목표
- [ ] 「내가 배울 것」 기준으로 행사에 우선순위(A/B/C)를 매기고 이유를 한 줄씩 붙일 수 있다
- [ ] 시간 충돌을 풀어 10/26~30 일자별 참가 일정을 확정하고, 녹화 가능 세션을 표시할 수 있다
- [ ] 티켓을 사고(Opening · Summit · 유료 세션) Google Calendar 에 등록해 실물 증거를 남길 수 있다

#### 주요 개념
1. **큐레이션 기준 = 배움**: 사용자 원문 1순위. 취업·네트워킹은 부차 기준 `[원문]`
2. **녹화 가능성이 일정에 들어간다**: 같은 시간대면 녹화 허용 세션을 고른다 — 이 Topic 의 산출물이 영상이기 때문
3. **매진은 지금 시작됐다**: 해커톤 이미 sold out `[실측 09-13]`. 결정을 미룰수록 선택지가 준다
4. **Tech Week 선례**: `02-Curation/priority-review.md` 의 표 형식과 `03-Schedule/final.md` 의 캘린더 등록 절차

#### 실습 과제

**실습 1: 우선순위 리뷰** ⭐⭐
- **단계**: 사실표 → A(꼭) / B(가능하면) / C(제외) · 이유 한 줄 · 배울 것 키워드 · 녹화 가능 여부 → `guides/priority-review.md`. **사용자 검토 게이트** — AI 가 A 를 정하지 않는다
- **예상 시간**: 60분
- **검증**: A 등급 전부에 사용자 승인 표시

**실습 2: 일자별 일정 + 충돌 해결** ⭐⭐
- **단계**: 10/26~30 시간표 → 충돌은 「녹화 가능 > 배움 > 무료」 순으로 해결 → 이동 시간·식사·녹화 배터리 교체 슬롯 → `guides/schedule-final.md`
- **예상 시간**: 45분
- **검증**: 하루에 겹치는 세션이 없고 이동 시간이 계산돼 있다

**실습 3: 티켓 + 캘린더** ⭐
- **단계**: 티켓 구매(사용자) → 영수증/확인 메일 요약을 `guides/tickets.md` (금액·주문번호·환불 조건, 개인정보 제외) → Google Calendar MCP 로 일정 등록 → 링크 기록
- **예상 시간**: 45분
- **검증**: 캘린더에 5일 일정이 보이고 티켓 확인 메일이 있다

#### 산출물
```
02-Curation-and-Schedule/
├── README.md
└── guides/
    ├── priority-review.md     ← A/B/C · 이유 · 녹화 가능
    ├── schedule-final.md      ← 일자별 확정 일정 + 캘린더 링크
    └── tickets.md             ← 구매 내역 (개인정보 제외)
```

#### Definition of Done
- [ ] 우선순위표 — A 등급 사용자 승인
- [ ] 일자별 일정 확정 · 충돌 0
- [ ] 🔴 실물 1건: 티켓 구매 확인 + Google Calendar 등록
- [ ] README · 링크 검사 통과
- [ ] WorkLog(실소요) · Daily Retrospective · 직전 「개선할 점」 체크

#### Self-Assessment
**개념 이해**: 큐레이션 기준 3개를 우선순위 순으로 / **실무 활용**: 새 행사가 추가되면 30초 안에 등급을 매길 수 있는가 / **문제 해결**: 세션이 매진되면 대안 세션이 표에 있는가

#### 예상 시간 배분
- 개념: 15분 · 실습 1: 60분 · 실습 2: 45분 · 실습 3: 45분 · 문서화: 15분 — **합계 3h**

#### 참조 자료
- `Topics/Seattle-Tech-Week-2026/02-Curation/priority-review.md` · `03-Schedule/final.md`
- Google Calendar MCP (`mcp__claude_ai_Google_Calendar__*`)

---

### M3 - 녹화·현장 정리 리허설

**난이도**: ⭐⭐
**예상 시간**: 2h
**산출물 폴더**: `03-Field-Kit-Rehearsal/`
**기한**: 10/18

#### 학습 목표
- [ ] 녹화 장비(폰/카메라·마이크·배터리·저장)·허가 문구·백업 절차를 목록으로 만들고 1회 리허설로 검증할 수 있다
- [ ] 일일 현장 정리 템플릿(세션 · 핵심 3줄 · 인용 · 질문 · 사진 · 외부 링크)을 만들어 폰에서 5분 안에 채울 수 있다
- [ ] 녹화본 1개를 `video-subtitles` 파이프라인에 넣어 자막 영상까지 한 번 돌려 리드타임을 잰다

#### 주요 개념
1. **허가는 문장으로 준비한다**: "이 세션을 개인 학습·한국어 자막 공유용으로 녹화해도 될까요" — 거절당하면 메모로 전환
2. **백업은 현장에서**: 하루 끝에 클라우드/외장으로. 5일치를 마지막 날 옮기면 사고가 난다 `[추론]`
3. **현장 정리는 그날 밤**: 원문 4번 — "그날 그날 정리". 다음 날로 넘기면 안 쓴다
4. **리드타임 3일**: 녹화 → 전사 → 번역 → 검토 게이트(Step 1.7) → 렌더 → 업로드. Anusua Trivedi 42:50 편이 이틀 걸렸다 `[실측 9/10~12]`

#### 실습 과제

**실습 1: 장비·허가·백업 체크리스트** ⭐
- **단계**: `guides/field-kit.md` — 장비표(무엇·배터리·용량·예비) · 허가 문구(영어) · 저장 경로(`C:/Users/dougg/Videos/SeattleAIWeek2026/DAY-N/`) · 백업 규칙 · 하루 루틴
- **예상 시간**: 30분
- **검증**: 목록의 각 항목에 「확인함」 날짜

**실습 2: 일일 현장 정리 템플릿** ⭐
- **단계**: `templates/daily-field-note.md` — 세션명·시간·연사 / 핵심 3줄 / 인용(원문) / 내 질문 / 사진·슬라이드 / 외부 링크 / 녹화 파일명. 폰에서 채워 보는 리허설 1회
- **예상 시간**: 30분
- **검증**: 5분 안에 한 세션분을 채웠다 (시간 기록)

**실습 3: 파이프라인 예행** ⭐⭐
- **단계**: 리허설 녹화(10분짜리 아무 영어 영상 또는 Builders Lounge 세션) → `video-subtitles` 스킬 전 구간 → 유튜브 비공개 업로드 → 소요 시간 기록 → `guides/pipeline-dry-run.md`
- **예상 시간**: 60분 (렌더 대기 포함)
- **검증**: 비공개 유튜브 링크와 구간별 소요 시간

#### 산출물
```
03-Field-Kit-Rehearsal/
├── README.md
├── templates/
│   └── daily-field-note.md
└── guides/
    ├── field-kit.md
    └── pipeline-dry-run.md
```

#### Definition of Done
- [ ] 장비·허가·백업 체크리스트 (확인 날짜)
- [ ] 현장 정리 템플릿 + 5분 리허설
- [ ] 🔴 실물 1건: 예행 자막 영상 비공개 링크
- [ ] README · 링크 검사 통과
- [ ] WorkLog(실소요) · Daily Retrospective · 직전 「개선할 점」 체크

#### Self-Assessment
**개념 이해**: 현장 하루 루틴을 순서대로 말할 수 있다 / **실무 활용**: 녹화 거절당했을 때 대안이 정해져 있다 / **문제 해결**: 저장 공간이 차면 어디로 옮기는지 안다

#### 예상 시간 배분
- 실습 1: 30분 · 실습 2: 30분 · 실습 3: 60분 — **합계 2h**

#### 참조 자료
- `_Settings_/Skills/video-subtitles/SKILL.md` · `AI/RemotionStudio/_staging/securityai-0910-entoko/` (9/12 실사용 흔적)
- `Topics/Seattle-Tech-Week-2026-Article-Writing/05c-User-Perspective/` (현장 관점 기록 선례)

---

### M4 - 현장 5일 운영

**난이도**: ⭐⭐⭐
**예상 시간**: 15h (하루 3h × 5)
**산출물 폴더**: `04-Field-Week/`
**기간**: **10/26(월)~30(금)**

#### 학습 목표
- [ ] 확정 일정대로 참가하며 허가된 세션을 녹화하고, 매일 밤 백업과 현장 정리를 마칠 수 있다
- [ ] 그날 나온 외부 보도·SNS·주최 측 자료 링크를 매일 수집할 수 있다
- [ ] 계획과 실제의 차이(놓친 세션 · 즉흥 참가 · 녹화 거절)를 기록할 수 있다

#### 주요 개념
1. **배움이 먼저, 녹화는 도구**: 녹화에 신경 쓰다 내용을 놓치면 본말전도 — 삼각대·자동 녹화로 손을 비운다
2. **그날 밤 세 가지**: 백업 · 현장 정리 · 첫 녹화본 파이프라인 투입(M5 병행)
3. **외부 보도는 행사 중에 가장 많다**: GeekWire · Seattle Times · LinkedIn 포스트 — 링크만이라도 그날 모은다
4. **차이 기록이 Retrospective 재료**

#### 실습 과제

**실습 1: 일일 루틴 × 5** ⭐⭐⭐
- **단계**: 아침: 오늘 일정·장비 확인 → 현장: 녹화·메모·사진 → 밤: 백업 → `daily/DAY-N.md`(템플릿) → 외부 링크 `daily/DAY-N.md#외부` → 내일 계획 조정
- **예상 시간**: 하루 3h (참가 시간 제외)
- **검증**: 5일치 `DAY-1~5.md` 와 녹화 파일 목록

**실습 2: 첫 자막 영상 병행 착수** ⭐⭐
- **단계**: DAY-1 녹화본 하나를 DAY-2 아침에 전사 시작 (M5 실습 1) — 리드타임 3일 검증
- **검증**: DAY-4 에 첫 영상 업로드

**실습 3: 차이 로그** ⭐
- **단계**: `guides/plan-vs-actual.md` — 계획/실제/이유/다음에
- **검증**: 5일 전부

#### 산출물
```
04-Field-Week/
├── README.md
├── daily/
│   ├── DAY-1.md … DAY-5.md    ← 현장 정리 (템플릿)
├── guides/
│   ├── recordings-index.md    ← 파일명 · 세션 · 길이 · 허가 · 백업 위치
│   └── plan-vs-actual.md
└── (녹화 파일은 볼트 밖)
```

#### Definition of Done
- [ ] DAY-1~5 현장 정리 · 매일 밤 작성
- [ ] 녹화 인덱스 · 백업 완료 표시
- [ ] 🔴 실물 1건: 녹화 파일 5일치 목록 + 첫 자막 영상 업로드(DAY-4)
- [ ] 외부 보도 링크 일별 수집
- [ ] 차이 로그 5일
- [ ] WorkLog(일별 실소요) · 각 날 짧은 Retrospective

#### Self-Assessment
**개념 이해**: 오늘 배운 것 3가지를 녹화 없이도 말할 수 있는가 / **실무 활용**: 내일 일정을 오늘 밤 조정했는가 / **문제 해결**: 장비 사고 1건을 현장에서 풀었는가

#### 예상 시간 배분
- 5일 × (아침 20분 · 밤 2h30m) ≈ **15h**

#### 참조 자료
- M2 `schedule-final.md` · M3 `field-kit.md` · `templates/daily-field-note.md`

---

### M5 - 자막 영상 — 세션별 전사·한국어 자막·유튜브

**난이도**: ⭐⭐⭐
**예상 시간**: 9h
**산출물 폴더**: `05-Subtitled-Videos/`
**기한**: 11/15

#### 학습 목표
- [ ] 허가된 녹화본을 `video-subtitles` 스킬로 전사 → 번역(용어집 되먹임) → 검토 게이트 → 렌더 → 업로드할 수 있다
- [ ] 세션당 리드타임 3일을 지키거나 못 지킨 이유를 기록할 수 있다
- [ ] 영상마다 업로드 자료(제목·설명·태그·타임스탬프·출처)와 SNS 홍보 글을 만들 수 있다

#### 주요 개념
1. **검토 게이트(Step 1.7)는 건너뛰지 않는다**: 고유명사·수치 오류는 여기서만 잡힌다 `[실측 9/10~12 — 4회 교정]`
2. **용어집 누적**: `glossary.json` 에 이 행사의 연사·회사·제품명을 먼저 넣는다 (M1 main-events 에서)
3. **긴 영상은 나눈다**: 15분 이하가 시청 유지율에 유리 `[YouTube Topic 실측]` — 세션은 챕터 또는 분할
4. **업로드 = 공개 전 자료 문서**: 유튜브 업로드 자료 문서 선례(`AI/Research/…유튜브 업로드 자료`)

#### 실습 과제

**실습 1: 첫 영상 — 리드타임 측정** ⭐⭐⭐ (M4 DAY-2 착수)
**실습 2: 나머지 세션 배치 처리** ⭐⭐⭐ — 우선순위: 배움 A 등급 · 허가 확실 · 음질 양호
**실습 3: 업로드 자료 + 홍보** ⭐⭐ — `youtube-sns-promo` 스킬, 플랫폼 순서대로

#### 산출물
```
05-Subtitled-Videos/
├── README.md                   ← 영상 목록 · 유튜브 링크 · 리드타임
├── guides/
│   ├── lead-time-log.md
│   └── glossary-additions.md   ← 이 행사에서 추가한 용어
└── upload/
    └── {session}-upload.md     ← 제목·설명·태그·타임스탬프
```

#### Definition of Done
- [ ] 영상 ≥ 3편 공개 (허가·음질에 따라 조정, 이유 기록)
- [ ] 리드타임 로그
- [ ] 🔴 실물 1건: 유튜브 링크
- [ ] 용어집 되먹임 · 업로드 자료 문서 · 홍보 글 ≥ 1편
- [ ] README · 링크 검사 · WorkLog(실소요) · Retrospective

#### Self-Assessment
**개념**: 파이프라인 6단계를 순서대로 / **실무**: 검토 게이트에서 무엇을 보는지 3가지 / **문제 해결**: 전사 품질이 나쁠 때 대안(Whisper 모델 변경 · 구간 재녹음 불가 시 자막 생략)

#### 예상 시간 배분
- 실습 1: 2h · 실습 2: 5h · 실습 3: 2h — **합계 9h**

#### 참조 자료
- `_Settings_/Skills/video-subtitles/SKILL.md` · `glossary.json` · `youtube-sns-promo` 스킬
- `Topics/YouTube-Channel-Revival-With-AI/` — 길이·유지율 실측

---

### M6 - 종합 — 외부 보도 · Evidence Bank · 2026 시애틀 AI 트렌드

**난이도**: ⭐⭐⭐
**예상 시간**: 7h
**산출물 폴더**: `06-Synthesis/`
**기한**: 11/22

#### 학습 목표
- [ ] 외부 보도(언론·주최·SNS·타 참가자 글)를 클리핑해 출처·날짜·주장 단위로 Evidence Bank 에 넣을 수 있다
- [ ] Transcript · 현장 정리 · 외부 보도 세 소스를 주제별로 교차해 「일치 · 상충 · 한 소스에만」을 표시할 수 있다
- [ ] 2026 시애틀 AI 트렌드를 5~7개로 뽑아 각 트렌드에 세 소스 근거를 붙일 수 있다

#### 주요 개념
1. **세 소스의 위계**: Transcript(1차, 연사 발언) > 현장 정리(1차, 내 관찰) > 외부 보도(2차). 상충하면 1차가 이긴다 `[Tech Week 기사 선례]`
2. **Evidence Bank**: 주장 하나 = 행 하나 = 출처 링크 · 인용 · 날짜 · 소스 종류. `Seattle-Tech-Week-2026-Article-Writing/05-Evidence-Bank` 형식
3. **트렌드는 반복에서 나온다**: 여러 세션·여러 보도에 같이 나오는 것만 트렌드. 한 연사의 주장은 「관찰」
4. **"60% 이상" 교훈**: 2차 출처의 숫자를 훅으로 쓰지 않는다 — 1차 확인 `[9/6 Learnings]`

#### 실습 과제

**실습 1: 외부 보도 수집·클리핑** ⭐⭐ — WebSearch/WebFetch · `Ingest/Clippings/` · 최소 10건 · 출처 종류 표시
**실습 2: Evidence Bank** ⭐⭐⭐ — 세 소스 → `guides/evidence-bank.md` (주장 · 출처 · 소스종류 · 날짜 · 신뢰)
**실습 3: 트렌드 5~7개** ⭐⭐⭐ — `guides/seattle-ai-trends-2026.md` — 트렌드마다 근거 ≥ 3 (소스 2종 이상) · 반례 · 사용자 관점

#### 산출물
```
06-Synthesis/
├── README.md
└── guides/
    ├── external-coverage.md    ← 보도 목록 · 출처 종류
    ├── evidence-bank.md
    └── seattle-ai-trends-2026.md
```

#### Definition of Done
- [ ] 외부 보도 ≥ 10건 클리핑
- [ ] Evidence Bank — 세 소스 전부 포함 · 상충 표시
- [ ] 🔴 실물 1건: 트렌드 문서 (근거 표기 완비)
- [ ] README · 링크 검사 · WorkLog(실소요) · Retrospective

#### Self-Assessment
**개념**: 세 소스 위계를 이유와 함께 / **실무**: 트렌드 하나를 근거 3개로 30초 안에 방어 / **문제 해결**: 보도와 Transcript 가 다를 때 어느 쪽을 쓰나

#### 예상 시간 배분
- 실습 1: 2h · 실습 2: 3h · 실습 3: 2h — **합계 7h**

#### 참조 자료
- `Topics/Seattle-Tech-Week-2026-Article-Writing/05-Evidence-Bank` · `05b-External-Coverage` · `08-Factcheck-Package`
- `youtube-transcript-summarizer` 스킬 (외부 영상 소스)

---

### M7 - Capstone — 콘텐츠 4축 × 매체 3종 + Retrospective

**난이도**: ⭐⭐⭐
**예상 시간**: 9h
**산출물 폴더**: `07-Content-Capstone/`
**기한**: 12/6

#### 학습 목표
- [ ] 콘텐츠 매트릭스(4축 × 3매체)에서 실제로 낼 것을 고르고 각각 claim ledger 를 붙일 수 있다
- [ ] 유튜브 종합 영상 1편(Remotion, 한국어) · 신문 기사 1편 · Substack 글 1편을 완성해 공개(또는 투고)할 수 있다
- [ ] Topic Retrospective — 실소요 vs 48h · 목표 6개 · 방법론 · 개선 제안 ≥ 2

#### 주요 개념
1. **콘텐츠 매트릭스**: 행 = 행사 소개 · 진행 상황 · 취재 내용 · 트렌드 / 열 = 유튜브 · 기사 · Substack. 12칸 중 낼 것 3~5칸
2. **매체마다 톤이 다르다**: 기사(3인칭 · 팩트) · Substack(1인칭 · 관점) · 영상(서사) — Tech Week 기사 연재의 시리즈 설계
3. **claim ledger**: 모든 주장 → Evidence Bank 행 번호
4. **실명 동의**: 기사에 타인 실명·발언을 쓰면 동의 필요 — Tech Week Substack 게시가 여기서 멈춰 있다 `[실측]`

#### 실습 과제

**실습 1: 콘텐츠 매트릭스 + 선택** ⭐⭐ — `guides/content-matrix.md` · 사용자 승인
**실습 2: 종합 영상** ⭐⭐⭐ — `remotion-video` 스킬 · 슬라이드 플랜 → 오디오 → 렌더 · 밝기 대역 원장 확인 · 유튜브 공개
**실습 3: 기사 + Substack** ⭐⭐⭐ — 기사 1편(투고처 정하기 · 실명 동의 목록) · Substack 1편 · 각 claim ledger
**실습 4: Topic Retrospective** ⭐⭐ — `vl_worklog/YYYYMMDD_Seattle-AI-Week-2026_Final_Retrospective.md`

#### 산출물
```
07-Content-Capstone/
├── README.md                  ← 공개 링크 전부
├── guides/
│   ├── content-matrix.md
│   ├── claim-ledger.md
│   └── consent-list.md        ← 실명·발언 동의
├── article/
│   └── {title}.md
└── substack/
    └── {title}.md
```
(Remotion 프로젝트는 `AI/RemotionStudio/`)

#### Definition of Done
- [ ] 매트릭스 승인 · 선택 3~5칸
- [ ] 🔴 실물: 유튜브 종합 영상 URL · 기사 1편(투고 또는 게시) · Substack 1편(게시)
- [ ] claim ledger 전 주장 · 동의 목록
- [ ] Topic Retrospective (실소요 합계 · 개선 제안 ≥ 2)
- [ ] 🔴 **Topic 최상위 README.md** — 무엇을 알아냈는지 · 모듈 순서 · 공개 링크 전부
- [ ] 링크 검사 (Topic 전체) · WorkLog · Retrospective

#### Self-Assessment
**개념**: 4축 × 3매체 중 왜 그 칸을 골랐는지 / **실무**: 기사의 주장 하나를 ledger 로 즉시 방어 / **문제 해결**: 동의를 못 받은 인용의 대안

#### 예상 시간 배분
- 실습 1: 1h · 실습 2: 3.5h · 실습 3: 3.5h · 실습 4: 1h — **합계 9h**

#### 참조 자료
- `Topics/Seattle-Tech-Week-2026-Article-Writing/06-Series-Design` · `07-Articles` · `08-Factcheck-Package`
- `_Settings_/Skills/remotion-video/` · `youtube-sns-promo`
- `Topics/Seattle-Tech-Week-2026/README.md` (영상 2편 선례)

---

## 📝 WorkLog 작성 가이드

**파일명**: `vl_worklog/YYYYMMDD_MX_Seattle-AI-Week-2026.md` (M4 는 `YYYYMMDD_M4-DAY-N_…`)

**필수 섹션**: 1. 세션 개요 — **날짜 · 시작·종료 · 실소요(사용자 대기 분리)** 2. 직전 WorkLog 「개선할 점」 체크 3. 오늘의 목표 4. 진행 내용(`[실측]/[문서]/[추론]`) 5. 문제 해결 로그 6. DoD 7. Daily Retrospective 8. 참조·산출물

---

## 🔍 Retrospective 가이드

- **Daily** (5-10분): What went well · improve · Insights · Tomorrow's focus — M4 는 매일 밤
- **Module** (15-20분): 계획 대비 실제(실소요) · 핵심 학습 · 문제 · Roadmap 정확도 · 다음 준비
- **Topic** (30-60분): `vl_worklog/YYYYMMDD_Seattle-AI-Week-2026_Final_Retrospective.md` — 실소요 vs 48h · 목표 6개 · 세 소스 종합이 실제로 콘텐츠 품질을 올렸는가 · 개선 제안

---

## 📂 전체 폴더 구조

```
Seattle-AI-Week-2026/
├── README.md                     # 🔴 Topic 을 닫을 때 (M7 DoD)
├── topic_starter.md
├── vl_prompts/{roadmap_prompt,daily_learning_prompt}.md
├── vl_roadmap/20260913_RoadMap_Seattle-AI-Week-2026.md
├── vl_worklog/
├── vl_materials/                 # Luma JSON · 클리핑
├── 01-Event-Research/
├── 02-Curation-and-Schedule/
├── 03-Field-Kit-Rehearsal/
├── 04-Field-Week/
├── 05-Subtitled-Videos/
├── 06-Synthesis/
└── 07-Content-Capstone/
```

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | | | ⏳ | 0% | 기한 9/20 |
| M2 | | | ⏳ | 0% | **기한 9/27** — 티켓 |
| M3 | | | ⏳ | 0% | 기한 10/18 |
| M4 | | | ⏳ | 0% | 10/26~30 |
| M5 | | | ⏳ | 0% | 기한 11/15 |
| M6 | | | ⏳ | 0% | 기한 11/22 |
| M7 | | | ⏳ | 0% | 기한 12/6 |

**범례**: ⏳ 대기 · 🔄 진행 중 · ✅ 완료

---

## 🎯 성공 기준

- [ ] 모든 모듈 완료 (DoD 100%)
- [ ] 최소 7개 산출물 폴더 생성
- [ ] Topic Retrospective 작성 (실소요 포함)
- [ ] Self-Assessment 평균 ⭐⭐⭐⭐ 이상
- [ ] Capstone — 유튜브 종합 영상 1편 · 기사 1편 · Substack 1편 + 세션 자막 영상 ≥ 3편 + Topic 최상위 README
- [ ] 원문의 목표 순서대로 — **배웠는가**(트렌드 문서에 내 관점이 있는가) → 녹화·자막 공유 → 세 소스 종합 콘텐츠

---

**생성자**: Claude with VibeLearn AI
**Roadmap 버전**: 1.0
**방법론 버전**: VibeLearn AI 2.0
