# Onur Matik Agent Skills

Public, installable agent skills for Onur Matik projects.

Each published skill lives under `skills/<name>/` and includes its complete
instruction package: `SKILL.md` plus any required `agents`, `references`,
`scripts`, or `assets` directories.

## Available skills

### Gezgin

Research and compare destinations with source-backed Gezgin data, then
coordinate connected travel and community workflows.

```bash
npx -y skills@latest add onurmatik/skills \
  -g -s gezgin -y --copy
```

The skill declares the Gezgin Streamable HTTP MCP dependency at
`https://gezgin.com/mcp`. The native agent client is responsible for creating
the connection and completing OAuth; the skill never asks users to paste
credentials or tokens.

## Repository layout

```text
skills/
  <skill-name>/
    SKILL.md
    agents/
    references/
scripts/
.github/workflows/
```

## Validation

Run the repository checks from the project root:

```bash
python3 scripts/validate_skills.py
npx -y skills@latest add "$PWD" -g -a codex -s gezgin -y --copy
```

CI repeats the structural validation and performs a clean local installation.
After changes reach `main`, CI also verifies that the repository is installable
anonymously without GitHub credentials.

## Publishing policy

- Published skills must be usable without access to a private application
  repository.
- Skill packages must contain every referenced local file.
- Credentials, access tokens, private URLs, production data, and application
  secrets must never be committed here.
- Project installation pages should serve their instructions directly and use
  this public repository as the skill source.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the release checklist.
