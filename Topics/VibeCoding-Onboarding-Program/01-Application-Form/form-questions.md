# 신청 Google Form — 확정 문항 (복사용, 한/영 이중언어)

**모듈**: M1 — 신청 접수 Form + 영상 안내 문구
**작성일**: 2026-07-21 (한/영 이중언어로 갱신)
**용도**: 아래 내용을 Google Forms에 그대로 복사해 넣으면 됩니다. 한국인·미국인(영어권) 신청자를 모두 대상으로 하므로 하나의 Form 안에 한국어와 영어를 함께 표기합니다.

---

## Form 제목

```
바이브 코딩 첫걸음 — 온보딩 신청서
Vibe Coding First Steps — Program Application
```

## Form 설명 (제목 아래 인사말)

```
🇰🇷 코딩을 몰라도 괜찮습니다. 컴퓨터가 익숙하지 않아도 괜찮습니다.

오랫동안 쌓아 오신 경험과 지식으로 나만의 앱을 만들어 보고 싶으신 분들을 위해,
컴퓨터에 바이브 코딩 환경을 준비하는 것부터 앱을 만들어 가는 과정까지 옆에서 함께해 드립니다.

미국 유타주에 계신 60대 선생님 한 분도 이렇게 시작하셨습니다. 컴퓨터 세팅을 도와드렸더니,
단 며칠 만에 자신의 인생 이야기를 녹음하고 글로 정리해 책으로 만들어 주는 앱을 직접 만드셨습니다.

아래 몇 가지만 적어 주시면, 제가 이메일로 연락드리겠습니다.

—

🇺🇸 You don't need to know how to code. You don't need to be comfortable with computers.

If you have deep knowledge and experience from your own field and want to turn it into
an app, I'll help you every step of the way — from setting up your computer for
"vibe coding" to actually building your app.

A teacher in his 60s in Utah started exactly this way. I helped him set up his computer,
and within just a few days he had built his own app — one that records his life stories,
turns them into text, and prepares them to become a book.

Just fill in a few details below, and I'll reach out to you by email.
```

---

## 구조 — 3개 Section + 조건 분기 (미국 선택 시에만 주 질문 표시)

미국을 선택한 사람에게만 주(State) Dropdown을 보여주기 위해, Form을 **3개 Section**으로 나누고
"나라" 문항에 **Go to section based on answer(응답에 따라 다른 섹션으로 이동)**를 건다.

```
[Section 1: 기본 정보]              [Section 2: 미국 거주자 전용]        [Section 3: 앱 소개]
성함, 이메일, 나라(Dropdown)    ──▶  주 State(Dropdown, 50개)      ──▶  만들고 싶은 앱 → 제출
  ├─ 🇺🇸 미국 선택 시 ───────────────▶ Section 2로 이동
  └─ 🇰🇷 한국 / 기타 선택 시 ───────────────────────────────────▶ Section 3으로 바로 이동 (건너뜀)
```

### Section 1 — 기본 정보

**문항 1 — 성함 / Name**

| 설정 | 값 |
|---|---|
| 질문 | 성함을 적어 주세요 / Your name |
| 유형 | 단답형 / Short answer |
| 필수 | ✅ |

**문항 2 — 이메일 / Email**

| 설정 | 값 |
|---|---|
| 질문 | 연락드릴 이메일 주소를 적어 주세요 / Your email address (so I can reach you) |
| 유형 | 단답형 / Short answer |
| 필수 | ✅ |
| 응답 확인 | 텍스트 → 이메일 주소 (Google Forms의 "응답 확인" 기능) |

**문항 3 — 나라 / Country** (분기 문항)

| 설정 | 값 |
|---|---|
| 질문 | 어느 나라에 사시나요? / Which country do you live in? |
| 유형 | 드롭다운 / Dropdown |
| 선택지 | 🇺🇸 미국 / USA → **Section 2(주 선택)로 이동**<br>🇰🇷 한국 / South Korea → **Section 3(앱 소개)로 바로 이동**<br>기타 / Other → **Section 3(앱 소개)로 바로 이동** |
| 필수 | ✅ |

### Section 2 — 주(State) 선택 (🇺🇸 미국을 선택한 사람에게만 표시)

목적이 "워싱턴주면 오프라인 안내 가능 여부 판단"이므로, 50개 주 전체 대신 **2개 선택지**로 단순화한다.

**문항 4 — 워싱턴주 거주 여부 / Washington State resident?**

| 설정 | 값 |
|---|---|
| 질문 | 워싱턴주에 살고 계시나요? / Do you live in Washington State? |
| 유형 | 드롭다운 / Dropdown |
| 선택지 | 예 / Yes<br>아니오 / No |
| 필수 | ✅ |
| Section 이동 | 이 Section 끝에서 **Section 3(앱 소개)으로 계속(Continue to next section)** |

### Section 3 — 앱 소개 (모든 신청자가 도착하는 마지막 Section)

**문항 5 — 만들어 보고 싶은 앱 / The app you want to build**

| 설정 | 값 |
|---|---|
| 질문 | 어떤 앱을 만들어 보고 싶으신가요? / What kind of app would you like to build? |
| 설명 | 떠오르는 대로 편하게 적어 주세요. 아직 막연해도 괜찮습니다. 예: "내 상담 경험을 정리해 주는 앱", "우리 가게 단골손님 관리 앱", "손주에게 들려줄 이야기를 모아 주는 앱" / Feel free to write whatever comes to mind — it's okay if it's still a bit vague. Examples: "An app that organizes my counseling notes," "An app to manage regular customers at my shop," "An app that collects stories to tell my grandchildren." |
| 유형 | 장문형 / Paragraph |
| 필수 | ✅ |

---

## Google Forms에서 만드는 순서 (진행자용, 10분 — Section·분기 포함)

1. https://forms.google.com 접속 → **+ 빈 양식** 클릭
2. 제목·설명(Section 1 카드)에 위 한/영 병기 내용 붙여넣기
3. Section 1에 문항 1(성함)·2(이메일) 추가
4. 문항 3(나라)을 Dropdown으로 추가, 옵션 3개(🇺🇸 미국/USA, 🇰🇷 한국/South Korea, 기타/Other) 입력
5. **오른쪽 사이드바 맨 아래 아이콘("Add section", 두 줄짜리 아이콘)을 클릭해 Section 2 추가** →
   문항 4(주, Dropdown) 추가, 옵션 입력창에 위 50개 주 목록을 통째로 붙여넣기
6. **Add section을 한 번 더 클릭해 Section 3 추가** → 문항 5(앱 소개, Paragraph) 추가
7. **Section 1의 "나라" 문항으로 돌아가서, 각 옵션 오른쪽의 화살표(⋮ 옆 점3개 메뉴 아님, 옵션
   목록 자체를 펼치면 나오는 화살표)를 클릭 → "Go to section based on answer" 선택**
   - 🇺🇸 미국 → **Section 2**로 이동
   - 🇰🇷 한국 → **Section 3**으로 이동
   - 기타 → **Section 3**으로 이동
8. **Section 2 카드 맨 아래(Section 2 자체에 대한 이동 설정)**: "Continue to next section"으로
   되어 있는지 확인 — 되어 있으면 주를 선택한 사람은 자동으로 Section 3(앱 소개)으로 넘어간다
9. **응답 탭 → Sheets 연결** (초록 아이콘) — 신청이 자동으로 표에 쌓임
10. **설정 → 응답 → 응답 사본 전송: 요청 시** (선택)
11. **보내기 → 링크 아이콘 → URL 단축** 체크 → 링크 복사
12. **테스트를 2번 해볼 것**: ① 🇺🇸 미국 선택 → 주 선택 화면이 뜨는지 확인 → 앱 소개까지 제출
    ② 🇰🇷 한국 선택 → 주 선택 화면 없이 바로 앱 소개로 넘어가는지 확인 → 제출
13. 테스트 응답 2건은 Sheets에서 행 삭제
14. 최종 링크를 `form-link.md`에 기록

**언어 설정 참고**: Google Forms 자체의 "표시 언어" 설정은 버튼 문구(제출, 필수 표시 등) 언어만 바꾸며, 문항 내용은 어차피 직접 입력한 한/영 병기 텍스트로 고정 표시된다. 별도 언어 설정 변경 없이 그대로 사용하면 된다.

---

## 설계 노트

- **문항 5개로 최소화**: 신청 문턱을 낮추는 것이 최우선. 상세한 배경은 이메일 연락 후 대화로
- **나라는 Dropdown + 조건 분기, 주는 미국 선택자에게만 Dropdown으로 표시**: 한국 신청자는 나라 선택 후 바로 앱 소개로 넘어가고(불필요한 질문 생략), 미국 신청자만 50개 주 Dropdown을 추가로 보게 된다. 자유 입력(단답형) 대신 Dropdown을 쓰면 "워싱턴", "워싱턴주", "WA" 같은 표기 차이 없이 데이터가 깔끔하게 모이는 것도 장점
- **예시 문구를 대상 독자의 삶에서**: "상담 경험", "가게 단골손님", "손주에게 들려줄 이야기" — 개발 용어 0개 (영어 예시도 동일한 정서로 번역)
- **이선생님 사례를 인사말에 배치**: "나 같은 사람도 했다"는 동일시가 신청 결심의 핵심 (M4에서 상세 스토리로 확장 예정). 영어 인사말에서는 "이선생님"을 "a teacher in his 60s in Utah"로 익명 처리해 동일하게 배치
- **하나의 Form, 두 언어 병기 방식 채택**: 별도 Form 두 개로 나누지 않고 한 Form 안에 한국어(🇰🇷)·영어(🇺🇸)를 함께 표기 — 관리 부담을 낮추고, 신청자가 자기 언어 부분만 읽어도 되는 구조
- 무료/유료 표현은 넣지 않음 — 프로그램 성격 확정 후 필요 시 추가
