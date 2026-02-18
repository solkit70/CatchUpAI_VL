# AI4PKM Video Cleaning Skill 작업일지 (2026-01-25)

**목표**: 긴 영상(1시간 이상) 처리 시 발생하는 오류를 해결하고, 트랜스크립션부터 편집까지의 전체 과정을 단일 명령으로 자동화.

---

## 1. 주요 변경 사항 요약

### 1.1. 자동 청킹(Chunking) 기능 구현
- **`transcribe_video.py`**: OpenAI Whisper API의 25MB 파일 크기 제한으로 인해 긴 영상 트랜스크립션이 실패하는 문제를 해결했습니다. 이제 스크립트는 `--chunk-duration` (기본 20분)을 기준으로 긴 영상의 오디오를 자동으로 분할하고, 각 청크를 개별적으로 API에 전송한 후, 타임스탬프를 재조정하여 하나의 완전한 트랜스크립트 파일로 병합합니다.
- **`edit_video_remove_pauses.py`**: 긴 영상 편집 시 수많은 세그먼트 파일 생성으로 인한 성능 저하 및 오류를 방지하기 위해, 이 스크립트에도 자동 청킹 기능을 추가했습니다. `--chunk-duration` (기본 30분)을 기준으로 비디오를 분할하여 각 청크별로 무음 구간을 편집하고, 마지막에 편집된 비디오 청크들을 병합하여 최종 결과물을 생성합니다.

### 1.2. 파이프라인 통합 (`--transcribe` 플래그)
- `edit_video_remove_pauses.py` 스크립트에 `--transcribe` 라는 새로운 명령줄 인수를 추가했습니다.
- 사용자가 이 플래그를 포함하여 스크립트를 실행하면, 스크립트는 먼저 트랜스크립트 JSON 파일의 존재 여부를 확인합니다.
- 파일이 없으면, **자동으로 `transcribe_video.py`의 로직을 호출하여 트랜스크립션을 먼저 수행**합니다.
- 트랜스크립션이 완료되면, 생성된 파일을 사용하여 **중단 없이 바로 영상 편집 단계로 진행**합니다.
- 이로써 사용자는 트랜스크립션과 편집을 별도로 실행할 필요 없이, 단 한 번의 명령으로 전체 워크플로우를 완료할 수 있게 되었습니다.

### 1.3. 문서 업데이트 (v3.0)
- `README.md`와 `SKILL.md` 파일을 수정하여 위에서 설명한 새로운 기능(통합 파이프라인, 자동 청킹, 신규 인수 등)을 상세히 반영했습니다.
- 특히 `SKILL.md`의 기술 세부사항을 수정하여, 기존의 MoviePy 기반이 아닌 **고성능 순수 FFmpeg 기반 편집 방식**임을 명시하고, 버전 기록을 **v3.0**으로 업데이트했습니다.
- `20260124_video_edit_skill_comparison.md` 비교 문서에서 AI4PKM 스킬의 단점으로 지적되었던 "긴 영상 처리 문제"가 v3.0에서 해결되었음을 명확히 기재하여 문서를 최신 상태로 유지했습니다.

---

## 2. 최종 실행 결과 (로컬 터미널)

아래는 약 92분 길이의 영상을 대상으로, 청킹 기능이 포함된 통합 파이프라인을 실행했을 때의 터미널 로그입니다. 트랜스크립션과 편집이 모두 청크 단위로 성공적으로 처리되었음을 확인할 수 있습니다.

- **실행 명령어**:
```powershell
python "c:\AI_study\2026\CatchUpAI_VL\Topics\Claude-Skills\04-Skill-C-Video-Edit\AI4PKM_Video_Cleaning\edit_video_remove_pauses.py" "C:\Users\dougg\Videos\Youtube\2026\PKM_Project\20260122_with_Jin_Prompt_Skills\AI4PKM_skill_300\original.mkv" --transcribe --no-fillers --pause-threshold 0.3 --chunk-duration 600
```

- **실행 로그**:
```
============================================================
Transcript not found. Running transcription for 'original.mkv'...
============================================================
Total video duration: 01:32:14.361
Video is long, processing in chunks of 1200s...

--- Processing Chunk 1/5 (00:00:00.000) ---
Transcribing audio with Whisper API (language: ko)...
Transcription successful for chunk.

--- Processing Chunk 2/5 (00:20:00.000) ---
Transcribing audio with Whisper API (language: ko)...
Transcription successful for chunk.

--- Processing Chunk 3/5 (00:40:00.000) ---
Transcribing audio with Whisper API (language: ko)...
Transcription successful for chunk.

--- Processing Chunk 4/5 (01:00:00.000) ---
Transcribing audio with Whisper API (language: ko)...
Transcription successful for chunk.

--- Processing Chunk 5/5 (01:20:00.000) ---
Transcribing audio with Whisper API (language: ko)...
Transcription successful for chunk.

Cleaned up temporary audio chunks.

Saving combined transcript to C:\Users\dougg\Videos\Youtube\2026\PKM_Project\20260122_with_Jin_Prompt_Skills\AI4PKM_skill_300\original - transcript.json...
Creating formatted transcript...

Transcription complete!
  JSON: C:\Users\dougg\Videos\Youtube\2026\PKM_Project\20260122_with_Jin_Prompt_Skills\AI4PKM_skill_300\original - transcript.json
  Markdown: C:\Users\dougg\Videos\Youtube\2026\PKM_Project\20260122_with_Jin_Prompt_Skills\AI4PKM_skill_300\original - transcript.md
  Word timings: C:\Users\dougg\Videos\Youtube\2026\PKM_Project\20260122_with_Jin_Prompt_Skills\AI4PKM_skill_300\original - word_timings.txt

Transcription complete. Proceeding to video editing...

============================================================
Starting video editing process...
============================================================
Total video duration: 01:32:14.361

Video is longer than 600s, processing in chunks...

Splitting chunk 1/10...

--- Processing Chunk 1 (00:00:00.000) ---
Editing chunk 1...
Chunk 1 processed successfully.

Splitting chunk 2/10...

--- Processing Chunk 2 (00:10:00.000) ---
Editing chunk 2...
Chunk 2 processed successfully.

Splitting chunk 3/10...

--- Processing Chunk 3 (00:20:00.000) ---
Editing chunk 3...
Chunk 3 processed successfully.

Splitting chunk 4/10...

--- Processing Chunk 4 (00:30:00.000) ---
Editing chunk 4...
Chunk 4 processed successfully.

Splitting chunk 5/10...

--- Processing Chunk 5 (00:40:00.000) ---
Editing chunk 5...
Chunk 5 processed successfully.

Splitting chunk 6/10...

--- Processing Chunk 6 (00:50:00.000) ---
Editing chunk 6...
Chunk 6 processed successfully.

Splitting chunk 7/10...

--- Processing Chunk 7 (01:00:00.000) ---
Editing chunk 7...
Chunk 7 processed successfully.

Splitting chunk 8/10...

--- Processing Chunk 8 (01:10:00.000) ---
Editing chunk 8...
Chunk 8 processed successfully.

Splitting chunk 9/10...

--- Processing Chunk 9 (01:20:00.000) ---
Editing chunk 9...
Chunk 9 processed successfully.

Splitting chunk 10/10...

--- Processing Chunk 10 (01:30:00.000) ---
Editing chunk 10...
Chunk 10 processed successfully.

Concatenating 10 edited chunks...

--- FINAL REPORT (CHUNKED) ---
Original duration: 01:32:14.361
Edited duration:   01:16:34.737
Time saved:        00:15:39.624 (17.0%)

✅ Success! Final video saved to: C:\Users\dougg\Videos\Youtube\2026\PKM_Project\20260122_with_Jin_Prompt_Skills\AI4PKM_skill_300\original_edited.mkv
Cleaned up chunk temporary directory.
```
