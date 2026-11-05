# Apple App Privacy worksheet

Derive from the inventory (`04-apple-privacy.md` §3). One row per **data type** the app or any SDK collects (transmits off-device so you or partners can access it beyond real-time servicing). If a row is all "No", delete it. Compare with the answers in App Store Connect and with `PrivacyInfo.xcprivacy`.

Legend: **Linked** = tied to identity (default yes unless de-identified before collection). **Tracking** = linked with third-party data for targeted ads/measurement, or shared with a data broker. Purposes: 3PA = Third-Party Advertising, DA = Developer's Advertising or Marketing, AN = Analytics, PP = Product Personalization, AF = App Functionality, OT = Other.

| Category | Data type | Collected? | Linked? | Tracking? | Purposes | Source (feature / SDK) | Optional disclosure? (all 4 criteria) | Manifest identifier |
|---|---|---|---|---|---|---|---|---|
| Contact Info | Name | | | | | | | `NSPrivacyCollectedDataTypeName` |
| Contact Info | Email Address | | | | | | | `…EmailAddress` |
| Contact Info | Phone Number | | | | | | | `…PhoneNumber` |
| Contact Info | Physical Address | | | | | | | `…PhysicalAddress` |
| Contact Info | Other User Contact Info | | | | | | | `…OtherUserContactInfo` |
| Health & Fitness | Health | | | | | | | `…Health` |
| Health & Fitness | Fitness | | | | | | | `…Fitness` |
| Financial Info | Payment Info | | | | | | | `…PaymentInfo` |
| Financial Info | Credit Info | | | | | | | `…CreditInfo` |
| Financial Info | Other Financial Info | | | | | | | `…OtherFinancialInfo` |
| Location | Precise Location | | | | | | | `…PreciseLocation` |
| Location | Coarse Location | | | | | | | `…CoarseLocation` |
| Sensitive Info | Sensitive Info | | | | | | | `…SensitiveInfo` |
| Contacts | Contacts | | | | | | | `…Contacts` |
| User Content | Emails or Text Messages | | | | | | | `…EmailsOrTextMessages` |
| User Content | Photos or Videos | | | | | | | `…PhotosorVideos` |
| User Content | Audio Data | | | | | | | `…AudioData` |
| User Content | Gameplay Content | | | | | | | `…GameplayContent` |
| User Content | Customer Support | | | | | | | `…CustomerSupport` |
| User Content | Other User Content | | | | | | | `…OtherUserContent` |
| Browsing History | Browsing History | | | | | | | `…BrowsingHistory` |
| Search History | Search History | | | | | | | `…SearchHistory` |
| Identifiers | User ID | | | | | | | `…UserID` |
| Identifiers | Device ID | | | | | | | `…DeviceID` |
| Purchases | Purchase History | | | | | | | `…PurchaseHistory` |
| Usage Data | Product Interaction | | | | | | | `…ProductInteraction` |
| Usage Data | Advertising Data | | | | | | | `…AdvertisingData` |
| Usage Data | Other Usage Data | | | | | | | `…OtherUsageData` |
| Diagnostics | Crash Data | | | | | | | `…CrashData` |
| Diagnostics | Performance Data | | | | | | | `…PerformanceData` |
| Diagnostics | Other Diagnostic Data | | | | | | | `…OtherDiagnosticData` |
| Surroundings | Environment Scanning | | | | | | | `…EnvironmentScanning` |
| Body | Hands | | | | | | | `…Hands` |
| Body | Head | | | | | | | `…Head` |
| Other Data | Other Data Types | | | | | | | `…OtherDataTypes` |

(All manifest identifiers share the prefix `NSPrivacyCollectedDataType`; purposes use `NSPrivacyCollectedDataTypePurpose{ThirdPartyAdvertising|DeveloperAdvertising|Analytics|ProductPersonalization|AppFunctionality|Other}`.)

## Summary answers

- **Do you or your third-party partners collect data from this app?** {{Yes | No}}
- **Tracking:** {{Yes: ATT required, `NSPrivacyTracking=true`, domains {{…}} | No}}
- **Privacy Policy URL:** {{…}} (required) · **Privacy Choices URL:** {{optional}}
- **ATT prompt shown?** {{yes/no}}; `NSUserTrackingUsageDescription` {{present/absent}}
- **Third-party AI sharing disclosed and consented (5.1.2(i))?** {{…}}

## Diff against the console

| Data type | Console says | Worksheet says | Action |
|---|---|---|---|
