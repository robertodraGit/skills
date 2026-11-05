# 09 — Roles, processors, transfers

## 1. Role per vendor

| Vendor type | Typical role | Consequence |
|---|---|---|
| Hosting, DB, auth, storage, email delivery, crash/analytics acting on your instructions | Processor | Art. 28 DPA, sub-processor list, instructions, deletion/return |
| Ad networks, attribution partners, data brokers, social login providers (for their own purposes) | Independent controller or joint controller | Disclose as recipient; consent where needed; Art. 26 arrangement if joint; for Google Play "sharing" |
| Payment processors, app stores | Often independent controllers for their own obligations (fraud, tax) | Disclose; they are not "your processors" for that processing |
| AI model providers | Processor when acting on instructions under API terms; check for provider-purpose processing | DPA, retention, training terms |

Developers building for clients: the client is the controller, the developer/agency a processor (see `00-method.md` §7). The agency still needs its own sub-processor chain (hosting, tools) covered by a DPA with the client.

## 2. DPA checklist (Art. 28(3), T-s)

A binding contract covering: subject matter and duration; nature and purpose; type of personal data and categories of subjects; controller obligations and rights; processing **only on documented instructions** (including transfers); **confidentiality** commitments of staff; **security measures** (Art. 32); **sub-processors** (prior specific or general written authorisation, same obligations flowed down, processor stays liable); **assistance** with data-subject rights, breach notification, DPIA; **deletion or return** at the end; **audit** and information rights.

Record per vendor: DPA signed / click-through accepted / not available (K evidence), where it lives, the date, sub-processor list URL.

## 3. Transfer mechanisms (Art. 44–49, T-s)

| Situation | Mechanism |
|---|---|
| Recipient in the EEA or in an adequacy country | No transfer restriction (adequacy list: verify current) |
| US recipient certified under the **EU–US DPF** | Adequacy (decision of 2023-07-10). **Status V\***: in force; General Court dismissed the *Latombe* challenge on 2025-09-03; appeal C-703/25 P pending. Advise a fallback (SCCs) for critical vendors |
| Other third country, no adequacy | **SCCs** (Decision 2021/914; modules for controller→processor etc.) plus a **transfer impact assessment** and supplementary measures if needed; or BCRs |
| Derogations (Art. 49: explicit consent, contract necessity) | Narrow, occasional; not for systematic flows |

Also consider **remote access** from outside the EEA (support staff, sub-processors) and **backups/log shipping** as transfers.

## 4. Region selection

| Vendor | Facts | Conf |
|---|---|---|
| **Supabase** | One primary region per project; choose a specific EU region: eu-central-1 Frankfurt, eu-west-1 Ireland, eu-west-3 Paris, eu-north-1 Stockholm. The "Europe" group includes London and Zurich (not EU member states). Postgres, Auth, Storage stay in the primary region; backups/logs/Edge Functions/sub-processors can affect residency | V |
| **PostHog** | Cloud EU hosted in Frankfurt; ingestion `eu.i.posthog.com`; DPA self-serve on all plans | V |
| **Firebase / Google Cloud** | Region choice varies per product; Auth/Analytics/Crashlytics have limited location control | T |
| **Sentry** | EU region available for organisations (de.sentry.io, T); verify | T |
| **Vercel** | Function and edge regions configurable; global CDN | T |
| **RevenueCat** | GDPR/EU hosting not found in pages read | — |
| **AI APIs** | Many offer region or zero-retention options on request | T |

## 5. Vendor register (copy into the inventory)

| Vendor | Service | Role | Data categories | DPA | Region | Transfer mechanism | Sub-processors URL | Evidence |
|---|---|---|---|---|---|---|---|---|

## 6. Verdicts

- Vendor receiving personal data without a DPA (processor) → 🟠 (🔴 if confirmed absent and no contractual terms apply).
- US vendor, no DPF certification, no SCCs → 🔴 (Art. 44–46).
- Non-EU region chosen for EU-only product without a documented reason → 🟡/🟠.
- Sub-processor list not published or monitored → 🟡.
