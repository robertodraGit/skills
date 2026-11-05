# 08 — Stack notes

Where each stack hides the settings the gates and rules need. Confidence **T** unless stated; verify key names against the framework docs of the installed version.

## Expo (managed or prebuild)

| Topic | Where / how | Pitfall |
|---|---|---|
| Usage descriptions | `expo.ios.infoPlist` and per-module config plugins (e.g. `expo-camera`, `expo-location`, `expo-image-picker` plugin options) | Plugin defaults are generic ("Allow $(PRODUCT_NAME) to access your camera"); 5.1.1(ii) wants specific strings. Override them |
| Privacy manifest | `expo.ios.privacyManifests` with `NSPrivacyAccessedAPITypes` (reason codes such as `CA92.1`). **V**: Expo's Apple privacy guide documents this; Expo SDK packages ship a `PrivacyInfo.xcprivacy` | **V**: "Apple does not correctly parse all the PrivacyInfo files included by static CocoaPods dependencies" — add reasons yourself when `ITMS-9105x` appears |
| Tracking | `expo-tracking-transparency` + plugin option `userTrackingPermission` writes `NSUserTrackingUsageDescription` (**V**: Apple rejects without the string when ATT is used) | Importing the module without a tracking use still adds the string and invites the question; include only when needed |
| Export compliance | `expo.ios.config.usesNonExemptEncryption` | Missing → upload prompts every time |
| Android permissions | `expo.android.permissions` (allow-list), `expo.android.blockedPermissions` | Modules and SDKs add permissions on merge; inspect the **merged manifest**, remove unused ones (`blockedPermissions`) |
| targetSdk / compileSdk | `expo-build-properties` → `android.targetSdkVersion`, `compileSdkVersion` | Expo SDK version bounds the maximum; plan SDK upgrades around G-G1 deadlines |
| 16 KB pages | Expo SDK / React Native version; NDK; third-party native libs | Upgrade RN/NDK; verify with `zipalign -P 16` on the produced APK |
| Build image | `eas.json` → `build.<profile>.ios.image` / `android.image` | **V** G-A1: Xcode 26 required for new uploads; pin an image with Xcode 26 |
| Entitlements | `expo.ios.entitlements`, capabilities via config plugins | Unused capabilities (push, background modes, App Groups) are reviewer questions |
| OTA updates | `expo-updates` (`updates.enabled`, `runtimeVersion`, channels) | See §OTA below |
| Bare/prebuild drift | After `expo prebuild`, `ios/` and `android/` become the source of truth if committed | Record which wins; fix both |

## Capacitor / Cordova (WebView shells)

| Topic | Where / how | Pitfall |
|---|---|---|
| Native projects | `ios/App`, `android/app` are committed; edit Info.plist, Manifest and Gradle there | Plugin installs do **not** add Info.plist strings; add them by hand |
| `server.url` | `capacitor.config.*` → `server.url` loads a remote site | **V** 4.2: a shell around a website with no native value is a minimum-functionality rejection. Remove `server.url` for production builds |
| SDK listing | **V** Capacitor and Cordova are on Apple's list of SDKs requiring manifests/signatures (G-A4) | Use a Capacitor version that ships `PrivacyInfo.xcprivacy`; verify in the Pods |
| Plugins with native SDKs | Community plugins (purchases, push, analytics, auth) pull SDKs with their own data flows | Enter every plugin into the SDK inventory |
| Live updates | Ionic Appflow / Capacitor live-updates | See §OTA |
| Android | `variables.gradle` for `targetSdkVersion`, `minSdkVersion` | G-G1 |
| WebView content | Web app served inside the shell | Reviewers see a website: lead with native features in the notes |

## React Native CLI / Flutter / native

- RN: Hermes is on the Apple SDK list (**V**); keep RN current for manifests and 16 KB support. Pods listed in G-A4 appear through RN modules (e.g. `RNCAsyncStorage` → UserDefaults/file APIs).
- Flutter: **V** the Apple list includes Flutter and many `*_plus`, `path_provider`, `shared_preferences`, `url_launcher`, `sqflite`, `webview_flutter_wkwebview`, `image_picker_ios`, `file_picker`, `geolocator_apple`, `flutter_local_notifications`, `video_player_avfoundation`. Check each plugin version ships a manifest.
- Native iOS: SPM packages and XCFrameworks need signatures when on the list. Native Android: dependency catalog audit for ad/analytics SDKs.

## OTA code updates (Expo Updates, CodePush, Live Updates)

**Rule**: Apple 2.5.2 (**V**): apps may not download, install or execute code that introduces or changes features or functionality. Apple's developer agreement permits downloaded interpreted code only when it does not change the app's primary purpose and does not bypass review (T: agreement text, re-read before 🔴).

Practical test:

1. List what an OTA can change: JS bundle logic, assets, config.
2. Could a payload add a feature the reviewer never saw, or switch the app's purpose, unlock paid content outside IAP, or hide behaviour in certain regions? → 🟠 minimum; 🔴 when intentional.
3. Document the update policy in the review notes: "OTA updates deliver bug fixes and minor UI changes within the reviewed functionality; features requiring review ship as store builds."
4. Google Play has a parallel Device and Network Abuse policy on loading executable code from outside Play (**T**, read the live article); JS bundles interpreted by an engine bundled in the app are the usual accepted pattern.

## Common config files to attach as evidence

`app.json`/`app.config.*`, `eas.json`, `capacitor.config.*`, `Info.plist`, `*.entitlements`, `PrivacyInfo.xcprivacy`, `AndroidManifest.xml` (merged), `build.gradle`, `Podfile.lock`.
