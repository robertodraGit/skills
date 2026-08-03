# ⚖️ ai-act-audit

> Audit any app, codebase or AI system against the **prohibited AI practices** of the EU AI Act — grounded in the full text of the European Commission Guidelines, with paragraph-level citations.

```bash
npx skills add robertodraGit/skills --skill ai-act-audit
```

## Why

Since **2 February 2025** the eight prohibitions in **Article 5 of Regulation (EU) 2024/1689** are in force. Breaching them costs up to **EUR 35 million or 7% of worldwide annual turnover** — the heaviest penalty tier in the whole AI Act.

Most teams don't know whether their recommender, trust score, chatbot or HR tool crosses the line, because the answer lives in a 200-page Commission guidance document nobody reads. This skill puts that document inside your agent and makes it screen your actual code.

## What it does

Point your agent at a repository, a product spec, or just describe your system, and it will:

1. **Inventory** every AI-relevant feature (models, recommenders, scoring, biometrics, emotion inference, scraping, profiling) by grepping the codebase for stack-agnostic signals.
2. **Screen applicability** — is it an AI system under Art. 3(1)? Placed on the EU market? Are you provider, deployer, or both? Do the exclusions (national security, R&D, personal use, open source) apply?
3. **Triage** each feature against the eight prohibitions.
4. **Deep-assess** only the triggered ones, checking every **cumulative condition** against the Guidelines, with evidence (`file:line`, quotes) and citations (`Guidelines ¶ N`).
5. **Write the report** using a fixed template, with a conservative verdict scale.

## The eight prohibitions covered

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

## Verdict scale

Deliberately conservative — uncertainty never becomes a clearance, and never becomes an accusation:

- 🔴 **Likely prohibited practice** — all cumulative conditions plausibly met
- 🟠 **Needs legal review** — prohibition triggered, some conditions uncertain
- 🟡 **Attention** — outside the prohibition but close to the line
- 🟢 **No issue identified**
- ⚪ **Not applicable**

## Quick start

Once installed, just ask:

```text
Audit this codebase for EU AI Act compliance.
```

```text
Does our recommendation engine respect the AI Act? It optimises for session length
and we personalise the feed for users under 18.
```

```text
Check our HR screening tool against Article 5 prohibited practices.
```

Output: a Markdown report you can hand to legal, with an executive summary table, a feature inventory, per-prohibition findings, remediation options, and explicit information gaps.

## What's in the box

```text
ai-act-audit/
├── SKILL.md                                       # 5-step audit workflow
├── assets/
│   └── report-template.md                         # fixed report structure
└── references/                                    # Guidelines C(2025) 5052, full text
    ├── 00-overview-scope-exclusions.md            # ¶¶ 1–57
    ├── 01-art5-1a-1b-manipulation-exploitation.md # ¶¶ 58–145
    ├── 02-art5-1c-social-scoring.md               # ¶¶ 146–183
    ├── 03-art5-1d-crime-risk-prediction.md        # ¶¶ 184–221
    ├── 04-art5-1e-facial-image-scraping.md        # ¶¶ 222–238
    ├── 05-art5-1f-emotion-recognition.md          # ¶¶ 239–270
    ├── 06-art5-1g-biometric-categorisation.md     # ¶¶ 271–288
    ├── 07-art5-1h-rbi-law-enforcement.md          # ¶¶ 289–428
    ├── 08-entry-into-application-review.md        # ¶¶ 429–433
    └── 09-footnotes.md                            # all 244 footnotes
```

The agent loads `00-…` plus only the chapters actually triggered — the 424 KB of references never all hit the context window at once.

## Scope and limits

Covers **Article 5 only**. Out of scope, but flagged when spotted: high-risk classification and obligations (Art. 6 + Annexes I/III), transparency obligations (Art. 50 — chatbot disclosure, deepfake labelling), GPAI model obligations, AI literacy (Art. 4).

> ⚠️ This is an engineering-level compliance screening, **not legal advice**. The Commission Guidelines are non-binding; only the CJEU can authoritatively interpret the AI Act. Any finding other than 🟢 needs qualified legal counsel.

## Sources

- [Regulation (EU) 2024/1689 (AI Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Commission Guidelines on prohibited artificial intelligence practices, **C(2025) 5052 final**, 29.7.2025

## License

[MIT](../LICENSE) © Roberto Drago
