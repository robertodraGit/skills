# 01 — Signals: stack detection and capability search

Adapt patterns to the stack found in §1. Search the whole repo, but ignore `node_modules/`, `Pods/`, `build/`, `.gradle/`, `DerivedData/`.

## 1. Stack detection

| Stack | Fingerprint | Where the truth lives |
|---|---|---|
| **Expo (managed)** | `app.json` / `app.config.(js|ts)` with `expo`, `eas.json`, no `ios/` or `android/` folders | App config (`ios.infoPlist`, `ios.privacyManifests`, `android.permissions`, `plugins`), `eas.json`, config plugins |
| **Expo (prebuild / bare)** | Expo + committed `ios/` and `android/` | Native files win over app config after prebuild; check both and note drift |
| **React Native CLI** | `react-native` in `package.json`, `ios/*.xcodeproj`, `android/app/build.gradle` | Native projects + `package.json` |
| **Capacitor** | `capacitor.config.(ts|json)`, `@capacitor/*`, `ios/App`, `android/app` | Native projects (committed), `capacitor.config`, plugin list in `package.json` |
| **Cordova** | `config.xml`, `platforms/` | `config.xml`, platform folders |
| **Flutter** | `pubspec.yaml`, `ios/Runner`, `android/app` | `pubspec.yaml` plugins, native folders |
| **Native iOS** | `*.xcodeproj` / `Package.swift` / `Podfile` | Info.plist, entitlements, PrivacyInfo.xcprivacy, SPM/Pods |
| **Native Android** | `build.gradle(.kts)`, `AndroidManifest.xml` | Manifest, Gradle, version catalogs |
| **Unity / other game engines** | `ProjectSettings/`, `UnityFramework` | Export settings + generated Xcode/Gradle projects |

Record the stack, the framework version (Expo SDK, RN, Capacitor major) and whether native folders are committed.

## 2. Files to open in every run

| Platform | Files |
|---|---|
| iOS | `Info.plist`, `*.entitlements`, `PrivacyInfo.xcprivacy` (app and each framework/SDK), `Podfile.lock` / `Package.resolved`, `project.pbxproj` (`IPHONEOS_DEPLOYMENT_TARGET`, bundle id, version), `ExportOptions.plist`, `fastlane/metadata/` |
| Android | `AndroidManifest.xml` (all variants), `app/build.gradle(.kts)` (`targetSdk`, `compileSdk`, `minSdk`, `versionCode`), `gradle/libs.versions.toml`, `proguard-rules.pro`, `res/xml/network_security_config.xml`, `res/xml/data_extraction_rules.xml` |
| Expo | `app.json` / `app.config.*`, `eas.json`, `package.json` (`expo` version, `expo-*` modules), `plugins/` |
| All | `package.json`/`pubspec.yaml` dependencies, `.env*` **names only** (never print values), privacy policy / ToS files, `store/` or `fastlane/` metadata, `CHANGELOG`, release notes |

### Stale native folders

When `ios/` and `android/` are gitignored or generated (Expo prebuild), they are **disposable and often stale**: compare their deployment target, purpose strings, permissions and version against the config (`app.config.*`). Config wins. Mark native-folder evidence as stale in the report, and ask for the real artifact (IPA/AAB) or its merged manifest/plist for gates that need it. Merged manifests add permissions (e.g. `POST_NOTIFICATIONS`, `CAMERA`) that the source manifest does not show.

## 3. Capability signals

Search each row; record found / not found with paths.

| Capability | Search patterns (case-insensitive) | Also check |
|---|---|---|
| **Account / auth** | `signUp`, `createUser`, `register`, `signInWith`, `auth.`, `supabase.auth`, `firebase/auth`, `clerk`, `auth0`, `next-auth`, `passport` | Is there a visible in-app delete-account path? `deleteAccount`, `delete_user`, `account/delete`, `deleteUser` |
| **Social / third-party login** | `google-signin`, `GoogleSignIn`, `FBSDKLoginKit`, `react-native-fbsdk`, `signInWithPopup`, `apple-authentication`, `AppleAuthentication`, `signInWithApple`, `authorization_code` | If a third-party login exists, is Sign in with Apple (or equivalent) also offered? Is Apple token revoked on deletion? |
| **IAP / subscriptions** | `StoreKit`, `SKPayment`, `Product.purchase`, `react-native-iap`, `expo-in-app-purchases`, `react-native-purchases`, `RevenueCat`, `BillingClient`, `@capacitor-community/in-app-purchases`, `cordova-plugin-purchase` | Restore purchases (`restorePurchases`, `restoreTransactions`), price/terms text, trial copy |
| **External payments** | `stripe`, `paypal`, `braintree`, `checkout.session`, `paymentIntent`, `window.open(.*checkout`, `Linking.openURL(.*(pay|checkout|subscribe))` | Is it for digital goods (3.1.1) or physical goods/services (3.1.3(e))? |
| **UGC / social** | `comment`, `post`, `chat`, `message`, `upload`, `report`, `block`, `moderation`, `flag`, `abuse` | Report, block, filter, published contact, moderation SLA |
| **Generative AI** | `openai`, `anthropic`, `gemini`, `generateContent`, `chat.completions`, `llm`, `stable-diffusion`, `replicate`, `elevenlabs`, `whisper` | Does user data go to a third-party AI? Is there consent? Can users report AI output? |
| **Kids** | `kids`, `children`, `age`, `birthdate`, `COPPA`, `parental`, `parentalGate`; store category "Kids", Play target audience | Third-party analytics/ads in a kids app |
| **Health** | `HealthKit`, `HKHealthStore`, `react-native-health`, `health-connect`, `GoogleFit`, `step`, `heart`, `bloodPressure`, `medical`, `dosage` | Claims of measuring vitals with the camera/sensors |
| **Location** | `CLLocationManager`, `expo-location`, `geolocation`, `ACCESS_FINE_LOCATION`, `ACCESS_BACKGROUND_LOCATION`, `requestAlwaysAuthorization` | Background/Always justification, coarse vs fine |
| **Camera / mic / screen** | `AVCaptureSession`, `expo-camera`, `getUserMedia`, `RECORD_AUDIO`, `ReplayKit`, `MediaRecorder`, `react-native-vision-camera` | Visible recording indicator and consent |
| **Photos / contacts / files** | `PHPhotoLibrary`, `expo-image-picker`, `expo-contacts`, `READ_CONTACTS`, `READ_MEDIA_IMAGES`, `READ_EXTERNAL_STORAGE`, `MANAGE_EXTERNAL_STORAGE`, `expo-document-picker` | System picker vs full library access |
| **Ads** | `AdMob`, `GADMobileAds`, `react-native-google-mobile-ads`, `ironSource`, `AppLovin`, `Unity Ads`, `Meta Audience Network`, `AD_ID` | Consent (UMP), ATT, Kids/Families gating |
| **Analytics / attribution / crash** | `posthog`, `amplitude`, `mixpanel`, `segment`, `firebase/analytics`, `appsflyer`, `adjust`, `branch`, `singular`, `sentry`, `bugsnag`, `crashlytics`, `datadog` | Each one: data collected, consent gate, privacy manifest |
| **Tracking / IDFA** | `ATTrackingManager`, `requestTrackingPermission`, `expo-tracking-transparency`, `advertisingIdentifier`, `IDFA`, `AAID`, `getAdvertisingId`, `fingerprint` | `NSUserTrackingUsageDescription`, `NSPrivacyTracking`, tracking domains |
| **WebView shell** | `WebView`, `WKWebView`, `react-native-webview`, `InAppBrowser`, `server.url` in `capacitor.config`, `<iframe` to own site, `Linking.openURL` for core flows | Does the app offer native value beyond the website? |
| **OTA code updates** | `expo-updates`, `Updates.checkForUpdateAsync`, `codepush`, `appcenter`, `Capacitor Live Updates`, `Ionic Appflow`, `eval(`, `new Function(`, downloaded `.js` bundles | What can an OTA change? Does it alter the app's primary purpose or add features beyond review? |
| **Push** | `UNUserNotificationCenter`, `expo-notifications`, `firebase/messaging`, `OneSignal`, `POST_NOTIFICATIONS`, `broadcast`, `campaign`, `push_broadcasts`, `notification_prefs` | Required for function? **Broadcast/campaign tables mean promotional pushes**: is there a per-user promotional opt-in and opt-out (Apple 4.5.4)? Sensitive content or message previews in payload? |
| **Env-gated features** | `EXPO_PUBLIC_*_ENABLED`, `process.env.APP_ENV`, `FREE_RELEASE`, `SKIP_`, `DEV_` in `app.config.*`, `env.js`, `eas.json` | Production value of each flag (K); guards against dev bypasses shipping (`DEV_SKIP_OTP`, dev credentials) on **both** platforms |
| **Background modes** | `UIBackgroundModes`, `FOREGROUND_SERVICE`, `foregroundServiceType`, `WorkManager`, `BGTaskScheduler`, `expo-background-fetch`, `expo-task-manager` | Each mode maps to a legitimate declared use |
| **Dynamic content/feature flags hiding features** | `featureFlag`, `isReviewer`, `reviewMode`, `if (.*demo` | Hidden or reviewer-only code paths (2.5.19) |
| **Crypto / finance / gambling** | `wallet`, `web3`, `ethers`, `walletconnect`, `bet`, `casino`, `lottery`, `loan`, `forex`, `trading` | Entity type, licences, geo-restriction |
| **Extensions** | `*Extension` targets in `project.pbxproj`, `WidgetKit`, `AppIntents`, `NSExtension`, App Clip target, keyboard extension | Ads/IAP in extensions, relevance |
| **Mini apps / plug-ins** | `miniapp`, `plugin`, `sandbox`, downloaded HTML5 bundles, emulator cores | Catalog, filtering, age restriction |
| **Hardware / sensors** | `CoreBluetooth`, `NFC`, `ARKit`, `CoreMotion`, `BLUETOOTH_SCAN`, `NFC` | Usage descriptions, Play declarations |

## 4. Gate commands (collect early)

```bash
# iOS source tree
find . -name PrivacyInfo.xcprivacy -not -path "*/node_modules/*" -not -path "*/Pods/*"
rg -n "IPHONEOS_DEPLOYMENT_TARGET|PRODUCT_BUNDLE_IDENTIFIER|MARKETING_VERSION" --glob "*.pbxproj"
plutil -p ios/*/Info.plist | rg "UsageDescription|ITSAppUsesNonExemptEncryption|UIBackgroundModes|NSAppTransportSecurity"

# iOS build artifact (.ipa)
unzip -p App.ipa 'Payload/*.app/Info.plist' > /tmp/Info.plist && plutil -p /tmp/Info.plist
unzip -l App.ipa | rg "PrivacyInfo.xcprivacy"
codesign -dv --verbose=4 path/to/Payload/App.app

# Android source tree
rg -n "targetSdk|compileSdk|minSdk|versionCode" --glob "*.gradle*" --glob "*.toml"
rg -n "uses-permission|uses-feature|foregroundServiceType|android:exported" --glob "AndroidManifest.xml"

# Android build artifact (.aab / .apk)
bundletool dump manifest --bundle=app.aab
apkanalyzer manifest print app.apk
zipalign -c -P 16 -v 4 app.apk          # 16 KB page-size alignment (native libs)
```

Write command output into the report as evidence. When a command cannot run (tool missing, no artifact), mark the gate ❓ and give the user the command.

## 5. Output of this step

A capability table:

| Capability | Found? | Paths | Notes |
|---|---|---|---|

Use it as the input to the triage matrix in `00-method.md` §5.
