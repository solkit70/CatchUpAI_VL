import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { FADE_FRAMES, SlideConfig } from "./slideData";

interface ClearlySlideProps {
  slide: SlideConfig;
  isFirst: boolean;
  isLast: boolean;
}

export const ClearlySlide: React.FC<ClearlySlideProps> = ({
  slide,
  isFirst,
  isLast,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  // Fade-in at start (skip for first slide), fade-out at end (skip for last slide)
  const fadeIn = isFirst
    ? 1
    : interpolate(frame, [0, FADE_FRAMES], [0, 1], { extrapolateRight: "clamp" });

  const fadeOut = isLast
    ? 1
    : interpolate(
        frame,
        [durationInFrames - FADE_FRAMES, durationInFrames],
        [1, 0],
        { extrapolateLeft: "clamp" }
      );

  const opacity = Math.min(fadeIn, fadeOut);

  const slideImageSrc = staticFile(
    `clearly-kr/slides/${slide.slideNum}.jpeg`
  );
  const audioSrc = staticFile(
    `clearly-kr/audio/slide_${slide.audioIndex}.mp3`
  );
  const screenshotSrc = slide.screenshot
    ? staticFile(`clearly-kr/screenshots/${slide.screenshot}`)
    : null;

  return (
    <AbsoluteFill style={{ opacity }}>
      {/* Background: Gemini-generated slide image */}
      <AbsoluteFill>
        <Img
          src={slideImageSrc}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
          }}
        />
      </AbsoluteFill>

      {/* Screenshot overlay (content-screenshot type only) */}
      {screenshotSrc && (
        <AbsoluteFill
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            padding: "60px 80px",
          }}
        >
          <div
            style={{
              background: "rgba(0, 0, 0, 0.55)",
              borderRadius: 16,
              padding: 12,
              boxShadow: "0 8px 40px rgba(0,0,0,0.6)",
              maxWidth: "72%",
              maxHeight: "72%",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <Img
              src={screenshotSrc}
              style={{
                borderRadius: 8,
                maxWidth: "100%",
                maxHeight: "100%",
                objectFit: "contain",
              }}
            />
          </div>
        </AbsoluteFill>
      )}

      {/* Audio */}
      <Audio src={audioSrc} />
    </AbsoluteFill>
  );
};
