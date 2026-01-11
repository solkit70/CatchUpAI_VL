# YouTube → MD Skill 사용 가이드

**버전**: 1.0
**작성일**: 2026-01-11
**대상**: YouTube 영상을 마크다운으로 변환하고 싶은 모든 사용자

---

## 📚 목차

1. [빠른 시작](#빠른-시작)
2. [설치 및 설정](#설치-및-설정)
3. [기본 사용법](#기본-사용법)
4. [고급 사용법](#고급-사용법)
5. [문제 해결](#문제-해결)
6. [FAQ](#faq)

---

## 빠른 시작

### 5분 안에 시작하기

1. **라이브러리 설치**:
   ```bash
   pip install youtube-transcript-api anthropic
   ```

2. **API 키 설정**:
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

3. **영상 변환**:
   ```bash
   python md-generator.py "https://www.youtube.com/watch?v=VIDEO_ID" "영상 제목"
   ```

4. **결과 확인**:
   - `outputs/markdown/` 폴더에서 생성된 MD 파일 확인

---

## 설치 및 설정

### 1. 사전 요구사항

- Python 3.7 이상
- pip (Python 패키지 관리자)
- 인터넷 연결
- (선택) Claude API 키 (요약 기능 사용 시)

### 2. 라이브러리 설치

```bash
# youtube-transcript-api: YouTube 자막 추출
pip install youtube-transcript-api

# anthropic: Claude API (요약 생성용)
pip install anthropic
```

**설치 확인**:
```bash
pip list | grep -E "(youtube-transcript-api|anthropic)"
```

출력 예시:
```
anthropic              0.75.0
youtube-transcript-api 1.2.3
```

### 3. Claude API 키 설정

#### 방법 1: 환경변수 (권장)

**Windows (PowerShell)**:
```powershell
$env:ANTHROPIC_API_KEY = "your-api-key-here"
```

**Linux/Mac**:
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

**영구 설정** (재시작 후에도 유지):

Windows: 시스템 환경변수에 추가
Linux/Mac: `~/.bashrc` 또는 `~/.zshrc`에 추가

#### 방법 2: .env 파일

프로젝트 루트에 `.env` 파일 생성:
```
ANTHROPIC_API_KEY=your-api-key-here
```

**Note**: API 키가 없어도 자막 추출 및 타임라인 생성은 가능하지만, AI 요약 기능은 사용 불가

### 4. 스크립트 다운로드

```bash
# GitHub에서 클론 (또는 파일 직접 복사)
git clone https://github.com/your-repo/youtube-to-md.git
cd youtube-to-md/examples
```

---

## 기본 사용법

### 1. 단일 영상 변환

#### 명령어 형식

```bash
python md-generator.py "<YouTube_URL>" "<영상_제목>"
```

#### 예시 1: 제목 포함

```bash
python md-generator.py "https://www.youtube.com/watch?v=7RTeHGbsd1o" "AI Memory, The Next Frontier - Charles Fan"
```

#### 예시 2: 제목 생략 (Video ID를 제목으로 사용)

```bash
python md-generator.py "https://www.youtube.com/watch?v=7RTeHGbsd1o"
```

### 2. 지원하는 URL 형식

다음 형식의 YouTube URL을 모두 지원합니다:

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`
- `VIDEO_ID` (URL 없이 ID만)

### 3. 출력 결과

#### 생성되는 파일

- **위치**: `outputs/markdown/`
- **파일명**: `YYYYMMDD_[제목]_[VIDEO_ID].md`
- **예시**: `20260111_AI-Memory-The-Next-Frontier-Charles-Fan_7RTeHGbsd1o.md`

#### MD 파일 구조

```markdown
# 영상 제목

**원본 영상**: [링크]
**작성일**: 2026-01-11
**Video ID**: VIDEO_ID

## 요약
(2-3문장 요약)

## 핵심 포인트
- 포인트 1
- 포인트 2
...

## 주요 내용
### 섹션 1: 제목
- 내용

## 타임라인
- **00:00**: 인트로
- **05:00**: 주요 내용 시작
...

## 전체 자막 (타임스탬프 포함)
**[00:00]** 자막 내용...
```

---

## 고급 사용법

### 1. 배치 처리 (여러 영상 한 번에 변환)

#### Step 1: URL 목록 파일 생성

`urls.txt` 파일 생성:

```
# AI Memory 360 Tour Videos

https://www.youtube.com/watch?v=7RTeHGbsd1o # AI Memory, The Next Frontier
https://www.youtube.com/watch?v=FbRcb8XryNg # Building the visual memory layer
https://www.youtube.com/watch?v=Q5ivWi1msos # The memory singularity
```

**파일 형식**:
- 한 줄에 하나의 URL
- `#` 뒤에 제목 작성 (선택)
- 빈 줄과 주석(`#`로 시작하는 줄) 무시

#### Step 2: 배치 스크립트 실행

**bash (Linux/Mac)**:
```bash
while IFS= read -r line || [ -n "$line" ]; do
    # 주석과 빈 줄 건너뛰기
    if [[ $line =~ ^# ]] || [[ -z $line ]]; then
        continue
    fi

    # URL과 제목 추출
    url=$(echo $line | awk '{print $1}')
    title=$(echo $line | cut -d'#' -f2 | xargs)

    # 변환 실행
    echo "처리 중: $title"
    python md-generator.py "$url" "$title"
    echo "---"
done < urls.txt
```

**PowerShell (Windows)**:
```powershell
Get-Content urls.txt | ForEach-Object {
    if ($_ -match '^#' -or $_.Length -eq 0) { return }

    $parts = $_ -split '#'
    $url = $parts[0].Trim()
    $title = if ($parts.Length -gt 1) { $parts[1].Trim() } else { "" }

    Write-Host "처리 중: $title"
    python md-generator.py "$url" "$title"
    Write-Host "---"
}
```

### 2. Claude Skill 사용 (Claude Code에서)

#### Skill 설치

```bash
# Personal Skills 폴더에 복사
cp -r youtube-to-md-skill ~/.claude/skills/youtube-to-md
```

#### Skill 사용

Claude Code 대화에서:

**예시 1: 단일 영상**
```
YouTube 영상을 MD로 변환해줘: https://www.youtube.com/watch?v=VIDEO_ID
```

**예시 2: 배치 처리**
```
AI Memory 360 Tour 영상들을 모두 변환해줘
```

Claude가 자동으로:
1. 라이브러리 설치 확인
2. 스크립트 실행
3. 결과 파일 생성
4. 통계 제공

### 3. 커스터마이징

#### 3.1 타임라인 간격 변경

`md-generator.py` 파일 수정:

```python
# 5분(300초) 간격을 10분(600초)로 변경
def create_timeline(transcript):
    interval = 600  # 5분 → 10분
    ...
```

#### 3.2 요약 스타일 변경

`md-generator.py`의 `summarize_with_claude()` 함수에서 프롬프트 수정:

```python
prompt = f"""다음은 YouTube 영상의 자막입니다.

...

- 더 자세한 요약이 필요하면 "4-5문장으로 요약"으로 변경
- 기술적 용어 설명 추가 요청
- 예제 코드 추출 요청 등
"""
```

#### 3.3 파일명 형식 변경

`md-generator.py`의 `main()` 함수:

```python
# YYYYMMDD_제목_ID.md → 제목_YYYYMMDD.md
filename = f"{safe_title}_{datetime.now().strftime('%Y%m%d')}.md"
```

---

## 문제 해결

### 문제 1: "자막을 가져올 수 없습니다"

**증상**:
```
[X] 자막 추출 실패: Could not retrieve a transcript
```

**가능한 원인**:
1. 영상에 자막이 없음
2. 영상이 비공개 또는 삭제됨
3. 네트워크 연결 문제
4. YouTube API 제한

**해결 방법**:

1. **YouTube에서 영상 확인**:
   - 영상이 재생되는지 확인
   - 자막(CC) 버튼이 활성화되어 있는지 확인

2. **다른 영상으로 테스트**:
   ```bash
   # 자막이 있는 것으로 알려진 영상으로 테스트
   python md-generator.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
   ```

3. **사용 가능한 자막 확인**:
   스크립트를 실행하면 사용 가능한 자막 목록이 출력됩니다.

### 문제 2: "Claude API 키가 없습니다"

**증상**:
```
[!] Claude API 키가 없습니다. 요약을 건너뜁니다.
```

**해결 방법**:

1. **환경변수 설정 확인**:
   ```bash
   echo $ANTHROPIC_API_KEY  # Linux/Mac
   echo %ANTHROPIC_API_KEY%  # Windows CMD
   echo $env:ANTHROPIC_API_KEY  # Windows PowerShell
   ```

2. **API 키 설정**:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-api03-..."
   ```

3. **API 키 없이 사용**:
   요약 기능만 제외하고 나머지 기능은 정상 작동합니다.
   - 자막 추출: ✅
   - 타임라인 생성: ✅
   - AI 요약: ❌ (건너뜀)

### 문제 3: UnicodeEncodeError

**증상**:
```
UnicodeEncodeError: 'charmap' codec can't encode characters
```

**원인**: Windows 콘솔 인코딩 문제

**해결 방법**:

1. **PowerShell 사용 (권장)**:
   CMD 대신 PowerShell에서 실행

2. **콘솔 인코딩 변경**:
   ```bash
   chcp 65001  # UTF-8로 변경
   ```

3. **스크립트는 이미 처리됨**:
   `md-generator.py`는 UTF-8 인코딩 처리가 포함되어 있어 대부분의 경우 문제없음

### 문제 4: ModuleNotFoundError

**증상**:
```
ModuleNotFoundError: No module named 'youtube_transcript_api'
```

**해결 방법**:

1. **라이브러리 설치**:
   ```bash
   pip install youtube-transcript-api anthropic
   ```

2. **Python 경로 확인**:
   ```bash
   which python  # Linux/Mac
   where python  # Windows
   ```

3. **가상환경 활성화** (사용 중인 경우):
   ```bash
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows
   ```

---

## FAQ

### Q1: 한국어 영상도 변환할 수 있나요?

**A**: 네, 한국어 자막이 있는 영상은 변환 가능합니다. 다만 현재 버전은 요약 기능이 한국어로 최적화되지 않았습니다.

개선 방향:
- 스크립트의 `languages` 파라미터를 `['ko', 'en']`으로 수정
- 프롬프트를 한국어 자막에 맞게 조정

### Q2: 영상 길이에 제한이 있나요?

**A**: 기술적 제한은 없지만, 매우 긴 영상(2시간 이상)은:
- 자막 추출 시간이 오래 걸릴 수 있음
- Claude API 토큰 제한으로 요약이 제한될 수 있음 (현재는 처음 15,000자만 사용)

해결 방법:
- 긴 영상은 요약 없이 자막만 추출
- 또는 청크 분할 로직 개선

### Q3: 여러 영상을 동시에 처리할 수 있나요?

**A**: 현재 버전은 순차 처리만 지원합니다. 동시 처리를 원한다면:

**병렬 처리 스크립트** (Linux/Mac):
```bash
cat urls.txt | xargs -P 4 -I {} sh -c 'python md-generator.py "{}"'
```

- `-P 4`: 최대 4개 동시 실행

### Q4: 생성된 MD 파일의 품질을 어떻게 확인하나요?

**A**: 다음 사항을 확인하세요:

1. **요약 정확성**: 실제 영상 내용과 일치하는지
2. **핵심 포인트**: 주요 내용이 빠짐없이 포함되었는지
3. **타임라인**: 주요 순간이 표시되었는지
4. **자막 완전성**: 전체 자막이 포함되었는지

**품질 개선 팁**:
- 영상 제목을 정확히 입력하면 요약 품질 향상
- 프롬프트 조정으로 원하는 스타일 요약 가능

### Q5: 비용이 얼마나 드나요?

**A**: 비용은 Claude API 사용료만 발생합니다.

**예상 비용** (Claude Sonnet 4.5 기준):
- 영상 1개 (10분): 약 $0.05-0.10
- 영상 1개 (30분): 약 $0.10-0.20

**무료 사용**:
- Claude API 키 없이 사용하면 요약만 제외하고 무료
- YouTube Transcript API는 무료

### Q6: 다른 사람과 공유할 수 있나요?

**A**: 네! 생성된 MD 파일은:
- GitHub에 업로드 가능
- 블로그 포스트로 변환 가능
- Notion/Obsidian 등 노트 앱에서 사용 가능

**주의사항**:
- 원본 영상의 저작권 확인
- 출처 표시 (MD 파일에 자동 포함됨)

---

## 📞 지원 및 피드백

### 문제 보고

GitHub Issues: [링크]

### 개선 제안

Pull Request 환영합니다!

### 커뮤니티

CUA_VL Discord: [링크]

---

**가이드 버전**: 1.0
**최종 업데이트**: 2026-01-11
**작성자**: CUA_VL Claude Skills 학습
