# Apple 04 — Guideline 4: Design

Source: App Review Guidelines, section 4. Confidence **V** (verbatim, read 2026-11-05; *Last Updated: October 16, 2026*). Paraphrased. Intro: apps that stop working or degrade may be removed at any time.

## 4.1–4.3 Originality and minimum functionality

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 4.1(a) | Copycats: original ideas; no copying or minor name/UI changes of another app | Clones, look-alikes | Compare with the category leaders cited in the listing | C, L |
| 4.1(b) [NR] | Impersonating other apps or services violates the Developer Code of Conduct (removal from the Program possible) | Name/icon resembling known brands | Review name, icon, screenshots | L |
| 4.1(c) | No use of another developer's icon, brand or product name in the app's icon/name without approval | Integrations ("for X") | Check naming and icon | L |
| 4.2 | **Minimum functionality**: the app must go beyond a repackaged website; song/movie apps go to iTunes; book/game guides go to Apple Books | WebView shells (Capacitor/Cordova/RN WebView), content-only apps | See §WebView test below | C |
| 4.2.1 | ARKit apps: rich, integrated AR experiences; a dropped-in model or replayed animation is not enough | AR | Review AR depth | C |
| 4.2.2 | Except catalogs, not primarily marketing materials, ads, web clippings, content aggregators or collections of links | Marketing/aggregator apps | Review feature set | C |
| 4.2.3(i) | Must work without requiring another app to be installed | Companion apps | Check hard dependencies | C |
| 4.2.3(ii) | If the app needs an additional download at first launch, disclose the size and prompt the user | Large first-launch downloads (games, assets) | Check the download prompt | C |
| 4.2.6 | Apps created from commercialised templates or app-generation services are rejected unless submitted by the content provider. Aggregated "picker" single binaries are acceptable | White-label builders | Check template origin, many near-identical bundles | C |
| 4.2.7 | Remote desktop clients: connect only to user-owned host on a local LAN; software runs on the host; account creation on the host; UI must not look like iOS or the App Store; thin clients for cloud-based apps are not appropriate | Remote desktop/game streaming clients | Review | C |

**WebView test (4.2)**: Could the same experience be delivered by a bookmark to the website? Look for native value that a reviewer can see in 60 seconds: push, offline, device APIs, native navigation, performance. A Capacitor/Cordova shell with `server.url` pointing at a website and no native feature → 🔴. A shell with real native plugins and offline data → 🟡, still write what is native in the review notes.

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 4.3(a) [NR] | No multiple bundle IDs of the same app (e.g. one map app per city); use one app with IAP variants | Many per-variant apps | List bundle IDs under the developer account (K) and repo targets | C, K |
| 4.3(b) | **Spam**: no apps indistinguishable from what is already widely available. Saturated categories (dating, flashlight, sound effects, wallpapers, simple timers, fortune telling) need a meaningfully different or improved experience, and may be removed if not maintained. Low-effort kinds (drinking games, Kama Sutra, fart/burp apps) can lead to removal from the Program on repeat submissions | Crowded categories | Write the "what is different" sentence for the review notes. If you cannot, expect 🟠 | C, L |

## 4.4 Extensions

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 4.4 [NR] | Follow extension guides; include some functionality where possible; disclose extensions accurately; extensions may not include marketing, advertising or IAP | Any app extension | Review extension targets | C |
| 4.4.1 [NR] | Keyboard extensions: provide keyboard input; follow Sticker rules for images/emoji; provide a next-keyboard method; work without full network access/Full Access; collect activity only to improve the keyboard on-device; do not launch other apps besides Settings; do not repurpose keys | Keyboards | Review | C |
| 4.4.2 [NR] | Safari extensions: current Safari version; no interference with system/Safari UI; never malicious or misleading; request access to no more websites than needed | Safari extensions | Review manifest permissions | C |

## 4.5 Apple sites and services

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 4.5.1 [NR] | Approved Apple RSS feeds allowed; no scraping Apple sites or building rankings from them | Apple data | Review | C |
| 4.5.2 [NR] | Apple Music/MusicKit: playback starts with user action and uses standard controls; no payment/indirect monetisation of Apple Music access; no downloading/uploading/sharing music files; cover art/metadata only for playback or playlists; playlist/favorites access disclosed in the purpose string, no sharing with third parties beyond app support | MusicKit | Review | C |
| 4.5.3 [NR] | No spam, phishing or unsolicited messages via Apple services (Game Center, Push Notifications, Live Activities); no mining Game Center Player IDs | Push, Game Center | Review notification triggers | C |
| 4.5.4 [NR] | **Push notifications must not be required for app function** and must not carry sensitive personal or confidential information. **Promotional/marketing pushes require explicit in-app opt-in consent and an opt-out method** | Push | Find opt-in UI for marketing pushes; check payload content; check app works with notifications denied | C |
| 4.5.5 [NR] | Game Center Player IDs only as the terms allow; not shown in the app or to third parties | Game Center | Review | C |
| 4.5.6 [NR] | Apple emoji: Unicode characters that render as Apple emoji are fine; Apple emoji may not be used on other platforms or embedded in the binary | Emoji assets | Check bundled emoji assets | C |

## 4.7 Mini apps, mini games, streaming games, chatbots, plug-ins, emulators

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 4.7 [NR] | HTML5/JavaScript mini apps and mini games, streaming games, chatbots, plug-ins not embedded in the binary; emulators may offer game downloads. The developer is responsible for all such software and must satisfy 4.7.1–4.7.5 | App hosts third-party or downloadable mini software | Identify every hosted unit | C |
| 4.7.1 | Such software must follow privacy rules incl. 5.1 (kids and health data); include content filtering, a reporting mechanism with timely responses, and blocking of abusive users; follow 3.1 for digital goods | Same | Verify the three mechanisms and IAP route | C |
| 4.7.2 [NR] | Do not extend or expose native platform APIs to such software without Apple's prior permission | Same | Review the bridge surface | C |
| 4.7.3 [NR] | No sharing of data or privacy permissions with such software without explicit user consent in each instance | Same | Check per-instance consent | C |
| 4.7.4 | An index of all such software and its metadata, with universal links to each | Same | Verify the index exists | C |
| 4.7.5 [NR] | Identify software exceeding the app's age rating; age restriction based on verified or declared age | Same | Verify mechanism | C |

## 4.8 Login services

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 4.8 [NR] | If a third-party or social login (Facebook Login, Google Sign-In, Log in with X, Sign In with LinkedIn, Login with Amazon, WeChat Login) is the **primary** account login, **also offer an equivalent login service** with all three: (1) data collection limited to name and email, (2) users can keep their email private, (3) no collection of app interactions for advertising without consent. **Exemptions**: only your own company's login; alternative marketplace login; education/enterprise/business apps requiring an existing account; government/industry-backed citizen or electronic ID; clients for a third-party service where users sign in directly to that mail/social account | Social/third-party login present | Find third-party login code (`01-signals.md`). If present and no own-login-only exemption: confirm Sign in with Apple (or an equivalent meeting the three conditions). A plain email+password option alone does **not** satisfy 4.8 when third-party login is the primary route unless it meets all three conditions (T: reviewers treat own email/password as an alternative only where it is a genuine, equivalent primary option, re-read live text) | C |

## 4.9–4.10

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 4.9 | Apple Pay: disclose all material purchase information before sale; use Apple Pay branding/UI per guidelines. Recurring payments must disclose: renewal term length and that it continues until cancelled; what is provided each period; actual charges; how to cancel | Apple Pay | Review checkout | C, L |
| 4.10 | May not monetise built-in capabilities of the device/OS (Push Notifications, camera, gyroscope) or Apple services (Apple Music access, iCloud storage, Screen Time APIs) | Selling OS capabilities | Review pricing/features | C |

## Rule-of-thumb verdicts

- Social login without an equivalent option → 🔴 (4.8); the fix is Sign in with Apple. Remember its deletion requirement: revoke tokens on account deletion (`apple-05` 5.1.1(v), `apple-06` G-A7).
- WebView shell with no native value → 🔴 (4.2).
- Marketing push without opt-in → 🔴 (4.5.4).
- Multiple apps that differ only by a city/theme → 🔴 (4.3(a)).
