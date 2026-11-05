# 07 — Children, sensitive data, location, AI processing

Open when the inventory shows minors, health, biometrics, precise location, third-party AI, employees, or user-generated content. Confidence per row.

## 1. Children and teens

| Source | Rule | Conf |
|---|---|---|
| **GDPR Art. 8** | Consent-based online services offered directly to a child need the child to be at least the national age (13–16; **Italy 14**); below it, parental-responsibility holder consent with reasonable verification | T-s |
| **GDPR recital 38, Art. 12(1)** | Children merit specific protection; notices in clear plain language a child can understand | T-s |
| **COPPA** (US) | Under-13 directed services/actual knowledge: verifiable parental consent before collecting personal information; no conditioning participation on excess data; persistent identifiers count | T-s |
| **UK Children's Code (AADC)** (if UK users) | 15 standards: high-privacy defaults, no nudging, geolocation off by default, DPIA | T |
| **Apple 1.3 (Kids Category)** | No links out/IAP/distractions without parental gate; no PII/device info to third parties; **no third-party analytics or ads** except limited analytics collecting no IDFA/identifiable info/location/device info; limited contextual ads only with documented Kids policies and human review | V |
| **Apple 5.1.4(a)/(b)** | Birthdate/parental contact only for statutory compliance; apps primarily for kids should not include third-party analytics/ads; minors' personal info (name, address, email, location, photos, videos, drawings, chat, persistent identifiers) requires a privacy policy; **parental gate is generally not parental consent**; "For Kids"/"For Children" reserved for the Kids Category | V |
| **Apple 2.5.13** | Face-based account authentication must offer an alternate method for users under 13 | V |
| **Google Families** | Target-audience declaration; no AAID/SIM/Build Serial/BSSID/MAC/SSID/IMEI/IMSI from children-only apps; no location in children-only apps; only approved SDKs; certified ad SDKs; no personalised ads; social features need safety reminders and adult controls; COPPA/GDPR compliance | V |
| **Age-assurance laws** | Texas, Utah, Louisiana app-store laws; Apple Declared Age Range API, Google Play Age Signals API | V\* |

Audit steps:

1. Decide the audience from the product, not from the store category: kids' characters, language, content, and marketing count.
2. If minors are possible: list every SDK; for each, record whether it collects identifiers; flag all analytics/ads/attribution SDKs.
3. Check an age gate (neutral age screen, not "Are you over 13?"), the parental-consent flow for under-age users, and what is blocked until consent.
4. Check DPIA need (children + profiling/monitoring).
5. Apple Kids Category / Play Families declarations match the above.

Verdicts: third-party analytics/ads SDK in a kids-directed app → 🔴. No age screen in a service using consent as basis → 🟠. Policy not written for the audience → 🟡.

## 2. Special-category and sensitive data

| Data | Rule | Check |
|---|---|---|
| **Health** (GDPR Art. 9; Apple 1.4.1, 5.1.2(vi), 5.1.3; Play Health Content and sensors) | Explicit consent or another Art. 9(2) condition; no ads/data-mining use; no third-party sharing except to improve health management or research with permission; HealthKit data not in iCloud; no false data written | Trace health data to every SDK; separate consent screen; DPIA flag |
| **Biometrics** | Art. 9 when used to uniquely identify. Face ID/Touch ID via LocalAuthentication keeps templates on-device → not collected by you (Apple definition). Server-side face matching = special-category data | Distinguish on-device auth from server-side recognition; Apple 2.5.13 |
| **Location** | Not special-category under Art. 9 but sensitive in practice; precise or continuous location is high-risk profiling. Apple 5.1.5; Play: minimum scope, no location solely for ads/analytics, background only for core with disclosure, no location in children-only apps | Level (coarse/precise), frequency, background, retention, recipients |
| **Contacts / photos / files** | Minimise: system pickers (Apple 5.1.1(iii); Play Photo Picker). No contact databases (Apple 5.1.2(iv)); contacting people only on individual initiative | Upload of address book = high-risk; just-in-time disclosure |
| **Financial** | Payment data via processor; regulated services (Apple 5.1.1(ix) legal entity) | Where card data lives |
| **Criminal data** (Art. 10) | Only under official authority or specific law | Background-check features |
| **Inferred sensitive attributes** | Inference of health, orientation, religion from behaviour can be special-category | Recommender/ML features; also check `ai-act-audit` prohibitions (e.g. biometric categorisation) |

## 3. AI and automated processing (privacy angle)

Third-party model calls are *recipients* and often *processors*. Required items:

| # | Check | Rule |
|---|---|---|
| 1 | Inventory every call that sends user content or identifiers to a model provider | Art. 28, 30 |
| 2 | **Disclosure and explicit permission before the first send** | **Apple 5.1.2(i)** "including with third-party AI" (V) |
| 3 | Provider DPA, retention, training use, region confirmed (verify current terms) | Art. 28, 44–49 |
| 4 | Minimise: strip identifiers and unnecessary context from prompts; avoid sending special-category data | Art. 5(1)(c) |
| 5 | Users informed that content is processed by AI, with a way to opt out where AI is optional | Art. 13, consent |
| 6 | Output handling: moderation, report path | Apple 1.2 (V), Play AI-Generated Content (V) |
| 7 | Decisions about people (scoring, eligibility) | GDPR Art. 22 (human review, explanation); AI Act → `ai-act-audit` |
| 8 | DPIA flag: innovative technology + large-scale or vulnerable subjects | Art. 35 |
| 9 | Embeddings/vector stores hold personal data too: include in deletion and retention | Art. 17 |
| 10 | Logs of prompts/responses contain personal data: retention and access | Art. 5(1)(e), 32 |

## 4. User-generated content

UGC contains third parties' personal data. Needs: report/block/moderation (Apple 1.2), a takedown/erasure path, a policy for minors' content, retention for deleted accounts (shared content: Apple's deletion FAQ expects deletion to cover user-generated content shared with others, **V**), and a terms-of-use clause on prohibited content.

## 5. Employees and B2B

Workplace apps: employee monitoring has national rules (Italy: Statuto dei lavoratori art. 4, `10`). B2B SaaS: customer is usually controller, you are processor: DPA, instructions, sub-processor list, assistance with rights, return/delete on termination. Admin/audit features that surface employee behaviour need purpose limitation.

## 6. Escalation

DPIA triggers (two or more of: evaluation/scoring, automated decisions with legal effect, systematic monitoring, sensitive data, large scale, dataset matching, vulnerable subjects, innovative technology, blocking access to a service): report as 🟠 "DPIA likely" with the triggers; do not perform the DPIA here.
