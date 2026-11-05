# Console and listing checklist

Everything here lives in App Store Connect, Play Console or the store listing, so the repo cannot prove it. For each row record **verified** (screenshot/export seen), **user-confirmed** (user said yes), or **unknown**. Ask in one batch.

## App Store Connect

| # | Item | Rule / gate | Status |
|---|---|---|---|
| 1 | App Privacy answers published; match SDK inventory and manifest | G-A8, 5.1.1(i) | |
| 2 | Privacy Policy URL set, loads publicly | 5.1.1(i) | |
| 3 | Support URL live with a contact route | 1.5 | |
| 4 | Marketing URL (optional) not a placeholder | 2.1(a) | |
| 5 | Age rating questionnaire answered with the new questions; "Made for Kids" intent consistent | 2.3.6, G-A9 | |
| 6 | Category correct; secondary category sensible | 2.3.5 | |
| 7 | Name ≤ 30 chars, subtitle, keywords: no competitors, prices, or claims | 2.3.7 | |
| 8 | Screenshots show real in-app use, per required device sizes; no real personal data | 2.3.3, 2.3.9 | |
| 9 | Description/What's New accurate; generic text only for bug fixes | 2.3, 2.3.12 | |
| 10 | Notes for Review filled (demo account, hardware, region, flagged features, IAP location, OTA policy) | 2.1(a), 2.3.1(a), 2.5.19 | |
| 11 | Demo account works against production, no OTP the reviewer cannot receive | 2.1(a) | |
| 12 | In-App Purchases/subscriptions: submitted with the binary, review screenshots, localized names | 2.1(b), 3.1.2 | |
| 13 | Subscription group, pricing, trial offers configured via App Store Connect | 3.1.1, 3.1.2(a) | |
| 14 | Trader status declared (EU) | G-A10 | |
| 15 | Export compliance answered | G-A11 | |
| 16 | Content rights declaration | 5.2 | |
| 17 | Sign in with Apple configured (if third-party login) | 4.8 | |
| 18 | Developer account type fits domain (legal entity for regulated) | 5.1.1(ix) | |
| 19 | Age-assurance entitlements/config (US states) if relevant | 09 §2 | |
| 20 | TestFlight external group metadata and review (beta app review) | 2.2 | |

## Play Console

| # | Item | Rule / gate | Status |
|---|---|---|---|
| 1 | Data safety published; matches SDK inventory | G-G3 | |
| 2 | Privacy policy URL: public HTML, names the developer/app | User Data | |
| 3 | Account deletion web link set; in-app path exists | G-G4 | |
| 4 | App access: credentials/instructions for login-gated areas | G-G6 | |
| 5 | Ads declaration correct | G-G6 | |
| 6 | Content rating (IARC) completed | G-G6 | |
| 7 | Target audience & content; Families declarations if children | Families | |
| 8 | Permissions declarations (photo/video, all-files, SMS/call log, background location, FGS types) | Permissions | |
| 9 | News/health/financial/government declarations as applicable | G-G6 | |
| 10 | Testing requirement: 12 testers × 14 days (new personal accounts) | G-G5 | |
| 11 | Developer verification / app registration | G-G8 | |
| 12 | Store listing: title/short/full description, screenshots, feature graphic accurate | Metadata (T) | |
| 13 | Release tracks: internal → closed → production, staged rollout | — | |
| 14 | Android vitals within thresholds | G-G9 | |
| 15 | Trader declaration (EU) | 09 §1 | |

## Cross-store consistency

| Item | Status |
|---|---|
| Privacy policy text covers every SDK and purpose declared in both labels | |
| App name, icon and description do not reference the other platform (Apple 2.3.10) | |
| Version/feature parity claims in listings match builds | |
