# WorkLog - M2: 비교표 만들기

**날짜**: 2026-10-04
**Topic**: AI-Agent-Apps-Compare
**모듈**: M2 - 비교표 만들기
**학습 시간**: Live #30 방송 중 (M1 직후)

> 아래 조사 과정과 회고는 2026-10-04 당시의 기록이다. Dots 실습 가능 여부와 비교 대상은 하단 「범위 업데이트」에 적힌 2026-10-09 판정을 우선한다.

## 🎯 오늘의 학습 목표

- [x] 다섯 기준 비교표 (맡길 수 있는 일 · 무료 범위 · 설정 난이도 · 개인정보 · 내 일에 쓸 곳)
- [x] 실습 대상 판정 갱신 (Muse 우선 · Dots Plus에서 불가 · Instinct 초대 대기)
- [x] 승인 · 개인정보 정리
- [x] M1 「확인 필요」 해결 시도

## 📚 진행 내용

### 1. 범위 조정 반영 (M2 시작 전)

박창수가 ChatGPT Pro 사용자라 Dots 를 실습 범위에 넣었다. 규칙을 「무료만」 → 「새 결제 없음 — 무료 플랜 + 이미 쓰는 구독」으로 바꾸고 topic_starter · 프롬프트 · Roadmap · M1 문서를 함께 고쳤다. M3 폴더 이름도 `03-Hands-On/` 으로 바꿨다.

### 2. 조사

1. Grok Bot 승인 · 보안 공식 문서를 다시 열어 승인 카드 · Auto-review · 내 PC 실행 정책을 확인했다
2. Grok Bot 출시일: 2026-08-11 초기 베타 (보조 출처). 출시 때는 상위 플랜만이었고 지금 공식 문서는 모든 유료 Cursor 개인 플랜 → 접근이 넓어진 것으로 정리
3. Dots 승인 · 개인정보: Custom Rules · 자동 검토 · 개인 플랜 학습 선택 (보조). chatgpt.com 소개 페이지도 403
4. ChatGPT Pro 가격: $100(5x) · $200(20x) (보조)
5. Muse 연결 앱 · 승인 · 감사 기록 · 영어 (보조)

### 3. 산출물

- [02-Comparison-Table/guides/comparison-table.md](../02-Comparison-Table/guides/comparison-table.md) — 다섯 기준 비교표 · 실습 판정 · 바뀐 것
- [02-Comparison-Table/concepts/approval-and-privacy.md](../02-Comparison-Table/concepts/approval-and-privacy.md) — 승인 경계 · 개인정보 · M3 에서 지킬 것

**메모/인사이트**: 세 서비스의 차이는 기능보다 **대상**에 있다 — Muse 는 누구나 · 생활, Dots 는 상위 구독자 · 이어지는 업무, Grok Bot 은 개발자 · 팀 업무(터미널 · 여러 Bot 협업).

## 🐛 문제 해결 로그

### 문제 1: OpenAI 계열 공식 페이지 전부 403

**증상**: openai.com · help.openai.com · chatgpt.com/features/dots 자동 읽기 차단
**해결**: 보조 출처로 채우고 「공식 원문 확인 필요」를 표에 표시. M3 에서 사용자가 브라우저로 원문 · 실제 설정 화면을 확인한다

### 문제 2: Grok Bot 회사 표기

**증상**: 보조 출처는 「SpaceXAI(구 xAI)」
**해결**: 공식 문서 도메인이 docs.x.ai 라 이 Topic 은 xAI 로 표기하고 비교표 「바뀐 것」에 남겼다

## 📊 DoD 체크리스트

- [x] 비교표 4 × 5 완성 (확인하지 못한 칸은 「확인 필요」)
- [x] 실습 대상 판정 갱신 (Muse 우선; Dots·Instinct·Grok Bot은 현재 조사·비교 대상)
- [x] 승인 · 개인정보 정리
- [x] 모듈 README 작성
- [x] 🔴 README 링크 확인 (`check_links.py`)
- [x] WorkLog + Daily Retrospective 작성

**완료율**: 6/6 (100%)

## 💡 Daily Retrospective

### What went well (잘된 점)
- 승인 장치를 비교하니 CoMC · 캐치에서 직접 만든 「AI 제안 → 사람 승인」 구조와 같다는 연결이 생겼다
- 이전 정보(9/4 리서치)와 지금 정보가 다른 점을 표로 남겨, 「AI 서비스 정보는 빨리 바뀐다」를 보여 줄 수 있게 됐다

### What could be improved (개선할 점)
- Dots 는 공식 원문을 하나도 직접 못 읽었다 — 보조 출처 비중이 높다. M3 에서 실제 화면으로 보완해야 한다

### Insights (인사이트)
- 시청자에게 가장 쓸모 있는 기준은 「누구를 위한 서비스인가」와 「무료로 써 볼 수 있나」다
- Muse 는 AI 학습 사용이 **기본 켜짐**이다 — 가입 직후 끄는 것을 실습 첫 단계로 넣는다

### Tomorrow's focus (내일 집중할 것)
- M3: Dots 가 내 ChatGPT Pro 계정에 열렸는지 확인 → 설정 · 첫 과제
- M3: Muse 가입 → 학습 사용 끄기 → 같은 첫 과제

## 🔄 범위 업데이트 (2026-10-09)

M2의 비교 산출물을 현재 조건에 맞게 갱신했다. Dots는 ChatGPT Plus 계정에서 사용할 수 없어 실습 판정을 「실습」에서 **조사·비교만**으로 바꿨다. 비교 대상에 Instinct를 추가하고, 공식 소개·개인정보 정책·약관에서 확인한 내용을 반영했다. Instinct의 대기 명단 승인 여부는 아직 확인되지 않았으므로 현 시점의 판정은 조사·비교만이며, 승인 뒤에 접근 조건과 실습 가능성을 다시 검토한다.

승인·개인정보 표에는 Instinct가 대리인으로 거래·약정할 수 있고, 연결 해제만으로 이미 색인된 자료가 자동 삭제되지 않는다는 약관 내용을 추가했다. 모델 학습 사용은 설정에서 거부할 수 있지만 안전 검토에 표시된 자료는 예외이며, 일반적인 서비스 개선 사용과도 구분해야 한다. 따라서 다른 세 서비스와 같은 승인 흐름을 가정하지 않고, 공식 문서 확인과 출처 수준을 함께 표시했다.

**확인 자료**: [Instinct 공식 소개](https://instinct.com/) · [개인정보 정책](https://instinct.com/privacy-policy) · [서비스 약관](https://instinct.com/terms). 공식 페이지 확인일: 2026-10-09.

### 갱신 후 상태

- Muse의 실제 가입·무료 범위·설정 확인은 M3에서 진행한다.
- Instinct 초대가 오면 최신 약관·개인정보 정책을 다시 확인한 뒤 실습 여부를 결정한다.

## 📎 참조 및 산출물

**생성된 파일/폴더**:
- `02-Comparison-Table/` — M2 산출물
- `vl_materials/official-sources.md` — M2 출처 추가
- `01-Identify-Services/guides/service-cards.md` — 확인 필요 목록 상태 갱신

**작성자**: 박창수 + Claude Code
**방법론**: VibeLearn AI
