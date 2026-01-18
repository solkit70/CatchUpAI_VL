# 배포 가이드 (Deployment Guide)

이 문서는 Claude Skills를 다른 환경에 배포하고 공유하는 방법을 설명합니다.

## 1. GitHub Repository 배포

### 1.1 Repository 구조 확인

```
Claude-Skills/
├── README.md              # 프로젝트 소개
├── CHANGELOG.md           # 버전 히스토리
├── LICENSE                # MIT 라이선스
├── .claude/
│   └── skills/            # Claude Skill 정의 파일들
│       ├── cua-vl/
│       │   └── SKILL.md
│       ├── youtube-to-md/
│       │   └── SKILL.md
│       └── video-edit/
│           └── SKILL.md
├── 01-Basic-Concepts/     # M1 학습 자료
├── 02-Skill-A-CUA-VL/     # M2 CUA_VL Skill
├── 03-Skill-B-YouTube-MD/ # M3 YouTube→MD Skill
├── 04-Skill-C-Video-Edit/ # M4 Video Edit Skill
├── 05-Integration-Deploy/ # M5 통합/배포
├── vl_materials/          # 학습 자료
└── vl_worklog/            # 학습 로그
```

### 1.2 GitHub에 공개하기

```bash
# 1. 원격 저장소 확인
git remote -v

# 2. 변경사항 커밋
git add .
git commit -m "Release v1.0.0: Complete Claude Skills learning project"

# 3. 푸시
git push origin main

# 4. (선택) 태그 생성
git tag -a v1.0.0 -m "First release with 3 skills"
git push origin v1.0.0
```

### 1.3 GitHub Release 생성

1. GitHub Repository 페이지에서 "Releases" 클릭
2. "Create a new release" 클릭
3. Tag 선택: `v1.0.0`
4. Release 제목: `v1.0.0 - Claude Skills Learning Complete`
5. Release 노트 작성 (CHANGELOG.md 참조)
6. "Publish release" 클릭

---

## 2. Skill 설치 방법 (사용자 가이드)

### 2.1 Claude Code 사용자용

1. **Repository 클론**
   ```bash
   git clone https://github.com/your-username/CatchUpAI_VL.git
   cd CatchUpAI_VL/Topics/Claude-Skills
   ```

2. **의존성 설치**
   ```bash
   # Python 라이브러리
   pip install youtube-transcript-api anthropic pydub ffmpeg-python openai-whisper

   # FFmpeg (필수)
   # Windows: choco install ffmpeg
   # Mac: brew install ffmpeg
   # Linux: apt install ffmpeg
   ```

3. **환경 변수 설정**
   ```bash
   # .env 파일 생성 (YouTube→MD Skill용)
   echo "ANTHROPIC_API_KEY=your_api_key_here" > .env
   ```

4. **Skill 사용**
   - Claude Code에서 해당 폴더를 열면 `.claude/skills/` 의 Skill들이 자동 인식됨
   - `/cua-vl`, `/youtube-to-md` 등으로 실행

### 2.2 일반 사용자용 (스크립트만)

Skill 정의 없이 Python 스크립트만 사용할 수 있습니다.

```bash
# YouTube→MD
python 03-Skill-B-YouTube-MD/examples/youtube-to-md.py "https://youtube.com/watch?v=..."

# Video Edit
python 04-Skill-C-Video-Edit/examples/video-editor.py video.mp4 --all
```

---

## 3. 커스터마이징

### 3.1 Skill 수정

각 Skill의 `SKILL.md` 파일을 수정하여 동작을 변경할 수 있습니다.

```
.claude/skills/
├── cua-vl/SKILL.md          # CUA_VL 방법론 프롬프트
├── youtube-to-md/SKILL.md   # YouTube 변환 가이드
└── video-edit/SKILL.md      # 영상 편집 가이드
```

### 3.2 스크립트 파라미터 조정

**YouTube→MD**:
- `--language`: 출력 언어 (ko, en)
- API 모델 변경: 코드 내 `claude-sonnet-4-5-20250929` 수정

**Video Edit**:
- `--threshold`: 무음 임계값 (dB)
- `--min-silence`: 최소 무음 길이 (ms)
- `--model`: Whisper 모델 (tiny, base, small)

---

## 4. 라이선스

MIT 라이선스로 배포됩니다.
- 자유롭게 사용, 수정, 배포 가능
- 저작권 표시 유지 필요
- 상업적 사용 가능

---

## 5. 기여 방법

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

**작성일**: 2026-01-18
**버전**: 1.0.0
