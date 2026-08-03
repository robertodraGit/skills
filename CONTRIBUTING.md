# Contributing

## Adding a skill

1. Create a top-level directory named after the skill (lowercase, hyphens).
2. Add a `SKILL.md` with YAML frontmatter — `name` and `description` are required:

   ```markdown
   ---
   name: my-skill
   description: What it does AND when the agent should use it — include the trigger phrases users actually type.
   ---
   ```

   The `description` is the only part loaded into context at all times: it is what makes the agent decide to open the skill. Write it for that job.

3. Keep `SKILL.md` short. Push depth into `references/` (loaded on demand) and templates into `assets/`.
4. Add a `README.md` in the skill directory, aimed at humans browsing GitHub.
5. Add a row to the table in the root [README](./README.md).

## Testing before you open a PR

```bash
npx skills add /path/to/this/repo --skill my-skill
```

Then run the skill against at least two different targets and check the agent triggers it without being told to.

## Conventions

- Skill content in English; issues and PR discussion in any language.
- If a skill has `evals/`, add a case covering your change.
- No secrets, no vendored binaries, no dependency on a specific agent.
