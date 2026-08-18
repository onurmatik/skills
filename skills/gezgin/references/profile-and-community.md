# Profile and community

Use these workflows for personalization, profile maintenance, member discovery, social choices, and current presence. Complete the connected-workflow bootstrap from the main skill first.

## Read and update profile context

1. Call `get_my_profile_context` when the answer depends on the actor's saved context or when the user asks what Gezgin knows about them.
2. Call `set_profile_suggestion_preference` only when the user asks to change that preference.
3. For a requested profile change, call `preview_profile_update`, then call `render_profile_update` when the selectable presentation is useful.
4. Call `apply_profile_update` only for the selection supported by the current user request and live tool contract.
5. Re-read profile context when the user needs confirmation of the resulting state.

Keep the primary answer separate from any optional profile-maintenance follow-up. Do not turn conversational details into a profile change on your own.

## Find members and manage follows

1. Call `find_members` with criteria grounded in the user's request and any location references already resolved in the conversation.
2. Call `render_member_recommendations` when cards would help the user evaluate the returned members.
3. Call `set_follow_state` only when changing a specific relationship is part of the user's current goal.
4. Report only the member information returned by Gezgin. Do not enrich it from outside sources or infer private attributes.

## Manage current presence

1. Call `get_current_presence` to answer state questions or establish current state before a dependent change.
2. Call `set_current_presence` when the user is managing their current city presence and the live schema can be satisfied.
3. Call `clear_current_presence` when the user asks to remove the active presence.
4. Use the returned state in later member or event workflows. Do not treat a destination mentioned for research as stored presence.
