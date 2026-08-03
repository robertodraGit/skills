---
name: ai-act-audit
description: Audit an application, codebase, product, or AI system for compliance with the prohibited AI practices of the EU AI Act (Article 5, Regulation (EU) 2024/1689), based on the official European Commission Guidelines C(2025) 5052. Use this skill whenever the user asks to check, audit, review, or verify AI Act compliance, EU AI regulation compliance, prohibited AI practices, Article 5 risks, or whether an app/feature/AI system "respects the AI Act" — even if they only mention "compliance" or "AI regulation" generically in an EU context. Also use it when reviewing AI-powered features (chatbots, recommenders, scoring, biometrics, emotion detection, scraping, profiling) for legal/regulatory risk in the EU.
---

# AI Act Prohibited Practices Audit

Audit a target system (codebase, application, product spec, or described system) against the **prohibited AI practices** in **Article 5 of Regulation (EU) 2024/1689 (AI Act)**, as interpreted by the **European Commission Guidelines on prohibited artificial intelligence practices, C(2025) 5052 final, 29.7.2025** — converted in full as navigable Markdown references bundled with this skill.

**Output**: a structured Markdown audit report (see `assets/report-template.md`).

## Scope and limits — state these in every report

- This audit covers **only Article 5 (prohibited practices)**. The AI Act has other compliance layers that are OUT of scope here: high-risk classification and obligations (Art. 6 + Annexes I/III), transparency obligations (Art. 50 — e.g. disclosing chatbots, labelling synthetic content/deepfakes), GPAI model obligations, and AI literacy (Art. 4). If during the audit you spot likely obligations under those layers, **flag them in the "Out-of-scope observations" section** of the report — do not analyse them in depth.
- The prohibitions apply since **2 February 2025**. Penalties: up to **EUR 35 million or 7% of worldwide annual turnover** (Guidelines ¶¶ 55–57).
- The Guidelines are **non-binding**; only the CJEU can authoritatively interpret the AI Act. The report is an engineering-level compliance screening, **not legal advice** — always recommend qualified legal review for any finding that is not clearly "No issue identified".
- Never give a definitive legal verdict. Use the verdict scale defined below.

## Workflow

### Step 1 — Inventory the AI features

Identify every AI-relevant capability in the target. For a **codebase**, search for signals; for a **described system**, ask the user targeted questions about the same categories.

Signals to search for (grep/glob, adapt to stack):

- **Model/LLM integrations**: `openai`, `anthropic`, `claude`, `gpt`, `gemini`, `mistral`, `llama`, `huggingface`, `transformers`, `tensorflow`, `pytorch`, `onnx`, `ml`, `inference`, `completion`, `embedding`
- **Recommenders / personalization / engagement**: `recommend`, `personaliz`, `ranking`, `feed`, `engagement`, `retention`, `nudge`, `ab_test`, `experiment`
- **Scoring / rating of people**: `score`, `scoring`, `trust`, `rating`, `creditworth`, `risk_score`, `churn`, `segment`, `profil`
- **Biometrics / face / voice**: `face`, `facial`, `biometric`, `recognition`, `fingerprint`, `voiceprint`, `opencv`, `mediapipe`, `rekognition`, `face_api`, `dlib`
- **Emotion / sentiment about persons**: `emotion`, `sentiment`, `mood`, `affect`, `stress`, `attention`, `engagement_detect`
- **Scraping / data collection**: `scrape`, `crawler`, `selenium`, `playwright`, `beautifulsoup`, `cctv`, `rtsp`, image bulk-download logic
- **Crime/fraud prediction about individuals**: `fraud`, `predict`, `criminal`, `offence`, `recidiv`, `watchlist`
- **Vulnerable-audience targeting**: age gates, `children`, `kids`, `minor`, `elderly`, `disability`, `accessibility` combined with targeting/ads logic, socio-economic segmentation

Also review: privacy policy, ToS, data flows, third-party AI SDKs, ad-tech integrations, admin/HR tooling, analytics configs.

Record each feature as: name, what it does, data it uses, who it affects, provider-vs-deployer role of the audited organisation.

### Step 2 — Applicability screening

Read `references/00-overview-scope-exclusions.md` and check, per feature:

1. Is it an **AI system** (Art. 3(1))? Rule-based non-adaptive logic is generally out; ML/LLM-based inference is in.
2. Is there a **placing on the market / putting into service / use** in the EU (¶¶ 11–14)?
3. Which **role**: provider, deployer, or both (¶¶ 15–20)? Prohibitions bind both.
4. Do **exclusions** apply: national security/defence/military (¶¶ 22–28), R&D prior to market placement (¶¶ 30–33), personal non-professional use (¶¶ 34–35), open-source release conditions (¶ 36)?
5. Note: GPAI systems (e.g. an integrated LLM) can trigger prohibitions through their actual use even if the provider's intended purpose is neutral (¶¶ 39–41) — a deployer misusing a general-purpose chatbot is still in scope.

If a feature is out of scope, record it with the reason and stop there for that feature.

### Step 3 — Triage against the eight prohibitions

For each in-scope feature, screen with this table. If ANY trigger question is plausibly "yes", the prohibition is **triggered for deep assessment** in Step 4.

| Prohibition | Typical feature signals | Trigger question |
|---|---|---|
| **(a) Harmful manipulation/deception** — `references/01-…` | Dark patterns driven by AI, engagement-maximising recommenders, persuasive chatbots, subliminal/covert techniques, deceptive AI content | Does the system use subliminal, purposefully manipulative or deceptive techniques that could materially distort behaviour and cause significant harm? |
| **(b) Exploitation of vulnerabilities** — `references/01-…` | Targeting children, elderly, disabled, or people in a specific socio-economic situation with AI-driven persuasion/ads/pricing | Does it exploit age, disability, or a specific social/economic situation to distort behaviour with (likely) significant harm? |
| **(c) Social scoring** — `references/02-…` | Trust/user scores, cross-context data aggregation, scoring that gates access to services | Does it evaluate/classify people over time on social behaviour or personal characteristics, leading to detrimental treatment in unrelated contexts or disproportionate treatment? |
| **(d) Criminal risk prediction** — `references/03-…` | Fraud/crime-risk models about individuals, predictive policing style features | Does it assess/predict a natural person's risk of committing a criminal offence based solely on profiling or personality traits? |
| **(e) Untargeted facial scraping** — `references/04-…` | Crawlers collecting face images, building/expanding face-recognition databases from the internet or CCTV | Does it create or expand a facial recognition database via untargeted scraping? |
| **(f) Emotion recognition (work/education)** — `references/05-…` | Emotion/stress/attention inference in HR tools, workplace monitoring, e-learning proctoring | Does it infer emotions of persons in a workplace or education institution (outside medical/safety exceptions)? |
| **(g) Biometric categorisation (sensitive traits)** — `references/06-…` | Classifying people from face/voice/gait into race, political opinion, union membership, religion, sex life, sexual orientation | Does it individually categorise persons from biometric data to deduce/infer those sensitive characteristics? |
| **(h) Real-time RBI for law enforcement** — `references/07-…` | Live face recognition on public-space cameras used for/by law enforcement | Is it real-time remote biometric identification in publicly accessible spaces for law-enforcement purposes? |

Sentiment analysis on **text alone** is generally not "emotion recognition" under (f) unless based on biometric data (see ¶¶ 244–252) — but check the reference before clearing it.

### Step 4 — Deep assessment of triggered prohibitions

For each triggered prohibition, **read the full corresponding reference file** and check every **cumulative condition** it lists (each chapter has a "Main concepts and components" section enumerating them, plus an "Out of scope" section and examples). For each condition record: met / not met / uncertain, with **evidence** (file paths and line references for code, quotes for docs/UX copy) and the supporting **Guidelines paragraph numbers** (cite as `(Guidelines ¶ N)`).

A practice is only prohibited if **all** cumulative conditions are fulfilled. Uncertainty on any condition → verdict "Needs legal review", never "Prohibited".

### Step 5 — Write the report

Use `assets/report-template.md`. Verdict scale per finding:

- 🔴 **Likely prohibited practice** — all cumulative conditions plausibly met; urgent legal review + remediation required
- 🟠 **Needs legal review** — prohibition triggered, one or more conditions uncertain
- 🟡 **Attention** — currently out of the prohibition but close to the line (e.g. lawful persuasion vs manipulation, ¶¶ 127–133); document safeguards
- 🟢 **No issue identified** — prohibition not triggered or clearly out of scope
- ⚪ **Not applicable** — no relevant feature

Every non-🟢/⚪ finding must include: evidence, the failed/uncertain conditions, Guidelines paragraph citations, and concrete remediation options. Write the report in English unless the user asks otherwise. Save it as a Markdown file and present it to the user.

## Reference navigation

All files in `references/` are the full converted text of Guidelines C(2025) 5052. Bold markers `**(N)**` are the official paragraph numbers (1–433) — always cite them. Inline trailing digits (e.g. `harm.105`) are footnote references, resolved in `09-footnotes.md`.

| File | Covers | Guidelines ¶¶ |
|---|---|---|
| `00-overview-scope-exclusions.md` | AI Act risk approach, legal basis, material/personal scope, exclusions, interplay with high-risk & GPAI & other EU law, enforcement & penalties | 1–57 |
| `01-art5-1a-1b-manipulation-exploitation.md` | Art. 5(1)(a) manipulation/deception + 5(1)(b) exploitation of vulnerabilities, lawful persuasion boundary | 58–145 |
| `02-art5-1c-social-scoring.md` | Art. 5(1)(c) social scoring | 146–183 |
| `03-art5-1d-crime-risk-prediction.md` | Art. 5(1)(d) individual criminal risk assessment/prediction | 184–221 |
| `04-art5-1e-facial-image-scraping.md` | Art. 5(1)(e) untargeted scraping of facial images | 222–238 |
| `05-art5-1f-emotion-recognition.md` | Art. 5(1)(f) emotion recognition in workplace/education | 239–270 |
| `06-art5-1g-biometric-categorisation.md` | Art. 5(1)(g) biometric categorisation of sensitive traits | 271–288 |
| `07-art5-1h-rbi-law-enforcement.md` | Art. 5(1)(h) real-time RBI + Art. 5(2)–(7) safeguards, authorisations, reporting | 289–428 |
| `08-entry-into-application-review.md` | Entry into application, review of the guidelines | 429–433 |
| `09-footnotes.md` | All 244 footnotes (legal citations, case law) | — |

Read only the files relevant to the triggered prohibitions (plus `00-…`, always). Do not load everything by default.

## Rules

1. Always run Steps 1–2 even if the user asks about a single prohibition — context determines applicability.
2. Cite Guidelines paragraphs for every substantive claim in the report.
3. Be conservative: prefer "Needs legal review" over both false alarms and false clearances.
4. If the target has no AI features at all, still produce the report: inventory, "no AI system in scope" conclusion, and the standard scope/limits disclaimer.
5. If the user provides only a partial description, list the unanswered screening questions in the report under "Information gaps".
