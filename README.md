# Agent Skills

Public, installable agent skills for my (@onurmatik) projects.

Each published skill lives under `skills/<name>/` and includes its complete
instruction package: `SKILL.md` plus any required `agents`, `references`,
`scripts`, `assets`, or installation guidance.

## Available skills

### Gezgin

Explore destinations, places, activities, events, derived city communities,
and privacy-safe member matches, then coordinate explicit connected actions.

```bash
npx -y skills@latest add onurmatik/skills \
  -g -s gezgin -y --copy
```

The skill declares the Gezgin Streamable HTTP MCP dependency at
`https://gezgin.com/mcp`. The native agent client is responsible for creating
the connection and completing OAuth; the skill never asks users to paste
credentials or tokens.

The public one-paste setup guide is available at
[`skills/gezgin/INSTALL.md`](skills/gezgin/INSTALL.md). Projects may redirect a
stable, branded installation URL to that version-controlled document.

### MenuFit

Analyze, translate, personalize, rank, revisit, and illustrate restaurant menus
through MenuFit's native MCP connection.

```bash
npx -y skills@latest add onurmatik/skills --skill menufit --global --copy --yes
```

The package declares the canonical Streamable HTTP dependency at
`https://menu.fit/mcp`. Connect and authenticate through the agent client's
native MCP controls; see [`skills/menufit/INSTALL.md`](skills/menufit/INSTALL.md).

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
npx -y skills@latest add onurmatik/skills --list
```

CI repeats the structural validation and performs a clean local installation
for every skill.
After changes reach `main`, CI also verifies that the repository is installable
anonymously without GitHub credentials.

## Publishing policy

- Published skills must be usable without access to a private application
  repository.
- Skill packages must contain every referenced local file.
- Credentials, access tokens, private URLs, production data, and application
  secrets must never be committed here.
- Project installation URLs may redirect to instructions in this public
  repository so the published skill and its setup guide share one source.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the release checklist.
