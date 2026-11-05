# Store Listing Audit — {{product}}

- **Date:** {{YYYY-MM-DD}}
- **Mode:** {{Audit | Create | Single piece}}
- **Stores / locales:** {{Apple: it, en · Play: it-IT, en-US}}
- **Inputs:** {{listing file, claims ledger, ASO data supplied: yes/no (which)}}
- **Sources:** Apple product page/App Store Connect help, App Review Guidelines (updated {{date}}), Google Play help and Metadata policy. Freshness: {{ok | Source drift: …}}
- **Lint:** `python3 scripts/lint-listing.py {{file}} --banned "{{terms}}"` → {{N errors, M warnings}}

## 1. Summary

| | Count |
|---|---|
| 🔴 Invalid | |
| 🟠 Weak or risky | |
| 🟡 Improve | |
| 🟢 Good | |
| ❓ Unverified | |

**Overall:** {{one paragraph: the three changes with the highest value, and what data is missing}}

## 2. Positioning and claims

- Positioning sentence: {{}}
- Banned/required terms: {{}}
- Claims ledger: {{N claims, N verified, N needing owner confirmation}}

## 3. Field-by-field

| Store | Locale | Field | Chars / limit | Verdict | Issue | Proposal |
|---|---|---|---|---|---|---|

## 4. Keywords

| Locale | Wasted characters | Duplicates | Missing high-value terms | Proposed set | Volume data |
|---|---|---|---|---|---|

## 5. Screenshots and graphics

| Check | Status | Notes |
|---|---|---|
| Frames 1–3 understandable alone | | |
| Real UI, demo data, no banned frames | | |
| Required sizes and formats | | |
| Localized captions | | |
| Play ≥ 4 screenshots at ≥ 1080 px; feature graphic | | |

## 6. Release notes

Source used: {{CHANGELOG | git range}} · Freshness: {{}} · Proposed notes per locale: {{}}

## 7. Cross-checks

| Listing statement | Contradicts | Verdict |
|---|---|---|

## 8. Findings

### {{ID}} — {{title}}  {{🔴|🟠|🟡}}
- **Where:** {{store · locale · field}}
- **Rule:** {{Apple 2.3.7 | Play Metadata | limit | project rule}} · **Confidence:** {{V | V* | T}}
- **Evidence:** {{lint line, quote, ledger id}}
- **Fix / proposal:** {{replacement text}}
- **Effort:** {{S | M | L}}

## 9. Rewritten fields

Paste-ready text per field, lint-clean.

## 10. Information gaps and limits

- {{Missing ASO data and where to get it}}
- {{Console-only facts not seen}}
- No ranking or uplift is predicted. Store rules change; rows tagged T were not re-read.
