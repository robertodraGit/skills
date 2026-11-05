# Screenshot plan — {{product}}

Framework: {{problem→solution | day in the life | feature tour | before/after}} · Locales: {{it, en}} · Stores: {{Apple, Play}}

## Never show

- {{e.g. a bare portrait with LIKE/NOPE under it}}
- Real user data; other platforms' chrome; "beta"/"coming soon"; fake ratings or press quotes

## Frames

| # | Message (one claim) | Screen | Must be visible | Ledger id | Caption IT | Caption EN | Demo data source | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | C? | | | seed script / account | planned / captured / composed |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |
| 5 | | | | | | | | |
| 6 | | | | | | | | |

Frames 1–3 appear in Apple search results: each must be understandable alone.

## Production

| Store | Asset | Size | Format | Count |
|---|---|---|---|---|
| Apple | iPhone screenshots | 1320×2868 (confirm the required set in the console) | PNG/JPEG no alpha | 1–10 |
| Apple | iPad | only if the app runs on iPad | | |
| Apple | App preview | optional, 15–30 s | | ≤ 3 |
| Play | Phone screenshots | ≥ 1080×1920, 9:16 | PNG/JPEG no alpha | 2–8 (≥ 4 for recommendations) |
| Play | Feature graphic | 1024×500 | PNG/JPEG no alpha | 1 |
| Play | Icon | 512×512 PNG | 32-bit | 1 |
| Play | Alt text | ≤ 140 chars per image | | |

Capture pipeline: {{fastlane snapshot / Maestro / simctl + adb}} · Locale loop: {{yes}} · Composition source: {{Figma / HTML / script path}}

## QA

- [ ] Dimensions and no alpha verified
- [ ] Readable at 25% size
- [ ] Captions localized; Play tagline ≤ 20%
- [ ] Demo data fictional
- [ ] iPad frames absent when the app is iPhone-only
