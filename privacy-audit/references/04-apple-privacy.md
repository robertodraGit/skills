# 04 — Apple: App Privacy labels, manifest, ATT, data rules

Sources read 2026-11-05 (**V**): Apple *App privacy details*, *User privacy and data use*, *Offering account deletion*, privacy-manifest DocC JSON, App Review Guidelines 5.1 (Last Updated 2026-10-16). Store-review mechanics (gates, rejections) live in the `store-review-preflight` skill; this file derives the **answers**.

## 1. Definitions that decide every answer

- **Collect**: transmit data off the device in a way that lets you **or third-party partners** access it longer than needed to service the request in real time. On-device-only processing is not collected. Data kept by Apple's own services (MapKit, CloudKit, App Analytics) need not be disclosed by you.
- **Third-party partners**: analytics tools, ad networks, third-party SDKs and other external vendors whose code you added. **You disclose their practices.**
- **Declare data even if used only for app functionality.**
- **Linked to you**: tied to identity (account, device or other details) unless **de-identified before collection** and never re-linked. Privacy-law "Personal Information/Personal Data" counts as linked.
- **Used to track you**: linking data collected from your app about a user/device with third-party data for targeted advertising or ad measurement, or sharing with a data broker.
- **Not tracking**: linking solely on-device and never sent off-device in identifying form; data brokers using data solely for fraud/security; consumer reporting agencies for creditworthiness.

## 2. Data types and manifest identifiers

Label category / type → manifest identifier (prefix `NSPrivacyCollectedDataType`).

| Category | Types → identifier |
|---|---|
| Contact Info | Name → `Name`; Email Address → `EmailAddress`; Phone Number → `PhoneNumber`; Physical Address → `PhysicalAddress`; Other User Contact Info → `OtherUserContactInfo` |
| Health & Fitness | Health → `Health`; Fitness → `Fitness` |
| Financial Info | Payment Info → `PaymentInfo`; Credit Info → `CreditInfo`; Other Financial Info → `OtherFinancialInfo` |
| Location | Precise → `PreciseLocation`; Coarse → `CoarseLocation` |
| Sensitive Info | `SensitiveInfo` |
| Contacts | `Contacts` |
| User Content | Emails or Text Messages → `EmailsOrTextMessages`; Photos or Videos → `PhotosorVideos`; Audio Data → `AudioData`; Gameplay Content → `GameplayContent`; Customer Support → `CustomerSupport`; Other User Content → `OtherUserContent` |
| Browsing History | `BrowsingHistory` |
| Search History | `SearchHistory` |
| Identifiers | User ID → `UserID`; Device ID → `DeviceID` |
| Purchases | Purchase History → `PurchaseHistory` |
| Usage Data | Product Interaction → `ProductInteraction`; Advertising Data → `AdvertisingData`; Other Usage Data → `OtherUsageData` |
| Diagnostics | Crash Data → `CrashData`; Performance Data → `PerformanceData`; Other Diagnostic Data → `OtherDiagnosticData` |
| Surroundings | Environment Scanning → `EnvironmentScanning` |
| Body | Hands → `Hands`; Head → `Head` |
| Other Data | `OtherDataTypes` |

Purposes (label → manifest): Third-Party Advertising → `…PurposeThirdPartyAdvertising`; Developer's Advertising or Marketing → `…PurposeDeveloperAdvertising`; Analytics → `…PurposeAnalytics`; Product Personalization → `…PurposeProductPersonalization`; App Functionality → `…PurposeAppFunctionality`; Other Purposes → `…PurposeOther`.

Use exactly these identifiers: Xcode's privacy report breaks when you define your own types or purposes.

## 3. Deriving answers from the inventory

For each data item in the inventory:

1. Does it leave the device to you or a partner? No → not collected; stop.
2. Map to a data type (§2). If two apply, declare both.
3. **Linked?** Yes when it is attached to an account, user ID, device ID or other identifier (usual case). No only when truly de-identified before collection.
4. **Tracking?** Yes when used for targeted advertising/ad measurement with third-party data, or shared with a data broker (e.g. attribution SDKs that match with ad-network data, ad SDKs). Then also: ATT prompt, `NSPrivacyTracking=true`, tracking domains listed.
5. **Purposes**: all that apply (a crash SDK = App Functionality + Analytics when also used for product metrics).
6. **Optional disclosure?** Only if all four criteria hold: (1) not tracking and not shared with a data broker; (2) not used for third-party ads, your own ads/marketing, or Other Purposes; (3) collected only in infrequent cases outside primary functionality and optional for the user; (4) user-provided in the app interface, clear to the user, with the user's name/account name prominent in the submission, and the user affirmatively chooses to provide it each time. Data collected on an ongoing basis after one permission request must be disclosed. Separate carve-outs: Product Improvement Programs (7 criteria incl. opt-in), Regulated Financial Services, Health Research (IRB-approved with consent).
7. Write the row into `assets/apple-privacy-worksheet.md`.

Then add SDK-contributed rows from `06-sdk-catalog.md`. Privacy Policy URL is **required**; Privacy Choices URL is optional.

## 4. Manifest (PrivacyInfo.xcprivacy)

- App manifest at `App.app/PrivacyInfo.xcprivacy`; each SDK bundles its own. Xcode aggregates (Product → Archive → Generate Privacy Report). Invalid manifests are rejected by App Store Connect; valid manifests required for listed SDKs since 2025-02-12.
- Keys: `NSPrivacyTracking`, `NSPrivacyTrackingDomains` (requests to these domains **fail** without ATT permission), `NSPrivacyCollectedDataTypes` (type, linked, tracking, purposes), `NSPrivacyAccessedAPITypes` (category + reason codes). Required-reason API categories and codes: `store-review-preflight/references/apple-06-technical-gates.md` G-A3. Template: `assets/privacy-manifest.example.xcprivacy`.
- The label (console) is what Apple publishes; the app-level `NSPrivacyCollectedDataTypes` array can be empty and still validate (Expo generates it empty). Prefer consistency: every type in the manifest must appear in the label (🔴 if not), and label types missing from the manifest are 🟡.

## 5. ATT

Required (iOS/iPadOS/tvOS 14.5+) to track or access IDFA. `NSUserTrackingUsageDescription` + `ATTrackingManager.requestTrackingAuthorization`. Statuses: `authorized`, `denied`, `notDetermined`, `restricted`. IDFA is all zeros without permission. Do not gate functionality on consent; no fingerprinting. Distinguish from GDPR consent (`03` §4).

## 6. Guideline 5.1 rules that touch privacy (summary; full rows in `store-review-preflight/references/apple-05-legal.md`)

- 5.1.1(i) policy in metadata **and** in-app; third parties give equal protection; retention/deletion/revocation explained.
- 5.1.1(ii) consent even for anonymous data; paid features must not depend on access; easy withdrawal; complete purpose strings.
- 5.1.1(iii)–(iv) minimisation, no forced access, alternatives when declined.
- 5.1.1(v) in-app account deletion when accounts can be created; Sign in with Apple tokens revoked.
- 5.1.2(i) permission before sharing personal data with third parties, **including third-party AI**; ATT for tracking.
- 5.1.2(ii)–(iv) no repurposing; no covert profiling/re-identification; no contact databases; no collecting installed-app lists for analytics/ads.
- 5.1.3 health: no ads/data-mining use; disclose specific health data collected.
- 5.1.4 kids: no third-party analytics/ads in Kids Category (1.3); parental gate ≠ consent.
- 2.5.14 explicit consent and visible indication when recording user activity.

## 7. Common mistakes

| Mistake | Fix |
|---|---|
| Label says "Data Not Collected" while an analytics/crash SDK is present | Declare Crash Data, Performance Data, Product Interaction, Device ID as relevant |
| Declared "not linked" for data attached to a user ID | Linked unless de-identified before collection |
| Missing Purchase History for RevenueCat/StoreKit server tracking | RevenueCat collects purchase history (**V**); declare with App Functionality and Analytics |
| ATT shown but `NSPrivacyTracking=false` | Align: tracking true plus domains, or stop tracking |
| Declared tracking but no ATT prompt | Add ATT or remove tracking |
| Third-party AI receives text/photos but label lacks User Content | Declare Emails/Text, Photos/Videos, Other User Content as relevant; get consent (5.1.2(i)) |
| Label not updated after SDK changes | Rebuild from the inventory every release |
