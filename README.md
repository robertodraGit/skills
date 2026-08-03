# skills

> Agent skills by [@robertodraGit](https://github.com/robertodraGit) — install any of them with one command, in any [skills.sh](https://skills.sh)-compatible agent.

```bash
npx skills add robertodraGit/skills --skill <skill-name>
```

Works with Claude Code, Cursor, Codex, GitHub Copilot, Gemini CLI, Cline, Windsurf, Amp and every other agent supported by the [`skills` CLI](https://github.com/vercel-labs/skills).

## Skills

| Skill | What it does | Install |
| --- | --- | --- |
| [**ai-act-audit**](./ai-act-audit) | Audits a codebase, product or AI system against the **prohibited practices** of the EU AI Act (Art. 5, Reg. (EU) 2024/1689), grounded in the full text of the European Commission Guidelines C(2025) 5052. Outputs a structured, paragraph-cited compliance report. | `npx skills add robertodraGit/skills --skill ai-act-audit` |
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
│   ├── references/              # 10 files, EU Commission Guidelines (¶¶ 1–433)
│   └── assets/report-template.md
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
