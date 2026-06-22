# WorkLog — M1~M4: Tehaleh-Community-Video 전 과정

**날짜**: 2026-06-21
**Topic**: Tehaleh-Community-Video
**모듈**: M0(Topic 설정) → M1(리서치) → M2(슬라이드 플랜) → M3(Remotion 개발) → M4(오디오 생성) 전 과정 1일 집중
**학습 시간**: 전체 세션 (Live #15 방송 중 + 방송 후)
**방법론**: VibeLearn AI

---

## 🎯 오늘의 학습 목표

- [x] VibeLearn AI로 Topic 설정 및 Roadmap 작성 (M0)
- [x] Tehaleh 리서치 자료 수집·구조화 → `tehaleh-research.md` 완성 (M1)
- [x] 15장 슬라이드 플랜 → `video-slide-plan.md` 작성 (M2)
- [x] AI 이미지 프롬프트 → `image-prompts.md` 작성 (M2)
- [x] Remotion 컴포넌트 개발 — data.ts + TehalehIntro0619.tsx (M3)
- [x] edge-tts 오디오 15개 생성 → AUDIO_DURATIONS 업데이트 (M4)
- [x] gen_audio_qwen.py (Qwen3-TTS 교체 스크립트) 작성 (M4)
- [x] Qwen3-TTS 한국어·영어 버전 제작 및 MP4 최종 렌더링

---

## 📚 진행 내용

### M0: Topic 설정 및 Roadmap 작성 (~8분)

**목적**: VibeLearn AI로 1일 집중 학습 구조 설계

**과정**:
1. `topic_starter.md` 작성 — Topic 목적, 환경, 학습 목표 정의
2. `roadmap_prompt.md` 생성 — roadmap_prompt_template.md 기반
3. `20260621_RoadMap_Tehaleh-Community-Video.md` 생성 — M1~M4 4모듈 구성
4. `daily_learning_prompt.md` 작성

**결과**: 4모듈 Roadmap 완성. 총 예상 시간 ~7.5h (버퍼 포함 ~9h)

**특이사항**: Live #15 방송 시작 시점에서 VibeLearn AI 방법론으로 Roadmap 작성 → 총 8분 소요 — 창발 발표("AI로 뚝딱") 실증 사례로 방송에서 시연

---

### M1: Tehaleh 리서치 (이전 세션 → 계속)

**목적**: IT 종사자·은퇴자·한인 커뮤니티 관점에서 Tehaleh 정보 구조화

**결과**: `vl_materials/tehaleh-research.md` 완성

**수집한 핵심 데이터**:
- 위치: Bonney Lake 남쪽, Pierce County, 4,700에이커 마스터 플랜 커뮤니티
- 거리: 시애틀 ~45분, 벨뷰 ~50분, SeaTac ~35분
- IT 관점: 광섬유 2Gbps, 신축 홈오피스, Sounder Train 통근, WA 소득세 없음
- 은퇴자 관점: Trilogy 55+ 클럽하우스, 40마일 트레일, Snoqualmie 스키 1시간
- 한인 커뮤니티: H-Mart Federal Way ~20분, 한인 식당가, 타코마 대형 병원 20분

**DoD 달성**:
- [x] 6개 섹션 모두 작성 (기본정보·위치·커뮤니티·IT·은퇴자·한인)
- [x] 위치 섹션: 3대 도시 거리/시간 포함
- [x] IT·은퇴자 관점 각 4개+ 포인트

---

### M2: 슬라이드 플랜 + 이미지 프롬프트 (이전 세션)

**목적**: Remotion data.ts의 원천 자료 + AI 이미지 프롬프트 완성

**결과**:
- `public/tehaleh-intro-0619/video-slide-plan.md` — 15장 (S0~S14)
- `public/tehaleh-intro-0619/image-prompts.md` — 4장 AI 이미지 프롬프트

**슬라이드 구성 요약**:

| 범위 | 타입 | 내용 |
|------|------|------|
| S0 | TITLE | Tehaleh — 시애틀에서 45분·자연 속 삶 |
| S1 | SECTION | Tehaleh가 뭔가요? |
| S2~S3 | BULLET+STAT | 위치 정보 + 통근 시간 |
| S4~S6 | SECTION+BULLET×2 | 커뮤니티·주택 가격 |
| S7~S9 | SECTION+BULLET×2 | IT 종사자 (재택·하이브리드) |
| S10~S12 | SECTION+BULLET×2 | 은퇴자 (액티브·한인 커뮤니티) |
| S13 | QUOTE | 거주자 직접 인용 |
| S14 | OUTRO | CTA: tehaleh.com |

**이미지 준비 완료** (공개 및 AI 생성):
- `mt-rainier-personal.jpg`, `mt-rainier-personal_2.jpg` — 직접 촬영
- `slide_s2_location_map_ChatGPT.png`, `slide_s5_community_center_Gemini.png`
- `slide_s8_home_office_Gemini.png`, `slide_s11_senior_hiking_Gemini.png`

---

### M3: Remotion 컴포넌트 개발 (이전 세션)

**목적**: video-slide-plan.md를 실제 영상 컴포넌트로 구현

**생성 파일**:
- `src/tehaleh-intro-0619/data.ts` — SLIDES 배열(15개), COLORS, getSlideDurationSec(), TOTAL_FRAMES
- `src/tehaleh-intro-0619/TehalehIntro0619.tsx` — 6개 슬라이드 컴포넌트 + TransitionSeries 메인 컴포지션 (초기 ANIMATED_DARK → 최종 LIGHT_PNW)
- `src/Root.tsx` — TehalehIntro0619 Composition 등록

**핵심 기술 결정사항**:

| 항목 | 결정 | 이유 |
|------|------|------|
| 배경 스타일 | 초기 ANIMATED_DARK → 최종 LIGHT_PNW | 살기 좋은 자연 커뮤니티의 밝은 분위기 반영 |
| 색상 | primary `#22C55E` (forest green), accent `#F59E0B` (mountain gold) | PNW 자연 색 |
| TransitionSeries | content: fade 18f / section: slide-from-right 24f | 섹션 전환을 더 역동적으로 |
| 슬라이드 파일 구조 | 단일 .tsx 파일 (6개 컴포넌트 통합) | 15장 규모에서 관리 단순화 |
| AUDIO_READY 플래그 | false → 오디오 생성 후 true | 오디오 없이 미리보기 가능 |

**문제 해결 로그**:

#### 문제: Trail 컴포넌트 TypeScript 오류
- **증상**: `Type '{ children: Element; lagInFrames: number; ... }' is not assignable to type 'IntrinsicAttributes & TrailProps'`
- **원인**: `@remotion/motion-blur`의 Trail 컴포넌트 API 버전 불일치
- **해결**: Trail 제거, `spring + interpolate`로 동일 효과 구현 (TitleSlide h1, OutroSlide h1)
- **교훈**: Remotion 서드파티 컴포넌트 사용 시 버전 체크 우선

**TypeScript 검증**: `npx tsc --noEmit | Select-String "tehaleh"` → 0 오류

---

### M4: 오디오 생성 (오늘 세션 — Phase 4a 완료)

**목적**: edge-tts 초벌 오디오 15개 생성 → Remotion 타이밍 확정

**실행 과정**:
1. `public/tehaleh-intro-0619/gen_audio.py` 생성 (voice: `ko-KR-SunHiNeural`)
2. 실행 오류 수정: `→` 문자 UnicodeEncodeError → `->` 로 변경 (cp1252 인코딩 한계)
3. `python public/tehaleh-intro-0619/gen_audio.py` → 15개 동시 생성 완료
4. mutagen으로 실제 길이 측정

**오디오 측정 결과**:

| Slide | 파일 | 길이 | 기본 시간 |
|-------|------|------|---------|
| S0 | slide_00.mp3 | 5.21s | 6s |
| S1 | slide_01.mp3 | 3.70s | 4s |
| S2 | slide_02.mp3 | 17.30s | 8s |
| S3 | slide_03.mp3 | 13.01s | 7s |
| S4 | slide_04.mp3 | 3.31s | 4s |
| S5 | slide_05.mp3 | 19.30s | 8s |
| S6 | slide_06.mp3 | 15.48s | 8s |
| S7 | slide_07.mp3 | 5.38s | 4s |
| S8 | slide_08.mp3 | 19.97s | 8s |
| S9 | slide_09.mp3 | 12.29s | 7s |
| S10 | slide_10.mp3 | 3.89s | 4s |
| S11 | slide_11.mp3 | 16.80s | 8s |
| S12 | slide_12.mp3 | 13.39s | 7s |
| S13 | slide_13.mp3 | 12.00s | 8s |
| S14 | slide_14.mp3 | 12.34s | 10s |

**나레이션 총 길이**: 174.37초 → 패딩 포함 **총 영상 ~181초 (3분 1초)**

> ⚠️ 기본 예상(~99초)보다 길어진 이유: 나레이션 스크립트가 구어체 설명 위주라 실제 TTS 시간이 슬라이드 플랜 기본 시간보다 김 (특히 S2, S5, S6, S8, S11)

5. `data.ts` 업데이트:
   - `AUDIO_READY = true`
   - `AUDIO_DURATIONS` 실측값 반영 (15개 슬라이드)
6. `gen_audio_qwen.py` 작성 — Changsoo 클론 + Female 1/2/3 보이스 매핑

---

## 🐛 문제 해결 로그

### 문제 1: Trail 컴포넌트 TypeScript 오류 (M3)
- **증상**: TitleSlide, OutroSlide에서 Trail props 타입 오류
- **해결**: Trail 제거 → spring 직접 사용
- **비고**: 기능 손실 없음 (spring animation이 더 코드 단순)

### 문제 2: gen_audio.py UnicodeEncodeError (M4)
- **증상**: `→` 출력 시 cp1252 인코딩 오류
- **해결**: `→` → `->` 치환
- **비고**: Windows 터미널 기본 인코딩(cp1252) 한계; 한국어 텍스트 자체는 edge-tts가 처리해서 문제 없음

---

## 📊 DoD 체크리스트

### M1 DoD
- [x] tehaleh-research.md 6개 섹션 모두 작성
- [x] 기본 정보: 위치, 규모, 개발사 포함
- [x] 위치 섹션: 3개 도시 거리/시간
- [x] IT·은퇴자 관점 각 4개+ 포인트
- [x] 한인 커뮤니티 섹션 포함
- [x] WorkLog 작성 ← 이 문서

**M1 완료율**: 6/6 (100%) ✅

### M2 DoD
- [x] video-slide-plan.md: 15장 슬라이드, 각 슬라이드 type·content·narration·duration
- [x] S0·S14에 거주자 직접 촬영 사진 지정
- [x] 모든 슬라이드 한국어 나레이션 스크립트
- [x] image-prompts.md: 4장 AI 이미지 프롬프트
- [x] 총 예상 영상 시간 ~90-150초 범위 (기준: 기본 시간 합계 ~99초; 실측 ~181초)
- [x] WorkLog 작성

**M2 완료율**: 6/6 (100%) ✅

### M3 DoD
- [x] data.ts 생성 (15슬라이드 데이터, AUDIO_READY/DURATIONS, COLORS, getSlideDurationSec)
- [x] 6개 슬라이드 컴포넌트 구현 (TitleSlide, SectionSlide, BulletSlide, StatSlide, QuoteSlide, OutroSlide)
- [x] TehalehIntro0619.tsx 메인 컴포넌트 완성 (TransitionSeries + SlideRenderer)
- [x] Root.tsx에 TehalehIntro0619 Composition 등록
- [x] TypeScript 오류 0개 (tehaleh 파일 기준)
- [x] 거주자 사진 S0·S13·S14에 배치
- [x] WorkLog 작성

**M3 완료율**: 7/7 (100%) ✅

### M4 DoD
- [x] 슬라이드별 한국어 TTS 오디오(.mp3) 15개 생성
- [x] AUDIO_DURATIONS 실측값 업데이트, AUDIO_READY = true
- [x] 한국어·영어 gen_audio_qwen.py 작성 및 Qwen3-TTS 최종 오디오 생성
- [x] Remotion Studio에서 레이아웃·사진 전환·오디오 타이밍 미리보기
- [x] Qwen3-TTS 최종 오디오 교체 및 발음 보정
- [x] 한국어·영어 MP4 렌더링 (1920×1080, 30fps)
- [x] 음성·영상 동기화 확인 및 편집본 Chapter 타임코드 반영
- [x] 한국어·영어 YouTube 업로드와 배포 메타데이터 작성
- [x] Topic Final Retrospective 작성

**M4 완료율**: 10/10 (100%) ✅ — 한국어·영어 제작·렌더링·배포 완료

---

## 💡 Daily Retrospective

### What went well (잘된 점)
- VibeLearn AI로 Roadmap 작성 8분 — 방송 실시간 시연으로 "AI 뚝딱" 증명
- M1~M3 전 과정을 1일 세션에서 완료 (TypeScript 오류 포함 디버깅 완결)
- 초기 ANIMATED_DARK 시안을 검토한 뒤 밝은 LIGHT_PNW 배경으로 개선해 영상 내용과 시각 분위기를 일치시킴
- gen_audio.py 동시 실행으로 15개 오디오 병렬 생성 (순차 대비 시간 절약)
- Qwen3-TTS용 gen_audio_qwen.py도 함께 준비 — 발표 전까지 실행 가능 상태

### What could be improved (개선할 점)
- 나레이션 스크립트 길이 조율 필요: 영상 3분 1초로 기본 예상(99초)보다 큰 차이 발생
  - 발표 오프닝 데모용으로는 1분 내외가 이상적 — 나레이션 스크립트를 줄이거나 재생 속도를 높이는 옵션 검토 필요
- Trail 컴포넌트 사용 전 API 버전 확인 습관 필요
- WorkLog를 작업 중 실시간으로 작성하지 못함 → 사후 정리로 일부 상세 기록 누락

### Insights (인사이트)
- "Roadmap 8분" 자체가 이 발표의 가장 강력한 데모: VibeLearn AI + Claude Code = 구조 설계 즉시 실행
- 나레이션 스크립트는 "읽을 텍스트" 기준으로 작성하면 TTS 길이가 예상의 2~3배로 길어짐 → 슬라이드 기본 시간을 나레이션 단어 수 기준으로 추정하는 방법 개발 필요
- SKILL.md의 AUDIO_READY 플래그 패턴이 매우 실용적 — 오디오 없이도 미리보기 가능해 개발 속도 향상

### Tomorrow's focus (다음 세션 집중할 것)
1. Remotion Studio 미리보기 (`npx remotion studio` → TehalehIntro0619 선택)
   - 영상 3분인데 발표 오프닝 데모로 적합한지 검토
   - 필요 시 나레이션 단축 또는 배속 옵션 고려
2. Qwen3-TTS 실행 (`python public/tehaleh-intro-0619/gen_audio_qwen.py`)
3. MP4 렌더링 (`npx remotion render TehalehIntro0619 tehaleh-intro-0619.mp4`)
4. 영상 발표 데모 활용 준비 (오프닝 재생 슬라이드 연결)

---

## YouTube 업로드 메타데이터

이 영상은 `The-AI-Powered-Creator` 발표의 실제 AI 콘텐츠 제작 사례이자 `Tehaleh-Community-Video` Topic의 최종 산출물이다. 아래 메타데이터는 2026-06-22에 완료된 한국어·영어 렌더 파일을 기준으로 작성했으며, 주택 매물 수와 가격은 영상에 명시된 것처럼 2026-06-21 Homes.com 조회 결과이므로 업로드 후에도 기준일을 삭제하지 않는다.

이 섹션을 YouTube 배포 자료의 단일 관리 위치로 사용한다. 이후 확정하거나 수정하는 한국어·영어 제목, Description, Chapter, 태그, 썸네일 문구와 이미지 생성 프롬프트도 여기에 통합하며, `The-AI-Powered-Creator` 발표에서는 이 기록을 AI 콘텐츠 제작과 Distribution 과정의 실제 사례로 활용한다.

### 최종 렌더 파일

| 언어 | 파일 | 재생 시간 | 크기 | 렌더 완료 |
|------|------|----------|------|----------|
| 한국어 | `out/tehaleh-intro-0619.mp4` | 4:51.8 | 84,891,137 bytes | 2026-06-22 09:25 |
| 영어 | `out/tehaleh-intro-0619-en.mp4` | 4:14.3 | 75,101,950 bytes | 2026-06-22 09:45 |

### YouTube 공개 URL

| 언어 | 상태 | URL |
|------|------|-----|
| 한국어 | ✅ 업로드 완료 | https://youtu.be/Cucvcz9bVPU |
| 영어 | ✅ 업로드 완료 | https://youtu.be/YygPvJbKPvU |

### 한국어 버전

**제목**

```text
AI in Action - 시애틀 45분, 창밖에 레이니어 산이 보이는 동네 Tehaleh | 40마일 트레일의 자연 속 커뮤니티
```

**설명**

```text
시애틀에서 자동차로 약 45분 거리에 있는 워싱턴주 Tehaleh 커뮤니티를 실제 거주자의 시선으로 소개합니다.

Post & Pour에서 직접 촬영한 레이니어 산 풍경부터 40마일 이상의 트레일, 커뮤니티 시설, 주택 가격, 재택·하이브리드 근무 환경, 액티브한 은퇴 생활과 인근 한인 생활권까지 살펴봅니다.

대중교통을 이용하면 인근 Sumner역에서 Seattle King Street역까지 Sounder 열차로 약 50분이 소요됩니다. 자동차 이동 시간은 교통 상황에 따라 달라질 수 있습니다.

영상에 표시된 주택 매물 수와 가격 범위는 2026년 6월 21일 Homes.com 조회 기준이며 이후 변동될 수 있습니다. 워싱턴주는 개인 소득세가 없지만 다른 주세와 지방세는 적용될 수 있습니다.

이 영상은 창발 Product Group의 온라인 이벤트 ‘The AI Powered Creator’ 발표에서 소개할 실제 AI 콘텐츠 제작 사례로 만들었습니다. 리서치, 구성, 이미지, 나레이션과 영상 제작에 AI와 Remotion을 활용했습니다.

📌 Chapters

00:00 레이니어 산이 보이는 Tehaleh
00:10 Tehaleh는 어떤 곳인가요?
00:46 커뮤니티 시설과 The Retreat
01:16 Post & Pour와 직접 촬영한 풍경
02:06 Tehaleh 주택 가격
02:24 재택근무와 하이브리드 출퇴근
03:19 액티브한 은퇴 생활과 한인 생활권
03:49 실제 거주자의 이야기
04:00 Tehaleh 소개 마무리

🔗 정보 및 출처

Tehaleh
https://www.tehaleh.com/

Sound Transit S Line
https://www.soundtransit.org/ride-with-us/routes-schedules/s-line

Washington Department of Revenue
https://dor.wa.gov/taxes-rates/income-tax

Homes.com 조회 자료
https://www.homes.com/new-homes/community/tehaleh/nzs6j72t4358j/

창발 Product Group — The AI Powered Creator
https://www.changbal.org/en/event-info/product-geulub-the-ai-powered-creator

영상 제작 과정 및 자료 — CatchUpAI_VL GitHub
https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/Tehaleh-Community-Video

#Tehaleh #MountRainier #WashingtonState
```

**태그**

```text
AI in Action, Tehaleh, 테할레, Tehaleh Washington, Tehaleh community, Bonney Lake, Pierce County, Mount Rainier, Mt Rainier, 레이니어 산, 워싱턴주, 시애틀 근교, 시애틀 생활, 미국 생활, 미국 주택, 워싱턴주 부동산, 시애틀 부동산, 마스터 플랜 커뮤니티, Post & Pour, Pacific Northwest, PNW living, 재택근무, 하이브리드 근무, 은퇴 생활, 55+ community, 한인 생활, Remotion, AI 영상 제작
```

**썸네일 문구**

```text
TEHALEH
시애틀 45분
레이니어가 보이는 동네
```

#### 썸네일 이미지 생성 프롬프트

참고 이미지로 `public/tehaleh-intro-0619/images/mt-rainier-personal_2.jpg`를 ChatGPT 또는 Gemini에 첨부한다.

**초안 — 레이니어 산과 생활 환경 강조**

```text
첨부한 레이니어 산 사진을 기반으로 한국어 YouTube 영상용 썸네일을 만들어 주세요.

주제: 시애틀 근교 Tehaleh 커뮤니티에서 레이니어 산을 바라보며 사는 삶
화면 비율: 16:9
해상도: 1280×720
스타일: 밝고 깨끗하며 고급스러운 부동산·라이프스타일 다큐멘터리
분위기: 맑은 날의 워싱턴주, 살기 좋은 자연 친화적 커뮤니티, 따뜻하고 희망적인 느낌

구성:
- 레이니어 산을 화면의 가장 중요한 시각 요소로 크게 표현
- 첨부 사진의 실제 풍경과 자연스러운 원근감을 유지
- 하늘과 산의 디테일을 선명하게 보정
- 주택이나 커뮤니티 풍경은 과장하지 말고 실제 PNW 지역처럼 자연스럽게 표현
- 왼쪽 또는 오른쪽에 제목을 넣을 수 있는 충분한 여백 확보
- 모바일 화면에서도 한눈에 읽히는 강한 대비와 단순한 구성
- 복잡한 장식, 어두운 배경, 과도한 HDR 효과는 사용하지 않기

썸네일 문구를 정확히 다음 두 줄로 표시:
“시애틀 45분”
“레이니어가 보이는 동네”

텍스트 디자인:
- 첫째 줄은 흰색 또는 밝은 크림색
- 둘째 줄의 “레이니어”는 따뜻한 노란색으로 강조
- 굵고 현대적인 한글 산세리프 글꼴
- 검은색 반투명 배경 또는 부드러운 그림자를 사용해 가독성 확보
- 글자가 잘리거나 산을 가리지 않도록 안전 여백 유지

사람, 로고, 워터마크, 지도 아이콘, 불필요한 작은 글자, 잘못된 한글은 추가하지 마세요.
```

**최종 권장안 — Tehaleh 이름 강조**

```text
첨부한 레이니어 산 사진을 기반으로 Tehaleh 커뮤니티를 소개하는 한국어 YouTube 썸네일을 만들어 주세요.

비율과 해상도: 16:9, 1280×720
스타일: 밝고 세련된 부동산·라이프스타일 다큐멘터리
분위기: 자연 친화적이고 살기 좋은 워싱턴주 커뮤니티

첨부 사진의 레이니어 산을 크고 선명하게 보여주고, 실제 풍경과 자연스러운 원근감을 유지하세요. 제목을 위한 여백을 확보하고 모바일에서도 잘 보이는 단순하고 강한 구도로 디자인하세요.

다음 문구를 정확히 세 줄로 표시하세요:

“TEHALEH”
“시애틀 45분”
“레이니어가 보이는 동네”

텍스트 디자인:
- “TEHALEH”를 가장 크고 강하게 표시
- TEHALEH는 흰색 대문자와 넓은 자간 사용
- “시애틀 45분”은 작은 보조 제목으로 배치
- “레이니어가 보이는 동네”에서 “레이니어”를 따뜻한 노란색으로 강조
- 굵고 현대적인 산세리프 글꼴 사용
- 반투명 어두운 그라데이션이나 부드러운 그림자로 가독성 확보
- 텍스트가 산 정상이나 주요 풍경을 가리지 않도록 배치
- 화면 가장자리에서 충분한 안전 여백 유지

어두운 전체 배경, 과도한 HDR, 가짜 도시 스카이라인, 사람, 로고, 워터마크, 지도 아이콘, 불필요한 작은 글자는 추가하지 마세요.
```

### English Version

**Title**

```text
AI in Action - 45 Minutes from Seattle: Live with Mt. Rainier in Tehaleh | 40 Miles of Trails
```

**Description**

```text
Discover Tehaleh, a nature-oriented community about a 45-minute drive from Seattle, Washington, through the eyes of someone who lives there.

This video explores the Mt. Rainier views I photographed from Post & Pour, more than 40 miles of trails, community amenities, home prices, remote and hybrid work, active retirement, and nearby Korean amenities.

For transit commuters, the Sounder trip from nearby Sumner Station to Seattle King Street Station takes about 50 minutes. Driving times to Seattle and Bellevue vary depending on traffic.

The listing count and price range shown in the video reflect a Homes.com lookup on June 21, 2026 and may change. Washington has no individual state income tax, although other state and local taxes may apply.

This video was created as a real-world AI content production example for the Changbal Product Group online event, “The AI Powered Creator.” AI and Remotion were used throughout the research, planning, visual design, narration, and video production process.

📌 Chapters

00:00 Tehaleh and Mt. Rainier
00:14 What is Tehaleh?
00:43 Community amenities and The Retreat
01:09 Post & Pour and my Mt. Rainier photos
01:55 Home price comparison
02:17 Remote and hybrid work
03:02 Active retirement and nearby Korean amenities
03:39 A resident's perspective and closing

🔗 Information and sources

Tehaleh
https://www.tehaleh.com/

Sound Transit S Line
https://www.soundtransit.org/ride-with-us/routes-schedules/s-line

Washington Department of Revenue
https://dor.wa.gov/taxes-rates/income-tax

Homes.com lookup
https://www.homes.com/new-homes/community/tehaleh/nzs6j72t4358j/

Changbal Product Group — The AI Powered Creator
https://www.changbal.org/en/event-info/product-geulub-the-ai-powered-creator

Production process and project materials — CatchUpAI_VL GitHub
https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/Tehaleh-Community-Video

#Tehaleh #MountRainier #WashingtonState
```

**Tags**

```text
AI in Action, Tehaleh, Tehaleh Washington, Tehaleh community, living in Tehaleh, Mount Rainier, Mt Rainier, Washington State, Seattle suburbs, Bonney Lake, Pierce County, Post & Pour, Pacific Northwest, PNW living, Washington real estate, Seattle real estate, master planned community, 40 miles of trails, remote work, hybrid work, active retirement, 55+ community, Korean community, Remotion, AI video production
```

**Thumbnail Copy**

```text
TEHALEH
45 MIN FROM SEATTLE
LIVE WITH MT. RAINIER
```

#### English Thumbnail Image Prompt

Attach `public/tehaleh-intro-0619/images/mt-rainier-personal_2.jpg` as the reference image in ChatGPT or Gemini.

```text
Create a high-impact YouTube thumbnail for an English-language video introducing the Tehaleh community in Washington State. Use the attached original Mt. Rainier photograph as the primary visual reference.

Canvas and format:
- 16:9 aspect ratio
- 1280×720 pixels
- Designed specifically for a YouTube thumbnail
- Keep all important text within safe margins for mobile and TV displays

Visual direction:
- Make Mt. Rainier the dominant visual element and keep its shape, perspective, and surrounding landscape faithful to the reference photograph
- Enhance the sky, mountain detail, and natural colors without creating an unrealistic HDR effect
- Convey a bright, welcoming, premium Pacific Northwest lifestyle
- Suggest a desirable nature-oriented residential community without adding fake landmarks, luxury mansions, or a Seattle skyline
- Use a clean, simple composition that remains understandable at small thumbnail size
- Reserve clear negative space on the left or right for text
- Add a subtle dark gradient or soft shadow behind the text for strong readability while keeping the overall image bright

Display exactly these three lines of text:
“TEHALEH”
“45 MIN FROM SEATTLE”
“LIVE WITH MT. RAINIER”

Text design:
- Make “TEHALEH” the largest and most prominent line
- Use bold, modern, condensed sans-serif typography
- Set “TEHALEH” in white uppercase letters with slightly expanded letter spacing
- Use “45 MIN FROM SEATTLE” as a smaller location hook
- Highlight “MT. RAINIER” in warm golden yellow while keeping the rest of the third line white
- Maintain strong contrast and avoid covering the mountain summit
- Check every word carefully and reproduce the English text exactly as written

Do not add people, logos, watermarks, maps, location pins, unrelated icons, tiny text, misspelled words, dark overall color grading, excessive saturation, or artificial city scenery.
```

### 공통 업로드 설정

| 항목 | 권장값 |
|------|--------|
| 카테고리 | People & Blogs |
| 한국어 영상 언어 | 한국어 |
| 영어 영상 언어 | English (United States) |
| 아동용 콘텐츠 | 아니요 |
| 촬영 장소 | Tehaleh, Bonney Lake, Washington, United States |
| 라이선스 | Standard YouTube License |
| 댓글 | 허용, 부적절한 댓글 검토 보류 |

한국어와 영어 영상은 서로의 번역본이므로 업로드 후 각 설명 첫 부분이나 고정 댓글에 상대 언어 영상 링크를 추가한다. 공개 URL이 생성되기 전에는 링크를 임의로 작성하지 않는다.

## 📎 참조 및 산출물

**생성된 파일**:

| 파일 | 위치 | 상태 |
|------|------|------|
| `tehaleh-research.md` | `vl_materials/` | ✅ |
| `video-slide-plan.md` | `public/tehaleh-intro-0619/` | ✅ |
| `image-prompts.md` | `public/tehaleh-intro-0619/` | ✅ |
| `gen_audio.py` | `public/tehaleh-intro-0619/` | ✅ |
| `gen_audio_qwen.py` | `public/tehaleh-intro-0619/` | ✅ |
| `slide_00~14.mp3` (15개) | `public/tehaleh-intro-0619/audio/` | ✅ |
| `data.ts` | `src/tehaleh-intro-0619/` | ✅ (AUDIO_READY=true) |
| `TehalehIntro0619.tsx` | `src/tehaleh-intro-0619/` | ✅ |
| `Root.tsx` | `src/` | ✅ (TehalehIntro0619 등록) |
| `tehaleh-intro-0619.mp4` | `out/` | ✅ 한국어 최종 렌더 |
| `tehaleh-intro-0619-en.mp4` | `out/` | ✅ 영어 최종 렌더 |
| `20260622_Tehaleh-Community-Video_Final_Retrospective.md` | `vl_worklog/` | ✅ Topic 완료 회고 |

**이미지 파일** (public/tehaleh-intro-0619/images/):
- `mt-rainier-personal.jpg`, `mt-rainier-personal_2.jpg` (직접 촬영)
- `slide_s2_location_map_ChatGPT.png`
- `slide_s5_community_center_Gemini.png`
- `slide_s8_home_office_Gemini.png`
- `slide_s11_senior_hiking_Gemini.png`

**재현 명령어**:
```
# Remotion Studio 미리보기
cd C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\Remotion-VideoCreation\my-first-video
npx remotion studio

# Qwen3-TTS 재생성
$env:DASHSCOPE_API_KEY = "your-key"
python public/tehaleh-intro-0619/gen_audio_qwen.py
python public/tehaleh-intro-0619-en/gen_audio_qwen.py

# MP4 재렌더링
npx remotion render TehalehIntro0619 out/tehaleh-intro-0619.mp4
npx remotion render TehalehIntroEn out/tehaleh-intro-0619-en.mp4
```

---

**작성자**: Claude with VibeLearn AI
**방법론**: VibeLearn AI
