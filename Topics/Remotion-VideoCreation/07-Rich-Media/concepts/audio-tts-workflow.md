# TTS 오디오 + Remotion 동기화 워크플로우

## 개요

이 프로젝트에서 사용하는 **TTS 기반 나레이션 영상 제작** 표준 패턴입니다.
OpenAI TTS API로 MP3를 생성하고, ffmpeg로 속도를 조절한 뒤, 오디오 길이에 맞춰
Remotion 슬라이드 Duration을 결정합니다.

---

## 전체 워크플로우

```
1. 대본 작성 (data.ts + slides.md)
       ↓
2. gen_audio.py 실행 → TTS MP3 생성
       ↓
3. ffmpeg 1.03x 속도 조정 → 길이 단축
       ↓
4. ffprobe 길이 측정 → durations.json
       ↓
5. data.ts SLIDE_DURATIONS 업데이트
       ↓
6. npx remotion render → MP4 출력
```

---

## Step 1: 오디오 생성 스크립트 구조 (gen_audio.py)

```python
import os, json, subprocess, urllib.request
from pathlib import Path

MODEL = "tts-1"
SPEEDUP = 1.03
OUTPUT_DIR = Path(__file__).parent / "audio"
OUTPUT_DIR.mkdir(exist_ok=True)

# (파일명, slide_id, voice, 나레이션_텍스트)
NARRATIONS = [
    ("slide_0", 0, "nova",   "안녕하세요, AI in Action입니다..."),
    ("slide_2", 2, "shimmer", "이번 방송에서는..."),
]

def generate_audio(text, voice, output_path, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = json.dumps({"model": MODEL, "voice": voice, "input": text}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech",
        data=payload, headers=headers, method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        output_path.write_bytes(resp.read())

def speedup_audio(path):
    tmp = path.with_suffix(".tmp.mp3")
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(path), "-filter:a", f"atempo={SPEEDUP}", str(tmp)],
        capture_output=True
    )
    tmp.replace(path)

def measure_duration(path):
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True
    )
    return round(float(result.stdout.strip()), 2)
```

### OpenAI TTS Voice 옵션

| Voice | 특징 | 적합한 용도 |
|-------|------|-------------|
| `nova` | 밝고 친근함 | 일반 나레이션, 뉴스 요약 |
| `shimmer` | 따뜻하고 부드러움 | 커뮤니티 소식, 이벤트 안내 |
| `onyx` | 깊고 권위있음 | 인사이트, 핵심 발표 |
| `alloy` | 중성적, 명료함 | 기술 설명, 튜토리얼 |
| `echo` | 남성적, 안정적 | 제품 소개 |
| `fable` | 이야기꾼 스타일 | 스토리텔링 |

---

## Step 2: Remotion에서 오디오 재생

```tsx
import { Audio, Sequence, staticFile } from 'remotion';
import { AUDIO_HEAD_PAD_FRAMES } from './data';

// AUDIO_HEAD_PAD_FRAMES = Math.ceil(0.8 * FPS)  ← 0.8초 헤드 패딩
// 슬라이드 전환 애니메이션이 끝나고 오디오 시작

export const BulletSlide: React.FC<Props> = ({ data }) => {
  return (
    <AbsoluteFill>
      {/* 슬라이드 콘텐츠 */}
      <SlideContent data={data} />

      {/* 오디오: 헤드 패딩 후 재생 */}
      {data.audioSrc && (
        <Sequence from={AUDIO_HEAD_PAD_FRAMES}>
          <Audio src={staticFile(data.audioSrc)} />
        </Sequence>
      )}
    </AbsoluteFill>
  );
};
```

### ✨ 4.0.452 신규: Audio에 from / durationInFrames 직접 지정

`<Sequence>`로 감싸지 않아도 `<Audio>` 자체에 `from`과 `durationInFrames`를 전달할 수 있습니다:

```tsx
// 이전 방식 (여전히 동작)
<Sequence from={AUDIO_HEAD_PAD_FRAMES}>
  <Audio src={staticFile(data.audioSrc)} />
</Sequence>

// 신규 방식 (4.0.452+) — Sequence 없이 동일 효과
<Audio
  src={staticFile(data.audioSrc)}
  from={AUDIO_HEAD_PAD_FRAMES}
  durationInFrames={totalDuration - AUDIO_HEAD_PAD_FRAMES}
/>
```

> **권장**: 기존 프로젝트는 `Sequence` 방식을 유지. 신규 컴포넌트에서는 `from` prop 방식이 더 간결합니다.

### ✨ 4.0.456: `<Audio>` — True Sequence 동작

v4.0.456부터 `<Audio>`도 `<Video>`와 함께 **true Sequence**로 동작합니다.
`from` prop이 부모 Sequence의 상대 프레임을 기준으로 계산됩니다.

```tsx
// 4.0.456+: Sequence 안에서 from은 상대 오프셋
<Sequence from={90}>
  <Audio
    src={staticFile(data.audioSrc)}
    from={24}   // 부모 Sequence 기준 24프레임 후 = 컴포지션 114프레임
  />
</Sequence>
```

> 기존에 최상위에서 `<Audio from={...}>`만 사용하는 경우 동작 변경 없음.

### ✨ 4.0.453: Player `initialVolume` prop

`<Player>` 컴포넌트에 초기 볼륨을 지정할 수 있습니다:

```tsx
import { Player } from '@remotion/player';

<Player
  component={MyComposition}
  initialVolume={0.5}   // 0~1 사이 초기 볼륨 (기본값 1)
  durationInFrames={300}
  fps={30}
  compositionWidth={1920}
  compositionHeight={1080}
/>
```

> 웹 임베드 플레이어에서 자동재생 정책 우회용으로 유용합니다.

### ✨ 4.0.453: 오디오 재생 순서 보장

여러 `<Audio>` 태그가 동시에 시작할 때 재생 순서가 일관되게 보장됩니다.
이전 버전에서 타이밍이 미세하게 어긋나던 현상이 수정되었습니다.

또한 4.0.455부터 **음소거된 Player는 AudioContext 활성화를 기다리지 않아** 초기 로딩이 빨라졌습니다:

```tsx
// muted 플레이어: AudioContext 대기 없이 즉시 재생 시작
<Player
  component={MyComposition}
  muted
  autoPlay
  ...
/>
```

### 패딩 계산

```
총 슬라이드 Duration = 오디오 길이 + 1.2s 패딩
  = 오디오 길이 + 0.8s 헤드 + 0.4s 테일

헤드 패딩 (0.8s): 전환 애니메이션 완료 후 오디오 시작
테일 패딩 (0.4s): 오디오 종료 후 자연스러운 페이드아웃
```

---

## Step 3: data.ts Duration 구조

```typescript
export const FPS = 30;
export const SEC = (s: number) => Math.ceil(s * FPS);
export const AUDIO_HEAD_PAD_FRAMES = Math.ceil(0.8 * FPS); // 24프레임

// gen_audio.py 실행 후 콘솔 출력값으로 업데이트
export const SLIDE_DURATIONS: Record<number, number> = {
  0:  20.4,  // slide_0.mp3   (19.21s + 1.2s 패딩)
  1:  8,     // SECTION       (오디오 없음 — 고정값)
  2:  25.9,  // slide_2.mp3   (24.73s + 1.2s 패딩)
  // ...
};
```

gen_audio.py 콘솔 출력 형식:
```
--- Paste into SLIDE_DURATIONS in data.ts ---
  1: 8,   // SECTION (no audio)
  0: 20.4,  // slide_0.mp3  (19.21s + 1.2s padding)
  2: 25.9,  // slide_2.mp3  (24.73s + 1.2s padding)
```

---

## Step 4: 오디오 볼륨 제어

```tsx
import { Audio, interpolate } from 'remotion';

// 페이드인
<Audio
  src={staticFile('audio.mp3')}
  volume={(f) => interpolate(f, [0, 24], [0, 1], { extrapolateRight: 'clamp' })}
/>

// 페이드아웃 (마지막 1초)
<Audio
  src={staticFile('audio.mp3')}
  volume={(f) =>
    interpolate(f, [durationInFrames - 30, durationInFrames], [1, 0], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
    })
  }
/>
```

---

## Step 5: 배경음악 레이어링

TTS 나레이션 + 배경음악을 동시에 사용:

```tsx
<AbsoluteFill>
  {/* 배경음악: 낮은 볼륨, 루프 */}
  <Audio
    src={staticFile('bgm/ambient.mp3')}
    volume={0.15}
    loop
  />

  {/* TTS 나레이션: 헤드 패딩 후 풀볼륨 */}
  {data.audioSrc && (
    <Sequence from={AUDIO_HEAD_PAD_FRAMES}>
      <Audio src={staticFile(data.audioSrc)} volume={1.0} />
    </Sequence>
  )}
</AbsoluteFill>
```

---

## calculateMetadata로 자동 Duration 계산 (미래 개선안)

현재는 gen_audio.py로 수동 측정 후 입력하는 방식이지만,
`calculateMetadata`를 사용하면 자동화할 수 있습니다:

```typescript
// data.ts 또는 Root.tsx에서
import { getAudioDurationInSeconds } from '@remotion/media-utils';

const calculateMetadata: CalculateMetadataFunction<Props> = async ({ props }) => {
  const durations = await Promise.all(
    SLIDES
      .filter(s => s.audioSrc)
      .map(async s => ({
        id: s.id,
        dur: await getAudioDurationInSeconds(staticFile(s.audioSrc!)) + 1.2,
      }))
  );
  // durations를 SLIDE_DURATIONS으로 변환하여 props에 주입
};
```

> 현재 프로젝트는 Python 스크립트로 사전 계산하는 방식을 유지 중.
> 오디오 파일이 자주 바뀌는 프로젝트라면 calculateMetadata 방식이 더 편리함.
