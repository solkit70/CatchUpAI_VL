# 클러스터 × 프로그램 매트릭스

**조사일**: 2026-08-30 (M4 실습 2)
**질문**: *"내 지역에 뭐가 있나"*

## 6개 프로그램 — 지역성의 종류가 다르다

매트릭스를 그리기 전에 알아야 할 것이 있다. **여섯 개가 같은 방식으로 지역에 매이지 않는다.**

| #   | 프로그램                         | 지역성의 종류                              |
| --- | ---------------------------- | ------------------------------------ |
| ①   | Meta AWA                     | **지정 도시** — 4개 파일럿 도시에서만             |
| ②   | MS Datacenter Academy        | **지정 대학** — 파트너 커뮤니티 칼리지 소재지         |
| ③   | MS × NABTU                   | **광역** — TradesFutures 네트워크 34개 주    |
| ④   | Google.org / etA             | **광역** — IBEW/NECA 지역 훈련센터, 20개 주 이상 |
| ⑤-a | AWS WBLP                     | **채용 공고 소재지** — 공고가 나야 존재한다          |
| ⑥   | AWS Technical Apprenticeship | **전국 온라인 지원** (군 출신 대상)              |

**②만이 "가서 다니는 학교"이고, ①은 도시 지정, ③④는 소속 조직 기반, ⑤는 채용 공고다.** 이 차이 때문에 같은 표에 넣어도 "○"의 뜻이 칸마다 다르다.

## 매트릭스

**범례**: ✅ 확인된 개설 · ⭕ 광역 대상에 포함(지역 지부 확인 필요) · ❌ 해당 없음 · ❓ 확인 불가

| 클러스터 | ① Meta AWA | ② MS DCA | ③ NABTU | ④ Google/etA | ⑤-a AWS WBLP | ⑥ AWS 견습 |
|---|---|---|---|---|---|---|
| **북버지니아** | ❌ | ❓ | ⭕ | ⭕ | **❌ 공고 0건** | ⭕ 군 출신 |
| **애틀랜타** (GA) | ❌ | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **댈러스–포트워스** (TX) | ❌ | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **휴스턴** (TX) | ✅ **파일럿** | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **피닉스** (AZ) | ❌ | ✅ **Estrella Mountain CC · Glendale CC** | ⭕ | ⭕ | ❌ | ⭕ |
| **시카고** (IL) | ❌ | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **컬럼버스** (OH) | ✅ **파일럿** | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **인디애나폴리스** (IN) | ✅ **파일럿** | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **배턴루지** (LA) | ✅ **파일럿** | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **데모인** (IA) | ❌ | ✅ **DMACC West** | ⭕ | ⭕ | ❌ | ⭕ |
| **중부 워싱턴** (Quincy·Moses Lake) | ❌ | ✅ **Big Bend CC** | ⭕ | ⭕ | ❌ | ⭕ |

## 읽는 법 — 이 표가 실제로 말하는 것

### 1. ⑤-a AWS WBLP는 오늘 기준 **미국 전역에 0건**이다

M5(8/28)는 *"전 세계 4건 / 미국은 Ohio 1건"* 이었다. **오늘(8/30) 다시 재니 3건이고 전부 해외다.**

| 공고 | 위치 | 게시일 |
|---|---|---|
| Data Center Operations Trainee - WBLP | **도쿄, 일본** | 2026-07-13 |
| Data Center Logistics Specialist Trainee | **베스테로스, 스웨덴** | 2026-07-02 |
| Logistics Specialist Trainee, Data Center Communities | **프랑크푸르트, 독일** | 2026-01-15 |

**이틀 사이에 미국 공고가 닫혔다.** M2가 "이 Topic 최적 후보"로 꼽았던 경로다.

> ⚠️ 검색 결과 페이지에는 여전히 버지니아(Sterling·Herndon·Manassas·Chantilly) WBLP 공고가 떠 있다. **전부 날짜 없는 애그리게이터 캐시**이고, 라이브 API 전수에는 없다. **화면에 보이는 것과 지금 지원 가능한 것은 다르다.**

### 2. ①과 ②는 지역이 겹치지 않는다

Meta AWA 4개 도시(휴스턴·컬럼버스·인디애나폴리스·배턴루지)와 MS DCA 개설지(피닉스·데모인·중부 워싱턴) 사이에 **겹치는 곳이 하나도 없다.**

우연이 아니라 성격 차이로 보인다 — **①은 건설 숙련직**(수료 후 Meta 건설 현장 고용 보장)이고 **②는 운영 기술직**(IT 네트워킹·DC 기술자)이다. M1의 2×2가 지역 분포로 재현된 셈이다.

### 3. 용량 상위 3개 시장에 "가서 다니는 프로그램"이 없다

**북버지니아·애틀랜타·댈러스** — 미국 최대 3개 시장인데 ①②가 모두 없다. 이 칸이 이 매트릭스에서 가장 눈에 띄는 공백이다.

## 프로그램 공백 지역 해석 — 왜 북버지니아에 없는가

미국 최대 시장이고 인력 수요도 가장 클 텐데 지정 프로그램이 없다. 가설 셋을 세운다.

**가설 A — 이미 인력 시장이 형성돼 있어 신규 파이프라인이 덜 급하다.**
20년 넘은 성숙 시장이라 경력자 풀·기존 훈련기관·인력 공급망이 자리 잡았다. 프로그램은 **인력이 없는 곳**에 생긴다. Meta가 배턴루지·인디애나폴리스처럼 **신규 진출지**를 고른 것과 일치한다.

**가설 B — 성숙 시장은 가동 중심이라 필요한 직종이 다르다.**
①은 건설 숙련직 프로그램이다. 북버지니아는 증설은 있어도 신규 건설 비중이 애틀랜타만 못하다. 필요한 것은 운영 기술직인데, 그건 **채용 공고(⑤)로 뽑지 훈련 프로그램으로 뽑지 않는다.**

**가설 C — 측정의 문제. 실제로는 있는데 못 찾았다.**
②는 파트너 대학 목록이 공개돼 있지 않다(전 세계 12곳, 40개 이상 기관 주장). 북버지니아 커뮤니티 칼리지(NOVA 등)에 유사 과정이 있어도 "Datacenter Academy" 브랜드가 아니면 이 조사에 안 잡힌다.

> **C를 먼저 배제해야 A·B를 말할 수 있다.** 지금은 배제하지 못했으므로 위 표의 북버지니아 ② 칸은 `❌`가 아니라 **`❓`** 다.

## ③④가 표에서 거의 전부 ⭕인 이유 — 그리고 그게 왜 함정인가

TradesFutures는 **34개 주**, Google.org/etA는 **20개 주 이상**에서 돌아간다. 거의 모든 클러스터가 사정권이다.

**그런데 이 ⭕는 "지원할 수 있다"가 아니다.**

- ③ TradesFutures는 **견습 준비**(MC3 교육)이지 견습 자체가 아니다. 본 게임은 **지역 노조 local의 선발**이고, 그건 별도 일정으로 열리고 닫힌다
- ④ Google.org는 **자금 지원**이다. 모집 주체는 IBEW/NECA 지역 훈련센터다

M5가 실물로 확인한 것이 이 함정이다 — **워싱턴주 PSEJATC는 2026-05-01부터 신규 접수를 중단했다.** 주 단위로는 "⭕ 34개 주에 포함"인데 실제로는 문이 닫혀 있었다.

> **광역 프로그램의 ⭕는 "당신 지역 지부에 물어보라"는 뜻이지 "열려 있다"는 뜻이 아니다.**

## 확인 불가로 남긴 것

정직하게 적어 둔다. 0으로 기록하지 않는다.

- **② MS DCA 전체 파트너 목록** — 공식 페이지에 전체 목록이 없다. 확인된 미국 4곳(Big Bend·DMACC·Estrella Mountain·Glendale) 외에 더 있을 가능성이 높다 (전 세계 12곳 주장)
- **③ TradesFutures 34개 주의 구체적 목록** — 숫자만 공개돼 있고 주 이름 목록은 없다
- **④ etA 20개 주 목록** — 같은 이유
- **AWS `data center technician` 미국 주별 분포** — API가 6회 재시도에도 응답하지 않았다. **확인 불가이지 0이 아니다**
- **① Meta AWA 4개 도시 이후 확대 계획** — "first launch"라는 표현으로 보아 확대 예정이나 일정 미공개

## 참조

- [Meta launches program to train workers for data center jobs — CBS News](https://www.cbsnews.com/news/meta-data-center-workforce-academy-training/)
- [Columbus named one of four cities to host Meta workforce academy](https://www.10tv.com/article/news/local/columbus-chosen-to-host-meta-workforce-academy/530-5735cfe6-d875-4ffc-aa7a-4b2e62604e6f)
- [Microsoft Datacenter Academy — Big Bend CC](https://local.microsoft.com/blog/big-bend-community-college-cultivates-a-hometown-tech-workforce/)
- [Microsoft Datacenter Academy — West Valley Phoenix](https://local.microsoft.com/blog/microsoft-datacenter-academy-in-the-west-valley-phoenix-az/)
- [DMACC West Campus Microsoft Datacenter Academy](https://www.dmacc.edu/west/microsoft-data-center.html)
- [NABTU × Microsoft 확대 발표 (2026-04-21)](https://nabtu.org/press_releases/nabtu-and-microsoft-expand-nationwide-initiative-to-strengthen-ai-training-and-career-pathways-across-the-skilled-trades/)
- [NECA / Google.org etA 지원 (2026-06-12)](https://www.necanet.org/news-media/detail/press-releases/2026/06/12/neca-applauds-google.org-for-support-of-the-electrical-training-alliance-and-skilled-trades-growth)
- `amazon.jobs` 검색 API 전수 조회 (2026-08-30, 4회 반복 일관성 확인)
