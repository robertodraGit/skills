# Data inventory — {{product}}

Seed of the record of processing (Art. 30). One row per fact; every row has an evidence path. Never write real personal data or secrets here.

## 1. Processing activities

| ID | Activity | Purpose | Data subjects | Role (controller / processor) | Lawful basis (Art. 6) | Art. 9 condition | Consent mechanism (where in code) | DPIA flag |
|---|---|---|---|---|---|---|---|---|
| P1 | Account creation and login | Service delivery | Users | | 6(1)(b) | n/a | n/a | |
| P2 | Product analytics | Improve the product | Users | | 6(1)(a) | n/a | | |
| P3 | Crash reporting | Stability | Users | | 6(1)(f)? / 6(1)(a)? | n/a | | |
| P4 | Subscriptions and purchases | Contract, tax | Users | | 6(1)(b), 6(1)(c) | n/a | | |
| P5 | Push notifications | Service / marketing | Users | | | n/a | | |

## 2. Data items

| ID | Data item | Category | Source (form / SDK / permission / server) | Activity | Special category? | Minor-related? | Storage location | Retention | Recipients | Leaves device? (Apple "collected") | Evidence (path:line) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D1 | Email | Contact Info / Personal info | Sign-up form | P1 | No | | DB `users.email` | Life of account | Supabase, email provider | Yes | |
| D2 | User ID | Identifier | Auth | P1, P2 | No | | DB | Life of account | Analytics SDK | Yes | |
| D3 | Device/installation ID | Identifier | SDK | P2, P3 | No | | Vendor | | | Yes | |
| D4 | Crash logs | Diagnostics | Crash SDK | P3 | No | | Vendor | | | Yes | |

## 3. Vendors and recipients

| Vendor | Service | Evidence (where found) | Role | Data categories | DPA | Region | Transfer mechanism | Consent-gated? | Declared in Apple label | Declared in Play form |
|---|---|---|---|---|---|---|---|---|---|---|

## 4. Permissions and device capabilities

| Permission / capability | Declared in | Purpose string / disclosure | Needed for | Deny path works? | Evidence |
|---|---|---|---|---|---|

## 5. Open questions

| # | Question | Owner | Needed for |
|---|---|---|---|
