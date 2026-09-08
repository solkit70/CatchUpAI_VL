# VibeLearn AI Roadmap 생성 프롬프트 - active-shooter-response

**버전**: 2.1
**생성일**: 2026-09-08
**방법론**: VibeLearn AI

---

## 📌 사용 방법

이 프롬프트는 `topic_starter.md`에서 입력한 Topic 정보를 바탕으로 학습 로드맵을 자동 생성합니다.

---

## [1단계] Topic 정보 (자동 주입 완료)

### 기본 정보

**Topic 이름**: `active-shooter-response`

**Topic 설명**:
```
총기난사 사건 발생 시 일반 시민이 생명을 지키기 위한 대처 요령(DHS 자료 및 개인 교육 경험 기반)을 교육하고, 이를 효과적으로 알릴 수 있는 Remotion AI 기반 영상을 기획/제작하는 학습 과정.
```

**학습 목적**:
```
- 미 국토안보부(DHS) 및 교육 자료의 핵심 행동 지침(Run, Hide, Fight 및 경찰 대응)을 체계적으로 정리하고 학습한다.   
- 시민단체(NGO) 실무진 및 자원봉사자들을 위해 실제 온/오프라인 전문 교육(FEMA IS-907.A, CRASE, ALICE)을 수강하는 방법과 이수 경로를 가이드한다.
- 단체 및 종교 시설 등의 비상 대처 역량을 높이기 위한 비상대응계획(EAP) 가이드라인, CISA Tabletop 시뮬레이션, 지혈법(Stop the Bleed) 등 도움이 될 만한 연계 안전 자원 정보를 취합하고 체계화한다.
- 정리된 내용을 효과적으로 시각화하고 전달하기 위한 Remotion 동영상 발표용 슬라이드 플랜 및 나레이션 스크립트를 설계한다.
- React, TypeScript, Remotion 프레임워크 및 TTS 기술을 활용하여 자막과 음성이 싱크된 완성도 높은 교육 영상을 제작한다.
- 시민 단체 및 소외 계층에 도움이 될 수 있는 공익적 목적의 배포 자료를 구성한다.
```

**예상 학습 기간**: `1주 (총 12~15시간)`

---

### 환경 및 사전 지식

**운영 체제**: `Windows`

**주요 도구 및 기술 스택**:
```
- Remotion 4.0
- React, TypeScript
- Node.js (v18+)
- Python (edge-tts 및 Qwen-TTS 생성)
- FFmpeg
```

**사전 지식**:
```
필수:
- 마크다운 기본 작성법 및 구조적 글쓰기
- 기본적인 React 컴포넌트 구조 이해

권장:
- TypeScript 기본 타이핑 개념
- FFmpeg CLI 기본 사용법
```

---

### 산출물 및 참조

**학습 목표**:
```
- [ ] 총기난사 발생 시 3대 핵심 대응 수칙(Run, Hide, Fight)과 대처 흐름을 말로 명확히 설명할 수 있다.
- [ ] FEMA IS-907.A, CRASE, ALICE 등 시민단체 및 일반인이 이수할 수 있는 무료/유료 온·오프라인 실무자 교육 과정의 특징과 참여 경로를 가이드할 수 있다.
- [ ] 시민단체 비상행동계획(EAP) 가이드라인, CISA 시뮬레이션 키트, 지혈법(Stop the Bleed) 등 NGO 단체 안전망 구축에 도움되는 핵심 안전 자원을 매핑할 수 있다.
- [ ] Remotion용 슬라이드 플랜(`video-slide-plan.md`) 및 지루하지 않은 감정 마커 나레이션 스크립트를 작성할 수 있다.
- [ ] Remotion 동적 효과(Spring, Stagger, Motion Blur 등)와 다양한 슬라이드 타입을 적용해 UI 컴포넌트를 설계할 수 있다.
- [ ] TTS 스크립트(`gen_audio.py` 및 `gen_audio_qwen.py`)를 활용해 완벽하게 패딩이 적용된 한국어 음성을 생성할 수 있다.
- [ ] 비디오 렌더링을 성공적으로 완료하여 시민 단체 등 필요한 곳에 바로 전파할 수 있는 최종 MP4 영상을 확보한다.    
```

**참조 자료**:
```
- 미 국토안보부(DHS) 자료-총기난사 발생 시 대응요령(국문).pdf
- U.S. DHS-Active Shooter_How to Respond (English).pdf
- FEMA IS-907.A (Active Shooter: What You Can Do): FEMA Independent Study
- ALERRT CRASE Course (Avoid, Deny, Defend Model): https://alerrt.org/
- Navigate360 ALICE Training: https://www.alicelearning.com/
- DHS Stop the Bleed: https://www.stopthebleed.org/
- CISA Emergency Planning: https://www.cisa.gov/active-shooter-preparedness
- Remotion 공식 문서: https://www.remotion.dev/
- Remotion Video Skill 지침: `_Settings_/Skills/remotion-video/SKILL.md`
- Remotion Effects Library: `_Settings_/Skills/remotion-video/effects-library.md`
```

**vl_materials/ 폴더**:
```
vl_materials/ 폴더 안에 국문/영문 미 국토안보부(DHS) PDF 가이드를 배치하여 분석 및 요약 자료로 활용합니다.
```

---

## [2단계] AI에게 요청할 작업

위 주입된 Topic 정보를 바탕으로 **VibeLearn AI 방법론**에 맞는 학습 로드맵을 생성해주세요.

---

### 🔍 STEP 1: 학습 기간 적정성 검토 (필수)

**로드맵 생성 전 반드시 수행:**

사용자가 입력한 학습 기간 `1주 (총 12~15시간)`이 해당 Topic에 적절한지 분석하고 피드백을 제공하세요.

*(이미 2026-09-07 검증 단계를 완료하였으며, 시민단체 가이드 및 추가 트레이닝 정보 보강 내용이 포함되어 1주 일정을 더욱 밀도 있게 설계하는 것이 적정함이 승인되었습니다. 분석 결과를 요약하여 로드맵에 바로 반영하고 생성을 진행합니다.)*

---

### 🗺️ STEP 2: 로드맵 생성 요구사항

사용자가 기간을 최종 확정한 후 아래 요구사항에 따라 로드맵을 생성하세요.

#### 전체 구조

**학습 기간**: `1주 (총 5개 모듈)`로 세분화
- M1: 안전 지침 분석 및 NGO 유관 교육/자원 분석 (이론/기획 20%) -> 2026-09-07 완료!
- M2: NGO 비상대응 자원이 반영된 Remotion 비디오 슬라이드 및 씬 기획 (실습 80%)
- M3: Remotion 컴포넌트 개발 및 동적 연출 (실습 80%)
- M4: TTS 초벌/최종 음성 생성 및 오디오 싱크 매핑 (실습 80%)
- M5: MP4 최종 렌더링 및 시민단체 전파 배포 자료 준비 (프로젝트 완성)

**모듈 구성 원칙**:
- 첫 모듈은 기존 자료(DHS 국문/영문 PDF) 분석 및 NGO용 대처 전문 교육 프로그램(FEMA, CRASE, ALICE), 핵심 비상 안전 자원(Stop the Bleed, CISA Tabletop, EAP) 요약 정리. (M1) -> 완료 상태 기록!
- M2는 Remotion 슬라이드 계획(`video-slide-plan.md`)에 "Run, Hide, Fight" 수칙뿐 아니라 **"어떻게 실제 교육을 이수할 수 있는지"** 및 **"시민단체를 위한 추가 안전 연계 자원"**을 시각적으로 어떻게 가이드 비디오에 매핑할지 상세 슬라이드로 기획함.
- 마지막 모듈은 최종 렌더링 검증 및 배포용 SNS 홍보 멘트/런다운 세트 준비.

---

#### 각 모듈 필수 포함 항목

각 모듈은 다음 9가지 항목을 반드시 포함해야 합니다:

##### 1. 모듈 기본 정보
##### 2. 학습 목표 (3-5개, 검증 가능하게)
##### 3. 주요 개념 (이론 20-30%)
##### 4. 실습 과제 (실습 70-80%, 단계별)
##### 5. 산출물 (폴더 구조 포함)
##### 6. Definition of Done (DoD) 체크리스트
##### 7. Self-Assessment (자기 평가)
##### 8. 예상 시간 배분 (버퍼 20% 포함)
##### 9. 참조 자료

---

## [3단계] 출력 형식

다음 Markdown 형식으로 로드맵을 생성하고 `vl_roadmap/20260908_RoadMap_active-shooter-response.md`에 저장하세요.     

*(상세 Markdown 템플릿 구조는 `templates/roadmap_prompt_template.md` 표준을 따름)*
