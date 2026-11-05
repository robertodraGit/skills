# 02 — GDPR core: articles as audit checks

Regulation (EU) 2016/679. Confidence **T-s** (statutory text, stable). Penalty tiers (Art. 83): up to **€10M / 2%** of worldwide turnover for the controller/processor-obligation articles (8, 11, 25–39, 42, 43 and others); up to **€20M / 4%** for principles (5–7, 9), data-subject rights (12–22) and transfers (44–49). National law adds rules (see `10-italy-notes.md`).

Columns: **Check** = what to verify; **Evidence** = C code, B build, K console, D documents.

## Scope and definitions

| Art. | Rule | Check | Evidence |
|---|---|---|---|
| 3 | Applies to controllers/processors established in the EU, and to those outside the EU that offer goods/services to people in the EU or monitor their behaviour in the EU | Is the product offered in EU languages/currencies/stores? Does it track users in the EU? If yes, GDPR applies regardless of where the developer sits | D, K |
| 4(1), (5) | Personal data includes online identifiers; pseudonymised data is still personal data | Do not treat hashed emails, device IDs or random user IDs as anonymous | C |
| 27 | Non-EU controllers/processors in scope need an EU representative | Non-EU operator with EU users | D |

## Principles (Art. 5) — the spine of the audit

| Principle | Check |
|---|---|
| Lawfulness, fairness, transparency | Every activity has a basis (Art. 6) and is explained in the policy |
| Purpose limitation | Data collected for one purpose is not reused (inventory "purpose" column vs actual flows, e.g. support emails used for marketing; Apple 5.1.2(ii)) |
| Data minimisation | Each field/permission is needed for a stated purpose; optional fields are optional (Apple 5.1.1(iii), (x)) |
| Accuracy | Users can correct data |
| Storage limitation | A retention rule exists per data item and is implemented (TTL jobs, deletion) |
| Integrity and confidentiality | TLS, access control, RLS, no secrets in the client, encryption at rest where appropriate (Art. 32) |
| Accountability | Records, DPAs, policy, evidence the controller can show (Art. 5(2), 24, 30) |

## Lawful basis (Art. 6) and consent (Art. 7)

| Basis | When it fits | Audit trap |
|---|---|---|
| 6(1)(a) Consent | Optional processing: marketing, non-essential analytics/SDK identifiers, personalised ads, optional AI features | Must be freely given, specific, informed, unambiguous, by clear affirmative action; **withdrawal as easy as giving** (Art. 7(3)); no pre-ticked boxes; no bundling with ToS; record it |
| 6(1)(b) Contract | Data needed to deliver the service the user signed up for (account, orders, subscription) | Not a basis for analytics, profiling or ads just because they are "in the ToS" |
| 6(1)(c) Legal obligation | Tax records, invoices, AML | Cite the law; retention follows it |
| 6(1)(d) Vital interests | Emergencies | Rare |
| 6(1)(e) Public task | Public bodies | Rare |
| 6(1)(f) Legitimate interests | Security/fraud, service improvement within expectations | Three-part test (purpose, necessity, balancing) documented; right to object (Art. 21); **cannot override ePrivacy consent for device access** (see `03`); Apple 5.1.1(ii) allows "legitimate interest" collection only if the whole GDPR is respected |

Consent checks in code: a consent record (timestamp, version, purpose, choice) is stored; SDKs initialise **after** the consent; a settings screen lets users change the choice; refusing does not degrade service beyond what the purpose requires.

## Special categories (Art. 9) and criminal data (Art. 10)

Processing special categories is prohibited unless an Art. 9(2) condition applies (explicit consent is the usual one for apps). Health, fitness data that reveals health, biometric identification, sexual-orientation inference and religion/politics count. Check: separate explicit consent screen, minimal collection, strict vendor limits (Apple 5.1.3 forbids ads/data-mining use). DPIA likely (Art. 35).

## Children (Art. 8)

Where consent is the basis for an online service offered directly to a child, the child must be at least the national digital-consent age (13–16; **Italy 14**, see `10-italy-notes.md`), otherwise holder-of-parental-responsibility consent with reasonable verification. See `07-children-sensitive-ai.md`.

## Transparency (Art. 12–14)

Art. 13 (data collected from the user) requires, at collection: controller identity and contact, DPO contact (if any), purposes and legal basis (and the legitimate interest pursued), recipients or categories, transfers outside the EEA and the safeguard used, retention period or criteria, the data subject rights (access, rectification, erasure, restriction, portability, objection, withdraw consent), the right to complain to a supervisory authority, whether providing data is a statutory/contractual requirement and consequences of not providing, and existence of automated decision-making/profiling with meaningful information. Art. 14 adds the source for data obtained elsewhere.

| Check | Evidence |
|---|---|
| Policy lists each purpose, basis, recipient category, retention, rights, complaint right; transfers named | D vs inventory |
| Policy is concise, intelligible, plain language, in the users' language (Art. 12(1)) | D |
| Layered notice at the point of collection (just-in-time text next to the field/permission) | C |
| The policy is linked in-app and in the store listing (Apple 5.1.1(i); Play User Data) | C, K |

## Data subject rights (Art. 15–22)

Respond within **one month** (extendable by two for complex requests, Art. 12(3)); free of charge generally; verify identity proportionately.

| Right | Check |
|---|---|
| 15 Access | Can the operator export all data about a person across systems? |
| 16 Rectification | Edit profile; propagate to vendors |
| 17 Erasure | Account deletion deletes the account and personal data from all systems, or retains with documented reason (legal obligation, claims). See `08` |
| 18 Restriction | Ability to freeze processing (flag) |
| 20 Portability | Machine-readable export for data provided by the user under consent/contract |
| 21 Objection | Opt-out of legitimate-interest processing and direct marketing (absolute for marketing) |
| 22 Automated decisions | Decisions with legal/similar effects need human involvement or specific bases; explain logic |

Where a mailbox is the only channel, check someone owns it and a log of requests exists.

## Controller design duties (Art. 24–25, 30, 32–36)

| Art. | Rule | Check |
|---|---|---|
| 24–25 | Data protection by design and by default | Defaults are privacy-protective: analytics off until consent, IP truncation, profile visibility private, minimal permissions |
| 26 | Joint controllers need an arrangement | Shared product with a partner, social plug-ins |
| 28 | Processor contract (DPA) with subject-matter, duration, nature, purpose, data types, categories of subjects; processor acts on documented instructions; confidentiality; security; sub-processor authorisation and flow-down; assistance with rights/breach/DPIA; delete or return at end; audits | A DPA exists for each processor; list sub-processors (see `09`) |
| 30 | Record of processing activities (RoPA). The SME exemption (<250 staff) is narrow: it does not apply to non-occasional processing | The inventory is a RoPA seed; a formal RoPA exists |
| 32 | Security appropriate to risk | TLS, access control, least privilege, encryption where fit, pseudonymisation, backups, logging, secrets management |
| 33–34 | Notify the authority within **72 hours** of becoming aware of a breach; inform individuals when high risk | A breach runbook and contacts exist |
| 35–36 | DPIA where processing is likely to result in high risk (systematic evaluation/profiling, large-scale special categories, large-scale monitoring of public areas); consult the authority if residual high risk | EDPB criteria (T): evaluation/scoring, automated decisions with legal effect, systematic monitoring, sensitive data, large scale, matching datasets, vulnerable subjects (children, employees), innovative tech (AI), blocking access to a service. Two or more criteria usually means a DPIA. Flag, do not perform |
| 37–39 | DPO required for public bodies and for core activities involving large-scale regular monitoring or special categories | Applicability |

## Transfers (Art. 44–49)

Personal data leaves the EEA only on an adequacy decision (including the EU–US DPF for certified US recipients, **V\***: in force, appeal pending), appropriate safeguards (SCCs 2021/914 plus transfer impact assessment, BCRs), or a derogation (Art. 49, narrow). See `09-transfers-vendors.md`.

## Cross-references to store rules

| GDPR | Apple | Google |
|---|---|---|
| Art. 13 transparency | 5.1.1(i) privacy policy in-app + metadata | User Data: privacy policy |
| Art. 7 consent | 5.1.1(ii) permission, withdrawal | Prominent disclosure and consent |
| Art. 17 erasure | 5.1.1(v) in-app account deletion | Account deletion in-app + web |
| Art. 5(1)(c) minimisation | 5.1.1(iii) | Permissions: incremental, core features |
| Art. 28 processors | 5.1.1(i) third parties equal protection | SDK responsibility |
| Art. 8 children | 1.3, 5.1.4 | Families |
