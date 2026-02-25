// slideData.ts — Clearly App Introduction Video (English) slide config
// audio durations measured with ffprobe, total = 828.336s = 24849 frames @ 30fps

export const FPS = 30;
export const FADE_FRAMES = 15; // 0.5s fade transition

export type SlideType = "title" | "content" | "content-screenshot" | "outro";

export interface SlideConfig {
  audioIndex: number;
  slideNum: number;
  type: SlideType;
  durationSec: number;
  screenshot: string | null;
}

export const SLIDE_DATA: SlideConfig[] = [
  { audioIndex: 0,  slideNum: 1,  type: "title",              durationSec: 27.960, screenshot: null },
  { audioIndex: 1,  slideNum: 2,  type: "content",            durationSec: 19.704, screenshot: null },
  { audioIndex: 2,  slideNum: 3,  type: "content",            durationSec: 24.768, screenshot: null },
  { audioIndex: 3,  slideNum: 4,  type: "content-screenshot", durationSec: 23.520, screenshot: "clearly-main_before_login.png" },
  { audioIndex: 4,  slideNum: 5,  type: "content",            durationSec: 23.664, screenshot: null },
  { audioIndex: 5,  slideNum: 6,  type: "content",            durationSec: 32.568, screenshot: null },
  { audioIndex: 6,  slideNum: 7,  type: "content",            durationSec: 27.216, screenshot: null },
  { audioIndex: 7,  slideNum: 8,  type: "content",            durationSec: 32.712, screenshot: null },
  { audioIndex: 8,  slideNum: 9,  type: "content-screenshot", durationSec: 44.856, screenshot: "clearly-main.png" },
  { audioIndex: 9,  slideNum: 10, type: "content",            durationSec: 33.648, screenshot: null },
  { audioIndex: 10, slideNum: 11, type: "content",            durationSec: 30.768, screenshot: null },
  { audioIndex: 11, slideNum: 12, type: "content",            durationSec: 28.512, screenshot: null },
  { audioIndex: 12, slideNum: 13, type: "content-screenshot", durationSec: 29.856, screenshot: "project-create.png" },
  { audioIndex: 13, slideNum: 14, type: "content-screenshot", durationSec: 36.360, screenshot: "brd-wizard.png" },
  { audioIndex: 14, slideNum: 15, type: "content",            durationSec: 28.752, screenshot: null },
  { audioIndex: 15, slideNum: 16, type: "content",            durationSec: 43.704, screenshot: null },
  { audioIndex: 16, slideNum: 17, type: "content-screenshot", durationSec: 37.704, screenshot: "brd-result.png" },
  { audioIndex: 17, slideNum: 18, type: "content-screenshot", durationSec: 31.968, screenshot: "prd-result.png" },
  { audioIndex: 18, slideNum: 19, type: "content-screenshot", durationSec: 39.960, screenshot: "output-tool.png" },
  { audioIndex: 19, slideNum: 20, type: "content",            durationSec: 28.248, screenshot: null },
  { audioIndex: 20, slideNum: 21, type: "content",            durationSec: 29.112, screenshot: null },
  { audioIndex: 21, slideNum: 22, type: "content",            durationSec: 24.864, screenshot: null },
  { audioIndex: 22, slideNum: 23, type: "content",            durationSec: 33.216, screenshot: null },
  { audioIndex: 23, slideNum: 24, type: "content-screenshot", durationSec: 27.456, screenshot: "homepage.png" },
  { audioIndex: 24, slideNum: 25, type: "content",            durationSec: 35.760, screenshot: null },
  { audioIndex: 25, slideNum: 26, type: "content",            durationSec: 26.064, screenshot: null },
  { audioIndex: 26, slideNum: 27, type: "outro",              durationSec: 25.416, screenshot: null },
];

/** Total frames (828.336 * 30 ≈ 24849) */
export const TOTAL_FRAMES = SLIDE_DATA.reduce(
  (sum, s) => sum + Math.round(s.durationSec * FPS),
  0
);
