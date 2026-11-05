# Review notes template

Use for App Store Connect → *Notes for Review* and Play Console → *App content → App access*. Fill every section that applies; delete the rest. Write for a reviewer who has 15 minutes and no context. Never put real secrets in a repo copy: keep this file in the report as placeholders and let the user paste real values in the console.

## 1. What the app does (2–3 sentences)

{{Primary purpose, audience, and the one thing that differentiates it (4.2, 4.3(b)).}}

## 2. How to sign in

- **Username:** {{demo account}}
- **Password:** {{set by the user in the console}}
- **Environment:** production, backend monitored during review.
- **2FA/OTP:** none for this account / fixed code {{…}}.
- **Sign in with Apple / Google:** {{works with sandbox accounts | N/A}}.

Apple 2.1(a): a built-in demo mode needs prior Apple approval. Google: up to five instruction sets in *App access*.

## 3. Where to find things

| Feature | Path in the app | Notes |
|---|---|---|
| In-app purchase / subscription | Settings → Premium | Sandbox account works; products {{IDs}} |
| Account deletion | Settings → Account → Delete account | Removes the account and personal data; Apple token revoked |
| Report / block (UGC, AI output) | Long-press content → Report / Block | Moderation contact {{email}}, response {{SLA}} |
| Privacy controls (analytics consent, ATT) | Settings → Privacy | |
| Contact / support | Settings → About → Support | |

## 4. Non-obvious or gated features (2.5.19, 2.3.1(a))

- {{Feature behind a region/hardware/remote flag and how the reviewer can see it}}
- {{Hardware needed: …; otherwise a video: {{URL}}}}
- {{OTA updates: bug fixes and minor UI changes within the reviewed functionality; features requiring review ship as store builds.}}

## 5. Third-party services and data (5.1.1, 5.1.2(i))

| Service | Purpose | Data | Consent |
|---|---|---|---|
| {{LLM provider}} | {{feature}} | {{user text}} | Disclosure + opt-in before first send |
| {{Analytics / crash}} | {{…}} | {{…}} | {{…}} |

## 6. Regulated or special content (if applicable)

- Health/medical: {{disclaimer, sources, regulatory status (1.4.1–1.4.2)}}
- Finance/crypto/gambling: {{entity, licences, geo-restriction (3.1.5, 5.3.4)}}
- Kids: {{parental gate location, no third-party analytics (1.3)}}
- Age assurance: {{Declared Age Range / Play Age Signals handling}}

## 7. Changes since the last version

{{Specific list, not "bug fixes" (2.3.1(a))}}
