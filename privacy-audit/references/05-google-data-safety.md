# 05 — Google Play: Data safety, User Data policy, Families

Sources read 2026-11-05 (**V**): Play *Data safety* help (answer 10787469), *User Data* policy (10144311), *Permissions and APIs that Access Sensitive Information* (16558241), *Families* (9893335), *App account deletion* (13327111), *App content* (9859455), *Advertising ID* (6048248). Store-review gates live in `store-review-preflight/references/google-02-technical-gates.md`; this file derives the **answers**.

## 1. Definitions

- **Collection**: transmitting data off the device, including by SDKs. On-device-only processing need not be declared.
- **Sharing**: transfer to a third party. Not sharing: service providers acting only on your behalf, legal requests, user-initiated actions or consented disclosures, fully anonymised data.
- **Ephemeral processing**: data used only in memory for the real-time request and not retained beyond it. It must still be answered but is not shown on the listing; building ad or user profiles can never be ephemeral.
- **Required vs optional**: if any version of the app requires a data type, mark it required.
- Declare pseudonymous data. Declare payment data handled by Google Play Billing only if your app never accesses it.
- Internal-testing-only apps are exempt; all published tracks must complete the form. Apps collecting nothing still complete it and link a privacy policy.

## 2. Data types, purposes, security practices

**Types**: Location (approximate, precise); Personal info (name, email, user IDs, address, phone, race and ethnicity, political or religious beliefs, sexual orientation, other); Financial info (user payment info, purchase history, credit score, other); Health and fitness; Messages (emails, SMS/MMS, other in-app); Photos and videos; Audio files; Files and docs; Calendar; Contacts; App activity (app interactions, in-app search history, installed apps, other user-generated content, other actions); Web browsing; App info and performance (crash logs, diagnostics, other); Device or other IDs (advertising ID, Firebase installation ID, etc.).

**Purposes**: App functionality; Analytics; Developer communications; Advertising or marketing; Fraud prevention, security and compliance; Personalisation; Account management.

**Security practices**: data encrypted in transit (industry-standard, e.g. TLS/HTTPS); users can request deletion (in-app, contact form or dedicated email alias; automatic deletion/anonymisation within 90 days qualifies); optional badges (independent security review MASA/OWASP MASVS, Families commitment, UPI).

## 3. Apple ↔ Google mapping (use one inventory for both)

| Inventory item | Apple label type | Google Data safety type |
|---|---|---|
| Name, email, phone, address | Contact Info | Personal info |
| User ID, account ID | Identifiers → User ID | Personal info → User IDs |
| Device ID, IDFA, AAID, installation ID, push token | Identifiers → Device ID | Device or other IDs |
| Precise / approximate location | Location | Location |
| Photos/videos, audio | User Content | Photos and videos / Audio files |
| Messages, free text, AI prompts | User Content (Emails or Text Messages / Other User Content) | Messages / App activity → Other user-generated content |
| Purchase records | Purchases → Purchase History | Financial info → Purchase history |
| Payment card details (processor-handled) | Financial Info (only if your app accesses it) | Financial info → Payment info (same rule) |
| Screen views, taps, feature use | Usage Data → Product Interaction | App activity → App interactions |
| Search queries | Search History | App activity → In-app search history |
| Crash logs, performance traces | Diagnostics | App info and performance |
| Health/fitness | Health & Fitness | Health and fitness |
| Contacts | Contacts | Contacts |
| Files | User Content / Other | Files and docs |
| Installed apps list | (not allowed to collect for analytics/ads, 5.1.2(iv)) | App activity → Installed apps |

## 4. Deriving answers from the inventory

1. Keep only items that leave the device (collection) — SDK traffic counts.
2. Classify each: **collected only** vs **shared** (does a third party that is not merely your service provider receive it?). Analytics/crash SDKs acting on your behalf as processors are generally service providers (Google's exemption); ad networks, attribution partners and data brokers are sharing. Record the reasoning (🟠 if unclear).
3. Required or optional per type.
4. Ephemeral? Only for real-time requests not retained (e.g. a translation call that is not stored). Profiles cannot be ephemeral.
5. Purposes: all that apply.
6. Security practices and deletion answers must reflect reality (`08` for deletion).
7. Fill `assets/play-data-safety-worksheet.md`; export CSV from Play Console and diff against the worksheet (Play import overwrites existing answers: warn the user).

## 5. User Data policy points to check

| Rule | Check |
|---|---|
| Privacy policy | Public HTML URL (no PDF, no geofence, non-editable), names developer/app, covers SDK data, includes contact, retention, deletion; linked in Play Console and in-app |
| Prominent disclosure and consent | For collection outside user expectation (background location, contacts upload, etc.): in-app disclosure in normal use, then affirmative consent **before** collection; backing out is not consent |
| Data safety consistency | Form matches policy and behaviour including SDKs |
| No sale | Personal and sensitive data may not be sold |
| Account deletion | In-app path plus web link; freezing/deactivation is not deletion; retention disclosed |
| Sensitive permissions | Incremental, core features only; declarations where required; Photo Picker preferred over `READ_MEDIA_*` |
| Persistent identifiers | IMEI/IMSI/SIM Serial not linked to personal data except narrow cases; App Set ID for analytics/fraud only |
| Advertising ID | Ads and analytics only; honour opt-out; `AD_ID` permission (API 33+) |
| EU/UK/Swiss data | Comply with the laws; consent-based purposes |
| SDKs | You are responsible for SDK practices |

## 6. Families

Declared target audience includes children → Families policy: no transmission of AAID, SIM/Build Serial, BSSID, MAC, SSID, IMEI/IMSI from children-only apps (or from children/unknown-age users in mixed apps); no location in children-only apps; only child-approved SDKs and Families Self-Certified Ads SDKs; no personalised ads; COPPA and GDPR compliance. Full table: `store-review-preflight/references/google-01-policies.md` §3.

## 7. Common mistakes

| Mistake | Fix |
|---|---|
| Form says "no data collected" with analytics/crash/auth/ads SDKs present | Declare per SDK (`06-sdk-catalog.md`) |
| Treating Firebase installation ID as "not personal" | Declare Device or other IDs |
| No web deletion link, or link not naming the app | Public page naming the app/developer with the deletion steps |
| Declaring sharing = none while an ad/attribution SDK receives identifiers | Mark shared; add Advertising or marketing purpose |
| Encryption in transit = yes while cleartext traffic permitted | Disable cleartext or answer accurately |
| Inconsistent with the privacy policy | Policy and form generated from the same inventory |
