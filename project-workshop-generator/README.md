# 🎓 project-workshop-generator

> Turns any codebase into a structured, ready-to-deliver workshop — Markdown modules plus an animated Remotion video deck.

```bash
npx skills add robertodraGit/skills --skill project-workshop-generator
```

## What it does

Once installed, your agent can analyze a repository and generate:

- A **6-module workshop** (Module 0–5) tailored to the stack it actually finds in the repo
- A **Remotion video presentation** (`workshop-video.tsx`) with animated slides
- **Multilingual output** — defaults to the language of your prompt or the project README

## Quick start

```text
Generate a 2-hour workshop for this project. Language: Italian.
```

```text
Create a Remotion video presentation based on this project's README and package.json.
```

## Workshop structure

| Module | Title | Audience | Duration |
| --- | --- | --- | --- |
| 0 | Prerequisites Check | Everyone | 10 min |
| 1 | Vision & Strategy | Management | 15 min |
| 2 | Technical Deep Dive | Developers | 30 min |
| 3 | Setup & Configuration | Developers | 20 min |
| 4 | Usage & Workflow | All users | 15 min |
| 5 | Labs (🟢🟡🔴) | Developers | 30 min |

## Stack agnostic

Detects the stack from project files and **never assumes a technology** unless confirmed in the repo:

| Signal | Stack |
| --- | --- |
| `package.json` | JS / TS / Node |
| `requirements.txt`, `pyproject.toml` | Python |
| `Cargo.toml` | Rust |
| `go.mod` | Go |
| `docker-compose.yml`, `kubernetes/` | containerized apps |

## What's in the box

```text
project-workshop-generator/
├── SKILL.md                   # core skill instructions
├── evals/evals.json           # 5 test cases for validation
└── references/
    └── remotion-template.tsx  # animated Remotion slide template
```

## Contributing

Adding support for a new stack or language? Add a matching eval in `evals/evals.json` with the PR.

## License

[MIT](../LICENSE) © Roberto Drago
