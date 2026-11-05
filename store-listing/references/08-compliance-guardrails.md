# 08 — Compliance guardrails for listing copy

The rules a writer needs while drafting. Full audit of the app against the guidelines is `store-review-preflight`. Confidence: Apple rows **V** (App Review Guidelines, last updated 2026-10-16, read 2026-11-05); Play rows **V** (Metadata policy and preview-asset pages read 2026-11-05).

## 1. Apple — Guideline 2.3 (accurate metadata)

| Rule | Writer's constraint |
|---|---|
| 2.3 | Privacy info, description, screenshots and previews reflect the core experience and stay current |
| 2.3.1(a) | New features and changes described **specifically** in Notes for Review; misleading marketing (features the app lacks, false pricing) is grounds for removal and account termination |
| 2.3.2 | Descriptions, screenshots, previews say which items, levels or subscriptions need additional purchases; promoted IAPs have name, screenshot and description |
| 2.3.3 | Screenshots show the app **in use**, not title art, login or splash; text/image overlays allowed |
| 2.3.4 | Previews: video screen captures of the app only; narration and overlays allowed |
| 2.3.5 | Category chosen by function |
| 2.3.6 | Answer age-rating questions honestly |
| 2.3.7 | Unique name, accurate keywords; **name ≤ 30 characters**; no trademarks, popular app names, prices or irrelevant terms in keywords; no prices/terms/unrelated descriptions in name, subtitle, screenshots, previews; subtitles free of inappropriate content, other apps, unverifiable claims |
| 2.3.8 | Metadata and icons, screenshots, previews suit **4+** even if the app is rated higher; "For Kids"/"For Children" reserved for Kids Category |
| 2.3.9 | You hold rights to all materials; use fictional account info |
| 2.3.10 | No names, icons or imagery of other mobile platforms or alternative marketplaces unless approved interactive functionality |
| 2.3.11 | Pre-orders complete and as advertised |
| 2.3.12 | "What's New" describes new features and product changes; generic text only for bug fixes, security updates, performance improvements |
| 2.3.13 | In-app events: accurate metadata, dates, working deep links |
| 2.3.14 | Creative assets (header/search images) relate to the app, appropriate for all audiences, no references to other apps, no unverifiable claims, no specific or discounted pricing |
| 5.2 | Only content you own or are licensed to use; no unpermitted trademarks |
| 5.2.4 | Do not imply Apple endorses the app; "Editor's Choice" is applied by Apple |
| 1.5 | Support URL must give an easy way to contact the developer |

## 2. Google Play — Metadata policy and asset rules

| Area | Constraint |
|---|---|
| Title | ≤ 30 characters; no emojis, emoticons or repeated special characters; avoid ALL CAPS unless brand; no ranking/price/promo/Google Play program claims; no "Free"/"No Ads" (best practices) |
| Icon, developer name | Same character rules; no misleading symbols (fake notification dots), no store-performance or price badges |
| Short description | No CTA; no "Best", "#1", "Top", "New", "Discount", "Sale", "Million Downloads"; no special characters, line breaks, emojis, repeated punctuation; no time-sensitive copy |
| Full description | No unattributed or anonymous testimonials; no repetitive/unrelated keywords; no celebrity names or brand logos without permission; no sexual imagery, profanity, graphic violence, illicit drug depictions |
| Screenshots/video | Real in-app footage; no fingers tapping the device; clean status bar; minimal taglines (≤ 20%); video public/unlisted, ads off, not age-restricted |
| Impersonation | Do not mislead by imitating another person, app or developer |
| Sensitive categories | Health, financial, gambling, AI-generated content and families have additional declarations (see `store-review-preflight` `google-01-policies.md`) |

## 3. Project-specific rules

Owners often add rules the stores do not: banned words (a housing app that must never read as a dating app), required disclaimers, brand terms. Capture them in Step 1 as `banned_terms` and `required_phrases`, pass banned terms to the linter (`--banned`), and treat violations as 🔴.

## 4. Cross-checks with other artifacts

| Listing statement | Must match |
|---|---|
| "Free", "no ads", "no in-app purchases" | Billing reality: IAP products, `BILLING` permission, ad SDKs |
| "Your data is never shared" | App Privacy label and Data safety form |
| "Adults only" / age | Age rating and in-app gate |
| "Reports read within N hours" | A staffed moderation process the owner confirms |
| "Photos reviewed by a person" | Moderation implementation |
| How matching/ranking works ("compares budget, dates, habits") | The privacy policy and Terms that describe the ranking parameters (an omitted parameter such as age, gender or occupation is a transparency gap) |
| Feature lists | Shipped build and enabled flags |
| Screens in screenshots | Current UI and demo-data policy |

## 5. Verdicts

- Over a limit, banned by policy, or contradicted by the product → 🔴.
- Unverifiable superlative or promise → 🟠.
- Compliant but inconsistent between stores/locales → 🟡.
