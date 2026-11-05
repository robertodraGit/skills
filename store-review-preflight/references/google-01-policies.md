# Google 01 — Play Developer Program Policy

Source: Google Play Policy Center. Policy hub banner on 2026-11-05: *"October 29, 2026: We're updating our policies."*

**Confidence is per row.** **V** = article read on 2026-11-05. **T** = only the Policy Center landing blurb was read or the row comes from training knowledge: open the live article (Policy Center index https://support.google.com/googleplay/android-developer/topic/9858052) **before issuing 🔴**. Evidence classes as in `00-method.md` §2.

## 1. Privacy, deception and device abuse → User Data (V)

| Rule | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| **Privacy policy** | Link in the Play Console field **and within the app**. Covers what data is accessed, collected, used and shared, **including via SDKs**; names a developer contact; secure handling; retention and deletion policy; labelled as a privacy policy. The listing entity (or the app name) appears in it. **Public, non-geofenced URL, not a PDF, non-editable.** Required even for apps with no sensitive data | Always | Open the URL logged out; confirm it loads worldwide, is HTML, names the developer/app; find the in-app link | C, K |
| **Prominent disclosure and consent** | Required when collection is outside user expectation (e.g. background). Disclosure must appear in normal app use (not buried in a menu or only in the privacy policy), describe the data, explain use/sharing. Consent must follow the disclosure, require **affirmative action**, not treat backing out as consent, not auto-dismiss, and be granted **before collection starts**. Format example: "[This app] collects/transmits/syncs/stores [data] to enable [feature], [in what scenario]" | Background location, contacts/call-log/SMS upload, non-obvious collection | Find the disclosure screen and verify its timing versus first collection | C |
| **Data safety form** | Complete and accurate for every app including **SDK** practices; consistent with the privacy policy; kept updated | Always | See `google-02-technical-gates.md` G-G3 | K |
| **Sale and limits** | Personal and sensitive data may not be **sold**. Use limited to disclosed functionality. Use **runtime permission requests** before gated data | Always | Review data flows; permission request code | C |
| **Account deletion** | Apps that allow account creation must offer deletion **in-app and through an external web resource**; the web link goes in the Play Console URL field. Deletion removes all associated user data (freezing/deactivating does not count). Legally required retention disclosed in the privacy policy. Deletion options also appear in Data safety | Account creation | See G-G4 | C, K |
| **Persistent identifiers** | IMEI, IMSI, SIM Serial may not be linked to personal/sensitive data or resettable IDs, except SIM-tied telephony and enterprise device-owner management | Any device identifier use | Search `getDeviceId`, `getImei`, `getSimSerialNumber`, `ANDROID_ID` use | C |
| **App Set ID** | Analytics and fraud prevention only; not ads personalisation/measurement; not linked to AAID or PII for ads; must be disclosed | App Set ID use | Search `AppSetId` | C |
| **EU/UK/Swiss personal data** | Comply with the laws; use only consented purposes; notify Google immediately if compliance fails | EU audience | Hand off to `privacy-audit` | — |
| **SDK responsibility** | You are responsible for SDKs' data practices; SDK providers may not sell personal and sensitive data from your app | Any SDK | SDK inventory | C |

## 2. Permissions and APIs that access sensitive information (V)

| Permission / API | Requirement | How to check | Ev |
|---|---|---|---|
| **General** | Sensitive permissions needed for **promoted core features**, requested **incrementally with context**, used only for consented purposes. Honour declined restricted permissions without manipulation; offer a reasonable alternative | Test the deny path | C |
| **Photos/videos** (`READ_MEDIA_IMAGES`, `READ_MEDIA_VIDEO`, API 33+) | Only if the system **Photo Picker** is insufficient for core functionality; **Play Console declaration** required | `rg "READ_MEDIA_(IMAGES|VIDEO)"`; prefer the Photo Picker | C, K |
| **All files access** (`MANAGE_EXTERNAL_STORAGE`, API 30+) | Only if platform intents (Storage Access Framework) are insufficient; declaration; users prompted to enable "All files access" in Special app access; no requests for third parties' non-core purposes | `rg MANAGE_EXTERNAL_STORAGE` | C, K |
| **SMS and call log** | The app must be the active default SMS/Phone/Assistant handler to declare/use them; stop using when status lost; core documented functionality only; use SMS Retriever API where possible | `rg "READ_SMS|RECEIVE_SMS|READ_CALL_LOG"` | C, K |
| **Location** | Device location is sensitive. Minimum scope (coarse not fine; foreground not background). **Never request location solely for advertising or analytics.** Background location only for core features with explicit consent. Foreground-service location only as a continuation of a user-initiated action. **Apps for children may not request location.** | `rg "ACCESS_(FINE|COARSE|BACKGROUND)_LOCATION"` | C |
| **Package visibility** (`QUERY_ALL_PACKAGES`) | Only for apps whose core purpose is to launch/search/interoperate with other apps; installed-app inventory never sold/shared for analytics or ads | `rg QUERY_ALL_PACKAGES` | C |
| **Accessibility API** | May not change settings without permission, bypass security controls, record remote call audio, or act autonomously. `isAccessibilityTool=true` only for core disability support. Others: document in listing, in-app disclosure, consent | `rg AccessibilityService` | C |
| **Install packages** (`REQUEST_INSTALL_PACKAGES`) | Only for permitted core function; user-initiated installs; no silent/self-updates; declaration | `rg REQUEST_INSTALL_PACKAGES` | C |
| **Body sensors** | Heart rate, SpO2, skin temperature are sensitive; apps targeting Android 16+ migrate to granular health permissions (`android.permission.health.*`) | `rg BODY_SENSORS` | C |
| **Also on the page (not re-read in full)** | Health Connect, `VpnService`, `USE_EXACT_ALARM`, `USE_FULL_SCREEN_INTENT`, Age Signals API (legal-obligation use only) | open the article | — |

Upcoming (Policy Deadlines table, V): see `google-02-technical-gates.md` §3.

## 3. Families policy and Designed for Families (V)

| Rule | Requirement | How to check |
|---|---|---|
| Target audience | Declare target age groups in Play Console before publishing; choose only groups the app was designed for; child-directed imagery/terminology can change Google's assessment | K: Target audience declaration vs listing and in-app art |
| Content | Appropriate for children; **not merely a webview of a website**; not primarily affiliate traffic without owner permission | C |
| Accurate declarations | Play Console target audience, Data safety and **IARC rating** accurate | K |
| Child data | Disclose child data collection. **Do not transmit** AAID, SIM Serial, Build Serial, BSSID, MAC, SSID, IMEI or IMSI from children-only apps (or from children/unknown-age users in mixed apps); no `TelephonyManager` phone number; **no location for children-only apps**; use Companion Device Manager for Bluetooth | `rg` identifiers; SDK inventory |
| SDKs | Only SDKs approved/self-certified for child-directed services | SDK inventory vs Families Self-Certified Ads SDK list (T: article 9900633, not re-read) |
| AR | Safety warning on launch | C |
| Social features | In-app online-safety reminder, adult gating, adult management controls; anonymous/random chat apps may not target children (**effective 2026-08-26**) | C |
| Legal | COPPA and GDPR compliance | `privacy-audit` |
| Ads in family apps | Only Families Self-Certified Ads SDKs; no personalised/remarketing ads to children or unknown-age users; no disruptive formats (ads not closable in 5 seconds, multiple placements, interstitials at launch); no deceptive/accidental-click designs; clear distinction between virtual currency and real money | C |

## 4. Restricted content (mixed)

| Rule | Requirement | Conf | How to check |
|---|---|---|---|
| **AI-Generated Content** | Apps generating content from user prompts (chatbots where chatting is central; image/video generation from text/image/voice) must follow existing policies, prevent Restricted Content (incl. content facilitating child exploitation) and Deceptive Behavior, and include **in-app user reporting/flagging of offensive content to the developer without leaving the app**; developers should use reports for filtering/moderation | V | Find the in-app report action on generated content; moderation/safety settings on the model |
| **Child Endangerment, Inappropriate Content, Age-Restricted Content & Functionality** | **2026-08-26**: Child Endangerment and Age-Restricted Content expanded to **anonymous and random chat apps** | V (deadline table) | Review chat features |
| **User Generated Content** | Expect: terms requiring users to accept, filtering/moderation, in-app reporting and blocking, removal of abusive content (mirrors Apple 1.2) | T | Apply the four mechanisms from `apple-01-safety.md` 1.2; then verify live |
| **Impersonation** | Apps misleading users by impersonating another person/app/developer are prohibited | V (blurb) | Review name/icon/listing |
| **Health content and services**, **Financial services**, **Real-money gambling**, **Illegal activities**, **Blockchain-based content** | Topic-specific declarations and licences | T | Open the live article if the capability exists |

## 5. Monetization and ads

| Rule | Requirement | Conf | How to check |
|---|---|---|---|
| **Payments** | Digital goods and in-app features sold through **Google Play Billing** (exceptions exist by region/programme) | T | Search non-Play-billing payment paths for digital goods; open the live Payments policy (article 9858738) before 🔴 |
| **Subscriptions** (V) | Must not mislead. Disclose offer terms, cost, billing frequency, auto-renewal, whether a subscription is required to use the app, other material terms, **with no extra clicks**. Ongoing value (one-time benefits use in-app products). Free trials state duration, pricing, auto-conversion, how to cancel. Fully localised. **In-app access to manage/cancel** (e.g. link to the Play Subscription Center). Disclose any flexible refund policy | V | Review the paywall and settings |
| **Ads** (V) | Ads must follow Restricted Content and content-rating rules and suit the app's rating. No ads mimicking system or other-app UI. **Disruptive ads** disallowed (full-screen without dismiss, false close buttons, outside the app, on home/exit). **Better Ads**: no unexpected full-screen interstitials during gameplay/content start; full-screen interstitials must be closable after 15 seconds (rewarded opt-in excepted); no repeated "made for ads" interstitials after user actions; no lockscreen monetisation unless a lockscreen app; no ad fraud. **Location for ads** disclosed in the privacy policy; location permission not requested solely for ads. **AAID**: only for advertising and analytics; check the opt-out on each access; no linking to persistent identifiers for ads; honour opt-out; disclose in privacy policy | V | Review ad placements and AAID code |
| **Upcoming** | **2027-01-27**: subscriptions with ongoing eligibility-based discounts (student plans etc.) must disclose eligibility criteria, verification, and post-eligibility pricing changes | V | Review subscription tiers |

## 6. Store listing, spam, minimum functionality, malware (blurbs only — T)

| Policy | What to verify on the live article |
|---|---|
| **Metadata** (9898842) | Title/icon/description accuracy, no keyword stuffing, no misleading claims, no performance/price claims in the title, no user testimonials, no other-app references |
| **App Promotion**, **User Ratings/Reviews/Installs** (9899004, 9898684) | No incentivised ratings, no install manipulation |
| **Content Ratings** (9898843) | IARC questionnaire accuracy |
| **Spam** (9899034) | No repetitive near-duplicate apps; webview wrappers that offer nothing |
| **Functionality, Content and User Experience** (9898783) | Minimum functionality, apps that crash or are broken |
| **Malware / Mobile Unwanted Software / Device and Network Abuse / Deceptive Behavior** | Code that endangers users/devices; dynamic code loading from outside Play; misrepresentation; elevated privilege abuse |

Default verdict for these rows is ❓ until the article is read.

## Rule-of-thumb verdicts

- Account creation without in-app **and** web deletion path → 🔴.
- Privacy policy URL is a PDF, geofenced, or missing the developer name → 🔴.
- Photo Picker would suffice but `READ_MEDIA_IMAGES` is declared → 🟠 (declaration likely rejected).
- Location requested solely for ads or analytics → 🔴.
- Generative-AI app without in-app report → 🔴.
- Children-only app transmitting AAID or using location → 🔴.
