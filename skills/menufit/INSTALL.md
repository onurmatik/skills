# Install MenuFit

MenuFit must be installed from the anonymous public repository. If either public discovery or installation fails, stop and report the failure; do not substitute a private repository or local checkout.

```bash
npx -y skills@latest add onurmatik/skills --list
npx -y skills@latest add onurmatik/skills --skill menufit --global --copy --yes
```

Add the production MCP connection through the client's native MCP settings. In Codex:

```bash
codex mcp add menufit --url https://menu.fit/mcp
codex mcp login menufit
```

For other supported clients, add `https://menu.fit/mcp` as a Streamable HTTP MCP server and use the client's native **Authenticate** control. Complete the browser OAuth flow; do not paste or configure access tokens.

After authentication, call `get_account_capabilities` to confirm the connection and current account availability.
