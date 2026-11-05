# skills

> Agent skills by [@robertodraGit](https://github.com/robertodraGit) — install any of them with one command, in any [skills.sh](https://skills.sh)-compatible agent.

```bash
npx skills add robertodraGit/skills --skill <skill-name>
```

Works with Claude Code, Cursor, Codex, GitHub Copilot, Gemini CLI, Cline, Windsurf, Amp and every other agent supported by the [`skills` CLI](https://github.com/vercel-labs/skills).

## Skills

| Skill | What it does | Install |
| --- | --- | --- |
| [**ai-act-audit**](./ai-act-audit) | Audits a codebase, product or AI system against the EU AI Act's **prohibited practices** (Art. 5) and **AI-content transparency duties** (Art. 50), grounded in the full text of the Commission Guidelines C(2025) 5052 and the Code of Practice on Transparency of AI-Generated Content. Outputs a structured, citation-backed compliance report. | `npx skills add robertodraGit/skills --skill ai-act-audit` |
| [**store-review-preflight**](./store-review-preflight) | Audits a mobile app **before** App Store / Google Play submission against the Apple App Review Guidelines, Apple build gates (privacy manifests, required-reason APIs, SDK signatures) and Google Play policies (Data safety, target API, account deletion, permissions). Outputs an evidence-backed rejection-risk report and draft reviewer notes. | `npx skills add robertodraGit/skills --skill store-review-preflight` |
| [**privacy-audit**](./privacy-audit) | Builds a data inventory from your code and SDKs, audits GDPR/ePrivacy compliance (consent, rights, deletion, vendors, transfers, children, AI), and generates the Apple App Privacy answers, `PrivacyInfo.xcprivacy`, Google Data safety answers and a privacy policy draft. | `npx skills add robertodraGit/skills --skill privacy-audit` |
| [**store-listing**](./store-listing) | Writes or audits an App Store / Google Play listing: localized metadata (Italian and English first), keyword allocation, descriptions, screenshot plan and release notes from a changelog. Claims ledger, store-limit linter (`lint-listing.py`) and changelog-to-notes helper included. | `npx skills add robertodraGit/skills --skill store-listing` |
| [**project-workshop-generator**](./project-workshop-generator) | Turns any repository into a 5-module onboarding workshop (Markdown) plus an animated Remotion slide deck. Stack-agnostic and multilingual. | `npx skills add robertodraGit/skills --skill project-workshop-generator` |

Install everything at once:

```bash
npx skills add robertodraGit/skills --skill '*'
```

## What is a skill?

A skill is a folder with a `SKILL.md` file: instructions your agent loads **only when the task matches**, plus optional `references/` (deep docs read on demand) and `assets/` (templates). No runtime, no MCP server, no API key — just context, delivered at the right moment.

The `skills` CLI copies the folder into your agent's skills directory (`.claude/skills/`, `.cursor/skills/`, …), so it works offline and travels with the project.

## Repository layout

```text
skills/
├── ai-act-audit/
│   ├── SKILL.md                 # entry point, loaded by the agent
│   ├── references/              # 12 files: Guidelines ¶¶ 1–433 + Code of Practice
│   └── assets/report-template.md
├── store-review-preflight/
│   ├── SKILL.md
│   ├── references/              # Apple 1–5 + gates, Play policies + gates, rejections, stacks
│   └── assets/                  # report, console checklist, review notes
├── privacy-audit/
│   ├── SKILL.md
│   ├── references/              # GDPR, ePrivacy, Apple/Play disclosures, SDK catalog, deletion
│   └── assets/                  # report, inventory, policy, worksheets, manifest
├── store-listing/
│   ├── SKILL.md
│   ├── references/              # field specs, keywords, copy, screenshots, release notes, IT/EN
│   ├── scripts/                 # lint-listing.py, changelog-to-notes.py
│   └── assets/                  # listing, claims ledger, keyword worksheet, plan, report
├── project-workshop-generator/
│   ├── SKILL.md
│   ├── evals/evals.json
│   └── references/remotion-template.tsx
└── docs/launch.md               # promo copy
```

Each top-level directory is one skill, discovered automatically by the CLI.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). New skills, extra language support and evals are welcome.

## License

[MIT](./LICENSE) © Roberto Drago
