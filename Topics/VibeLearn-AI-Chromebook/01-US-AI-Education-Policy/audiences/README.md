---
title: "대상별 AI 교육 접근법 — 재사용 지식 자산"
created: 2026-08-16 22:30:00
tags:
  - ai-education
  - audience-mapping
  - reusable-asset
---

## 이 폴더의 목적

이 폴더는 **VibeLearn-AI-Chromebook Topic이 끝나도 남는 자산**이다. 학습자(Catch Up AI)가 앞으로 학생·시니어·시민단체 활동가·비IT 배경 성인 등 다양한 대상에게 AI 교육을 할 계획이므로, 이번 정책 조사에서 얻은 것을 대상별로 재정리해 둔다. 향후 별도 AI 교육 Topic의 입력이 된다.

**조사 시점**: 2026-08-16
**기준 축**: 미 노동부 AI Literacy Framework의 5개 콘텐츠 영역 ([../concepts/dol-ai-literacy-framework.md](../concepts/dol-ai-literacy-framework.md))

## 왜 DoL 프레임워크를 축으로 삼는가

세 가지 이유가 있다.

**첫째, 대상 범위가 맞다.** DoL 프레임워크는 학교에 한정되지 않고 "모든 미국 근로자"와 교육 시스템 전체를 대상으로 한다. AI4K12 Five Big Ideas는 K-12 전용이라 시니어·성인에게 쓸 수 없다.

**둘째, 원문이 이미 대상 구분을 한다.** "Audience Considerations" 절에서 Workers / Employers / Education and Training Providers / State and Local Agencies 4개로 나누고 각각에 "무엇부터 시작하라"까지 제시한다. 새로 발명할 필요가 없다.

**셋째, 권위가 있다.** 연방 정부 문서이므로 학교·기관·비영리에 제안할 때 공용 어휘로 쓸 수 있다.

### 원문 4개 구분을 5개로 재편한 이유

원문의 구분은 **정책 이행 주체** 기준이다(누가 프로그램을 만드는가). 우리에게 필요한 것은 **가르칠 대상** 기준이다(누가 배우는가). 그래서 다음과 같이 재편했다.

| DoL 원문 구분 | 이 폴더의 재편 |
|---|---|
| Workers (재직자·구직자·**학생** 포함) | → `k12-students` / `adult-learners` / `seniors`로 분화 |
| Education and Training Providers | → `educators` |
| Employers | 기관 대상이라 제외 (필요 시 `adult-learners`의 맥락으로 흡수) |
| State and Local Agencies | 기관 대상이라 제외 |
| (원문에 없음) | → `community-nonprofit` **신규** |

원문의 공백은 두 곳이다. **시니어**는 Workers에 흡수돼 별도 고려가 없고, **시민단체·비영리 활동가**는 아예 없다. 이 두 대상이 이 폴더가 원문에 더하는 가치다.

## 5개 영역 × 5개 대상 매트릭스

각 칸은 **그 대상에게 그 영역을 가르칠 때의 초점**이다.

| DoL 영역 | K-12 학생 | 교사·교육자 | 성인 학습자 | 시니어 | 시민단체·비IT |
|---|---|---|---|---|---|
| **1. AI 원리 이해** | AI4K12와 연계. 환각 개념은 필수 | 학생 질문에 답할 수준 + 탐지 도구의 한계 | 직무 맥락의 확률적 출력 | **최소한만** — "왜 자신 있게 틀리는가" | 최소한 + 데이터가 어디로 가는가 |
| **2. 활용처 탐색** | 교과 과제 중심 | 수업 준비·행정 시간 절감 | 실제 업무 과제 | 일상 과제 (편지, 정보 검색, 번역) | 조직 업무 (보도자료, 보조금 신청, 회의록) |
| **3. 효과적 지시** | ⭐ **최우선 진입점** | ⭐ 최우선 | ⭐ 최우선 | ⭐ 최우선 (단 예시를 매우 구체적으로) | ⭐ 최우선 |
| **4. 출력 평가** | 학업 정직성과 함께 | 학생 결과물 판단 기준 | 업무 품질 기준 | **사기·피싱 방어와 결합** | 조직 신뢰도 리스크 |
| **5. 책임 있는 사용** | 학군 AUP·공개 의무 | 학생 데이터·FERPA | 직장 정책·기밀 | **개인정보·금융 사기** | 회원·수혜자 정보 보호 |

**공통 패턴 세 가지**

1. **영역 3(효과적 지시)이 모든 대상에서 최우선 진입점이다.** 성공 경험이 가장 빠르고, DoL 원칙 1(체험 학습)과 직결된다. 영역 1(원리)부터 시작하면 대부분의 대상에서 이탈한다.
2. **영역 5(책임 있는 사용)는 대상마다 내용이 완전히 다르다.** 학생은 학업 정직성, 시니어는 사기 방어, 시민단체는 수혜자 정보 보호다. 같은 영역이라고 같은 수업을 하면 안 된다.
3. **영역 1(AI 원리)의 깊이 차이가 가장 크다.** K-12는 AI4K12 수준까지, 시니어는 "환각" 한 개념이면 충분하다.

## DoL 원칙 4 — 대상별 선결 조건

원칙 4(Address Prerequisites)는 디지털 리터러시·기기 접근성·인터넷 연결을 먼저 해소하라고 요구한다. 대상별로 장벽이 다르다.

| 대상 | 주된 선결 장벽 | 대응 |
|---|---|---|
| K-12 학생 | 기기는 있으나 **관리 정책으로 제약** | 이 Topic 전체가 이 문제 |
| 교사·교육자 | 시간 부족, 정책 불확실성 | 짧은 모듈 + 명확한 정책 근거 제시 |
| 성인 학습자 | 업무 시간 확보 | 실제 업무 과제로 실습 |
| 시니어 | **기기·연결·자신감 모두** | 대면 소그룹, 반복, 느린 속도 |
| 시민단체·비IT | 비용, 조직 승인 | 무료 도구, 조직 정책 템플릿 |

## 대상별 문서

1. [k12-students.md](k12-students.md) — K-12 학생 (18세 미만)
2. [educators.md](educators.md) — 교사 및 교육 제공자
3. [adult-learners.md](adult-learners.md) — 대학생·직장인 성인 학습자
4. [seniors.md](seniors.md) — 시니어
5. [community-nonprofit.md](community-nonprofit.md) — 시민단체·비영리 활동가, 비IT 배경 성인

## 연방 채널 — 이미 존재하는 협력 상대

조사 중 발견한 가장 실용적인 사실이다. **학생 밖 대상에 대한 AI 교육 채널이 연방 차원에서 이미 지정돼 있다.**

**USDA 4-H · Cooperative Extension System** — EO 14277 Sec. 7(c)가 농무부 장관에게 **"formal and non-formal education"**에서의 AI 교육을 이 채널로 우선하라고 지시했다. 4-H와 Extension은 미국 농촌·지역사회·성인 교육의 전통적 통로다.

특히 **4-H Tech Changemakers**(2017년 시작)는 이 프로젝트와 구조적으로 닮았다.

- 청소년이 **성인에게** 디지털 역량을 가르치는 adult-youth 파트너십 모델
- 청소년은 정식 훈련을 거쳐 자격을 얻고, 기술 지원과 지역사회 참여 훈련을 받음
- 누적 성인 1만 명 이상 도달. 기업 투자 850만 달러로 **164개 지역 5만 명** 목표
- **광대역이 부족한 농촌 지역과 유색인종 커뮤니티**에 초점
- 인기 주제: 책임 있는 온라인 행동, 이메일, 온라인 안전, 화상회의

> **전략적 함의**: Chromebook판 VibeLearn AI를 배운 학생이 지역사회 성인에게 가르치는 경로가 이미 제도로 존재한다. K-12 트랙과 시니어·지역사회 트랙을 잇는 다리다. 이 Topic 완료 후 별도로 검토할 가치가 크다.

AI 쪽으로도 이미 움직이고 있다. 10개 주(콜로라도·플로리다·인디애나·아이오와·네브래스카·오하이오·노스캐롤라이나·사우스캐롤라이나·유타·펜실베이니아) 교육자들이 **National AI Curriculum Committee**를 구성해 4-H AI 커리큘럼을 개발 중이고, 네브래스카 4-H는 National 4-H Council·Google과 함께 청소년 1.5만 명 + **성인 5천 명** 대상 AI 프로젝트를 진행 중이다. 아이오와는 2024-25 프로그램 연도에 청소년 1만 명 이상이 AI 교육에 참여했다.

## 참조 자료

| 자료 | 유형 | 링크 |
|---|---|---|
| DOL AI Literacy Framework (Attachment I) | 1차 | `../../vl_materials/sources/DOL-TEN-07-25-Attachment-I-Framework.pdf` |
| EO 14277 (Sec. 7(c) 4-H·Extension) | 1차 | `../../vl_materials/sources/EO-14277-advancing-AI-education-youth.pdf` |
| 4-H Tech Changemakers | 1차 | https://4-h.org/about/4-h-at-home/tech-changemakers/ |
| 4-H Tech Changemakers 확대 보도 | 2차 | https://www.agdaily.com/lifestyle/4-h-teens-drive-digital-inclusion-resourced-communities/ |
| Cooperative Extension System 개요 (CRS) | 1차 | https://www.congress.gov/crs-product/R48071 |
