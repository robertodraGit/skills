# 00 — Method

Read first, every run.

## 1. Modes

| Mode | Input | Output |
|---|---|---|
| **Create** | Product repo/docs, no listing yet | `listing.md` in the canonical format (`assets/listing-template.md`), screenshot plan, release notes |
| **Audit** | Existing listing (markdown, fastlane `metadata/`, console export, pasted text) | Audit report (`assets/audit-report-template.md`) with a rewritten proposal for every failing field |
| **Single piece** | "write the release notes", "fix the keywords", "plan the screenshots" | Steps 1, the relevant step, and 8 only |

Audit mode keeps the owner's positioning rules and wording unless a rule or limit forces a change. Every changed word in a proposal carries a reason.

## 2. Verdict scale

| Mark | Meaning |
|---|---|
| 🔴 | **Invalid**: over a store limit, banned by store policy, or contradicts a hard project rule; the console rejects it or review will |
| 🟠 | **Weak or risky**: wasted indexed space, unverifiable claim, ambiguous policy reading, mismatch with the product |
| 🟡 | **Improve**: works, measurable upside |
| 🟢 | **Good** |
| ⚪ | **Not applicable** |
| ❓ | **Unverified**: needs console data, live store page, or ASO data the user must supply |

## 3. Evidence rules

1. **Claims ledger.** Every factual claim in the copy (feature, number, price, safety promise, "free", "no ads", response times) maps to evidence: a repo path, a console value the user confirmed, or a document. A claim without evidence is removed or flagged ❓. Apple 2.3 and Google's Metadata policy treat unverifiable claims as grounds for rejection.
2. **No invented ASO data.** Search volumes, popularity scores, difficulty, rankings, conversion rates and download uplifts come from the user's tools (App Store Connect Analytics, Apple Search Ads, Play Console search-terms report, a third-party ASO tool). Without them, label volume **unknown** and rank by relevance and specificity only. Never state predicted uplift.
3. **Competitor listings** are read from public store pages the user names. Do not scrape accounts, ratings or private data.
4. **Native copy.** Each locale is written for that audience, not translated word for word (`06-localization-it-en.md`).
5. **One canonical file.** The listing lives in one `listing.md`; Play's full description may point to Apple's with `same-as`. Delivery notes, asset READMEs and console runbooks link to it instead of copying text (drift is the usual cause of stale claims).
6. **Read-only.** Never upload, submit or edit the console; deliver files and paste-ready text.

## 4. Confidence tags

- **V** — read from the live official page on **2026-11-05**.
- **V\*** — read from a page partly summarised by the fetch tool, or a secondary description; re-read the live page before 🔴.
- **T** — training knowledge or ASO practice, not re-read. State it as practice, not as store fact.

## 5. Freshness protocol

Run when the date is more than 90 days after 2026-11-05 or the user mentions a console change: re-open the sources, compare, list differences under "Source drift".

| Source | URL |
|---|---|
| App Store product page + search guidance | https://developer.apple.com/app-store/product-page/ · https://developer.apple.com/app-store/search/ |
| App Store Connect field/screenshot/preview specs | https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information · …/screenshot-specifications · …/app-preview-specifications |
| Required, localizable and editable properties | https://developer.apple.com/help/app-store-connect/reference/app-information/required-localizable-and-editable-properties |
| Custom product pages / product page optimization | https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions · …/create-product-page-optimization-tests/overview-of-product-page-optimization |
| App Review Guidelines 2.3 | https://developer.apple.com/app-store/review/guidelines/#accurate-metadata |
| Play store listing | https://support.google.com/googleplay/android-developer/answer/9859152 |
| Play preview assets | https://support.google.com/googleplay/android-developer/answer/9866151 |
| Play Metadata policy | https://support.google.com/googleplay/android-developer/answer/9898842 |
| Play custom listings / experiments | https://support.google.com/googleplay/android-developer/answer/9867158 · …/12053285 |
| Play translations / release notes | https://support.google.com/googleplay/android-developer/answer/9844778 · …/9859348 |
| Play listing best practices | https://support.google.com/googleplay/android-developer/answer/13393723 |

## 6. Workflow map and artifacts

| Step | Artifact |
|---|---|
| 1 Frame | positioning sentence, audience, locales, rules |
| 2 Product truth | `claims-ledger` |
| 3 Keywords | `keyword-worksheet` |
| 4 Field allocation | field map in the worksheet |
| 5 Copy | `listing.md` (canonical format, lint-clean) |
| 6 Screenshots | `screenshot-plan` |
| 7 Release notes | notes per locale and store |
| 8 Lint and report | lint output + audit report |

## 7. Handoffs and limits

- Compliance of the listing (Apple 2.3.x, Play Metadata) is checked by `store-review-preflight` when installed; `08-compliance-guardrails.md` carries the rules this skill needs while writing.
- Privacy labels and Data safety are `privacy-audit` territory; the listing must not contradict them (e.g. "no data collected" while labels declare data).
- Not legal advice; claims about safety, health, finance or minors need the owner's confirmation.
