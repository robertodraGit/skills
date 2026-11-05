# 🔐 privacy-audit

> Find what personal data your app or product really handles, compare it with what you tell people, and generate the store disclosures from the code: GDPR/ePrivacy audit, privacy policy draft, Apple App Privacy answers plus `PrivacyInfo.xcprivacy`, and Google Play Data safety answers.

```bash
npx skills add robertodraGit/skills --skill privacy-audit
```

## Why

Privacy answers are scattered across five places that must agree: the code, the privacy policy, the Apple label and manifest, the Play Data safety form, and the consent UI. They drift every time an SDK is added. Reviewers and regulators check them against each other.

This skill makes the **data inventory** the single source of truth, built from the repository, then derives and checks everything else.

## What it does

An eight-step audit, each step ending on a verifiable *done when*:

1. **Frame**: product, role (controller or processor), audience, regions, special data.
2. **Build the data inventory** from forms, permissions, storage, schemas, logs, outbound domains and every SDK.
3. **Lawful basis, consent and tracking**: Art. 6/7/9, ePrivacy 5(3), SDK consent gating, ATT vs GDPR consent, UMP.
4. **Transparency, rights, retention, deletion**: policy vs inventory, deletion trace through every system.
5. **Vendors and transfers**: roles, DPAs, regions, SCCs, EU–US DPF status.
6. **Special regimes**: children, health, biometrics, location, third-party AI, UGC, employees, Italy.
7. **Store disclosures**: Apple App Privacy worksheet, manifest, Play Data safety worksheet, diff against console answers.
8. **Report and drafts**: findings with evidence, citations, fixes; optional privacy policy draft.

## Coverage

| Area | Content | Source status |
| --- | --- | --- |
| GDPR core | Articles as audit checks: principles, bases, consent, Art. 9, children, transparency, rights, design, RoPA, breach, DPIA triggers, transfers | Statute (`T-s`) |
| ePrivacy and tracking | Art. 5(3) scope for apps/SDKs, valid consent tests, per-SDK gating patterns, ATT vs GDPR, identifier cheat-sheet | Mixed `T` / `V` |
| Apple | Data types ↔ manifest identifiers, definitions, optional-disclosure criteria, tracking, manifest keys, Guideline 5.1 | Apple pages and DocC read |
| Google Play | Data types, purposes, collection vs sharing vs ephemeral, security practices, User Data policy, Families | Play pages read |
| SDK catalog | Firebase, PostHog, Sentry, RevenueCat, AppsFlyer, Meta, AdMob, Supabase, Expo; patterns for the rest, incl. third-party AI | Vendor docs read; gaps marked "not in pages read" |
| Rights and deletion | Per-system deletion patterns (Supabase, Firebase, PostHog, RevenueCat, Sentry, push, storage, vectors), retention schedule, DSR handling | Store rules `V`, vendor APIs `T` |
| Transfers | Roles, Art. 28 checklist, DPF status (appeal pending), region selection | `V*` |
| Italy | Age 14, Garante cookie guidelines, workplace monitoring, retention anchors | `T` |

Confidence tags: `V` read on the source date · `V*` partly summarised or secondary · `T-s` statute · `T` re-verify before a 🔴.

## Legal-status snapshot (2026-11-05)

- GDPR/ePrivacy in force. The Digital Omnibus data/cookie changes are **proposals**; the Council mandate (21 Oct 2026) exists, Parliament's position is unconfirmed. The AI part is already law (Reg. 2026/1744).
- EU–US Data Privacy Framework in force; the Court of Justice appeal C-703/25 P is pending.

## Layout

```text
privacy-audit/
├── SKILL.md
├── references/
│   ├── 00-method.md … 10-italy-notes.md
└── assets/
    ├── report-template.md
    ├── data-inventory-template.md
    ├── privacy-policy-skeleton.md
    ├── apple-privacy-worksheet.md
    ├── play-data-safety-worksheet.md
    └── privacy-manifest.example.xcprivacy
```

## Limits

Engineering-level screening, not legal advice. It does not perform DPIAs, security testing or contract review; it flags them. Never prints personal data or secrets it finds. Pairs with [`store-review-preflight`](../store-review-preflight) and [`ai-act-audit`](../ai-act-audit).
