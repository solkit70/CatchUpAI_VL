# WorkLog - M3: Skill B - YouTube→MD Skill 개발

**날짜**: 2026-01-11
**Topic**: Claude-Skills
**모듈**: M3 - Skill B: YouTube→MD Skill 개발
**학습 시간**: 오전 시작 - 진행 중 (총 약 10시간)

---

## 🎯 오늘의 학습 목표

- [x] YouTube 자막 추출 방법 이해 ✅
- [x] 번역 API/라이브러리 사용 가능 ✅
- [x] MD 파일 구조화 변환 가능 ✅
- [x] Skill로 전체 워크플로우 자동화 ✅
- [x] AI Memory 360 Tour 영상 처리 완료 (최소 3개) ✅

**달성률**: 5/5 (100%) ✅

---

## 📚 진행 내용

### 1. 환경 설정 및 라이브러리 설치

**시간**: 09:00 - 09:30 (30분)

**목적**:
YouTube 자막 추출을 위한 개발 환경 준비

**과정**:
1. M3 폴더 구조 생성 (`03-Skill-B-YouTube-MD/`)
2. Python 라이브러리 설치:
   - `youtube-transcript-api` (v1.2.3)
   - `anthropic` (v0.75.0)
3. AI Memory 360 Tour 영상 URL 목록 수집 (WebFetch)

**결과**:
- ✅ 폴더 구조 완성
- ✅ 라이브러리 설치 완료
- ✅ 15개 영상 URL 목록 확보

**메모/인사이트**:
- WebFetch를 사용해 AI Memory 360 Tour 페이지에서 YouTube URL을 효율적으로 추출
- URLs.txt 파일에 주석으로 각 영상 제목 기록

---

### 2. YouTube 자막 추출 및 번역 테스트

**시간**: 09:30 - 11:00 (90분)

**목적**:
youtube-transcript-api를 사용하여 자막 추출 및 번역 검증

**과정**:
1. `youtube-transcript-test.py` 스크립트 작성
2. YouTube Transcript API 최신 버전 사용법 학습:
   - 구버전: `get_transcript()` (deprecated)
   - 신버전: `list()` → `find_transcript()` → `fetch()`
3. Windows UTF-8 인코딩 문제 해결:
   - `io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')`
4. Claude API 모델명 수정:
   - `claude-3-5-sonnet-20241022` → `claude-sonnet-4-5-20250929`
5. 첫 번째 영상으로 테스트 (Charles Fan - AI Memory)

**결과**:
- ✅ 658개 자막 세그먼트 추출 성공
- ✅ 한국어 번역 성공 (샘플 1000자)
- ✅ 타임스탬프 유지 확인

**메모/인사이트**:
- YouTube Transcript API가 최근 업데이트되어 사용법 변경됨
- `FetchedTranscript` 객체의 속성 접근 방식 이해 (`entry.start`, `entry.text`)
- Windows 콘솔 인코딩 이슈를 초반에 해결하여 이후 작업 원활

---

### 3. MD 파일 생성 로직 구현

**시간**: 11:00 - 14:00 (180분)

**목적**:
추출된 자막을 구조화된 마크다운으로 변환

**과정**:
1. `md-generator.py` 스크립트 작성 (~400 라인)
2. 핵심 기능 구현:
   - `get_transcript()`: 자막 추출
   - `format_timestamp()`: 초 → HH:MM:SS 변환
   - `create_timeline()`: 5분 간격 타임라인 생성
   - `summarize_with_claude()`: AI 요약 생성
   - `generate_markdown()`: 최종 MD 문서 생성
3. Claude API 프롬프트 설계:
   - 요약, 핵심 포인트, 주요 섹션 구조화 요청
   - 한국어 출력 명시
4. 첫 영상으로 테스트 실행

**결과**:
- ✅ 48,929자 크기의 완성된 MD 파일 생성
- ✅ 요약, 핵심 포인트, 섹션, 타임라인, 전체 자막 모두 포함
- ✅ 읽기 쉬운 구조화된 문서 확인

**메모/인사이트**:
- Claude API의 구조화된 프롬프트가 매우 효과적
- 5분 간격 타임라인이 긴 영상 파악에 유용
- 처음 15,000자만 요약에 사용하여 API 비용 절감

---

### 4. Skill 통합 및 SKILL.md 작성

**시간**: 14:00 - 18:00 (240분)

**목적**:
YouTube→MD 변환을 Skill로 통합

**과정**:
1. SKILL.md 작성 (~700 라인):
   - Description: "YouTube 영상을 마크다운 문서로 변환합니다..."
   - 단계별 실행 지침 상세 작성
   - 오류 처리 시나리오 포함
   - 문제 해결 가이드 추가
2. Personal Skills 폴더에 설치:
   - `~/.claude/skills/youtube-to-md/`
   - SKILL.md와 md-generator.py 복사
3. Skill 구조 검증

**결과**:
- ✅ SKILL.md 완성
- ✅ Personal Skills에 설치 완료
- ✅ 재사용 가능한 Skill 준비 완료

**메모/인사이트**:
- M2에서 배운 "Skill is Gateway" 철학 적용
- SKILL.md에 충분한 설명을 포함하면 Claude가 자율적으로 실행 가능
- 오류 처리 시나리오를 미리 작성하여 Skill 안정성 향상

---

### 5. AI Memory 360 Tour 영상 배치 처리

**시간**: 18:00 - 19:30 (90분)

**목적**:
실제 행사 준비 - 영상 학습 자료 생성

**과정**:
1. URL 목록에서 3개 영상 선택
2. 순차적으로 변환 실행:
   - ✅ 영상 1: "AI Memory, The Next Frontier" (Charles Fan) - 658 세그먼트
   - ❌ 영상 2: "Amazon Bedrock AgentCore" - 자막 없음 (건너뜀)
   - ✅ 영상 3: "Building the visual memory layer for AI" (Ben Zhou) - 345 세그먼트
   - ✅ 영상 4: "The memory singularity" (Gabriel Kreiman) - 315 세그먼트
3. 생성된 MD 파일을 vl_materials 폴더로 이동

**결과**:
- ✅ 3개 영상 성공적으로 변환
- ✅ vl_materials/AI-Memory-360-Tour/ 폴더에 저장
- ✅ 총 98,754자 분량의 학습 자료 확보

**메모/인사이트**:
- 일부 영상은 자막이 없어 건너뛰어야 함
- 자막이 있는 영상은 2-3분 만에 완성된 MD 생성
- 2026-01-16 행사 준비 완료 ✅

---

### 6. 문서화 및 정리

**시간**: 19:30 - 현재 (90분)

**목적**:
README, 사용 가이드 작성

**과정**:
1. README.md 작성:
   - 모듈 개요, 학습 목표 달성도
   - 산출물 설명
   - 주요 성과 및 인사이트
   - 폴더 구조
2. user-guide.md 작성:
   - 빠른 시작 가이드
   - 설치 및 설정 상세
   - 기본/고급 사용법
   - 문제 해결 및 FAQ
3. concepts/ 문서 (예정)

**결과**:
- ✅ README.md 완성 (~500 라인)
- ✅ user-guide.md 완성 (~600 라인)
- ✅ 교과서 품질 문서화 달성

**메모/인사이트**:
- 사용 가이드에 실제 사용 예시와 문제 해결 포함
- 다음 학습자가 바로 활용 가능한 수준
- FAQ 섹션에 실제 테스트 중 발견한 이슈 반영

---

## 🐛 문제 해결 로그

### 문제 1: YouTube Transcript API 변화

**증상**:
```python
YouTubeTranscriptApi.get_transcript(video_id)  # AttributeError
```

**원인**:
API가 최신 버전으로 업데이트되면서 사용법 변경

**해결**:
```python
api = YouTubeTranscriptApi()
transcript_list = api.list(video_id)
transcript = transcript_list.find_transcript(['en'])
fetched = transcript.fetch()
```

**참조**:
- `help(YouTubeTranscriptApi)` 명령어로 메서드 확인
- `FetchedTranscript` 객체 속성 직접 접근 (`entry.start`, `entry.text`)

---

### 문제 2: Windows 콘솔 UTF-8 인코딩

**증상**:
```
UnicodeEncodeError: 'charmap' codec can't encode character
```

**원인**:
Windows 콘솔 기본 인코딩이 cp1252 (이모지, 한글 미지원)

**해결**:
```python
import sys, io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
```

**참조**:
- 스크립트 최상단에 추가
- 이모지 대신 `[OK]`, `[X]` 등 ASCII 문자 사용

---

### 문제 3: Claude API 모델명 오류

**증상**:
```
Error code: 404 - model: claude-3-5-sonnet-20241022
```

**원인**:
Claude API 모델명이 업데이트됨

**해결**:
```python
model="claude-sonnet-4-5-20250929"  # 최신 모델명
```

**참조**:
- Claude Code에서 사용 중인 모델명 확인
- 향후 model 파라미터를 변수로 분리하여 쉽게 업데이트 가능하게 개선

---

## 📊 DoD 체크리스트

로드맵 M3의 Definition of Done:

- [x] 모든 학습 목표 달성 (5개 체크) ✅
- [x] 실습 과제 3개 완료 ✅
- [x] YouTube → MD Skill 완성 및 테스트 성공 ✅
- [x] **AI Memory 360 Tour 영상들을 MD로 변환 완료** (최소 3개 영상) ✅
- [x] 생성된 MD 파일 품질 확인 (읽기 쉬움, 요약 정확함) ✅
- [x] README.md 및 사용 가이드 작성 ✅
- [x] WorkLog 작성 완료 ✅
- [ ] Daily Retrospective 작성 (다음 단계)
- [x] **2026-01-16 행사 준비 완료** ✅

**완료율**: 8/9 (89%)

---

## 💡 Daily Retrospective

### What went well (잘된 점)

1. **API 변화 빠른 대응**:
   - YouTube Transcript API 업데이트를 `help()` 명령어로 빠르게 파악
   - 에러 메시지를 통해 정확한 사용법 학습

2. **실전 테스트 우선**:
   - AI Memory 360 Tour 영상으로 직접 테스트
   - 실제 사용 케이스에서 품질 검증

3. **효율적인 문서화**:
   - 개발 중 발생한 이슈를 바로 문제 해결 가이드에 반영
   - 다음 사용자를 위한 FAQ 작성

4. **2026-01-16 행사 준비 완료**:
   - 3개 핵심 발표 내용 정리
   - 구조화된 학습 자료 확보 ✅

### What could be improved (개선할 점)

1. **배치 처리 자동화**:
   - 현재는 수동으로 각 영상 실행
   - URL 목록 파일을 읽어 자동 처리하는 스크립트 필요

2. **영상 제목 자동 추출**:
   - 현재는 수동으로 제목 입력
   - YouTube Data API를 사용하면 자동 추출 가능

3. **API 비용 최적화**:
   - 현재는 영상당 요약 생성 (API 비용 발생)
   - 캐싱 메커니즘 추가하면 중복 호출 방지

### Insights (인사이트)

1. **"API 문서는 최신 버전 확인"**:
   - YouTube Transcript API처럼 사용법이 변경될 수 있음
   - 에러 발생 시 공식 문서 및 `help()` 명령어 활용

2. **"구조화된 프롬프트의 힘"**:
   - Claude API에 명확한 형식 지정 시 일관된 결과
   - "## 요약", "## 핵심 포인트" 등 구조 명시가 핵심

3. **"실전 테스트가 최고의 검증"**:
   - 간단한 예제보다 실제 사용할 데이터로 테스트
   - AI Memory 360 Tour 영상으로 실용성 확인

4. **"90% 시간 절약 달성"**:
   - Before: 영상당 35-70분 (시청 + 메모 + 정리)
   - After: 영상당 2-3분 (스크립트 실행)
   - 자동화의 가치 실감

### Tomorrow's focus (내일 집중할 것)

1. M3 Retrospective 작성
2. GitHub 커밋 및 Push
3. M4 시작 (선택) 또는 M3 회고 후 휴식

---

## 📎 참조 및 산출물

**생성된 파일/폴더**:
- `03-Skill-B-YouTube-MD/examples/youtube-transcript-test.py`: 자막 추출 테스트 스크립트
- `03-Skill-B-YouTube-MD/examples/md-generator.py`: MD 생성 스크립트
- `03-Skill-B-YouTube-MD/examples/youtube-to-md-skill/SKILL.md`: Claude Skill
- `03-Skill-B-YouTube-MD/README.md`: 모듈 완료 문서
- `03-Skill-B-YouTube-MD/guides/user-guide.md`: 사용 가이드
- `vl_materials/AI-Memory-360-Tour/`: 변환된 MD 파일 3개

**참조 자료**:
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/): Python 자막 추출 라이브러리
- [Anthropic API](https://docs.anthropic.com/): Claude API 문서
- [AI Memory 360 Tour](https://memverge.ai/memmachine/ai-memory-360-tour/november-2025/): 영상 및 슬라이드

**다음 세션 준비사항**:
- M3 Retrospective 작성
- GitHub에 M3 산출물 커밋
- (선택) 추가 AI Memory 360 Tour 영상 변환 (나머지 12개)

---

**작성자**: CUA_VL Claude Skills 학습
**방법론**: CUA_VL (Catch Up AI Vibe Learning)
**상태**: ✅ M3 거의 완료 (Retrospective 남음)
