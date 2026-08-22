---
name: gezgin
description: Explore destinations, places, activities, derived city-and-interest community views, canonical Events, concrete EventInstances, and privacy-safe member matches with AI-first Gezgin data, then coordinate explicit profile, presence, interest, follow, and participation actions. Use when a user asks what to do, whom to meet, where to go, destination research, personalized travel planning, member discovery, city community discovery, presence, or meetup coordination.
metadata:
  skill-contract-version: "3.0.0"
---

# Gezgin

Use the tools supplied by the declared Gezgin MCP dependency to complete the user's travel or community goal.

## Keep the runtime boundary

- Treat the live MCP catalog, schemas, metadata, and results as authoritative.
- This installed package implements Gezgin Skill Contract `3.0.0` and targets Gezgin Agent Contract `3.0.0`. On the first Gezgin use in a task and after a reconnect or update, inspect the live `gezgin/minimumSkillContractVersion` metadata when the client exposes it. Update only when that minimum is newer than the installed skill-contract version; do not add timer-based probes or extra tool calls solely to check a version.
- Use the skill only for tool selection, sequencing, clarification, and presentation. Leave live data, identity, access, account entitlements, controlled-action policy, and runtime failures to MCP.
- Call `explore` directly for discovery; it works anonymously and uses only the connected facets whose scopes are available. For a later connected action or owner-state workflow, call `get_account_capabilities` before other connected tools. Let the native client establish or extend the connection. Never ask the user for credentials, construct authentication headers, or call the MCP endpoint through raw HTTP.
- Use only tools available in the current catalog. If the Gezgin catalog is present but an expected tool is missing, or a call returns `skill_update_required`, stop that workflow without guessing a replacement or retrying it. Tell the user the installed skill needs an update, use only the client's native skill or plugin update flow when available, then re-read the complete updated `SKILL.md`, refresh the tool catalog or start a new task when the client requires it, and retry once. Never overwrite skill files through raw HTTP. Do not run this recovery flow for ordinary authentication, authorization, validation, rate-limit, domain, or network errors.
- If no Gezgin catalog is present, report that the declared MCP dependency is not connected; do not misclassify a missing connection as an outdated skill.
- Call the smallest set of tools needed for the current request. Re-read state when a later step depends on current server-owned values.

## Route the request

- Route every side-effect-free “what should I do?”, “who should I meet?”, “where should I go?”, public event, activity, place, and destination-data request through `explore`. Send the current message as the request and only short, explicit, relevant prior facts as conversation context; never reconstruct the full chat.
- Treat `suggested.people`, `suggested.places`, `suggested.activities`, and `suggested.communities` as one ranked response surface. Each community is a deterministic city plus one canonical interest view, not a saved group or membership. Use `context` for source, freshness, assumption, and uncertainty disclosure. Clarification is optional: give the best available suggestions first, then ask about the returned topics only when useful.
- If `status` is `degraded`, clearly say detailed results are temporarily unavailable, present only the returned fallback ideas, and offer to retry. Never turn a refs-free idea into a claim about a live person, place, or event.
- Move to a profile, interest, follow, participation, Event, or EventInstance write only after the user explicitly chooses that outcome. Apply a selected community view through `update_profile`; preserve returned canonical refs and revisions.
- Read [destination research](references/destination-research.md) for source-backed location discovery and comparisons.
- Read [profile and community](references/profile-and-community.md) for profile context, presence, saved interests, member discovery, derived city communities, and follows.
- Read [event workflows](references/events.md) for Event/EventInstance semantics, flexible intent, scheduling, participation, and comments.
- Read every relevant reference when a request crosses domains, then compose one coherent workflow instead of repeating the same read.

## Clarify and present

- Ask a focused question only when the answer would select a different action, target, or outcome. For discovery, return the best available `explore` suggestions before any non-blocking clarification. Resolve names to server-returned references whenever possible instead of asking the user for opaque identifiers.
- Do not guess missing facts, tool results, references, availability, or freshness. State what is unknown when the tools do not resolve it.
- Preserve source attribution, freshness, and uncertainty returned by Gezgin. Distinguish tool-backed facts from recommendations or synthesis.
- Answer in the user's language unless they request another language. Lead with the useful result, then summarize any completed or still-pending connected action.
