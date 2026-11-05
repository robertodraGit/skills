# 04 — Screenshots, previews and graphics

Screenshots are the highest-converting asset on both stores. Apple surfaces the **first 1–3** in search results when there is no preview (V); Play shows the first frames in the listing carousel. Specs: `01-field-specs.md` §3.

## 1. The plan comes before the capture

Deliver a `screenshot-plan` (`assets/screenshot-plan-template.md`) with one row per frame:

| # | Message (one claim) | Screen to capture | Must be visible | Caption IT | Caption EN | Evidence (ledger id) | Demo data source |
|---|---|---|---|---|---|---|---|

Rules for the plan:

1. **One message per frame**, written first as the caption, then matched to a screen. The sequence tells a story: promise → how it works → differentiator → trust → call to act.
2. **Frames 1–3 carry the positioning.** They are the ones seen in search; frame 1 states the core benefit with the product visible. A frame that needs context to be understood belongs later.
3. **Real UI only.** Apple 2.3.3: show the app in use, not title art, a login page or a splash screen. Google: real footage, no fingers tapping, clean status bar.
4. **Captions are marketing, not UI text**: short (≤ 5–7 words per line, ≤ ~30 characters when possible), large type, high contrast, localized. Play: taglines ≤ 20% of the image (V).
5. **Demo data, never real users** (Apple 2.3.9: fictional account info). Seed an environment with fictional people, plausible prices, real city names. A real listing or face in a screenshot is a personal-data disclosure.
6. **Same story in every locale**, captions localized, UI captured in the locale (set the simulator/device language, not photo-edited text).
7. **Age and content suitability**: metadata, icons and screenshots must suit a 4+ audience even if the app is rated higher (Apple 2.3.8).
8. **No other platform's frames**: no Android chrome on App Store frames and vice versa (Apple 2.3.10).
9. **No fake claims**: no ratings, press quotes, "beta", "coming soon" (see the claims ledger).
10. **Sensitive domains** (housing, dating-adjacent, health, finance): decide which frames must *not* exist (e.g. a bare portrait with LIKE/NOPE under it) and write them into the plan's "never show" list.

## 2. Narrative frameworks

| Framework | Sequence | Fits |
|---|---|---|
| **Problem → solution** | pain frame, product answer, 3 proof frames, trust | single-purpose utilities, marketplaces |
| **Day in the life** | morning/commute/evening scenes with the app | habit and lifestyle apps |
| **Feature tour** | one top feature per frame in value order | complex tools |
| **Before/after** | outcome comparison | fitness, productivity, finance |

Pick one; do not mix. Count frames: Apple allows 10, uses of 6–8 are typical (T); Play needs ≥ 2 to publish and ≥ 4 at ≥ 1080 px for recommendation eligibility (V).

## 3. Per-store production specs

| | Apple | Google Play |
|---|---|---|
| Orientation | Portrait for iPhone-only apps | Portrait 9:16 (or landscape for games) |
| Size to produce | 1320×2868 (largest iPhone set; scales down when UI identical, V\*) | 1080×1920 or larger; each side 320–3840; long ≤ 2× short |
| Format | JPEG/PNG, no alpha | JPEG/24-bit PNG, no alpha |
| Count | 1–10 per size and localization | 2–8 per device type |
| iPad | Only if the app runs on iPad. If `supportsTablet=false`, **do not** upload iPad screenshots: they make the app look iPad-compatible | Tablet screenshots optional unless targeting large screens |
| Device frames | Allowed; use neutral frames, no other-platform hardware | Same |
| Alt text | n/a | ≤ 140 characters per image |
| Preview video | up to 3, 15–30 s, ≤ 500 MB | one YouTube URL, real app in first 10 s, ≥ 80% real footage |

Confirm the required Apple set in the console (the spec page is summarised; V\*).

## 4. Capture pipeline (tool-agnostic)

1. **Seed** a dedicated environment/account with demo data; freeze dates and times (9:41 status bar on Apple is a convention, T).
2. **Drive the UI** deterministically: fastlane `snapshot` (iOS UI tests), Maestro flows, Detox/Appium, `xcrun simctl io booted screenshot`, `adb exec-out screencap -p`. Expo apps: use the dev client or a release build on a simulator/emulator with the target locale.
3. **Locale loop**: run the flow once per locale with `-AppleLanguages`/`simctl` language settings or emulator locale.
4. **Compose** captions with a script or design tool from the plan (brand font and colors), not by hand per locale; keep source files (Figma/HTML/Remotion) in the repo for the next release.
5. **Verify**: dimensions, no alpha (`sips -g hasAlpha`), file sizes, readable at thumbnail size (view at 25%).
6. **Upload** with the user's tooling (fastlane `deliver`/`supply`, console). This skill delivers files and text; it does not upload.

## 5. Graphics

- **Icon**: simple, single focal shape, no text badges implying rank/price (Play V), no transparency on Apple.
- **Feature graphic (Play, 1024×500)**: brand + one benefit; no device imagery or store badges; keep important content away from the edges (cutoffs).
- **Apple creative assets** (header, search-result artwork, universal art; sizes in `01-field-specs.md` §3): one clear idea for a first-time visitor; "state the obvious" in search artwork; short localized text only; no prices, discounts, URLs, copyright symbols, awards, other platforms or Apple recognitions; key elements centered for the safe area (V).
- **Dark Mode**: if the app supports it, include at least one screenshot that shows it (Apple product page guidance, V).

### Preview video (Apple, V from the App Previews page)

1. Up to 3 per language, each up to 30 s; make each show something new.
2. **Muted by default**: the story must work silently; captions legible and on screen long enough to read.
3. Stay inside the app: no over-the-shoulder shots or fingers tapping the screen; capture native UI resolution rather than zooming; use dissolves/fades, avoid quick cuts.
4. Lead with the value proposition; loop seamlessly; pick a poster frame that works alone (changing the poster of an approved preview needs a new version).
5. **No specific prices or dates** ("new for spring"): they vary and age.
6. **If login, a purchase or a subscription is required, disclose it** in the footage or end frame.
7. Licensed audio only; a single soundtrack; audio ≥ muted-safe.

Play: real app in the first 10 seconds, ≥ 80% real footage, YouTube-hosted, captions (V, `01-field-specs.md`).

## 5b. If an asset pack already exists

Verify, do not trust: dimensions, alpha and size per file.

```bash
sips -g pixelWidth -g pixelHeight -g hasAlpha path/to/*.png
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,duration -of default=nw=1 preview.mp4
```

Compare to the plan: each frame's caption, locale and ledger id. Two documents describing the screenshots (a copy plan and a delivery note) drift: keep one source (`copy.json`, the plan table) and generate the rest.

## 6. Experiments

Screenshot order and captions are the first thing to test (`07-experiments.md`): one variable per test (message, order, or style), same locale, enough traffic.

## 7. Lint for the plan

- [ ] Every frame has a message, a ledger id, a demo data source.
- [ ] Frames 1–3 are understandable alone.
- [ ] Captions fit and are localized; Play tagline ≤ 20%.
- [ ] No frame shows real user data, other platforms, or banned content.
- [ ] iPad frames absent when the app is iPhone-only.
- [ ] Required sizes for both stores listed with their production resolution.
