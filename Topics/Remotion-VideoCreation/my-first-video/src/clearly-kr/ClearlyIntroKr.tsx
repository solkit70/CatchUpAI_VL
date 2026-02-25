import React from "react";
import { AbsoluteFill, Series } from "remotion";
import { ClearlySlide } from "./ClearlySlide";
import { FPS, SLIDE_DATA } from "./slideData";

export const ClearlyIntroKr: React.FC = () => {
  const lastIndex = SLIDE_DATA.length - 1;

  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <Series>
        {SLIDE_DATA.map((slide, idx) => (
          <Series.Sequence
            key={slide.audioIndex}
            durationInFrames={Math.round(slide.durationSec * FPS)}
          >
            <ClearlySlide
              slide={slide}
              isFirst={idx === 0}
              isLast={idx === lastIndex}
            />
          </Series.Sequence>
        ))}
      </Series>
    </AbsoluteFill>
  );
};
