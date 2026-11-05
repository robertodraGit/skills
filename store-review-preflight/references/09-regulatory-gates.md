# 09 — Regulatory gates that block or shape a release

Laws that the stores enforce through requirements, or that change what a reviewer or regulator expects. Status as of **2026-11-05**. Most rows are moving targets: the verdict ceiling for unstable rows is 🟡/🟠 with a live-source check, never 🔴.

## 1. EU Digital Services Act — trader status — **V**

Apple: **trader status** required for apps in the EU; since **2025-02-17** apps without it are removed from the EU App Store (since 2024-10-16 required to submit updates in the EU). Check (K) App Store Connect → trader status declared; contact details visible on the product page. Google Play has an equivalent trader declaration in Play Console (T: verify path).

## 2. Age assurance laws (US states) — **V\*** unstable

Search results on 2026-11-05 (secondary sources; confirm on Apple/Google developer news):

| Law | Status reported |
|---|---|
| **Texas SB 2420** (App Store Accountability Act) | Effective 2026-01-01; blocked by a December 2025 preliminary injunction; reportedly stayed by the Fifth Circuit on 2026-06-01 (no permanent stay); Apple told developers compliance began **2026-06-04** for new Texas Apple Accounts |
| **Utah** | Developer obligations reportedly from **2026-05-06**; enforcement reportedly from **2026-12-31** |
| **Louisiana** | Sources disagree: **2026-07-01** or pushed to **2027-07-01** |
| **Apple tooling** | **Declared Age Range API** (returns an age category plus a verification signal rather than a birthdate), **Significant Change API** in PermissionKit, new age-rating property in StoreKit, App Store Server Notifications |
| **Google tooling** | **Play Age Signals API** (returned signals for eligible Texas users who created accounts after 2026-05-28); Play policy: Age Signals API for legal-obligation use only, no ads/profiling/sharing |

Audit action: if the app has US users and age-gated features (social, UGC, adult content, purchases by minors), check whether it calls the age-range APIs and handles significant-change notifications. Verdict ceiling 🟡; recommend reading the live Apple/Google developer news.

## 3. European Accessibility Act (EAA) — **V\*** secondary sources

- Applies to private companies since **2025-06-28** for in-scope products/services (e-commerce, banking, transport, e-books, etc.; micro-enterprise services exemption exists, T). Mobile apps are generally expected to meet EN 301 549 (WCAG 2.1 AA).
- Italy: AgID is the enforcement authority; reported complaints platform live in **March 2026**; sources conflict on the guideline/determination numbers and penalty amounts: do not cite them.
- Providers need a working **feedback mechanism** for accessibility complaints, including in the store listing and on the provider's website (reported by one secondary source).
- Audit action: accessibility labels (`accessibilityLabel`, `contentDescription`), dynamic type support, contrast, screen-reader flow on the login/purchase path; a published accessibility statement and contact. Verdict ceiling 🟡 unless a clear in-scope service has no accessibility statement (🟠).

## 4. GDPR, ePrivacy, transfers, Digital Omnibus — **V\***

Owned by `privacy-audit` (`references/00-method.md` §5). Snapshot:

- **EU–US Data Privacy Framework** in force; the Court of Justice appeal *Latombe v Commission* (C-703/25 P, lodged 2025-10-31) is pending; a 2026-06-28 report notes Microsoft intervened in support of the Commission.
- **Digital Omnibus (data/cookies/GDPR part)**: Commission proposal COM(2025) 837 (2025-11-19); Council mandate agreed **2026-10-21**; Parliament position unconfirmed; **not law**. Do not audit against proposed text.
- **Digital Omnibus on AI** adopted as Regulation (EU) 2026/1744 (published 2026-07-24): see `ai-act-audit`.

## 5. AI features — pointer

Generative-AI transparency (Art. 50) applies since **2026-08-02**; prohibitions since 2025-02-02. If the app generates synthetic media or text for EU users, run `ai-act-audit` (if installed) and keep the store-side requirements here (Apple 1.2 AI content creation, 5.1.2(i) third-party AI; Play AI-Generated Content).

## 6. Regulated domains

Financial services, health, gambling, cannabis, crypto: Apple 5.1.1(ix) requires a **legal-entity** account; Apple 3.1.5, 3.2.1(viii), 3.2.2(viii)–(ix) and Play's Financial Services/Gambling/Health policies add licences and geo-fencing. Record the licences the developer holds and where the app is offered.

## 7. Using this file in the report

Add a "Regulatory gates" section with one line per row: status (🟢/🟡/🟠/⚪/❓), evidence, and the live source the user should confirm. Never present these as legal advice.
