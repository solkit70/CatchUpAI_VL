# Claude-Artifacts-Routines 학습 로드맵

**생성일**: 2026-09-13 (Live #27 방송 중)
**방법론**: VibeLearn AI
**버전**: 1.0

---

## 📊 학습 기간 적정성 분석

**사용자 입력 기간**: 3주 (주당 약 5시간, 총 15시간) — 원문에 기간이 없어 AI 가 제안, 사용자 승인(9/13 "1. 그대로 진행")
**Topic 복잡도**: 중간 — 기능은 둘뿐이고 실물 4건이 이미 있으나, 공식 문서 클리핑 0건 · 화면 기록 0건 · Routines 사례 1건뿐이라 확인·실험·정리가 남았고 끝이 Remotion 영상이다
**권장 기간**: 2~4주

**분석 결과**: ✅ **적정함.** 6모듈 · 15h. 9/16 BL5 발표 · 9/26 BigHug 행사 · 9/27 Personal Ops Board 착수와 겹치므로 M4 의 「두 번째 루틴」을 Personal Ops Board 의 Deadline 에이전트로 잡아 두 Topic 이 서로 재료가 되게 한다.

**조치 제안**: 계획대로 진행한다. 이 Topic 은 Live-CoMC-App Retrospective(2026-09-12)의 방법론 개선 제안 4건을 **처음 적용**한다 — ① WorkLog 헤더에 실소요 필수 ② 세션 시작 시 직전 WorkLog 「개선할 점」 체크 ③ 모듈 DoD 에 「실물 1건」 필수 ④ 확신 문장에 `[실측]/[문서]/[추론]` 표기.

---

## 📚 학습 개요

### Topic 소개
다른 Topic(Datacenter-Workforce-Programs · WA-Caregiver-Pathways)을 공부하다 "일하다 마주쳐" 쓰게 된 Claude 의 두 기능 — **Artifacts**(발행되는 웹페이지·앱, db/자산/댓글 등 런타임 기능 포함)와 **Routines**(클라우드에서 정해진 시각·조건에 스스로 도는 작업) — 를 이미 만든 실물 4건(BigHug 부스 매니저·현황판, Builders Lounge 입장 안내, AWS WBLP 주간 확인 루틴)을 출발점으로 삼아 공식 문서와 실험으로 정확히 이해하고, 더 잘·효율적으로 쓰는 사용 패턴을 정리한 뒤, 그 정보와 경험을 다른 사람에게 전달하는 Remotion 영상으로 마무리하는 Topic.

사용자 원문: `Materials_For_Topics/Claude-Artifacts-Routines/2026-09-13 시작 프롬프트 (원문).md`
실사용 인덱스: `Materials_For_Topics/Claude-Artifacts-Routines/2026-09-13 사례 인덱스.md`

### 학습 목표
- [ ] Artifacts 의 공개 범위(비공개·링크·조직·db 있음/없음)와 버전·재발행·pin·댓글 동작을 공식 문서 근거로 설명하고, 「db 연동 페이지는 왜 공유가 안 되는가」에 정확히 답할 수 있다
- [ ] 기존 Artifact 3건을 재검토해 공유 범위·버전 상태를 시크릿 창으로 검증하고, 잘못된 것을 고칠 수 있다
- [ ] Artifact 런타임 기능(db · user · assets · comments · 다중 파일)을 각각 최소 예제로 한 번씩 만들어 보고, 어떤 일에 어떤 기능이 맞는지 표로 정리할 수 있다
- [ ] Routines 의 트리거(cron · 조건) · 실행 환경 · 알림 · 비용 구조를 공식 문서 근거로 설명하고, 기존 루틴 1건(AWS WBLP)을 점검해 개선할 수 있다
- [ ] 볼트의 실제 일에서 두 번째 루틴 1건을 설계·발행해, 로컬 AI4PKM cron 과 클라우드 루틴을 언제 어느 쪽으로 쓸지 판단 기준을 세울 수 있다
- [ ] 「더 잘·효율적으로 쓰는 패턴」 가이드 1편 + Remotion 영상 1편(한국어, 5~8분)을 제작해 유튜브에 올릴 수 있다

### 예상 학습 기간
3주 (주당 약 5시간, 총 15시간) — 2026-09-13 → 10-04

### 학습 환경
- OS: Windows 11 Home 10.0.26200
- 도구: Claude Code(VS Code 확장·CLI) · claude.ai 아티팩트 갤러리·루틴 관리 · 브라우저 시크릿 창 · AI4PKM 오케스트레이터 · Remotion + edge-tts · Obsidian
- 사전 지식: Claude Code 기본 사용 · HTML/CSS/JS 읽고 고치기 · 실물 4건의 맥락 / 권장: cron 표현식 · remotion-video 스킬 · Personal-Ops-Board PRD

---

## 🗺️ 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 |
|------|--------|--------|----------|------------|
| M1 | 실물 재검토와 질문 목록 | ⭐ | 2h | `01-Inventory-and-Questions/` |
| M2 | Artifacts 공식 문서 — 공개 범위·버전·pin·댓글 | ⭐⭐ | 2.5h | `02-Artifacts-Sharing-and-Versions/` |
| M3 | Artifacts 런타임 기능 실험 — db·user·assets·comments·다중 파일 | ⭐⭐⭐ | 3h | `03-Artifacts-Capabilities-Lab/` |
| M4 | Routines — 공식 문서·기존 루틴 점검·두 번째 루틴 발행 | ⭐⭐ | 2.5h | `04-Routines-Lab/` |
| M5 | 사용 패턴 가이드 — 더 잘·효율적으로 쓰기 | ⭐⭐ | 1.5h | `05-Usage-Patterns/` |
| M6 | Capstone — Remotion 영상 「내가 몰랐던 기능을 AI 가 찾아냈다」 | ⭐⭐⭐ | 3.5h | `06-Capstone-Video/` |

**총 예상 시간**: 15시간 (모듈마다 버퍼 20% 포함)

**리듬**: M1 조사(2h) → M2~M4 문서+실험(8h) → M5 정리(1.5h) → M6 영상(3.5h). M2·M3 은 Artifacts, M4 는 Routines 로 나뉘고 M5 에서 합친다.

---

## 📖 모듈별 상세 계획

### M1 - 실물 재검토와 질문 목록

**난이도**: ⭐
**예상 시간**: 2h
**산출물 폴더**: `01-Inventory-and-Questions/`

#### 학습 목표
- [ ] 실물 4건(부스 매니저·부스 현황판·입장 안내·WBLP 루틴)의 현재 상태(버전·공유 범위·마지막 수정·실제 사용 여부)를 시크릿 창과 갤러리로 확인해 표로 적을 수 있다
- [ ] 각 실물을 만들 때 "몰라서 못 쓴 것"과 "쓰다 막힌 것"을 구분해 질문 목록으로 만들 수 있다
- [ ] 이 Topic 이 답해야 할 질문을 우선순위 순으로 10개 이내로 확정할 수 있다

#### 주요 개념
1. **실물 우선 조사**: 문서를 읽기 전에 내가 만든 것부터 다시 본다 — 질문이 구체적이어야 문서에서 답을 찾는다
2. **소유자 시점 vs 공유 시점**: 소유자 브라우저는 항상 최신을 보여 준다 `[실측 9/7]`. 공유 상태는 시크릿 창으로만 안다
3. **db 있음/없음**: 같은 세션에서 만든 두 아티팩트가 db 유무로 공유 범위가 갈렸다 `[실측 9/3]` — 이유는 아직 모른다 `[추론]`
4. **"일하다 마주친 기능"**: 지시에 도구 이름이 없었는데 AI 가 찾아 썼다 `[실측 9/1]` — 영상의 서사 축

#### 실습 과제

**실습 1: 실물 4건 상태표** ⭐
- **목적**: 지금 무엇이 어떤 상태인지 사실부터 고정한다
- **단계**:
  1. `Artifact` 도구 `action: list` 로 소유 아티팩트 목록을 뽑는다 (제목·URL·마지막 수정)
  2. 실물 3건 각각 `action: read` 로 현재 HTML 을 받아 `capabilities` 선언(db 유무 등)을 확인한다
  3. 시크릿 창에서 3건의 공유 링크를 열어 **열리는가 / 어느 버전이 보이는가**를 기록한다
  4. claude.ai/code/routines 에서 WBLP 루틴의 마지막 실행·결과·알림 여부를 확인한다
  5. `guides/inventory.md` 표로 정리 — 열: 실물 · 만든 날 · capabilities · 시크릿 창 결과 · 마지막 실행/수정 · 지금도 쓰는가
- **예상 시간**: 50분
- **검증**: 4건 모두 「시크릿 창 결과」 칸이 실측값으로 채워져 있다 (빈칸·추정 없음)

**실습 2: 질문 목록** ⭐
- **목적**: M2~M4 가 찾아야 할 답을 먼저 정한다
- **단계**:
  1. 사례 인덱스의 「배운 것」·「없는 것」과 실습 1 의 표에서 질문을 뽑는다
  2. 원문의 질문 「db 연동 페이지는 왜 공유가 안 되는가」를 1번으로 둔다
  3. 각 질문에 「어느 모듈이 답하는가」와 「답의 근거는 무엇이어야 하는가(공식 문서 / 실험)」를 붙인다
  4. `guides/questions.md` 로 저장. 10개 이내
- **예상 시간**: 40분
- **검증**: 모든 질문에 담당 모듈과 근거 종류가 붙어 있다

**실습 3: 영상 서사 씨앗** ⭐ (선택)
- **목적**: M6 영상이 기능 나열이 되지 않게 지금 서사를 한 줄로 적어 둔다
- **단계**: Journal 9/1·9/3 원문에서 "어떻게 알게 됐고 무엇이 달라졌는가"를 3문장으로 뽑아 `guides/story-seed.md` 에 둔다
- **예상 시간**: 15분
- **검증**: 3문장 모두 Journal 원문에 대응 인용이 있다

#### 산출물
```
01-Inventory-and-Questions/
├── README.md
├── guides/
│   ├── inventory.md        ← 실물 4건 상태표 (실측)
│   ├── questions.md        ← 질문 10개 이내 · 담당 모듈 · 근거 종류
│   └── story-seed.md       ← 영상 서사 3문장 (선택)
└── examples/
    └── artifact-list.json  ← Artifact list 결과 원본
```

#### Definition of Done
- [ ] 실물 4건 상태표 — 시크릿 창 실측 포함
- [ ] 질문 목록 10개 이내 · 담당 모듈 · 근거 종류
- [ ] 🔴 실물 1건: `Artifact list` 실제 실행 결과가 `examples/` 에 있다
- [ ] README 작성 · 링크 검사 통과 (`python scripts/check_links.py Topics/Claude-Artifacts-Routines`)
- [ ] WorkLog — **헤더에 실소요(시작·종료·사용자 대기) 기록**
- [ ] Daily Retrospective

#### Self-Assessment
**개념 이해**: 소유자 브라우저와 시크릿 창이 다른 것을 보여 주는 이유를 한 문장으로 말할 수 있는가 / **실무 활용**: 새 아티팩트를 만들면 공유 전에 무엇을 확인할지 3단계로 말할 수 있는가 / **문제 해결**: "링크가 안 열려요"라는 말을 들으면 무엇부터 물을지 안다

#### 예상 시간 배분
- 개념: 15분 · 실습 1: 50분 · 실습 2: 40분 · 실습 3: 15분 · 문서화: 20분 — **합계 2h** (버퍼 포함)

#### 참조 자료
- `Materials_For_Topics/Claude-Artifacts-Routines/2026-09-13 사례 인덱스.md` — 실물 링크 4건과 배운 것
- `Journal/2026-09-01.md#Learnings` · `Journal/2026-09-03.md` — 계기 원문
- Claude Code 세션 도구 `Artifact` (list / read / status) — 이 볼트에서 바로 실행 가능

---

### M2 - Artifacts 공식 문서 — 공개 범위·버전·pin·댓글

**난이도**: ⭐⭐
**예상 시간**: 2.5h
**산출물 폴더**: `02-Artifacts-Sharing-and-Versions/`

#### 학습 목표
- [ ] 아티팩트의 공개 범위 종류(비공개 · 링크 공유 · 조직 · 인증 필요)와 각각의 조건을 공식 문서에서 찾아 인용과 함께 적을 수 있다
- [ ] 「db(런타임 capability)가 있으면 왜 공유 범위가 달라지는가」를 문서 근거로 답하고, 우회 방법(정적 스냅샷 · 권한 설정 등)이 있으면 실험으로 확인할 수 있다
- [ ] 버전·재발행·pin·댓글·watch 의 동작을 실물 1건에서 실제로 돌려 보고 기록할 수 있다

#### 주요 개념
1. **발행(publish)과 버전**: 같은 파일 경로로 다시 발행하면 같은 URL 에 새 버전이 쌓인다 `[문서]`; 다른 세션이 고친 뒤엔 재읽기 없이 발행이 거부된다 `[실측 9/12 부스 현황판]`
2. **공개 범위와 capabilities**: 페이지가 `db`·`user` 같은 런타임 기능을 선언하면 익명 접근이 제한된다 `[추론 — M2 에서 문서로 확정]`
3. **pin**: 사용자 사이드바에 꽂는 것. 공유 범위와 무관 `[문서]`. 9/7 "공유 링크가 옛 버전" 이슈는 pin 이 아니라 브라우저 캐시/소유자 시점 문제였는지 재확인 `[추론]`
4. **댓글과 watch**: 시청자가 남긴 댓글을 세션이 읽고 답할 수 있다 — 팀 협업 시나리오의 핵심
5. **정적 vs 동적 아티팩트**: 부스 현황판(정적) vs 부스 매니저(db). 공유가 목적이면 정적을 먼저 고려한다 `[실측 9/3]`

#### 실습 과제

**실습 1: 공식 문서 클리핑 + 인용 표** ⭐⭐
- **목적**: 볼트에 없는 공식 근거를 만든다
- **단계**:
  1. Claude Code 문서(docs.claude.com)에서 Artifacts · 공유 · capabilities 페이지를 찾아 `vl_materials/` 에 클리핑한다 (WebFetch → md)
  2. `artifact-capabilities` 스킬을 Skill 도구로 로드해 이 계정에 실제 열려 있는 capability 목록을 `concepts/capabilities-roster.md` 에 적는다
  3. M1 질문 1(「db 페이지는 왜 공유가 안 되나」)에 **인용 문장**으로 답을 쓴다. 문서에 없으면 "문서에 없음"이라 적고 실습 2 로 넘긴다
- **예상 시간**: 60분
- **검증**: 질문 1 의 답에 문서 인용(또는 "없음" 명시)이 있다

**실습 2: 공유 범위 실험 — 2×2** ⭐⭐
- **목적**: 문서가 말한 것을 실물로 확인한다
- **단계**:
  1. 최소 HTML 두 개를 발행한다 — `capabilities: {}` 하나, `capabilities: {db: …}` 하나
  2. 각각을 ①소유자 브라우저 ②시크릿 창 ③다른 계정(가능하면)에서 열어 결과를 2×2 표로 적는다
  3. db 쪽을 정적 스냅샷으로 다시 발행해(db 제거) 공유가 열리는지 확인한다 — 부스 현황판이 바로 이 경로였다
  4. `guides/sharing-matrix.md` 로 정리
- **예상 시간**: 45분
- **검증**: 표의 모든 칸이 실측이고, 실습 1 의 문서 인용과 일치하거나 불일치를 명시했다

**실습 3: 버전·댓글·watch 한 바퀴** ⭐⭐
- **목적**: 팀 협업 기능을 실물에서 한 번 돌린다
- **단계**:
  1. 입장 안내 아티팩트(e9c029bd)에 `action: read` → 사소한 수정 → `url` 로 재발행 → 갤러리에서 버전 확인
  2. 시크릿 창에서 댓글을 남기고 `action: comments` 로 읽는다 · `reply` · `resolve` 까지
  3. `action: watch` 를 걸고 다른 창에서 republish 해 알림이 오는지 본다
  4. `guides/versions-comments-watch.md` 에 절차와 결과
- **예상 시간**: 30분
- **검증**: 댓글 1건이 read → reply → resolve 까지 기록돼 있다

#### 산출물
```
02-Artifacts-Sharing-and-Versions/
├── README.md
├── concepts/
│   ├── sharing-scopes.md            ← 공개 범위 종류 + 문서 인용
│   └── capabilities-roster.md       ← 이 계정에 열린 capability 목록
├── examples/
│   ├── minimal-static.html          ← 실습 2 정적
│   └── minimal-db.html              ← 실습 2 db
├── guides/
│   ├── sharing-matrix.md            ← 2×2 실측표 · 질문 1 의 답
│   └── versions-comments-watch.md
└── troubleshooting/
    └── shared-link-shows-old-version.md  ← 9/7 이슈 재해석
```

#### Definition of Done
- [ ] 공식 문서 클리핑 2건 이상이 `vl_materials/` 에 있다
- [ ] 질문 1 에 문서 인용 또는 "문서에 없음 + 실험 결과"로 답했다
- [ ] 🔴 실물 1건: 2×2 실험용 아티팩트 2개가 실제로 발행됐고 URL 이 기록돼 있다
- [ ] 댓글 read→reply→resolve 1회 실행
- [ ] README · 링크 검사 통과
- [ ] WorkLog(실소요) · Daily Retrospective · **세션 시작 시 M1 「개선할 점」 체크 기록**

#### Self-Assessment
**개념 이해**: 공개 범위 4종을 조건과 함께 말할 수 있다 · db 가 공유를 바꾸는 이유를 문서 문장으로 인용할 수 있다 / **실무 활용**: "팀에 공유할 페이지"를 요청받으면 정적/동적 중 무엇을 먼저 고를지 이유와 함께 말할 수 있다 / **문제 해결**: 공유 링크가 옛 버전을 보여 줄 때 확인 순서 3개

#### 예상 시간 배분
- 개념: 25분 · 실습 1: 60분 · 실습 2: 45분 · 실습 3: 30분 · 문서화: 20분 — **합계 3h** → 버퍼 포함 표기는 2.5h+0.5h

#### 참조 자료
- Claude Code 문서 — Artifacts (M2 실습 1 에서 정확한 URL 을 찾아 클리핑)
- 세션 스킬 `artifact-capabilities` · `artifact-design`
- 실물: 입장 안내 https://claude.ai/code/artifact/e9c029bd-e072-45a9-9618-a47881af3676

---

### M3 - Artifacts 런타임 기능 실험 — db·user·assets·comments·다중 파일

**난이도**: ⭐⭐⭐
**예상 시간**: 3h
**산출물 폴더**: `03-Artifacts-Capabilities-Lab/`

#### 학습 목표
- [ ] 런타임 capability 5종(db · user · assets · comments · 다중 파일)을 각각 최소 예제로 발행하고 동작을 확인할 수 있다
- [ ] `write_db` / `read_db` / `if_version` 으로 세션에서 아티팩트 데이터를 안전하게 읽고 쓸 수 있다
- [ ] 기존 실물 2건(부스 매니저·부스 현황판)에서 잘못 쓰거나 놓친 기능을 찾아 고칠 수 있다
- [ ] 「어떤 일에 어떤 기능이 맞는가」 선택표를 만들 수 있다

#### 주요 개념
1. **db**: 페이지가 공유 상태를 갖는다 — 여러 사람이 같은 데이터를 본다. 부스 매니저가 이것 `[실측]`. `if_version` 으로 동시 수정 충돌을 막는다 `[문서]`
2. **user**: 보는 사람이 누구인지 페이지가 안다 · `data/users/me` 는 각자 비공개 `[문서]`
3. **assets**: 이미지·PDF·폰트를 아티팩트에 올려 페이지가 참조한다 — 부스 배치도 캡처가 이 경로였어야 했는지 `[추론]`
4. **다중 파일(files)**: HTML 한 장이 아니라 CSS/JS/데이터를 따로 발행 — 16MB 제한과 CDN 허용 목록 `[문서]`
5. **localStorage 는 저장이 아니다**: 보는 사람의 브라우저에만 남는다 `[문서]` — 부스 매니저가 처음에 이걸 썼다면 사고였다

#### 실습 과제

**실습 1: 5종 최소 예제** ⭐⭐
- **목적**: 각 기능을 가장 작은 형태로 한 번씩
- **단계**: 5개 HTML 을 `examples/` 에 만들어 각각 발행 — ① 카운터(db) ② "안녕, {viewer}"(user) ③ 이미지 1장(assets) ④ 댓글 유도(comments) ⑤ CSS 분리(files). 각 URL·capability 선언·확인 결과를 `guides/lab-log.md` 에 기록
- **예상 시간**: 75분
- **검증**: 5개 URL 이 모두 열리고 각 기능이 시크릿 창에서 기대대로/기대와 다르게 동작했는지 적혀 있다

**실습 2: 세션에서 db 읽고 쓰기** ⭐⭐
- **목적**: 사람이 화면에서 바꾼 것을 AI 세션이 읽고, 세션이 쓴 것을 화면이 보는 왕복
- **단계**: ① 실습 1 카운터를 화면에서 바꾼다 ② `read_db` 로 읽는다(version 확인) ③ `write_db` + `if_version` 으로 쓴다 ④ 일부러 옛 version 으로 써서 거부되는지 본다 ⑤ 결과를 `guides/db-roundtrip.md`
- **예상 시간**: 30분
- **검증**: 옛 version 쓰기가 실제로 거부된 로그가 있다

**실습 3: 기존 실물 재검토·수정** ⭐⭐⭐
- **목적**: 배운 것을 내 것에 적용한다
- **단계**: ① 부스 매니저·부스 현황판을 `read` 로 받아 capability 선언·저장 방식·공유 범위를 대조 ② 놓친 것 목록(예: 배치도를 assets 로, 댓글 켜기, 현황판을 매니저 db 에서 자동 생성) ③ 9/26 행사 전에 필요한 것만 골라 수정·재발행 ④ 시크릿 창 검증
- **예상 시간**: 45분
- **검증**: 수정 전/후 표 + 시크릿 창 결과

#### 산출물
```
03-Artifacts-Capabilities-Lab/
├── README.md
├── concepts/
│   └── capability-selection-table.md   ← 어떤 일에 어떤 기능
├── examples/
│   ├── 01-counter-db.html
│   ├── 02-hello-user.html
│   ├── 03-image-assets.html
│   ├── 04-comments.html
│   └── 05-multi-file/ (index.html + app.css)
├── guides/
│   ├── lab-log.md
│   ├── db-roundtrip.md
│   └── bighug-artifacts-review.md      ← 실물 2건 재검토·수정 기록
└── troubleshooting/
    └── cdn-and-storage-gotchas.md
```

#### Definition of Done
- [ ] 5종 예제 발행 · URL 기록 · 시크릿 창 결과
- [ ] db 왕복 + `if_version` 거부 로그
- [ ] 🔴 실물 1건: 부스 매니저 또는 현황판을 실제로 수정·재발행했다 (또는 "수정 불필요" 근거)
- [ ] 선택표 완성
- [ ] README · 링크 검사 통과
- [ ] WorkLog(실소요) · Daily Retrospective · 직전 「개선할 점」 체크

#### Self-Assessment
**개념 이해**: db·user·assets·localStorage 의 차이를 "누가 볼 수 있는가"로 설명 / **실무 활용**: "회의 중 현황판 만들어 줘"를 받으면 어떤 capability 로 갈지 10초 안에 고른다 / **문제 해결**: 다른 세션이 고친 아티팩트에 발행이 거부되면 무엇을 하는지 안다

#### 예상 시간 배분
- 개념: 30분 · 실습 1: 75분 · 실습 2: 30분 · 실습 3: 45분 · 문서화: 20분 — **합계 3h20m** (버퍼 포함 3.5h 로 잡되 로드맵 표는 3h)

#### 참조 자료
- 세션 스킬 `artifact-capabilities` (contract · 각 capability 의 호출 정의)
- `Artifact` 도구 설명 — db(read_db/write_db/batch/if_version) · assets · files · comments
- 실물: 부스 매니저 991fb41f… · 부스 현황판 aa2d46bf…

---

### M4 - Routines — 공식 문서·기존 루틴 점검·두 번째 루틴 발행

**난이도**: ⭐⭐
**예상 시간**: 2.5h
**산출물 폴더**: `04-Routines-Lab/`

#### 학습 목표
- [ ] 클라우드 루틴의 트리거(cron · 일회성) · 실행 환경(어떤 레포/볼트에 접근하는가) · 알림 · 비용을 공식 문서 근거로 설명할 수 있다
- [ ] 기존 WBLP 루틴의 실행 이력을 읽고 "조건 충족 시에만 이메일"이 실제로 그렇게 동작했는지 확인·개선할 수 있다
- [ ] 두 번째 루틴 1건을 설계·발행하고 첫 실행 결과를 확인할 수 있다
- [ ] 로컬 AI4PKM cron(GDR 04:00 등)과 클라우드 루틴을 언제 어느 쪽으로 쓸지 판단표를 만들 수 있다

#### 주요 개념
1. **루틴 = 서버에서 도는 Claude Code 세션**: 내 PC 가 꺼져 있어도 돈다 `[문서]`. 반면 볼트 파일에 쓰려면 접근 경로가 있어야 한다 `[추론 — 확인]`
2. **조건부 알림**: WBLP 루틴은 "워싱턴주 공고가 뜨면"만 메일 `[실측 9/1 설정]`. 매주 "없음" 메일이 오면 곧 무시된다
3. **AI4PKM cron 과의 차이**: 로컬은 볼트를 직접 쓰고 무료, 클라우드는 외부 웹을 보고 PC 없이 돈다 `[추론 — M4 판단표로 확정]`
4. **일회성 스케줄**: "내일 3시에 한 번"도 루틴이다 `[문서]`
5. **관측 가능성**: 루틴이 돌았는지·무엇을 했는지 어디서 보는가 — 실행 이력 화면

#### 실습 과제

**실습 1: 공식 문서 클리핑 + WBLP 루틴 점검** ⭐
- **목적**: 문서 근거 확보 + 유일한 실물의 상태 확인
- **단계**: ① Routines/Scheduled agents 문서 클리핑 → `vl_materials/` ② `schedule` 스킬 로드해 명령 목록 확인 ③ claude.ai/code/routines 에서 WBLP 루틴의 실행 이력(횟수·마지막 실행·메일 발송 여부)을 `guides/wblp-routine-audit.md` 에 기록 ④ 개선점(검색 조건·알림 문구·빈도)이 있으면 수정
- **예상 시간**: 50분
- **검증**: 실행 이력 표에 실제 날짜가 최소 2회 있다

**실습 2: 두 번째 루틴 설계·발행** ⭐⭐
- **목적**: 사례 1건을 2건으로 — 패턴을 말할 수 있게
- **후보** (하나 선택): (a) Personal Ops Board **Deadline 경고** — 매일 아침 `AI/Tasks/items/` 의 tier 1 due 를 보고 D-3·지남을 메일 (볼트 접근이 되는지가 관건) (b) Builders Lounge 6차 모임 D-7·D-1 알림 (c) 유튜브 채널 주간 지표 요약
- **단계**: ① 후보의 "볼트 접근 필요 여부"를 먼저 판정 ② `/schedule` 로 발행 ③ 첫 실행을 기다려(또는 즉시 실행) 결과 확인 ④ `guides/second-routine.md`
- **예상 시간**: 50분
- **검증**: 첫 실행 결과(메일 또는 실행 로그)가 캡처돼 있다

**실습 3: 로컬 vs 클라우드 판단표** ⭐⭐
- **목적**: Personal Ops Board 설계에 바로 쓸 기준
- **단계**: 축 — 볼트 파일 읽기/쓰기 필요 · PC 켜짐 의존 · 외부 웹 접근 · 비용 · 알림 · 실패 시 관측. GDR(04:00)·TIU(04:30)·WBLP·두 번째 루틴을 표에 놓고 각각 왜 그쪽인지 적는다 → `concepts/local-vs-cloud.md`
- **예상 시간**: 25분
- **검증**: 4건 모두 표에 있고 이유가 한 줄씩 있다

#### 산출물
```
04-Routines-Lab/
├── README.md
├── concepts/
│   ├── routines-basics.md          ← 트리거·환경·알림·비용 + 문서 인용
│   └── local-vs-cloud.md           ← 판단표
├── guides/
│   ├── wblp-routine-audit.md
│   └── second-routine.md
└── troubleshooting/
    └── routine-did-not-run.md      ← (있으면) 안 돌았을 때 확인 순서
```

#### Definition of Done
- [ ] 공식 문서 클리핑 1건 이상
- [ ] WBLP 루틴 실행 이력 실측 + 개선 여부 결정
- [ ] 🔴 실물 1건: 두 번째 루틴이 실제로 발행되고 첫 실행 결과가 있다
- [ ] 로컬 vs 클라우드 판단표
- [ ] README · 링크 검사 통과
- [ ] WorkLog(실소요) · Daily Retrospective · 직전 「개선할 점」 체크

#### Self-Assessment
**개념 이해**: 루틴이 AI4PKM cron 과 다른 점 3가지 / **실무 활용**: "매주 X 확인해 줘"를 받으면 로컬/클라우드를 30초 안에 고르고 이유를 말한다 / **문제 해결**: 루틴 메일이 안 왔을 때 확인 순서

#### 예상 시간 배분
- 개념: 25분 · 실습 1: 50분 · 실습 2: 50분 · 실습 3: 25분 · 문서화: 15분 — **합계 2h45m** (로드맵 표 2.5h + 버퍼)

#### 참조 자료
- Claude Code 문서 — Scheduled cloud agents / Routines (M4 실습 1 에서 클리핑)
- 세션 스킬 `schedule`
- 실물: https://claude.ai/code/routines/trig_01LKgvHWt4ZfJbTqJgn5KvVT
- `orchestrator.yaml` — GDR·TIU 로컬 cron 선례
- `Materials_For_Topics/Personal-Ops-Board/2026-09-12 PRD.md` — Deadline 에이전트 계약

---

### M5 - 사용 패턴 가이드 — 더 잘·효율적으로 쓰기

**난이도**: ⭐⭐
**예상 시간**: 1.5h
**산출물 폴더**: `05-Usage-Patterns/`

#### 학습 목표
- [ ] M1~M4 의 실측·문서에서 「이럴 땐 이렇게」 패턴 5개 안팎을 뽑아 각 패턴에 실물 예시와 근거를 붙일 수 있다
- [ ] 「하지 말 것」 목록(안티패턴)을 실제 겪은 사고로 쓸 수 있다
- [ ] 가이드 1편을 다른 사람이 읽고 바로 따라 할 수 있는 수준으로 쓸 수 있다

#### 주요 개념
1. **패턴은 실측에서만 나온다**: M2~M4 에서 `[실측]` 표기가 붙은 것만 패턴이 된다. `[추론]` 은 "확인 필요"로 남긴다
2. **공유 목적이면 정적 먼저**: 부스 현황판 경로
3. **회의 중 즉석 제작**: 요구가 떠오른 그 자리에서 만들어 그 회의에서 쓴다 — 시간이 아니라 **맥락이 살아 있을 때** 만드는 것이 핵심 `[실측 9/3]`
4. **조건부 알림**: 루틴은 "있을 때만" 알려야 살아남는다
5. **AI 가 도구를 고르게 두기**: 지시에 목적·제약만 넣고 도구 이름을 안 넣어도 된다 `[실측 9/1]` — 단, 결과를 검증하는 것은 사람

#### 실습 과제

**실습 1: 패턴 카드 5장** ⭐⭐
- **단계**: 패턴마다 — 상황 · 하는 것 · 하지 않는 것 · 실물 예시(링크) · 근거(`[실측]`/`[문서]`) → `guides/patterns.md`
- **예상 시간**: 45분
- **검증**: 5장 모두 실물 링크와 근거 표기가 있다

**실습 2: 안티패턴·사고 목록** ⭐
- **단계**: 겪은 것만 — db 페이지 공유 안 됨 · 옛 버전 보임 · republish 충돌 · (M3·M4 에서 나온 것) → `guides/anti-patterns.md`
- **예상 시간**: 20분
- **검증**: 각 항목에 날짜와 출처

**실습 3: 가이드 1편 조립** ⭐⭐
- **단계**: 패턴 + 안티패턴 + 선택표(M3) + 판단표(M4) 를 한 문서로 — `guides/artifacts-routines-playbook.md`. 영상 대본의 뼈대가 된다
- **예상 시간**: 25분
- **검증**: 다른 사람이 이 문서만 보고 "팀 공유 페이지 하나"를 만들 수 있는가 (사용자 판단)

#### 산출물
```
05-Usage-Patterns/
├── README.md
└── guides/
    ├── patterns.md
    ├── anti-patterns.md
    └── artifacts-routines-playbook.md
```

#### Definition of Done
- [ ] 패턴 5장 · 안티패턴 목록 · 플레이북 1편
- [ ] 🔴 실물 1건: 플레이북의 예시 링크가 전부 실제로 열린다 (시크릿 창)
- [ ] README · 링크 검사 통과
- [ ] WorkLog(실소요) · Daily Retrospective · 직전 「개선할 점」 체크

#### Self-Assessment
**개념 이해**: 패턴 5개를 실물 없이도 말할 수 있다 / **실무 활용**: 다음에 아티팩트를 만들 때 플레이북을 실제로 열어 볼 것인가 / **문제 해결**: 안티패턴 목록에 새 사고를 추가하는 절차가 있다

#### 예상 시간 배분
- 실습 1: 45분 · 실습 2: 20분 · 실습 3: 25분 — **합계 1.5h**

#### 참조 자료
- M2~M4 산출물 전체
- `Live-CoMC-App/10-Live-Rehearsal-Capstone/guides/incident-classification.md` — 사고를 유형으로 적는 선례

---

### M6 - Capstone — Remotion 영상 「내가 몰랐던 기능을 AI 가 찾아냈다」

**난이도**: ⭐⭐⭐
**예상 시간**: 3.5h
**산출물 폴더**: `06-Capstone-Video/`

#### 학습 목표
- [ ] 기능 나열이 아니라 「어떻게 알게 됐고 무엇이 달라졌는가」 서사로 5~8분 한국어 영상 슬라이드 플랜을 쓸 수 있다
- [ ] M1~M5 의 실물(아티팩트 화면·루틴 화면·회의 사진)을 스크린샷으로 확보해 영상에 넣을 수 있다
- [ ] `remotion-video` 스킬의 3단계 승인(슬라이드 플랜 → 오디오 → 렌더링)을 거쳐 MP4 를 만들고 유튜브에 올릴 수 있다
- [ ] Topic Retrospective 를 쓸 수 있다 — 실소요 vs 15h 비교 포함

#### 주요 개념
1. **서사 축**: 9/1 *"지시자가 모르는 것도 AI 가 채울 수 있다"* — 오래된 전제의 반례. 9/3 *"예전 같으면 상상도 못한 일"* — 회의 중 즉석 제작
2. **정보 + 경험**: 원문 요구. 패턴(M5)이 정보, Journal 원문이 경험
3. **밝기 대역**: remotion-video 스킬 원장 확인 — 직전 영상들과 다른 대역으로 `[스킬 규칙]`
4. **claim ledger**: 영상의 모든 주장에 M2~M4 의 `[실측]`/`[문서]` 출처를 붙인다 — Live-CoMC-App 이 만든 습관

#### 실습 과제

**실습 1: 서사 + 슬라이드 플랜** ⭐⭐
- **단계**: ① M1 story-seed 확장 ② 장면 8~12개 — 계기 → 첫 실물 → 막힌 것(db 공유) → 알게 된 것 → 패턴 → 루틴 → 달라진 것 ③ `remotion-video` 스킬 호출 → `video-slide-plan.md` ④ **사용자 승인**
- **예상 시간**: 60분
- **검증**: 플랜의 각 장면에 출처(실물 링크 또는 Journal 원문)가 있다

**실습 2: 스크린샷·자료 확보** ⭐
- **단계**: 아티팩트 3건 · 루틴 화면 · 갤러리 · 댓글 화면 · (있으면) BigHug 회의 사진 → `assets/`. 개인정보·이메일 주소 가리기
- **예상 시간**: 30분
- **검증**: 플랜의 모든 이미지 자리에 파일이 있다

**실습 3: 오디오 → 렌더링 → 업로드** ⭐⭐⭐
- **단계**: edge-tts 초벌 → 사용자 검토 → 렌더링 → 유튜브 업로드 자료 문서(제목·설명·태그) → 업로드 → `youtube-sns-promo` 스킬로 홍보 글(선택)
- **예상 시간**: 90분
- **검증**: 유튜브 URL 이 README 에 있다

**실습 4: Topic Retrospective** ⭐
- **단계**: `vl_worklog/YYYYMMDD_Claude-Artifacts-Routines_Final_Retrospective.md` — 실소요 합계 vs 15h · 목표 6개 점검 · 개선 제안 4건(CoMC 에서 온 것)이 실제로 도움됐는지 평가 · 다음 제안 2개 이상
- **예상 시간**: 30분
- **검증**: 실소요 숫자가 WorkLog 헤더 합계와 일치한다

#### 산출물
```
06-Capstone-Video/
├── README.md                 ← 유튜브 링크 · 제작 과정
├── video-slide-plan.md
├── assets/                   ← 스크린샷
├── claim-ledger.md           ← 장면별 주장 · 출처
└── upload-materials.md       ← 제목·설명·태그
```
(Remotion 프로젝트 자체는 `AI/RemotionStudio/` — 공개 레포 밖)

#### Definition of Done
- [ ] 슬라이드 플랜 승인 · 오디오 승인 · 렌더링 완료
- [ ] 🔴 실물 1건: 유튜브 URL
- [ ] claim ledger 전 장면
- [ ] Topic Retrospective (실소요 포함)
- [ ] 🔴 **Topic 최상위 README.md** — 무엇을 알아냈는지 · 모듈 순서 · 영상 링크 · 실물 링크
- [ ] 링크 검사 통과 (Topic 전체)
- [ ] WorkLog(실소요) · Daily Retrospective

#### Self-Assessment
**개념 이해**: 영상을 본 사람이 두 기능의 차이와 "언제 쓰는지"를 말할 수 있는가 / **실무 활용**: 영상 후 댓글·질문에 플레이북으로 답할 수 있는가 / **문제 해결**: 영상 속 주장에 이의가 오면 claim ledger 로 출처를 댈 수 있는가

#### 예상 시간 배분
- 실습 1: 60분 · 실습 2: 30분 · 실습 3: 90분 · 실습 4: 30분 — **합계 3.5h**

#### 참조 자료
- `_Settings_/Skills/remotion-video/SKILL.md` · `effects-library.md` · 밝기 원장
- `Ingest/CatchUpAI_VL/Topics/WA-Caregiver-Pathways/` 캡스톤 영상 선례 · `Datacenter-Workforce-Programs/10-Capstone-Video/examples/narrative-material.md`(루틴 소개 부분)
- Task Board Backlog 「내가 몰랐던 기능을 AI 가 찾아냈다」 발상(9/1)

---

## 📝 WorkLog 작성 가이드

각 학습 세션마다 WorkLog 를 작성하여 진행 상황을 추적합니다.

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_Claude-Artifacts-Routines.md`

**WorkLog 필수 섹션**:
1. 세션 개요 — **날짜 · 시작·종료 시각 · 실소요(그중 사용자 대기 시간 분리)** ← 이 Topic 부터 필수
2. 직전 WorkLog 「개선할 점」 체크 — 세션 시작 시 읽고 지켰는지 한 줄
3. 오늘의 학습 목표 (체크리스트)
4. 진행 내용 (실습별 상세 기록 — `[실측]`/`[문서]`/`[추론]` 표기)
5. 문제 해결 로그
6. DoD 체크리스트 (모듈 완료 기준)
7. Daily Retrospective
8. 참조 및 산출물

---

## 🔍 Retrospective 가이드

### Daily Retrospective (매일, 5-10분)
WorkLog 내에 작성: What went well? · What could be improved? · Insights · Tomorrow's focus

### Module Retrospective (모듈 완료 시, 15-20분)
WorkLog 말미 또는 `vl_worklog/YYYYMMDD_MX_Retrospective.md`: 계획 대비 실제(실소요 포함) · 핵심 학습 내용 · 발생한 문제와 해결 · Roadmap 정확도 평가 · 다음 모듈 준비사항

### Topic Retrospective (전체 완료 시, 30-60분)
`vl_worklog/YYYYMMDD_Claude-Artifacts-Routines_Final_Retrospective.md`: 전체 여정 통계(실소요 vs 15h) · VibeLearn AI 방법론 효과성(특히 CoMC 개선 제안 4건의 적용 결과) · 산출물 품질 · 영상 결과 · 향후 개선

---

## 📂 전체 폴더 구조

```
Claude-Artifacts-Routines/
├── README.md                          # 🔴 필수 — Topic 을 닫을 때 (M6 DoD)
├── topic_starter.md
├── vl_prompts/
│   ├── roadmap_prompt.md
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── 20260913_RoadMap_Claude-Artifacts-Routines.md
├── vl_worklog/
├── vl_materials/                      # 공식 문서 클리핑 (M2·M4)
├── 01-Inventory-and-Questions/
├── 02-Artifacts-Sharing-and-Versions/
├── 03-Artifacts-Capabilities-Lab/
├── 04-Routines-Lab/
├── 05-Usage-Patterns/
└── 06-Capstone-Video/
```

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | 2026-09-13 | 2026-09-13 | ✅ | 100% (7/7) | Live #27 방송 중 완료, 실소요 50분. **실물 4건 → 7건**(설명 페이지 2건 발견). 질문 9개. 시크릿 창 6건 실측 — db·private 는 Sign in, 나머지 열림(예측 6/6) |
| M2 | 2026-09-13 | 2026-09-13 | ✅ | 100% (6/6) | 방송 중 완료, 실소요 55분. **질문 1 답: 페이지는 공개되고 db 데이터는 로그인 사용자만** (플랫폼 대화상자 문구 + 시크릿 창 실측). 이 계정 Pro/Max → 댓글·편집자 불가. watch 한도 5 |
| M3 | | | ⏳ | 0% | |
| M4 | 2026-09-21 | | 🟡 | 25% (1.5/6) | **실습 1 을 사고 대응으로 먼저** — WBLP 루틴 9/7·14·21 3주 연속 실패 원인 = 환경 `Default` 의 Network access `Trusted`(amazon.jobs 차단). 환경 수정 → 수동 실행 성공 → 첫 알림 메일 · 무시되던 검색 파라미터 2개 교체. 문서 클리핑·두 번째 루틴·판단표 남음 → `04-Routines-Lab/` |
| M5 | | | ⏳ | 0% | |
| M6 | | | ⏳ | 0% | |

**범례**: ⏳ 대기 · 🔄 진행 중 · ✅ 완료

---

## 🎯 성공 기준

전체 Topic 완료 기준:
- [ ] 모든 모듈 완료 (DoD 100%)
- [ ] 최소 6개 산출물 폴더 생성
- [ ] Topic Retrospective 작성 (실소요 포함)
- [ ] Self-Assessment 평균 ⭐⭐⭐⭐ 이상
- [ ] Capstone — 유튜브에 올라간 영상 1편 + Topic 최상위 README
- [ ] 원문의 질문 「db 연동 페이지는 왜 공유가 안 되는가」에 문서·실험 근거로 답했다

---

**생성자**: Claude with VibeLearn AI
**Roadmap 버전**: 1.0
**방법론 버전**: VibeLearn AI 2.0
