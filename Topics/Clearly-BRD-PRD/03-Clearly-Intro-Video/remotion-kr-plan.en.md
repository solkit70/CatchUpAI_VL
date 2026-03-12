# Remotion Production Plan: Clearly App Intro Video (Korean)

> **[← Korean Version](remotion-kr-plan.md)**

**Created**: 2026-02-24
**Goal**: Remake the existing FFmpeg-based `clearly-intro-kr.mp4` with Remotion for improved motion graphics quality

---

## Background

The existing `clearly-intro-kr.mp4` (16:28, 38MB) was produced using an FFmpeg pipeline:
- 27 Gemini JPEGs + 27 TTS MP3s → static slideshow
- Scene transitions: hard cuts (no transition effects)

Using Remotion (React-based video framework) enables:
- Smooth crossfade/slide scene transitions
- Motion graphics on title, section, and outro slides
- Full reuse of existing audio (MP3) assets (no extra cost)
- Auto-generation of animated components using Remotion Skills (AI)

---

## Existing Assets (Reusable)

| Asset | Location | Count | Reuse |
|-------|----------|-------|-------|
| Korean MP3 audio | `audio-kr/slide_0.mp3` ~ `slide_26.mp3` | 27 files | ✅ 100% reuse |
| Gemini slide images | `slides-gemini-kr/1.jpeg` ~ `27.jpeg` | 27 files | ✅ Reuse as backgrounds |
| Real screenshots | `_files_/*.png` | 8 files | ✅ Overlay on specific slides |
| Remotion project | `Remotion-VideoCreation/my-first-video/` | existing | ✅ Extend (no npm install needed) |
| Remotion Skills rules | `.agents/skills/remotion-best-practices/` | 27 rules | ✅ Use for AI component generation |

---

## Implementation Strategy

**Add a new Composition to the existing `my-first-video/` project**
- Reason: Start immediately without reinstalling node_modules; Skills rules remain usable

### Slide Component Strategy

27 slides handled with 3 component types:

| Component Type | Slides | Approach |
|---------------|--------|----------|
| **TitleSlide** | Slide 1 (main title) | Remotion Skills — motion graphics |
| **SectionDivider** | Slides 5, 9, 13, 20, 25 (section dividers) | Remotion Skills — slide-in |
| **ContentSlide** | Remaining general slides | Gemini JPEG + audio + fade-in |
| **OutroSlide** | Slide 27 (closing) | Remotion Skills — subscribe CTA animation |

---

## Implementation Steps

### Step 1: Pre-calculate Audio Durations
```bash
# Extract exact playback duration (seconds) for each MP3 file
# Use mutagen or ffprobe
# → Hardcode into slideData.ts
```

### Step 2: Copy Assets
```bash
# Copy to my-first-video/public/clearly-kr/ folder
audio/slide_0.mp3 ~ slide_26.mp3   (27 MP3 files)
slides/1.jpeg ~ 27.jpeg             (27 JPEG files)
screenshots/*.png                   (8 PNG files)
```

### Step 3: Slide Data Config File
`my-first-video/src/clearly-kr/slideData.ts`
```ts
export const FPS = 30;
export const SLIDE_DATA = [
  { id: 0, type: 'title',   durationSec: XX.X, screenshot: null },
  { id: 1, type: 'content', durationSec: XX.X, screenshot: null },
  // ...all 27 entries
];
```

### Step 4: Create Core Components

| File | How to Create | Content |
|------|--------------|---------|
| `SlideWrapper.tsx` | Manual | Audio playback + image + fade transition |
| `TitleSlide.tsx` | Remotion Skills | Gradient background + text spring animation |
| `SectionDivider.tsx` | Remotion Skills | Section number + title slide-in |
| `ContentSlide.tsx` | Manual | Gemini JPEG background |
| `OutroSlide.tsx` | Remotion Skills | Subscribe button pulse + link display |

### Step 5: Main Composition
`my-first-video/src/clearly-kr/ClearlyIntroKr.tsx`
```tsx
// Full video composed of 27 Series.Sequences
<Series>
  {SLIDE_DATA.map((slide) => (
    <Series.Sequence durationInFrames={Math.round(slide.durationSec * FPS)}>
      <SlideWrapper {...slide} />
    </Series.Sequence>
  ))}
</Series>
```

### Step 6: Register Composition in Root.tsx
```tsx
<Composition id="ClearlyIntroKr" component={ClearlyIntroKr}
  durationInFrames={totalFrames} fps={30} width={1920} height={1080} />
```

### Step 7: Preview & Render
```bash
cd Topics/Remotion-VideoCreation/my-first-video
npx remotion studio                    # Preview in Studio
npx remotion render ClearlyIntroKr \
  out/clearly-intro-kr-remotion.mp4 \
  --video-bitrate 8M
```

---

## Final File Structure

```
my-first-video/
├── src/
│   ├── Root.tsx                              # ClearlyIntroKr added
│   └── clearly-kr/
│       ├── ClearlyIntroKr.tsx               # Main Composition
│       ├── slideData.ts                     # Slide config + audio durations
│       ├── SlideWrapper.tsx                 # Common wrapper
│       ├── TitleSlide.tsx                   # Title (Skills)
│       ├── SectionDivider.tsx               # Section divider (Skills)
│       ├── ContentSlide.tsx                 # General slide
│       └── OutroSlide.tsx                   # Outro (Skills)
└── public/clearly-kr/
    ├── audio/slide_0.mp3 ~ slide_26.mp3     # 27 MP3 files
    ├── slides/1.jpeg ~ 27.jpeg              # 27 JPEG files
    └── screenshots/                         # 8 PNG files

Output: my-first-video/out/clearly-intro-kr-remotion.mp4
```

---

## Expected Quality Improvements

| Item | Existing (FFmpeg) | Remotion Version |
|------|-------------------|-----------------|
| Scene transitions | Hard cut | Crossfade (0.5s) |
| Title slide | Static image | Spring animation |
| Section dividers | Static image | Slide-in + emphasis effect |
| Outro | Static image | Subscribe button pulse animation |
| Audio | Same (TTS) | Same (reused) |
| Total length | 16:28 | Same (~16:28) |
| Resolution | 1920×1080 | 1920×1080 |

---

## Reference Files

| File | Path | Purpose |
|------|------|---------|
| Existing final video integration code | `my-first-video/src/VibeLearnIntro.tsx` | Series pattern reference |
| Explanation scene code | `my-first-video/src/ExplanationScene.tsx` | Stagger animation reference |
| Audio rules | `.agents/skills/.../rules/audio.md` | Audio sync patterns |
| Timing rules | `.agents/skills/.../rules/timing.md` | spring/interpolate settings |
| Korean script | `clearly-intro-script-kr.md` | Slide content reference |
| Slides MD | `clearly-intro-script-kr - slides.md` | Section structure |

---

**Created**: 2026-02-24
**Topic**: Clearly-BRD-PRD / M3
