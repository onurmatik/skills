# Gezgin — one-paste setup for agents

The user wants to connect the current agent client to Gezgin. First identify the current client,
then complete only the applicable steps below in order. Pause only when native OAuth needs the
browser. Do not create a custom OAuth client, PKCE script, API wrapper, or MCP smoke-test program.

The setup is: **install the skill → configure native MCP → authenticate → verify the connection**.

Gezgin provides public, source-backed destination research plus connected workflows for profile
context, member discovery, temporary presence, interests, follows, and Event participation. Treat the
live MCP tool catalog, schemas, metadata, and results as authoritative. Never ask the user for a
password, OAuth code, access token, refresh token, API key, or other secret.

## Step 1 — Install or update the standalone skill

Run this even when `$gezgin` is already available so the shared copy matches the current public
workflow instructions:

```bash
npx -y skills@latest add \
  https://github.com/onurmatik/skills/tree/main/skills/gezgin \
  -g -s gezgin -y --copy
```

The global install places a shared copy in the compatible agent's user-level skills directory. The
installer may skip a detected client that does not support global skills. Do not manually copy only
`SKILL.md`; the `references` and `agents` directories are part of the skill package.

## Step 2 — Configure the client's native MCP connection

The MCP server name is `gezgin`, its transport is Streamable HTTP, and its exact URL is:

```text
https://gezgin.com/mcp
```

If the current client is Codex, first use an MCP-capable Codex CLI to inspect the existing entry:

```bash
codex mcp get gezgin --json
```

If no `gezgin` entry exists, add it with:

```bash
codex mcp add gezgin \
  --url https://gezgin.com/mcp \
  --oauth-resource https://gezgin.com/mcp
```

Keep an existing entry only when its URL is exactly `https://gezgin.com/mcp`. If the name points to
a different server, stop and report the conflict instead of replacing it. If the `codex` executable
on `PATH` does not support `codex mcp`, use **Settings → MCP servers → Add server** in the ChatGPT
desktop app or Codex IDE extension, choose **Streamable HTTP**, name it `gezgin`, and enter the exact
URL above. Do not edit unrelated MCP entries.

For any other compatible client, add the same server name, transport, and URL through that client's
native MCP settings. Do not edit Codex configuration for another client and do not call the MCP URL
through raw HTTP.

## Step 3 — Complete native OAuth

In Codex, keep OAuth client registration on its default automatic selection. Gezgin advertises CIMD
support and keeps DCR available only as a compatibility fallback. Do not override the registration
method or manually create a client. Start the native OAuth flow with all Gezgin connected-workflow
scopes:

```bash
codex mcp login \
  --scopes account:read,communities:read,events:read,events:write,events:participate,presence:read,profile:read,profile:write,members:read,follows:write \
  gezgin
```

Wait for the user to finish Gezgin sign-in, email verification when required, and consent in the
browser. If the CLI does not support `codex mcp`, open **Settings → MCP servers → gezgin** and select
**Authenticate**. Restart the client only if its newly saved server or authentication control is not
visible.

In another client, use that client's native MCP authentication control. Do not substitute a custom
OAuth implementation.

## Step 4 — Verify the authenticated connection

After OAuth completes, first check whether the `gezgin` MCP tools are available in the current task.
If they are, call `get_account_capabilities`. A successful result confirms the authenticated
connection; report the returned capabilities and limits without starting another workflow or
reading profile, member, presence, interest, or event data.

Only when the tools are unavailable should you use that client's native reload or restart action,
start a new task if the client requires it, and retry `get_account_capabilities` once. Do not
prescribe a universal restart for every agent. If the tool is available but returns an
authentication error, reconnect with the client's native OAuth control instead of restarting.

Setup is complete when `get_account_capabilities` succeeds. Continue with destination research or
a connected Gezgin workflow only when the user asks for it.

If the live catalog reports a newer minimum skill-contract version, an expected Gezgin tool is
missing from an otherwise available catalog, or a retired tool returns `skill_update_required`,
repeat Step 1 through the client's native skill update flow. Re-read the updated skill, refresh the
tool catalog or open a new task when required, and retry once. Do not treat ordinary OAuth, input,
rate-limit, application, or network failures as update signals, and do not overwrite skill files
through raw HTTP.
