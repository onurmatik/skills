---
name: gezgin
description: Research and compare destinations with source-backed Gezgin data, and coordinate connected Gezgin workflows for shortlists, profile context, member discovery, follows, presence, and casual meetups. Use when a user asks for destination research, personalized travel planning, Gezgin community discovery, or meetup creation and management.
---

# Gezgin

Use the tools supplied by the declared Gezgin MCP dependency to complete the user's travel or community goal.

## Keep the runtime boundary

- Treat the live MCP catalog, schemas, metadata, and results as authoritative.
- Use the skill only for tool selection, sequencing, clarification, and presentation. Leave live data, identity, access, account entitlements, controlled-action policy, and runtime failures to MCP.
- For a connected workflow, call `get_account_capabilities` before other connected tools. Let the native client establish or extend the connection. Never ask the user for credentials, construct authentication headers, or call the MCP endpoint through raw HTTP.
- Use only tools available in the current catalog. If a named tool is unavailable, stop that workflow and explain which capability is missing without inventing a substitute.
- Call the smallest set of tools needed for the current request. Re-read state when a later step depends on current server-owned values.

## Route the request

- Read [destination research](references/destination-research.md) for location discovery, comparisons, shortlists, and comparison presentation.
- Read [profile and community](references/profile-and-community.md) for profile context, profile changes, member discovery, follows, and current presence.
- Read [event workflows](references/events.md) for public event discovery, meetup drafts, launch, invitations, participation, and organizer actions.
- Read every relevant reference when a request crosses domains, then compose one coherent workflow instead of repeating the same read.

## Clarify and present

- Ask a focused question only when the answer would select a different tool, target, or outcome. Resolve names to server-returned references whenever possible instead of asking the user for opaque identifiers.
- Do not guess missing facts, tool results, references, availability, or freshness. State what is unknown when the tools do not resolve it.
- Preserve source attribution, freshness, and uncertainty returned by Gezgin. Distinguish tool-backed facts from recommendations or synthesis.
- Answer in the user's language unless they request another language. Lead with the useful result, then summarize any completed or still-pending connected action.
