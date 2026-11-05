# 03 — ePrivacy, consent and tracking in apps and sites

Why this file exists: **GDPR Art. 6 and ePrivacy Art. 5(3) are separate gates.** Storing or reading information on a user's device needs **consent**, unless strictly necessary for a service the user requested or for transmission. A legitimate-interest basis under GDPR does not cure a missing Art. 5(3) consent.

Confidence: Art. 5(3) wording **T-s**; EDPB guidance and regulator practice **T**; UMP/SDK specifics **V** where marked.

## 1. Art. 5(3) ePrivacy — the rule applied to apps

- **Scope is technology-neutral** (EDPB Guidelines 2/2023 on the technical scope of Art. 5(3), T): cookies, local storage, SDK identifiers, device fingerprinting, tracking pixels/URLs, IoT. It covers *reading* information from the terminal equipment (e.g. IDFA/AAID, installed-apps list, device attributes sent to a server) as well as *storing*.
- **Exemptions** (narrow): (1) sole purpose of carrying out a transmission over a network; (2) strictly necessary to provide a service explicitly requested by the user (session cookie after login, load balancing, security token, remembering a cart, user-interface preference chosen by the user).
- **Not exempt in the EU as a general rule**: advertising, cross-site/app tracking, A/B tests on users, usage analytics that create or link persistent identifiers, session replay, crash/diagnostic SDKs that read persistent device identifiers *beyond* what is strictly necessary. Some authorities accept narrow first-party audience measurement without consent if IP is truncated, no cross-correlation and no secondary use (Italy: see `10-italy-notes.md`, T). Treat those as 🟠 decisions, not 🟢 defaults.

## 2. Valid consent in apps and sites (GDPR Art. 4(11), 7; EDPB Guidelines 05/2020, T)

| Requirement | Test in the product |
|---|---|
| **Freely given** | Refusal has no detriment beyond the purpose; no "cookie wall" for general content; consent not bundled with ToS or with unrelated purposes |
| **Specific** | Separate choices for distinct purposes (analytics, personalisation, ads); no single "I accept everything" as the only path |
| **Informed** | Identity of controller(s), purposes, vendors (or a list), data types shown before choice |
| **Unambiguous, affirmative** | No pre-ticked boxes; scrolling/continuing to browse is not consent; closing the dialog is not consent |
| **Equal ease to refuse** | A "Reject" or "Only necessary" button at the same level and visual weight as "Accept" (regulators have fined for hidden reject paths, T) |
| **Withdrawable as easily as given** | Persistent entry point to change the choice (Settings → Privacy) and a record of the change |
| **Provable** | Stored: timestamp, policy/banner version, purposes, choice, user/device ID |
| **Before processing** | SDKs that need consent are not initialised, and do not send network requests, until the choice is made |

Apple 5.1.1(ii) and Play "prominent disclosure and consent" demand the same in store terms: consent before collection, affirmative action, easy withdrawal, no auto-dismiss.

## 3. SDK gating patterns

Gate initialisation behind the consent state. Patterns (confirm option names in the installed version):

| SDK | Gate |
|---|---|
| **PostHog** | Start opted out by config and call opt-in after consent; opt-out APIs exist (`PostHogSDK.shared.optOut()` iOS, `PostHog.optOut()` Android; **V**). Web: `opt_out_capturing_by_default` (T). Disable session replay and autocapture until consent. Choose **EU Cloud** (Frankfurt, `eu.i.posthog.com`; **V**) and discard IP capture (EU Cloud defaults IP capture off for new projects; **V**) |
| **Firebase Analytics / Crashlytics** | Disable at install (`firebase_analytics_collection_enabled=false` in `AndroidManifest`; `FIREBASE_ANALYTICS_COLLECTION_ENABLED=NO` in `Info.plist`; Crashlytics `firebase_crashlytics_collection_enabled=false`), then `setAnalyticsCollectionEnabled(true)` after consent (T) |
| **Sentry** | `sendDefaultPii: false`; scrub user data in `beforeSend`; Sentry states it collects only configured data and does not use IDFA/Android ID (**V**). Diagnostics with random per-install IDs may be argued as legitimate interest/necessary for stability: record as a 🟠 decision with a minimal-data configuration |
| **AdMob / Google Mobile Ads** | Use Google's **User Messaging Platform**: call `requestConsentInfoUpdate` at **every app launch**; `canRequestAds` returns false until the update is made; show a privacy-options entry point when `privacyOptionsRequirementStatus` requires it (**V**) |
| **Meta SDK** | Plist `FacebookAutoLogAppEventsEnabled=false` and `FacebookAdvertiserIDCollectionEnabled=false` until consent; set `isAdvertiserTrackingEnabled` per ATT (**V**) |
| **AppsFlyer** | Delay `start()` until consent; `anonymizeUser`; `setSharingFilterForPartners` before start; `disableIDFVCollection` (**V**) |
| **RevenueCat** | Purchases are contract necessity; avoid sending name/email unless needed; use anonymous app user IDs where possible (**V**: Purchases data; custom user ID/identifiers may be required in the label) |
| **OneSignal / push** | Push needs OS permission; marketing pushes need consent (Apple 4.5.4); store tags/external IDs minimally (T) |
| **Session replay** (PostHog, FullStory, Hotjar, Smartlook, LogRocket) | Consent required; mask inputs; show a recording indicator (Apple 2.5.14 **V**); never record special-category screens |

Check pattern in code: `init` calls are inside `if (consent.analytics)` / consent callback, not at app start. Confirm in a network capture (**N**): no calls to vendor hosts before the choice.

## 4. ATT vs GDPR consent — different questions

| | Apple ATT | GDPR/ePrivacy consent |
|---|---|---|
| Triggered by | "Tracking" (linking with other companies' data for ads/measurement, or sharing with data brokers) | Any non-necessary device access or personal-data processing based on consent |
| Granted via | System prompt (`ATTrackingManager`) with purpose string | Your own consent UI (CMP) |
| Satisfies the other? | **No.** ATT approval does not equal a GDPR-valid consent; GDPR consent does not replace the ATT prompt | Same |
| Apple EU variant | From iOS 27.2 an alternative prompt with an "Additional Information" button; mandatory for DE/FR/IT/PL/RO (reported on Apple's page, **V\***) | — |

Recommended order: CMP/consent first (explain purposes), then ATT only if consent covers tracking. Never gate functionality on tracking consent (Apple 5.1.2(i)).

## 5. Identifiers cheat-sheet

| Identifier | Reset by user? | Needs consent (EU)? | Store rule |
|---|---|---|---|
| IDFA | Yes | Yes for ads/tracking; ATT also required | ATT; label: Device ID, tracking |
| IDFV | Per vendor | Treat like a persistent ID; consent unless necessary | Allowed across your own apps without ATT, not for cross-company tracking |
| AAID | Yes | Yes for ads/analytics beyond necessity | Play: ads/analytics only, honour opt-out, `AD_ID` permission (API 33+) |
| App Set ID | Resets on reinstall/app-set | Analytics/fraud only | Play: not for ads personalisation |
| Firebase installation ID | Per install | Treated as an identifier; "does not uniquely identify a user or physical device" (**V**, Firebase) but still personal data when linked | Label: Device ID if linked |
| Push token | Rotates | Provided on OS permission | Label: Device ID / User ID depending on linkage |
| IP address | No | Always personal data; truncation/discarding reduces risk | Label: part of diagnostics/usage |
| Fingerprint (hash of device traits) | No | Consent; Apple prohibits fingerprinting (**V**) | Rejection risk |

## 6. Web and hybrid apps

- Cookie banner with granular choices, equal-prominence reject, and a footer link to reopen; scripts blocked until choice (tag manager respects consent state; Google Consent Mode v2 for EEA ad/analytics signals, T).
- Third-party embeds that transmit IP before consent (Google Fonts, YouTube, Maps): self-host or load after consent.
- Capacitor/WebView apps: the web layer's cookies/storage fall under the same rules inside the app.

## 7. Findings format

For each SDK/identifier: classification **necessary / consent-gated / gap**, evidence (init location, gate, N-capture), and fix (gate, remove, replace, switch region). A SDK that initialises identifiers before consent is 🔴 unless it is demonstrably strictly necessary.
