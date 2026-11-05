# 00 — Method

Read first, every run.

## 1. Verdict scale

| Mark | Meaning | Use when |
|---|---|---|
| 🔴 | **Will fail** | A gate is red, or a rule is clearly violated and the evidence is in hand |
| 🟠 | **Likely rejection / needs a human decision** | Rule triggered, one condition uncertain, or a judgement call a reviewer can read either way |
| 🟡 | **Risk** | Compliant today, but one release, SDK bump or metadata edit from a violation; or reliant on an exception that needs documentation |
| 🟢 | **Pass** | Requirement verified with evidence |
| ⚪ | **Not applicable** | Capability absent; state the reason |
| ❓ | **Unverified** | Evidence lives outside the repo (console, build artifact, listing) or the row is tagged `T` and the live source was not re-read |

Every non-🟢/⚪ finding carries: evidence, rule ID, fix, effort (S ≤ 1 h, M ≤ 1 day, L > 1 day).

## 2. Evidence classes

| Class | Source | How to collect |
|---|---|---|
| **C** code | Repository | Read files, search signals (`01-signals.md`) |
| **B** build | `.ipa`, `.aab`, `.apk`, Xcode archive | Commands in the gate tables; if no artifact exists, hand the user the command |
| **K** console | App Store Connect, Play Console | Ask the user to confirm or paste a screenshot/export; mark ❓ until then |
| **L** listing | Store page text, screenshots, preview video | Read from files in the repo (fastlane metadata, `store/` folders) or ask the user |

A row's **Ev** column says which classes can settle it.

## 3. Confidence tags

- **V** — Read from the live official page on **2026-11-05**. Apple App Review Guidelines page footer: *Last Updated: October 16, 2026*. Google Play policy hub banner: *October 29, 2026: We're updating our policies*.
- **V\*** — Read from a page whose text was partly summarised by the fetch tool. Treat as V for triage, re-read before 🔴.
- **T** — Training knowledge, not re-read. Stable facts (Info.plist key names) are low risk; policy wording and dates are high risk. **Re-open the live source before issuing 🔴 on a T row.**

## 4. Freshness protocol

Run this when the user's date is more than 90 days after 2026-11-05, or when the user mentions a recent policy change:

1. Re-open the live sources below.
2. Compare the "last updated" marker with section 3.
3. If changed, scan for rules touching the capabilities found in Step 2 and note differences in the report under "Source drift". Do not silently trust the rows.

| Source | URL |
|---|---|
| Apple App Review Guidelines | https://developer.apple.com/app-store/review/guidelines/ |
| Apple upcoming requirements | https://developer.apple.com/news/upcoming-requirements/ |
| Apple privacy manifest (DocC JSON works when HTML is JS-rendered) | https://developer.apple.com/tutorials/data/documentation/bundleresources/privacy-manifest-files.json |
| Apple third-party SDK requirements | https://developer.apple.com/support/third-party-SDK-requirements/ |
| Apple App Privacy details | https://developer.apple.com/app-store/app-privacy-details/ |
| Apple account deletion | https://developer.apple.com/support/offering-account-deletion-in-your-app/ |
| Google Play Policy Center | https://support.google.com/googleplay/android-developer/topic/9858052 |
| Google Play policy deadlines | https://support.google.com/googleplay/android-developer/table/12921780 |
| Android target API requirement | https://developer.android.com/google/play/requirements/target-sdk |
| Play Data safety | https://support.google.com/googleplay/android-developer/answer/10787469 |

## 5. Triage matrix

Capability found in Step 2 → rules to assess → files to read.

| Capability | Apple rules | Play policy | Read |
|---|---|---|---|
| Account creation / login | 5.1.1(v), 5.1.1(iv), 4.8, 2.1(a) demo access | User Data → Account deletion; App content → sign-in instructions | apple-05, apple-04, apple-02 / google-01, google-02 |
| Third-party / social login | 4.8, 5.1.1(v) | — | apple-04, apple-05 |
| Digital goods, IAP, unlocks | 3.1.1, 3.1.1(a), 3.1.4, 2.1(b), 2.3.2 | Payments (T) | apple-03, apple-02 / google-01 |
| Subscriptions, trials | 3.1.2(a)–(c), 2.3.2, 4.9 | Subscriptions | apple-03 / google-01 |
| External payment links, web checkout | 3.1.1(a), 3.1.3(a)–(g) | Payments (T) | apple-03 |
| Crypto, trading, loans, regulated finance | 3.1.5, 3.2.1(viii), 3.2.2(viii)–(ix), 5.1.1(ix) | Financial Services (T) | apple-03, apple-05 |
| User-generated content, chat, social | 1.2, 1.2.1, 4.7.1 | User Generated Content (T) | apple-01, apple-04 / google-01 |
| Generative AI features | 1.2 (AI content creation), 5.1.2(i) third-party AI | AI-Generated Content | apple-01, apple-05 / google-01 |
| Kids audience | 1.3, 5.1.4, 2.3.8 | Families | apple-01, apple-05, apple-02 / google-01 |
| Health, medical, fitness data | 1.4.1, 1.4.2, 5.1.3, 5.1.2(vi) | Health Content (T), Health Connect, body sensors | apple-01, apple-05 / google-01 |
| Location | 5.1.5, 5.1.1(iii), 5.1.1(iv) | Location permissions | apple-05 / google-01 |
| Camera, microphone, screen recording | 2.5.14, 5.1.1(ii)–(iv) | Sensitive permissions | apple-02, apple-05 / google-01 |
| Photos, contacts, files | 5.1.1(iii), 5.1.2(iv)–(v), 2.5.15 | Photo/video, contacts, all-files | apple-05, apple-02 / google-01 |
| Ads | 2.5.18, 1.3, 5.1.2(i) | Ads, Families ads | apple-02 / google-01 |
| Analytics, attribution, third-party SDKs | 5.1.1(i)–(ii), 5.1.2(i), ATT, privacy manifest | User Data, Data safety | apple-05, apple-06 / google-01, google-02 |
| Cross-app/site tracking, IDFA | 5.1.2(i) ATT, 3.2.2(vii) | Advertising ID | apple-05, apple-06 / google-02 |
| WebView wrapper, Capacitor/Cordova shell | 4.2, 4.2.2, 2.5.6 | Spam/minimum functionality (T) | apple-04, apple-02, 08-stack-notes |
| OTA code updates (Expo Updates, CodePush) | 2.5.2 | Device & Network Abuse (T) | apple-02, 08-stack-notes |
| Push notifications | 4.5.3, 4.5.4 | POST_NOTIFICATIONS (T) | apple-04 |
| Background modes | 2.5.4 | Foreground service declarations (T) | apple-02 / google-02 |
| Loot boxes, gambling, contests | 3.1.1, 5.3.x, 1.1.x | Real-money gambling (T) | apple-03, apple-05 |
| Mini apps, plug-ins, chatbots inside the app | 4.7–4.7.5 | — | apple-04 |
| Widgets, extensions, App Clips, keyboards | 2.5.16, 4.4–4.4.2, 4.5 | — | apple-02, apple-04 |
| Store listing text, name, screenshots | 2.3.x, 4.1, 5.2.x | Metadata, Impersonation (T) | apple-02, apple-04, apple-05 / google-01 |
| Template/white-label/many near-identical apps | 4.2.6, 4.3(a)–(b) | Spam (T) | apple-04 |

## 6. Scope and limits

- This is an engineering-level screening, not legal advice and not a guarantee of approval.
- Reviewers can reject for reasons outside the written rules; the report says so.
- Store policies change. The `V` rows reflect 2026-11-05; the protocol in section 4 is the remedy.
- Out of scope: Mac App Store (rule 2.4.5), tvOS/visionOS/watchOS specifics, alternative marketplaces and notarization, Play enterprise/private apps. Flag, do not analyse.

## 7. Handoffs

- Personal-data flows, consent design, privacy policy drafting, label/Data-safety answers → `privacy-audit` (if installed). In its absence, check only that disclosures exist and are consistent with the code.
- Generative-AI transparency and prohibited-practice duties for EU users → `ai-act-audit` (if installed).
