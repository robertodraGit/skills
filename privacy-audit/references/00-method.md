# 00 — Method

Read first, every run.

## 1. Verdict scale

| Mark | Meaning | Use when |
|---|---|---|
| 🔴 | **Likely violation / will fail** | A mandatory element is missing or contradicted by evidence in hand (e.g. SDK sets identifiers before consent; label omits an SDK's data; no deletion path) |
| 🟠 | **Decision or legal review needed** | Rule triggered, one condition is judgement (lawful basis, necessity, legitimate interest, DPIA need) |
| 🟡 | **Improve** | Compliant on the evidence, fragile or below best practice |
| 🟢 | **No issue identified** | Requirement verified with evidence |
| ⚪ | **Not applicable** | Activity or regime absent; reason stated |
| ❓ | **Unverified** | Evidence outside the repo (console, contract, vendor dashboard) or a `T` row not re-read |

Every non-🟢/⚪ finding: evidence, citation, fix, effort (S ≤ 1 h, M ≤ 1 day, L > 1 day), and the **party** who must act (controller, processor/developer, vendor).

## 2. Evidence classes

| Class | Source | Handling |
|---|---|---|
| **C** code/config | Repo | Search, read; cite path:line |
| **B** build | Merged manifest, IPA, AAB, network capture | Commands in `01-detection-signals.md` §5 |
| **K** console/vendor | App Store Connect, Play Console, vendor dashboards, DPAs | Ask the user; ❓ until confirmed |
| **D** documents | Privacy policy, ToS, RoPA, DPA | Read as provided |
| **N** network | Observed traffic of a running build | Only if the user runs it and shares the result |

## 3. Confidence tags

- **V** — Read from a live official page on **2026-11-05** (Apple/Google/vendor docs, Council/Commission or court-tracker via search).
- **V\*** — Read from a page partly summarised by the fetch tool, or from secondary reporting; confirm on the official source before 🔴.
- **T-s** — Statutory text (GDPR articles, ePrivacy 5(3), COPPA) from training knowledge. Stable; cite article numbers.
- **T** — Regulator guidance, case-law application, vendor behaviour, thresholds and dates from training knowledge. **Re-verify before 🔴.**

## 4. Freshness protocol

Run when the user's date is more than 90 days after 2026-11-05 or when a legal development is mentioned. Re-open the sources, compare, and list differences under "Source drift".

| Topic | Source |
|---|---|
| Apple App Privacy / manifest / ATT | https://developer.apple.com/app-store/app-privacy-details/ · https://developer.apple.com/tutorials/data/documentation/bundleresources/privacy-manifest-files.json |
| Apple guideline 5.1 | https://developer.apple.com/app-store/review/guidelines/#data-collection-and-storage |
| Play Data safety / User Data | https://support.google.com/googleplay/android-developer/answer/10787469 · https://support.google.com/googleplay/android-developer/answer/10144311 |
| EU–US DPF litigation | CJEU case register C-703/25 P |
| Digital Omnibus (GDPR/ePrivacy part) | Council press releases; Parliament Legislative Observatory 2025/0360(COD) |
| EDPB guidelines | https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en |
| Garante (Italy) | https://www.garanteprivacy.it |
| Vendor docs | URLs in `06-sdk-catalog.md` |

## 5. Legal-status snapshot (2026-11-05)

| Item | Status | Conf |
|---|---|---|
| **GDPR** (Reg. 2016/679) and **ePrivacy Directive** 2002/58/EC art. 5(3) | In force; national implementation applies (Italy: D.Lgs. 196/2003 as amended by D.Lgs. 101/2018) | T-s |
| **EU–US Data Privacy Framework** | Adequacy decision of 2023-07-10 in force. General Court dismissed *Latombe* (T-553/23) on 2025-09-03; appeal **C-703/25 P** lodged 2025-10-31 and pending; a 2026-06-28 report notes Microsoft intervened for the Commission. No CJEU ruling found | V\* |
| **Digital Omnibus — data part** (GDPR/ePrivacy/Data Act changes; COM(2025) 837, 2025-11-19) | **Not law.** Council negotiating mandate agreed 2026-10-21 (keeps cookie rules in ePrivacy, reportedly shortens cookie re-prompt wait); Parliament position unconfirmed. Audit against current law only; mention the proposal as a watch item | V\* |
| **Digital Omnibus — AI part** | Adopted as Regulation (EU) 2026/1744, published 2026-07-24 | V\* |
| **US state app-store age laws** (TX SB 2420, UT, LA) | Moving: injunction/stay history in Texas; Apple/Google age-signal APIs exist. See `store-review-preflight` `09-regulatory-gates.md` | V\* |
| **Apple App Review Guidelines 5.1.x** | Last updated 2026-10-16 | V |
| **Google Play policies** | Hub banner 2026-10-29 | V |
| **EAA** (accessibility) | Applies since 2025-06-28; out of scope except noting accessibility of consent UI | V\* |

## 6. Scope and limits

- In scope: personal-data handling by the audited software and its vendors: collection, use, sharing, retention, deletion, consent, transparency, store disclosures, children, sensitive data, AI processing from a privacy angle.
- Out of scope, flagged only: full DPIA, security penetration testing, employment-law monitoring rules beyond a pointer, sector rules (HIPAA, PSD2, MDR), licensing of regulated services, contractual review of DPAs.
- Not legal advice. Recommend qualified legal review for any 🟠 about lawful basis, legitimate-interest balancing, transfers, minors, or special-category data.

## 7. Role map

| Situation | Typical role of the audited party |
|---|---|
| Company's own product, own users | Controller |
| Agency/freelancer building and operating a client's product | Processor (client is controller) for client data; controller for own staff data |
| SaaS vendor processing customer data on customer instructions | Processor |
| Vendor using data for its own purposes (e.g. ad network, some analytics) | Independent or joint controller |

Record the role per processing activity in the inventory. Article 28 obligations apply to processors; Articles 5–22 and 24–25 to controllers.

## 8. Handoffs

- Store readiness (rejections, gates, review notes) → `store-review-preflight`.
- Generative AI duties for EU users → `ai-act-audit`.

Pointers in this skill to `store-review-preflight/references/…` assume that skill is installed. When it is not, use the live sources: Apple required-reason API categories and reason codes at the DocC JSON `https://developer.apple.com/tutorials/data/documentation/bundleresources/app-privacy-configuration/nsprivacyaccessedapitypes/nsprivacyaccessedapitype.json`, Play policy deadlines at the URL in §4, Apple guideline text at the guidelines URL in §4.
