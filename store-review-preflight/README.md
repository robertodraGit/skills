# 🛫 store-review-preflight

> Audit a mobile app **before** the App Store or Google Play reviewer does. Checks your codebase, build config and store metadata against the Apple App Review Guidelines, Apple's build gates and Google Play policies, and returns an evidence-backed rejection-risk report.

```bash
npx skills add robertodraGit/skills --skill store-review-preflight
```

## Why

Rejections are cheap to avoid and expensive to discover: a review cycle costs days, and many causes are mechanical — a missing demo account, no in-app account deletion, a privacy manifest that does not list a required-reason API, a Data safety form that forgot an SDK, a `targetSdk` below the deadline.

The rules live in two constantly changing policy sites. This skill puts them inside your agent, row by row, and ties each one to something it can check in your repository.

## What it does

A seven-step preflight, each step ending on a verifiable *done when*:

1. **Frame** the target: platforms, stack, first submission vs update, account type, monetization, audience.
2. **Inventory** capabilities (login, IAP, UGC, AI, ads, health, location, WebView shell, OTA updates, …) with file paths.
3. **Run the gates**: binary requirements that fail uploads — Xcode/SDK minimums, privacy manifests, required-reason APIs, listed third-party SDK manifests and signatures, purpose strings, ATT, target API level, 16 KB page alignment, Data safety, account deletion, Play testing requirement.
4. **Triage rules** with a capability → rule matrix.
5. **Assess only the triggered rules**: Apple Guidelines 1–5 and Play policies, each rule with *applies when*, *how to check*, *evidence class*.
6. **Walk the console checklist** for everything the repo cannot prove (App Store Connect, Play Console, listing).
7. **Write the report** and a draft of the reviewer notes.

## Coverage

| Layer | Content | Source status |
| --- | --- | --- |
| Apple Guidelines 1–5 | Every numbered rule and sub-rule with check and evidence class | Read verbatim, guideline update of 2026-10-16 |
| Apple gates | Xcode 26 / iOS 13 floor, privacy manifest keys, 35 data types, 6 purposes, 5 required-reason categories and 18 reason codes, 86 listed SDKs, ATT, account deletion, App Privacy, new age ratings, DSA trader status | DocC JSON and Apple pages read |
| Google Play | User Data, permissions, Families, AI-generated content, subscriptions, ads; target API 36, 16 KB, Data safety, account deletion, new-account 12×14 testing, developer verification, deadlines through Aug 2027 | Pages read; sections marked `T` need a live check |
| Regulatory gates | DSA trader status, US state age-assurance laws, EAA, GDPR/Omnibus pointers | Secondary sources marked `V*` |
| Field patterns | 22 Apple and 13 Play rejection patterns with fixes | Experience-based (`T`) |
| Stacks | Expo, Capacitor/Cordova, React Native, Flutter, native, OTA updates | Config locations and traps |

Every row carries a **confidence tag**: `V` read on the audit source date, `V*` partly summarised, `T` training knowledge that must be re-verified before a 🔴.

## Verdicts

🔴 will fail · 🟠 likely rejection / decision needed · 🟡 risk · 🟢 pass · ⚪ not applicable · ❓ unverified

## Layout

```text
store-review-preflight/
├── SKILL.md
├── references/
│   ├── 00-method.md                  # verdicts, evidence, freshness, triage matrix
│   ├── 01-signals.md                 # stack detection, capability search, gate commands
│   ├── apple-01-safety.md … apple-05-legal.md
│   ├── apple-06-technical-gates.md
│   ├── google-01-policies.md
│   ├── google-02-technical-gates.md
│   ├── 07-common-rejections.md
│   ├── 08-stack-notes.md
│   └── 09-regulatory-gates.md
└── assets/
    ├── report-template.md
    ├── console-checklist.md
    └── review-notes-template.md
```

## Limits

Read-only: the skill never uploads, submits or runs store CLIs. It is an engineering-level screening, not legal advice, and it cannot guarantee approval. Policies change: the skill ships a freshness protocol and the live URLs to re-check.

Pairs with [`privacy-audit`](../privacy-audit) (data inventory, consent, store disclosure answers) and [`ai-act-audit`](../ai-act-audit) (EU AI Act).
