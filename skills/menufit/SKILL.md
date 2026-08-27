---
name: menufit
description: Analyze, translate, personalize, rank, revisit, or illustrate restaurant menus with the connected MenuFit MCP service.
metadata:
  agent-contract-version: "0.1.0"
---

# MenuFit

Use MenuFit for restaurant-menu work backed by the connected `menufit` MCP catalog.

## Route the request

- For a new public menu URL, pasted menu text, image, or PDF, call `analyze_menu` with exactly that source. Ask for the missing source when the user has not provided one.
- For an existing analysis, call `get_analysis`. Supply `locale` only when the user wants an available translated view.
- Call `recommend_items` after an analysis is complete when the user asks for personalized ranking or suitable choices. The server applies the saved profile; do not read the profile merely to make ranking work.
- Call `translate_menu` only when the user asks for translation or a bilingual result and provide the requested target locale.
- Call `visualize_menu` only when the user asks for representative dish images. Select one to five unique item ids from the analysis, then use `get_visualization` when a result needs to be reopened or polled.
- Call `get_my_profile` only when saved personalization details themselves need to be shown. Call `update_my_profile` only when the user asks to replace profile information.
- Use `get_account_capabilities` when the account's current availability or connection needs to be checked. Use `get_usage_ledger` only when the user asks to see usage history.

For a multi-step request, analyze or open the menu first, wait for a completed result when necessary, then rank, translate, or visualize in the order implied by the user's goal. Do not repeat work when an existing result satisfies the request.

## Present results

- Preserve original and translated dish names as distinct fields. Preserve prices and currency exactly as returned.
- Describe generated dish images as representative illustrations, not evidence of actual appearance.
- Treat allergen uncertainty as uncertainty. Never turn incomplete evidence into a guarantee that a dish is safe; advise confirmation with the restaurant when the result calls for it.
- Relay runtime authorization, availability, and error guidance from the MCP result without inventing parallel policy.

## Connection boundary

If the `menufit` MCP catalog is unavailable, report that the native MenuFit connection is missing and direct the user to the package's `INSTALL.md`. Use only the native MCP connection flow; do not call MenuFit through raw HTTP or request access tokens.
