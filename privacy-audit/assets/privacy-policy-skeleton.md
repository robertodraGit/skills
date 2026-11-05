# Privacy policy skeleton

Generate a draft **only from inventory facts**. Replace every `{{…}}`; delete sections that do not apply; do not add claims the inventory cannot support. The draft needs legal review before publication. Write in the users' language (Italian for Italian users).

Store requirements to satisfy (see `04-apple-privacy.md`, `05-google-data-safety.md`): public HTML URL; linked in the app and in App Store Connect / Play Console; names the developer/app; states what is collected, how and all uses; third-party equal protection; retention, deletion and consent revocation; developer contact.

---

# Privacy Policy — {{App / Product name}}

Last updated: {{date}} · Version {{n}}

## 1. Who we are

{{Controller legal name, address, registration number}}. Contact: {{privacy email}}. {{DPO name and contact, if appointed}}. {{EU representative, if applicable}}.

## 2. What data we process, why, and on what basis

| Purpose | Data | Legal basis | Retention |
|---|---|---|---|
| Create and manage your account | {{email, name, password hash, user ID}} | Contract (Art. 6(1)(b)) | Until you delete the account |
| Provide {{core feature}} | {{data}} | Contract | {{period}} |
| Process purchases and subscriptions | {{purchase history, subscription status}}; payment details are handled by {{Apple/Google/Stripe}} | Contract; legal obligation (Art. 6(1)(c)) for invoices | {{10 years for accounting records in Italy}} |
| Measure how the app is used | {{events, device identifiers, IP}} | Consent (Art. 6(1)(a)); you can change your choice in {{Settings → Privacy}} | {{period}} |
| Detect crashes and keep the service secure | {{crash logs, device/OS info}} | {{Legitimate interest (Art. 6(1)(f)) | consent}} | {{period}} |
| Send you notifications | {{push token}} | {{Service: your device permission | Consent for marketing}} | Until you disable or delete |
| {{AI feature}} | {{text/images you submit}} sent to {{provider}} | Consent (Art. 6(1)(a)) | {{period at provider and at us}} |

## 3. Where the data comes from

You (forms, content, permissions), your device (identifiers, usage), {{sign-in provider}}, {{purchase platform}}.

## 4. Who receives your data

| Recipient | Role | Purpose | Location |
|---|---|---|---|
| {{Supabase}} | Processor | Hosting and database | {{EU region}} |
| {{PostHog}} | Processor | Analytics | {{EU (Frankfurt)}} |
| {{RevenueCat}} | Processor | Subscription management | {{…}} |
| {{Sentry}} | Processor | Crash reporting | {{…}} |
| {{AI provider}} | Processor | {{feature}} | {{…}} |
| {{Apple / Google}} | Independent controllers | App distribution, payments, sign-in | — |

We do not sell personal data. {{We do not use your data for advertising | We share data with advertising partners as described in section 6.}}

## 5. Transfers outside the EEA

{{Describe each: country, recipient, safeguard (adequacy decision, EU–US Data Privacy Framework certification, Standard Contractual Clauses), how to get a copy}}.

## 6. Tracking, identifiers and your choices

{{List SDK identifiers and what they do; how consent is requested; how to change or withdraw it; Apple App Tracking Transparency if used; Android advertising ID opt-out if used}}.

## 7. How long we keep data

{{Retention table or criteria per data item. Backups expire after {{N}} days.}}

## 8. Your rights

Access, rectification, erasure, restriction, portability, objection, withdrawal of consent at any time (without affecting prior processing), and the right not to be subject to solely automated decisions with legal or similarly significant effects. How to exercise them: {{in-app path / email}}; we answer within one month. You can lodge a complaint with {{Garante per la protezione dei dati personali (www.garanteprivacy.it) | your local supervisory authority}}.

## 9. Delete your account

In the app: {{Settings → Account → Delete account}}. Without the app: {{URL / email with verification}}. What is deleted: {{…}}. What we keep and why: {{legal obligations, e.g. invoices}}. Active subscriptions are managed through {{Apple/Google}}: {{instructions}}.

## 10. Children

{{Not directed to children under {{age}} | age gate and parental consent description}}. {{Italy: under 14 parental consent is required for services based on consent.}}

## 11. Security

{{Encryption in transit, access controls, hosting security, breach notification commitment}}.

## 12. Changes to this policy

{{How you notify users of material changes}}.

## 13. Contact

{{Privacy contact}}.

---

## Drafting checklist

- [ ] Every row of the inventory data table appears in section 2 or 6.
- [ ] Every vendor appears in section 4 with role and location.
- [ ] Section 9 matches the actual deletion flow (trace in the report).
- [ ] Apple/Play labels and this policy say the same thing.
- [ ] Language and tone fit the audience (plain language; children's version if needed).
