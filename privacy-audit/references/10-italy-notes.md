# 10 — Italy notes

Open when users, clients or the operator are in Italy. Confidence **T** unless marked. The Garante (Garante per la protezione dei dati personali, www.garanteprivacy.it) is the authority. Verify each point on the Garante site before stating it as a 🔴.

## 1. Legal framework

- GDPR applies directly. National rules: **Codice in materia di protezione dei dati personali**, D.Lgs. 196/2003 as amended by D.Lgs. 101/2018 (T-s).
- **Age of digital consent: 14** (art. 2-quinquies Codice Privacy, T-s). Under 14, consent for information-society services requires the holder of parental responsibility.
- Italy's national AI law (Legge 132/2025, in force from October 2025, T) includes provisions on minors' access to AI systems (parental consent under 14) and on AI in the workplace: check with legal counsel if the product uses AI for minors or employees. Link to `ai-act-audit`.

## 2. Cookies and other tracking tools

- **Garante Guidelines on cookies and other tracking tools** (10 June 2021; compliance window ended January 2022, T):
  - Banner with a choice to refuse; the **"X" close button** is equivalent to continuing with default settings (no consent), not a reject (T).
  - Granular consent per purpose; scrolling or continued browsing alone is not consent.
  - Do not re-prompt for **6 months** after a refusal unless circumstances change (T; the Council's Digital Omnibus mandate discusses a 4-month interval, **V\***, not law).
  - Analytics cookies may be treated like technical cookies only if audience data is aggregated, third-party analytics is restricted to the controller's purposes, **IP is masked** (at least partially), and the third party cannot cross-correlate (T). Otherwise consent.
  - Cookie wall: generally not permitted when it blocks access without alternative (T).
  - Information: short banner plus extended notice with the list of cookies/trackers.
- The Garante applies the same logic to SDKs and device identifiers in apps (EDPB 2/2023, T).

## 3. International transfers and analytics

The Garante and several EU authorities held in 2022 that Google Analytics transfers to the US were unlawful before the DPF (T). The DPF now supports certified US recipients (**V\***: in force, appeal pending). For Italian clients, document the transfer mechanism and the mitigation (IP anonymisation, EU region, consent) explicitly.

## 4. Workplace and monitoring

Tools capable of monitoring employees (activity tracking, geolocation of company devices, productivity analytics, session replay of staff tools) are governed by **art. 4 Statuto dei lavoratori (L. 300/1970)** as amended: agreement with unions or authorisation from the labour inspectorate, plus information to workers (T). Flag as 🟠 "legal review" and do not conclude.

## 5. Records and retention

- Accounting records and invoices: **10 years** (art. 2220 Codice civile, T). Use this as the "legal obligation" retention in `08`.
- Video surveillance, health data, and biometric attendance have Garante-specific measures: refer to counsel.

## 6. Language and presentation

- Information to Italian users in clear Italian; layered notice; links to the full policy in app and store listing (Apple 5.1.1(i), Play User Data).
- The Italian privacy policy should name the controller, DPO (if appointed), purposes/bases, retention, recipients, transfers, rights and the right to complain to the Garante.

## 7. Accessibility

European Accessibility Act applies since 2025-06-28; AgID oversees complaints in Italy (**V\***, secondary sources). Consent banners and privacy settings must be keyboard- and screen-reader-accessible.

## 8. Using this file

Add an "Italy-specific" section to the report with: age-gate (14), cookie/SDK banner behaviour, analytics treatment, workplace-monitoring flag, retention anchors, language of notices. All `T` rows get an explicit "verify on garanteprivacy.it" action.
