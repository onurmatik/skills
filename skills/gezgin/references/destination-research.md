# Destination research

Use these workflows for source-backed location questions and saved location choices.

## Discover and compare destinations

1. Call `get_location_research_catalog` when the requested metrics, filters, or comparison coverage are unclear.
2. Call `search_locations` to resolve user language to Gezgin locations. If multiple results plausibly match, present the candidates and ask the user to choose.
3. Call `compare_locations` after the locations and comparison dimensions are known.
4. Call `render_location_comparison` when an interactive comparison would materially improve the answer.
5. Summarize the result using the provenance and freshness returned by the tools. Do not fill gaps with remembered or external values.

Skip the catalog call when the user's requested fields already map unambiguously to the live tool schema. Skip rendering when a concise text answer is clearer.

## Work with the saved shortlist

1. Complete the connected-workflow bootstrap from the main skill.
2. Call `get_shortlist` before answering questions about saved choices or preparing a change that depends on current contents.
3. Call `update_shortlist` only when the user's goal includes changing the saved list. Build the call from the latest server result and the live input schema.
4. Report the resulting order and any unresolved request. Do not claim a location was saved until the tool result confirms it.

## Compose research with community context

Finish the location research first, then load the relevant profile or event reference. Reuse the returned location references rather than searching again unless the user changes the target.
