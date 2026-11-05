# Store Review Preflight Report — {{app name}}

- **Date:** {{YYYY-MM-DD}}
- **Audited by:** AI-assisted screening (not legal advice, not an approval guarantee)
- **Target:** {{platforms}} · {{stack}} · {{version/build}} · {{first submission | update}}
- **Developer account:** {{individual | organization}} (Apple) · {{personal | organization}} (Google)
- **Sources used:** Apple App Review Guidelines (last updated {{date seen}}), Apple *Upcoming requirements*, Google Play Policy Center ({{banner date}}). Reference freshness: {{ok | Source drift: …}}

## 1. Verdict summary

| | Count |
|---|---|
| 🔴 Will fail | |
| 🟠 Likely rejection / decision needed | |
| 🟡 Risk | |
| 🟢 Pass | |
| ⚪ Not applicable | |
| ❓ Unverified | |

**Overall:** {{Ready | Not ready: N blockers}}. {{One paragraph: the three findings most likely to cause rejection, and the single fastest fix.}}

## 2. Capability inventory

| Capability | Found? | Paths | Notes |
|---|---|---|---|

## 3. Gates

### Apple

| Gate | Evidence | Status | Detail |
|---|---|---|---|
| G-A1 Toolchain and deployment target | | | |
| G-A2 Privacy manifest valid | | | |
| G-A3 Required-reason APIs | | | |
| G-A4 Listed SDKs: manifest + signature | | | |
| G-A5 Purpose strings | | | |
| G-A6 ATT consistent | | | |
| G-A7 Account deletion (+ Apple revoke) | | | |
| G-A8 App Privacy answers | | | |
| G-A9 Age rating | | | |
| G-A10 DSA trader status | | | |
| G-A11 Export compliance | | | |
| G-A12 APNs / receipts | | | |

### Google Play

| Gate | Evidence | Status | Detail |
|---|---|---|---|
| G-G1 targetSdk ≥ 36 | | | |
| G-G2 16 KB alignment | | | |
| G-G3 Data safety | | | |
| G-G4 Account deletion in-app + web | | | |
| G-G5 12 testers × 14 days (new personal account) | | | |
| G-G6 App content declarations | | | |
| G-G7 AD_ID consistency | | | |
| G-G8 Developer verification / registration | | | |
| G-G9 Bundle, FGS types, notifications, exported, cleartext | | | |

## 4. Findings

One block per finding, ordered: upload-blocking gates, 🔴, 🟠, metadata, 🟡.

### {{ID}} — {{short title}}  {{🔴|🟠|🟡}}

- **Rule / gate:** {{Apple 5.1.1(v) | Play: User Data → Account deletion | G-A4}}
- **Confidence:** {{V | V* | T (re-verified live: yes/no)}}
- **Evidence:** {{path:line · command output · console value (user-confirmed) · listing quote}}
- **Why it fails:** {{conditions met / uncertain}}
- **Fix:** {{concrete steps}}
- **Effort:** {{S | M | L}}
- **Reviewer note to add:** {{text for Notes for Review, if relevant}}

## 5. Regulatory gates

| Row (`09-regulatory-gates.md`) | Status | Evidence | Live source to confirm |
|---|---|---|---|

## 6. Console and listing checklist

Completed from `assets/console-checklist.md`: {{verified | user-confirmed | unknown}} counts, and the unknown items listed here.

## 7. Common-rejection second pass

Rows from `07-common-rejections.md` that match this app, each linked to a finding above.

## 8. Draft review notes

{{Filled from assets/review-notes-template.md}}

## 9. Information gaps and limits

- {{What could not be verified and the exact command or console path that would settle it}}
- Reviewers apply judgement beyond the written rules; passing this audit does not guarantee approval.
- Store policies change; rows tagged **T** were not re-read on the audit date unless marked.
