# 06 — SDK catalog

What common SDKs and services collect, whether they need consent, their GDPR role, and how to declare them. **Read the entry for each SDK in the inventory, then verify against the installed version's docs.**

Confidence tags: **V** = vendor page read 2026-11-05 (URL given). **T** = training knowledge or vendor page not read: verify before declaring. "Not in pages read" means the fetched page was silent; do not infer.

For every entry: label/Data-safety rows are *starting points*; the final answer depends on configuration (identify calls, custom properties, session replay, PII passed in).

## Analytics, crash, session replay

### Firebase (Analytics, Crashlytics, Auth, Messaging, Remote Config, Performance, Firestore) — V
Sources: https://firebase.google.com/docs/ios/app-store-data-collection · https://firebase.google.com/docs/android/play-data-disclosure (Android page truncated after Performance Monitoring; Analytics points to Google Analytics docs).
- **Always collected (Apple page)**: Crashlytics stack traces and device/OS info; Performance IP addresses plus device/OS/app info; Remote Config country, language, time zone, OS version, app ID, bundle ID; Messaging APNs token and installation ID (FCM registration token); Sessions app metadata and backgrounding time; Functions caller IP and function name.
- **Identifiers**: Firebase Installation ID (FID): per-installation, "does not uniquely identify a user or physical device" (Android page); Auth generates a user ID; Firebase user agent (device, OS, bundle ID) never linked to a user/device identifier.
- **Usage-dependent**: Auth email, phone, display name, Game Center ID, third-party profile data; Crashlytics custom keys and free-text user IDs; Android Auth IP "to provide added security and prevent abuse".
- **Responsibility**: "It is your responsibility to ensure your privacy nutrition labels are accurate"; on Android "you are solely responsible for deciding how to respond to Google Play's Data safety section form".
- **Privacy manifests**: Firebase privacy manifests disclose always-collected and default-collected data (per-library detail on Apple's SDK page, not read).
- **Not in pages read**: ATT/consent need, GDPR role, EU hosting. (T: Google acts as processor for Firebase under its data processing terms; Analytics storage region options are limited. Verify.)
- **Consent**: treat Analytics and non-essential identifiers as consent-gated in the EU (see `03` §3).
- **Declare (start)**: Device ID; Crash Data; Performance Data; Product Interaction; User ID if Auth; email/phone per Auth config.

### PostHog — V
Sources: https://posthog.com/docs/privacy · /privacy/gdpr-compliance · /privacy/data-collection.
- **Default (iOS)**: app opened/backgrounded/installed/updated, `$screen` (if screen capture on), `$rageclick`, `$autocapture` when `captureElementInteractions` is on. React Native touch capture is off by default (`captureTouches`).
- **Identifiers**: `distinct_id`; web cookies/localStorage; opt-out flag stored in iOS support directory `posthog.optOut` and Android SharedPreferences. PostHog states a persistent distinct ID "is considered Personal Data under GDPR".
- **IP**: captured by default; **EU Cloud** defaults IP capture to disabled for new projects; when discarded, "PostHog does not store client IP addresses with your events".
- **Session replay (mobile)**: selective unmasking not available.
- **Consent**: opt-out/opt-in APIs (`PostHogSDK.shared.optOut()` iOS, `PostHog.optOut()` Android); gate init.
- **GDPR role**: PostHog Cloud may be a data processor; self-serve **DPA** at app.posthog.com/legal on any plan including free. **EU hosting**: PostHog Cloud EU, Frankfurt, ingestion host `eu.i.posthog.com`.
- **Not in pages read**: ATT need, privacy manifest, Apple/Google label guidance.
- **Declare (start)**: Product Interaction (Analytics), Device ID/User ID if `identify` is used, Other Usage Data; plus User Content if replay captures it. Tracking = No unless data is combined with third-party data for ads.

### Sentry — V
Sources: https://docs.sentry.io/security-legal-pii/security/mobile-privacy/ · /scrubbing/ · /security/.
- Collects only data you configure; **does not use `Secure.ANDROID_ID` or the iOS `advertisingIdentifier`**; uses random per-device/app/install IDs reset on reinstall. PII becomes involved via user names, emails, attached logs.
- **Apple**: disclose as third-party SDK; standard purposes Analytics and App Functionality; examples Contact Info and Identifiers if you send them. Does not use IDFA, does not track. **Google**: disclose all data types collected; Sentry does not add ads.
- **ATT**: not needed. **Privacy manifest** and EU region and `send_default_pii` details: not in pages read. **DPA** listed under Legal and Compliance Documents; role not stated in pages read (T: processor).
- **Declare (start)**: Crash Data, Performance Data, Other Diagnostic Data; Device ID/User ID if `setUser` is used; keep `sendDefaultPii` off and scrub.

### Mixpanel / Amplitude / Segment — T
Typical: events with user IDs, device info, IP/geolocation (configurable), optional session replay (Mixpanel, Amplitude). Roles: processor for event data; Segment forwards to destinations (each destination is a recipient). Consent-gate; check region (EU residency options exist, verify). Declare Product Interaction, User ID, Device ID, Other Usage Data.

### Google Analytics 4 (web) — T
Cookies/identifiers; consent required in the EU; Consent Mode v2 for EEA ads/analytics signals; IP not logged; US transfers rely on DPF (V\* pending appeal). Italian regulator history on GA (see `10`).

### LogRocket / FullStory / Hotjar / Smartlook (session replay) — T
Records screens and inputs; consent + masking + visible indicator (Apple 2.5.14 **V**); exclude special-category screens and payment fields.

## Monetisation and attribution

### RevenueCat — V
Source: https://www.revenuecat.com/docs/platform-resources/apple-platform-resources/apple-app-privacy (the shorter app-privacy URL returned 404).
- **Apple label table**: **Purchases** required (RevenueCat collects purchase history). Identifiers "may be required": User ID if you use a custom app user ID; Device ID if you use IDFA-based integrations. Usage Data "may be required" if you use Mixpanel, Firebase, PostHog or Amplitude integrations. Contact Info "may be required" if you send name, email or phone as customer attributes. Location: only locale and currency code. Diagnostics: not required.
- **Purchase History**: select **Analytics** and **App Functionality** (both required); "Linked to Identity" depends on whether your app user ID maps to a person; RevenueCat "does not inherently use purchase history to track users".
- **ATT**: not stated (tracking depends on integrations). **Privacy manifest, GDPR role, EU hosting**: not in pages read.
- **Declare (start)**: Purchase History (Analytics, App Functionality), User ID/Device ID if applicable. Use anonymous IDs; avoid attributes with PII.

### AppsFlyer — V
Source: https://dev.appsflyer.com/hc/docs/preserve-user-privacy-ios-7.md.
- Install event sent on `start()` with attribution parameters. Identifiers: GAID, IDFA, IDFV, CUID, AppsFlyer ID, with IP address.
- `anonymizeUser` deletes GAID, IDFA, IDFV, CUID and hashes AppsFlyer ID and IP. `disableAdvertisingIdentifier` (iOS 14 and below); `disableIDFVCollection`. **Delay `start()` until consent**; call `setSharingFilterForPartners` before start.
- Attribution links user/device data with ad-network data → **tracking**: ATT + `NSPrivacyTracking` + tracking domains. Not in pages read: privacy manifest, label guidance, EU hosting.
- **Declare (start)**: Device ID, Advertising Data, Product Interaction; purposes Third-Party Advertising/Analytics; Tracking Yes.

### Adjust / Branch / Singular — T (Adjust page not read; 429)
Attribution SDKs: device IDs, IP, install/event data, ad-network matching → treat like AppsFlyer: consent-gated, ATT, tracking.

### Meta (Facebook) SDK / App Events — V
Source: https://developers.facebook.com/docs/app-events/overview (+ getting-started iOS).
- Default automatic events: App Install, App Launch, In-App Purchase plus app metadata. Crash report event "for Facebook Use Only", no user data.
- iOS: set `isAdvertiserTrackingEnabled` per ATT; plist opt-outs `FacebookAutoLogAppEventsEnabled=false`, `FacebookAdvertiserIDCollectionEnabled=false`. Meta: events sent "may require you to disclose these data types in the App Store Connect questionnaire".
- Not in pages read: manifest, GDPR role, Play Data safety.
- **Declare (start)**: Device ID, Product Interaction, Advertising Data, Purchase History (if purchase events); Tracking Yes if used for ads/measurement.

### Google AdMob / Google Mobile Ads — V (consent pages only)
Source: https://developers.google.com/admob/ios/privacy · /android/privacy.
- UMP: `requestConsentInfoUpdate` at every launch; `canRequestAds` false until then; privacy options entry point when required.
- Data types, ATT, manifest, label guidance: not in pages read. T: IDFA/AAID collection by default; ATT needed on iOS for personalised ads; `AD_ID` permission on Android 13+; Families: only certified ad SDKs.
- **Declare (start)**: Device ID, Advertising Data, Product Interaction, Location (coarse) if used; Third-Party Advertising; Tracking Yes for personalised ads.

### Stripe / Paddle / Lemon Squeezy — T
Payment processors: controller or processor depending on product (Stripe acts as independent controller for some processing). Apple: digital goods must use IAP (3.1.1). Declare Payment Info only if your app accesses it; card data stays with the processor (Play: payment data handled by Play Billing declared only if accessed).

## Backend and identity

### Supabase — V
Sources: https://supabase.com/docs/guides/platform/regions · /security/gdpr-compliance.
- Each project is deployed to **one primary region**; Postgres, Auth and Storage stay there. Choose a specific EU region (eu-central-1 Frankfurt, eu-west-1 Ireland, eu-west-3 Paris, eu-north-1 Stockholm), not the "Europe" group that includes London and Zurich (not EU member states).
- **DPA** available (supabase.com/legal/dpa, not read). Role not stated in pages read. Backups, logs, Edge Function execution and sub-processors can affect residency.
- Supabase is infrastructure: no label guidance; the app declares what **it** stores (auth email, profile fields, content).
- Audit: RLS on every personal table; storage bucket visibility; service-role key never in the client; deletion cascade including `storage.objects` (see `08`).

### Firebase Auth / Clerk / Auth0 / Cognito — T
Identity vendors: email/phone/name/profile/IP, device and sign-in logs. Roles: processor. Check MFA/session logs retention and EU region options.

### Sign in with Apple / Google Sign-In — T/V
Apple: name+email only, private relay, revoke tokens on deletion (**V**, Apple deletion page). Google Sign-In: profile scopes requested; Google is an independent controller for its own sign-in processing (T). Keep scopes minimal; Facebook Login adds Meta SDK obligations (see above).

### Expo (platform) — V
Sources: https://docs.expo.dev/guides/apple-privacy/ · /versions/latest/sdk/tracking-transparency/.
- Privacy manifests configured via `expo.ios.privacyManifests`; Expo SDK packages that use required-reason APIs ship a `PrivacyInfo.xcprivacy`. Apple may not parse all `PrivacyInfo` files from static CocoaPods: add reasons yourself.
- `expo-tracking-transparency` needs `NSUserTrackingUsageDescription`; denial → IDFA zeros; Android always "granted" and `getAdvertisingId` returns the AAID.
- App Store Connect label declarations are not covered by the Expo guide.

### OneSignal — T (docs index only)
Push provider: push token, external ID, tags, device model/OS/IP. OneSignal SDK is on Apple's manifest/signature list (**V**). Marketing pushes need opt-in (Apple 4.5.4). Declare Device ID, User ID, Product Interaction (if tags/events).

## Communication, maps, content

| Service | Likely data | Notes |
|---|---|---|
| **Twilio / SMS / WhatsApp APIs** | Phone numbers, message content, delivery logs | Processor; message content retention; consent for marketing |
| **Resend / SendGrid / Postmark / SES** | Email addresses, content, open/click tracking | Open/click tracking is device access → consent in EU for tracking pixels; processor |
| **Intercom / Crisp / Zendesk** | Identity, chat content, device/page metadata | Processor; widget identifiers on web need consent unless strictly necessary |
| **Google Maps / Mapbox** | Location queries, IP, device ID | Declare Location when sent; web embeds transmit IP |
| **Google Fonts / YouTube embed (web)** | IP address and referrer | Self-host fonts; load embeds after consent |
| **Cloudflare / CDN / WAF** | IP, request logs | Processor; security purposes; retention |
| **Vercel Analytics / Speed Insights** | Aggregated web vitals; Vercel states privacy-friendly modes | Verify cookies/identifiers and region for the configured product |

## Third-party AI APIs (LLMs, speech, vision) — T

Providers (OpenAI, Anthropic, Google Gemini, Mistral, ElevenLabs, Replicate and similar). For each integration record:

| Question | Why |
|---|---|
| Which user data goes in (text, images, audio, identifiers, files)? | Inventory rows; label/Data-safety User Content |
| Is it retained, and for how long? Used for training? Opt-out? | Purpose limitation, Art. 28, policy text |
| Is a **DPA** in place and what is the processing region? | Art. 28, transfers |
| Is there a user-facing disclosure and consent before the first send? | **Apple 5.1.2(i)** (V): disclose third-party AI sharing and get explicit permission |
| Can outputs include personal data about others? Is there a report path? | Apple 1.2 (V), Play AI-Generated Content (V) |
| Does the feature make decisions about people? | GDPR Art. 22; AI Act (see `ai-act-audit`) |

Verify each provider's current API data-usage terms before stating retention or training behaviour in the report; do not rely on this file for those facts.

## Cataloguing a new SDK (procedure)

1. Open the vendor's official privacy/data-collection page and its Apple/Google disclosure guidance, if any.
2. Record: data collected by default, identifiers, configurable PII, consent/ATT stance, privacy manifest status, GDPR role, DPA link, hosting region options.
3. Mark each fact **V** (read now) or "not in pages read".
4. Add the entry to the inventory vendor table; add label/Data-safety starting rows.
