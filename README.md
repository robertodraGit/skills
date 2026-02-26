# 🎓 project-workshop-generator

> A universal AI skill that transforms any codebase into a structured, 
> ready-to-deliver workshop — with Markdown output and a Remotion video deck.

## What it does

Install this skill once and any supported AI agent (Cursor, Claude Code, Codex, etc.)
will be able to analyze a repository and automatically generate:

- A **5-module workshop** (Module 0–4) tailored to the actual stack found in the repo
- A **Remotion video presentation** (`workshop-video.tsx`) with animated slides
- **Multilingual output**: defaults to the language of the user's prompt or README

## Install

```bash
npx skills add https://github.com/robertodraGit/workshop-generator --skill project-workshop-generator
```

## Quick start

Once installed, just tell your agent:

```text
Generate a 2-hour workshop for this project. Language: Italian.
```

Or for the video deck:

```text
Create a Remotion video presentation based on this project's README and package.json.
```

## Workshop structure

| Module | Title                 | Audience   | Duration |
| ------ | --------------------- | ---------- | -------- |
| 0      | Prerequisites Check   | Everyone   | 10 min   |
| 1      | Vision & Strategy     | Management | 15 min   |
| 2      | Technical Deep Dive   | Developers | 30 min   |
| 3      | Setup & Configuration | Developers | 20 min   |
| 4      | Usage & Workflow      | All users  | 15 min   |
| 5      | Labs (🟢🟡🔴)         | Developers | 30 min   |

## Supported agents

Works with any agent supported by skills.sh:
Cursor · Claude Code · Codex · GitHub Copilot · Gemini CLI · Cline · and more.

## Stack agnostic

The skill detects the stack automatically from project files:

package.json → JS / TS / Node
requirements.txt / pyproject.toml → Python
Cargo.toml → Rust
go.mod → Go
docker-compose.yml / kubernetes/ → containerized apps

**Never assumes a specific technology** unless confirmed in the repository.

## Files in this skill

```text
project-workshop-generator/
├── SKILL.md                   # Core skill instructions
├── evals/
│   └── evals.json             # 5 test cases for validation
└── references/
    └── remotion-template.tsx  # Animated Remotion slide template
```

## Contributing

PRs welcome. If you add support for a new stack or language, add a corresponding
eval in evals/evals.json before submitting.

## License

MIT