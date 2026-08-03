# ⚖️ ai-act-audit

> Audit any app, codebase or AI system against the EU AI Act's **prohibited practices (Art. 5)** and **AI-content transparency duties (Art. 50)** — grounded in the full text of the European Commission Guidelines and the Code of Practice, with paragraph-level citations.

```bash
npx skills add robertodraGit/skills --skill ai-act-audit
```

## Why

Two deadlines have already passed:

- **2 February 2025** — the eight prohibitions in **Article 5** of Regulation (EU) 2024/1689 apply. Penalty: up to **EUR 35 million or 7% of worldwide annual turnover**.
- **2 August 2026** — the **Article 50** transparency obligations for AI-generated content apply. Penalty: up to **EUR 15 million or 3%**.

Most teams don't know whether their recommender, trust score, chatbot or HR tool crosses the Art. 5 line, and most generative features ship with no machine-readable marking, no detection solution and no deep-fake label at all. The answers live in a 200-page Commission guidance document and a Code of Practice nobody reads.

This skill puts both documents inside your agent and makes it screen your actual code.

## What it does

Point your agent at a repository, a product spec, or just describe your system, and it runs a six-step audit:

1. **Inventory** every AI-relevant feature (models, recommenders, scoring, biometrics, emotion inference, scraping, profiling) *and* whether it generates or manipulates audio, image, video or text.
2. **Screen applicability** — is it an AI system under Art. 3(1)? Placed on the EU market? Are you provider, deployer, or both? Do the exclusions (national security, R&D, personal use, open source) apply?
3. **Triage against the eight prohibitions** (Art. 5).
4. **Transparency screening** (Art. 50) — provider marking & detection duties, deployer labelling duties.
5. **Deep-assess** only the triggered items, condition by condition and mandatory measure by mandatory measure, with evidence (`file:line`, quotes) and citations (`Guidelines ¶ 127`, `CoP S1, Measure 1.1`).
6. **Write the report** from a fixed template, with a conservative verdict scale.

## Layer 1 — the eight prohibitions (Art. 5)

| Art. 5(1) | Prohibition | Typical trigger in real products |
| --- | --- | --- |
| (a) | Harmful manipulation & deception | AI-driven dark patterns, persuasive chatbots, engagement-maximising feeds |
| (b) | Exploitation of vulnerabilities | Targeting children, elderly, disabled or a socio-economic situation |
| (c) | Social scoring | Trust/user scores, cross-context data aggregation gating access |
| (d) | Criminal risk prediction | Fraud/crime-risk models about individuals based on profiling |
| (e) | Untargeted facial scraping | Crawlers building face-recognition databases from web or CCTV |
| (f) | Emotion recognition at work/school | HR tools, workplace monitoring, e-learning proctoring |
| (g) | Biometric categorisation | Inferring race, religion, political opinion, sexual orientation |
| (h) | Real-time remote biometric identification | Live face recognition in public spaces for law enforcement |

The skill also screens image/video generation features against the **new prohibitions added by the Digital Omnibus** (Reg. (EU) 2026/1744, applicable **December 2026**): non-consensual sexual or intimate content depicting real persons, nudification / clothing-removal tools, and AI-generated CSAM.

## Layer 2 — AI-content transparency (Art. 50)

Benchmarked against the **Code of Practice on Transparency of AI-Generated Content**, distinguishing its mandatory **"will"** measures from merely encouraged ones.

**If you are a provider** of a generative AI system — Art. 50(2)+(5), CoP Section 1:

- **Marking** — multi-layered by default: digitally signed metadata **plus** imperceptible watermarking (single layer only for closed embedded products and free-form text)
- **Non-removal** — preserve incoming metadata, ban tampering in ToS, ship no circumvention tools
- **Detection** — a detection solution (spec, software or API), free of charge, accessible, zero-retention
- **Quality** — effectiveness, robustness against adversarial attacks, interoperability (watermark-detection interop due **2 Feb 2027**)

**If you are a deployer** producing deep fakes or AI-generated published text — Art. 50(4)+(5), CoP Section 2:

- **Disclosure** — EU icon ("AI GENERATED" / "AI MODIFIED") or equivalent, meeting design *and* placement specs: perceivable without user action, at first exposure, repeated for video/live/audio, WCAG/EAA accessible
- **Internal processes** — documentation, training, review and remediation of mislabelled content
- **Artistic/satirical works** — lighter regime that must not hamper enjoyment of the work
- **Editorial-control exception** for published text — verified against its actual policy elements (named responsible person, organisational measures, published contact)

### Timing (as amended by the Digital Omnibus)

| Date | What |
| --- | --- |
| 2 Feb 2025 | Art. 5 prohibitions apply |
| **2 Aug 2026** | Art. 50 transparency obligations apply |
| 2 Dec 2026 | End of the transitional window — generative systems already on the market before 2 Aug 2026 must comply with the Art. 50(2) **marking** duty (that duty only; every other Art. 50 duty had no grace period) |
| Dec 2026 | New Digital Omnibus prohibitions (non-consensual intimate content, nudification, CSAM) |
| 2 Feb 2027 | CoP deadline for watermark-detection interoperability |
| Dec 2027 / Aug 2028 | Art. 6 high-risk obligations (postponed — out of scope here) |

## Verdict scale

Deliberately conservative — uncertainty never becomes a clearance, and never becomes an accusation:

- 🔴 **Likely violation** — Art. 5: all cumulative conditions plausibly met; Art. 50: a mandatory obligation clearly unmet
- 🟠 **Needs legal review** — triggered, one or more conditions uncertain
- 🟡 **Attention** — compliant but close to the line, or relying on an exception that needs documenting
- 🟢 **No issue identified**
- ⚪ **Not applicable**

## Quick start

Once installed, just ask:

```text
Audit this codebase for EU AI Act compliance.
```

```text
We generate marketing images with a diffusion model and publish them.
Are we compliant with the Article 50 transparency obligations?
```

```text
Does our recommendation engine respect the AI Act? It optimises for session length
and we personalise the feed for users under 18.
```

```text
Check our HR screening tool against Article 5 prohibited practices.
```

Output: a Markdown report you can hand to legal, with an executive summary table, a feature inventory, per-obligation findings, remediation options, out-of-scope flags and explicit information gaps.

## What's in the box

```text
ai-act-audit/
├── SKILL.md                                       # 6-step audit workflow
├── assets/
│   └── report-template.md                         # fixed report structure
└── references/                                    # 532 KB of primary sources
    ├── 00-overview-scope-exclusions.md            # Guidelines ¶¶ 1–57
    ├── 01-art5-1a-1b-manipulation-exploitation.md # ¶¶ 58–145
    ├── 02-art5-1c-social-scoring.md               # ¶¶ 146–183
    ├── 03-art5-1d-crime-risk-prediction.md        # ¶¶ 184–221
    ├── 04-art5-1e-facial-image-scraping.md        # ¶¶ 222–238
    ├── 05-art5-1f-emotion-recognition.md          # ¶¶ 239–270
    ├── 06-art5-1g-biometric-categorisation.md     # ¶¶ 271–288
    ├── 07-art5-1h-rbi-law-enforcement.md          # ¶¶ 289–428
    ├── 08-entry-into-application-review.md        # ¶¶ 429–433
    ├── 09-footnotes.md                            # all 244 footnotes
    ├── 10-cop-transparency-s1-…-marking-detection.md  # CoP Section 1 (provider)
    └── 11-cop-transparency-s2-deployer-labelling.md   # CoP Section 2 (deployer)
```

The agent loads `00-…` plus only the chapters actually triggered — the 532 KB of references never all hit the context window at once.

## Scope and limits

Covers **Article 5** and **Article 50(2)/(4)/(5)**. Out of scope, but flagged when spotted: high-risk classification and obligations (Art. 6 + Annexes I/III), Art. 50(1) AI-interaction disclosure (chatbots), Art. 50(3) disclosure of emotion recognition / biometric categorisation, GPAI model obligations (Chapter V), AI literacy (Art. 4).

> ⚠️ This is an engineering-level compliance screening, **not legal advice**. The Commission Guidelines are non-binding and the Code of Practice is a voluntary pathway — adherence is not conclusive evidence of compliance, and other adequate means are allowed. Only the CJEU can authoritatively interpret the AI Act. Any finding other than 🟢 needs qualified legal counsel.

## Sources

- [Regulation (EU) 2024/1689 (AI Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Commission Guidelines on prohibited artificial intelligence practices, **C(2025) 5052 final**, 29.7.2025
- Code of Practice on Transparency of AI-Generated Content
- Digital Omnibus on AI, **Reg. (EU) 2026/1744**, OJ 24.7.2026

## License

[MIT](../LICENSE) © Roberto Drago
