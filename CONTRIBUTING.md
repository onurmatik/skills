# Contributing

## Skill structure

Place each public skill in `skills/<skill-name>/`. The folder name must match
the lowercase `name` in `SKILL.md` frontmatter.

Keep the entrypoint concise. Put substantial workflow-specific guidance in
`references/`, deterministic reusable helpers in `scripts/`, and UI metadata
or MCP dependencies in `agents/openai.yaml`.

## Before opening a pull request

1. Confirm that every relative link from `SKILL.md` resolves inside the skill.
2. Confirm that the package contains no private source code, credentials,
   tokens, customer data, or internal-only URLs.
3. Run structural validation:

   ```bash
   python3 scripts/validate_skills.py
   ```

4. Test installation from the local checkout:

   ```bash
   test_home="$(mktemp -d)"
   HOME="$test_home" npx -y skills@latest add "$PWD" \
     -g -a codex -s gezgin -y --copy
   ```

5. After merging, verify anonymous installation from GitHub:

   ```bash
   env -u GH_TOKEN -u GITHUB_TOKEN \
     npx -y skills@latest add onurmatik/skills \
       -g -a codex -s gezgin -y --copy
   ```

An authenticated installation is not evidence that a skill is publicly
available. The anonymous post-merge check is part of the release contract.
