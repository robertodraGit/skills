# 01 — Detection signals: where personal data hides

Search the whole repo, ignoring `node_modules/`, `Pods/`, `build/`, `.gradle/`, `DerivedData/`, `dist/`. Never print values of secrets or personal data; list names and paths.

## 1. What counts as personal data (for searching)

Anything that relates to an identified or identifiable person, directly or by an identifier (GDPR Art. 4(1), T-s). **Pseudonymous data is still personal data** (Art. 4(5), recital 26). Typical items:

- Direct: name, email, phone, postal address, photo, voice, government IDs, payment tokens, employee numbers.
- Online/device identifiers: user ID, device ID, IDFA/IDFV, AAID, Firebase installation ID, push tokens, cookie IDs, IP address, `distinct_id`, session IDs, fingerprints.
- Content: messages, uploads, support tickets, search queries, prompts sent to AI, free-text fields.
- Behavioural: events, screen views, session recordings, clickstreams, purchase history.
- Location: GPS, Wi-Fi/Bluetooth scans, IP geolocation.
- Special categories (Art. 9): health, biometric (for identification), genetic, racial/ethnic origin, political/religious/philosophical beliefs, union membership, sex life/orientation. Plus criminal-conviction data (Art. 10).

## 2. Collection points

| Where | Patterns | Note |
|---|---|---|
| Forms and sign-up | `<input name=`, `TextInput`, `email`, `phone`, `birth`, `dob`, `firstName`, `lastName`, `address`, `zip` | Mark required vs optional (minimisation, Apple 5.1.1(x)) |
| Auth | `signUp`, `createUser`, `auth.users`, `signInWith`, `oauth`, `apple-authentication`, `google-signin` | Third-party login scopes: what profile data is requested? |
| Permissions | `NSCameraUsageDescription` … (see store-review `apple-06` G-A5), `AndroidManifest uses-permission`, `PermissionsAndroid`, `requestPermissionsAsync` | Each permission = potential collection |
| Uploads | `upload`, `storage.from(`, `S3`, `putObject`, `FormData`, `multipart` | Files may hold faces, documents, EXIF GPS |
| Device/browser data | `navigator.userAgent`, `Device.`, `DeviceInfo`, `getUniqueId`, `ANDROID_ID`, `identifierForVendor`, `advertisingIdentifier`, `localStorage`, `sessionStorage`, `document.cookie`, `AsyncStorage`, `MMKV`, `SecureStore`, `Keychain` | What is stored locally and is it sent off-device? |
| Location | `Geolocation`, `expo-location`, `CLLocationManager`, `FusedLocationProvider`, `ip-api`, `ipinfo`, `geoip` | Precision, frequency, background |
| Biometrics | `LocalAuthentication`, `FaceID`, `BiometricPrompt`, `faceapi`, `vision` | On-device match only (no template leaves device) = not "collected" in Apple's sense |
| AI inputs | `chat.completions`, `messages:`, `generateContent`, `prompt`, `embedding`, `vector`, `rag` | User text and files to a third-party model |
| Support/contact | `intercom`, `zendesk`, `crisp`, `helpscout`, `mailto:`, `contact` | Free-text content and identity |

## 3. Storage and backends

| Where | Patterns | Check |
|---|---|---|
| SQL schemas/migrations | `CREATE TABLE`, `supabase/migrations`, `prisma/schema.prisma`, `drizzle`, `typeorm`, `knex`, `alembic`, `*.sql` | Columns holding personal data; `ON DELETE CASCADE`; RLS policies; retention columns (`deleted_at`, `expires_at`) |
| NoSQL/rules | `firestore.rules`, `database.rules.json`, `mongoose.Schema` | Access control over personal docs |
| Object storage | Supabase Storage buckets, S3, GCS, Firebase Storage rules | Public buckets with personal files; deletion on account removal |
| Logs/telemetry | `console.log(user`, `logger.info(`, `Sentry.setUser`, `datadog`, `LogRocket`, server access logs | Personal data in logs; retention |
| Email/SMS | `resend`, `sendgrid`, `postmark`, `twilio`, `nodemailer`, `ses` | Content and recipient lists |
| Payments | `stripe`, `paddle`, `lemonsqueezy`, `revenuecat` | Customer objects, metadata with PII |
| Environment | `.env*` **names only**, `process.env.`, `Constants.expoConfig.extra` | Which vendors are connected (key names reveal them) |
| Infra | `vercel.json`, `fly.toml`, `serverless.yml`, `terraform`, region settings | Where data lives (transfers). **Supabase region hides in the pooler host** (`aws-N-<region>.pooler.supabase.com`, e.g. `us-east-2` = Ohio) and in agent/runbook notes: search `pooler.supabase.com`, `eu-central`, `us-east` |
| Existing compliance docs | `docs/compliance/`, `docs/store/`, privacy page source (`app/privacy/page.tsx`), `PRIVACY`, `GDPR`, `store-privacy-declarations` | Treat as claims to diff against the inventory (Step 7), not as evidence |
| Push campaigns | `push_broadcasts`, `broadcast`, `campaign`, `notification_prefs` | Promotional vs service notices; per-user preference (Apple 4.5.4, marketing consent) |
| Backups | pg_dump scripts, snapshot settings | Deletion vs backups |

## 4. Outbound flows (recipients)

- Domains and base URLs: search `https?://[a-z0-9.-]+` in source and config; unique non-first-party hosts become vendor rows.
- SDK init calls: `Sentry.init`, `posthog.init`, `PostHog(`, `Purchases.configure`, `Analytics.`, `FirebaseApp.configure`, `AppsFlyer`, `Adjust.create`, `OneSignal.initialize`, `Branch`, `Amplitude.init`, `mixpanel`, `GADMobileAds.start`, `Facebook` SDK flags, `Segment`.
- Dependency manifests: `package.json`, `Podfile.lock`, `Package.resolved`, `build.gradle` deps, `pubspec.lock`.
- Native config: `GoogleService-Info.plist`, `google-services.json` (Firebase), `Info.plist` SDK keys (e.g. `FacebookAppID`, `FacebookAutoLogAppEventsEnabled`, `FacebookAdvertiserIDCollectionEnabled`), `AndroidManifest` meta-data (e.g. `com.google.android.gms.ads.APPLICATION_ID`, `firebase_analytics_collection_enabled`).
- Server-side calls from edge functions/API routes to third parties.
- Web: `<script src=`, tag managers (`gtm.js`), pixels (`fbq(`, `gtag(`, `ttq`), embedded fonts/maps/video (Google Fonts, YouTube, Maps) that transmit the IP.

For each SDK found, open `06-sdk-catalog.md`.

## 5. Build-level evidence

```bash
# Merged Android manifest (permissions, SDK meta-data, services)
bundletool dump manifest --bundle=app.aab
apkanalyzer manifest print app.apk

# iOS: aggregated privacy report (Xcode): Product > Archive > Generate Privacy Report
find . -name PrivacyInfo.xcprivacy -not -path "*/node_modules/*"
plutil -p path/to/Info.plist | rg "UsageDescription|Facebook|GAD|Firebase"

# Third-party hosts contacted by the JS bundle
rg -o "https?://[a-zA-Z0-9.-]+" dist/ build/ --no-filename | sort -u
```

Runtime network capture (proxy, `mitmproxy`, Charles) gives **N** evidence about what really leaves the device before and after consent. Ask the user to run it and share domains and payload field names, not payloads with real data.

## 6. Output of this step

Fill the three tables of `assets/data-inventory-template.md`: **processing activities**, **data items**, **vendors/recipients**. Every SDK from §4 appears in the vendor table with the evidence path where it was found.
