# Worklog 2026-01-24

## 작업 개요
- **프로젝트**: AI4PKM Video Cleaning Skill 테스트
- **작업 내용**: OpenAI Whisper API 기반 무음 구간 제거 (단어 타임스탬프 방식)
- **사용한 Skill**: `AI4PKM_Video_Cleaning` (GitHub: jykim/claude-obsidian-skills)
- **입력 파일**: `original.mkv` (92.2분, 364MB)
- **출력 파일**: `original_edited_AI4PKM.mkv` (81.0분, 318MB)
- **작성자**: Claude

---

## 작업 시간

| 구분 | 시작 | 종료 | 소요 시간 |
|------|------|------|----------|
| **전체 작업** | 09:25 | 10:45 | **1시간 20분** |
| 동영상 편집 | 09:50 | 10:40 | 50분 |

- **준비 작업** (09:25 - 09:50): AI4PKM Skill 분석, 영상 분할, 오디오 추출
- **동영상 편집** (09:50 - 10:40): Whisper API 자막 생성 및 무음 구간 제거
- **마무리 작업** (10:40 - 10:45): 파트 병합, 결과 확인

---

## 실험 결과

| 항목 | 원본 | 편집 후 | 변화 |
|------|------|---------|------|
| 길이 | 92.2분 (5,534초) | 81.0분 (4,862초) | **-12.1%** |
| 크기 | 364MB | 318MB | -12.6% |
| 무음 구간 | 266개 | - | 11.2분 제거 |
| 세그먼트 | 269개 | - | 269개 유지 |

- **실험 성공**: AI4PKM Skill로 무음 제거 완료
- **무음 기준**: 단어 사이 간격 1.0초 이상 (`--pause-threshold 1.0`)
- **필러 단어**: 제거 안 함 (`--no-fillers` 옵션 사용)

---

## 파트별 결과

영상이 92분으로 OpenAI API 25MB 제한을 초과하여 3개 파트로 분할 처리함.

| 파트 | 시간 범위 | 무음 구간 | 세그먼트 | 단축 비율 |
|------|----------|----------|----------|----------|
| Part 1 | 0-30분 | 118개 | 119개 | **18.2%** |
| Part 2 | 30-60분 | 62개 | 63개 | **8.8%** |
| Part 3 | 60-92분 | 86개 | 87개 | **9.8%** |
| **합계** | 92분 | **266개** | **269개** | **12.1%** |

---

## video-editor.py vs AI4PKM Skill 비교

동일한 영상(`original.mkv`, 92분)을 두 방식으로 처리한 결과 비교:

| 항목 | video-editor.py (01-23) | AI4PKM Skill (01-24) |
|------|------------------------|---------------------|
| **무음 감지 방식** | 음량 기반 (pydub, -40dB) | 단어 타임스탬프 (Whisper API) |
| **무음 기준** | 500ms 이상 | 1.0초 이상 |
| **감지된 무음** | 1,730개 | 266개 |
| **단축 비율** | 32.5% | 12.1% |
| **편집 후 길이** | 62.3분 | 81.0분 |
| **비용** | 무료 | ~$0.55 (API) |
| **처리 시간** | ~3시간 | ~1시간 |

**분석**:
- video-editor.py는 짧은 무음(500ms)도 감지하여 더 공격적으로 제거
- AI4PKM은 단어 사이 간격만 감지하므로 더 보수적
- 같은 threshold(1초)로 설정하면 유사한 결과가 예상됨

---

## 발생한 이슈 및 해결

### Issue 1: OpenAI API 파일 크기 제한 (25MB)

**증상**:
```
Error code: 413 - Maximum content size limit (26214400) exceeded
```

**원인**:
- 92분 영상의 오디오 파일이 25MB 제한 초과

**해결**:
- 영상을 30분씩 3개 파트로 분할
- 각 파트별 오디오를 80kbps로 압축 (18-19MB)
- 각각 Whisper API로 처리 후 최종 병합

### Issue 2: Windows 콘솔 이모지 출력 오류

**증상**:
```
UnicodeEncodeError: 'charmap' codec can't encode character '\u2705'
```

**원인**:
- 성공 메시지의 체크마크 이모지(✅)가 Windows cp1252 인코딩에서 지원 안 됨

**해결**:
- 편집은 정상 완료됨 (출력 메시지만 오류)
- 향후 스크립트에서 이모지 제거 필요

---

## 사용된 스크립트 및 Skill

| 파일 | 용도 | 비고 |
|------|------|------|
| `transcribe_video.py` | Whisper API 자막 생성 | 단어별 타임스탬프 추출 |
| `edit_video_remove_pauses.py` | 무음/필러 제거 | `--no-fillers` 옵션 사용 |

---

## 워크플로우 요약

```
1. 영상 분할 (30분씩 3개)
   ffmpeg -i original.mkv -t 1800 -c copy part1.mkv
   ffmpeg -i original.mkv -ss 1800 -t 1800 -c copy part2.mkv
   ffmpeg -i original.mkv -ss 3600 -c copy part3.mkv

2. 오디오 추출 (80kbps, 25MB 이하)
   ffmpeg -i part1.mkv -vn -acodec aac -ab 80k part1_audio.m4a

3. Whisper API 자막 생성
   python transcribe_video.py part1.mkv --language ko

4. 무음 제거 (필러 단어 제외)
   python edit_video_remove_pauses.py part1.mkv --no-fillers

5. 최종 병합
   ffmpeg -f concat -i concat_list.txt -c copy original_edited_AI4PKM.mkv
```

---

## 비용 분석

| 항목 | 단가 | 수량 | 비용 |
|------|------|------|------|
| Whisper API | $0.006/분 | 92분 | **~$0.55** |

---

## 학습 포인트

1. **OpenAI Whisper API 제한**:
   - 파일 크기 25MB 제한
   - 대용량 영상은 분할 처리 필요

2. **무음 감지 방식 차이**:
   - 음량 기반 (pydub): 더 많은 무음 감지, 공격적 편집
   - 단어 타임스탬프 (Whisper): 보수적 편집, 자연스러운 결과

3. **파라미터 비교**:
   - `--min-silence` (video-editor.py): 음량이 threshold 이하인 최소 구간 길이 (ms)
   - `--pause-threshold` (AI4PKM): 단어 사이 간격 최소 길이 (초)

4. **비용 vs 정확도**:
   - video-editor.py: 무료, 음량 기반으로 단순하지만 효과적
   - AI4PKM: 유료($0.006/분), 단어 레벨 정밀도, 필러 단어 제거 가능

---

## 생성된 파일

```
C:\Users\dougg\Videos\Youtube\2026\PKM_Project\20260122_with_Jin_Prompt_Skills\AI4PKM_skill\
├── original.mkv                    (원본, 364MB)
├── original_edited_AI4PKM.mkv      (편집 완료, 318MB)
├── part1.mkv, part2.mkv, part3.mkv (분할 파일)
├── part1_edited.mkv, part2_edited.mkv, part3_edited.mkv (편집된 파트)
├── part1 - transcript.json, etc.   (자막 파일)
└── concat_list.txt                 (병합용 리스트)
```

---

## 다음 작업

- [ ] video-editor.py에 `--min-silence 1000` 옵션으로 동일 조건 테스트
- [ ] AI4PKM Skill의 필러 단어 제거 기능 테스트 (`--no-fillers` 제거)
- [ ] 두 방식의 결과물 품질 비교 (실제 시청 후 평가)
- [ ] 임시 파일 정리 스크립트 작성
