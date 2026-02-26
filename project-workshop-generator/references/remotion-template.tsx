import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
  Sequence,
  Series,
} from "remotion";
import React from "react";

// ─── Types ────────────────────────────────────────────────────────────────────

type Slide = {
  moduleNumber: number;
  title: string;
  bullets: string[];
};

type WorkshopVideoProps = {
  projectName: string;
  slides: Slide[];
};

// ─── Single Slide Component ───────────────────────────────────────────────────

const WorkshopSlide: React.FC<Slide> = ({ moduleNumber, title, bullets }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Fade + slide-up entrance driven by useCurrentFrame (no CSS transitions)
  const progress = spring({ frame, fps, config: { damping: 80 } });

  const opacity = interpolate(progress, [0, 1], [0, 1]);
  const translateY = interpolate(progress, [0, 1], [40, 0]);

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#0f0f0f",
        justifyContent: "center",
        alignItems: "flex-start",
        padding: "80px 100px",
        fontFamily: "Inter, sans-serif",
      }}
    >
      <div style={{ opacity, transform: `translateY(${translateY}px)` }}>
        {/* Module badge */}
        <span
          style={{
            fontSize: 14,
            color: "#888",
            textTransform: "uppercase",
            letterSpacing: 3,
            marginBottom: 16,
            display: "block",
          }}
        >
          Module {moduleNumber}
        </span>

        {/* Title */}
        <h1
          style={{
            fontSize: 56,
            color: "#fff",
            fontWeight: 700,
            marginBottom: 40,
            lineHeight: 1.2,
          }}
        >
          {title}
        </h1>

        {/* Bullets with staggered entrance */}
        <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
          {bullets.map((bullet, i) => {
            const bulletProgress = spring({
              frame: frame - i * 6, // stagger each bullet by 6 frames
              fps,
              config: { damping: 100 },
            });
            const bulletOpacity = interpolate(bulletProgress, [0, 1], [0, 1]);
            const bulletX = interpolate(bulletProgress, [0, 1], [-20, 0]);

            return (
              <li
                key={i}
                style={{
                  fontSize: 24,
                  color: "#d4d4d4",
                  marginBottom: 14,
                  opacity: bulletOpacity,
                  transform: `translateX(${bulletX}px)`,
                  display: "flex",
                  alignItems: "center",
                  gap: 12,
                }}
              >
                <span style={{ color: "#6366f1" }}>▸</span>
                {bullet}
              </li>
            );
          })}
        </ul>
      </div>
    </AbsoluteFill>
  );
};

// ─── SlideFactory: iterates slides without touching this template ──────────────

export const WorkshopVideo: React.FC<WorkshopVideoProps> = ({
  projectName,
  slides,
}) => {
  const SLIDE_DURATION = 180; // 6 seconds @ 30fps — override per slide if needed

  return (
    <AbsoluteFill style={{ backgroundColor: "#0f0f0f" }}>
      <Series>
        {/* Title card */}
        <Series.Sequence durationInFrames={90}>
          <TitleCard projectName={projectName} />
        </Series.Sequence>

        {/* Slides from props — AI passes data, never touches this file */}
        {slides.map((slide, i) => (
          <Series.Sequence key={i} durationInFrames={SLIDE_DURATION}>
            <WorkshopSlide {...slide} />
          </Series.Sequence>
        ))}
      </Series>
    </AbsoluteFill>
  );
};

// ─── Title Card ───────────────────────────────────────────────────────────────

const TitleCard: React.FC<{ projectName: string }> = ({ projectName }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const opacity = interpolate(
    spring({ frame, fps }),
    [0, 1],
    [0, 1]
  );

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#0f0f0f",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <h1
        style={{
          fontSize: 72,
          color: "#fff",
          fontWeight: 800,
          opacity,
          textAlign: "center",
        }}
      >
        {projectName}
      </h1>
      <p style={{ color: "#6366f1", fontSize: 20, opacity, marginTop: 16 }}>
        Workshop
      </p>
    </AbsoluteFill>
  );
};

// ─── Default Props (required by Remotion Composition) ────────────────────────

export const defaultProps: WorkshopVideoProps = {
  projectName: "My Project",
  slides: [
    {
      moduleNumber: 0,
      title: "Prerequisites",
      bullets: ["Node.js 20+", "pnpm installed", "Access to .env file"],
    },
    {
      moduleNumber: 1,
      title: "Vision & Strategy",
      bullets: ["Project goals", "Target users", "Business impact"],
    },
  ],
};
