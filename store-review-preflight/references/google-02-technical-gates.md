# Google 02 — Technical gates (Play Console and build)

Status as of **2026-11-05**. Sources read on that date: Android target-SDK requirement page, Play Data safety, new-account testing requirement, account deletion, App content, page-size guide, Advertising ID, developer verification, Policy Deadlines table. Confidence per row.

## 1. Gate list

### G-G1 Target API level — **V**

Source: https://developer.android.com/google/play/requirements/target-sdk

- Since **2026-08-31** new apps and updates must **target Android 16 (API 36) or higher**. Exceptions: Wear OS and Android Automotive OS API 35+; Android TV and Android XR API 34+. Permanently private organisation apps are exempt.
- Existing apps must target **API 35+** to stay available to new users on devices running a newer OS than their target. Apps targeting older levels are offered only on devices at or below their target.
- Extension to **2026-11-01** was possible via a Play Console request; that window has passed. Confirm in Play Console whether anything is still open.

Check: `targetSdk` in Gradle; Expo: `expo-build-properties` → `android.targetSdkVersion`; Capacitor: `variables.gradle` (`targetSdkVersion`). Red if < 36 for new submissions/updates.

### G-G2 16 KB memory page size — **V**

Source: https://developer.android.com/guide/practices/page-sizes

- Rule (verbatim): all apps targeting Android 15 (API 35) and higher must support 16 KB memory page sizes on 64-bit devices on Google Play. **From 2027-02-01, updates that do not support it cannot be released.**
- Affects apps with native code (NDK, or SDKs shipping `.so` libraries: React Native/Hermes, game engines, ML, camera, crypto). Pure Java/Kotlin apps comply but should be tested.
- Tooling: AGP 8.5.1+ and NDK r28+ compile 16 KB-aligned by default. NDK r27 and lower: add `-Wl,-z,max-page-size=16384 -Wl,-z,common-page-size=16384`.
- Verify: `zipalign -c -P 16 -v 4 app.apk`; on a test device `adb shell getconf PAGE_SIZE` returns 16384.

Check: native libs in the AAB (`unzip -l app.aab | rg "\.so"`), versions of React Native / game engine / SDKs. Status 🟠 until alignment is proven; 🔴 after 2027-02-01 if unaligned.

### G-G3 Data safety form — **V**

Source: https://support.google.com/googleplay/android-developer/answer/10787469 (change log to 2023-12-05; form content current)

- Required for every published app (closed, open, production tracks; pregranted/preloaded). **Internal-testing-only** apps are exempt. Apps collecting nothing must still complete it and link a privacy policy.
- **Collection** = transmitting data off the device (including via SDKs). On-device-only processing need not be declared. **Ephemeral** processing (in memory for the real-time request, not retained) must still be answered but is not displayed; building ad or user profiles cannot be ephemeral.
- **Sharing** = transfer to a third party. Exceptions: service providers acting only on your behalf, legal requests, user-initiated actions or consented disclosures, fully anonymised data. Declare pseudonymous data. Declare payment data processed by Google Play Billing only if your app never accesses it.
- Each type is **required** or **optional**; if any version requires it, mark required.
- **Data types**: Location (approximate, precise); Personal info (name, email, user IDs, address, phone, race/ethnicity, political/religious beliefs, sexual orientation, other); Financial info (payment info, purchase history, credit score, other); Health and fitness; Messages (emails, SMS/MMS, in-app messages); Photos and videos; Audio files; Files and docs; Calendar; Contacts; App activity (interactions, in-app search history, installed apps, other user-generated content, other actions); Web browsing; App info and performance (crash logs, diagnostics, other performance data); Device or other IDs (advertising ID, Firebase installation ID, etc.).
- **Purposes**: App functionality, Analytics, Developer communications, Advertising or marketing, Fraud prevention/security/compliance, Personalisation, Account management.
- **Security practices**: encryption in transit ("industry standard", TLS/HTTPS); whether users can request deletion (in-app feature, contact form, dedicated email alias; or automatic deletion/anonymisation within 90 days qualifies). Optional badges: independent security review (MASA/OWASP MASVS via authorised lab), Play Families commitment, UPI (India).
- Process: Play Console → App content → Data safety; CSV export/import (import overwrites). Reviewed with the app. Misrepresentation → required fixes, blocked updates or removal.

Check: derive answers from the SDK inventory (`privacy-audit` `references/05-google-data-safety.md`), compare to the console export the user pastes. A collected type missing from the form → 🔴.

### G-G4 Account deletion — **V**

Sources: https://support.google.com/googleplay/android-developer/answer/13327111 and the User Data policy.

- App allows account creation → **both** (1) an in-app path to delete the account and associated data, and (2) a **web link** where users can request deletion without reinstalling the app.
- The web link must work, reference the app or developer name as listed on the store, and feature the deletion path prominently. If steps such as cancelling a subscription are needed, spell them out and provide a support path.
- Data kept for security, fraud prevention or regulatory reasons disclosed in the privacy policy.
- Exempt: permanently private apps and enterprise device-management apps. Non-mobile surfaces (TV, Wear OS, web) need only a web link.
- Deadlines (2023-12-07, extension to 2024-05-31) have passed; non-compliant apps risk enforcement.
- Also answer the **Data deletion** questions in the Data safety form.

Check: in-app flow (C); web URL in Play Console (K) loads logged-out and names the app.

### G-G5 Testing requirement for new personal accounts — **V**

Source: https://support.google.com/googleplay/android-developer/answer/14151465

- Applies to **personal** developer accounts created after **2023-11-13**.
- Run a **closed test** with **≥ 12 testers continuously opted in for ≥ 14 consecutive days**. Production and Pre-registration stay disabled until met. Opt-out/opt-in resets a tester's count.
- Then apply for production access: about the closed test (recruitment ease, engagement, feedback), about the app (target audience, value proposition, estimated installs), production readiness. Review usually ≤ 7 days; may require more testing if fewer than 12 opted-in testers or low engagement.
- Open testing becomes available only after production access.

Check (K): account type and creation date; if new personal account, plan the 14 days **before** the target launch date. Organisation accounts are not subject to this requirement (T: verify on the live page).

### G-G6 App content declarations — **V**

Source: https://support.google.com/googleplay/android-developer/answer/9859455

| Declaration | Requirement |
|---|---|
| Privacy policy | Public http(s) URL with valid SSL, accessible worldwide without login, HTML page (not PDF), specific to the app; required on the listing **and in-app**, even with no sensitive data |
| Ads | Yes/No; third-party SDK and house ads count; "More Apps" cross-promotion does not; misrepresentation → suspension |
| App access / sign-in | Instructions for restricted content; up to five instruction sets (→ demo credentials, see `assets/review-notes-template.md`) |
| Target audience and content | Age groups; if children included, Families policy applies |
| Permissions declaration | Required for high-risk/sensitive permissions (SMS, Call Log, all-files, photo/video, background location…) |
| Content ratings | IARC questionnaire per app; unrated apps may be removed |
| Data safety | G-G3 |

### G-G7 Advertising ID — **V**

Source: https://support.google.com/googleplay/android-developer/answer/6048248

- Apps targeting Android 13+ must declare `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>` if they use the advertising ID (an ads SDK may already declare it). Use AAID for advertising; for non-ad uses (analytics, fraud) prefer **App Set ID**.
- Advertising ID is a "Device or other IDs" type in Data safety. Check the user opt-out at each access.
- Check: merged manifest (`bundletool dump manifest`) for `AD_ID`; if the app does **not** use ads and the manifest still carries `AD_ID` from an SDK, decide on removal (`tools:node="remove"`) and make Data safety consistent.

### G-G8 Developer verification — **V\***

Source: https://developer.android.com/developer-verification

- Effective **2026-09-30**: protections begin for users installing apps from participating stores in select regions (Brazil, Indonesia, Singapore, Thailand) on certified Android devices; global rollout planned for **2027**.
- Paths: distributing only outside Play → Android Developer Console; on or outside Play → Play Console (Play registers most apps automatically). The Policy Deadlines table also lists **2026-09-30**: register Play apps in Play Console to avoid global removal (announced 2026-07-15).
- Check (K): app registered in Play Console; signing key registered.

### G-G9 Other build gates — **T** (stable)

| Gate | Check |
|---|---|
| **App Bundle (.aab)** required for new apps | Build produces `.aab`; Play App Signing enrolled |
| **Foreground service types** (Android 14+) | Each `<service android:foregroundServiceType>` matches a real use and a Play Console declaration where required |
| **POST_NOTIFICATIONS** (Android 13+) | Runtime request in context; app works with it denied |
| **Exact alarms** (`USE_EXACT_ALARM`, `SCHEDULE_EXACT_ALARM`) | Core alarm/calendar function only |
| **`android:exported`** explicit on every component with an intent filter | Manifest lint |
| **Cleartext traffic** | `usesCleartextTraffic` off; `network_security_config.xml` reviewed |
| **Backup rules** | `data_extraction_rules.xml` excludes sensitive data from backups |
| **64-bit** native libs | `arm64-v8a` present |
| **Crash/ANR rates** (Android vitals bad-behaviour thresholds) | Check the vitals dashboard (K) |

Re-verify any `T` row on the live developer.android.com / Play Console help page before 🔴.

## 2. Gate summary table (copy into the report)

| Gate | Evidence | Status |
|---|---|---|
| G-G1 targetSdk ≥ 36 (new apps/updates) | C, B | |
| G-G2 16 KB page alignment | B | |
| G-G3 Data safety matches SDK inventory | K, C | |
| G-G4 Account deletion in-app + web link | C, K | |
| G-G5 New personal account: 12 testers × 14 days | K | |
| G-G6 App content declarations complete | K | |
| G-G7 AD_ID permission consistent | B, K | |
| G-G8 Developer verification / Play registration | K | |
| G-G9 Bundle, FGS types, notifications, exported, cleartext | C, B | |

## 3. Upcoming deadlines — **V** (Policy Deadlines table, latest announcement 2026-10-29)

| Date | Change | Notes |
|---|---|---|
| 2026-08-26 (passed) | Families, Child Endangerment and Age-Restricted Content policies expanded to anonymous and random chat apps | Check chat features |
| 2026-09-30 (passed) | Android developer verification: register Play apps in Play Console | G-G8 |
| 2027-01-27 | Contacts permission: broad contacts access restricted; use the Android Contact Picker. Location: apps targeting **Android 17 (API 37+)** must use the Android location button for one-time/infrequent location; `ACCESS_FINE_LOCATION` needs a declaration | Plan now if targeting API 37 |
| 2027-01-27 | SMS/call log: account verification by phone call no longer a permitted `READ_CALL_LOG` use; use Digital Credentials API or SMS Retriever | — |
| 2027-01-27 | Foreground service/full-screen intent: geofencing no longer an approved foreground-service use; use the Geofence API | — |
| 2027-01-27 | Subscriptions with ongoing eligibility-based discounts must disclose eligibility, verification and post-eligibility pricing | — |
| 2027-02-01 | 16 KB page size enforced for updates (G-G2) | — |
| 2027-04-14 | AppFunctions API must not deceive/manipulate AI agents, bypass security, or interfere with other apps | — |
| 2027-08-25 | Manage Contacts restricted to core functionality where pickers are insufficient (API 38+); Local Network permission restricted to core functionality with a declaration (API 37+) | — |

Date statuses relative to 2026-11-05. Re-open the live table (see `00-method.md` §4) for later runs.
