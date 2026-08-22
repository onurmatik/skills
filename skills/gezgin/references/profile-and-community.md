# Profile and community

Use these workflows for personalization, profile maintenance, member discovery, social choices, and current presence. Discovery starts with `explore`; complete the connected-workflow bootstrap only before an owner-state read or action.

## Read and update profile context

1. Call `get_profile` when the user asks what Gezgin knows about them or when a later explicit action depends on current revision, presence, or saved interests.
2. Call `update_profile` once for explicitly requested profile-field, relationship, mobility, suggestion-preference, or city-presence changes.
3. Presence is part of the profile action surface: use `set_presence` or `clear_presence` items inside `update_profile`, never a separate presence tool.
4. Re-read with `get_profile` when the user needs confirmation beyond the mutation result.

Keep the primary answer separate from any optional profile-maintenance follow-up. Do not turn conversational details into a profile change on your own.

## Find members and manage follows

1. Call `explore` for member discovery. Report only its privacy-safe canonical cards and matching reasons; do not enrich them from outside sources or infer private attributes.
2. Call `set_follow_state` only after the user chooses a specific returned member and asks to change that relationship.

Do not infer that a person has a private life circumstance. Present only the person and community results the live tools return.

## Discover city community views

1. Call `explore` for every community discovery request, including “my communities.” Present `suggested.communities` alongside the other suggestion types.
2. Treat every result as a live view of exactly one canonical city and one canonical interest. Its deterministic URL, public people, counts, posts, and events come from current signals; never describe it as a saved group or membership.
3. Matching-only and sensitive interest signals may personalize ranking but never justify a person identity or exact count.
4. If the user explicitly asks to make a selected view part of their profile, call `get_account_capabilities`, then `get_profile`, and apply the missing city and interest together with one idempotent `update_profile` request using the current revision. Include that exact location and interest in `explicit_cohort`; do not mark any other profile-derived pair explicit.
5. If the city is already present, omit its update and preserve the existing relationship. If it is absent, ask which relationship applies before writing. Do not infer `currently_here`, `live`, `planning`, `curious`, or `past`.
6. Confirm the exact city and interest profile signals written and the explicitly selected cohort pair, then present the deterministic community URL. The pair remains a derived community view, not a separately stored group membership.

A city, interest, household detail, or life circumstance mentioned in natural language personalizes only the current discovery. It is not permission to update the profile. Never use private matching context to infer or describe another person. If any named tool is absent from the live catalog, stop that workflow rather than inventing an alternate name.

## Remember activity or location intent

1. Call `set_interest` only when the user asks Gezgin to remember or remove flexible intent tied to a canonical Event or location.
2. Include every explicitly known preference and availability detail rather than reducing the interest to a boolean.
3. A phrase such as “this weekend any time works” belongs here, not in a timeless EventInstance.
4. Use saved context in later exploration when authorized. Do not treat a destination or preference mentioned for the current answer as stored data.
