# YouTube Transcript Summarizer Skill 작업일지 (2026-01-28)

**목표**: 기존 YouTube-to-MD Skill을 범용화하여 다국어 지원 및 커뮤니티 공개용 Skill로 개선하고, claude-obsidian-skills 레포지토리에 PR 제출.

---

## 1. 주요 작업 내용 요약

### 1.1. 기존 Skill 분석
- **분석 대상**: `03-Skill-B-YouTube-MD/examples/youtube-to-md-skill/SKILL.md` 및 `md-generator.py`
- **기존 기능**: 영어 YouTube 영상 → 한국어 요약 (고정)
- **개선 필요 사항**: 다국어 지원, 배치 처리 옵션, 커맨드라인 인터페이스 강화

### 1.2. 대상 레포지토리 형식 파악
- **레포지토리**: https://github.com/jykim/claude-obsidian-skills
- **Skill 구조 분석**: `video-cleaning`, `markdown-video` 등 기존 Skill들의 SKILL.md 형식 확인
- **필수 요소**: Frontmatter (name, description, allowed-tools, license), When to Use, Requirements, Workflow, Troubleshooting

### 1.3. YouTube Transcript Summarizer Skill 개발

**새로운 기능**:
| 기능 | 기존 | 개선 |
|------|------|------|
| 소스 언어 | 영어 고정 | `--source-lang` 옵션 (11개 언어 + auto) |
| 타겟 언어 | 한국어 고정 | `--target-lang` 옵션 (11개 언어) |
| 배치 처리 | 쉘 스크립트 필요 | `--batch` 옵션 내장 |
| 타임라인 간격 | 5분 고정 | `--timeline-interval` 옵션 |
| 요약 스킵 | 불가 | `--no-summary` 옵션 |
| 프로그래밍 사용 | 불가 | 클래스로 import 가능 |

**지원 언어**: English, Korean, Japanese, Chinese, Spanish, French, German, Portuguese, Russian, Arabic, Hindi, Auto-detect

### 1.4. GitHub PR 제출
- **Fork 레포지토리**: https://github.com/solkit70/claude-obsidian-skills
- **브랜치**: `feature/youtube-transcript-summarizer`
- **PR 대상**: jykim/claude-obsidian-skills

---

## 2. 생성된 파일

### 2.1. Skill 파일
| 파일 | 설명 | 크기 |
|------|------|------|
| `youtube-transcript-summarizer/SKILL.md` | Skill 문서 (사용법, 옵션, 트러블슈팅) | ~8KB |
| `youtube-transcript-summarizer/youtube_transcript_summarizer.py` | Python 스크립트 | ~15KB |

### 2.2. 테스트 결과 파일
| 파일 | 영상 내용 | 세그먼트 | 크기 |
|------|----------|----------|------|
| `20260128_YouTube-Video-XfsXCfv7wKM_XfsXCfv7wKM.md` | Chrome 확장 프레임워크 | 136개 | 9,911자 |
| `20260128_YouTube-Video-MUDvwqJWWIw_MUDvwqJWWIw.md` | Claudebot AI 비서 | 572개 | 34,382자 |

---

## 3. 테스트 실행 결과

### 3.1. 테스트 1: Chrome 확장 프레임워크 영상
```
============================================================
YouTube Transcript Summarizer
============================================================
Source Language: English
Target Language: Korean
AI Summary: Yes

============================================================
Processing: YouTube Video XfsXCfv7wKM
Video ID: XfsXCfv7wKM
============================================================

[*] Fetching transcript...
[OK] Transcript retrieved: 136 segments

[*] Generating markdown...
[*] Generating AI summary...

[OK] Saved: test-output\20260128_YouTube-Video-XfsXCfv7wKM_XfsXCfv7wKM.md
     Size: 9,911 characters

============================================================
[OK] Processing complete!
============================================================
```

### 3.2. 테스트 2: Claudebot AI 비서 영상 (긴 영상)
```
============================================================
YouTube Transcript Summarizer
============================================================
Source Language: English
Target Language: Korean
AI Summary: Yes

============================================================
Processing: YouTube Video MUDvwqJWWIw
Video ID: MUDvwqJWWIw
============================================================

[*] Fetching transcript...
[OK] Transcript retrieved: 572 segments

[*] Generating markdown...
[*] Generating AI summary...

[OK] Saved: test-output\20260128_YouTube-Video-MUDvwqJWWIw_MUDvwqJWWIw.md
     Size: 34,382 characters

============================================================
[OK] Processing complete!
============================================================
```

---

## 4. 사용 방법

### 4.1. 기본 사용법
```bash
# 기본 (영어 영상 -> 한국어 요약)
python youtube_transcript_summarizer.py "https://www.youtube.com/watch?v=VIDEO_ID"

# 제목 지정
python youtube_transcript_summarizer.py "VIDEO_URL" --title "My Video Title"
```

### 4.2. 다국어 옵션
```bash
# 일본어 영상 -> 영어 요약
python youtube_transcript_summarizer.py "VIDEO_URL" --source-lang ja --target-lang en

# 한국어 영상 -> 한국어 요약
python youtube_transcript_summarizer.py "VIDEO_URL" --source-lang ko --target-lang ko

# 자동 감지 -> 프랑스어 요약
python youtube_transcript_summarizer.py "VIDEO_URL" --source-lang auto --target-lang fr
```

### 4.3. 배치 처리
```bash
# urls.txt 파일의 모든 영상 처리
python youtube_transcript_summarizer.py --batch "urls.txt" --output-dir "summaries"
```

### 4.4. 기타 옵션
```bash
# AI 요약 없이 자막만 추출
python youtube_transcript_summarizer.py "VIDEO_URL" --no-summary

# 타임라인 간격 변경 (10분)
python youtube_transcript_summarizer.py "VIDEO_URL" --timeline-interval 10
```

---

## 5. PR 정보

- **Fork URL**: https://github.com/solkit70/claude-obsidian-skills
- **Branch**: `feature/youtube-transcript-summarizer`
- **Commit**: `58bdd46 feat: Add youtube-transcript-summarizer skill`
- **PR Target**: jykim/claude-obsidian-skills (main branch)

### PR 내용 요약
```
feat: Add youtube-transcript-summarizer skill

- Extract transcripts from any YouTube video
- Multi-language support (source and target languages)
- Batch processing capability
- Configurable timeline intervals
- Structured markdown output with summary, key points, and timeline
```

---

## 6. 향후 개선 사항

- [ ] YouTube Data API를 사용한 영상 제목 자동 추출
- [ ] 프로그레스 바 추가 (긴 영상 처리 시)
- [ ] 요약 품질 개선 (더 긴 컨텍스트 사용)
- [ ] 썸네일 이미지 포함 옵션
- [ ] Obsidian 플러그인 연동

---

## 7. 참고 자료

- **원본 Skill**: `Topics/Claude-Skills/03-Skill-B-YouTube-MD/`
- **대상 레포지토리**: https://github.com/jykim/claude-obsidian-skills
- **YouTube Transcript API**: https://pypi.org/project/youtube-transcript-api/
- **Anthropic API**: https://docs.anthropic.com/

---

**작성자**: CUA_VL Claude Skills 학습
**작성일**: 2026-01-28
