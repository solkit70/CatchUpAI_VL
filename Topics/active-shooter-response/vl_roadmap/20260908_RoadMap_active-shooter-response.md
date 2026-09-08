# active-shooter-response 학습 로드맵

**생성일**: 2026-09-08
**방법론**: VibeLearn AI
**버전**: 2.1 (시민단체 안전 교육 및 자원 연계 보강판)

---

## 📚 학습 개요

### Topic 소개
총기난사 사건 발생 시 일반 시민이 생명을 지키기 위한 대처 요령(DHS 자료 및 개인 교육 경험 기반)을 학습하고, **시민단체(NGO) 실무진 및 자원봉사자들이 이수할 수 있는 전문 교육 프로그램(FEMA, CRASE, ALICE)과 단체 안전망 구축을 위한 비상대응 자원(EAP, Tabletop, Stop the Bleed) 정보를 연계**하여, 이를 효과적으로 알릴 수 있는 Remotion AI 기반 교육 동영상을 기획/제작하는 종합 학습 과정.

### 학습 목표
- [x] 총기난사 발생 시 3대 핵심 대응 수칙(Run, Hide, Fight)과 대처 흐름을 말로 명확히 설명할 수 있다. (M1 완수)
- [ ] FEMA IS-907.A, CRASE, ALICE 등 시민단체 및 일반인이 이수할 수 있는 무료/유료 온·오프라인 실무자 교육 과정의 특징과 참여 경로를 가이드할 수 있다.
- [ ] 시민단체 비상행동계획(EAP) 가이드라인, CISA 시뮬레이션 키트, 지혈법(Stop the Bleed) 등 NGO 단체 안전망 구축에 도움되는 핵심 안전 자원을 매핑할 수 있다.
- [ ] Remotion용 슬라이드 플랜(`video-slide-plan.md`) 및 지루하지 않은 감정 마커 나레이션 스크립트를 작성할 수 있다.
- [ ] Remotion 동적 효과(Spring, Stagger, Motion Blur 등)와 다양한 슬라이드 타입을 적용해 UI 컴포넌트를 설계할 수 있다.
- [ ] TTS 스크립트(`gen_audio.py` 및 `gen_audio_qwen.py`)를 활용해 완벽하게 패딩이 적용된 한국어 음성을 생성할 수 있다.
- [ ] 비디오 렌더링을 성공적으로 완료하여 시민 단체 등 필요한 곳에 바로 전파할 수 있는 최종 MP4 영상을 확보한다.    

### 예상 학습 기간
1주 (총 12~15시간, 20% 버퍼 포함)

### 학습 환경
- OS: Windows 11
- 도구: Remotion Studio 4.0, Node.js, Python (v3.10+), FFmpeg
- 사전 지식: Markdown 구조적 글쓰기, React 기초 컴포넌트 이해

---

## 🗺️ 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 | 상태 |
|------|--------|--------|----------|------------|------|
| **M1** | 안전 지침 분석 및 NGO 유관 교육/자원 분석 | ⭐ | 3.0h | `01-DHS-Analysis/` | ✅ **완료 (2026-09-08)** |
| **M2** | NGO 비상대응 자원이 반영된 비디오 슬라이드 기획 | ⭐⭐ | 3.0h | `02-Remotion-Setup/` | ✅ **완료 (2026-09-08)** |
| **M3** | 모션 애니메이션 컴포넌트 및 배경 개발 | ⭐⭐⭐ | 4.0h | `03-Remotion-Development/` | 🔄 **진행 중** |
| **M4** | 나레이션 오디오 생성 및 자막 매핑 | ⭐⭐ | 2.5h | `04-TTS-Audio/` | ⏳ 대기 |
| **M5** | 최종 고화질 MP4 렌더링 및 시민 배포 패키지 마감 | ⭐⭐ | 2.5h | `05-Final-Delivery/` | ⏳ 대기 |

**총 예상 시간**: 15.0시간 (버퍼 20% 포함)

---

## 📖 모듈별 상세 계획

### M1 - 안전 지침 분석 및 NGO 유관 교육/자원 분석

**난이도**: ⭐
**예상 시간**: 3.0h
**산출물 폴더**: `01-DHS-Analysis/`
**상태**: ✅ 완료 (2026-09-08)

#### 학습 목표
- [x] DHS Webinar 전사 데이터(7월 27일 자)에서 Run, Hide, Fight 3대 대처 요령과 경찰 조우 시 행동 수칙을 완벽히 도출한다.
- [x] **FEMA IS-907.A(온라인 과정), CRASE(무료 Civilian Response), ALICE(조직형 대응) 등 NGO 실무자들이 참여할 수 있는 전문 교육 이수 경로 정보를 취합하고 정리한다.**
- [x] **시민단체의 자체 안전 훈련 및 자구책 구축에 필수적인 비상행동계획(EAP) 수립 가이드, CISA Tabletop 시뮬레이션, Stop the Bleed(지혈 교육) 자원 데이터를 정교하게 매핑한다.**
- [x] 취합된 핵심 안전 메시지와 NGO 전용 안전 자원을 포괄하는 가독성 높은 시민용 안전 매뉴얼 가이드북(`active_shooter_guide.md`)을 집필한다.

#### 주요 개념
1. **Run-Hide-Fight 수칙**: 시위, 점거, 다중밀집 장소에서 총기 난사 상황 발생 시 최우선 생존 지침.
2. **Civilian Training Pathways (FEMA/CRASE/ALICE)**: 시민과 자원봉사자들이 수강할 수 있는 정규 정부 및 민간 재난대응 과정.
3. **NGO Safety Kit (EAP, Tabletop, Stop the Bleed)**: 단체의 비상 작전 지속과 부상자 회생율을 높이기 위한 세 가지 핵심 구성 요소.

#### 실습 과제

**실습 1: DHS 웨비나 및 NGO 역량 강화 자료 분석** ⭐
- **목적**: 원본 DHS 전사록 분석 및 시민단체 대상의 교육 연계망 설계.
- **단계**:
  1. 제공된 DHS 국문/영문 가이드를 비교 검독하여 3대 대처 요령(Run, Hide, Fight)을 추출한다.
  2. FEMA IS-907.A, CRASE, ALICE, Stop the Bleed 등 실제 이수할 수 있는 전문 교육 과정의 주소와 이수 방식을 분석하고 가이드북 내용에 삽입한다.
- **검증**: `01-DHS-Analysis/webinar_digest.md` 내에 핵심 대화 발췌 및 이수 가이드라인 구축 완료.

**실습 2: NGO 맞춤형 시민 가이드북 개발** ⭐⭐
- **목적**: 생존 수칙 및 단체 대비 역량 강화를 전파하기 위한 통합 대응 가이드 구축.
- **단계**:
  1. 7월 26일 총격 사건 뉴스 흐름을 오프닝으로 세팅하여 경각심을 고취한다.
  2. Run, Hide, Fight 수칙을 정교화하고, 경찰 조우 시 행동 요령을 대조표로 작성한다.
  3. 시민단체 및 종교 시설을 위한 EAP 수립 가이드, CISA Tabletop Exercise 키트 사용법, Stop the Bleed 지혈 세트 구비 안내를 추가하여 종합 안내서로 완성한다.
- **검증**: `01-DHS-Analysis/active_shooter_guide.md`에 정교한 마크다운 문서로 반영 완료.

#### 산출물
```
01-DHS-Analysis/
├── README.md                 ← 학습 가이드 및 산출물 링크 (완료)
├── webinar_digest.md         ← 타임스탬프 인용 요약 및 전문 교육 경로 정리 (완료)
└── active_shooter_guide.md   ← 안전 가이드북 및 NGO 전용 비상 자원 연계 가이드 (완료)
```

#### Definition of Done (M1)
- [x] 모든 학습 목표 달성 (DHS 수칙 도출 완료)
- [x] 시민단체가 이수 가능한 온/오프라인 교육 자료(FEMA, CRASE, ALICE) 정합성 확인
- [x] NGO 유용 자원(EAP, Tabletop, Stop the Bleed) 데이터 매핑 완료
- [x] `webinar_digest.md` 및 `active_shooter_guide.md` 문서 정밀 집필 완료
- [x] WorkLog 및 Daily Retrospective 작성 완료

---

### M2 - NGO 비상대응 자원이 반영된 비디오 슬라이드 기획

**난이도**: ⭐⭐
**예상 시간**: 3.0h
**산출물 폴더**: `02-Remotion-Setup/`
**목표 상태**: ✅ 완료 (2026-09-08)

#### 학습 목표
- [ ] M1에서 취합한 생존 지침과 **NGO 전문 교육 참여 방법(FEMA IS-907.A, CRASE) 및 단체 비상 자원(EAP, Stop the Bleed) 가이드를 포괄하는 10장 구성의 비디오 슬라이드 플랜(`video-slide-plan.md`)**을 기획한다.
- [ ] 각 슬라이드에 어울리는 visual 에셋 매핑을 정의하는 `image-prompts.md` 명세서를 도출한다.
- [ ] 다중 슬라이드 템플릿(Title, Run-Hide-Fight, Training, NGO-Safety-Kit, Outro)에 전달될 정교한 데이터 구조인 `data.ts`를 정의한다.

#### 주요 개념
1. **NGO Capacity-Building Slide Sequence**: 단순 생존 수칙 나열을 넘어, 자원봉사자들에게 추가 전문 교육 이수를 독려하고 비상 자원을 제공하는 전용 슬라이드 기획.
2. **Visual Continuity (Art to Photo)**: AI가 생성한 예술적 배경 배경 이미지와 실제 연수 캡쳐 화면을 자연스럽게 융합하는 레이아웃.

#### 실습 과제

**실습 1: NGO 안전 교육 가이드가 포함된 `video-slide-plan.md` 설계** ⭐⭐
- **목적**: 생존 수칙 70% + NGO 전용 안전 자원 가이드 30% 비율의 지루하지 않은 영상 흐름 기획.
- **단계**:
  1. Run, Hide, Fight 및 경찰 대처 슬라이드를 먼저 순차 배치한다.
  2. **독립 슬라이드로 [교육 수강 안내 - FEMA & CRASE] 정보 카드를 설계한다.** (온라인 수강 주소 및 오프라인 무료 교육 안내 포함)
  3. **독립 슬라이드로 [시민단체 단합 훈련 Kit - EAP & Stop the Bleed] 카드를 배치하여 비상 구급 가방 구성과 시뮬레이션 키트를 홍보한다.**
  4. 슬라이드별 나레이션 대본 및 비주얼 매핑을 작성한다.
- **검증**: `02-Remotion-Setup/video-slide-plan.md` 내에 기획안과 나레이션 스크립트 작성 완료.

**실습 2: `image-prompts.md` 및 데이터 소스 `data.ts` 정의** ⭐⭐
- **목적**: 영상에 활용할 배경 및 가이드 이미지 프롬프트 명문화 및 컴포넌트 렌더링용 JSON 데이터 타입 확정.
- **단계**:
  1. 학습 및 자구책 홍보 슬라이드에 투영할 이미지의 테마(조명, 신뢰감을 주는 구조)를 반영한 영어 프롬프트를 작성한다.
  2. `data.ts` 데이터 원장에 슬라이드 제목, 본문 불렛(Bullet), 하단 추가 리소스 링크(FEMA, Stop the Bleed) 등을 객체 배열 형태로 명시한다.
- **검증**: `02-Remotion-Setup/image-prompts.md`와 `02-Remotion-Setup/data.ts` 파일이 무결하게 생성됨.

#### 산출물
```
02-Remotion-Setup/
├── README.md               ← M2 학습 가이드 및 산출물 목록
├── video-slide-plan.md     ← 3대 생존수칙 + NGO 교육 연계 슬라이드 기획 및 대본
├── image-prompts.md        ← 배경 AI 이미지 생성용 구체적 프롬프트 리스트
└── data.ts                 ← Remotion 컴포넌트 전체를 구동할 데이터 소스 원장
```

#### Definition of Done (M2)
- [ ] `video-slide-plan.md` 작성이 완료되고, FEMA 온라인 교육 및 NGO 비상 자원 가이드 슬라이드가 각각 1장 이상 독립 구성됨.
- [ ] `image-prompts.md`에 신뢰성 높은 배경 이미지 생성을 위한 고품질 프롬프트 10개 이상 작성 완료.
- [ ] `data.ts`에 슬라이드 렌더링을 제어하기 위한 구조화된 객체 배열이 타이핑 에러 없이 작성됨.
- [ ] WorkLog 및 Daily Retrospective 작성 완료.

---

### M3 - 모션 애니메이션 컴포넌트 및 배경 개발

**난이도**: ⭐⭐⭐
**예상 시간**: 4.0h
**산출물 폴더**: `03-Remotion-Development/`
**목표 상태**: ⏳ 대기

#### 학습 목표
- [ ] Remotion 프로젝트 내에 고품질 Glassmorphism 테마의 레이아웃을 구현한다.
- [ ] SlideType에 맞춰 순차적(Stagger)으로 팝업되는 React 컴포넌트 8종(`SlideTitle`, `SlideSection`, `SlideBullet`, `SlideCompare`, `SlideQuote`, `SlideStat`, `SlideTraining`, `SlideOutro`)을 개발한다.
- [ ] FEMA 교육 가이드 및 NGO Safety Kit 슬라이드 전용의 맞춤형 인터랙션(예: 마우스오버 느낌의 카드 스케일 모션, 원형 게이지) 컴포넌트를 연출한다.

#### 주요 개념
1. **Spring-based Stagger Animation**: `@remotion/transitions` 또는 `spring` 값을 활용한 물리 기반의 세련된 UI 등장 모션.
2. **Glassmorphism UI Frame**: 블러 처리된 반투명 배경과 미세한 경계선(Border)을 통해 전문적인 인포그래픽 느낌 선사.

#### 실습 과제

**실습 1: Remotion 베이스 테마 및 슬라이드 컴포넌트 개발** ⭐⭐⭐
- **목적**: 세련된 재난 대비 레이아웃 컴포넌트 구현.
- **단계**:
  1. `AI/RemotionStudio/src/active-shooter-0908/`에 개발 환경을 구성하고 슬라이드 기본 라우팅을 확보한다.
  2. 흐르는 어두운 도트 배경(`SlateDotsBackground`) 위에 유리처럼 빛나는 텍스트 및 이미지 패널 프레임을 코딩한다.
  3. `SlideTitle`, `SlideBullet`, `SlideCompare` 등 기본 컴포넌트 렌더러를 개발한다.
- **검증**: `npm run start` 실행 시 브라우저 프리뷰 창에 기본 슬라이드들이 정상적으로 등장하고 튀어오르는 모션이 확인됨.

**실습 2: NGO 자원/교육 카드 전용 슬라이드 뷰어 구현** ⭐⭐⭐
- **목적**: FEMA 교육 안내 및 EAP 훈련 킷을 직관적으로 보여주는 특화 컴포넌트 구축.
- **단계**:
  1. 무료 온라인 교육 이수 스텝을 인포그래픽(화살표 및 순차 하이라이팅)으로 렌더링하는 `SlideTraining` 컴포넌트를 구축한다.
  2. EAP, Tabletop, Stop the Bleed를 세련된 3열 그리드 카드로 렌더링하는 컴포넌트를 추가 개발한다.
- **검증**: `data.ts`를 교체하여 NGO 자원 슬라이드가 세련되게 스케일 애니메이션되며 렌더링되는가 확인.

#### 산출물
```
03-Remotion-Development/
├── README.md               ← M3 개발 가이드 및 재생 매뉴얼
├── SlideTraining.tsx       ← FEMA, CRASE 교육 경로 특화 컴포넌트 소스
├── SlateDotsBackground.tsx ← 세련된 인포그래픽 애니메이션 배경 소스
└── index.tsx (or main.tsx) ← 전체 Remotion 엔트리 포인트 등록 내용 백업
```

#### Definition of Done (M3)
- [ ] `SlideTraining`을 포함한 총 8가지 타입의 슬라이드 컴포넌트가 무결하게 빌드됨.
- [ ] `@remotion/transitions` 및 `spring`을 활용하여 모션 씹힘 없이 부드러운 화면 전환이 구현됨.
- [ ] 브라우저 개발자 도구 및 Remotion 콘솔 상에 React Warning이나 타입 오류가 전혀 검출되지 않음.

---

### M4 - 나레이션 오디오 생성 및 자막 매핑

**난이도**: ⭐⭐
**예상 시간**: 2.5h
**산출물 폴더**: `04-TTS-Audio/`
**목표 상태**: ⏳ 대기

#### 학습 목표
- [ ] Python TTS 생성 스크립트를 활용해 슬라이드별 나레이션 음성 파일(Qwen-TTS 또는 Edge-TTS 고품질 성우)을 획득한다.
- [ ] 나레이션의 시작과 끝이 씹히는 것을 방지하기 위해 **오디오 전후방 딜레이 패딩 연산 공식(HEAD_PAD 0.1s + TAIL_PAD 0.12s)**을 디버깅 및 보정한다.
- [ ] 각 슬라이드의 실제 오디오 재생 길이를 정확히 밀리초 단위로 추출하여 `durations` 테이블을 생성하고, Remotion 타임라인에 완벽히 매핑한다.

#### 주요 개념
1. **Audio Padding Padding Formula**: TTS 음성 생성 직후 자막 렌더 타임과의 싱크 정합을 위해 전방 헤더와 후방 트레일러에 0.1초 수준의 미세 딜레이 무음 패딩을 인위 주입하는 기법.
2. **Narration-Driven Timeline Calibration**: 전체 비디오 듀레이션(프레임 수)을 사전에 하드코딩하지 않고, 생성된 오디오 길이 데이터를 합산하여 동적으로 전체 비디오 길이를 선언하는 연산.

#### 실습 과제

**실습 1: 고품질 나레이션 오디오 자동 생성 및 패딩** ⭐⭐
- **목적**: 자연스러운 끊어 읽기와 딜레이가 보정된 오디오 파일셋 확보.
- **단계**:
  1. `02-Remotion-Setup/video-slide-plan.md`에서 작성한 나레이션 원고를 TTS 입력용 한글 보정 텍스트로 정제한다.
  2. Python 스크립트를 실행하여 슬라이드 0번부터 9번까지의 개별 `.mp3` 또는 `.wav` 오디오 파일들을 순차 생성한다.
  3. FFmpeg 또는 Python 오디오 라이브러리를 통해 오디오 전방 0.1초, 후방 0.12초의 무음 영역을 덧붙이는 전처리를 가한다.
- **검증**: 생성된 오디오 재생 시 첫 음절과 마지막 음절이 깨끗하게 재생되는지 청음 테스트 통과.

**실습 2: 오디오 듀레이션 추출 및 Remotion 동적 타임라인 매핑** ⭐⭐
- **목적**: 자막 및 슬라이드 프레임과 오디오의 100% 싱크 보증.
- **단계**:
  1. 완성된 10개 오디오 파일의 재생 시간(초)을 정밀 추출한다.
  2. 추출된 시간 데이터를 기반으로 각 슬라이드의 프레임 수(FPS 30 기준, 재생시간 * 30)를 계산하여 `durations.json` 파일로 저장한다.
  3. Remotion 프로젝트의 `data.ts`가 이 `durations.json` 데이터를 동적으로 불러와 각 슬라이드의 `<Sequence>` 길이를 정밀 통제하게 바인딩한다.
- **검증**: `durations.json` 파일이 정상 출력되고, Remotion Preview 창에서 슬라이드가 오디오가 끝남과 동시에 다음 슬라이드로 지연 없이 매끄럽게 넘어가는지 검증.

#### 산출물
```
04-TTS-Audio/
├── README.md               ← M4 오디오 빌드 가이드
├── gen_audio_qwen.py       ← 오디오 생성 및 패딩 Python 스크립트 백업
├── durations.json          ← 각 슬라이드별 오디오 재생 시간 및 프레임 수 매핑 테이블
└── audios/                 ← 생성 완료된 슬라이드별 고품질 성우 MP3 파일 세트
```

#### Definition of Done (M4)
- [ ] 10개 슬라이드 전체의 나레이션 오디오가 누락 없이 깨끗하게 생성됨.
- [ ] 오디오 전후방 무음 패딩이 적용되어 첫 발음 씹힘이나 슬라이드 전환 시 끝말 끊김 현상이 발생하지 않음.
- [ ] `durations.json` 명세 파일이 오류 없이 출력되고 Remotion 타임 바인딩 코드가 성공적으로 작동함.

---

### M5 - 최종 고화질 MP4 렌더링 및 시민 배포 패키지 마감

**난이도**: ⭐⭐
**예상 시간**: 2.5h
**산출물 폴더**: `05-Final-Delivery/`
**목표 상태**: ⏳ 대기

#### 학습 목표
- [ ] Remotion CLI를 사용하여 빌드 오류 없이 FHD(1080p, 30fps) 해상도의 무결한 최종 MP4 비디오를 렌더링한다.
- [ ] **시민단체(NGO)가 이 영상을 즉시 채널(YouTube, Slack, Gobi, LinkedIn 등)에 배포할 수 있도록, 전문 교육 가이드 및 안전망 자원 링크가 포함된 고밀도 배포용 SNS 홍보 포스트 스크립트(`promo_text.md`)**를 작성한다.
- [ ] 학습 과정을 회고하고 산출물을 다음 학습자를 위해 정리하는 Topic Retrospective를 집필하여 VibeLearn AI 대장정을 마감한다.

#### 주요 개념
1. **Lossless Rendering Optimization**: 비디오 코덱(h264) 및 프레임 레이트 매칭을 최적화하여 인포그래픽 텍스트 가독성을 최상으로 유지하는 렌더링 세팅.
2. **Public-Safety NGO Campaign Delivery**: 정보 획득 장벽이 높은 비영리단체 및 자원봉사자 그룹에 실무적인 안전 유틸리티 및 교육 참여 기회를 전파하기 위한 고품질 포스트 패키징.

#### 실습 과제

**실습 1: Remotion CLI 활용 무결점 FHD 렌더링** ⭐⭐
- **목적**: 빌드 깨짐 없는 완성본 MP4 비디오 획득.
- **단계**:
  1. `npx remotion render active-shooter-0908 output.mp4` 명령을 가동하여 렌더링 연산을 수행한다.
  2. 렌더링 중 발생하는 듀레이션 불일치, 캔버스 비율 경고, 폰트 깨짐 경고 등을 해결하고 무결점 빌드를 통과시킨다.
- **검증**: `C:\AI_study\2026\Changsoo_Vault\outputs\active-shooter-0908.mp4` 경로에 깨끗한 비디오 파일 확보.

**실습 2: NGO 배포 패키지 및 SNS 프로모션 글 작성** ⭐⭐
- **목적**: 시민단체 실무진의 주의를 환기하고 참여를 독려하는 고품질 마케팅 포스트 작성.
- **단계**:
  1. 제작된 비디오의 다운로드 경로와 함께, FEMA IS-907.A 수강 링크, Stop the Bleed 참여 지침, 비상 계획 수립 지원 도구(CISA) 소개 등을 가독성 높게 아우르는 배포 문안을 작성한다.
  2. 문안은 정중하고 신뢰감을 주는 어조로 집필하며, 자원봉사자 수칙을 요약해 본문에 투영한다.
- **검증**: `05-Final-Delivery/promo_text.md`에 플랫폼별(Facebook, Gobi Space, LinkedIn) 배포 멘트 포맷이 정밀 구축됨.

#### 산출물
```
05-Final-Delivery/
├── README.md               ← M5 렌더링 및 배포 가이드
├── active-shooter-0908.mp4 ← 렌더 완료된 최종 FHD 공익 교육 영상 (outputs/에 실물 배치 후 가상 링크)
└── promo_text.md           ← FEMA/NGO 안전 자원 링크가 가미된 홍보용 SNS 문안 패키지
```

#### Definition of Done (M5)
- [ ] 최종 렌더링 성공 및 `output.mp4` 파일의 프레임 저하(Lag), 오디오 밀림, 자막 씹힘이 전혀 없음.
- [ ] `promo_text.md` 내에 FEMA, ALERRT, Stop the Bleed 등 NGO용 외부 교육 링크가 명확히 기재되어 배포 준비가 끝남.
- [ ] 전체 VibeLearn AI Topic Retrospective 작성이 완료됨.

---

## 📝 WorkLog 작성 가이드

각 학습 세션마다 WorkLog를 작성하여 진행 상황을 추적합니다.

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_{Topic}.md`
- 예: `vl_worklog/20260908_M2_active-shooter-response.md`

**WorkLog 필수 섹션**:
1. 오늘의 학습 목표 (체크리스트)
2. 진행 내용 (실습별 상세 기록, 코드 블록 및 텍스트 증적 확보)
3. 문제 해결 로그 (Troubleshooting 기록)
4. DoD 체크리스트 (모듈 완료 기준 만족 여부)
5. Daily Retrospective (What went well, What could be improved, Insights, Tomorrow's focus)
6. 참조 및 산출물 경로

---

## 🔍 Retrospective 가이드

### Daily Retrospective (매일, 5-10분)
WorkLog 내의 하단에 작성:
- **What went well?**: 오늘 학습/구현에서 원활하게 진행된 점, 성취한 점.
- **What could be improved?**: 겪은 어려움이나 효율화할 수 있었던 점.
- **Insights**: 오늘 배운 본질적인 배움이나 통찰력.
- **Tomorrow's focus**: 내일의 주요 학습 마일스톤 및 계획.

### Module Retrospective (모듈 완료 시, 15-20분)
`vl_worklog/YYYYMMDD_MX_Retrospective.md`:
- 계획 대비 실제 시간 및 구현 범위 비교
- 모듈에서 획득한 핵심 지식 요약
- 발생한 문제 해결 사례 공유
- 다음 모듈로 넘어가기 위한 준비 확인

### Topic Retrospective (전체 완료 시, 30-60분)
`vl_worklog/YYYYMMDD_{Topic}_Final_Retrospective.md`:
- 전체 1주간의 대장정 통계 (총 소요 시간, 산출물 수)
- 시민단체 역량 강화 및 공익 배포물로서의 산출물 가치 평가
- 학습 중 AI 가이드와 본인의 상호작용 프로세스 개선점 도출

---

## 📂 전체 폴더 구조

```
active-shooter-response/
├── topic_starter.md              # Topic 기본 계획서 (NGO 가이드 확장 완료)
├── vl_prompts/
│   ├── roadmap_prompt.md         # 로드맵 생성 가이드 프롬프트 (v2.1)
│   └── daily_learning_prompt.md  # 일일 학습 구동 프롬프트
├── vl_roadmap/
│   └── 20260908_RoadMap_active-shooter-response.md  # [본 파일]
├── vl_worklog/
│   ├── 20260907_M1_active-shooter-response.md       # M1 학습 완료 일지 (DHS)
│   ├── 20260908_M2_active-shooter-response.md       # M2 예정 일지
│   └── ...
├── vl_materials/                 # 학습 원본 PDF 및 참고 리소스 배치 폴더
│   ├── 미 국토안보부(DHS) 자료-총기난사 발생 시 대응요령(국문).pdf
│   └── U.S. DHS-Active Shooter_How to Respond (English).pdf
├── 01-DHS-Analysis/              # M1 산출물 폴더 (Run-Hide-Fight + NGO 자원 지도)
│   ├── README.md
│   ├── webinar_digest.md
│   └── active_shooter_guide.md
├── 02-Remotion-Setup/            # M2 산출물 폴더 (DHS + NGO 교육 매핑 슬라이드 설계)
│   ├── README.md
│   ├── video-slide-plan.md
│   ├── image-prompts.md
│   └── data.ts
└── ... (03 ~ 05 순차적 생성 예정)
```

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| **M1** | 2026-09-08 | 2026-09-08 | ✅ 완료 | 100% | 시민단체 교육 및 안전망 자원 수록 M1 보강 재완수 |
| **M2** | 2026-09-08 | 2026-09-08 | ✅ 완료 | 100% | NGO 비상대응 자원이 반영된 비디오 슬라이드 기획 M2 완수 |
| **M3** | 2026-09-08 | | 🔄 진행 중 | 0% | Remotion React 컴포넌트 개발 및 모션 구현 착수 |
| **M4** | | | ⏳ 대기 | 0% | |
| **M5** | | | ⏳ 대기 | 0% | |

**범례**:
- ⏳ 대기
- 🔄 진행 중
- ✅ 완료

---

## 🎯 성공 기준

전체 Topic 완료 기준:
- [ ] 모든 5개 모듈 완료 (DoD 100%)
- [ ] 총 5개의 정교한 산출물 폴더 생성 및 고품질 README 구축
- [ ] Topic Final Retrospective 작성 완료
- [ ] FEMA 공식 및 Stop the Bleed 캠페인 연계가 완벽히 완료된 FHD 비디오 파일 확보
- [ ] 시민단체 즉각 배포용 홍보 포스트 문안 확보

---

**생성자**: Gemini with VibeLearn AI
**Roadmap 버전**: 2.1 (NGO 특화 개정판)
**방법론 버전**: VibeLearn AI 2.0
