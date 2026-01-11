---
name: youtube-to-md
description: YouTube 영상을 마크다운 문서로 변환합니다. 영상 URL을 입력하면 자막을 추출하고, AI로 요약하여 구조화된 MD 파일을 생성합니다.
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
---

# YouTube → MD Skill

이 Skill은 YouTube 영상을 구조화된 마크다운 문서로 변환합니다.

## 🎯 기능

1. **단일 영상 변환**: YouTube URL 하나를 MD로 변환
2. **배치 처리**: 여러 YouTube URL을 한 번에 처리
3. **AI 요약**: Claude API를 사용하여 영상 내용 자동 요약
4. **타임라인 생성**: 5분 간격 타임라인 자동 생성
5. **한국어 지원**: 영어 자막을 한국어로 번역 가능

## 📋 사용 방법

사용자가 다음과 같은 요청을 하면 이 Skill이 자동으로 활성화됩니다:

- "YouTube 영상을 마크다운으로 변환해줘"
- "이 영상의 내용을 정리해줘: [URL]"
- "AI Memory 360 Tour 영상들을 MD로 만들어줘"
- "youtube-to-md 스킬 실행"

## 🚀 실행 단계

### 단계 1: 사용자 요청 확인

사용자가 제공한 내용을 확인합니다:

1. **단일 URL 제공**: 사용자가 YouTube URL 하나를 제공한 경우
   - 예: "https://www.youtube.com/watch?v=7RTeHGbsd1o 를 MD로 변환해줘"
   - → 바로 단계 2로 이동

2. **여러 URL 또는 배치 요청**:
   - 예: "AI Memory 360 Tour 영상들을 모두 변환해줘"
   - → 단계 2에서 URL 목록 파일을 찾거나 생성

3. **URL 없음**: URL이 제공되지 않은 경우
   - 사용자에게 YouTube URL을 요청

### 단계 2: 환경 확인 및 준비

#### 2.1 필수 라이브러리 확인

다음 Python 라이브러리가 설치되어 있는지 확인합니다:

```bash
pip list | grep -E "(youtube-transcript-api|anthropic)"
```

설치되어 있지 않으면 설치합니다:

```bash
pip install youtube-transcript-api anthropic
```

#### 2.2 스크립트 위치 확인

MD 생성 스크립트의 위치를 확인합니다. 다음 경로를 순서대로 확인:

1. `c:\AI_study\2026\CatchUpAI_VL\Topics\Claude-Skills\03-Skill-B-YouTube-MD\examples\md-generator.py`
2. 현재 작업 디렉토리의 `md-generator.py`
3. 사용자의 홈 디렉토리의 `.claude\skills\youtube-to-md\md-generator.py`

**IMPORTANT**: 스크립트를 찾을 수 없으면 사용자에게 알리고 스크립트 경로를 요청합니다.

#### 2.3 Claude API 키 확인

환경변수 `ANTHROPIC_API_KEY`가 설정되어 있는지 확인:

```bash
echo %ANTHROPIC_API_KEY%  # Windows
echo $ANTHROPIC_API_KEY  # Linux/Mac
```

API 키가 없으면:
- 사용자에게 알림: "Claude API 키가 설정되지 않았습니다. 요약 기능이 제한됩니다."
- 계속 진행 (요약 없이 자막만 변환 가능)

### 단계 3: 영상 정보 수집

#### 3.1 단일 URL 처리

사용자가 제공한 YouTube URL에서 video ID를 추출합니다.

지원 형식:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`

#### 3.2 배치 처리

여러 영상을 처리해야 하는 경우:

1. **URL 목록 파일 찾기**:
   - 사용자가 파일 경로를 제공한 경우: 해당 파일 사용
   - 제공하지 않은 경우: 다음 경로 순서대로 확인
     - `./urls.txt`
     - `./AI-Memory-360-Tour/urls.txt`
     - `c:\AI_study\2026\CatchUpAI_VL\Topics\Claude-Skills\03-Skill-B-YouTube-MD\outputs\AI-Memory-360-Tour\urls.txt`

2. **URL 목록 파일이 없는 경우**:
   - 사용자에게 URL을 하나씩 입력받거나
   - AI Memory 360 Tour 등 알려진 컬렉션의 URL을 사용

3. **파일 형식**:
   - 한 줄에 하나의 YouTube URL
   - `#`로 시작하는 줄은 주석으로 무시
   - 빈 줄 무시

#### 3.3 영상 제목 추출 (선택)

사용자가 영상 제목을 제공하지 않은 경우:
- URL만으로 처리 (스크립트가 자동으로 video ID를 제목으로 사용)
- 또는 사용자에게 제목을 물어볼 수 있음

### 단계 4: 영상 변환 실행

#### 4.1 단일 영상 변환

md-generator.py 스크립트를 실행합니다:

```bash
python md-generator.py "YouTube_URL" "영상 제목"
```

예시:
```bash
python md-generator.py "https://www.youtube.com/watch?v=7RTeHGbsd1o" "AI Memory, The Next Frontier - Charles Fan"
```

#### 4.2 배치 처리

URL 목록 파일의 각 URL에 대해 순차적으로 실행:

```bash
# 파일 읽기
while IFS= read -r line; do
    # 주석과 빈 줄 건너뛰기
    if [[ $line =~ ^# ]] || [[ -z $line ]]; then
        continue
    fi

    # URL 추출
    url=$(echo $line | awk '{print $1}')

    # 제목 추출 (있으면)
    title=$(echo $line | cut -d'#' -f2 | xargs)

    # 변환 실행
    python md-generator.py "$url" "$title"

    echo "완료: $url"
    echo "---"
done < urls.txt
```

#### 4.3 진행 상황 표시

배치 처리 중에는 진행 상황을 사용자에게 표시합니다:

```
[1/15] 처리 중: AI Memory, The Next Frontier...
[OK] 완료
[2/15] 처리 중: Amazon Bedrock AgentCore...
[OK] 완료
...
```

#### 4.4 오류 처리

다음과 같은 오류가 발생할 수 있습니다:

1. **자막 없음**:
   - 사용자에게 알림: "영상에 자막이 없습니다"
   - 다음 영상으로 계속

2. **API 에러**:
   - Claude API 호출 실패 시 요약 없이 계속
   - 사용자에게 알림

3. **네트워크 오류**:
   - 재시도 (최대 3회)
   - 실패 시 사용자에게 알림하고 건너뛰기

### 단계 5: 결과 확인 및 정리

#### 5.1 생성된 파일 확인

md-generator.py는 다음 위치에 파일을 저장합니다:

```
outputs/markdown/YYYYMMDD_[제목]_[VIDEO_ID].md
```

생성된 파일 목록을 사용자에게 표시합니다.

#### 5.2 파일 이동 (선택)

사용자가 원하는 경우 생성된 MD 파일을 특정 위치로 이동:

예: AI Memory 360 Tour 영상들을 `vl_materials` 폴더로 이동

```bash
mv outputs/markdown/*.md c:/AI_study/2026/CatchUpAI_VL/Topics/Claude-Skills/vl_materials/AI-Memory-360-Tour/
```

#### 5.3 요약 통계 제공

배치 처리 완료 후 다음 정보를 제공:

```
============================================================
변환 완료!
============================================================

총 영상: 15개
성공: 13개
실패: 2개 (자막 없음)

생성된 파일:
- outputs/markdown/20260111_AI-Memory-The-Next-Frontier_7RTeHGbsd1o.md
- outputs/markdown/20260111_Amazon-Bedrock-AgentCore_7qX5iV2bqU4.md
...

총 처리 시간: 25분 30초
```

### 단계 6: 사용자 피드백 및 다음 단계

변환이 완료되면 사용자에게 다음을 물어봅니다:

1. **추가 영상 변환**: "다른 영상도 변환하시겠습니까?"
2. **파일 확인**: "생성된 파일을 확인하시겠습니까?"
3. **다른 작업**: "MD 파일을 다른 곳으로 이동하거나 추가 작업이 필요하신가요?"

## ⚙️ 고급 옵션

사용자가 다음과 같은 옵션을 요청할 수 있습니다:

### 옵션 1: 번역 없이 원본만

```bash
# 한국어 번역 없이 원본 영어 자막만 저장
# (스크립트 수정 필요 - 현재 버전은 자동으로 요약만 생성)
```

### 옵션 2: 특정 언어 자막 선택

```bash
# 영어 외 다른 언어 자막 추출
# 스크립트의 languages 파라미터 수정
```

### 옵션 3: 타임라인 간격 조정

```bash
# 5분 대신 10분 간격 타임라인
# 스크립트의 interval 변수 수정
```

## 🐛 문제 해결

### 문제 1: "자막을 가져올 수 없습니다"

**원인**:
- 영상에 자막이 없음
- 영상이 비공개 또는 삭제됨
- 네트워크 문제

**해결**:
1. YouTube에서 영상을 직접 확인
2. 자막(CC) 버튼이 활성화되어 있는지 확인
3. 다른 영상으로 테스트

### 문제 2: "Claude API 키가 없습니다"

**원인**:
- 환경변수 ANTHROPIC_API_KEY가 설정되지 않음

**해결**:
```bash
# Windows (PowerShell)
$env:ANTHROPIC_API_KEY = "your-api-key-here"

# Linux/Mac
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 문제 3: "md-generator.py를 찾을 수 없습니다"

**원인**:
- 스크립트가 예상 경로에 없음

**해결**:
1. 스크립트 경로 확인:
   ```bash
   find / -name "md-generator.py" 2>/dev/null
   ```
2. 사용자에게 정확한 경로 요청
3. 필요하면 스크립트 다시 생성

### 문제 4: UnicodeEncodeError

**원인**:
- Windows 콘솔 인코딩 문제

**해결**:
- 스크립트는 이미 UTF-8 인코딩 설정을 포함하고 있음
- PowerShell에서 실행 시 `chcp 65001` 명령 실행

## 📚 참조

- Python 스크립트 위치: `../md-generator.py`
- YouTube Transcript API: https://pypi.org/project/youtube-transcript-api/
- Anthropic API: https://docs.anthropic.com/

## ✅ Definition of Done

이 Skill 실행이 성공적으로 완료되려면:

- [ ] 사용자가 요청한 모든 YouTube URL 처리 완료
- [ ] 각 영상마다 MD 파일 생성됨
- [ ] 생성된 파일에 요약, 핵심 포인트, 타임라인 포함
- [ ] 오류가 발생한 영상은 사용자에게 명확히 알림
- [ ] 생성된 파일 위치를 사용자에게 제공

---

**Skill 버전**: 1.0
**작성일**: 2026-01-11
**작성자**: CUA_VL Claude Skills 학습
