# Apple 02 — Guideline 2: Performance

Source: App Review Guidelines, section 2. Confidence **V** (verbatim, read 2026-11-05; *Last Updated: October 16, 2026*). Paraphrased. `[NR]` = rule also applies to Notarization for iOS/iPadOS apps.

## 2.1 App completeness

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 2.1(a) | Submission (including pre-orders) must be final: complete metadata, working URLs, no placeholder text or empty sites. Test on-device for bugs and stability. **Provide a demo account and keep the backend live.** If a demo account is impossible for legal/security reasons, a built-in demo mode needs **prior Apple approval** and must show full functionality. Incomplete bundles and crashing binaries are rejected | Always. Demo account: any app with login | Search for placeholders (`lorem`, `TODO`, `placeholder`, `coming soon`, `example.com`). Verify demo credentials exist in the review-notes draft and work against production (ask the user to confirm). Check every URL in metadata. List crash risks (unhandled promise rejections, missing permissions strings) | C, K, L |
| 2.1(b) | In-app purchases must be complete, current, visible to the reviewer and functional. If a configured IAP cannot be found, explain in review notes | App has IAPs | Compare IAP product IDs configured in App Store Connect with product IDs in code; check every product has a reachable purchase path and a review screenshot | C, K |

## 2.2 Beta testing

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 2.2 | Demos, betas and trials belong in TestFlight, not the App Store. TestFlight builds must be intended for public distribution; no compensation of any kind to testers (including crowdfunding rewards). Significant beta updates go through TestFlight App Review | Submitting a "beta", "demo", "test" or "preview" app | Search app name, subtitle, in-app strings for `beta|demo|test|preview` | C, L |

## 2.3 Accurate metadata

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 2.3 | Privacy info, description, screenshots and previews must accurately reflect the core experience and stay current | Always | Compare listing claims to implemented features one by one | L, C |
| 2.3.1(a) [NR] | New features/changes must be described **specifically** in Notes for Review (generic descriptions rejected) and be accessible for review. Misleading marketing (promoting features the app lacks, false pricing) is grounds for removal and account termination | Always | Draft review notes (`assets/review-notes-template.md`); list features gated behind flags/regions/hardware | L |
| 2.3.2 | Metadata must state which featured items/levels/subscriptions need additional purchases. Promoted IAPs need an appropriate Display Name, Screenshot and Description, and the app must handle `SKPaymentTransactionObserver` so purchases complete at launch | IAP/subscriptions/promoted IAP | Check description for "requires purchase" wording; check transaction observer is registered at launch (iOS payments flow) | L, C |
| 2.3.3 | Screenshots must show the app **in use**, not title art, a login page or a splash screen. Overlays allowed | Always | Review the screenshot set: each frame shows real functionality | L |
| 2.3.4 | Previews: video screen captures of the app only; narration and overlays allowed | App preview video | Watch for non-app footage, device marketing footage | L |
| 2.3.5 [NR] | Choose the most appropriate category; Apple may change it | Always | Compare category to primary function | K, L |
| 2.3.6 [NR] | Answer age-rating questions honestly; comply with local rating/warning requirements per territory | Always | Compare questionnaire answers (UGC, web access, ads, chat, gambling/loot boxes, medical topics) to the code. Under the new age system (4+, 9+, 13+, 16+, 18+) see `apple-06-technical-gates.md` G-A9 | K, C |
| 2.3.7 [NR] | Unique name and accurate keywords; no stuffing with trademarks, popular app names, prices or irrelevant terms. **App name ≤ 30 characters.** No prices/terms/unrelated descriptions in name, subtitle, screenshots or previews. Subtitles: no inappropriate content, other apps, unverifiable claims | Always | Count characters; scan name/subtitle/keywords for competitor names, "best", "#1", prices | L, K |
| 2.3.8 [NR] | Metadata and IAP icons/screenshots/previews must suit a **4+** rating even if the app is rated higher. "For Kids"/"For Children" reserved for the Kids Category. Names and icons (incl. Watch, alternate icons) similar enough to avoid confusion | Always | Review imagery for age-inappropriate content; search metadata for "kids/children" | L |
| 2.3.9 | You hold rights to all materials in icons, screenshots, previews; use fictional account info in screenshots, not real people's data | Always | Check asset provenance, real names/emails visible in screenshots | L |
| 2.3.10 | Focus on Apple platforms: no names/icons/imagery of other mobile platforms or alternative marketplaces in metadata, unless approved interactive functionality | Cross-platform products | Scan listing for "Android", "Google Play" badges | L |
| 2.3.11 | Pre-order apps must be complete and deliverable as submitted; material changes (e.g. business model) restart pre-order sales | Pre-orders | Compare pre-order build to advertised | K |
| 2.3.12 | "What's New" must describe new features and product changes; generic text allowed only for bug fixes, security updates, performance improvements | Updates | Check release notes vs the diff of the release | L |
| 2.3.13 | In-app events: match an event type, accurate metadata, run on the set dates across storefronts, working deep links | In-app events | Check deep links resolve; dates | K |
| 2.3.14 | Creative assets (product page header, search results) must pertain to the app's content/functionality/brand, follow metadata rules, suit all audiences; no references to other apps, unverifiable claims, specific/discounted pricing | Featured creative assets | Review assets | L |

## 2.4 Hardware compatibility

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 2.4.1 | iPhone apps should run on iPad when possible; build for all of the user's devices | iPhone-only builds | Check `TARGETED_DEVICE_FAMILY`, Expo `ios.supportsTablet`; test iPad layout (reviewers test on iPad when supported) | C, B |
| 2.4.2 [NR] | Efficient power use: no rapid battery drain, excess heat, resource strain; no unrelated background processes such as cryptocurrency mining (including in third-party ads) | Heavy compute, background work, ads | Search for mining/WebAssembly miners; profile background tasks | C |
| 2.4.3 | Apple TV apps work with Siri Remote or game controllers without other hardware; required controllers must be stated in metadata | tvOS | Out of scope: flag | — |
| 2.4.4 [NR] | Never suggest or require a device restart or unrelated system-settings changes (e.g. turn off Wi-Fi or security features) | Always | Search copy for "restart your (phone|device)", "turn off Wi‑Fi", "disable" | C |
| 2.4.5 | Mac App Store requirements (sandboxing, installers, launch-at-login, updates, etc.) | macOS | Out of scope: flag | — |

## 2.5 Software requirements

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 2.5.1 [NR] | Public APIs only, on the currently shipping OS; phase out deprecated features; APIs used for their intended purpose (HomeKit for home automation, HealthKit for health/fitness) and described accordingly | Any native module; private-API-using libraries | Search for private selectors (`_setApplicationIconBadgeNumber`, `dlopen`, `objc_getClass(@"_UI`); check native deps for known private-API use | C, B |
| 2.5.2 [NR] | Apps must be self-contained: no reading/writing outside the container, no downloading/installing/executing code that adds or changes features (including other apps). Narrow exception: educational coding apps with fully viewable/editable source | OTA updates, scripting, plugin systems, downloaded bundles | See `08-stack-notes.md` §OTA. Test: can an OTA payload add a feature the reviewer never saw? If yes → 🟠 and document policy; if the payload only changes bundled-JS behaviour within the reviewed purpose → generally acceptable, still note it | C |
| 2.5.3 [NR] | No transmitting viruses/malicious code or programs that could harm the OS/hardware (including via Push Notifications or Game Center) | Always | Dependency audit for known-malicious packages | C |
| 2.5.4 [NR] | Multitasking apps may use background services only for intended purposes: VoIP, audio, location, task completion, local notifications, etc. | `UIBackgroundModes` set | Each mode declared in Info.plist must map to a real, observable feature. Unused modes (`audio`, `location`, `fetch`, `voip`) → 🟠/🔴 | C |
| 2.5.5 | Apps must work fully on IPv6-only networks | Any networking | Check for hard-coded IPv4 literals; reviewers test on IPv6 | C |
| 2.5.6 [NR] | Apps that browse the web must use WebKit and WebKit JavaScript (alternative engine entitlements exist for EU/Japan) | In-app browsers | Ensure `WKWebView`/`SFSafariViewController`, no embedded Chromium/Gecko | C |
| 2.5.8 | Apps creating alternate desktop/home screen environments are rejected | Launchers | Flag | C |
| 2.5.9 [NR] | Do not alter or disable standard switches (Volume, Ring/Silent) or other native UI behaviour (e.g. blocking links out to other apps) | Always | Search for volume-button hijack, hardware key interception, link blocking | C |
| 2.5.11 [NR] | SiriKit/Shortcuts: register only intents you can handle without another app and users would expect; related vocabulary; resolve requests directly with no ads in between | Siri/Shortcuts/App Intents | Review intents list | C |
| 2.5.12 [NR] | CallKit / SMS Fraud Extension: block only confirmed spam; identify blocking/spam features in marketing text; data not used for tracking, profiling, selling or sharing | Call/SMS filtering | Review | C |
| 2.5.13 [NR] | Facial recognition for account authentication must use LocalAuthentication where possible (not ARKit/other); provide an alternate method for users under 13 | Face login | Check implementation and alternates | C |
| 2.5.14 [NR] | **Explicit user consent and a clear visual/audible indication when recording or logging user activity** (camera, microphone, screen recording, other input) | Any recording, call recording, screen capture, session replay | Find the indicator and the consent prompt. Session-replay SDKs (PostHog, FullStory, Hotjar, Smartlook) count: consent + masking needed | C |
| 2.5.15 | Apps that let users view/select files must include items from the Files app and iCloud Drive documents | File pickers | Check document picker config | C |
| 2.5.16 [NR] | Widgets, extensions and notifications must relate to the app's content/functionality. (a) All App Clip features must be in the main app binary; App Clips may not contain advertising | Widgets, extensions, App Clips | Review extension targets | C |
| 2.5.17 [NR] | Matter support must use Apple's Matter framework to initiate pairing; non-Apple Matter components must be CSA-certified | Matter | Flag | C |
| 2.5.18 [NR] | Display ads only in the main app binary (not extensions, App Clips, widgets, notifications, keyboards, watchOS). Ads must suit the app's age rating. Users must see all targeting information without leaving the app. No targeted/behavioural ads from sensitive data (HealthKit, ClassKit) or for Kids Category users. Interstitials must be clearly labelled, not deceptive, with large visible close buttons. Users must be able to report inappropriate or age-inappropriate ads | Ads | Verify placement, close buttons, ad content filters, report path, ATT, Kids gating | C |
| 2.5.19 [NR] | No hidden, dormant or undocumented features. Functionality must be clear to users and App Review. Hiding undocumented features (e.g. through obfuscation) is grounds for removal and account termination | Always, especially remote-config / flag-gated features | List flagged/remote features. Everything reachable in production must be described in the review notes. Reviewer-only toggles or country switches are a red flag | C |

## Rule-of-thumb verdicts

- Login app with no demo credentials in review notes → 🔴 (2.1(a)); most frequent rejection cause.
- `UIBackgroundModes` entries with no matching feature → 🔴 (2.5.4).
- Session replay or screen recording without visible indicator and consent → 🟠/🔴 (2.5.14).
- Remote-config feature that changes what the app does after review → 🟠 (2.5.2 / 2.5.19), document in notes.
