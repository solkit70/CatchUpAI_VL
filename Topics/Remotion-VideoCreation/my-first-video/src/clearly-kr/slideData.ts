// slideData.ts — Clearly App 소개 영상 (한국어) 슬라이드 설정
// audio durations measured with ffprobe, total = 988.584s = 29658 frames @ 30fps

export const FPS = 30;
export const FADE_FRAMES = 15; // 0.5초 페이드 전환

export type SlideType = "title" | "content" | "content-screenshot" | "outro";

export interface SlideConfig {
  /** audio-kr/slide_{audioIndex}.mp3 의 인덱스 */
  audioIndex: number;
  /** slides-gemini-kr/{slideNum}.jpeg 의 번호 */
  slideNum: number;
  type: SlideType;
  /** ffprobe로 측정한 정확한 오디오 길이 (초) */
  durationSec: number;
  /** screenshots/ 폴더 내 파일명 (content-screenshot 타입만) */
  screenshot: string | null;
}

export const SLIDE_DATA: SlideConfig[] = [
  { audioIndex: 0,  slideNum: 1,  type: "title",              durationSec: 35.352, screenshot: null },
  { audioIndex: 1,  slideNum: 2,  type: "content",            durationSec: 22.104, screenshot: null },
  { audioIndex: 2,  slideNum: 3,  type: "content",            durationSec: 29.856, screenshot: null },
  { audioIndex: 3,  slideNum: 4,  type: "content-screenshot", durationSec: 26.208, screenshot: "clearly-main_before_login.png" },
  { audioIndex: 4,  slideNum: 5,  type: "content",            durationSec: 30.408, screenshot: null },
  { audioIndex: 5,  slideNum: 6,  type: "content",            durationSec: 39.912, screenshot: null },
  { audioIndex: 6,  slideNum: 7,  type: "content",            durationSec: 39.552, screenshot: null },
  { audioIndex: 7,  slideNum: 8,  type: "content",            durationSec: 37.752, screenshot: null },
  { audioIndex: 8,  slideNum: 9,  type: "content-screenshot", durationSec: 52.200, screenshot: "clearly-main.png" },
  { audioIndex: 9,  slideNum: 10, type: "content",            durationSec: 33.312, screenshot: null },
  { audioIndex: 10, slideNum: 11, type: "content",            durationSec: 37.848, screenshot: null },
  { audioIndex: 11, slideNum: 12, type: "content",            durationSec: 33.120, screenshot: null },
  { audioIndex: 12, slideNum: 13, type: "content-screenshot", durationSec: 37.056, screenshot: "project-create.png" },
  { audioIndex: 13, slideNum: 14, type: "content-screenshot", durationSec: 40.512, screenshot: "brd-wizard.png" },
  { audioIndex: 14, slideNum: 15, type: "content",            durationSec: 36.168, screenshot: null },
  { audioIndex: 15, slideNum: 16, type: "content",            durationSec: 57.768, screenshot: null },
  { audioIndex: 16, slideNum: 17, type: "content-screenshot", durationSec: 41.016, screenshot: "brd-result.png" },
  { audioIndex: 17, slideNum: 18, type: "content-screenshot", durationSec: 34.560, screenshot: "prd-result.png" },
  { audioIndex: 18, slideNum: 19, type: "content-screenshot", durationSec: 43.656, screenshot: "output-tool.png" },
  { audioIndex: 19, slideNum: 20, type: "content",            durationSec: 44.952, screenshot: null },
  { audioIndex: 20, slideNum: 21, type: "content",            durationSec: 31.848, screenshot: null },
  { audioIndex: 21, slideNum: 22, type: "content",            durationSec: 27.264, screenshot: null },
  { audioIndex: 22, slideNum: 23, type: "content",            durationSec: 37.152, screenshot: null },
  { audioIndex: 23, slideNum: 24, type: "content-screenshot", durationSec: 35.616, screenshot: "homepage.png" },
  { audioIndex: 24, slideNum: 25, type: "content",            durationSec: 38.712, screenshot: null },
  { audioIndex: 25, slideNum: 26, type: "content",            durationSec: 32.712, screenshot: null },
  { audioIndex: 26, slideNum: 27, type: "outro",              durationSec: 31.968, screenshot: null },
];

/** 총 프레임 수 (988.584 * 30 = 29658) */
export const TOTAL_FRAMES = SLIDE_DATA.reduce(
  (sum, s) => sum + Math.round(s.durationSec * FPS),
  0
);
