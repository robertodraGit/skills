# Apple 03 — Guideline 3: Business

Source: App Review Guidelines, section 3. Confidence **V** (verbatim, read 2026-11-05; *Last Updated: October 16, 2026*). Paraphrased.

**Intro rule**: explain monetization in metadata and review notes; rip-off pricing is rejected; manipulating reviews or rankings can mean expulsion from the Developer Program.

## 3.1 Payments

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 3.1.1 | Unlocking features or functionality (subscriptions, in-game currencies, game levels, premium content, full versions) requires **In-App Purchase**. No license keys, AR markers, QR codes, cryptocurrencies as unlock mechanisms. IAP currency may be used to tip. **Purchased credits may not expire**; restorable IAP needs a **restore mechanism**. Gifts refundable only to the original purchaser. **Loot boxes must disclose item odds before purchase.** Digital gift cards/vouchers redeemable for digital goods: IAP only. **Free trials**: Non-Consumable IAP at Price Tier 0 named "XX-day Trial", with duration, loss of access and downstream charges disclosed before the trial. NFTs: minting/listing/transferring via IAP; NFT ownership may not unlock features | App sells digital goods or unlocks features | List every paid feature and its purchase path. Any path ending in Stripe/PayPal/web checkout for a digital good → 🔴. Check restore purchases, odds disclosure, credit expiry logic, trial copy | C |
| 3.1.1(a) | Link to other purchase methods requires the **StoreKit External Purchase Link Entitlement** (or Music Streaming Services Entitlement), limited to specific storefronts/platforms; the link may mention a lower price elsewhere. Outside the US storefront, no buttons/CTAs to other purchase methods without the entitlement. Misleading marketing, scams, fraud → removal | App links out to web purchase | Find outbound payment links and CTAs. Confirm the entitlement and storefront scope; check the US-storefront carve-out as stated in 3.1.1/3.1.3(a) (T: US exception details are litigation-sensitive, re-read live) | C, K |
| 3.1.2 | Auto-renewable subscriptions allowed in any category | Subscriptions | — | — |
| 3.1.2(a) | Permissible: **ongoing value**; **minimum period 7 days**; available on **all** the user's devices; **no extra tasks** to receive value (social posts, contact uploads, check-ins). May mix with à-la-carte offerings. Existing paid users keep primary functionality when moving to subscriptions. Free trials via App Store Connect offers. Scam/bait-and-switch subscriptions removed. Carrier bundles need prior approval | Subscriptions | Check the subscription duration config, cross-device entitlement sync, no "post to unlock", one-time benefits not sold as subscription | C, K |
| 3.1.2(b) | Upgrades/downgrades must be seamless; users must not subscribe accidentally to multiple variations | Multiple tiers | Check subscription group config | K |
| 3.1.2(c) | Before asking users to subscribe, clearly describe what the user gets for the price (how many issues, how much cloud storage, etc.); meet Schedule 2 of the Apple Developer Program License Agreement | Subscriptions | Check paywall copy: price, period, auto-renewal statement, cancel instructions, links to Terms and Privacy Policy visible on the paywall | C, L |
| 3.1.3 | Other purchase methods allowed for categories (a)–(g) below. In the app, do not encourage other methods, except under 3.1.1(a) / 3.1.3(a) and the US storefront rule. Off-app communication with the user base is allowed | Non-IAP billing | Identify which category (a)–(g) justifies it | C |
| 3.1.3(a) | **Reader apps**: access to previously purchased magazines, newspapers, books, audio, music, video; free-tier signup and account management. External Link Account Entitlement allows an informational link to the developer's own account site | Reader apps | Verify the category fits; entitlement | C, K |
| 3.1.3(b) | **Multiplatform services**: access to content acquired on other platforms or the web, provided the same items are also sold as IAP in the app | Cross-platform content | Verify IAP parity | C |
| 3.1.3(c) | **Enterprise services**: sold directly to organisations for employees/students; consumer, single-user, family sales use IAP | B2B apps | Verify the buyer is an organisation | C |
| 3.1.3(d) | **Person-to-person** one-to-one real-time services (tutoring, medical consultations, real-estate tours, fitness training) may use other payment; one-to-few/one-to-many must use IAP | Marketplace/coaching | Verify real-time 1:1 | C |
| 3.1.3(e) | Goods and services consumed **outside** the app: must use Apple Pay or card entry | Physical goods/services | Verify nothing digital is sold | C |
| 3.1.3(f) | Free stand-alone companion apps to paid web-based VoIP, cloud storage, email, web hosting: no IAP if no in-app purchasing and no CTAs | Companion apps | Verify absence of CTAs | C, L |
| 3.1.3(g) | Ad-management apps for campaign buying that don't display the ads. Ads shown in the same app (e.g. post "boosts") must use IAP | Ad tools | — | C |
| 3.1.4 | Hardware-specific content may unlock without IAP; optional features tied to a physical product need an IAP alternative; no forced unrelated purchases or ads/marketing to unlock features | Hardware companion apps | Verify | C |
| 3.1.5 | Cryptocurrencies: (i) wallets only from organisation developers; (ii) mining only off-device; (iii) exchanges only where licensed; (iv) ICOs/crypto futures/crypto-securities trading only from established banks, securities firms, FCMs or approved institutions; (v) no currency for completing tasks such as installing apps or posting | Crypto features | Check entity type, licences, mining location | C, K |

## 3.2 Other business model issues (lists are non-exhaustive)

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 3.2.1 | Acceptable: (i) promoting your own apps (not a pure catalog); (ii) recommending third-party app collections with robust editorial content; (iii) disabling approved **rental** content after the period (nothing else may expire); (iv) Wallet passes only for payments, offers, ID; (v) insurance apps free, legally compliant, no IAP; (vi) approved nonprofits may fundraise with Apple Pay, disclose fund use, provide tax receipts, platforms vet nonprofits; (vii) optional individual-to-individual gifts without IAP if 100% goes to the recipient; (viii) financial trading/investing/money-management apps must come from the licensed institution | Corresponding business models | Match the model to the clause | C, L |
| 3.2.2 | Unacceptable: (i) store-like interface for third-party apps/extensions/plug-ins; (iii) artificially inflating ad impressions/clicks or apps mainly showing ads; (iv) collecting charity funds in-app unless approved nonprofit (3.2.1(vi)); (v) arbitrarily restricting users by location or carrier; (vii) manipulating visibility/status/rank on other services unless their terms allow; (viii) binary options banned; CFD/FOREX apps licensed in every jurisdiction served; (ix) personal loans disclose all terms including max APR and payment due date; **max APR 36% including costs and fees**; no full repayment required within 60 days or less; (x) **no forcing ratings, reviews, downloads or other store actions to access functionality** (incentives for in-app actions allowed) | Corresponding models | Search copy for "rate us to unlock", "review to continue" | C, L |

## Paywall checklist (cheap to verify, frequent rejection)

- Price, billing period and auto-renewal stated next to the purchase button.
- Free trial: length, price after trial, what happens at the end.
- Links to Terms of Use (EULA) and Privacy Policy on the paywall and in the listing.
- Restore Purchases reachable without purchasing.
- Cancellation instruction or link to Manage Subscriptions.
- No dark patterns: the close button is visible, no misleading default selection.

## Rule-of-thumb verdicts

- Digital good sold via Stripe/web checkout inside the app, with no entitlement → 🔴 (3.1.1).
- Missing Restore Purchases → 🔴 (3.1.1).
- Loot box without odds → 🔴 (3.1.1).
- Subscription whose value is one-off → 🟠/🔴 (3.1.2(a)).
- Gate reading "rate the app to continue" → 🔴 (3.2.2(x)).
