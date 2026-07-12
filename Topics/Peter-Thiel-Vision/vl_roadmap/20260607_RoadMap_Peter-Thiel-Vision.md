# Peter-Thiel-Vision 학습 로드맵

**생성일**: 2026-06-07  
**방법론**: VibeLearn AI  
**버전**: 1.0  
**방법론 버전**: VibeLearn AI 2.0

## 학습 기간 적정성 분석

**사용자 입력 기간**: 2주 집중 학습 또는 12-15시간  
**Topic 복잡도**: 중간-복잡  
**권장 기간**: 2주 또는 12-18시간

**분석 결과**: 적정하다. 피터 틸 학습은 단순 인물 요약이 아니라 세계관, 기업 사례, 투자 네트워크, 정치적 영향력, 국방 AI, 민주주의 비판, 한국 AI 생태계 적용까지 포함한다. 학술 논문 수준의 완결성을 목표로 하면 더 긴 시간이 필요하지만, 에세이와 방송 콘텐츠로 이어질 수 있는 리서치 기반을 만드는 목적이라면 2주 집중 학습이 현실적이다.

**조치 제안**: 입력한 기간으로 진행한다. 다만 M2 웹 리서치는 자료가 많아질 수 있으므로, 출처 맵을 완벽하게 만드는 것보다 후속 모듈에 필요한 핵심 출처를 우선한다.

## 학습 개요

### Topic 소개

`Peter-Thiel-Vision`은 **"피터 틸이 바라는 세상은 과연 옳은가?"**라는 질문을 중심으로 피터 틸의 사상과 현실적 영향력을 CUA_VL 방식으로 학습하는 Topic이다. 로컬 Vault 자료와 웹 자료를 모두 활용하되, 자료 수집 자체가 목적이 아니라 다음 학습자가 따라올 수 있는 구조화된 리서치 산출물을 만드는 것이 목표다.

### 학습 목표

- [ ] 피터 틸의 핵심 명제 5개 이상을 원문 인용과 함께 설명할 수 있다.
- [ ] Palantir, Founders Fund, Anduril, PayPal Mafia, 정치 프로젝트를 각각 별도 문서로 분석할 수 있다.
- [ ] 주요 주장별 찬성 논리, 반론, 판단 기준을 매트릭스로 정리할 수 있다.
- [ ] 한국 AI 스타트업과 개인 창작자 관점에서 피터 틸 철학의 유효성과 한계를 설명할 수 있다.
- [ ] 최종 에세이 아웃라인과 리서치 종합 문서를 작성할 수 있다.

### 예상 학습 기간

2주 집중 학습 또는 12-15시간

### 학습 환경

- OS: Windows 11
- 도구: VS Code, PowerShell, `rg`, Obsidian Vault, Codex/Claude 계열 AI 에이전트, Web search
- 사전 지식: 스타트업/VC 기본 개념, AI와 플랫폼 기업 기본 이해, Obsidian wiki link와 Vault 검색 사용법
- 권장 배경: `Zero to One`, Palantir, Founders Fund, Anduril, PayPal Mafia, 민주주의/독점/국방 AI 관련 기초 관심

## 전체 로드맵 구조

| 모듈 | 모듈명 | 상태 | 난이도 | 예상 시간 | 산출물 폴더 |
|------|--------|------|--------|-----------|-------------|
| M1 | 로컬 자료 맵 작성 | ⏭ 건너뜀 | ⭐ | 2h | `vl_materials/` |
| M2 | 웹 리서치 맵과 출처 체계 구축 | ⏭ 건너뜀 | ⭐⭐ | 3h | `vl_materials/` |
| M3 | 피터 틸 세계관 재구성 | ✅ 완료 (6/14~6/19) | ⭐⭐ | 2.5h | `01-Worldview-Reconstruction/` |
| M4 | 사업·권력 네트워크 분석 | ✅ 완료 (6/19) | ⭐⭐⭐ | 3h | `02-Business-and-Power-Network/` |
| M5 | 비판 프레임 + 찬반 매트릭스 | 🔶 부분 완료 | ⭐⭐⭐ | 3h | `03-Critical-Debates/` |
| **M5.5** | **본인 AI 세계관 정리 & 피터 틸 비전 평가** | **🔄 진행 중** | ⭐⭐⭐ | 3h | `04-Alternative-Vision/` |
| **M5.6** | **CP 관점 심화 리서치 — 플라톤 & 봉건제→자본주의** | **⏳ 다음 작업** | ⭐⭐⭐ | 4h | `vl_materials/`, `03-Critical-Debates/` |
| M6 | Capstone 에세이 리서치 종합 | ⏳ 대기 | ⭐⭐⭐ | 2h | `05-Capstone-Essay/` |

**총 예상 시간**: 22.5시간 (M5.6 추가로 +4h)

## 모듈별 상세 계획

### M1 - 로컬 자료 맵 작성

**난이도**: ⭐  
**예상 시간**: 2h  
**산출물 폴더**: `vl_materials/`

#### 학습 목표

- [ ] Vault 내부의 피터 틸 관련 직접 자료와 간접 자료를 찾을 수 있다.
- [ ] Topic 파일과 원본 클리핑/노트를 구분해 출처 추적 기준을 세울 수 있다.
- [ ] 내부 자료의 강점과 빈틈을 요약할 수 있다.

#### 주요 개념

1. **Local Source Map**: Vault 내부에서 이미 축적된 지식의 위치와 활용 가능성을 정리한 지도.
2. **원본 우선 링크**: Topic 인덱스보다 클리핑, 책 노트, 행사 기록 같은 원자료를 우선 링크하는 방식.
3. **리서치 빈틈**: 내부 자료만으로 답하기 어려운 질문 목록.

#### 실습 과제

**실습 1: Vault 검색 쿼리 실행 계획 작성** ⭐  
- **목적**: 내부 자료 탐색 범위를 명확히 한다.
- **단계**:
  1. 피터 틸, Thiel, Palantir, Anduril, Founders Fund 등 검색어 목록을 작성한다.
  2. `Topics`, `Roundup`, `Ingest`, `AI`, `Projects`, `Publish` 중 검색 대상과 이유를 정한다.
  3. 결과 분류 기준을 직접 자료, 간접 자료, 맥락 자료, 제외 자료로 나눈다.
- **예상 시간**: 30분
- **검증**: `vl_materials/local-source-map.md`에 검색어와 대상 폴더가 기록되어 있다.

**실습 2: 로컬 자료 맵 작성** ⭐⭐  
- **목적**: 내부 자료를 원본 중심으로 정리한다.
- **단계**:
  1. `rg`로 로컬 검색을 수행한다.
  2. 관련 파일을 원본 노트 중심으로 분류한다.
  3. 각 자료의 활용 가능성과 부족한 점을 기록한다.
- **예상 시간**: 75분
- **검증**: 최소 5개 이상의 내부 후보 자료 또는 "자료 없음" 사유가 정리되어 있다.

**실습 3: 리서치 빈틈 목록 작성** ⭐  
- **목적**: M2 웹 리서치에서 찾아야 할 질문을 만든다.
- **단계**:
  1. 내부 자료로 답할 수 있는 질문과 답할 수 없는 질문을 나눈다.
  2. 웹에서 확인해야 할 주장, 기업 정보, 비판 논점을 기록한다.
  3. M2 검색 쿼리 초안을 만든다.
- **예상 시간**: 15분
- **검증**: 웹 리서치 질문 10개 이상이 작성되어 있다.

#### 산출물

```text
vl_materials/
├── local-source-map.md
└── research-gaps.md

vl_worklog/
└── YYYYMMDD_M1_Peter-Thiel-Vision.md
```

#### Definition of Done

- [ ] 내부 검색어 목록 작성
- [ ] 검색 대상 폴더와 이유 정리
- [ ] 관련 내부 자료 후보 정리
- [ ] 원본 링크 우선 원칙 적용
- [ ] M2용 리서치 빈틈 목록 작성
- [ ] WorkLog 작성 완료
- [ ] Daily Retrospective 작성

#### Self-Assessment

**개념 이해**:
- [ ] 내부 자료와 외부 자료의 역할을 구분해 설명할 수 있다.
- [ ] 원본 링크 우선 원칙이 왜 중요한지 설명할 수 있다.

**실무 활용**:
- [ ] AI에게 추가 Vault 검색을 정확히 요청할 수 있다.
- [ ] 검색 결과가 부족할 때 다음 질문을 설계할 수 있다.

#### 예상 시간 배분

- 개념 학습: 20분
- 실습 1: 30분
- 실습 2: 55분
- 실습 3 및 문서화: 15분
- **합계**: 2h

#### 참조 자료

- `topic_info.md`: Topic 목표와 범위
- `vl_prompts/Peter Thiel Vision Research (PTV).md`: 세부 연구 프롬프트
- [[Roundup/2026-05-19 - Live11 Weekly Rundown#4️⃣ 4부: 피터 틸이 꿈꾸는 세상 — 라이브 리서치 & 에세이 프리뷰|Live #11 Rundown 피터 틸 섹션]]

### M2 - 웹 리서치 맵과 출처 체계 구축

**난이도**: ⭐⭐  
**예상 시간**: 3h  
**산출물 폴더**: `vl_materials/`

#### 학습 목표

- [ ] 피터 틸 관련 웹 자료를 1차, 준1차, 비판 자료, 맥락 자료로 분류할 수 있다.
- [ ] 핵심 인용 후보와 출처 신뢰도를 함께 정리할 수 있다.
- [ ] 최신 기업·정치·국방 AI 관련 정보는 웹으로 확인하고 확인 날짜를 남길 수 있다.

#### 주요 개념

1. **1차 자료**: 책, 인터뷰, 강연, 공식 문서처럼 당사자 발화나 공식 기록에 가까운 자료.
2. **비판 자료**: 감시, 독점, 민주주의, 국방 AI 등 피터 틸 비전에 반대하거나 위험을 지적하는 자료.
3. **Quote Bank**: 에세이에 사용할 수 있는 짧은 원문 인용과 해석 모음.

#### 실습 과제

**실습 1: 웹 리서치 쿼리 설계** ⭐  
- **목적**: 광범위하지만 통제된 검색을 준비한다.
- **단계**:
  1. 세계관, 기업, 정치, 비판, 한국 적용 영역으로 검색 범주를 나눈다.
  2. 각 범주별 검색 쿼리를 3개 이상 만든다.
  3. 1차 자료 우선순위와 비판 자료 우선순위를 분리한다.
- **예상 시간**: 40분
- **검증**: `web-source-map.md`에 범주별 검색 쿼리가 작성되어 있다.

**실습 2: 출처 맵 작성** ⭐⭐  
- **목적**: 자료 유형과 신뢰도를 구분한다.
- **단계**:
  1. 검색 결과를 1차, 준1차, 비판, 맥락 자료로 분류한다.
  2. 각 출처의 핵심 주장과 활용 목적을 기록한다.
  3. 최신성이 필요한 정보에는 확인 날짜를 남긴다.
- **예상 시간**: 100분
- **검증**: `web-source-map.md`와 `source-bibliography.md`가 작성되어 있다.

**실습 3: 인용 뱅크 초안 작성** ⭐⭐  
- **목적**: 후속 논증에 필요한 원문 인용 후보를 확보한다.
- **단계**:
  1. 핵심 원문 인용 후보를 짧게 수집한다.
  2. 각 인용의 문맥과 에세이 활용 가능성을 기록한다.
  3. 저작권 제한을 고려해 긴 원문 복사는 피한다.
- **예상 시간**: 40분
- **검증**: 핵심 인용 후보 10개 이상과 해석 메모가 있다.

#### 산출물

```text
vl_materials/
├── web-source-map.md
├── source-bibliography.md
└── quote-bank.md

vl_worklog/
└── YYYYMMDD_M2_Peter-Thiel-Vision.md
```

#### Definition of Done

- [ ] 검색 쿼리 세트 작성
- [ ] 1차/준1차/비판/맥락 자료 분류
- [ ] 최신 정보 확인 날짜 기록
- [ ] 인용 후보 10개 이상 정리
- [ ] 출처별 활용 목적 작성
- [ ] WorkLog 작성 완료
- [ ] Daily Retrospective 작성

#### Self-Assessment

**개념 이해**:
- [ ] 피터 틸의 직접 발화와 타인의 해석을 구분할 수 있다.
- [ ] 출처 신뢰도 기준을 설명할 수 있다.

**실무 활용**:
- [ ] AI에게 웹 리서치를 맡길 때 출처 우선순위를 지시할 수 있다.
- [ ] 신뢰도 낮은 자료를 배제하거나 보조 자료로 제한할 수 있다.

#### 예상 시간 배분

- 개념 학습: 30분
- 실습 1: 40분
- 실습 2: 100분
- 실습 3 및 문서화: 30분
- **합계**: 3h 20m. 필요 시 실습 2 범위를 줄여 3h로 조정한다.

#### 참조 자료

- `vl_materials/research-gaps.md`: M1에서 도출한 웹 리서치 질문
- Peter Thiel 공식 인터뷰와 강연: 직접 발화 확인용
- Palantir, Founders Fund, Anduril 공식 자료: 기업 사례 확인용

### M3 - 피터 틸 세계관 재구성

**난이도**: ⭐⭐  
**예상 시간**: 2.5h  
**산출물 폴더**: `01-Worldview-Reconstruction/`

#### 학습 목표

- [ ] 경쟁, 독점, 비밀, 기술 정체론, 민주주의 회의론, 불멸 추구를 하나의 세계관으로 연결할 수 있다.
- [ ] 각 핵심 명제를 원문 인용과 함께 설명할 수 있다.
- [ ] 피터 틸식 contrarian thinking의 장점과 위험을 구분할 수 있다.
- [ ] 민주주의와 자본주의에 대한 피터 틸의 세계관을 정리하고, 페이팔 사단의 미래 비전을 하나의 프레임으로 통합할 수 있다.

#### 주요 개념

1. **Competition is for losers**: 경쟁보다 독점적 위치를 만드는 것이 창업의 핵심이라는 주장.
2. **Secrets**: 아직 발견되지 않았거나 말해지지 않은 중요한 진실.
3. **Technological stagnation**: 디지털 혁신과 원자 세계 혁신의 불균형에 대한 문제의식.
4. **Contrarian thinking**: 모두가 동의하지 않는 중요한 진실을 찾는 사고방식.
5. **민주주의와 자본주의 세계관**: 틸의 민주주의 회의론(대중 민주주의 불신)과 독점적 자본주의 옹호 — 두 입장이 어떻게 연결되는지.
6. **미래 비전**: 불멸 추구, 장수 기술, 우주 개척, 기술 가속주의 등 틸과 페이팔 사단이 그리는 세계의 미래.

#### 실습 과제

**실습 1: 핵심 명제 카드 작성** ⭐⭐  
- **목적**: 피터 틸의 사상을 주장 단위로 분해한다.
- **단계**:
  1. `quote-bank.md`에서 핵심 인용 후보를 고른다.
  2. 각 명제를 한 문장으로 요약한다.
  3. 원문 인용, 해석, 비판 가능성을 함께 기록한다.
- **예상 시간**: 60분
- **검증**: 5개 이상 명제가 원문 인용, 요약, 해석으로 정리되어 있다.

**실습 2: 세계관 맵 작성** ⭐⭐  
- **목적**: 명제 간 관계를 시각화한다.
- **단계**:
  1. 독점, 비밀, 기술 정체론, 민주주의 회의론, 불멸 추구의 관계를 정리한다.
  2. Mermaid 또는 표로 관계를 표현한다.
  3. 세계관의 강점과 위험을 구분한다.
- **예상 시간**: 50분
- **검증**: 명제 간 관계가 Mermaid 또는 표로 표현되어 있다.

**실습 3: 모듈 README 작성** ⭐  
- **목적**: 다음 학습자가 학습 순서를 이해할 수 있게 한다.
- **단계**:
  1. 생성된 문서를 학습 순서대로 배열한다.
  2. 각 문서에 상대 경로 링크와 1줄 설명을 붙인다.
  3. 이전/다음 모듈 링크를 넣는다.
- **예상 시간**: 40분
- **검증**: 모듈 학습 순서와 문서 링크가 README에 정리되어 있다.

#### 산출물

```text
01-Worldview-Reconstruction/
├── README.md
├── core-claims.md
├── thiel-worldview-map.md
└── democracy-capitalism-future-vision.md

vl_worklog/
└── YYYYMMDD_M3_Peter-Thiel-Vision.md
```

#### Definition of Done

- [ ] 핵심 명제 5개 이상 정리
- [ ] 원문 인용과 해석 포함
- [ ] 세계관 관계 맵 작성
- [ ] 민주주의·자본주의 세계관 및 미래 비전 문서 작성
- [ ] README 작성
- [ ] WorkLog 작성 완료
- [ ] Daily Retrospective 작성

#### Self-Assessment

**개념 이해**:
- [ ] 피터 틸 세계관을 3분 안에 설명할 수 있다.
- [ ] 명제와 개인적 평가를 분리할 수 있다.

**실무 활용**:
- [ ] AI에게 이 세계관을 바탕으로 에세이 구조를 요청할 수 있다.
- [ ] AI가 만든 요약이 원문 근거와 맞는지 검토할 수 있다.

#### 예상 시간 배분

- 개념 학습: 30분
- 실습 1: 60분
- 실습 2: 40분
- 실습 3 및 문서화: 20분
- **합계**: 2.5h

#### 참조 자료

- `vl_materials/quote-bank.md`: 핵심 인용 후보
- `vl_materials/source-bibliography.md`: 출처별 신뢰도와 활용 목적

### M4 - 사업·권력 네트워크 분석

**난이도**: ⭐⭐⭐  
**예상 시간**: 3h  
**산출물 폴더**: `02-Business-and-Power-Network/`

#### 학습 목표

- [ ] 피터 틸의 철학이 Palantir, Anduril, Founders Fund, PayPal Mafia에서 어떻게 제도화되었는지 분석할 수 있다.
- [ ] "그가 말했다"와 "그가 만든 구조"를 분리해 설명할 수 있다.
- [ ] 감시, 국방 AI, 사유화, 엘리트 네트워크의 쟁점을 구분할 수 있다.

#### 주요 개념

1. **Palantir model**: 데이터 분석, 국가 안보, 민간 기업의 공공 권력 참여.
2. **Defense AI**: AI 기술과 국방 산업의 결합.
3. **Network power**: 창업자·투자자 네트워크가 산업과 정치 영향력으로 확장되는 방식.
4. **Public-private power shift**: 공공 권한이 민간 기술 기업으로 이동하는 현상.
5. **DOGE와 정부 효율화**: 트럼프 2기에서 페이팔 사단이 주도하는 정부 효율부(DOGE)의 역할과 기술 엘리트의 정부 개입.
6. **트럼프 2기 권력 구조**: 머스크·틸·JD 밴스 등 페이팔 사단이 트럼프 2기 행정부에서 맡은 구체적 역할과 영향력.

#### 실습 과제

**실습 1: 사례별 분석 문서 작성** ⭐⭐  
- **목적**: 피터 틸의 철학이 실제 조직과 사업에 어떻게 반영되었는지 본다.
- **단계**:
  1. Palantir, Anduril, Founders Fund, PayPal Mafia 자료를 나눈다.
  2. 각 사례의 핵심 기능, 권력 구조, 비판 지점을 정리한다.
  3. 피터 틸 세계관과 연결되는 지점을 표시한다.
- **예상 시간**: 100분
- **검증**: Palantir, Anduril, PayPal Mafia 중 최소 3개 사례가 별도 섹션으로 정리되어 있다.

**실습 2: 권력 네트워크 맵 작성** ⭐⭐⭐  
- **목적**: 기업, 투자, 정치, 국방 연결을 구조적으로 이해한다.
- **단계**:
  1. 주요 기업과 인물을 노드로 정리한다.
  2. 투자, 창업, 정치, 국방 관계를 엣지로 표현한다.
  3. 네트워크가 만드는 사회적 효과를 요약한다.
- **예상 시간**: 45분
- **검증**: 기업, 투자, 정치, 국방 연결이 표 또는 Mermaid로 정리되어 있다.

**실습 3: 모듈 README 작성** ⭐  
- **목적**: 분석 문서를 학습 순서대로 재사용 가능하게 만든다.
- **단계**:
  1. 사례 분석 문서를 학습 순서대로 배열한다.
  2. 각 문서의 목적을 1줄로 설명한다.
  3. 이전/다음 모듈 링크를 넣는다.
- **예상 시간**: 35분
- **검증**: 모듈 문서 링크와 학습 순서가 정리되어 있다.

#### 산출물

```text
02-Business-and-Power-Network/
├── README.md
├── palantir-and-surveillance.md
├── anduril-and-defense-ai.md
├── paypal-mafia-and-power-network.md
└── trump-admin-and-doge.md

vl_worklog/
└── YYYYMMDD_M4_Peter-Thiel-Vision.md
```

#### Definition of Done

- [ ] Palantir 분석 작성
- [ ] Anduril/국방 AI 분석 작성
- [ ] PayPal Mafia/네트워크 권력 분석 작성
- [ ] DOGE·트럼프 2기 행정부 역할 분석 작성
- [ ] 철학과 실제 제도화 연결
- [ ] README 작성
- [ ] WorkLog 작성 완료
- [ ] Daily Retrospective 작성

#### Self-Assessment

**개념 이해**:
- [ ] 피터 틸의 사상이 실제 기업 구조와 어떻게 연결되는지 설명할 수 있다.
- [ ] 공공 권력과 민간 기술 기업의 결합이 왜 논쟁적인지 설명할 수 있다.

**실무 활용**:
- [ ] AI가 만든 기업 분석에서 과장과 사실을 구분할 수 있다.
- [ ] 최신 기업 정보 확인이 필요한 지점을 식별할 수 있다.

#### 예상 시간 배분

- 개념 학습: 30분
- 실습 1: 100분
- 실습 2: 30분
- 실습 3 및 문서화: 20분
- **합계**: 3h

#### 참조 자료

- `vl_materials/web-source-map.md`: 기업별 웹 자료
- Palantir, Founders Fund, Anduril 공식 자료: 최신 기업 정보 확인용

### M5 - 비판 프레임과 한국 AI 적용

**난이도**: ⭐⭐⭐  
**예상 시간**: 3h  
**산출물 폴더**: `03-Critical-Debates/`, `04-Korea-AI-Implications/`

#### 학습 목표

- [ ] 피터 틸의 핵심 주장마다 찬성 논리, 반론, 판단 기준을 만들 수 있다.
- [ ] 독점, 민주주의, 국방 AI, 불멸 추구의 쟁점을 균형 있게 설명할 수 있다.
- [ ] 한국 AI 스타트업과 개인 창작자에게 적용 가능한 교훈을 정리할 수 있다.

#### 주요 개념

1. **Claim-counterclaim matrix**: 주장, 근거, 반론, 판단 기준을 한 표에 놓는 방식.
2. **기술 엘리트주의**: 기술 창업자와 투자자가 사회 설계 권한을 더 많이 가져야 한다는 암묵적 또는 명시적 관점.
3. **한국 적용성**: 미국식 스타트업 철학이 한국 사회·시장 구조에서 갖는 유효성과 한계.
4. **Platform monopoly risk**: 창조적 독점론이 플랫폼 독점 정당화로 바뀔 위험.

#### 실습 과제

**실습 1: 비판 매트릭스 작성** ⭐⭐  
- **목적**: 찬반을 넘어 판단 기준을 만든다.
- **단계**:
  1. 독점, 민주주의, 국방 AI, 불멸 추구, 스타트업 철학을 쟁점으로 둔다.
  2. 각 쟁점마다 찬성 논리와 반론을 작성한다.
  3. 최종 판단 기준을 별도 열로 정리한다.
- **예상 시간**: 70분
- **검증**: 최소 5개 쟁점에 대해 찬성 논리, 비판 논리, 판단 기준이 있다.

**실습 2: 한국 AI 적용 문서 작성** ⭐⭐⭐  
- **목적**: 피터 틸 철학을 한국 맥락에서 그대로 가져올 수 있는지 검토한다.
- **단계**:
  1. 한국 스타트업, 국방/공공 AI, 개인 창작자, 플랫폼 전략 관점으로 나눈다.
  2. 유효한 교훈과 위험한 교훈을 분리한다.
  3. Catch Up AI와 AI4PKM 맥락에서 활용 가능한 질문을 만든다.
- **예상 시간**: 70분
- **검증**: 스타트업, 국방/공공 AI, 개인 창작자, 플랫폼 전략 관점이 포함되어 있다.

**실습 3: 모듈 README 작성** ⭐  
- **목적**: 비판 문서와 한국 적용 문서를 연결한다.
- **단계**:
  1. 두 폴더의 문서를 학습 순서대로 배열한다.
  2. 각 문서의 목적을 1줄로 설명한다.
  3. 이전/다음 모듈 링크를 넣는다.
- **예상 시간**: 40분
- **검증**: 두 모듈 폴더의 학습 순서와 링크가 정리되어 있다.

#### 산출물

```text
03-Critical-Debates/
├── README.md
└── claim-counterclaim-matrix.md

04-Korea-AI-Implications/
├── README.md
└── korean-ai-startup-lessons.md

vl_worklog/
└── YYYYMMDD_M5_Peter-Thiel-Vision.md
```

#### Definition of Done

- [ ] 5개 이상 쟁점의 찬반 매트릭스 작성
- [ ] 한국 AI 생태계 적용 문서 작성
- [ ] 스타트업과 개인 창작자 관점 포함
- [ ] README 2개 작성
- [ ] WorkLog 작성 완료
- [ ] Daily Retrospective 작성

#### Self-Assessment

**개념 이해**:
- [ ] 피터 틸을 영웅화하거나 악마화하지 않고 비판할 수 있다.
- [ ] 한국 맥락에서 그대로 가져오면 위험한 주장을 구분할 수 있다.

**실무 활용**:
- [ ] AI에게 균형 잡힌 반론 생성을 요청할 수 있다.
- [ ] 에세이에서 쓸 수 있는 판단 기준을 만들 수 있다.

#### 예상 시간 배분

- 개념 학습: 35분
- 실습 1: 70분
- 실습 2: 55분
- 실습 3 및 문서화: 20분
- **합계**: 3h

#### 참조 자료

- `01-Worldview-Reconstruction/core-claims.md`: 핵심 주장
- `02-Business-and-Power-Network/README.md`: 실제 제도화 사례
- 한국 AI/스타트업 관련 내부 노트: 한국 적용성 검토용

---

### M5.5 - 본인 AI 세계관 정리 & 피터 틸 비전 평가 ← **다음 작업**

**추가일**: 2026-06-27
**난이도**: ⭐⭐⭐
**예상 시간**: 3h
**산출물 폴더**: `04-Alternative-Vision/`

#### 배경 및 목적

에세이 4부(글쓴이 관점)를 쓰기 전, 본인의 AI 시대 세계관을 영상 기록에서 직접 끌어낸다. 피터 틸의 세계관(M3/M4)과 비판 프레임(M5)을 이미 정리한 상태에서, "그렇다면 나는 어떤 세계관을 가지고 있는가?"를 체계적으로 정리하는 작업이다.

**소스**: AI & Humanity 플레이리스트 11개 영상 전사 (이미 확보)
- `Ingest/YouTube/playlists/ai-humanity/_index.md` 참조

#### 학습 목표

- [ ] AI & Humanity 11개 영상 전사에서 본인의 핵심 주장 5개 이상 추출할 수 있다.
- [ ] 정치·사회·AI 관련 본인의 일관된 관점을 하나의 문서로 정리할 수 있다.
- [ ] 본인 세계관과 피터 틸 세계관의 공통점·차이점을 비교 정리할 수 있다.
- [ ] 피터 틸 비전의 유효성과 한계를 본인 관점에서 평가할 수 있다.

#### 주요 개념

1. **본인 세계관 축**: 11개 영상에서 반복되는 핵심 입장 (AI와 인간, 노동, 민주주의, 창의성)
2. **대안 비전**: 틸의 엘리트·독점 비전 대신 개인 역량 확장 모델
3. **Catch Up AI 철학**: VibeLearn AI, Vibe Guiding이 그 대안의 실천적 증거

#### 11개 영상 주제 분류

| 주제 | 영상 | 핵심 질문 |
|------|------|---------|
| 인간의 가치·무가치함 | 모두가 자신의 무가치함과 싸우고 있다 (KR+EN) | AI 시대에 인간은 더 쓸모없어지는가? |
| AI를 향한 사회적 시각 | 시애틀 사람들은 AI를 어떻게 느낄까 (KR+EN) | 사람들은 AI를 어떻게 받아들이는가? |
| 휴먼터치와 AI | 스타벅스는 왜 바리스타를 더 고용했나 (KR+EN) | AI가 강해질수록 휴먼터치는 왜 더 가치 있어지는가? |
| 노동의 의미 재정의 | 역사 속 "일 안 하면 쓸모없다" (KR+EN) | "일"이란 무엇인가, AI 시대에 노동은 어떻게 바뀌는가? |
| 정치·거버넌스와 AI | 계엄과 AI : 계엄 하의 경찰청장 | AI가 정치적 판단을 도운다면 어떻게 되는가? |
| AI 시대 인간 창의성 | GenAI 가 까발린 Human Creativity의 하찮음 | 인간 창의성은 AI에게 대체되는가? |
| 디지털 혁명과 아날로그 | AI: The Analog Revolution | AI 혁명의 본질은 무엇인가? |

#### 실습 과제

**실습 1: 영상 전사 핵심 추출 (2h)**
- 11개 영상 전사에서 정치·사회·AI 관련 본인의 핵심 발언 추출
- 주제별로 분류 (인간 가치, 노동, 민주주의, 창의성, AI 역할)
- 반복되는 입장과 일관된 논리 파악
- 산출물: `04-Alternative-Vision/my-worldview-from-videos.md`

**실습 2: 본인 세계관 vs 피터 틸 비교 정리 (1h)**
- M3 `core-claims.md`, `thiel-worldview-map.md`와 대조
- 공통점: "AI는 변화를 가속한다" 등
- 차이점: 누가 AI 시대의 주역인가, 독점 vs 개방, 엘리트 vs 개인
- 산출물: `04-Alternative-Vision/thiel-vs-my-worldview.md`

#### 산출물

```text
04-Alternative-Vision/
├── alternative-vision-draft.md      ← 기존 초안 (AI 작성, 본인 보완 필요)
├── my-worldview-from-videos.md      ← 새로 작성 (영상 전사 기반)
└── thiel-vs-my-worldview.md         ← 새로 작성 (비교 정리)

vl_worklog/
└── YYYYMMDD_M5.5_Peter-Thiel-Vision.md
```

#### Definition of Done

- [ ] 11개 영상 전사 검토 완료
- [ ] 본인 핵심 주장 5개 이상 추출 + 근거 인용 포함
- [ ] `my-worldview-from-videos.md` 작성
- [ ] `thiel-vs-my-worldview.md` 비교 작성 (M3 산출물과 대조)
- [ ] `alternative-vision-draft.md` 본인 관점으로 보완
- [ ] WorkLog 작성

#### 소스 자료

- `Ingest/YouTube/playlists/ai-humanity/_index.md` — 11개 영상 목록
- `01-Worldview-Reconstruction/core-claims.md` — 틸 핵심 주장 (비교 기준)
- `01-Worldview-Reconstruction/thiel-worldview-map.md` — 틸 세계관 맵
- `03-Critical-Debates/claim-counterclaim-matrix.md` — 찬반 매트릭스

---

### M5.6 - CP 관점 심화 리서치 — 플라톤 & 봉건제→자본주의 ← **다음 작업**

**추가일**: 2026-07-03
**난이도**: ⭐⭐⭐
**예상 시간**: 4h
**산출물 폴더**: `vl_materials/`, `03-Critical-Debates/`

#### 배경 및 목적

지금까지 피터 틸의 미래 비전을 리뷰하기 위해 자료를 모으는 과정(M3~M5.5)이었다면,
이제부터는 **CP의 관점을 제대로 정립**하기 위한 심화 리서치 단계다.

특히 피터 틸의 "기술 엘리트 독점 정당화" 논리를 반박하기 위해
두 가지 역사적 근거를 탄탄하게 구축한다:
1. **플라톤 철인 정치론** — 엘리트 지배 논리의 원형과 그 한계
2. **봉건제→자본주의 전환** — AI 시대 시스템 변화의 역사적 유추

**소스**: `vl_materials/essay-braindump-20260703.md` (CP 초안 메모)

#### 학습 목표

- [ ] 플라톤 철인 정치론의 핵심 주장과 형성 배경을 정리할 수 있다.
- [ ] 철인 정치론의 허점·비현실성을 피터 틸 기술 엘리트 독점 논리에 적용해 반박할 수 있다.
- [ ] 봉건제→자본주의 전환의 핵심 사건(나폴레옹, 파리 코뮌, 미국 건국, 권력 분립)을 정리할 수 있다.
- [ ] 이 역사적 유추를 AI 시대 시스템 변화 논거로 연결할 수 있다.

#### 주요 개념

1. **플라톤 철인 정치(Philosopher-King)**: 가장 지혜로운 자가 통치해야 한다는 플라톤의 주장 — 기술 엘리트 독점 정당화와의 구조적 유사성
2. **창조적 파괴의 한계**: 나폴레옹·공포정치·파리 코뮌이 새 시스템을 만들지 못한 이유
3. **권력 분립**: 봉건제를 대체한 핵심 메커니즘 — AI 시대 적용 가능성
4. **조지 워싱턴 모델**: 권력을 가진 자가 자발적으로 내려놓는 시스템 정착의 역할
5. **AI 시대 시스템 변화**: 자본주의 한계 도달 + AI 기술 발전 = 새 정치·경제 시스템 필요

#### 실습 과제

**실습 1: 플라톤 철인 정치론 리서치 (1.5h)**
- 철인 정치의 핵심 주장과 형성 배경 정리
- 실패 이유·비현실성 분석
- 피터 틸 기술 엘리트 독점 논리와 구조 비교
- 반박 논거 도출
- 산출물: `vl_materials/plato-philosopher-king-research.md`

**실습 2: 봉건제→자본주의 전환 역사 심층 조사 (1.5h)**
- 왕권 체제 한계 → 반복된 실패 (나폴레옹, 공포정치, 파리 코뮌)
- 미국 건국과 권력 분립의 역사적 의미
- 조지 워싱턴의 역할 — 새 시스템 정착의 조건
- AI 시대와의 유추 논거 구성
- 산출물: `vl_materials/feudalism-to-capitalism-research.md`

**실습 3: CP 관점 에세이 논거 통합 (1h)**
- 두 리서치를 피터 틸 반박 논거로 통합
- `03-Critical-Debates/claim-counterclaim-matrix.md` 업데이트
- `core-claims.md` 비판 섹션에 CP 관점 추가
- 에세이 아웃라인 반영 검토

#### 산출물

```text
vl_materials/
├── essay-braindump-20260703.md    ← 완료 (CP 초안 메모, GitHub 비공개)
├── plato-philosopher-king-research.md    ← 신규
└── feudalism-to-capitalism-research.md  ← 신규

03-Critical-Debates/
└── claim-counterclaim-matrix.md  ← CP 관점 반박 논거 추가

vl_worklog/
└── YYYYMMDD_M5.6_Peter-Thiel-Vision.md
```

#### Definition of Done

- [ ] 플라톤 철인 정치론 리서치 문서 작성
- [ ] 봉건제→자본주의 전환 리서치 문서 작성
- [ ] 피터 틸 기술 엘리트 독점 반박 논거 도출
- [ ] claim-counterclaim-matrix.md CP 관점 업데이트
- [ ] WorkLog 작성

---

### M6 - Capstone 에세이 리서치 종합

**난이도**: ⭐⭐⭐  
**예상 시간**: 2h  
**산출물 폴더**: `05-Capstone-Essay/`

#### 학습 목표

- [ ] M1-M5 산출물을 에세이용 논증 구조로 통합할 수 있다.
- [ ] "피터 틸이 바라는 세상은 과연 옳은가?"에 대한 잠정 결론을 쓸 수 있다.
- [ ] 방송/에세이 제작에 바로 연결되는 아웃라인을 만들 수 있다.

#### 주요 개념

1. **Research synthesis**: 자료 요약이 아니라 주장, 근거, 반론, 판단을 하나의 구조로 엮는 작업.
2. **Essay outline**: 독자가 따라올 수 있는 문제 제기, 논증, 결론의 흐름.
3. **Topic retrospective**: 학습 방법 자체를 돌아보고 다음 학습자가 활용할 개선점을 남기는 문서.

#### 실습 과제

**실습 1: 리서치 종합 문서 작성** ⭐⭐⭐  
- **목적**: M1-M5 산출물을 하나의 논증 구조로 통합한다.
- **단계**:
  1. 세계관, 기업 사례, 비판 프레임, 한국 적용을 연결한다.
  2. 핵심 주장별 근거와 반론을 정리한다.
  3. 에세이에서 사용할 중심 논지를 도출한다.
- **예상 시간**: 60분
- **검증**: 핵심 주장, 근거, 반론, 판단이 하나의 문서에 연결되어 있다.

**실습 2: 에세이 아웃라인 작성** ⭐⭐  
- **목적**: 방송/에세이 제작으로 바로 이어지는 구조를 만든다.
- **단계**:
  1. 제목 후보와 핵심 논지를 작성한다.
  2. 섹션별 주장과 인용 후보를 연결한다.
  3. 결론에서 피터 틸의 질문과 답을 분리해 판단한다.
- **예상 시간**: 35분
- **검증**: 제목, 핵심 논지, 섹션별 주장, 인용 후보가 있다.

**실습 3: Topic Retrospective 작성** ⭐  
- **목적**: CUA_VL 학습 방법 자체를 평가한다.
- **단계**:
  1. 계획 대비 실제 진행을 기록한다.
  2. 산출물 품질과 부족한 부분을 평가한다.
  3. 다음 학습자에게 남길 개선점을 정리한다.
- **예상 시간**: 25분
- **검증**: CUA_VL 방식의 효과, 한계, 다음 단계가 정리되어 있다.

#### 산출물

```text
05-Capstone-Essay/
├── README.md
├── peter-thiel-vision-research-synthesis.md
├── peter-thiel-vision-essay-outline.md
└── topic-retrospective.md

vl_worklog/
└── YYYYMMDD_M6_Peter-Thiel-Vision.md
```

#### Definition of Done

- [ ] 리서치 종합 문서 작성
- [ ] 에세이 아웃라인 작성
- [ ] 핵심 인용 후보 연결
- [ ] Topic Retrospective 작성
- [ ] 전체 산출물 링크 점검
- [ ] WorkLog 작성 완료
- [ ] Daily Retrospective 작성

#### Self-Assessment

**개념 이해**:
- [ ] 피터 틸 비전에 대해 찬반을 넘어선 판단 기준을 제시할 수 있다.
- [ ] 피터 틸의 질문과 피터 틸의 답을 분리해서 평가할 수 있다.

**실무 활용**:
- [ ] AI에게 에세이 초안 작성을 맡길 수 있을 정도로 요구사항과 근거를 정리할 수 있다.
- [ ] 이 Topic을 다른 학습자가 이어받을 수 있게 설명할 수 있다.

#### 예상 시간 배분

- 실습 1: 60분
- 실습 2: 35분
- 실습 3 및 링크 점검: 25분
- **합계**: 2h

#### 참조 자료

- M1-M5 전체 산출물
- `vl_materials/quote-bank.md`: 인용 후보
- `vl_materials/source-bibliography.md`: 출처 확인용

## WorkLog 작성 가이드

각 학습 세션마다 WorkLog를 작성하여 진행 상황을 추적한다.

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_Peter-Thiel-Vision.md`

**WorkLog 필수 섹션**:
1. 오늘의 학습 목표
2. 진행 내용
3. 문제 해결 로그
4. DoD 체크리스트
5. Daily Retrospective
6. 참조 및 산출물

## Retrospective 가이드

### Daily Retrospective

매 학습 세션 종료 시 WorkLog 안에 작성한다.
- What went well?
- What could be improved?
- Insights
- Tomorrow's focus

### Module Retrospective

모듈 완료 시 필요하면 `vl_worklog/YYYYMMDD_MX_Retrospective.md`를 작성한다.
- 계획 대비 실제 비교
- 핵심 학습 내용
- 발생한 문제와 해결
- Roadmap 정확도 평가
- 다음 모듈 준비사항

### Topic Retrospective

전체 Topic 완료 시 `05-Capstone-Essay/topic-retrospective.md`와 필요 시 `vl_worklog/YYYYMMDD_Peter-Thiel-Vision_Final_Retrospective.md`에 작성한다.
- 전체 학습 여정 통계
- VibeLearn AI 방법론 효과성 평가
- 산출물 품질 평가
- 향후 학습 개선 사항

## 전체 폴더 구조

```text
Peter-Thiel-Vision/
├── topic_info.md
├── vl_prompts/
│   ├── roadmap_prompt.md
│   ├── daily_learning_prompt.md
│   └── Peter Thiel Vision Research (PTV).md
├── vl_roadmap/
│   └── 20260607_RoadMap_Peter-Thiel-Vision.md
├── vl_worklog/
│   ├── 20260607_M0_Peter-Thiel-Vision.md
│   └── YYYYMMDD_MX_Peter-Thiel-Vision.md
├── vl_materials/
│   ├── local-source-map.md
│   ├── research-gaps.md
│   ├── web-source-map.md
│   ├── source-bibliography.md
│   └── quote-bank.md
├── 01-Worldview-Reconstruction/
│   ├── README.md
│   ├── core-claims.md
│   └── thiel-worldview-map.md
├── 02-Business-and-Power-Network/
│   ├── README.md
│   ├── palantir-and-surveillance.md
│   ├── anduril-and-defense-ai.md
│   └── paypal-mafia-and-power-network.md
├── 03-Critical-Debates/
│   ├── README.md
│   └── claim-counterclaim-matrix.md
├── 04-Korea-AI-Implications/
│   ├── README.md
│   └── korean-ai-startup-lessons.md
└── 05-Capstone-Essay/
    ├── README.md
    ├── peter-thiel-vision-research-synthesis.md
    ├── peter-thiel-vision-essay-outline.md
    └── topic-retrospective.md
```

## 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|------------|------|
| M0 | 2026-06-07 | 2026-06-07 | ✅ 완료 | 7/8 | 사용자 승인 후 M1 시작 |
| M1 | — | — | ⏳ 건너뜀 | 0% | 추후 보강 가능 |
| M2 | — | — | ⏳ 건너뜀 | 0% | 추후 보강 가능 |
| M3 | 2026-06-14 | 2026-06-19 | ✅ 완료 | 5/6 | thiel-worldview-map + README 추가 완료 |
| M4 | 2026-06-14 | 2026-06-19 | ✅ 완료 | 8/8 | palantir·anduril·paypal-mafia 완료 |
| M5 | 2026-06-14 | | 🔄 진행 중 | 1/5 | claim-counterclaim-matrix 완료, README 등 미완 |
| M5.5 | 2026-06-28 | | 🔄 진행 중 | 3/5 | alternative-vision-draft, my-worldview, thiel-vs-my-worldview 작성 |
| **M5.6** | — | — | **⏳ 다음 작업** | 0% | 플라톤 철인정치 + 봉건제→자본주의 리서치 필요 |
| M6 | 2026-06-14 | | 🔄 진행 중 | 2/6 | essay-outline 3부·에필로그 채움(2026-07-12), 종합 문서 미완 |

**범례**:
- ⏳ 대기
- 🔄 진행 중
- ✅ 완료

## 성공 기준

전체 Topic 완료 기준:
- [ ] 모든 모듈 완료 (DoD 100%)
- [ ] 로컬 자료와 웹 자료가 모두 정리됨
- [ ] 원문 인용과 출처가 검증됨
- [ ] 최소 5개 산출물 폴더 또는 자료 파일 완성
- [ ] 에세이 아웃라인과 리서치 종합 문서 완성
- [ ] Topic Retrospective 작성
- [ ] Self-Assessment 평균 ⭐⭐⭐⭐ 이상

## 로드맵 품질 체크

### 구조

- [x] 학습 기간에 맞는 6개 모듈 구성
- [x] 점진적 난이도 상승
- [x] 마지막 Capstone 모듈 포함
- [x] 각 모듈의 독립성 확보

### 각 모듈

- [x] 학습 목표 3개 이상
- [x] 주요 개념 3개 이상
- [x] 실습 과제 2-3개
- [x] 산출물 구조 명시
- [x] DoD 체크리스트 5-8개
- [x] Self-Assessment 포함
- [x] 시간 배분 명시
- [x] 참조 자료 포함

### VibeLearn AI 통합

- [x] WorkLog 가이드
- [x] Retrospective 가이드
- [x] 폴더 구조 명시
- [x] 진행 상황 추적 테이블

**생성자**: Codex with VibeLearn AI  
**Roadmap 버전**: 1.0  
**방법론 버전**: VibeLearn AI 2.0
