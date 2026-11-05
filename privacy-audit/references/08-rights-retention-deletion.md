# 08 — Rights handling, retention, account deletion

Goal: prove that "delete my account" removes or anonymises personal data in **every** system that holds it, and that access/portability requests are answerable.

Store rules (**V**): Apple 5.1.1(v) and the account-deletion page; Play account deletion (in-app + web link). GDPR Art. 12, 15–22 (**T-s**); vendor APIs **T** (verify names and endpoints).

## 1. Deletion requirements to satisfy

| Source | Requirement |
|---|---|
| Apple 5.1.1(v) | Apps that support account creation must let people **initiate deletion of the account within the app**; delete the account record and associated personal data (deactivation is insufficient); easy to find; link directly to a web page if one must be visited; tell users about timing, subscriptions and legally retained data; customer-service-only flows not allowed outside highly regulated industries; reauth/confirmation allowed; **revoke Sign in with Apple tokens** via the REST API; guest accounts deletable; deletion covers user-generated content shared with others; available to everyone, not only GDPR/CCPA users; subscribers told billing continues via Apple with `showManageSubscriptions`/subscriptions link/`beginRefundRequest`; scheduling deletion for subscription end allowed if immediate deletion is also offered |
| Play | In-app deletion **and** a web link (named after the app/developer, steps prominent, subscription steps explained); freezing/deactivation does not count; legally required retention disclosed in the privacy policy; Data safety deletion answers |
| GDPR Art. 17 | Erasure without undue delay (within one month, Art. 12(3)) unless an exception applies (legal obligation, establishment/exercise/defence of legal claims, public-interest). Inform recipients (Art. 19) |

## 2. Deletion trace procedure

1. List every system that holds the user's data (inventory vendor + storage rows).
2. For each: how is it deleted (cascade, job, vendor API, manual), when, and is it verified?
3. Mark: **deleted** / **anonymised** / **retained with reason (legal basis, period)** / **gap**.
4. Identify what is *not* reached by the primary delete: storage objects, analytics profiles, subscription records, push tokens, logs, search indexes, embeddings, backups, email-service contacts, support tickets.

## 3. Per-system patterns

| System | Pattern | Pitfall |
|---|---|---|
| **Postgres / Supabase** | Delete the auth user (admin API `auth.admin.deleteUser`) from a trusted server/edge function; make child tables reference `auth.users(id)` with `ON DELETE CASCADE` or delete rows explicitly; anonymise rows you must keep (orders) by nulling the user link | **Storage objects are not removed by row cascades**: list and delete the user's files in each bucket; service-role key must stay server-side; RLS blocks clients from deleting other tables |
| **Firebase** | Auth user delete; delete Firestore docs/Storage objects (Extension "Delete User Data" exists, T); Analytics user deletion via Google's user-deletion API (T) | Crashlytics keys/user IDs persist until their TTL |
| **PostHog** | Delete the person and events by `distinct_id` via the person-deletion API (T) | Replays and cached identifies; use a deletion request pipeline |
| **RevenueCat** | Delete the customer/subscriber via REST API (T); active store subscriptions are **not** cancelled by this | Apple/Play subscriptions continue billing: notify the user and link to management; schedule deletion option |
| **Stripe / processors** | Delete customer object or redact PII; keep invoices as required by tax law | Retained for legal obligation; disclose |
| **Sentry** | Delete user events by user ID where supported, or rely on short retention and no PII (T) | `setUser` with email defeats minimisation |
| **Push (APNs/FCM/OneSignal)** | Delete device tokens and external IDs on logout/deletion | Stale tokens keep the user in segments |
| **Email provider / CRM** | Remove contact and suppress; keep a hashed suppression entry if needed to avoid re-adding | Suppression list is retained data: disclose |
| **Object storage / CDN** | Delete objects and invalidate caches | Public URLs may remain cached |
| **Search index / vectors** | Delete documents and embeddings keyed to the user | Embeddings derived from user text are personal data |
| **Logs / backups** | Short retention; document that backups expire within N days and are not restored for deleted users without re-applying deletions | State the period in the policy |
| **Sign in with Apple** | Revoke refresh/access tokens with Apple's REST API (`appleid.apple.com/auth/revoke`, T) using the user's token | Required by Apple's FAQ (V). **With Supabase's native Apple flow (identity token) no refresh token is kept**: to revoke later you must exchange the authorization code at sign-in, store the resulting refresh token server-side, and call revoke in the deletion function. Absence of any such code in a project that offers Sign in with Apple is a 🟠/🔴 finding (confirm the production flag first) |
| **Third-party logins** | Remove stored provider tokens; instruct users to revoke app access in the provider (Apple 5.1.1(v): in-app way to revoke social credentials) | — |

## 4. Retention schedule

Create a table for the report:

| Data | Purpose | Retention | Trigger | Mechanism | Evidence |
|---|---|---|---|---|---|
| Account profile | Service delivery | Life of the account | Deletion | Cascade | |
| Invoices | Legal obligation | Per tax law (Italy: 10 years for accounting records, T) | Issuance | Archive table | |
| Support tickets | Support/claims | e.g. 24 months | Ticket close | Job | |
| Analytics events | Product improvement | e.g. 14 months | Capture | Vendor retention setting | |
| Crash reports | Stability | e.g. 90 days | Capture | Vendor setting | |
| Logs | Security | e.g. 30–90 days | Write | Log TTL | |
| Backups | Recovery | e.g. 30 days | Snapshot | Provider setting | |

Retention periods in the examples are placeholders: record the product's real values and the justification; "unknown" is a finding.

## 5. Data subject requests (access, portability, rectification, objection, restriction)

- **Channel**: a monitored address or in-app form, linked from the policy; identity verification proportionate (logged-in session is usually enough).
- **Timeline**: one month, extendable by two months for complexity with notice (Art. 12(3)).
- **Access/portability export**: structured, commonly used, machine-readable (JSON/CSV) covering data provided by the user and generated about them; implement as a job that queries all systems from the inventory.
- **Rectification**: profile edit propagates to vendors (CRM, billing).
- **Objection/withdrawal**: marketing opt-out absolute; analytics consent withdrawal stops SDKs and deletes identifiers; record the change.
- **Log**: requests, dates, actions (accountability, Art. 5(2)).

## 6. Web deletion page (Play requirement and good practice)

Public URL (no login needed to request), names the app/developer exactly as on the store, explains the in-app path and the offline request path (email/form with verification), states what is deleted, what is retained and why, and timeframes. Link it from the privacy policy and Play Console.

## 7. Verdicts

- No in-app deletion with account creation → 🔴 (Apple 5.1.1(v), Play).
- Deletion removes DB rows but leaves storage/analytics/subscription data undocumented → 🟠.
- Sign in with Apple present, no revoke call → 🔴 (Apple FAQ).
- Retention unknown for a data item → 🟠 (Art. 5(1)(e)).
- Web deletion link missing or not naming the app → 🔴 (Play).
