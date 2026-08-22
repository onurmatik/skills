# Event workflows

Use these workflows for reusable activities and concrete social plans. Discovery always starts with `explore`; connected writes require explicit user intent.

## Keep the domain distinction

- `Event` is a canonical reusable activity, such as “Jordaan & 9 Streets walk”. It can originate from Gezgin AI, a member, curation, or imported recommendations. Its reusable content may include a public map with ordered named points and optional verified route geometry.
- `EventInstance` is one concrete occurrence with a start time and meeting place. It inherits Event defaults for meeting place, capacity, participation policy, minimum participants, and required roles; the creator may override them.
- A location or Event `Interest` is actor-owned flexible intent with known preferences and availability. It is the correct representation when the user has no concrete start time.
- An Event may exist without an active EventInstance. Treat it as an unscheduled reusable activity, not as a provisional Event or draft.
- There is no EventDraft, forming-event, consensus, organizer privilege, launch, invitation, cancellation, or published-instance editing workflow. `refine_event` is a narrow pre-adoption canonical-content refinement, not a general Event update or organizer tool.

## Start from “I want to do something this weekend”

1. Call `explore` and present the strongest returned Events, EventInstances, places, people, and refs-free generated ideas. Preserve each returned `next_actions` entry with its indexed activity, trigger, confirmation requirement, and schedule requirement.
2. Ask only useful non-blocking clarification topics after giving best-effort suggestions.
3. If the user selects an existing EventInstance, call `set_event_participation` for their explicit interest, join, or leave choice.
4. If the user selects an Event but wants another concrete time or meeting place, call `create_event_instance`; creation also joins the actor.
5. If the user selects or expresses enthusiasm for a refs-free generated idea and its `next_actions` entry offers `create_event`, offer to create it as a reusable Event before asking for schedule details. Explain the returned `make_activity_discoverable` reason as making the activity easier for other interested people to discover. The selection itself is not write approval.
6. After the user explicitly asks to create or keep the reusable idea, prepare a stable and distinctive canonical title plus a summary and description that each add information. Prefer “Ankara Parklar Arası Şehir İçi Bisiklet Turu” over a title dominated by unresolved ranges such as “Ankara’da 2–3 Parkı Bağlayan Kısa–Orta Mesafeli Tur”. Use only known facts, state unresolved variables in prose, and call `create_event` even when no date, time, or meeting point is known.
7. Preserve the returned `event_ref`, revision, and public identity for the rest of the dialogue. Never call `create_event` again for the same evolving idea. If later choices make reusable content more specific, explain the canonical change and obtain explicit approval, then call `refine_event` with the latest revision. A scheduling confirmation may bundle this approval when the proposed reusable copy is clear.
8. Use `refine_event` only for reusable title, summary, description, typical duration, structured attributes, or Event map data. Add named map points only from supplied, returned, or verified coordinates, and only for public reusable landmarks—not homes, private meeting points, or live locations. Preserve their order; provide `path` only when verified route geometry is available. Without it, Gezgin connects the ordered points as an explicitly approximate route. The authenticated idea source may refine repeatedly until the first EventInstance exists or another actor has an active Event interest. The slug and URL remain stable. This temporary content lease never grants cancellation, scheduling, invitation, approval, or participant-management authority.
9. Missing schedule details block only `create_event_instance`; they never block `create_event` or a reusable-content refinement. After the user wants a concrete meetup, require an exact start time with timezone and an effective meeting point: either the selected Event's returned default or a name/address the user supplies. Ask for whichever fact is missing and never invent it.
10. If the selected concrete plan has no canonical Event yet, call `create_event` after explicit approval, then call `create_event_instance`. If reusable refinement is still open and explicitly approved, call `refine_event` before instance creation because the first instance closes the window. Carry a user-supplied meeting name/address into the instance override when the new Event result has no resolved default meeting place. Creation joins the actor and makes the occurrence public according to the returned visibility.
11. After refinement closes, keep the same Event and place route- or occurrence-specific title, summary, and description in `create_event_instance` overrides. Never create a replacement canonical Event merely to capture later detail.
12. If intent remains flexible, call `set_interest` only when the user asks Gezgin to remember it. Include known location, activity group, child-friendly/accessibility needs, environment, intensity, and availability; describe it as saved intent, not a public post. A reusable Event and the actor's flexible Interest may coexist because they represent different things.

## Work with scheduled instances

1. Call `list_events` for the actor's participation, active interests, suggested canonical Events, and relevant upcoming instances.
2. Call `get_event` for canonical details and its currently active instances.
3. If the returned Event has a non-null map and the user wants to see its route or points, call `render_event_map` with the same `event_ref`. A `path_kind` of `ordered_points` is approximate; `routed` means route geometry was supplied.
4. Any member may create a nearby alternative instance, including the same Event an hour later or one street away. Do not require consensus and do not block near duplicates.
5. The Event or instance initiator is only the idea source. They cannot cancel, reschedule, approve members, manage participants, or edit a public instance.
6. Each member changes only their own state with `set_event_participation`. When no one remains going, the instance is derived as inactive; it is not cancelled.
7. Call `add_event_comment` only when a participating member explicitly asks to publish the supplied comment.

Do not generate Event cover media. Preserve every returned ref, revision, time, location, aggregate count, and viewer-owned relationship. Never infer attendance from interest.
