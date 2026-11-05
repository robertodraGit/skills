# 01 — Field specs: App Store Connect and Google Play

Status as of **2026-11-05**. Confidence per row: **V** live page · **V\*** summarised page, re-read before 🔴 · **T** practice. `scripts/lint-listing.py` encodes the limits in section 1 and 3.

## 1. Text fields

### Apple (App Store Connect)

| Field | Limit | Editable | Indexed for search | Rules and notes | Conf |
|---|---|---|---|---|---|
| **Name** | 30 characters (2–30) | With a version submission | **Yes** | Distinctive, easy to spell; no prices, terms or unrelated descriptions (2.3.7); no competitor/trademark stuffing | V |
| **Subtitle** | 30 characters | With a new version submission (not on its own) | **Yes** | Concise value statement; no inappropriate content, other apps or unverifiable claims (2.3.7) | V |
| **Promotional text** | 170 characters | **Any time, no new version** | **No** | Shown above the description; for current news; do not park keywords here | V |
| **Description** | 4000 characters, plain text | With a new version | No (not documented as indexed) | Must reflect the core experience; state which features need purchases (2.3.2) | V\* |
| **Keywords** | 100 characters, comma separated, no spaces after commas; spaces allowed inside a phrase | Per localization; submitted with a version (no "any time" wording found) | **Yes** | Do not repeat words already in name, subtitle or category; avoid plurals of words already used, "app"/"game", filler words, special characters; terms longer than two characters. One Apple page says "bytes": keep UTF-8 bytes ≤ 100 for accented text | V (chars) / V\* (bytes) |
| **What's New** | 4000 characters | With a version; **required for updates**, not for the first version | No | Describe new features and product changes; generic text only for bug fixes, security, performance (2.3.12) | V\* |
| **Support URL** | URL with protocol | Per localization | — | Must lead to real contact information (1.5) | V\* |
| **Marketing URL** | URL with protocol | Per localization | — | Optional | V\* |
| **Privacy Policy URL** | URL | App-level | — | Required for iOS and macOS apps | V\* |
| **Copyright** | "year owner name"; © added automatically | — | — | e.g. `2026 Example S.r.l.` | V\* |
| **Primary / secondary category** | One each | App-level | **Yes** | Choose the most appropriate (2.3.5); subcategories (up to two) for Games/Stickers | V |
| **Primary language** | One | Can change | — | Metadata falls back to it when a locale is missing | V\* |

Not on the pages read: the full "Required, localizable, editable" matrix (checkmark columns were lost). Treat per-locale/editable details as ❓ and let the console confirm.

In-app events (text limits not found on the pages read; **T**: name 30, short description 50, long description 120 characters): card image 16:9, 1920×1080 to 3840×2160; details image 9:16, 1080×1920 to 2160×3840; video MOV/M4V/MP4, ≤ 500 MB (V\*). Start/publish times are editable only for future dates per storefront (V\*).

### Google Play (Play Console)

| Field | Limit | Indexed | Rules and notes | Conf |
|---|---|---|---|---|
| **App name (title)** | 30 characters | Not documented; practice: yes (T) | No emojis, emoticons or repeated special characters; avoid ALL CAPS unless brand; no ranking, price, promotion or Google Play program claims ("#1", "free for a limited time", "Editor's choice", "New"); no "Free"/"No Ads" in the title (best practices) | V |
| **Short description** | 80 characters | Not documented; practice: yes (T) | No call to action ("download/install/play/try now"); no "Best", "#1", "Top", "New", "Discount", "Sale", "Million Downloads"; no special characters, line breaks, emojis, repeated punctuation; final period only for multiple sentences; no time-sensitive copy | V |
| **Full description** | 4000 characters | Not documented; practice: yes (T) | Do not repeat the short description; no unattributed testimonials; no repetitive/unrelated keywords; no keyword lists | V |
| **Release notes** | 500 characters per language | — | `<en-US>…</en-US>` tags on their own lines; no promotion or calls to action; add translations first | V |
| **Contact email** | required | — | website recommended | V |
| **Default language** | English (United States) by default | — | Translations: Store listing → Manage translations | V |

Character counting: Play counts full-width and half-width characters the same (V). Repetitive or irrelevant keywords can cause suspension (V). Google's pages do **not** say which fields are indexed or weighted: state "T" when advising on Play keyword placement.

## 2. Localizations

| Store | Languages | Notes | Conf |
|---|---|---|---|
| Apple | ~50 App Store localizations incl. **Italian**, **English (U.S.)**, **English (U.K.)**, English (Australia), English (Canada) | Primary language is the fallback when a locale lacks metadata; primary language can be changed | V\* |
| Play | ~90 translatable languages incl. it-IT, en-US, en-GB | Free machine translation for 10 languages (ar, fr-FR, de-DE, id, **it-IT**, ja-JP, pt-BR, es-419, es-ES, th), not human-reviewed; human translation from USD 0.07/word in 7 days; untranslated locales get a Google Translate version; text translations without localized graphics keep default-language graphics | V |

Folder and locale codes: `06-localization-it-en.md` §4.

## 3. Graphics and video

### Apple

| Asset | Spec | Conf |
|---|---|---|
| Screenshots | 1–10 per device size and localization; JPEG/JPG/PNG, **no alpha**; iPhone sets include 1320×2868, 1290×2796, 1260×2736 (Dynamic Island large), 1206×2622, 1179×2556 (medium), 1284×2778/1242×2688 (Face ID large), 1170×2532/1125×2436/1080×2340 (Face ID medium) and Home-button sizes; iPad 13" 2064×2752 or 2048×2732; if the UI is identical across sizes/localizations, supply the largest and App Store Connect scales down; fallbacks between iPhone sets are defined by the console. **Confirm the required set in the console** (the page is summarised) | V\* |
| App previews | up to 3 per device size and language; 15–30 seconds; ≤ 500 MB; H.264 (10–12 Mbps, AAC 256 kbps) or ProRes 422 HQ; ≤ 30 fps; iPhone 886×1920 portrait or 1920×886 landscape (Dynamic Island/Face ID sets); poster frame default 5 s; processing up to 24 h; previews display before screenshots | V\* |
| Product page | up to 10 screenshots and 3 previews; **the first 1–3 screenshots/previews appear in search results**; up to 20 IAPs/subscriptions shown; IAP names 35 characters, descriptions 55 | V |
| Icon | in the binary (1024×1024, no alpha); alternate icons only via product page optimization with icon variants in the binary | V |
| **Creative assets** (product page header, search-result artwork, used for featuring and Apple placements) | Header image 21:9 **3840×1646** (JPEG/PNG) or 16:9 **5244×2950** (PNG); search-result image 3:2 from 1920×1280 to **3840×2560** or 16:9 5244×2950; header video 21:9 3840×1646, 30/60 fps, 5–30 s, muted by default and looping; search-result video 3:2; no alpha. A single "universal" 16:9 asset can serve both placements. Safe areas are defined in Apple's templates, not as pixel numbers on the page | V\* |
| Creative-asset content rules | No specific pricing, discounts, website URLs or copyright symbols; no unverifiable awards; no logos or references to other platforms; no Apple-designated recognitions (Editor's Choice, App of the Day…); must meet a 4+ rating; short localized text that enhances the visual; key content centered | V |
| Featuring | No checklist; Featuring Nominations in App Store Connect (App Launch, New Content, App Enhancements); give at least 2 weeks, up to 3 months ahead for wider consideration (form recommends ≥ 3 weeks); up to 10 related apps and 5 supplemental URLs; Apple may email Admin/App Manager/Marketing roles for promotional assets | V / V\* |

### Google Play

| Asset | Spec | Conf |
|---|---|---|
| App icon | 512×512 px, 32-bit PNG with alpha, ≤ 1024 KB; no badges or text implying ranking, price, categories | V |
| Feature graphic | 1024×500 px, JPEG or 24-bit PNG **no alpha**; keep key content away from cutoff zones; avoid device imagery and store badges | V |
| Phone screenshots | up to 8 per device type; **minimum 2** to publish; JPEG/24-bit PNG no alpha; each side 320–3840 px; long side ≤ 2× short side | V |
| Recommendation eligibility (apps) | ≥ 4 screenshots at ≥ 1080 px; portrait ≥ 1080×1920, landscape ≥ 1920×1080 | V |
| Large screens | ≥ 4 recommended; 16:9 landscape or 9:16 portrait | V |
| Alt text | ≤ 140 characters per graphic/screenshot | V |
| Screenshot taglines | ≤ 20% of the image; real in-app footage; no fingers tapping; clean status bar | V |
| Promo video | one YouTube URL (not playlist/channel, no timecode); public/unlisted; ads off; not age-restricted; embeddable; first 30 s autoplay muted; show real app in first 10 s; ≥ 80% real footage; captions | V |
| Other form factors | Wear OS 1:1 ≥ 384×384; Android TV banner 1280×720; Android XR 4–8 screenshots 8:5; Automotive portrait 800×1280 and landscape 1024×768 | V |

## 4. Variants and experiments (summary; details in `07-experiments.md`)

| Feature | Limit | Conf |
|---|---|---|
| Apple custom product pages | up to 70 per app; differ in screenshots, previews, promotional text (and per-locale keywords per the help page); own URL; reviewed independently of an app update | V / V\* |
| Apple product page optimization | up to 3 treatments; icon, screenshots, previews; test name ≤ 64; ≤ 90 days; one test at a time; locked once started | V |
| Play custom store listings | up to 50; name, icon, descriptions, graphics differ; privacy policy, category, contact shared; one custom listing per country; URL `&listing=<param>` | V |
| Play store listing experiments | one default-graphics experiment or up to five localized ones at once; up to 2 variants vs current; name ≤ 50; stops after 6 months | V |
