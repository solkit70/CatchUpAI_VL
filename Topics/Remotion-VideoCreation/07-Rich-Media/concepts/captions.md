# 자동 자막 — @remotion/captions + Whisper

## 개요

`@remotion/captions`는 오디오에서 자동으로 자막을 생성하고,
TikTok 스타일의 단어 하이라이트 자막을 Remotion 영상에 표시합니다.

YouTube 쇼츠, TikTok, Reels 스타일의 동적 자막에 특히 유용합니다.

---

## 전체 워크플로우

```
오디오 파일 (MP3/WAV)
       ↓
Whisper 자동 전사 (로컬 or API)
       ↓
captions.json (타임스탬프 포함)
       ↓
@remotion/captions으로 페이지 그룹핑
       ↓
단어별 하이라이트 자막 렌더링
```

---

## 설치

```bash
npx remotion add @remotion/captions
npx remotion add @remotion/install-whisper-cpp  # 로컬 Whisper 사용 시
```

---

## Step 1: Whisper로 자막 생성

### 옵션 A: OpenAI Whisper API (간단)

```python
# transcribe.py
import openai, json
from pathlib import Path

client = openai.OpenAI()

def transcribe(audio_path: str, output_path: str):
    with open(audio_path, 'rb') as f:
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            response_format="verbose_json",
            timestamp_granularities=["word"],
        )
    # word-level 타임스탬프를 Caption 포맷으로 변환
    captions = [
        {
            "text": word.word,
            "startMs": int(word.start * 1000),
            "endMs": int(word.end * 1000),
            "timestampMs": int(word.start * 1000),
            "confidence": None,
        }
        for word in response.words
    ]
    Path(output_path).write_text(json.dumps(captions, ensure_ascii=False, indent=2))

transcribe("public/audio/slide_0.mp3", "public/captions/slide_0.json")
```

### 옵션 B: 로컬 Whisper.cpp (무료, 오프라인)

```bash
# 설치 (최초 1회)
npx remotion install-whisper-cpp
npx remotion download-whisper-model medium

# 실행
npx remotion transcribe public/audio/slide_0.mp3 \
  --model=medium \
  --output=public/captions/slide_0.json
```

---

## Step 2: captions.json 포맷

```json
[
  { "text": " 안녕하세요", "startMs": 0,    "endMs": 480,  "timestampMs": 0 },
  { "text": " AI",         "startMs": 480,  "endMs": 720,  "timestampMs": 480 },
  { "text": " in",         "startMs": 720,  "endMs": 860,  "timestampMs": 720 },
  { "text": " Action",     "startMs": 860,  "endMs": 1200, "timestampMs": 860 }
]
```

> 각 토큰의 `text` 앞에 공백이 있어야 함 (whitespace-sensitive)

---

## Step 3: TikTok 스타일 자막 컴포넌트

```tsx
import { useState, useEffect, useCallback } from 'react';
import { AbsoluteFill, staticFile, useDelayRender, continueRender, cancelRender,
         Sequence, useVideoConfig } from 'remotion';
import { createTikTokStyleCaptions } from '@remotion/captions';
import type { Caption, TikTokPage } from '@remotion/captions';

const SWITCH_EVERY_MS = 1200; // 페이지 전환 간격
const HIGHLIGHT_COLOR = '#39E508'; // 현재 단어 하이라이트 색

// 단일 캡션 페이지 컴포넌트
const CaptionPage: React.FC<{ page: TikTokPage }> = ({ page }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentMs = page.startMs + (frame / fps) * 1000;

  return (
    <div style={{
      position: 'absolute', bottom: 120, left: 0, right: 0,
      display: 'flex', flexWrap: 'wrap', justifyContent: 'center',
      padding: '0 80px', gap: 8,
    }}>
      {page.tokens.map((token) => {
        const isActive = token.fromMs <= currentMs && token.toMs > currentMs;
        return (
          <span
            key={token.fromMs}
            style={{
              fontSize: 52,
              fontWeight: 'bold',
              color: isActive ? HIGHLIGHT_COLOR : 'white',
              textShadow: '0 2px 8px rgba(0,0,0,0.8)',
              whiteSpace: 'pre',
            }}
          >
            {token.text}
          </span>
        );
      })}
    </div>
  );
};

// 자막 전체 컴포넌트
export const CaptionedSlide: React.FC<{
  children: React.ReactNode;
  captionSrc: string;
}> = ({ children, captionSrc }) => {
  const [captions, setCaptions] = useState<Caption[] | null>(null);
  const [handle] = useState(() => useDelayRender('Loading captions'));
  const { fps } = useVideoConfig();

  const load = useCallback(async () => {
    try {
      const res = await fetch(staticFile(captionSrc));
      setCaptions(await res.json());
      continueRender(handle);
    } catch (e) {
      cancelRender(e);
    }
  }, [handle, captionSrc]);

  useEffect(() => { load(); }, [load]);

  if (!captions) return <>{children}</>;

  const { pages } = createTikTokStyleCaptions({
    captions,
    combineTokensWithinMilliseconds: SWITCH_EVERY_MS,
  });

  return (
    <AbsoluteFill>
      {children}
      {pages.map((page, i) => {
        const nextPage = pages[i + 1] ?? null;
        const startFrame = (page.startMs / 1000) * fps;
        const endFrame = Math.min(
          nextPage ? (nextPage.startMs / 1000) * fps : Infinity,
          startFrame + (SWITCH_EVERY_MS / 1000) * fps,
        );
        const dur = endFrame - startFrame;
        if (dur <= 0) return null;

        return (
          <Sequence key={i} from={startFrame} durationInFrames={dur}>
            <CaptionPage page={page} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
```

---

## Step 4: 슬라이드에 적용

```tsx
// 기존 슬라이드를 CaptionedSlide로 감싸기
export const Live7Slide: React.FC = () => (
  <CaptionedSlide captionSrc="live7-highlight/captions/slide_0.json">
    <BulletSlide data={slideData} durationInFrames={612} />
  </CaptionedSlide>
);
```

---

## 이 프로젝트에서의 활용 방안

현재 프로젝트에서 gen_audio.py로 TTS MP3를 생성하고 있으므로,
같은 Python 스크립트에 Whisper 전사 단계를 추가하면 됩니다:

```python
# gen_audio.py에 추가
def transcribe_audio(audio_path: Path, output_path: Path, api_key: str):
    client = openai.OpenAI(api_key=api_key)
    with open(audio_path, 'rb') as f:
        response = client.audio.transcriptions.create(
            model="whisper-1", file=f,
            response_format="verbose_json",
            timestamp_granularities=["word"],
        )
    captions = [
        {"text": w.word, "startMs": int(w.start * 1000),
         "endMs": int(w.end * 1000), "timestampMs": int(w.start * 1000)}
        for w in response.words
    ]
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(captions, ensure_ascii=False, indent=2))
```

> 한국어 자막: `whisper-1` 모델은 한국어를 지원하므로 별도 언어 설정 없이 사용 가능.

---

## ✨ 4.0.452 신규: @remotion/elevenlabs

ElevenLabs TTS 출력을 `@remotion/captions` 형식으로 자동 변환하는 공식 패키지입니다.
ElevenLabs를 TTS로 사용할 때 별도 Whisper 전사 없이 단어 타임스탬프를 바로 얻을 수 있습니다.

### 설치

```bash
npx remotion add @remotion/elevenlabs
```

### 사용법

```tsx
import { getElevenLabsCaptions } from '@remotion/elevenlabs';

// ElevenLabs API 응답(alignment 데이터)을 Caption[] 형식으로 변환
const captions = getElevenLabsCaptions(elevenLabsAlignment);

// 이후 @remotion/captions의 createTikTokStyleCaptions()에 그대로 전달
const { pages } = createTikTokStyleCaptions({
  captions,
  combineTokensWithinMilliseconds: 1200,
});
```

### ElevenLabs API에서 alignment 데이터 받기

```python
# elevenlabs_tts.py
import requests, json
from pathlib import Path

def generate_with_alignment(text: str, voice_id: str, api_key: str, output_path: Path):
    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/with-timestamps",
        headers={"xi-api-key": api_key},
        json={
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
        },
    )
    data = response.json()
    # audio_base64: data["audio_base64"]
    # alignment: data["alignment"] ← 단어 타임스탬프 포함

    output_path.write_bytes(__import__('base64').b64decode(data["audio_base64"]))

    # alignment를 captions.json으로 저장
    alignment_path = output_path.with_suffix('.alignment.json')
    alignment_path.write_text(json.dumps(data["alignment"]))
    return data["alignment"]
```

### TTS 서비스 비교

| 서비스 | 패키지 | 한국어 | 단어 타임스탬프 | 비용 |
|--------|--------|--------|----------------|------|
| OpenAI TTS + Whisper | 직접 구현 | ✅ | Whisper 전사 필요 | TTS $.015/1K + Whisper $.006/min |
| **ElevenLabs** | `@remotion/elevenlabs` | ✅ | **자동 포함** | $0.30/1K chars |
| 로컬 Whisper.cpp | `@remotion/install-whisper-cpp` | ✅ | 무료 | 무료 (로컬 처리) |

> **권장**: 한국어 콘텐츠는 OpenAI TTS + Whisper 조합. 영어 고품질 나레이션은 ElevenLabs.
