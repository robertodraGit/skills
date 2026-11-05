# 🏷️ store-listing

> Write or audit an app's App Store and Google Play listing: localized metadata (Italian and English first), keyword allocation, descriptions, a screenshot plan, and user-facing release notes from a developer changelog. Every claim traces to evidence and every field passes a lint against store limits and policy.

```bash
npx skills add robertodraGit/skills --skill store-listing
```

## Why

The listing is the first thing a reviewer and a user read. Limits are enforced after you paste into a web form; keyword fields silently waste space on words the store already indexes; descriptions drift from privacy policies and labels; changelogs written for developers end up as release notes. This skill treats the listing like code: one canonical file, a claims ledger, a linter.

## What it does

An eight-step workflow, each step ending on a verifiable *done when*:

1. **Frame**: mode (create or audit), stores, locales, positioning, banned terms.
2. **Product truth**: claims ledger (every claim with evidence; policy-sensitive claims cross-checked).
3. **Keyword research**: candidates per locale, qualitative scoring, volume only from the user's tools.
4. **Field allocation**: what Apple indexes (name, subtitle, keywords, categories) vs what it does not; Play field rules.
5. **Copy**: native Italian and English, lint-clean.
6. **Screenshot plan**: one message per frame, captions per locale, demo data, sizes per store, "never show" list; verifies existing asset packs.
7. **Release notes**: changelog or git range → user-facing notes (Apple 4000, Play 500 per language with `<lang>` tags).
8. **Lint and report**: cross-checks against billing, privacy labels, age rating and moderation promises.

## Included tooling

```bash
python3 scripts/lint-listing.py docs/store/listing.md --banned "dating,incontri"
python3 scripts/changelog-to-notes.py --changelog CHANGELOG.md --version 3.4.1
python3 scripts/changelog-to-notes.py --git v3.3.0..HEAD
```

`lint-listing.py` (Python 3 stdlib) reads a markdown listing (`**Field** (limit)` + fenced block) and checks character limits, Apple keyword hygiene (spaces, duplicates, UTF-8 bytes, words already in name/subtitle including plural/singular), Play title/short-description rules, price and ranking claims, other-platform mentions, HTML, keyword stuffing, banned terms (flagging negated mentions separately), missing fields.

## Coverage

| Area | Content | Source status |
| --- | --- | --- |
| Field specs | Apple and Play text limits, editability, what is indexed, localizations, screenshots, previews, creative assets, custom pages, experiments | Official pages read 2026-11-05; summarised tables marked `V*` |
| Keywords | Research inputs, scoring, Apple packing rules, Play guidance | Store facts `V`, practice `T` |
| Copy | Field recipes, description skeleton, trust and sensitive domains, style checks | Practice, policy guardrails `V` |
| Screenshots | Plan template, narrative frameworks, specs, capture pipeline, preview rules | `V` / `V*` |
| Release notes | Conversion table, limits, templates, fastlane wiring | `V` / `T` |
| Italian and English | Locale strategy, codes, tone, quality checks | `T` |
| Experiments | Product page optimization, custom pages, Play experiments | `V` |
| Compliance for writers | Apple 2.3.x and Play Metadata rules | `V` |

Confidence tags: `V` read live on the audit date · `V*` summarised page · `T` practice (re-verify before a 🔴).

## Layout

```text
store-listing/
├── SKILL.md
├── references/00-method.md … 08-compliance-guardrails.md
├── scripts/lint-listing.py, changelog-to-notes.py
├── assets/listing-template.md, claims-ledger-template.md, keyword-worksheet.md,
│          screenshot-plan-template.md, audit-report-template.md
└── evals/evals.json
```

## Limits

It never invents search volumes, rankings or uplift, and never uploads to a console. Verdicts are an engineering and editorial review, not a guarantee of approval or ranking. Pairs with [`store-review-preflight`](../store-review-preflight) (compliance of the app) and [`privacy-audit`](../privacy-audit) (labels and policy).
