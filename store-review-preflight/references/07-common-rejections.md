# 07 — Common rejection patterns and fixes

Confidence **T** for the frequency ranking (field experience, not store data). The rule citations are **V** and point to the verified reference files. Use this file as a **second pass** over the report: if a pattern below fits the app and the report shows 🟢, re-check the evidence.

## Apple

| # | Pattern | Rule | Why it happens | Fix | Effort |
|---|---|---|---|---|---|
| A1 | **Reviewer cannot sign in**: no demo account, expired credentials, 2FA or SMS code the reviewer cannot receive, backend asleep | 2.1(a) | Test account lives in staging, or OTP goes to the developer's phone | Fixed demo account on **production**, no 2FA for that account (or a fixed OTP via allowlist), credentials in Notes for Review, backend monitored during review | S |
| A2 | **Account creation without in-app deletion** | 5.1.1(v) | Deletion handled by email to support | In-app "Delete account" that removes account + personal data; Apple token revocation; confirm dialog; subscription notice | M |
| A3 | **Social login without Sign in with Apple** | 4.8 | Google/Facebook login added late | Add Sign in with Apple (name+email only, private relay supported), or restrict to exemptions | M |
| A4 | **Paywall missing terms**: price, period, renewal, links to Terms/Privacy, no Restore | 3.1.2(c), 3.1.1, 2.3.2 | Paywall built by designers, not by policy | Paywall checklist in `apple-03-business.md` | S |
| A5 | **Web checkout for digital goods** | 3.1.1 | Stripe reused from the web app | IAP (RevenueCat/StoreKit), or external-purchase entitlement where available; remove CTAs | L |
| A6 | **Missing/vague purpose strings** or permission requested at launch with no context | 5.1.1(ii), 5.1.1(iv) | SDK pulled in a permission | Specific strings; ask in context; test deny paths | S |
| A7 | **App Privacy answers don't match behaviour** (analytics/crash SDK not declared) | 5.1.1(i), 2.3 | Label filled once, SDKs added later | Rebuild the label from the SDK inventory every release | S |
| A8 | **ATT mismatch**: tracking SDK with no prompt, or prompt with nothing tracking | 5.1.2(i) | SDK defaults | Audit SDKs; remove tracking or add ATT; align manifest | M |
| A9 | **Minimum functionality**: Capacitor/WebView shell around a site | 4.2 | Fast port of a web app | Add native value (push, offline, device APIs) and explain in notes; or ship as a PWA | L |
| A10 | **Hidden/undocumented features** or remote-config switches | 2.5.19, 2.3.1(a) | Staged rollouts, region flags | Document every flagged feature in the review notes; remove reviewer-only paths | S |
| A11 | **Metadata mismatch**: screenshots show features that do not exist, placeholder copy, competitor names in keywords | 2.3.x | Marketing ahead of product | Align listing to the build; scrub keywords; ≤ 30-char name | S |
| A12 | **UGC without report/block/filter** (incl. AI chat/image) | 1.2 | MVP social feature | Four mechanisms: filter, report, block, contact | M |
| A13 | **Third-party AI receiving personal data without consent** | 5.1.2(i) | LLM call from the client | Disclosure + explicit consent before first send; note in privacy policy and label | M |
| A14 | **Crash on launch** on the reviewer's device/OS/iPad | 2.1(a) | Not tested on iPad or latest OS | Test the release build on iPad and the newest OS | M |
| A15 | **Unused background modes** | 2.5.4 | Template left `audio`/`location`/`fetch` in `UIBackgroundModes` | Remove unused modes; justify the used ones in notes | S |
| A16 | **Invalid/missing privacy manifest** (ITMS-9105x) | G-A2/A3/A4 | SDK upgrade | Add manifests/reasons; regenerate the privacy report | S |
| A17 | **Spam / clone** | 4.3(b) | Crowded category | Describe the differentiator; cut duplicate apps | M |
| A18 | **Custom rating prompt** or "rate to unlock" | 5.6.1, 3.2.2(x) | Growth tactics | Use the system review prompt only | S |
| A19 | **Kids Category with third-party analytics/ads** | 1.3, 5.1.4 | Standard SDK stack | Strip SDKs; parental gate on links/IAP | M |
| A20 | **Marketing push without opt-in / push required to use the app** | 4.5.4, 5.1.2(i) | Default enablement | Opt-in screen; app works with push off | S |
| A21 | **Support URL dead or without contact** | 1.5 | Placeholder site | Live page with contact method | S |
| A22 | **Pre-release naming**: "Beta", "Test", "Demo" in the name or UI | 2.2 | Staging name shipped | Rename; use TestFlight for betas | S |

## Google Play

| # | Pattern | Rule | Fix | Effort |
|---|---|---|---|---|
| P1 | **Data safety ≠ behaviour** (SDK data not declared) | User Data / G-G3 | Rebuild from SDK inventory; align privacy policy | S |
| P2 | **No account-deletion web link** or link not naming the app | G-G4 | Public page with the deletion path, app name, steps | S |
| P3 | **Privacy policy unreachable/PDF/geofenced or missing in-app link** | User Data | HTML, public, named entity, in-app link | S |
| P4 | **Sensitive permission without declaration or Photo Picker alternative** | Permissions | Use system picker, drop permission, or complete the declaration | S–M |
| P5 | **Background location without prominent disclosure + consent** | User Data | Pre-permission disclosure screen; justify core feature | M |
| P6 | **Target API too low** | G-G1 | Raise `targetSdk`, run behaviour-change testing | M–L |
| P7 | **New personal account: no 12×14 closed test** | G-G5 | Start the test early; recruit and keep testers | M (calendar-bound) |
| P8 | **Generative AI app without in-app report** | AI-Generated Content | Add flag/report on outputs; moderation | M |
| P9 | **Families app using non-certified ad SDK or AAID** | Families | Switch to certified SDKs; strip identifiers | M |
| P10 | **AD_ID inconsistent**: declared with no ads, or ads with no declaration | G-G7 | Align manifest and Data safety | S |
| P11 | **Misleading subscription disclosure** | Subscriptions | Show price, period, renewal, cancel path | S |
| P12 | **16 KB alignment missing** (post-2027-02-01) | G-G2 | Update NDK/AGP/SDKs | M |
| P13 | **App access instructions missing** for login-gated apps | G-G6 | Provide credentials in App content → App access | S |

## Using this file

1. For each row that matches the app's capability table, find the corresponding finding in the report.
2. If the report is 🟢 for the matching rule, re-open the evidence and confirm.
3. Add rows the report missed as findings with the same format.
