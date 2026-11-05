# Privacy Audit Report — {{product name}}

- **Date:** {{YYYY-MM-DD}}
- **Audited by:** AI-assisted screening (not legal advice)
- **Target:** {{mobile | web | backend}} · {{stack}} · {{version}}
- **Role of the audited party:** {{controller | processor for {{client}} | joint}}
- **Audience and regions:** {{adults | minors | employees}} · {{EU, Italy, US, …}}
- **Special data:** {{health | biometrics | precise location | none}}
- **Sources:** GDPR/ePrivacy (statute), Apple App Privacy / Guidelines 5.1 (updated {{date}}), Play Data safety / User Data ({{banner date}}), vendor docs per `06-sdk-catalog.md`. Freshness: {{ok | Source drift: …}}

## 1. Verdict summary

| | Count |
|---|---|
| 🔴 Likely violation / will fail | |
| 🟠 Decision or legal review needed | |
| 🟡 Improve | |
| 🟢 No issue identified | |
| ⚪ Not applicable | |
| ❓ Unverified | |

**Overall:** {{one paragraph: top three findings, fastest fix, and the biggest unknown}}

## 2. Data inventory (summary)

Full tables in the inventory file. Totals: {{N}} processing activities · {{N}} data items · {{N}} vendors.

| Activity | Data | Purpose | Basis | Recipients | Retention |
|---|---|---|---|---|---|

## 3. Findings

One block per finding. Order: 🔴, 🟠, store-blocking disclosures, 🟡.

### {{ID}} — {{short title}}  {{🔴|🟠|🟡}}

- **Requirement:** {{GDPR Art. 7 | ePrivacy 5(3) | Apple 5.1.2(i) | Play User Data → …}}
- **Confidence:** {{V | V* | T-s | T (re-verified: yes/no)}}
- **Party:** {{controller | developer | vendor}}
- **Evidence:** {{path:line · command output · console value (user-confirmed) · vendor doc URL}}
- **Why:** {{conditions met / uncertain}}
- **Fix:** {{concrete steps}}
- **Effort:** {{S | M | L}}

## 4. Consent and tracking matrix

| SDK / identifier | Reads/stores device data? | Classification (necessary / consent-gated / gap) | Gate location | Network check (N) |
|---|---|---|---|---|

## 5. Transparency check

| Inventory item | In privacy policy? | Notes |
|---|---|---|
| | | |

Policy gaps listed here; draft in `privacy-policy-skeleton.md` if requested.

## 6. Rights, retention, deletion

### Deletion trace

| System | Method | Status (deleted / anonymised / retained-with-reason / gap) | Evidence |
|---|---|---|---|

### Retention schedule

| Data | Retention | Mechanism | Status |
|---|---|---|---|

### Data subject requests

Channel · timeline · export capability · log: {{status}}

## 7. Vendors and transfers

| Vendor | Role | DPA | Region | Mechanism | Status |
|---|---|---|---|---|---|

## 8. Special regimes

Children · special categories · location · AI processing · UGC · employees · Italy: one line each with verdict or ⚪ and reason.

## 9. Store disclosures

### Apple

- Worksheet: `apple-privacy-worksheet.md` — {{complete}}
- Manifest: {{drafted | existing, differences listed}}
- ATT: {{required | not required}} — {{reason}}
- Differences from console answers: {{list}}

### Google Play

- Worksheet: `play-data-safety-worksheet.md` — {{complete}}
- Differences from console answers: {{list}}
- Account deletion: in-app {{ok}} · web link {{ok}}

## 10. Watch items

{{Digital Omnibus (not law), DPF appeal C-703/25 P, US state age laws, vendor changes}}

## 11. Information gaps and limits

- {{What could not be verified and the exact action that settles it}}
- Not legal advice; legal review recommended for all 🟠 on lawful basis, legitimate interest, transfers, minors, special categories.
- Rows tagged `T` were not re-read on the audit date unless marked.
