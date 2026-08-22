# Event workflows

Use these workflows for reusable activities and concrete social plans. Discovery always starts with `explore`; connected writes require explicit user intent.

## Keep the domain distinction

- `Event` is a canonical reusable activity, such as “Jordaan & 9 Streets walk”. It can originate from Gezgin AI, a member, curation, or imported recommendations.
- `EventInstance` is one concrete occurrence with a start time and meeting place. It inherits Event defaults for meeting place, capacity, participation policy, minimum participants, and required roles; the creator may override them.
- A location or Event `Interest` is actor-owned flexible intent with known preferences and availability. It is the correct representation when the user has no concrete start time.
- An Event may exist without an active EventInstance. Treat it as an unscheduled reusable activity, not as a provisional Event or draft.
- There is no EventDraft, forming-event, consensus, organizer privilege, launch, invitation, cancellation, or published-instance editing workflow.

## Start from “I want to do something this weekend”

1. Call `explore` and present the strongest returned Events, EventInstances, places, people, and refs-free generated ideas.
2. Ask only useful non-blocking clarification topics after giving best-effort suggestions.
3. If the user selects an existing EventInstance, call `set_event_participation` for their explicit interest, join, or leave choice.
4. If the user selects an Event but wants another concrete time or meeting place, call `create_event_instance`; creation also joins the actor.
5. If the user selects or expresses enthusiasm for a refs-free generated idea, offer to create it as a reusable Event before asking for schedule details. Explain that materializing it makes the activity easier for other interested people to discover. The selection itself is not write approval.
6. After the user explicitly asks to create or keep the reusable idea, call `create_event` even when no date, time, or meeting point is known. Stop before instance creation unless the user also wants a concrete meetup.
7. Missing schedule details block only `create_event_instance`; they never block `create_event`. After the user wants a concrete meetup, require an exact start time with timezone and an effective meeting point: either the selected Event's returned default or a name/address the user supplies. Ask for whichever fact is missing and never invent it.
8. If the selected concrete plan has no canonical Event yet, call `create_event` after explicit approval, then call `create_event_instance`. Carry a user-supplied meeting name/address into the instance override when the new Event result has no resolved default meeting place. Creation joins the actor and makes the occurrence public according to the returned visibility.
9. If intent remains flexible, call `set_interest` only when the user asks Gezgin to remember it. Include known location, activity group, child-friendly/accessibility needs, environment, intensity, and availability; describe it as saved intent, not a public post. A reusable Event and the actor's flexible Interest may coexist because they represent different things.

## Work with scheduled instances

1. Call `list_events` for the actor's participation, active interests, suggested canonical Events, and relevant upcoming instances.
2. Call `get_event` for canonical details and its currently active instances.
3. Any member may create a nearby alternative instance, including the same Event an hour later or one street away. Do not require consensus and do not block near duplicates.
4. The Event or instance initiator is only the idea source. They cannot cancel, reschedule, approve members, manage participants, or edit a public instance.
5. Each member changes only their own state with `set_event_participation`. When no one remains going, the instance is derived as inactive; it is not cancelled.
6. Call `add_event_comment` only when a participating member explicitly asks to publish the supplied comment.

Do not generate Event cover media. Preserve every returned ref, revision, time, location, aggregate count, and viewer-owned relationship. Never infer attendance from interest.
