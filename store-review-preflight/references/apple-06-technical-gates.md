# Apple 06 — Technical gates (build and upload)

Gates fail an upload or a review regardless of opinion. Status as of **2026-11-05**. Confidence per row. Evidence class **B** (build artifact) is usually needed; mark ❓ with the command when no artifact exists.

## G-A1 Toolchain and deployment target — **V**

Source: Apple *Upcoming requirements*.

| Requirement | Since |
|---|---|
| Apps uploaded to App Store Connect must be built with **Xcode 26 or later** using an **SDK for iOS 26 / iPadOS 26 / tvOS 26 / visionOS 26 / watchOS 26** | 2026-04-28 |
| iOS and iPadOS apps uploaded must target **iOS 13 or later** | 2026-09-09 |

Check: `xcodebuild -version`, `xcodebuild -showBuildSettings | rg "SDKROOT|IPHONEOS_DEPLOYMENT_TARGET"`; Expo: `expo.ios.deploymentTarget` or `expo-build-properties`; EAS build image version in `eas.json`. Red when Xcode < 26 or deployment target < 13.

## G-A2 Privacy manifest — **V**

Source: Apple DocC *Privacy manifest files*, *Adding a privacy manifest*. File: `PrivacyInfo.xcprivacy`, at `App.app/PrivacyInfo.xcprivacy` (iOS); frameworks follow the same pattern. App Store Connect **rejects invalid manifests**; since **2025-02-12** apps must include valid manifests for a set of commonly used third-party SDKs (G-A4).

Top-level keys:

| Key | Type | Meaning |
|---|---|---|
| `NSPrivacyTracking` | Boolean | App or SDK uses data for tracking as defined by ATT. If `true`, provide `NSPrivacyTrackingDomains` |
| `NSPrivacyTrackingDomains` | Array of strings | Domains that engage in tracking. **If the user has not granted ATT, network requests to these domains fail** |
| `NSPrivacyCollectedDataTypes` | Array of dicts | Data types collected: `NSPrivacyCollectedDataType`, `NSPrivacyCollectedDataTypeLinked` (Boolean), `NSPrivacyCollectedDataTypeTracking` (Boolean), `NSPrivacyCollectedDataTypePurposes` (array) |
| `NSPrivacyAccessedAPITypes` | Array of dicts | Required-reason API use: `NSPrivacyAccessedAPIType` (category) + `NSPrivacyAccessedAPITypeReasons` (array of codes) |

Check:

```bash
find . -name PrivacyInfo.xcprivacy -not -path "*/node_modules/*"
plutil -lint path/to/PrivacyInfo.xcprivacy
# Xcode: Product > Archive > Generate Privacy Report (aggregates app + SDK manifests)
```

Xcode will not build the report correctly if you define your own data type or purpose values. The app-level `NSPrivacyCollectedDataTypes` array may be empty (Expo generates it empty) and the build still validates; the App Store Connect "App Privacy" answers (G-A8) are what Apple publishes. Report a mismatch between manifest and label as 🟡, since the manifest feeds Xcode's privacy report and any SDK-contributed types should appear in the label.

**Collected data type identifiers (35)** — **V**: `NSPrivacyCollectedDataTypeName`, `…EmailAddress`, `…PhoneNumber`, `…PhysicalAddress`, `…OtherUserContactInfo`, `…Health`, `…Fitness`, `…PaymentInfo`, `…CreditInfo`, `…OtherFinancialInfo`, `…PreciseLocation`, `…CoarseLocation`, `…SensitiveInfo`, `…Contacts`, `…EmailsOrTextMessages`, `…PhotosorVideos` (lowercase "or"), `…AudioData`, `…GameplayContent`, `…CustomerSupport`, `…OtherUserContent`, `…BrowsingHistory`, `…SearchHistory`, `…UserID`, `…DeviceID`, `…PurchaseHistory`, `…ProductInteraction`, `…AdvertisingData`, `…OtherUsageData`, `…CrashData`, `…PerformanceData`, `…OtherDiagnosticData`, `…EnvironmentScanning`, `…Hands`, `…Head`, `…OtherDataTypes` (all prefixed `NSPrivacyCollectedDataType`).

**Purpose identifiers (6)** — **V**: `NSPrivacyCollectedDataTypePurposeThirdPartyAdvertising`, `…DeveloperAdvertising`, `…Analytics`, `…ProductPersonalization`, `…AppFunctionality`, `…Other`.

## G-A3 Required-reason APIs — **V**

Since **2024-05-01**, App Store Connect does not accept apps using required-reason APIs without declared reasons, **including usage from third-party SDKs**. Missing/invalid declarations surface as ITMS-9105x emails (T: ITMS-91053 missing API declaration, ITMS-91054 invalid category, ITMS-91055/91056 invalid manifest, ITMS-91061 missing SDK manifest).

| Category identifier | APIs covered (examples) |
|---|---|
| `NSPrivacyAccessedAPICategoryFileTimestamp` | `NSFileAttributeKey` creation/modification dates, `UIDocument.fileModificationDate`, `URLResourceKey` content-modification/creation dates, `getattrlist`/`getattrlistbulk`/`fgetattrlist`/`getattrlistat`, `stat`/`fstat`/`fstatat`/`lstat` |
| `NSPrivacyAccessedAPICategorySystemBootTime` | `ProcessInfo.systemUptime`, `mach_absolute_time()` |
| `NSPrivacyAccessedAPICategoryDiskSpace` | `URLResourceKey` `volumeAvailableCapacity*Key` / `volumeTotalCapacityKey`, `FileAttributeKey.systemFreeSize`/`systemSize`, `statfs`/`statvfs`/`fstatfs`/`fstatvfs`, `getattrlist` family |
| `NSPrivacyAccessedAPICategoryActiveKeyboards` | `UITextInputMode.activeInputModes` |
| `NSPrivacyAccessedAPICategoryUserDefaults` | Foundation `UserDefaults` |

Reason codes (18):

| Category | Code | Use it to… | Key restriction |
|---|---|---|---|
| FileTimestamp | **DDA9.1** | display file timestamps to the user | no off-device sending of derived info |
| FileTimestamp | **C617.1** | access timestamps/size/metadata of files inside the app container, app group container or CloudKit container | — |
| FileTimestamp | **3B52.1** | access metadata of files the user granted access to (document picker) | — |
| FileTimestamp | **0A2A.1** | SDK wrapper around file-timestamp APIs; **SDKs only**; not if the SDK exists primarily to wrap required-reason APIs | not for the SDK's own purposes, not sent off-device |
| SystemBootTime | **35F9.1** | measure time elapsed between in-app events / timers | boot-time derived data not sent off-device (elapsed-time exception) |
| SystemBootTime | **8FFB.1** | calculate absolute timestamps for in-app events | absolute event timestamps may be sent; boot time itself not |
| SystemBootTime | **3D61.1** | include boot time in an optional user-submitted bug report, prominently displayed | — |
| DiskSpace | **85F4.1** | display disk space to the user | local-network same-user exception only |
| DiskSpace | **E174.1** | check space before writing/deleting files; behaviour observable to users | not sent off-device (exception: skip downloads when space is low) |
| DiskSpace | **7D9E.1** | include disk space in an optional user-submitted bug report, prominently displayed | — |
| DiskSpace | **B728.1** | health research app detecting low disk space affecting data collection | must follow 5.1.3 and offer only research functionality |
| ActiveKeyboards | **3EC4.1** | custom keyboard app determining active keyboards | systemwide keyboard must be primary functionality |
| ActiveKeyboards | **54BD.1** | present the correct customised UI based on active keyboards; observable behaviour; app has text fields | — |
| UserDefaults | **CA92.1** | read/write info accessible only to the app itself | no data written by other apps/system, none accessible to other apps |
| UserDefaults | **1C8F.1** | read/write info shared within the same App Group (app, extensions, App Clips) | nothing from outside the group |
| UserDefaults | **C56D.1** | SDK wrapper around UserDefaults; **SDKs only** | not for the SDK's own purposes |
| UserDefaults | **AC6B.1** | read `com.apple.configuration.managed` or set `com.apple.feedback.managed` (MDM) | — |

**SDK-only codes** (`0A2A.1`, `C56D.1`) appear in aggregated app manifests generated by Expo; Apple normally accepts them. Report as 🟡, not 🔴, and remove only if an ITMS-9105x email names them.

Check: grep for the API symbols in first-party code and native dependencies, then confirm each used category has a matching manifest entry with a **valid** reason. Typical React Native / Expo apps use `UserDefaults` (CA92.1), file timestamps (C617.1) and boot time (35F9.1) via native modules.

## G-A4 Third-party SDK manifests and signatures — **V**

Source: Apple *Third-party SDK requirements*. A privacy manifest is required for any listed SDK when submitting a new app that includes it or an update that adds it; **signatures** are required where the listed SDK is a binary dependency. Covers any version and any SDK that repackages a listed one. Xcode validates that a new SDK version is signed by the same developer.

Listed SDKs (86): Abseil, AFNetworking, Alamofire, AppAuth, BoringSSL/openssl_grpc, **Capacitor**, Charts, connectivity_plus, **Cordova**, device_info_plus, DKImagePickerController, DKPhotoGallery, FBAEMKit, FBLPromises, FBSDKCoreKit, FBSDKCoreKit_Basics, FBSDKLoginKit, FBSDKShareKit, file_picker, FirebaseABTesting, FirebaseAuth, FirebaseCore, FirebaseCoreDiagnostics, FirebaseCoreExtension, FirebaseCoreInternal, FirebaseCrashlytics, FirebaseDynamicLinks, FirebaseFirestore, FirebaseInstallations, FirebaseMessaging, FirebaseRemoteConfig, **Flutter**, flutter_inappwebview, flutter_local_notifications, fluttertoast, FMDB, geolocator_apple, GoogleDataTransport, GoogleSignIn, GoogleToolboxForMac, GoogleUtilities, grpcpp, GTMAppAuth, GTMSessionFetcher, **hermes**, image_picker_ios, IQKeyboardManager, IQKeyboardManagerSwift, Kingfisher, leveldb, Lottie, MBProgressHUD, nanopb, **OneSignal** (+Core/Extension/Outcomes), OpenSSL, OrderedSet, package_info, package_info_plus, path_provider, path_provider_ios, Promises, Protobuf, Reachability, RealmSwift, RxCocoa, RxRelay, RxSwift, SDWebImage, share_plus, shared_preferences_ios, SnapKit, sqflite, Starscream, SVProgressHUD, SwiftyGif, SwiftyJSON, Toast, UnityFramework, url_launcher, url_launcher_ios, video_player_avfoundation, wakelock, webview_flutter_wkwebview.

Check: compare `Podfile.lock` / `Package.resolved` / `pubspec.lock` / `package.json` native modules with the list. For each hit, verify `PrivacyInfo.xcprivacy` is inside the SDK bundle and the framework is signed. Static CocoaPods caveat (Expo docs): Apple may not parse all `PrivacyInfo` files from static pods; add reasons yourself in app config (`expo.ios.privacyManifests`) when needed.

## G-A5 Purpose strings (Info.plist) — **T** (stable)

Every protected API used (by app code **or any SDK**) needs a specific, user-readable purpose string; missing strings crash at runtime and fail upload validation (ITMS-90683).

| Key | Triggered by |
|---|---|
| `NSCameraUsageDescription` | camera |
| `NSMicrophoneUsageDescription` | microphone, video with audio |
| `NSPhotoLibraryUsageDescription` / `NSPhotoLibraryAddUsageDescription` | photo library read / write |
| `NSLocationWhenInUseUsageDescription` / `NSLocationAlwaysAndWhenInUseUsageDescription` | location |
| `NSContactsUsageDescription` | contacts |
| `NSCalendarsFullAccessUsageDescription` (and legacy variants) | calendar |
| `NSFaceIDUsageDescription` | Face ID |
| `NSBluetoothAlwaysUsageDescription` | Core Bluetooth |
| `NSMotionUsageDescription` | Core Motion |
| `NSSpeechRecognitionUsageDescription` | speech recognition |
| `NSHealthShareUsageDescription` / `NSHealthUpdateUsageDescription` | HealthKit |
| `NSUserTrackingUsageDescription` | ATT (G-A6) |
| `NSLocalNetworkUsageDescription` | local network discovery |

Strings must be specific (5.1.1(ii)): "We use the camera to scan receipts", not "Camera is needed". Strings for permissions the app does not request are a smell (SDK-injected permission): either strip the capability or explain it.

## G-A6 App Tracking Transparency — **V**

Source: Apple *User privacy and data use*.

- ATT is required (iOS/iPadOS/tvOS 14.5+) to **track** the user or access the advertising identifier.
- **Tracking** = linking app data with other companies' app/website/offline data for targeted advertising or ad measurement, or sharing data with data brokers.
- **Not tracking**: linking only on-device and never sent off-device in identifying form; data brokers using data solely for fraud/security; consumer reporting agencies for creditworthiness.
- Need `NSUserTrackingUsageDescription` and a call to `ATTrackingManager.requestTrackingAuthorization`. Without permission the IDFA is all zeros. Status values: `authorized`, `denied`, `notDetermined`, `restricted`.
- IDFV may be used for analytics across the developer's own apps without ATT but must not be combined with other data to track across other companies' apps/websites.
- Functionality **may not be gated** on tracking consent (5.1.2(i)). Device fingerprinting is prohibited.
- EU: from iOS/iPadOS 27.2 an alternative prompt with an "Additional Information" text button is optional; it is the only prompt for Germany, France, Italy, Poland, Romania; re-prompt allowed after one year (reported on Apple page, **V\***).
- Expo: `expo-tracking-transparency` + plist key; denial returns zeros for IDFA; on Android always "granted".

Verdicts: tracking SDK active with no ATT prompt → 🔴. ATT prompt but nothing tracks and manifest says `NSPrivacyTracking=false` → 🟡 (unneeded prompt invites questions). `NSPrivacyTrackingDomains` set but domain contacted before permission → functional breakage.

## G-A7 Account deletion — **V**

Source: Apple *Offering account deletion in your app* (maps to 5.1.1(v)).

- Account creation supported → the user must be able to **initiate deletion in-app** of the account **and associated personal data**; temporary deactivation is insufficient.
- Easy to find (typically account settings). If a website is required, link directly to that page. tvOS: static URL or QR code.
- Inform about timing, subscriptions and legally retained data.
- Customer-service-only flows (email/phone) are not allowed outside highly regulated industries (5.1.1(ix)).
- Re-authentication and confirmation steps allowed. Manual deletion acceptable if reasonably quick and the user is told.
- **Sign in with Apple accounts must be revoked via the Sign in with Apple REST API** on deletion. Guest accounts must be deletable. Deletion must cover user-generated content shared with others. Must be available to everyone, not only GDPR/CCPA users.
- Subscribers must be told billing continues through Apple, and offered `showManageSubscriptions`, the subscriptions link, or `beginRefundRequest`. Scheduling deletion at the subscription end is allowed if immediate deletion is also offered.

Check: grep delete-account flow; trace what it deletes (DB rows, storage objects, analytics profile, subscription records, push tokens); verify Apple token revocation call (`appleid.apple.com/auth/revoke`, T endpoint). Backend deep-dive → `privacy-audit` `references/08-rights-retention-deletion.md`.

## G-A8 App Privacy details (nutrition labels) — **V**

Source: Apple *App privacy details*. Console-resident (**K**): the user answers in App Store Connect.

- **Collect** = transmit data off the device so you or third-party partners can access it longer than needed to service the request in real time. Third-party partners include analytics tools, ad networks, SDKs. **You are responsible for their practices.** On-device-only processing is not "collected". Apple-collected data (MapKit, CloudKit, App Analytics) need not be disclosed by you.
- Declare even data used only for app functionality. Data types and purposes are the identifiers in G-A2.
- **Linked to you** unless de-identified before collection (strip direct identifiers or break the link) and never re-linked. **Used to track you** = G-A6 tracking definition.
- Optional disclosure only when **all** four conditions hold (not tracking/not shared with a data broker; not used for third-party ads, own ads/marketing or other purposes; collected only infrequently outside primary functionality and optional; user-provided in the app interface each time). Product Improvement Programs, Regulated Financial Services and Health Research have separate carve-outs.
- A **Privacy Policy URL is required**; Privacy Choices URL optional.

Check: derive the label from the SDK inventory (`privacy-audit` `references/06-sdk-catalog.md`), compare to the console answers the user pastes and to the aggregated manifest (G-A2). Any collected type missing from the label → 🔴 (2.3 accuracy + 5.1.1).

## G-A9 Age rating — **V\*** (tier lists from a summarised page; re-read live)

- Apple moved to a new system: tiers **4+, 9+, 13+, 16+, 18+, Unrated**; ratings were updated automatically and developers were asked to answer the **updated questions by 2026-01-31** (deadline passed).
- Questionnaire areas: In-App Controls (parental controls, age assurance); Capabilities (unrestricted web access, user-generated content, social media, messaging/chat, advertising); Mature themes; Medical or wellness; Sexuality or nudity; Violence; Chance-based activities (gambling, simulated gambling, contests, loot boxes).
- Age category **"Made for Kids"** cannot be changed after approval. Regional values exist (Australia, Korea, Vietnam, Brazil).
- Check: answers match code (UGC, chat, web view, ads, loot boxes) and 2.3.6 honesty rule. Mismatch → 🟠/🔴.

## G-A10 DSA trader status (EU) — **V**

Since **2025-02-17**, **trader status** is required for apps distributed in the EU; apps without it are removed from the EU App Store (since 2024-10-16 it was required to submit updates in the EU). Check (K): trader declaration completed in App Store Connect, with contact details publicly displayed.

## G-A11 Export compliance — **T**

Encryption declarations are required at upload. Set `ITSAppUsesNonExemptEncryption` in Info.plist (`false` when only standard HTTPS/OS-provided encryption is used; `true` with documentation otherwise). Expo: `expo.ios.config.usesNonExemptEncryption`. Missing key → every upload stops on the encryption question. Re-verify rules for custom crypto and France-specific distribution declarations on the live Apple page before 🔴.

## G-A12 Server-side Apple dependencies — **V**

- APNs: update the trust store to the **USERTrust RSA Certification Authority** root (production cert change effective 2025-02-24); APNs sandbox certificate update (2025-01-20).
- Receipt validation: SHA-1 intermediate certificate expired 2025-01-24; support **SHA-256** or use `AppTransaction`/`Transaction` (StoreKit 2).
- Check: server code validating receipts or talking to APNs.

## G-A13 Age-assurance laws (US states) — **T** (unstable; see `09-regulatory-gates.md`)

Texas SB 2420, Utah and Louisiana app-store accountability laws drive Apple's **Declared Age Range API**, **PermissionKit Significant Change API** and StoreKit age-rating property. Dates and injunctions moved repeatedly in 2026. Do not issue 🔴 on this row; surface it as 🟡 with the live-source check.

## Gate summary table (copy into the report)

| Gate | Evidence | Status |
|---|---|---|
| G-A1 Xcode 26+ / SDK 26, deployment target ≥ iOS 13 | B | |
| G-A2 Privacy manifest valid, aggregated | B | |
| G-A3 Required-reason APIs declared (app + SDKs) | C, B | |
| G-A4 Listed SDKs: manifest + signature | C, B | |
| G-A5 Purpose strings complete and specific | C, B | |
| G-A6 ATT consistent with tracking | C | |
| G-A7 In-app account deletion (+ Apple revoke) | C | |
| G-A8 App Privacy answers match SDK inventory | K, C | |
| G-A9 Age rating questionnaire honest | K, C | |
| G-A10 DSA trader status (EU) | K | |
| G-A11 Export compliance key | C, B | |
| G-A12 APNs / receipt validation | C | |
