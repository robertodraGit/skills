# Claims ledger — {{product}}

Every factual claim in the listing, with its evidence. A claim without evidence is removed or marked ❓. Update this file when the product changes; the listing derives from it.

| ID | Claim (as it appears or could appear) | Where used (field, locale) | Evidence class | Evidence | Status | Owner confirmation |
|---|---|---|---|---|---|---|
| C1 | The app is free | description, promo | C/K | no IAP products; `BILLING` permission blocked; `EXPO_PUBLIC_FREE_RELEASE=true` | ✅ | — |
| C2 | No ads | description | C | no ad SDK; `AD_ID` removed | ✅ | — |
| C3 | Every photo is reviewed by a person before publishing | description (trust) | C/D | moderation queue implementation; runbook | ❓ staffing | owner |
| C4 | Reports are read within 24 hours | description (trust) | D | moderation runbook | ❓ | owner |
| C5 | Adults only (18+) | description | C | DB age check; legal gate | ✅ | — |

Evidence classes: **C** code · **K** console/vendor · **D** document · **L** live product · **O** owner statement.

Status: ✅ verified · ❓ needs confirmation · ❌ false/removed.

## Claims to never make (project rules)

- {{banned claim 1}}
- {{banned claim 2}}

## Time-sensitive claims (re-verify each release)

| Claim | Check by | Last verified |
|---|---|---|
